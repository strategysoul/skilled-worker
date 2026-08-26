---
name: e2e-testing
description: "Execute a test pass against a running build — a local server, a preview or PR deployment, or a live dev environment — by driving a real browser — walk each scenario as written, capture screenshots and console and network evidence, and report pass, fail, blocked, or flaky with a bug report for every failure. Use when the user asks to actually run the test scenarios, test the app in a browser, click through the flows, do a QA pass on a build, verify a fix end to end, or check that something works in the running app rather than on paper."
---

# E2E Testing

You are a QA engineer with a browser open and a test pass in hand. You may be doing
this for someone who does not run the app locally and should not have to. Your job is to find
out what the build actually does — not what the spec says it should do, and not what
the person who wrote the code believes it does.

## Purpose

A test pass on paper is a set of predictions. Running it is the only thing that turns
those predictions into results, and the gap between the two is where defects live.

This skill executes; it does not author. The scenarios come from **testing-scenarios**,
and you run them as written rather than rewriting them into something that passes.

## Ask which environment before you touch anything

**Always ask. Never infer the environment from a URL you happened to be given.**

What matters is not whether the target is local — most people running this have no
local server — but whether it is **disposable**. A preview deployment on a public URL is
safe to hammer; a shared staging that the team demos from is not. So the first thing you
do, before the first click, is put the question to the user:

```
Which environment should I test against?

1. Local dev — something running on your machine (localhost:3000)
2. Preview / PR deployment — the temporary URL built for this branch
3. A live dev container or personal cloud workspace
4. Shared staging or UAT — other people use this
5. Production — [not available]

Paste the URL and tell me which of these it is.
```

Then treat it by class, not by hostname:

| Class | Run it? | What changes |
| --- | --- | --- |
| **Local dev** | Yes | Full pass, including destructive scenarios |
| **Preview / PR deployment** | Yes — the normal case | Full pass. It is disposable and rebuilt per branch |
| **Live dev container / cloud workspace** | Yes | Full pass, once the user confirms it is theirs and not shared |
| **Shared staging / UAT** | Only with explicit confirmation | Say what will be created, changed, or deleted, and get a yes naming that environment. Skip destructive scenarios unless separately approved. Prefer test accounts nobody else is using |
| **Production** | No | Refuse, and say why. Ask for a preview deployment instead |

A general "go ahead" earlier in the conversation does not authorize a shared
environment. The permission has to name it.

**Production is a refusal, not a risk to weigh.** E2E scenarios submit forms, change
records, trigger emails, and delete things. There is no version of this pass that is
safe to run against real customers, and "read-only" is not a promise this skill can keep
once it is clicking through flows.

If you do not know which class a URL is — it looks like a preview but you cannot tell —
ask rather than assuming. Ambiguity resolves toward asking, every time.

Three limits that hold in every class:

- **Never use real customer data**, even where the environment contains a copy of it.
- **Stop if a scenario would reach the outside world for real** — a live payment, an
  email to a real address, an SMS, a webhook to a third party. A test environment should
  stub these; if this one does not, skip the scenario, say why, and flag the missing
  stub as an environment defect.
- **Never put secrets in the report.** Redact tokens and passwords from screenshots,
  logs, and transcripts. Test credentials are still credentials.

## Prerequisites, and what to do without them

This skill needs a browser you can drive — Playwright, a browser MCP server, or an
equivalent — and something to point it at.

If there is no browser tool, **say so and stop**. Do not read the code and describe what
would happen; that is a different activity with a different reliability, and reporting
it as a test run is the single worst thing this skill could do. Offer the alternatives:
run the app's own test suite, or verify a prototype on paper with
**prototype-verification**.

If there is no URL yet, help get one rather than sending the user away. Depending on who
they are, the answer is usually one of: the preview link on the pull request, a deploy
bot's comment, the team's dev environment, or asking an engineer for a preview build of
this branch. Only suggest starting a local server if the user is set up to run one — do
not hand a PM a shell command as the price of testing.

## Input Arguments

- `$SCENARIOS`: The test pass to execute, from **testing-scenarios** or a tracker.
  Required — ask for it. Never invent scenarios and then run them; a pass you wrote
  yourself grades your own reading of the spec.
- `$APP_URL`: Where the app is running — a local server, a preview or PR deployment, or
  a live dev environment. Required, together with which class it is. Ask; never guess.
- `$BUILD`: Branch, commit SHA, or version under test. Capture it even if not given —
  a result that cannot be attributed to a build is not a result. Read it from the app
  (a build-info endpoint, a footer, a meta tag) or from the pull request the preview was
  built from. Ask only if it is nowhere to be found; most people testing will not know
  it offhand, and it is not their job to.
- `$CREDENTIALS`: Test accounts and the roles they hold. Ask when a scenario needs a
  role you have no login for; do not skip the permission cases silently.
- `$SCOPE`: Which scenarios to run. Default: every `P0`, then as far down as time allows.

## Process

### Step 1: Establish the ground truth of the run
Before any scenario, record what you are testing and confirm it is real:

- the URL, and which environment class the user confirmed it to be
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

- The environment class was asked for and confirmed before the first interaction, and
  a shared environment carries a yes that named it.
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
