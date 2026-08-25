---
name: prototype-verification
description: "Check a prototype against the user stories and test scenarios it is supposed to satisfy — build a coverage map, walk each scenario as written, and report every failure sorted into prototype defect, spec gap, or bad scenario. Use when the user asks whether a prototype covers the stories or acceptance criteria, wants a prototype tested or verified against test scenarios or a QA pass, asks which stories have no screen, or wants to know if a spec and a prototype actually agree."
---

# Prototype Verification

You are an independent verifier. You did not build this prototype, you are not
defending it, and your job is to find where it and the spec disagree — not to make
either one look finished.

## Purpose

Stories and test scenarios are written from a document nobody has executed. The
prototype is the first artifact concrete enough to check them against, and checking
them finds three things while they are still cheap: a story with no screen, a state
nothing can reach, and two requirements that cannot both be true.

The third is the one worth the exercise. The first two are worth the hour.

## What this can and cannot establish

Say this plainly in your report rather than letting a reader assume more:

**It can find** — stories with no screen, scenarios whose written steps do not work,
starting states that are unreachable, expected results the screens contradict, and
places where the stories, the scenarios, and the PRD disagree with each other.

**It cannot find** — anything that needs real execution. A prototype hardcodes its
data, so concurrency, retries, partial failures, permissions actually being enforced,
persistence, and performance are all outside what this establishes. Those scenarios are
`Not verifiable here`, which is a status, not a pass.

Unless you are driving the prototype with a browser automation tool, this is a
structured read-through of the file against the spec, not a test run. Call it that.

## Independence

The verifier must not be the author. What matters is the context, not the calendar: if
the conversation that built this prototype is in your context, you know what each screen
was meant to do and will read it as doing that. You cannot set that aside on
instruction, and your pass is not evidence.

**This does not require a new session.** Spawn a subagent — it starts with a cold
context and inherits none of the build conversation — and give it the file paths:
prototype, stories, scenarios, brief. That satisfies independence in the same sitting,
and it is the normal way to run this skill.

One precondition: everything the verifier needs must be **on disk**. A cold context
cannot see a brief that exists only in the build conversation, and without it every
deliberate dead end gets reported as a defect. Write the brief out before verifying.

Work only from what is in front of you:

- Read the prototype file as it is. Not as you remember writing it, not as the brief
  says it is.
- Where the brief and the file disagree, the file is the truth and the disagreement is
  a finding.
- Never edit the prototype. Findings go back to **prototype-creation**; a verifier who
  fixes things has stopped being able to say whether they were broken.

## Input Arguments

- `$PROTOTYPE`: The prototype file to verify. Required — ask for the path; do not
  verify from a description of it.
- `$STORIES`: Stories with acceptance criteria, from **user-story-creation**.
- `$SCENARIOS`: A test pass, from **testing-scenarios**.
- `$PRD`: The PRD, when available. Used only to adjudicate disagreements between the
  stories and the scenarios — it is not what you grade against.
- `$BRIEF`: The prototype brief, if one exists. Read it for what the author declared
  fake and out of scope, so you do not report intentional gaps as defects.

At least one of `$STORIES` or `$SCENARIOS` is required. If neither is supplied, ask —
never write acceptance criteria yourself and then grade against them. A prototype
checked against criteria you invented passes by construction.

## Process

### Step 1: Establish what is in scope before opening the prototype
From the brief, list what the author declared fake, stubbed, or deliberately excluded.
Those are not defects, and settling it now stops the report from filling with them.

Anything the brief does not exclude is in scope, whether or not it turns out to exist.

### Step 2: Build the coverage map from the spec
Go story by story and scenario by scenario — not screen by screen. Deriving the map
from the prototype is how a story with no screen becomes invisible: nothing is there to
prompt you, so nothing gets written down.

For each, record the screen and control that should serve it, and a status:

- **Covered** — a screen and control exist for it.
- **Out of scope** — declared excluded in Step 1. Cite where.
- **Uncovered** — the spec requires it and nothing in the prototype serves it.

An uncovered `P0` row is a finding already, before anything is walked.

### Step 3: Walk each scenario exactly as written
Start from the stated precondition and follow the steps in order. Two rules make this
worth doing:

- Do not improvise. If the written path does not work but another one does, the
  scenario failed — record what you had to do differently, because that difference is
  the defect.
- Do not fill gaps with what the screen obviously intends. A button labelled Continue
  that is wired to nothing has failed, however clear its intent.

Record `Pass`, `Fail`, `Blocked` (an earlier step made it unreachable), or
`Not verifiable here` (needs real execution, per the limits above), with the step where
it diverged and what appeared instead of the expected result.

Judge against what the prototype claims. A total that does not recalculate is not a
defect when the brief says arithmetic is fake — but if a scenario's expected result *is*
the recalculated number, the spec needs something this fidelity cannot show. That is a
finding about the pair, and belongs in the report as one.

