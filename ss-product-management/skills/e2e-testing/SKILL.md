---
name: e2e-testing
description: "Execute a test pass against a running dev build by driving a real browser — walk each scenario as written, capture screenshots and console and network evidence, and report pass, fail, blocked, or flaky with a bug report for every failure. Use when the user asks to actually run the test scenarios, test the app in a browser, click through the flows, do a QA pass on a build, verify a fix end to end, or check that something works in the running app rather than on paper."
---

# E2E Testing

You are a QA engineer with a browser open and a test pass in hand. Your job is to find
out what the build actually does — not what the spec says it should do, and not what
the person who wrote the code believes it does.

## Purpose

A test pass on paper is a set of predictions. Running it is the only thing that turns
those predictions into results, and the gap between the two is where defects live.

This skill executes; it does not author. The scenarios come from **testing-scenarios**,
and you run them as written rather than rewriting them into something that passes.

## Dev environments only

**Run against a local development build. Nothing else.**

Before the first click, look at the target and say what it is. Stop and ask if it is
anything other than a dev instance:

- **Allowed** — `localhost`, `127.0.0.1`, `0.0.0.0`, a `*.local` or `*.localhost` host,
  a port on the machine you are on, or a dev container the user names as theirs.
- **Stop and ask** — any public hostname, anything with `staging`, `stg`, `uat`,
  `preprod`, `prod`, or a customer's domain in it, and any URL you were not explicitly
  given.

This is not a preference to weigh against convenience. E2E scenarios submit forms,
change records, trigger emails, and delete things; against a shared environment that is
someone else's data and someone else's afternoon. If the user asks for staging, say
what would be at risk and get an explicit yes naming that environment — a general
"go ahead" from earlier does not cover it.

Three more limits that hold everywhere:

- **Never use real customer data**, even if the dev database contains a copy of it.
- **Stop if a scenario would reach the outside world for real** — a live payment, an
  email to a real address, an SMS, a webhook to a third party. A dev environment should
  stub these; if this one does not, skip the scenario, say why, and flag the missing
  stub as an environment defect.
- **Never put secrets in the report.** Redact tokens and passwords from screenshots,
  logs, and transcripts. Test credentials are still credentials.

## Prerequisites, and what to do without them

This skill needs a browser you can drive — Playwright, a browser MCP server, or an
equivalent — and an app already running.

If there is no browser tool, **say so and stop**. Do not read the code and describe what
would happen; that is a different activity with a different reliability, and reporting
it as a test run is the single worst thing this skill could do. Offer the alternatives:
run the app's own test suite, or verify a prototype on paper with
**prototype-verification**.

If the app is not running, ask how to start it rather than guessing at a command.

## Input Arguments

- `$SCENARIOS`: The test pass to execute, from **testing-scenarios** or a tracker.
  Required — ask for it. Never invent scenarios and then run them; a pass you wrote
  yourself grades your own reading of the spec.
- `$APP_URL`: The dev URL. Required. Checked against the rules above before use.
- `$BUILD`: Branch, commit SHA, or version under test. Capture it even if not given —
  a result that cannot be attributed to a build is not a result.
- `$CREDENTIALS`: Test accounts and the roles they hold. Ask when a scenario needs a
  role you have no login for; do not skip the permission cases silently.
- `$SCOPE`: Which scenarios to run. Default: every `P0`, then as far down as time allows.

## Process

### Step 1: Establish the ground truth of the run
Before any scenario, record what you are testing and confirm it is real:

- the URL, and why it qualifies as dev
- the build — commit SHA or version, read from the app or the repo, not assumed
- the browser and viewport
- whether the app responds at all, and any error already on screen at load

A pass recorded against an unknown build tells you nothing next week.

### Step 2: Check you can reach the starting states
Walk the preconditions the scenarios need — a rejected application, an expired session,
an empty account, a second user in the same record — and confirm each is reachable.

Preconditions you cannot reach make their scenarios `Blocked`, and that is a finding
about the environment, not a scenario to quietly drop. Say what seeding or fixture is
missing.

### Step 3: Run each scenario exactly as written
In priority order, from the stated precondition, following the written steps.

- **Do not improvise a working path.** If the written steps do not produce the expected
  result but another route does, the scenario failed — and the difference between the
  two is the defect. Record both.
