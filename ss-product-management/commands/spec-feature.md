---
description: Take a feature idea from problem statement to PRD, prototype, stories, and a test pass, then run the spec back through the prototype and fix what fails — with a checkpoint after each artifact
argument-hint: "<feature idea, problem statement, or path to notes>"
---

# /spec-feature -- Idea to Sprint-Ready Spec

Runs the product management chain end to end: a PRD, a clickable prototype of its
riskiest flow, the backlog stories sliced from it, and the test pass that verifies it —
then closes the loop by running the stories and scenarios back through the prototype and
fixing what fails. Each artifact is reviewed before the next one is built on top of it.

The chain is a loop, not a line. Everything from the PRD down is written from a document
nobody has executed; Step 6 executes it, and what comes back goes into the PRD.

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

**Checkpoint.** Confirm the test pass before running it against the prototype.

### Step 6: Verify the prototype against the stories and scenarios

Apply the **prototype-verification** skill with the prototype from Step 3, the stories
from Step 4, and the scenarios from Step 5.

This is the payoff for building the prototype early. The stories and scenarios were
written *from* the PRD; checking them against something concrete is the first moment
anyone finds out whether they agree with each other. Expect failures — a first round
where everything passes usually means the scenarios only cover happy paths.

**Run this in a fresh context — spawn a subagent.** By this point the conversation holds
everything Step 3 decided, and a context that knows what each screen was meant to do
reads it as doing that. A pass awarded to itself is worth nothing, which is the entire
reason this is a separate skill.

This does not mean starting a new session. Spawn a subagent, which begins with a cold
context, and pass it the **file paths** — prototype, brief, stories, scenarios — not the
conversation. Write the brief out first if it is not already a file: without it the
verifier reports every deliberate dead end as a defect.

Then loop, and keep the roles apart:

1. **prototype-verification** reports findings. It never edits the prototype.
2. **prototype-creation** fixes only the `PROTO-BUG` items and hands the file back.
3. Re-verify — every `P0` scenario, not just the ones that failed.

The verification skill holds the stopping rule. Report back after each round:

- `P0` scenarios passing, failing, blocked, not verifiable, and out of scope — as five
  numbers, not one
- `PROTO-BUG` items fixed, and anything that regressed on the way
- `SPEC-GAP` items, which are the real output of this step
- `TEST-DEFECT` items, with the correction proposed

Skip this step only when Step 3 was skipped. Say so if you do.

**Checkpoint.** Every `SPEC-GAP` is a decision the user has to make. Take them back to
Step 2 and revise the PRD — then push the change down to the stories and scenarios it
touches. Do not carry an unresolved contradiction into Step 7; that is the whole reason
this step exists.

### Step 7: Close the loop

Summarize what came back from the chain that the PRD did not know at the start:

```
## Spec pack: [Feature]

| Artifact | Path | State |
| --- | --- | --- |
| PRD | [path] | [approved / needs input] |
| Prototype | [path or "skipped — reason"] | [n]/[n] P0 scenarios passing, round [n] |
| Stories | [path] | [n] stories, [n] blocked |
| Test scenarios | [path] | [n] scenarios, [n] P0 |
| Verification report | [path] | [converged / stopped — reason] |

### Send back to the PRD
- [Gap, assumption, or contradiction found downstream — including every SPEC-GAP from
  Step 6, which is where most of them will have come from]

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
specs/<feature-slug>/prototype-brief.md
specs/<feature-slug>/stories.md
specs/<feature-slug>/test-scenarios.md
specs/<feature-slug>/verification.md
```

The brief is a file rather than a message because Step 6 reads it from a cold context:
it is what declares which gaps are deliberate, and a verifier that cannot see it reports
every intentional dead end as a defect.

Step 6 edits `prototype.html` in place across rounds rather than writing
`prototype-v2.html`; `verification.md` carries the round log, so the history is there
without a directory of near-identical files.

Ask before writing outside the current directory, and never overwrite an existing spec
without showing what changes.

## Offer Next

- "Want me to file the open questions as tickets?"
- "Should I revise the PRD with what the stories and tests surfaced?"
- "Ready to start Story 1?"

## Notes

- The chain is resumable. If a PRD already exists, start at Step 3 or 4 with that file
  as input rather than regenerating it. If a prototype, stories, and scenarios all
  already exist, start at Step 6 — verification is worth running on its own.
- Never regenerate an approved PRD to fix a downstream gap. Edit it, and say what
  changed — the PRD is the spine, and a silent rewrite invalidates every trace to it.
- If the user wants only one artifact, invoke that skill directly. This command is for
  the full pass, and its cost is the checkpoints.
