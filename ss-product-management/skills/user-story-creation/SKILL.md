---
name: user-story-creation
description: "Break a feature, PRD, or epic into user stories with acceptance criteria — INVEST-checked, vertically sliced, with Given/When/Then criteria and estimates. Use when the user asks for user stories, backlog items, tickets, acceptance criteria, how to split an epic, or help turning requirements into sprint-ready work."
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

- `$FEATURE`: The feature, PRD, or epic to break down. Required.
- `$USER_TYPES`: Known personas or roles. Infer from the feature if not supplied.
- `$TEAM_CONTEXT`: Sprint length, estimation scale, existing conventions. Optional.

## Process

### Step 1: Identify the user journey
List the steps a user takes from trigger to outcome. Stories come from steps in this
journey, never from architecture layers.

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

[repeat per story]

## Sequencing
1. [Story] — [why first]
2. [...]

## Deferred
- [Thing pulled out of scope, and which story it should become]
```

## Quality Bar

- No story is named after a layer, a component, or a technology.
- Every story could be demoed to a non-technical stakeholder.
- Acceptance criteria contain no unverifiable claims like "should be user-friendly".
- Dependencies are stated; a story depending on three others needs re-slicing.
- If every story comes out size L, the slicing failed — split again.

## Notes

- If the input is a PRD, keep requirement priorities (`P0`/`P1`) attached to the
  stories they produce, so later scope cuts stay traceable.
- Spikes are legitimate stories when something is not estimable, but they need a
  timebox and a stated question to answer.
- Hand acceptance criteria to **testing-scenarios** to expand into a full test pass.
  Hand a UI-heavy story to **prototype-creation** before committing to a design.
