---
name: prototype-creation
description: "Design and build a prototype that tests a product idea before it is built — takes a PRD, story, or rough idea as its source, picks the right fidelity, states the question it must answer, and produces a working single-file clickable HTML prototype or a wireframe spec. Use when the user asks to prototype a PRD or feature, wants a mockup, clickable demo, wireframe, or proof of concept, or wants to validate an idea cheaply before development."
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
- `$QUESTION`: What must this prototype tell you? Derive candidates from the PRD when
  one exists (see Step 0); otherwise ask. Required before building anything.
- `$AUDIENCE`: Who will see it — users in a test, an exec, the eng team. Sets fidelity.
- `$SCOPE`: Which flow or requirement to prototype, when the PRD covers several.

## Process

### Step 0: Read the PRD first (when there is one)
Pull the context out of the document rather than interviewing the user again. Map it:

| From the PRD | Use it for |
| --- | --- |
| Problem | The situation the prototype must put the participant in |
| Target Users | Who to recruit, and whose vocabulary the copy uses |
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

For a wireframe spec instead, describe each screen: purpose, elements top to bottom,
primary action, and what changes on interaction.

### Step 5: Write the test plan
State the task to give someone, what you will watch for, and what result would kill or
change the idea. Without this, the prototype degrades into a demo.

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