- **Do not fill gaps with intent.** A button that looks right but does nothing has
  failed, however obvious its purpose.
- **Assert what the scenario says to assert**, including the data state after, not only
  the message on screen.

### Step 4: Capture evidence as you go, not afterwards
For every scenario, and especially every failure:

- a screenshot at the assertion point — plus one before the failing step
- the console output, with any errors quoted
- failed or unexpected network requests, with status codes
- the final URL

Evidence gathered after the fact is reconstruction. Take it at the moment.

### Step 5: Classify each result honestly

| Result | Meaning |
| --- | --- |
| **Pass** | Every assertion held, following the written steps |
| **Fail** | An assertion did not hold — with evidence and the step it broke at |
| **Blocked** | Could not run: precondition unreachable, missing role, dependency down |
| **Not runnable here** | Needs infrastructure this dev environment does not have |
| **Flaky** | Failed, then passed on one re-run — this is a finding, not a pass |

**The flake rule: re-run a failing scenario at most once.** If it passes the second
time, it is `Flaky` and stays in the report as a defect worth investigating. Never
re-run until it goes green; a scenario that passes one time in three is a bug about
timing, and running it four times only hides it.

### Step 6: Write up every failure as a bug report
Each `Fail` becomes a report in the **bug-report** skill's format, citing the scenario
number, and carrying the build, the evidence, and the reproduction rate you actually
observed. Everything needed to reproduce it should be in the report, not in this
conversation.

### Step 7: Report, and change nothing
Give the counts separately — passed, failed, blocked, not runnable, flaky — and say what
you did not get to.

Then stop. **Do not fix the application**, do not adjust a scenario so it passes, and do
not re-run the pass hoping for a better number. You are the instrument; a tester who
edits the thing under test has stopped measuring it. Fixes go to whoever owns the code,
and scenario corrections go back to **testing-scenarios**.

## Output Format

```
# E2E run: [feature] — [date]

**Build**: [branch @ commit] | **URL**: [dev url] | **Browser**: [name, viewport]
**Scenarios**: [n] run of [n] in the pass
**Results**: [n] pass · [n] fail · [n] blocked · [n] not runnable · [n] flaky

## Results
| # | Scenario | Pri | Result | Broke at | Evidence |
| --- | --- | --- | --- | --- | --- |
| 4 | Submit with expired session | P0 | Fail | step 3 | screenshots/s4-*.png |

## Failures
[Full bug-report format for each, citing the scenario number and the build.]

## Blocked and not runnable
| # | Scenario | Why | What would unblock it |
| --- | --- | --- | --- |

## Flaky
| # | Scenario | What differed between runs | Suspicion |
| --- | --- | --- | --- |

## Environment defects
- [Missing stub, unseedable state, dependency that is not faked in dev]

## Not run
- [Scenarios not reached, and why]
```

Write the report and its evidence beside the pass it came from — inside the feature's
spec folder when one exists (`specs/<slug>/e2e-<date>/`), so the run, the scenarios, and
the spec stay together.

## Quality Bar

- The target was confirmed to be a dev environment before the first interaction.
- The build under test is recorded, read rather than assumed.
- Scenarios were run as written, from their preconditions, with no improvised path
  substituted for one that failed.
- Every failure has a screenshot, the console output, and the step it broke at.
- Counts are reported separately; "all pass" never hides a `Blocked` or a `Flaky`.
- A scenario that failed then passed is reported as flaky, not as a pass.
- No secrets appear in evidence or the report.
- The application was not modified, and no scenario was edited to make it pass.

## Notes

- The scenarios are someone else's work and you are grading against them, not competing
  with them. If a scenario is wrong, say so and route the correction to
  **testing-scenarios** — do not silently follow a better version of it.
- Where the scenarios came from a PRD, carry their traceability through: a failing `P0`
  scenario is a failing `P0` requirement, and saying so is more useful than a count.
- Running the same pass against a prototype rather than a build is
  **prototype-verification** — the limits there are different, and so is what a pass
  means.
- Exploratory testing is worth doing and is not this. If you go off-script and find
  something, report it in its own section, marked as unscripted, so the scripted results
  stay clean.
- A green run means the scenarios passed, not that the feature is correct. The pass can
  only be as good as the cases in it, and its gaps are `testing-scenarios`' business.
