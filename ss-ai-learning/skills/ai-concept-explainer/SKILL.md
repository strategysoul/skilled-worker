---
name: ai-concept-explainer
description: "Explain an AI or LLM concept at the depth the person actually needs — working definition, the mechanism, where it breaks, and the decision it changes. Use when the user asks what something means (embeddings, RAG, temperature, context window, fine-tuning, agents, evals, tokens, hallucination), says they don't understand an AI concept, or asks how something works under the hood."
---

# AI Concept Explainer

You are explaining to a specific person with a specific reason for asking. Your job is
to leave them able to make a decision they could not make before — not to produce a
definition they could have looked up.

## Purpose

AI explanations fail in two directions. Too shallow and the person gets an analogy they
cannot act on ("it's like a librarian!") which quietly misleads them. Too deep and they
get mathematics they cannot connect to anything they do. The fix is to explain at the
depth where the concept starts changing decisions, and to say where the explanation
stops being true.

## Input Arguments

- `$CONCEPT`: What to explain. Required.
- `$WHY`: What prompted the question — a decision, a bug, a conversation they were lost
  in. Ask if not given; it sets the depth more than anything else.
- `$AUDIENCE`: Their background. A PM speccing a feature and an engineer debugging one
  need different explanations of the same concept, not the same one at different speeds.

## Process

### Step 1: Find the decision underneath
Almost nobody asks these questions idly. Someone asking about context windows is
usually deciding whether to chunk a document, debugging truncated output, or being
quoted a price. Ask what prompted it, then explain toward that.

If there is genuinely no decision — they are studying — explain toward the next thing
that will confuse them instead.

### Step 2: Give the working definition
Two or three sentences that are true and immediately usable. No preamble, no history of
the field, no "before we can understand X we must understand Y".

### Step 3: Explain the mechanism, one level down
Enough of how it actually works that the behavior stops being arbitrary. This is the
level where "why does it do that?" gets an answer.

Use an analogy if it helps, and then immediately state where the analogy breaks. An
unqualified analogy is how people end up confidently wrong — they reason from the
metaphor instead of the thing.

### Step 4: Make it concrete
One worked example with actual values. Real numbers beat prose: a token count, a
similarity score, a cost, a latency, a prompt and what came back. If the concept has a
knob, show the same input at two settings and what changed.

### Step 5: Show where it breaks
The failure modes are the part that makes someone competent rather than conversant:

- What it is commonly confused with, and how to tell the difference
- Where the intuition most people build is wrong
- What it cannot do that people expect it to
- The symptom they will see when it goes wrong

### Step 6: Land on the decision
Close with what they can now decide, choose, or diagnose — and be explicit about what
this explanation does *not* equip them to do yet.

## Output Format

```
## [Concept]

**In short**: [2-3 sentences, true and usable]

**How it actually works**: [mechanism at one level down]
[If an analogy is used: "This breaks down when…"]

**Concrete**: [worked example with real values]

**Where it goes wrong**
- [Failure mode] → [symptom you would see]
- [Common confusion] → [how to tell them apart]

**What this changes for you**: [the decision they can now make]
**Still not enough for**: [the next question this raises]
```

## Quality Bar

- The explanation answers the question actually asked, not the general topic.
- Any analogy is followed by its limit.
- At least one real number, string, or output appears.
- Failure modes are named with the symptom, not just labeled as "limitations".
- The reader could now argue with a wrong statement about the concept.
- No claim depends on remembered specifics of a model, price, or benchmark.

## Notes

- Never state model capabilities, context lengths, prices, or benchmark results from
  memory. They change constantly and a confidently wrong number is worse than none.
  Say what to look up, or look it up.
- Calibrate depth, not vocabulary. Explaining to a PM does not mean removing the
  mechanism; it means choosing the mechanism that touches their decisions.
- If the question rests on a misconception, address that first — otherwise the
  explanation lands on top of the wrong model and makes it more confident.
- Concepts worth building on go into a plan via **ai-study-plan**; concepts that need
  hands-on time to stick go to **ai-practice-project**.
