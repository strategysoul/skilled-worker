# Skilled Worker

A plugin marketplace of structured AI workflows for knowledge workers — built for
[Claude Code](https://claude.com/claude-code) and Claude Cowork.

Generic prompting gives you text. A skill gives you a repeatable process: the same
framework, the same output shape, every time you ask. Ask for a PRD and you get the
same nine sections, with the questions you skipped marked as skipped, every time.

**Early days — one plugin works today.** `ss-product-management` has five skills and a
command. The other three plugins are published as empty scaffolds so the structure is
visible; they install cleanly but do nothing yet. Watch or star the repo if you want
to know when they land.

## Plugins

| Plugin | What it covers | Status |
| --- | --- | --- |
| `ss-product-management` | PRDs, user stories, prototypes, test scenarios, bug reports | **5 skills, 1 command** |
| `ss-job-search` | Role targeting, company research, applications, interview prep | Planned — empty |
| `ss-resume` | Resume review, tailoring to a job description, impact bullets | Planned — empty |
| `ss-ai-learning` | Study plans, concept explainers, hands-on practice workflows | Planned — empty |

### `ss-product-management` skills

| Skill | Produces |
| --- | --- |
| `prd-drafting` | A PRD: problem, users, goals, a two-lane flow walkthrough (what the user sees / how data moves), scoped requirements, metrics, open questions |
| `user-story-creation` | Takes a PRD (or feature) and produces vertically sliced stories with Given/When/Then criteria, INVEST-checked, sequenced, and traced back to requirements |
| `prototype-creation` | Takes a PRD (or story) as context and produces a prototype brief plus a single-file clickable HTML prototype or wireframe spec |
| `testing-scenarios` | Takes a PRD (or story) and produces a prioritized test pass — happy paths, boundaries, failures, permissions, state transitions — with a traceability table |
| `bug-report` | A reproducible bug report with expected vs actual, evidence, and separate severity/priority |

They chain in that order: the PRD is the spine, and the prototype, stories, and test
pass all read it directly; the test pass feeds bug reports.

### `ss-product-management` commands

| Command | Runs |
| --- | --- |
| `/spec-feature` | The full chain — PRD, prototype, stories, test pass — stopping for review after each artifact |

## Installing

Claude Code CLI:

```bash
claude plugin marketplace add strategysoul/skilled-worker
```

```bash
claude plugin install ss-product-management@skilled-worker
```

Claude Cowork: **Customize → Browse Plugins → Add Marketplace from GitHub**, then
enter the same `strategysoul/skilled-worker`.

Working on the skills themselves? Clone the repo and add it as a local marketplace by
path instead — your edits then apply after `claude plugin marketplace update
skilled-worker`, with no push required.

## Using it

Skills load on their own when what you ask matches what they do. You don't name them:

> "Write up a PRD for letting agencies onboard sub-accounts"
> "Turn this PRD into stories"
> "How should we test this before release?"
> "Something's broken — the submit button spins forever"

The command is explicit, and runs the whole chain with a review stop after each piece:

```
/spec-feature onboarding form for new agency accounts
```

It goes problem framing → PRD → prototype → stories → test pass, writing each artifact
to `specs/<feature>/` so you can edit them independently.

### What makes these different from a prompt

The PRD skill produces a **two-lane flow walkthrough**: one numbered sequence showing
what the user sees beside what the system does with the data — payload, states,
failure handling, what is persisted. "Account creation in progress" and
`status=pending` are the same fact in two vocabularies, and a spec containing only one
of them gets the other invented later, differently.

Everything downstream reads that walkthrough. Stories slice it, tests verify it,
prototypes render it — and each one reports back what the PRD got wrong.

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
skilled-worker/
├── .claude-plugin/
│   └── marketplace.json          # every plugin listed here, or it doesn't install
├── ss-product-management/
│   ├── .claude-plugin/
│   │   └── plugin.json           # name, version, description, keywords, license
│   ├── skills/
│   │   └── <skill-name>/SKILL.md
│   └── commands/
│       └── <command-name>.md
├── ss-job-search/                # same shape
├── ss-resume/                    # same shape
├── ss-ai-learning/               # same shape
├── templates/                    # copy these when adding a skill or command
│   ├── SKILL.md
│   └── COMMAND.md
├── validate_plugins.py           # manifest + frontmatter checks
├── CLAUDE.md                     # conventions Claude should follow in this repo
└── CONTRIBUTING.md               # how to add a skill
```

## Adding a skill

```bash
mkdir -p ss-resume/skills/tailor-to-job
cp templates/SKILL.md ss-resume/skills/tailor-to-job/SKILL.md
```

Fill in the template, then validate:

```bash
python validate_plugins.py
```

The directory name and the frontmatter `name` must match — the validator enforces it.

## Contributing

Issues and pull requests are welcome — especially reports that a skill *didn't fire*
when it should have. A skill loads based on its `description` alone, so a description
that doesn't match how people actually phrase things is the most common defect here,
and it's invisible to the author.

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a skill, and
[CLAUDE.md](CLAUDE.md) for the writing conventions this repo follows.

Structure is checked in CI:

```bash
python validate_plugins.py
```

## License

MIT — see [LICENSE](LICENSE).
