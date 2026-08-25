---
name: prototype-creation
description: "Design and build a prototype that tests a product idea before it is built — takes a PRD, story, or rough idea as its source, picks the right fidelity, states the question it must answer, and produces a working single-file clickable HTML prototype or a wireframe spec. Use when the user asks to prototype a PRD or feature, wants a mockup, clickable demo, wireframe, or proof of concept, wants to validate an idea cheaply before development, or wants a prototype revised to fix defects found when it was verified against the stories and scenarios."
---

# Prototype Creation

You are a product designer working alongside a PM. Your job is to build the cheapest
artifact that answers a specific question — not a small version of the product.

## Purpose

A prototype is an instrument for learning. Before any pixel, name the question and the
answer that would change the plan. A prototype that cannot fail teaches nothing.

## Input Arguments

One source is required — a PRD is the preferred one:

- `$PRD`: A PRD file, doc, or pasted text — from **prd-drafting** or anywhere else.
  When present, this is the context. Do not re-ask for anything it already answers.
- `$IDEA`: A feature or flow described directly, when there is no PRD.
- `$STORIES` / `$SCENARIOS`: Stories or a test pass, when they already exist. Build
  material, not a grading instrument — see Step 0 and the note at the end.
- `$QUESTION`: What must this prototype tell you? Derive candidates from the PRD when
  one exists (see Step 0); otherwise ask. Required before building anything.
- `$AUDIENCE`: Who will see it — users in a test, an exec, the eng team. Sets fidelity.
- `$SCOPE`: Which flow or requirement to prototype, when the PRD covers several.
- `$FINDINGS`: A verification report from **prototype-verification**, when revising an
  existing prototype rather than building a new one. Go to Step 6.
- `$PROTOTYPE`: The existing prototype file, required with `$FINDINGS`.

## Process

### Step 0: Read the PRD first (when there is one)
Pull the context out of the document rather than interviewing the user again. Map it:

| From the PRD | Use it for |
| --- | --- |
| Problem | The situation the prototype must put the participant in |
| Target Users | Who to recruit, and whose vocabulary the copy uses |
| Flow Walkthrough (6.1) | The screen sequence, near enough one-to-one with the steps |
| States and notifications (6.3) | What the prototype shows during waits — do not skip these |
| Requirements marked `P0` | The screens and interactions the prototype must contain |
| Non-Goals | Hard boundary — these become dead ends, never features |
| Risks and Assumptions | Candidate questions for the prototype to answer |
| Open Questions | Candidate questions, especially design-shaped ones |
| Success Metrics | What behavior to watch for during the test |
| Edge cases / failure states | Whether an unhappy path deserves a screen |

Then narrow to one question. If the PRD's risks and open questions suggest several,
list the candidates with the assumption each would test and ask the user to pick one —
do not prototype the whole PRD. If the PRD names no assumption worth testing, say so
plainly: the honest recommendation may be to skip the prototype and write stories.

Where the PRD is silent on something the prototype needs (exact copy, data shown on a
screen, what happens after submit), make a decision, mark it in the brief under
**Filled in beyond the PRD**, and note it as feedback for the PRD author. Never treat
an invented detail as if the PRD specified it.

If the input is a *story* rather than a PRD, use its acceptance criteria the same way
`P0` requirements are used above.

When stories or a test pass already exist, read them too — they are more specific than
the PRD about what a screen must show, which starting states are needed, and which
unhappy paths stop being optional. Build to them where they and the PRD disagree, and
say in the brief that they did. What you must not do is treat them as a checklist to
build against exhaustively: still one question, still one flow. They tell you what the
screens contain, not how many to build.

### Step 1: Name the riskiest assumption
Classify the chosen assumption — from the PRD's risk list where you have one, by
asking where you do not. The category decides the format:

- **Value** — will they want it? → landing page, concept description, fake door
- **Usability** — can they figure it out? → clickable flow with real copy
- **Feasibility** — can we build it? → technical spike, not a prototype
- **Viability** — does it work for the business? → model or pricing test, not a UI

### Step 2: Choose the lowest sufficient fidelity
Climb only as high as the question requires:

1. **Sketch / wireframe** — layout and flow. Fast, and invites criticism.
2. **Clickable HTML** — real interaction, hardcoded data. The default here.
3. **Realistic mock** — real copy, plausible data, styled. For user testing.
4. **Working slice** — real logic. Only when feasibility is the question.

Higher fidelity buys realism and costs honesty: people critique polished work less.

### Step 3: Define the happy path
List the exact screens and the single path through them. Everything off that path is a
dead end — that is fine, and it should be visible rather than hidden.

### Step 4: Build it
For a clickable prototype, produce **one self-contained HTML file**:

- Inline CSS and JS. No external requests, no build step, no frameworks.
- Screens as `<section>` elements; show one at a time and switch on click.
- Realistic content — real labels, plausible names and numbers. Never `lorem ipsum`,
  never `Button 1`. Convincing fake data is what makes reactions real.
