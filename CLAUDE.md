# Working in this repository

This repo is a **plugin marketplace of skills**, not an application. Almost every
change is a markdown file that instructs a model. Treat the prose as the product.

## Structure rules

- Every plugin listed in `.claude-plugin/marketplace.json` must have a matching
  directory with `.claude-plugin/plugin.json`. A plugin that isn't listed doesn't exist.
- Skills live at `<plugin>/skills/<skill-name>/SKILL.md`. The directory name and the
  frontmatter `name` must be identical and kebab-case.
- Commands live at `<plugin>/commands/<command-name>.md` and are invoked as
  `/<command-name>`.
- Start from `templates/SKILL.md` or `templates/COMMAND.md`. Don't invent a new shape.
- Run `python validate_plugins.py` before committing. It must exit clean.

## Writing rules

- **The `description` is the trigger.** Claude decides whether to load a skill from
  that one line alone. Write what the skill produces *and* when to use it, using the
  words a user would actually type. Vague descriptions mean the skill never fires.
- Write instructions to the model in the second person ("You are…", "Ask for…"),
  not as documentation about the skill.
- Prefer numbered steps with a stated output format over general advice. If the output
  shape isn't pinned down, results drift between runs.
- Say what to do when an input is missing: ask, don't fabricate.
- Keep a skill focused on one framework. If it needs two, that's two skills and a
  command that chains them.
- No filler sections. Every heading should change the output.

## Versioning

- `version` in each `plugin.json` and in `marketplace.json` follows semver.
- Bump the plugin's minor version when adding a skill or command; patch for edits.

## Scope

- Don't copy skill content from other marketplaces. Frameworks can be credited and
  referenced; text should be written here.
- Don't add runtime code or dependencies. If a skill needs a script, keep it inside
  that skill's directory and document it in its SKILL.md.
