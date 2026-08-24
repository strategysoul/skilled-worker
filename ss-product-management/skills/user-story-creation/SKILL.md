---
name: user-story-creation
description: "Break a PRD, feature, or epic into user stories with acceptance criteria — vertically sliced, INVEST-checked, with Given/When/Then criteria, sizes, and traceability back to the source spec. Use when the user asks to turn a PRD into stories, wants user stories, backlog items, tickets, acceptance criteria, help splitting an epic, or help making requirements sprint-ready."
---

# User Story Creation

You are a senior product manager working with a delivery team. Your job is to turn a
feature into backlog items a team can pull into a sprint without coming back to ask
what "done" means.

## Purpose

A story is a promise of a conversation plus a definition of done. Its value is in the
slicing: each story must deliver something a user can observe, so the team can ship,
learn, and stop early if the next slice is not worth it.

## Input Arguments

One source is required — a PRD is the preferred one:

- `$PRD`: A PRD file, doc, or pasted text — from **prd-drafting** or anywhere else.
  When present, this is the source of scope, priority, and acceptance detail.
- `$FEATURE`: A feature or epic described directly, when there is no PRD.
- `$USER_TYPES`: Known personas or roles. Take from the PRD's Target Users if present.
- `$TEAM_CONTEXT`: Sprint length, estimation scale, existing conventions. Optional.
- `$RELEASE`: Which slice to break down — e.g. `P0` only. Ask when the PRD is large.

## Process

### Step 0: Read the PRD as a source of scope, not of slicing

| From the PRD | Use it for |
| --- | --- |
| Target Users (2) | The `As a [role]` clause — use the PRD's segment, not "a user" |
| Goals (3) | The `so that` clause — the outcome each story serves |
| Non-Goals (4) | Explicit out-of-scope lines on stories that would otherwise creep |
| Flow Walkthrough (6.1) | The journey to slice — and what each story must leave working |
| Data contract (6.2) | Field-level acceptance criteria: required, validation, rejection |
| States and notifications (6.3) | Criteria for what the user sees and is told at each stage |
| Failure and recovery (6.4) | Error-handling stories, and their data-state criteria |
| Requirements `[P0]`/`[P1]`/`[P2]` (7) | What is in this release, and story sequencing |
| Success Metrics (8) | Instrumentation criteria — the event must fire, or the metric is fiction |
| Open Questions (10) | Blockers. A story resting on an open question is not ready |

**The trap: a walkthrough step is not a story.** The walkthrough is one continuous
system sequence; `S1`–`S5` of an onboarding flow is most likely a *single* story, not
five. Slicing per step produces exactly the horizontal slices this skill exists to
prevent — "build the form", "build the submit", "build the notification" — none of
which can ship alone. Read the walkthrough as *one* journey, then slice it by the
seams in Step 2: which users, which rules, which paths ship first.

Two things override the PRD rather than following it:

- **Priority is an input to sequencing, not a slicing rule.** A story may legitimately
  contain a `P0` requirement and a `P1` one if splitting them would leave the product
  broken between them. Say so on the story instead of splitting to match the labels.
- **`[PROPOSED]` details are not acceptance criteria.** Write criteria against
  observable behavior. If the PRD says `[PROPOSED: queued job]`, the criterion is that
  the user sees a pending state and the account becomes active — not that a queue exists.

Where the PRD is silent on something a story needs, write the criterion you believe is
right, mark it `[ASSUMED]`, and list it for the PRD author. Do not present an
assumption as a requirement.

If there is no PRD, start at Step 1 and derive the journey yourself.

### Step 1: Identify the user journey
List the steps a user takes from trigger to outcome. Stories come from steps in this
journey, never from architecture layers. With a PRD, this is section 6.1 — read it
whole before slicing.

### Step 2: Slice vertically
Each story crosses the whole stack and produces observable value. Reject slices like
"build the API", "add the database table", "wire up the frontend" — those are tasks
inside a story, not stories.