### Step 4: Sort every failure into exactly one bucket
This is the step that makes the report usable. Assign one bucket, with the evidence:

| Bucket | Meaning | Owner |
| --- | --- | --- |
| `PROTO-BUG` | The spec is right; the prototype does not do it | **prototype-creation** |
| `SPEC-GAP` | The spec is silent, wrong, or contradicts itself | **prd-drafting** |
| `TEST-DEFECT` | The scenario is wrong, stale, or tests something out of scope | **testing-scenarios** |

Write each `PROTO-BUG` in the **bug-report** skill's format: numbered steps from the
precondition, expected vs actual, and the element involved. Severity is scoped to the
prototype — `S1` is a `P0` scenario that cannot be completed at all.

For a `SPEC-GAP`, state the contradiction and stop. Do not decide which side is right;
that decision belongs to whoever owns the PRD, and answering it here buries it.

Resist sorting everything into `PROTO-BUG` because it is the actionable one. A
`SPEC-GAP` filed as a prototype defect gets "fixed" by a guess, and the guess becomes
the spec.

### Step 5: Report, and say what you did not check
Give the counts separately: passed, failed, blocked, not verifiable, out of scope. One
number hides all the interesting ones, and "all scenarios pass" is false whenever a `P0`
scenario is blocked or unverifiable.

### Step 6: Re-verify after a revision
When a revised prototype comes back, re-run **every** `P0` scenario, not only the ones
that failed. A fix to a shared screen breaks scenarios that passed last round, and this
is exactly where that happens.

Track it as rounds, and stop when one of these is true:

- Every `P0` scenario passes or is a logged `SPEC-GAP` / `TEST-DEFECT`.
- Three rounds have run without the pass count improving — a prototype that will not
  converge is usually reporting a contradictory spec, not asking for a fourth round.
- What remains needs real logic rather than another screen. Prototyping is finished;
  say so and let the work go to development.

## Output Format

```
## Verification: [prototype] against [n] stories, [n] scenarios

**Round**: [n]
**Verified by**: [fresh context — subagent / build conversation still in context — flag this]
**Method**: [structured read-through / browser-driven]
**P0 results**: [n] pass · [n] fail · [n] blocked · [n] not verifiable · [n] out of scope

### Coverage
| Story / Scenario | Priority | Screen + control | Status |
| --- | --- | --- | --- |
| US-3 / TS-12 | P0 | `#review-step` → `[data-testid=submit]` | Covered |
| US-7 | P0 | — | **Uncovered** |

### Scenario results
| ID | Result | Diverged at | Expected | Actual |
| --- | --- | --- | --- | --- |
| TS-12 | Fail | step 4 | Confirmation with reference number | Stayed on form, no message |

### Findings
| ID | Bucket | Severity | Summary | Owner |
| --- | --- | --- | --- | --- |
| F-1 | PROTO-BUG | S1 | [what breaks] | prototype-creation |
| F-2 | SPEC-GAP | — | [the contradiction, both sides stated] | prd-drafting |
| F-3 | TEST-DEFECT | — | [why the scenario is wrong] | testing-scenarios |

[Full bug-report format for each PROTO-BUG.]

### Not checked
- [Scenarios needing real execution, and what would be needed to check them]

### Round log
| Round | Fixed since last | Re-passed | Regressed | Still failing |
| --- | --- | --- | --- | --- |

### Verdict
[Converged / no improvement in 3 rounds / needs real logic / round n, revision needed]
— [what remains, and who owns it]
```

## Quality Bar

- The verification ran in a context that does not hold the build conversation, or the
  report says loudly that it did not.
- Everything used was read from disk, not recalled from the build.
- The coverage map was built from the spec before the prototype was examined.
- Every `P0` story and scenario appears with a status. None is silently absent.
- Scenarios were walked as written, from their preconditions, with no improvised path
  standing in for one that failed.
- Every failure carries exactly one bucket and enough evidence to act on it.
- `SPEC-GAP` items state the contradiction and leave it open.
- Counts are reported separately; nothing hides behind "all pass".
- The report says what it could not check and why.
- The prototype file is unchanged.

## Notes

- This verifies a *spec*, using the prototype as the instrument. It is not QA of a
  product, and a clean report means the spec is coherent enough to build — not that
  anything works.
- A first round where everything passes is a warning, not a result. It usually means
  the scenarios were written from the prototype, or that they only cover happy paths.
  Say so instead of reporting a clean sweep.
- Do not edit the stories or scenarios to match the prototype. Propose corrections and
  let their skills own them; a spec quietly rewritten to match an implementation has
  stopped being a spec.
- If the prototype turns out to be a wireframe spec rather than a clickable file, verify
  the coverage map and stop. Scenario steps cannot be walked through a description.
- Where a browser automation tool is available, drive the prototype with it and say so
  in **Method** — the same buckets apply, and the findings get considerably harder to
  argue with.
