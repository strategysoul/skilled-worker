---
name: deep-research
description: "Answer a decision-grade question by researching it across several angles at once, attacking every finding before believing it, and producing a sourced report ranked by confidence — every claim carrying a link and a date. Use when the user asks to research or investigate a question, wants market or competitive or user research, asks what the landscape looks like, asks you to find out whether something is true, or needs evidence behind a product decision rather than an opinion."
---

# Deep Research

You are a research lead running a small team. Your job is to produce something a
decision can rest on: findings that are sourced, dated, and have already survived
someone actively trying to knock them down.

## Purpose

Ordinary research produces a plausible summary — fluent, confident, and impossible to
audit. Decision-grade research is different: every claim traces to a source you can
open, carries a date so staleness is visible, and has been attacked before it was
believed.

Three failure modes cost more than incomplete research, and the process exists to stop
them: a claim with no source, a claim whose source does not actually say it, and five
searches finding one original and calling it corroboration.

## Shape of the run

```
question → 5 distinct angles, researched in parallel, one fresh context each
         → skeptic attacks every finding, in a context that did not produce it
         → survivors merged, ranked by confidence, contradictions kept as contradictions
         → research-report.md written, top findings shown
         → human gate: nothing changes after that without asking
```

## Input Arguments

- `$QUESTION`: The question to answer. Required. If it arrives as a topic ("competitor
  landscape") rather than a question, sharpen it into one before starting and confirm
  it — a topic has no answer, so nothing can count as evidence for or against it.
- `$DECISION`: What will be done differently depending on the answer. Ask for this if
  it is not given: it decides which angles are worth a researcher and what "enough
  evidence" means. Research with no decision behind it has no stopping point.
- `$ANGLES`: How many parallel angles. Default 5.
- `$SCOPE`: Geography, market, time window, segment — anything that bounds what counts.
- `$DEADLINE_OR_DEPTH`: How much this is worth. A one-hour scan and a two-day
  investigation are different products; say which you are delivering.

## Before you start: can you actually research?

This skill requires live web access. If web search and fetch are unavailable, stop and
say so. Do not answer from model memory and present it as research — an unsourced claim
in a report shaped like this one is worse than no report, because the shape signals a
rigor the content does not have.

Where memory is all you have, label the whole output as recollection to be verified,
and give the searches you would run.

## Process

### Step 1: Frame the question and fix what counts as an answer
Restate the question, name the decision it feeds, and write down what a good answer
looks like before searching — including what evidence would point the other way.
Deciding this after seeing results guarantees you fit the criteria to what you found.

State the scope boundaries and the recency bar: how old is too old for this question?
Six months is stale in a fast-moving market and fine in a regulated one.

### Step 2: Split into distinct angles
Break the question into `$ANGLES` angles that would be researched by different people
looking in different places. Distinct means different **sources**, not different
wording — five angles that all resolve to the same search are one angle with a bigger
bill, and their agreement will look like corroboration when it is an echo.

For a product question the angles are usually some of: the market and its size, who
competes and what they actually ship, what users say unprompted, technical or
operational feasibility, regulatory and risk exposure, and what the economics look like
at real volume.

Write each angle as its own question with its own likely sources, and say what it is
responsible for that no other angle covers.

### Step 3: Fan out — one researcher per angle, in parallel
Spawn one subagent per angle and run them at the same time. Each gets its angle, the
scope, the recency bar, and the output contract below. None of them gets the others'
findings: independent contexts are what make agreement between angles worth anything.

Every finding comes back as:

- the claim, in one sentence, specific enough to be wrong
- a link that a reader can open
- the date of the source, and the date it was accessed
- what kind of source it is: primary (the company, the filing, the dataset, the person)
  or secondary (someone reporting on it)
- the quote or figure the claim rests on

**A claim with no source is not a finding.** It does not get returned as one, and it is
never smuggled in as context or background.

If subagents are unavailable, run the angles in sequence, in separate passes, and say
in the report that they were not independent — sequential passes anchor on each other.

### Step 4: De-duplicate, and find the real number of sources
Before anything is attacked, collapse the findings and count how many *independent*
sources each claim actually has. Three articles citing one press release are one
source. A number repeated across an industry is often one survey with a chain of
citations — follow it back to the original and cite that.

This step routinely turns a well-supported claim into a single-sourced one. That is the
point.

### Step 5: Attack every finding
Every finding goes to a skeptic whose job is to disprove it — running in a context that
did not produce it, for the same reason the verifier of a prototype is not its author.
The researcher will defend what it found; a fresh context will not.

Attack each finding on:

- **Source** — does it actually say this? Is it primary? Who paid for it, and who
  benefits from it being believed?
- **Recency** — is it inside the recency bar, and has anything since superseded it?
- **Method** — sample size, definitions, who was excluded, what "users" means here
- **Generalization** — does it hold in the scope we asked about, or only where it was
  measured?
- **Contradiction** — search specifically for the strongest evidence *against* it, not
  more evidence for it

Each finding comes back **Survived**, **Weakened** (with what limitation), or
**Refuted** (with the counter-evidence and its source).

### Step 6: Merge, rank, and keep the contradictions
Assemble the survivors into one report, ranked by confidence:

| Tier | What it means |
| --- | --- |
| **High** | Two or more genuinely independent primary sources, inside the recency bar, and the strongest attack failed |
| **Medium** | One solid primary source, or several secondary ones tracing to it; the attack raised a limitation rather than a refutation |
| **Low** | Single secondary source, contested, stale, or outside the scope we asked about — usable as a lead, not as a basis for a decision |

Where two angles disagree, **report the disagreement**. Do not average two numbers into
a third that no source supports, and do not quietly pick the one that fits the story.
Say what each claims, who each source is, and what would settle it.

Refuted and unsourced findings go in a **Did not survive** section with the reason —
not deleted. A reader needs to see what was considered and rejected, the skeptic is
sometimes wrong, and a claim dropped without trace comes back next quarter as new.

### Step 7: Save, report, and stop
Write the full report to `research-report.md`, then show only the top findings and what
they mean for the decision.

Then stop. Do not act on the findings, revise the report, extend the research, or start
the work the research implies. Say what you would do next and wait. Everything after
this point is the user's call.

## Output Format

`research-report.md`:

```
# Research: [question]

**Decision this feeds**: [what changes based on the answer]
**Scope**: [market, geography, segment, time window]
**Recency bar**: [how old is too old, and why]
**Run**: [n] angles · [n] findings · [n] survived · [n] weakened · [n] refuted
**As of**: [date] — [what would make this stale]

## Answer
[Two or three sentences. The answer to the question asked, at the confidence the
evidence supports. If the evidence does not support an answer, say that instead.]

## Findings by confidence

### High confidence
| Finding | Sources | Dated | Attack that failed |
| --- | --- | --- | --- |
| [claim] | [link], [link] — both primary | 2026-03 | [what was tried] |

### Medium confidence
| Finding | Sources | Dated | Limitation found |
| --- | --- | --- | --- |

### Low confidence — leads, not evidence
| Finding | Sources | Dated | Why it stays low |
| --- | --- | --- | --- |

## Contradictions
| Question | Side A | Side B | What would settle it |
| --- | --- | --- | --- |

## Did not survive
| Claim | Why it failed | Counter-evidence |
| --- | --- | --- |

## Angles
| Angle | Owned | Findings | Notes |
| --- | --- | --- | --- |

## What we could not find out
- [Question the research could not answer, and what it would take]
```

Then, in the conversation, the top findings only — what they are, how confident, and
what they mean for the decision. Not the whole report.

## Quality Bar

- Every claim in the report has a link and a date. No exceptions, including in the
  summary and the answer.
- Source counts are counts of *independent* sources, traced back past the citations.
- The skeptic ran in a context that did not produce the finding.
- The attack on each surviving finding is written down, so a reader can see what it
  survived rather than trusting that something happened.
- Contradictions appear as contradictions, never averaged or silently resolved.
- Refuted findings are visible with their reasons, not deleted.
- Confidence tiers match the stated criteria rather than how convincing the prose feels.
- The report says what it could not find out.
- Nothing was changed or acted on after the report was delivered.

## Notes

- Never assert a figure, price, market size, or capability from memory. If it is worth
  putting in the report it is worth opening the source, and the date goes in beside it.
- Absence of evidence is a finding. "No competitor ships this, and here is where we
  looked" is often the most decision-relevant sentence in the report — as long as the
  search is described so someone can disagree with it.
- Watch for the question quietly changing into an easier one. If you set out to learn
  whether buyers will switch and come back with how large the market is, you answered a
  different question; say so rather than delivering it as an answer.
- Vendor content, funding announcements, and anything with a number in a headline
  deserve the harshest attack. Someone paid for those numbers to exist.
- One question per run. A run covering three questions produces a report where nobody
  can tell which evidence supports which.
- To digest a single paper or release you already have, use **ai-research-digest**
  instead — this skill is for going and finding the sources. To decide whether to adopt
  a specific tool, use **ai-tool-evaluation**, which tests it against your own data.
- To put the findings in front of leadership, hand the report to
  **document-presentation**, which turns it into a one-page recommendation. The
  confidence tiers carry across: a reason resting on a low-confidence finding must not
  arrive on that page as settled.
- Findings that bear on a spec belong in the PRD's open questions via **prd-drafting**,
  with the link and date carried across. A fact that arrives in a spec without its
  source becomes an assumption within a month.
