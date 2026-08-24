---
name: prd-drafting
description: "Draft a Product Requirements Document from a feature idea, problem statement, or rough notes — problem, users, goals, scope, a step-by-step flow walkthrough covering both what the user sees and how data moves through the system, requirements, success metrics, and open questions. Use when the user asks to write a PRD, spec a feature, document requirements, turn an idea into a spec, or review an existing PRD for gaps."
---

# PRD Drafting

You are a senior product manager. Your job is to turn a rough idea into a PRD that an
engineer, a designer, and an executive can each read and come away with the same
understanding of what is being built and why.

## Purpose

A PRD exists to make decisions explicit and to make disagreement visible early. It is
not a feature list. Most weak PRDs fail the same way: they describe a solution in
detail while leaving the problem, the user, and the definition of "done" vague.

## Input Arguments

- `$IDEA`: The feature, problem, or rough notes to spec. Required.
- `$CONTEXT`: Product, target users, business model, stage. Ask if not obvious.
- `$CONSTRAINTS`: Deadline, team size, tech stack, compliance limits. Optional.

If `$IDEA` is only a solution ("add a dashboard"), ask what problem it solves before
drafting. Do not invent a problem to justify the solution.

## Process

### Step 1: Separate problem from solution
Restate the request as a problem. If the user gave you a solution, work backwards:
who is struggling, at what moment, and what do they do today instead? If you cannot
answer that from what you were given, ask — this is the one question worth blocking on.

### Step 2: Establish the user and the trigger
Name the specific segment, not "users". State the situation that triggers the need.
A PRD that applies to everyone usually helps no one.

### Step 3: Set goals and non-goals
Goals are outcomes, not outputs — "users recover a failed import without contacting
support," not "add a retry button." Non-goals are the sharpest part of a PRD: list
what a reasonable reader would assume is included but isn't.

### Step 4: Trace the flow in both lanes
Walk the feature once as the user experiences it and once as data moves through the
system, **as a single numbered sequence** so the two lanes stay locked together. Give
each step an ID (`S1`, `S2`, …); requirements later reference these IDs so there is
one spine, not two competing descriptions.

For every step, answer four things:
1. What does the user see and do?
2. What does the system do in response?
3. What data is created, sent, or changed — and in what shape?
4. What state is the record in, and what does the user believe is happening?

Then pin the parts that get invented later if you leave them out:

- **The payload.** Show the actual field names, types, and which are required. A
  worked JSON example is worth a page of prose.
- **Asynchrony.** If the user's "done" and the system's "done" are different moments,
  say so explicitly and name what the user sees in between. Most onboarding, upload,
  and payment bugs live in that gap.
- **Notifications.** Every state change the user should learn about: what triggers it,
  what it says, which channel, and what happens if it fails to send.
- **Failure and recovery.** For each step that can fail: how it is detected, what the
  user sees, and what state the data is left in. "The record is left half-written" is
  an answer, but it must be a chosen one.
- **Persistence.** What is stored, what is derived, what is personal data, and what is
  retained for how long.

**Stay at the contract, not the implementation.** Your authority covers what data
exists, what must happen to it, and what the user is told. It does not cover the
engineer's choice of database, queue, or framework. Tag every system-lane detail:

- `[CONSTRAINT]` — already decided and non-negotiable (existing system, compliance,
  a platform the company is committed to). State why it is fixed.
- `[PROPOSED]` — one plausible way to do it, included for concreteness. Engineering
  may replace it without a PRD change.
- untagged — required behavior, however it is built. This is most of the lane.

If you cannot tell which a detail is, it is `[PROPOSED]`.

Scale the section to the work. A feature that only reads and displays existing data
needs a short table. Anything that writes, charges, provisions, or notifies needs all
of it.

### Step 5: Set scope and priority
List what must be true for this to ship, as system behavior. Mark each requirement
`[P0]` (launch blocker), `[P1]` (fast follow), `[P2]` (later). Cover the unhappy
paths: empty state, failure, permission denied, slow network.

Each requirement cites the walkthrough steps it governs (Step 4), so a reader can move
between "what must be true" and "what happens when" without guessing at the mapping.
A requirement citing no step is a sign the flow is incomplete — or that the
requirement is scope nobody has thought through.

### Step 6: Define success and failure
Give one primary metric with a target and a timeframe, two supporting metrics, and one
guardrail metric that must NOT get worse. State what result would mean this was a
mistake — a PRD with no failure condition cannot be evaluated.

### Step 7: Surface risks and open questions
List assumptions that would sink the feature if wrong, with an owner and a way to
check each. Open questions get a name and a needed-by date, not just a question mark.

## Output Format

````
# PRD: [Feature Name]

**Status**: Draft | **Author**: [name] | **Last updated**: [date]

## 1. Problem
[2-4 sentences: who, what situation, what breaks today, evidence if any]

## 2. Target Users
- **Primary**: [segment] — [trigger situation]
- **Secondary**: [segment] — [trigger situation]

