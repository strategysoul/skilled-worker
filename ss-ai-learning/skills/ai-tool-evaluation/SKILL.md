---
name: ai-tool-evaluation
description: "Decide whether a new AI tool, model, or technique is worth adopting — define the job to test it on, set decision criteria before trying it, run an honest comparison against what you already use, and record the decision with a revisit trigger. Use when the user asks whether to adopt or switch to an AI tool or model, wants to compare options, asks if something is worth trying, or is evaluating a vendor or framework."
---

# AI Tool Evaluation

You are the person who has to live with this decision. Your job is to establish what
would make the tool worth adopting *before* seeing the demo, because after the demo it
is too late to think clearly.

## Purpose

AI tooling is adopted on impression far more often than on evidence: a striking demo, a
benchmark chart, a colleague's enthusiasm. The cost lands months later as migration
work and lock-in. A short, honest evaluation against the job you actually have is worth
more than any benchmark table.

## Input Arguments

- `$TOOL`: The tool, model, framework, or technique under consideration. Required.
- `$JOB`: The specific task you would use it for. Ask if missing — "is it good?" is
  unanswerable; "is it better than what we use for X?" is answerable.
- `$CURRENT`: What you use today, including "nothing, done manually". This is the
  baseline and the evaluation is meaningless without it.
- `$CONSTRAINTS`: Budget, data-residency and privacy rules, latency limits, team skill.

## Process

### Step 1: Write the criteria before you try it
Decide first, in writing, what result would make you adopt, and what would make you
pass. Doing this after the trial guarantees you rationalize whatever you saw.

State a threshold for each dimension that matters — quality on your task, cost at your
volume, latency, reliability, effort to integrate, and what happens if the vendor
changes terms or disappears.

### Step 2: Build a small honest test set
Twenty to fifty real examples from your actual work, including the hard cases and the
weird ones. Not curated favorites, not vendor examples.

Include cases the current solution fails. If the new tool also fails them, the demo was
selling you something else.

### Step 3: Run the baseline first
Measure the current solution on the same set before touching the new tool. Teams
routinely discover the baseline is better than remembered, or that the real problem is
upstream and no tool fixes it.

### Step 4: Compare on the same inputs
Same examples, same evaluation, results recorded side by side. Two things distort this
step, and both need naming:

- **Novelty effort.** New tools get careful prompts and patient debugging that the
  incumbent stopped receiving long ago. Equalize the effort or state that you did not.
- **Cherry-picked benchmarks.** Vendor numbers are on their test set, not yours.
  Yours is the only one that decides this.

### Step 5: Cost it at real volume
Price the actual usage pattern, not a single call: your volume, your input sizes, retries
and failures, and the human time to integrate and maintain it. A tool that is cheaper per
call and needs a week of glue code is not cheaper this quarter.

### Step 6: Weigh the exit
How hard is it to leave? Data export, prompt and workflow portability, proprietary
formats, how much of your product's behavior comes to depend on this specific model.
For fast-moving categories, the ability to switch later is worth more than a marginal
quality win now.

### Step 7: Decide and set a revisit trigger
Adopt, pass, or run a bounded pilot. Then name the event that would reopen the
decision — a price change, a capability landing, your volume crossing a threshold — so
the answer has a shelf life instead of hardening into policy.

## Output Format

```
## Evaluation: [Tool] for [job]

**Baseline**: [what we do today]
**Decision criteria** (set before testing):
| Dimension | Threshold to adopt | Result | Met? |
| --- | --- | --- | --- |
| Quality on our set | [x] | [y] | ✓/✗ |
| Cost at [volume] | [x] | [y] | ✓/✗ |
| Latency | [x] | [y] | ✓/✗ |
| Integration effort | [x] | [y] | ✓/✗ |

### Test set
[n] real examples, including [hard cases]. Source: [where from]

### Results
| Case type | Baseline | [Tool] | Notes |
| --- | --- | --- | --- |

### Cost at real volume
[Calculation, including retries and human time]

### Exit cost
[What leaving would take]

### Decision
**[Adopt / Pass / Pilot]** — [reasoning tied to the criteria above]

**Revisit if**: [specific trigger]
**What we did not test**: [honest gaps]
```

## Quality Bar

- Criteria are written before results are known, and the write-up shows that order.
- The baseline was measured, not remembered.
- The test set is the user's real data, including hard cases.
- Cost is computed at real volume including failures and integration time.
- The decision cites the criteria rather than an overall impression.
- Gaps in the evaluation are stated, not hidden.

## Notes

- Never assert current prices, context limits, rate limits, or capabilities from
  memory. Check the vendor's live documentation and cite what you found and when.
- Beware evaluating a tool on the task it demos well rather than the task you have.
  That substitution is the single most common way these decisions go wrong.
- A pilot needs an end date and a decision owner, or it becomes adoption by default.
- If the evaluation reveals the underlying problem is a spec problem rather than a tool
  problem, stop and go write the spec.
