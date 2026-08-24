---
description: Take a feature idea from problem statement to PRD, prototype, stories, and a test pass — with a checkpoint after each artifact
argument-hint: "<feature idea, problem statement, or path to notes>"
---

# /spec-feature -- Idea to Sprint-Ready Spec

Runs the product management chain end to end: a PRD, a clickable prototype of its
riskiest flow, the backlog stories sliced from it, and the test pass that verifies it.
Each artifact is reviewed before the next one is built on top of it.

## Invocation

```
/spec-feature onboarding form for new agency accounts
/spec-feature ./notes/kickoff-2026-08.md
/spec-feature [paste a rough problem statement]
```

## Why this is checkpointed

Every downstream artifact inherits the PRD's mistakes and multiplies them. A wrong
problem statement becomes eight wrong stories and forty wrong test scenarios, and the
error is far harder to see at that volume than it was in the paragraph it came from.

So: stop after each artifact, show it, and get a decision before continuing. Do not
run the whole chain silently and present four documents at the end.

## Workflow

### Step 1: Frame the problem

Apply the **prd-drafting** skill, but do not draft yet. First produce only:

- The problem, restated in your own words
- The target user and the trigger situation
- What you understand to be in scope, and what you believe is out

Show this and ask: *is this the right problem?* If the input was a solution ("build a
form"), this is where the misunderstanding surfaces — cheaply.

**Checkpoint.** Do not proceed until the framing is confirmed or corrected.

### Step 2: Draft the PRD

Apply the **prd-drafting** skill in full, including the two-lane Flow Walkthrough —
what the user sees and does alongside what the system does with the data, as one
numbered sequence with step IDs.

Give the user the file. Then say plainly:

- What you marked `[NEEDS INPUT]` and could not answer
- What you tagged `[PROPOSED]` that engineering should review
- Which open questions block the work

**Checkpoint.** Ask whether to fix the PRD or continue to the prototype.

### Step 3: Prototype the flow

Apply the **prototype-creation** skill with the PRD as input. It produces a brief and
a single self-contained HTML file exercising **one** flow — the riskiest one — not the
whole PRD.

This step runs by default. Seeing the flow before it is sliced into stories is the
cheapest correction available: a wrong screen order costs minutes here and a sprint
later. Build it from the walkthrough (6.1) and the states table (6.3) so the waiting
and in-progress states are visible, not just the happy screens.

Skip it only when one of these is true, and say which:

- The flow is a variation on something users already use, with no new interaction.
- The risk is not a design risk — it is feasibility (needs a spike) or viability
  (needs a model), and the PRD's open questions say so.
- The user asks to skip.

Never skip it silently.

**Checkpoint.** If the prototype changes the flow, return to Step 2 and revise the PRD
before slicing stories. Do not carry a known-wrong walkthrough forward.

### Step 4: Slice the stories

Apply the **user-story-creation** skill with the PRD as input.

Watch the failure mode the skill warns about: the walkthrough is one journey, not a
story each. Slice by user, rule, and path — then check the story count against the
step count and be suspicious if they match.

Report alongside the stories:

- Which `P0` requirements are covered, and which are deferred
- Anything marked `[ASSUMED]` where the PRD was silent
- Stories blocked by an open question

**Checkpoint.** Confirm the slicing and the release scope before generating tests.

### Step 5: Build the test pass

Apply the **testing-scenarios** skill with the PRD as input, and the stories for
acceptance-criteria coverage.

Then report the two-way traceability honestly: spec items with no scenario, and
scenarios that trace to nothing.

### Step 6: Close the loop

Summarize what came back from the chain that the PRD did not know at the start:

```
## Spec pack: [Feature]

| Artifact | Path | State |
| --- | --- | --- |
| PRD | [path] | [approved / needs input] |
| Prototype | [path or "skipped — reason"] | [tested / not tested] |
| Stories | [path] | [n] stories, [n] blocked |
| Test scenarios | [path] | [n] scenarios, [n] P0 |

### Send back to the PRD
- [Gap, assumption, or contradiction found downstream]

### Blocked on a decision
- [Open question] — [who decides] — [needed by]

### Ready to start
- [Stories with no blocker, in sequence]
```

## Output Files

Write each artifact to its own file so it can be reviewed, edited, and versioned:

```
specs/<feature-slug>/PRD.md
specs/<feature-slug>/prototype.html
specs/<feature-slug>/stories.md
specs/<feature-slug>/test-scenarios.md
```

Ask before writing outside the current directory, and never overwrite an existing spec
without showing what changes.

## Offer Next

- "Want me to file the open questions as tickets?"
- "Should I revise the PRD with what the stories and tests surfaced?"
- "Ready to start Story 1?"

## Notes

- The chain is resumable. If a PRD already exists, start at Step 3 or 4 with that file
  as input rather than regenerating it.
- Never regenerate an approved PRD to fix a downstream gap. Edit it, and say what
  changed — the PRD is the spine, and a silent rewrite invalidates every trace to it.
- If the user wants only one artifact, invoke that skill directly. This command is for
  the full pass, and its cost is the checkpoints.