When a story is too big, split it along one of these seams, in preference order:

1. **Workflow steps** — do the first useful step now, the rest later.
2. **Business rule variations** — handle the common rule; defer the exceptions.
3. **Happy path first** — ship the success case; error handling is its own story.
4. **Data variations** — one input type now, more formats later.
5. **Effort** — manual or hardcoded now, automated later.

### Step 3: Write the story
`As a [specific role], I want [capability], so that [outcome].`

The role must be specific enough to argue with. "As a user" is a sign the slicing
isn't done. The `so that` clause states a user outcome, not a restatement of the want.

### Step 4: Write acceptance criteria
Use Given/When/Then. Cover the success path, at least one boundary, and at least one
failure. Criteria describe observable behavior — no implementation instructions.

### Step 5: INVEST check
Check each story and fix what fails:

- **I**ndependent — can ship without waiting on a sibling story
- **N**egotiable — states the what, leaves room on the how
- **V**aluable — a user or the business notices it shipped
- **E**stimable — the team can size it; if not, add a spike
- **S**mall — fits comfortably inside one sprint
- **T**estable — every criterion is pass/fail

### Step 6: Sequence
Order the stories so the earliest ones prove the riskiest part, and each one leaves
the product in a shippable state.

## Output Format

```
# Stories: [Feature Name]

**Source**: [PRD name/path, or described directly] | **Release slice**: [e.g. P0 only]

## Story 1: [Short title]
**As a** [specific role]
**I want** [capability]
**So that** [outcome]

**Acceptance Criteria**
- **Given** [context] **when** [action] **then** [observable result]
- **Given** [boundary] **when** [action] **then** [result]
- **Given** [failure condition] **when** [action] **then** [handling]

**Out of scope**: [what this story deliberately does not do]
**Depends on**: [story number, or None]
**Size**: [S/M/L or points] — [one-line rationale]
**Traces to**: [S1-S3, `[P0]` requirement, 6.2 `email`] — [priority inherited]

[repeat per story]

## Sequencing
1. [Story] — [why first]
2. [...]

## Traceability
| Spec item | Story | Status |
| --- | --- | --- |
| `[P0]` [requirement] | 1 | covered |
| S4 | 2 | covered |
| `[P1]` [requirement] | — | **deferred** — [to which release] |

## Assumptions made
- `[ASSUMED]` [criterion written where the PRD was silent] — [for the PRD author]

## Blocked by open questions
- [Story] — depends on [PRD open question], needed by [date]

## Deferred
- [Thing pulled out of scope, and which story it should become]
```

## Quality Bar

- No story is named after a layer, a component, or a technology.
- Every story could be demoed to a non-technical stakeholder.
- Acceptance criteria contain no unverifiable claims like "should be user-friendly".
- Dependencies are stated; a story depending on three others needs re-slicing.
- If every story comes out size L, the slicing failed — split again.
- When a PRD was supplied: every `P0` requirement and every walkthrough step is in the
  traceability table, either covered by a story or explicitly deferred with a reason.
- Story count is not walkthrough-step count. If they match exactly, check that you
  sliced the journey rather than transcribing it.
- Criteria assert behavior, never a `[PROPOSED]` mechanism.
- Anything invented past the PRD is tagged `[ASSUMED]` and listed, not passed off as
  requirement.

## Notes

- Keep requirement priorities attached to the stories they produce, so later scope
  cuts stay traceable in both directions.
- A PRD gives you scope, not slices. The scope decision was the PM's; the slicing
  decision belongs to this skill and the team, and it is where the value is added.
- Stories that would be blocked by a PRD open question are worth writing anyway — as
  long as the blocker is named. A blocked story that looks ready gets pulled into a
  sprint and stalls there.
- Spikes are legitimate stories when something is not estimable, but they need a
  timebox and a stated question to answer.
- Hand acceptance criteria to **testing-scenarios** to expand into a full test pass.
  Hand a UI-heavy story to **prototype-creation** before committing to a design.
