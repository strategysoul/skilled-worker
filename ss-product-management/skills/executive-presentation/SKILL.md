---
name: executive-presentation
description: "Turn an analysis, report, or document into a one-page recommendation for senior leadership — the recommendation first, then the reasoning with its numbers and sources, the risks of acting and of doing nothing, and the next steps. Use when the user needs to present findings to executives or a leadership team, wants an executive summary or a decision memo or a recommendation page, asks how to pitch or land something upward, or has an analysis that needs to become an ask."
---

# Executive Presentation — R3N

Recommendation · Reason · Risk · Next steps

You are writing for someone with eight minutes and four other decisions today. They will
read the first line. Whether they read the second depends entirely on the first.

## Purpose

Most analysis reaches leadership in the order it was performed — background, method,
findings, and a recommendation at the end, if at all. That order is backwards for the
reader. They cannot judge whether your evidence matters until they know what you want.

R3N inverts it. The recommendation leads. Everything after it exists to answer the
questions the recommendation provokes, in the order an executive actually asks them:

**R**ecommendation — what we should do
**R**eason — why, with the numbers and where they came from
**R**isk — what happens if we do it, and what happens if we do not
**N**ext steps — how we get from here to done

## Input Arguments

- `$ANALYSIS`: The work this recommendation comes out of — a research report, a data
  analysis, a PRD, a deck, a spreadsheet, a memo. Required. Ask for it rather than
  writing a recommendation from the conversation alone; a recommendation with nothing
  behind it is an opinion in a decision's clothing.
- `$AUDIENCE`: Who is in the room, and what each of them controls. Changes which
  reasons land — a CFO and a VP Engineering do not care about the same number.
- `$ASK`: What you want from them: a decision, a budget, a headcount, a sign-off, or
  nothing at all. Ask if unclear. A page with no ask wastes the meeting.
- `$CONSTRAINTS`: Deadlines, budget ceilings, commitments already made, politics you
  should not walk into blind.

If the analysis does not support a recommendation, say so and stop. "The data does not
tell us yet, and here is what would" is a legitimate output of this skill and a better
one than a confident guess.

## Process

### Step 1: Find the decision
Before writing anything, name the decision this analysis serves and who owns it. If the
analysis serves no decision, the honest recommendation may be that no one needs to meet
about it.

State the ask in one line at the top, above the recommendation: what is being decided,
what you need from this room, and by when. Executives read faster when they know why
they are in the room.

### Step 2: Write the recommendation as a decision, not a topic
One sentence. It must contain an action, and it must be specific enough that someone
could refuse it.

- Not a recommendation: "We should improve onboarding." That is a topic.
- A recommendation: "Cut agency onboarding from five steps to two by removing manual
  verification for accounts under $10k, starting next sprint."

Name the owner, the resource ask, and the date. A recommendation with no owner and no
date is a suggestion, and suggestions do not survive the walk back to the desk.

**One recommendation per page.** Where genuinely different options exist, present them —
but recommend one of them. Handing leadership three options and no view is asking them
to do your job with less context than you have.

### Step 3: Give three reasons, each carrying a number and its source
Three at most. This is not stylistic — it is what a reader retains from a page they read
once, standing up.

Each reason:

- leads with the number, not the narrative — "£1.4m of annual support cost", not "support
  costs are significant"
- says where the number came from: the query, the report, the model, the date it covers
- shows the arithmetic where a figure was derived, so someone can check it rather than
  believe it
- states the confidence, and what would change it

Round to the precision that survives scrutiny. `£1.4m` reads as a considered estimate;
`£1,437,216.40` reads as false precision and invites an argument about the wrong thing.

**Never invent a figure.** Where the analysis has no number for something that needs one,
write `[NEEDS DATA: what and from where]` and leave it visible. A placeholder in a draft
is a task; a fabricated number in a board pack is a career event.

The reasons are why *this recommendation*, not a summary of everything you found. Most of
the analysis does not belong here. That is what the appendix is for.

### Step 4: State the risk in both directions
Two questions, both answered:

- **If we do this, what could go wrong?** Cost, disruption, what it forecloses, who is
  affected, what breaks if the assumption underneath it is false.
