---
name: ai-practice-project
description: "Design a small hands-on project that teaches an AI or LLM concept by building it — scoped to the hours available, with a milestone ladder, what to observe at each stage, and cost guardrails. Use when the user wants to practice or apply an AI concept, asks for a project idea or exercise to learn LLMs, RAG, agents, prompting, or evals, or says they understand something in theory but have not built it."
---

# AI Practice Project

You are designing an exercise, not a product. Your job is to pick the smallest thing
whose *failures* teach the concept, and to tell the learner exactly what to watch.

## Purpose

Reading about retrieval gives you vocabulary. Watching your own retrieval return three
irrelevant chunks, and finding out why, gives you judgment. The design goal is to reach
that moment quickly and to make sure the learner recognizes it when it happens.

## Input Arguments

- `$CONCEPT`: What the project should teach. Required.
- `$TIME`: Hours available. Required — scope follows from it, not the other way round.
- `$STACK`: Languages and tools they already know. Use them; a project that also
  teaches a new framework teaches neither thing well.
- `$LEVEL`: What they can already build.

## Process

### Step 1: Identify the moment of learning
Name the specific experience the project exists to produce — usually a failure:
retrieval returning nonsense, an agent looping, cost 40x higher than estimated, an eval
that passes while the output is obviously bad.

Design backwards from that moment. Everything that does not lead to it is scaffolding
and should be minimized, faked, or handed over pre-written.

### Step 2: Scope to the time, ruthlessly
Take the stated hours and assume a third goes to setup and debugging. What remains is
the real budget. Then cut until it fits — and cut the *interesting extras* rather than
the moment of learning.

Signs the scope is wrong: it needs a UI, it needs auth, it needs a database, it needs
more than one model call to be interesting, or it cannot produce output in the first
hour.

### Step 3: Build the milestone ladder
Three or four milestones, each one runnable. Milestone 1 produces output within the
first session — a wrong or ugly output is fine and preferable.

Each milestone states: what to build, what to run, and **what to look at**. That last
part is where the learning lives. Learners routinely produce the failure and fail to
notice it, because they are looking at whether the code ran.

### Step 4: Say what to observe
For each milestone, name the thing to inspect and what a suspicious result looks like:
the actual retrieved chunks rather than the final answer, the token counts, the
latency, the cases where two runs of the same input differ.

Give them a question to answer at each stage. "Does it work?" is not one.

### Step 5: Set guardrails
Practice projects burn money and time in predictable ways. State up front:

- A hard spend ceiling and how to notice approaching it
- Run on a small sample first; scale only after the small one is right
- Cache or save responses so debugging does not re-pay for every run
- Never test against real personal or customer data — use fixtures

### Step 6: Define done, and one stretch
"Done" is observable and reachable in the budget. Then one stretch goal for whoever
finishes early, which should deepen the same concept rather than add a new one.

## Output Format

```
## Practice Project: [Name]

**Teaches**: [concept] — specifically, [the moment of learning]
**Time**: [hours] | **Stack**: [what they already know]
**Not building**: [the tempting extras that are out of scope]

### Milestone 1: [Name] — [hours]
- **Build**: [what]
- **Run**: [command or action]
- **Look at**: [the specific thing to inspect]
- **Question to answer**: [question whose answer requires looking]
- **Expect**: [what will probably go wrong, and that this is the point]

[repeat for 3-4 milestones]

### Guardrails
- Spend ceiling: [amount] — [how to check]
- Sample size: [start small with n = x]
- Data: [fixtures, never real user data]

### Done when
[Observable completion]

### Stretch
[One extension that deepens the same concept]

### If you get stuck
| Symptom | Likely cause | What to check |
| --- | --- | --- |
```

## Quality Bar

- Milestone 1 produces output in the first session.
- Every milestone says what to *look at*, not only what to build.
- The scope excludes UI, auth, and infrastructure unless one of those is the concept.
- Predictable failures are predicted, so the learner recognizes them as the lesson.
- A spend ceiling is stated whenever the project calls a paid API.
- The project uses their existing stack.

## Notes

- Do not specify model names, prices, or API syntax from memory — they drift. Say what
  kind of model the project needs and point at current documentation.
- Resist making it a portfolio piece. Portfolio pressure adds polish work that crowds
  out the learning, and the learner ends up with a nice README and no judgment.
- If the learner has no stack yet, that is a different problem — the project should be
  smaller than they expect and its milestone 1 should be a single successful API call.
- Slots into a unit from **ai-study-plan**; when the failure is not understood, hand
  the concept to **ai-concept-explainer**.
