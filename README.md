# Skilled Worker

A plugin marketplace of structured AI workflows for knowledge workers — built for
[Claude Code](https://claude.com/claude-code) and Claude Cowork.

Generic prompting gives you text. A skill gives you a repeatable process: the same
framework, the same output shape, every time you ask.

## Plugins

| Plugin | What it covers |
| --- | --- |
| `product-management` | Discovery, strategy, requirements, prioritization, delivery |
| `job-search` | Role targeting, company research, applications, interview prep |
| `resume` | Resume review, tailoring to a job description, impact bullets |
| `ai-learning` | Study plans, concept explainers, hands-on practice workflows |

> Status: **skeleton**. The structure, manifests, and templates are in place; the
> skills themselves are still to be written.

## Skills vs. commands

Two different things, and the difference matters:

- **A skill** (`<plugin>/skills/<name>/SKILL.md`) is a reusable framework. It is
  *model-invoked* — Claude loads it on its own when the user's request matches the
  skill's `description`. That description is the entire trigger, so it must name the
  situations and phrases a real user would type.
- **A command** (`<plugin>/commands/<name>.md`) is a `/slash` workflow the user runs
  deliberately. Its job is to sequence several skills into one end-to-end deliverable.

A skill should stand alone. A command should not duplicate a skill's content — it
should point at it.

## Repository layout

```
Skilled_worker/
├── .claude-plugin/
│   └── marketplace.json          # every plugin listed here, or it doesn't install
├── product-management/
│   ├── .claude-plugin/
│   │   └── plugin.json           # name, version, description, keywords, license
│   ├── skills/
│   │   └── <skill-name>/SKILL.md
│   └── commands/
│       └── <command-name>.md
├── job-search/                # same shape
├── resume/                    # same shape
├── ai-learning/               # same shape
├── templates/                    # copy these when adding a skill or command
│   ├── SKILL.md
│   └── COMMAND.md
├── validate_plugins.py           # manifest + frontmatter checks
├── CLAUDE.md                     # conventions Claude should follow in this repo
└── CONTRIBUTING.md               # how to add a skill
```

## Adding a skill

```bash
mkdir -p resume/skills/tailor-to-job
cp templates/SKILL.md resume/skills/tailor-to-job/SKILL.md
```

Fill in the template, then validate:

```bash
python validate_plugins.py
```

The directory name and the frontmatter `name` must match — the validator enforces it.

## Installing (once published to GitHub)

Claude Code CLI:

```bash
claude plugin marketplace add <your-github-user>/Skilled_worker
```

```bash
claude plugin install resume@skilled-worker
```

Claude Cowork: **Customize → Browse Plugins → Add Marketplace from GitHub**, then
enter the same `<user>/Skilled_worker`.

To use a plugin locally before publishing, point Claude Code at this directory as a
local marketplace instead of the GitHub path.

## License

MIT — see [LICENSE](LICENSE).