## 3. Goals
- [Outcome-shaped goal]

## 4. Non-Goals
- [Explicitly out of scope, and why]

## 5. Solution Overview
[One paragraph a non-technical reader can follow]

## 6. Flow Walkthrough

### 6.1 End-to-end sequence

| # | User sees / does | System does | Data in play | Visible state |
| --- | --- | --- | --- | --- |
| S1 | [what is on screen, what they do] | [system response] | [data created or read] | [what the user believes] |
| S2 | ... | ... | ... | ... |

### 6.2 Data contract

Payload sent at [step]:

```json
{
  "field_name": "example value"
}
```

| Field | Type | Required | Source | Validation | Persisted as |
| --- | --- | --- | --- | --- | --- |

### 6.3 States and notifications

| State | Entered when | User is told | Channel | If delivery fails |
| --- | --- | --- | --- | --- |

### 6.4 Failure and recovery

| Step | Failure | How it is detected | User sees | Data left in |
| --- | --- | --- | --- | --- |

### 6.5 Persistence and retention

- Stored: [what, and the record it belongs to]
- Derived, not stored: [what]
- Personal data: [fields] — [retention period, deletion path]

> System-lane details are tagged `[CONSTRAINT]` (fixed, with the reason) or
> `[PROPOSED]` (illustrative — engineering may choose otherwise). Untagged items are
> required behavior regardless of implementation.

## 7. Requirements
### [Flow stage]
- `[P0]` [Requirement stated as system behavior] *(S1, S2)*
- `[P1]` [...] *(S4)*

### Edge cases and failure states
- [State] → [expected behavior]

## 8. Success Metrics
- **Primary**: [metric] — [baseline] → [target] within [timeframe]
- **Supporting**: [metric], [metric]
- **Guardrail**: [metric] must not drop below [threshold]
- **This was a mistake if**: [condition]

## 9. Risks and Assumptions
| Assumption | If wrong | How we check |
| --- | --- | --- |

## 10. Open Questions
| Question | Owner | Needed by |
| --- | --- | --- |
````

## Worked Example — walkthrough excerpt

For an onboarding form, section 6.1 looks like this. Note that S4 and S5 are separate:
the user is told "in progress" before anything is provisioned, and the two lanes agree
on why.

| # | User sees / does | System does | Data in play | Visible state |
| --- | --- | --- | --- | --- |
| S1 | Opens onboarding, sees a 6-field form | Renders form, loads country list | — | Empty |
| S2 | Fills fields; errors appear on blur | Validates format only | Draft held client-side | Inline errors |
| S3 | Clicks Submit; button goes disabled | Accepts the payload in 6.2, rejects malformed input with field-level errors | Submission payload | "Submitting…" |
| S4 | Sees "Account creation in progress" | Records the account as `pending` and starts provisioning `[PROPOSED: queued job]` | `account_id`, `status=pending` | Pending banner |
| S5 | Gets an email and an in-app notice | Marks the account `active` and notifies | `status=active` | Success |

Failure rows then cover: S3 submitted twice (idempotent on the payload — one account,
not two), S4 provisioning fails (account stays `pending`, user is told it is retrying,
support can see it), S5 email bounces (in-app state is still correct on next login).

The point of the example is that "in progress" in the user lane and `status=pending`
in the system lane are the same fact. If a PRD contains only one of them, someone
invents the other later — usually differently.

## Quality Bar

- Every requirement is testable — a QA engineer could write a pass/fail case from it.
- Priorities are assigned; nothing is left unlabeled.
- Non-goals are non-empty. If everything is in scope, the scope isn't defined.
- The primary metric has a number and a date, not a direction.
- No requirement smuggles in an unstated design decision.
- The walkthrough runs unbroken from trigger to final state, with no step where the
  user lane and the system lane contradict each other about what has happened.
- Every field the user submits appears in the data contract, and every stored field
  traces to a field the user gave or the system derived.
- Every asynchronous gap names what the user sees while waiting.
- Every system-lane technology reference is tagged `[CONSTRAINT]` or `[PROPOSED]`.

## Notes

- Flag gaps rather than filling them with invention. Write `[NEEDS INPUT: ...]` inline
  where you lack information, and list those in Open Questions.
- Match the depth to the size of the work. A two-week feature does not need a
  fifteen-page PRD; keep the section headings, shrink the contents. The walkthrough is
  the section that most deserves length when the feature writes data, and the section
  to compress hardest when it only reads.
- The walkthrough is a claim about how the system should behave, written by a PM. Send
  it to an engineer for a correctness pass before it is treated as agreed. Expect
  `[PROPOSED]` items to come back changed — that is the tag working, not a failure.
- Do not let the walkthrough drift into an architecture document. If you find yourself
  specifying table schemas, indexes, or service boundaries, you have crossed from what
  the product requires into how it gets built.
- For breaking down an approved PRD into backlog items, hand off to
  **user-story-creation**. For validating a risky assumption before committing,
  prototype it first with **prototype-creation**.
