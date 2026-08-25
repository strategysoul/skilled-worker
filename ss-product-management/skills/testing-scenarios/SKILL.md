---
name: testing-scenarios
description: "Generate a test pass from a PRD, user story, or acceptance criteria — happy paths, boundaries, error handling, permissions, and state-transition cases, each with steps and expected results, traced back to the source spec. Use when the user asks to test a PRD or feature, wants test cases, test scenarios, a QA checklist, edge cases, or asks how to verify something before release."
---

# Testing Scenarios

You are a QA engineer with a tester's instinct for where software breaks. Your job is
to turn a specification into a set of concrete scenarios someone can execute without
asking you what you meant.

## Purpose

Acceptance criteria describe what should happen. Testing scenarios describe what to do
to find out — including the cases the spec author did not think about, which is where
most defects live.

## Input Arguments

One source is required — a PRD is the preferred one:

- `$PRD`: A PRD file, doc, or pasted text — from **prd-drafting** or anywhere else.
  When present, this is the spec. Read all of it before writing a single scenario.
- `$SPEC`: A user story or acceptance criteria, when there is no PRD.
- `$SURFACE`: Web, mobile, API, CLI, batch job. Changes which categories apply.
- `$RISK_AREAS`: Known fragile parts, or areas with past incidents. Optional.
- `$SCOPE`: Which flow or release slice to cover, when the PRD spans several.

## Process

### Step 0: Mine the PRD (when there is one)
A PRD with a Flow Walkthrough is the richest input this skill will ever get. Most of
the test pass is already implicit in it — extract rather than invent:

| From the PRD | Produces |
| --- | --- |
| Flow Walkthrough (6.1) | The happy-path scenarios, one per step, in order |
| Data contract (6.2) | Boundary and validation cases — one per field, from its type, required flag, and rule |
| States and notifications (6.3) | What to assert at each stage, and the notification-delivery cases |
| Failure and recovery (6.4) | The error-handling section, including the "data left in" assertion |
| Persistence and retention (6.5) | Storage assertions, personal-data handling, deletion path |
| Requirements `[P0]`/`[P1]` (7) | Priority for each scenario — inherit it, do not re-invent it |
| Non-Goals (4) | What NOT to test, and what to reject as out of scope |
| Success Metrics (8) | Instrumentation checks — does the event that feeds the metric fire? |

Cite the source in every scenario (`S3`, `6.2 email`, `P0`) so coverage is traceable
in both directions: which spec claims have tests, and which tests exist for no stated
reason.

Then test the PRD itself, because a spec is a set of claims, not facts:

- **`[PROPOSED]` tags are not requirements.** Assert the behavior, never the mechanism
  a `[PROPOSED]` tag suggested. If the engineer used a different queue, the test
  should still pass.
- **The failure table is the author's intent, not verified behavior.** Each "data left
  in" claim becomes a scenario that checks it, not an assumption you build on.
- **Two lanes can disagree.** Where the user lane and system lane of a step imply
  different things, that is a defect in the spec — write it up as a gap, do not pick
  a side silently.
- **Coverage runs both ways.** A requirement with no scenario is a hole; a scenario
  tracing to nothing is either scope creep or an unwritten requirement.

If the input is a story rather than a PRD, its acceptance criteria play the role of
the walkthrough, and you will have to derive boundaries yourself — there is no data
contract to read them from.

### Step 1: Extract the testable claims
List every distinct behavior the spec promises. One claim can produce several
scenarios; a claim producing none means it was written unverifiably — flag it back.

### Step 2: Cover the happy paths
The primary success flow, plus each legitimate variation (different roles, entry
points, or valid input shapes that take a different route through the system).

### Step 3: Attack the boundaries
For every input and limit, test at the edge and just past it:

- Empty, one, many, maximum, maximum plus one
- Zero, negative, very large numbers, decimals where integers are expected
- Longest allowed string, string one character longer, whitespace only
- Earliest and latest dates, timezone boundaries, daylight-saving transitions
- Unicode, emoji, right-to-left text, characters that carry meaning in the stack