- **If we do nothing, what happens?** The cost of the status quo, its trajectory, and
  when it stops being reversible. This is the half that is usually missing, and it is
  usually the half that moves the decision — inaction reads as free until someone prices
  it.

Each risk gets a mitigation or a trigger to watch, and an honest likelihood. A risks
section that lists only manageable risks is not credible, and any executive worth
presenting to will find the one you left out.

Then name your own falsifier: **what would make this recommendation wrong?** A
recommendation that cannot be wrong cannot be evaluated, and volunteering the condition
under which you would reverse it buys more credibility than another supporting number.

Where the stakes justify it, run the question backwards: it is a year from now and this
failed — what happened? Risks written forward tend to be the polite ones.

### Step 5: Make the next steps startable
Not a plan. The first few moves, each with a name against it and a date, and the first
one startable this week. Include what you need from the room to unblock step one.

End with when you will come back and with what — a decision that disappears into
"we'll pick it up next quarter" was not really taken.

### Step 6: Prepare for the second question
Everything cut from the page goes into an appendix, ordered by how likely it is to be
asked for. Executives probe one level deeper than the page, and "I can follow up on
that" spends credibility that the page just earned.

Anticipate the three hardest challenges and know where the answer is.

## Output Format

```
**Deciding**: [the decision] · **Need from you**: [approval / budget / sign-off / nothing]
· **By**: [date]

## Recommendation
[One sentence: action, scope, and when. Specific enough to refuse.]
Owner: [name] · Ask: [budget, headcount, or none] · Start: [date]

## Reason
1. **[Number]** — [what it means]. [Source, and the period it covers.]
   [Derivation, where the figure was calculated.] Confidence: [high/medium/low — why]
2. **[Number]** — ...
3. **[Number]** — ...

## Risk
**If we proceed**
| Risk | Likelihood | Impact | Mitigation |
| --- | --- | --- | --- |

**If we do nothing**
| What continues | Cost | When it becomes irreversible |
| --- | --- | --- |

**This recommendation is wrong if**: [the condition that would reverse it]

## Next steps
| # | Step | Owner | By |
| --- | --- | --- | --- |
| 1 | [startable this week] | [name] | [date] |

**Blocked on**: [what you need from this room]
**Back to you**: [date] with [what]

---
## Appendix
[Method, full data, alternatives considered and why they lost, detail behind each number
— ordered by how likely it is to be asked for.]
```

Keep the page above the line to one page. If it does not fit, the recommendation is
doing too much, not the page too little.

Offer a spoken version when the user is presenting live: sixty seconds covering the
recommendation, the strongest number, the cost of doing nothing, and the ask.

## Quality Bar

- The recommendation is the first thing on the page and contains a verb.
- Someone could disagree with it — it names an action, a scope, and a date.
- Exactly one recommendation. Options, where present, come with a recommended one.
- Three reasons at most, each leading with a number that carries its source and date.
- Every derived figure can be checked from what is on the page or in the appendix.
- No invented numbers. Gaps are marked `[NEEDS DATA]`, not filled in.
- Risk is answered in both directions, and doing nothing has a stated cost.
- The falsifier is named — what would make this wrong.
- Step one is startable this week and has a name against it.
- Nothing in the analysis appears on the page unless it supports the recommendation.

## Notes

- Cut the method. How the work was done belongs in the appendix; leadership is buying
  the conclusion and your judgment, and a page that defends its method before its answer
  reads as unsure of the answer.
- Write "we should", not "it is recommended that". Passive recommendations have no
  owner, which is often exactly why they are written that way.
- If the honest recommendation is "do nothing", write that, with the same structure. It
  is a real answer and a rarer one.
- Where the analysis came from **deep-research**, carry the confidence tiers through: a
  reason resting on a low-confidence finding should not be presented as settled, and the
  links and dates come with it.
- Where it came from an analysis with open questions — a PRD via **prd-drafting**, a
  test pass, a verification report — the unresolved ones are risks, not omissions.
- Resist the pull to include the work you are proudest of. The analysis that took three
  weeks and does not change the decision still does not go on the page.
