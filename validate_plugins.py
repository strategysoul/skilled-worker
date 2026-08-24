#!/usr/bin/env python3
"""Validate the Skilled Worker marketplace: manifests, skills, and commands.

Run from the repo root:  python validate_plugins.py
Exits non-zero if anything is malformed, so it can gate CI.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
KEBAB = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        err(f"{path.relative_to(ROOT)}: missing")
    except json.JSONDecodeError as exc:
        err(f"{path.relative_to(ROOT)}: invalid JSON - {exc}")
    return None


def parse_frontmatter(path: Path) -> dict[str, str] | None:
    """Minimal YAML frontmatter reader: flat `key: value` pairs only."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        err(f"{path.relative_to(ROOT)}: no YAML frontmatter (file must start with ---)")
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        err(f"{path.relative_to(ROOT)}: frontmatter is not closed with ---")
        return None
    fields: dict[str, str] = {}
    for line in parts[1].strip().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip().strip('"').strip("'")
    if not parts[2].strip():
        err(f"{path.relative_to(ROOT)}: frontmatter present but body is empty")
    return fields


def validate_skill(skill_dir: Path) -> None:
    rel = skill_dir.relative_to(ROOT)
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        err(f"{rel}: skill directory has no SKILL.md")
        return
    fm = parse_frontmatter(skill_md)
    if fm is None:
        return
    name = fm.get("name")
    description = fm.get("description")
    if not name:
        err(f"{rel}/SKILL.md: frontmatter is missing `name`")
    elif name != skill_dir.name:
        err(f"{rel}/SKILL.md: name '{name}' does not match directory '{skill_dir.name}'")
    elif not KEBAB.match(name):
        err(f"{rel}/SKILL.md: name '{name}' is not kebab-case")
    if not description:
        err(f"{rel}/SKILL.md: frontmatter is missing `description`")
    elif len(description) < 40:
        warn(f"{rel}/SKILL.md: description is short ({len(description)} chars) - "
             "the model uses it to decide when to load the skill")


def validate_command(cmd_md: Path) -> None:
    rel = cmd_md.relative_to(ROOT)
    fm = parse_frontmatter(cmd_md)
    if fm is None:
        return
    if not fm.get("description"):
        err(f"{rel}: frontmatter is missing `description`")
    if not KEBAB.match(cmd_md.stem):
        err(f"{rel}: command filename '{cmd_md.stem}' is not kebab-case")


def validate_plugin(entry: dict) -> None:
    name = entry.get("name", "<unnamed>")
    source = entry.get("source")
    for field in ("name", "description", "source"):
        if not entry.get(field):
            err(f"marketplace.json: plugin '{name}' is missing `{field}`")
    if not source:
        return
    plugin_dir = (ROOT / source).resolve()
    if not plugin_dir.is_dir():
        err(f"marketplace.json: plugin '{name}' source '{source}' does not exist")
        return

    manifest = load_json(plugin_dir / ".claude-plugin" / "plugin.json")
    if manifest is None:
        return
    if manifest.get("name") != name:
        err(f"{source}/.claude-plugin/plugin.json: name '{manifest.get('name')}' "
            f"does not match marketplace entry '{name}'")
    for field in ("version", "description"):
        if not manifest.get(field):
            err(f"{source}/.claude-plugin/plugin.json: missing `{field}`")

    skills = [d for d in (plugin_dir / "skills").glob("*") if d.is_dir()]
    commands = sorted((plugin_dir / "commands").glob("*.md"))
    for skill_dir in sorted(skills):
        validate_skill(skill_dir)
    for cmd in commands:
        validate_command(cmd)

    if not skills and not commands:
        warn(f"{name}: no skills or commands yet (skeleton)")
    print(f"  {name}: {len(skills)} skill(s), {len(commands)} command(s)")


def main() -> int:
    marketplace = load_json(MARKETPLACE)
    if marketplace is None:
        print("\n".join(errors), file=sys.stderr)
        return 1

    for field in ("name", "description", "plugins"):
        if not marketplace.get(field):
            err(f"marketplace.json: missing `{field}`")

    plugins = marketplace.get("plugins") or []
    print(f"Validating {len(plugins)} plugin(s) in '{marketplace.get('name')}':")
    for entry in plugins:
        validate_plugin(entry)

    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}", file=sys.stderr)

    if errors:
        print(f"\nFailed with {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"\nOK - {len(warnings)} warning(s), no errors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