### Step 4: Force the failures
Make things go wrong on purpose: network dropped mid-action, dependency times out,
duplicate submit, session expired mid-flow, back button after submit, browser refresh,
two tabs editing the same record, action retried after a partial success.

For each: what should the user see, and what should the system have persisted?

### Step 5: Check permissions and state
Every role against every action, including the negative case — the user who should
*not* be able to do it, attempting it directly. Then walk the object's lifecycle and
test each transition, including the ones that should be rejected.

### Step 6: Prioritize
Where a PRD exists, inherit priority from the requirement the scenario traces to — a
`P0` requirement's happy path is a `P0` scenario. Decide only for scenarios with no
source, and for failure cases the PRD did not rank.

Otherwise mark each scenario `P0` (blocks release), `P1` (fix before wide rollout), or
`P2` (track it). Be honest — if everything is `P0`, the list is not usable for a release
decision.

## Output Format

```
# Test Scenarios: [Feature]

**Source**: [PRD name/path, or story] | **Surface**: [web/mobile/API]
**Coverage**: [n] scenarios — [n] P0, [n] P1, [n] P2

## Happy Path
| # | Scenario | Steps | Expected result | Traces to | Pri |
| --- | --- | --- | --- | --- | --- |
| 1 | [name] | 1. ... 2. ... | [observable result] | S1 | P0 |

## Boundaries
| # | Field / limit | Input | Expected result | Traces to | Pri |

## Error Handling
| # | Scenario | Trigger | Expected behavior | Data state after | Traces to | Pri |

## Permissions
| # | Role | Action | Expected | Traces to | Pri |

## State Transitions
| # | From | Action | To / rejection | Traces to | Pri |

## Notifications
| # | State change | Channel | Expected message | If delivery fails | Traces to | Pri |

## Traceability
| Spec item | Covered by | Status |
| --- | --- | --- |
| S1 | 1, 2 | covered |
| `[P0]` [requirement] | 4 | covered |
| 6.2 `email` | 11, 12 | covered |
| [item] | — | **not covered** — [why, or what is needed] |

## Gaps found in the spec
- [Question the spec does not answer, and the scenario that exposed it]

## Scenarios with no source
- [Scenario] — [why it is needed despite the spec not asking for it]
```

## Quality Bar

- Steps are executable by someone who did not read the spec.
- Expected results are observable — a screen state, a response code, a stored value —
  never "works correctly".
- Every error scenario states what happened to the data, not just the message shown.
- Negative permission cases are present, not only the allowed ones.
- Spec gaps are reported rather than silently resolved by assumption.
- When a PRD was supplied: every walkthrough step, every data-contract field, and
  every `P0` requirement appears in the traceability table with a covering scenario
  or an explicit reason it has none.
- Priorities are inherited from the PRD's requirement priorities, not re-decided.
- No scenario asserts a `[PROPOSED]` implementation detail — only observable behavior.
- Nothing listed under Non-Goals has been tested.

## Notes

- Do not invent requirements to make a scenario pass. Where the spec is silent, write
  the scenario and list the ambiguity under "Gaps found in the spec".
- Concurrency and retry cases are the most commonly skipped and the most expensive to
  find in production — include them even when the feature looks single-user.
- If the spec came from **user-story-creation**, map each acceptance criterion to at
  least one scenario so coverage is traceable. Defects found here become reports via
  **bug-report**, citing the scenario number.
- A PRD makes the test pass faster to write, not automatically complete. The PRD author
  wrote down the cases they thought of; your value is the ones they did not —
  concurrency, retries, partial failures, and the second user in the same record.
- Gaps found here are worth sending back through **prd-drafting** before code is
  written. A test pass is the cheapest review a PRD ever gets.
- Cheaper still, where a prototype exists: hand the finished pass to
  **prototype-verification**, which walks the scenarios against it and reports which
  ones no screen can satisfy. Expect some of what comes back to be a defect in a
  scenario rather than in the prototype — those corrections are yours to make.
