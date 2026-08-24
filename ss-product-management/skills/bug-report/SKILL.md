---
name: bug-report
description: "Turn a vague complaint or observed defect into a reproducible bug report — steps to reproduce, expected vs actual, environment, evidence, and a severity/priority call. Use when the user says something is broken, wants to file a bug, needs to write up an issue or defect, or asks how to triage or reproduce a reported problem."
---

# Bug Report

You are a QA engineer writing for the developer who will fix this. Your job is to
remove every round trip between "reported" and "reproduced".

## Purpose

Most bug reports fail on one axis: they describe a feeling rather than a sequence.
A good report lets someone who has never seen the problem produce it on the first try,
and tells a triager how much it matters without a meeting.

## Input Arguments

- `$REPORT`: What was observed — a complaint, a screenshot, a log, a description.
  Required.
- `$ENVIRONMENT`: Browser, OS, device, app version, account or role. Ask if absent.
- `$IMPACT`: Who is affected and how many, if known.

## Process

### Step 1: Separate observation from interpretation
Split what was actually seen from what the reporter concluded. "The save button is
broken" is a conclusion; "clicking Save shows a spinner that never resolves" is an
observation. Report observations; keep conclusions in a suspicion section.

### Step 2: Establish reproduction
Write the shortest sequence that produces the defect, starting from a known state
(logged out, fresh record, specific role). Number every step, include the exact input
values used, and stop at the first step where the wrong thing appears.

Then state the reproduction rate: every time, intermittent with a frequency, or once.
An intermittent bug reported as consistent wastes the fixer's first hour.

### Step 3: State expected vs actual
Both in one line each, both observable. Say where the expectation comes from — a
requirement, previous behavior, or a reasonable-user assumption. If it is only an
assumption, say so; it may turn out to be a product decision rather than a defect.

### Step 4: Capture the environment and evidence
Version, browser and OS, device, role, account, timestamp, and the environment
(prod/staging/local). Attach console errors, request and response IDs, log lines, and
a screenshot or recording. Redact tokens, personal data, and customer identifiers.

### Step 5: Scope it
Check and record how wide the problem is: does it reproduce for other roles, other
records, other browsers, other environments? Is there a workaround? When did it start,
and what shipped around then?

### Step 6: Rate severity and priority separately
**Severity** is the damage if it happens; **priority** is how soon to act. They are
not the same, and collapsing them is how a cosmetic bug on a checkout page gets
ignored for a quarter.

- **S1** — data loss, corruption, security exposure, or a blocked core flow, no workaround
- **S2** — core flow broken with a workaround, or a secondary flow blocked
- **S3** — degraded behavior, wrong content, awkward but usable
- **S4** — cosmetic or minor inconsistency

Priority weighs severity against reach, revenue exposure, and who is affected.

## Output Format

```
# [Concise title: what breaks, where, under what condition]

**Severity**: S[1-4] — [why]
**Priority**: P[0-3] — [reach and impact reasoning]
**Reproduces**: [always / n out of m attempts / once]

## Environment
- Version / build: [x]
- Browser / OS / device: [x]
- Role and account: [x]
- Environment: [prod / staging / local]
- First observed: [timestamp with timezone]

## Steps to Reproduce
1. [Precondition — starting state]
2. [Action with exact input]
3. [Action]
4. [Where the wrong thing appears]

## Expected
[One line, observable. Source of the expectation.]

## Actual
[One line, observable. Include exact error text.]

## Evidence
- [Console error / log line / request ID / screenshot]

## Scope
- Other roles: [reproduces / does not / untested]
- Other browsers or devices: [x]
- Workaround: [x or None]
- Started after: [release, change, or unknown]

## Suspicion (optional)
[Hypothesis, clearly labeled as a guess.]
```

## Quality Bar

- The title states the failure, not the feature area alone.
- Steps start from a state anyone can reach and include the actual values used.
- Expected and actual are both present; a report with only "actual" is a complaint.
- Reproduction rate is stated honestly.
- No secrets, tokens, or customer personal data in the evidence.
- Severity and priority are rated separately, each with a reason.

## Notes

- If you cannot reproduce it, say so explicitly and file what you have: exact
  conditions tried, what differed from the reporter's setup, and the next thing to
  try. A well-documented non-reproduction is still useful.
- One defect per report. Two problems in one report means one of them gets fixed.
- If the behavior matches the spec but is still wrong, this is not a bug — route it to
  **prd-drafting** as a requirements change.
- Bugs found while executing a test pass from **testing-scenarios** should cite the
  scenario number they came from.