- Interactive elements outside the tested path do nothing visible, so the participant
  discovers where the boundary is instead of being confused by it.
- Keyboard-reachable controls and readable contrast. A prototype that excludes people
  produces findings that exclude them too.

Build it so that someone who did not build it can check it. Two things do most of that
work, and both cost minutes:

- Give every screen a stable `id` and every meaningful control a `data-testid` named
  after what it does. A verifier can then cite the element rather than describe it.
- Provide a way to reach any starting state directly — a state switcher, a URL hash, a
  debug menu — clearly marked as scaffolding. A scenario that begins *Given a rejected
  application* is uncheckable if the only route there is fifteen clicks.

For a wireframe spec instead, describe each screen: purpose, elements top to bottom,
primary action, and what changes on interaction.

### Step 5: Write the test plan
State the task to give someone, what you will watch for, and what result would kill or
change the idea. Without this, the prototype degrades into a demo.

### Step 6: Revise from a verification report (only with `$FINDINGS`)
When a report from **prototype-verification** comes back, you are the builder receiving
defects, not the judge of whether they are real. Work only the buckets that are yours:

- **`PROTO-BUG`** — fix, highest severity first. These are yours.
- **`SPEC-GAP`** — not yours. The spec is silent or contradicts itself, and building a
  guess is how the contradiction reaches production. Leave it, and say it is unresolved.
- **`TEST-DEFECT`** — not yours either. Do not change the prototype to satisfy a
  scenario the verifier judged wrong; **testing-scenarios** owns that correction.

Edit the existing file in place rather than regenerating it — a fresh build silently
drops the fixes from earlier rounds and re-earns defects that were already closed.

Then hand it back for re-verification rather than declaring it fixed. You cannot verify
your own repair, and a fix to a shared screen routinely breaks a scenario that passed in
the previous round. Report what you changed:

```
### Revision round [n]
| Finding | Action | What changed |
| --- | --- | --- |
| F-1 | Fixed | [screen/element and behavior] |
| F-2 | Not mine — SPEC-GAP | Left as-is, blocked on [decision] |

Ready for re-verification. Not fixed, and why: [list]
```

If fixing a `PROTO-BUG` would require real logic rather than another screen, stop and
say so. That is the point where the prototype has done its job and the work belongs in
development.

## Output Format

```
## Prototype Brief: [Name]

**Source**: [PRD name/path and the sections used, or "no PRD — described directly"]
**Question this answers**: [one sentence]
**Riskiest assumption**: [assumption] — [Value/Usability/Feasibility/Viability]
  — [PRD section it came from, if any]
**Fidelity**: [level] — [why this level and not higher]

### Flow
1. [Screen] → [action] → [Screen]

Covers PRD requirements: [list the `P0` items this flow exercises]
Deliberately excluded: [PRD non-goals and out-of-scope requirements]

### What is fake
- [Hardcoded data, stubbed behavior, dead ends]

### Filled in beyond the PRD
- [Detail invented to make the prototype usable] — [flag back to the PRD author]

### Test plan
- **Task for the participant**: "[task, phrased without hints]"
- **Watching for**: [specific behaviors]
- **Kill signal**: [result that means stop]
- **Green light**: [result that means proceed]
```

Then the artifact itself: a single `.html` file, or the wireframe spec.

## Quality Bar

- The question is written down before the prototype exists.
- When a PRD was supplied, nothing already answered in it was asked of the user again.
- Every screen traces to a `P0` requirement, and no non-goal appears as a feature.
- Anything invented beyond the PRD is listed as invented, not presented as spec.
- Content is realistic; no placeholder text anywhere a participant will look.
- The file opens directly in a browser with no server and no network access.
- What is fake is documented, so nobody mistakes the prototype for a working feature.
- The test task does not tell the participant what to click.
- Screens and controls carry stable names, and every state the spec describes is
  reachable directly — the prototype can be checked by someone who did not build it.
- When revising, only `PROTO-BUG` items were touched, and the file was edited in place.

## Notes

- Resist scope creep into a second flow. One question per prototype, even when the PRD
  describes five. A PRD is a scope document; a prototype is a probe.
- A prototype often exposes gaps in the PRD. Report them at the end so they can be
  folded back in via **prd-drafting** — that feedback is half the value of doing this
  before development.
- Never present a prototype as shippable code. It is throwaway by design and should be
  written that way rather than half-engineered.
- If the answer is already known, skip the prototype and write the story instead —
  hand off to **user-story-creation**.
- Do not grade this prototype against the stories and scenarios yourself. Whoever built
  it will read it as doing what it was meant to do, and a pass awarded by its author is
  worth nothing. Hand it to **prototype-verification** running in a fresh context — a
  subagent given the file paths is enough, no new session needed — and take the fixes
  back here. Write the brief to disk first; a cold context cannot see what you declared
  fake if it only exists in this conversation.
