---
name: mathia-research-clues
description: Hand off speculative but source-motivated research clues from Mind, Graph Curator, Research Watch, Adversarial Research, or Master Researcher without treating clues as evidence or discoveries.
---

# Mathia Research Clues

## Responsibility

Use this skill together with `mathia-research-mind`, `mathia-research-graph-curator`, `mathia-research-watch`, `mathia-research-adversarial`, or `mathia-master-researcher` when a recurring process needs to hand off a promising but unvalidated mathematical direction to research.

A **clue is not a finding, intuition, theorem, novelty claim, review verdict, portfolio recommendation, or accepted research result**. It is a compact, falsifiable research lead suggested by already-persisted repository structure, synthesis, primary research, adversarial friction, or program-level cross-line analysis but still requiring the normal Research Watch derivation, stress test, literature check, and evidence gate.

This skill is a narrow extension of the caller skill's path gate for clue files only. All other caller ownership restrictions remain unchanged.

The existing Mind, Graph Curator, Research Watch, and Adversarial Research clue behavior remains unchanged; this skill additionally allows the Master Researcher to emit source-grounded clues from cross-line/portfolio analysis.

## Storage

For a clue that clearly belongs to an existing research line, use:

```text
research/<line>/clues/CLUE-<slug>.md
```

This is preferred because the corresponding line-specific Research Watch can triage it without cross-line ownership ambiguity.

For a genuinely cross-line clue, a possible entirely new research line, or a clue that cannot yet be assigned honestly, use:

```text
research/clues/CLUE-<slug>.md
```

Global clues are a frontier inbox. Existing line-specific watches must not silently adopt or rewrite them unless this skill explicitly authorizes the operation.

Do not create a clue directory merely to show that a run happened.

## Stable identity and deduplication

Use a descriptive deterministic slug rather than a numeric sequence. Before creating a clue, search existing local and global clues for the same mathematical question.

Prefer strengthening an existing `proposed` clue with materially better persisted motivation over creating a near-duplicate. Do not merge two clues unless their research question and decisive test are genuinely the same.

Repository path is the clue identity.

## Minimal clue schema

Use compact frontmatter:

```yaml
---
id: CLUE-<scope>-<slug>
type: research-clue
status: proposed
origin: mind | graph-curator | research-watch | adversarial | master-researcher
target_line: <line> | global | new-line-candidate
based_on:
  - <repository path>
---
```

Then keep only these substantive sections:

```text
# <research question>

## Observation
What persisted finding, intuition, review, graph structure, or cross-line program state suggested the clue.

## Research question
The precise candidate mechanism, connection, obstruction, or distinction to investigate.

## Why it may matter
Why resolving the question could materially redirect or extend the research program.

## Decisive test
The derivation, theorem, counterexample, control, or novelty audit that would accept or kill the direction.

## Evidence boundary
What is explicitly NOT established yet and why this remains a clue rather than evidence.
```

Do not add dates, run logs, priorities, confidence percentages, owners, schedules, or speculative claims of novelty.

## Status semantics

Allowed lifecycle states are:

```text
proposed
accepted
rejected
resolved
```

Their meanings are strict:

- `proposed`: a producer identified a research-worthy question, but the owning Research Watch has not triaged it.
- `accepted`: the owning Research Watch checked scope and basic plausibility/prior-art fit and considers it worth active investigation. This does **not** assert truth or novelty.
- `rejected`: Research Watch found a reason not to pursue it, such as duplication, known prior art with no residual question, an exact obstruction, malformed premise, or scope mismatch.
- `resolved`: research produced a durable outcome. Link the resulting finding(s) and state whether the outcome supported, narrowed, classicalized, or refuted the clue.

Status is workflow metadata for handoff only. It must never be used as mathematical evidence.

## Producer: Mathia Research Mind

When loaded with `mathia-research-mind`, the Mind may emit a clue when its synthesis exposes a precise potentially fertile direction that **cannot yet be promoted to a durable intuition or research line from persisted evidence alone**.

Good Mind clues include:

- two local intuitions suggesting a possible exact bridge whose proof is missing;
- several findings suggesting a deeper ordered-memory coefficient not yet derived;
- an apparent cross-line common invariant needing an explicit equivalence or counterexample;
- a plausible escape from a known impossibility principle requiring new mathematical work.

The Mind must not use a clue to smuggle unsupported claims into the repository. The `Evidence boundary` must make the missing premise explicit.

For an existing local line, write under that line's `clues/**`. For a genuinely cross-line or new-line candidate, write under `research/clues/**`.

The Mind may create a new clue or strengthen the motivation of an existing `proposed` clue. It must not set `accepted`, `rejected`, or `resolved`; those states belong to Research Watch evaluation.

## Producer: Research Graph Curator

When loaded with `mathia-research-graph-curator`, the Curator may emit a clue only when graph curation reveals a **source-grounded structural pattern that is interesting precisely because the required mathematical edge is not yet established**.

Examples:

- two branches repeatedly touch the same canonical prior-art node but no finding proves a direct bridge;
- multiple independent obstruction chains terminate at the same unexplored representation;
- a cluster of findings/intuitions suggests an untested cross-line equivalence or control;
- the graph exposes an isolated frontier component whose missing connection is a precise mathematical question.

Graph topology, semantic proximity, co-citation, or shared vocabulary alone are not enough. A clue needs explicit persisted source nodes and a falsifiable mathematical question.

The Curator must not create a graph edge for the unproved relation. It may create or strengthen only `proposed` clues and must not perform the research needed to accept/reject them.

## Producer and consumer: Mathia Research Watch

When loaded with `mathia-research-watch`, a line-specific Research Watch should inspect:

```text
research/<line>/clues/**
```

as optional candidate input after reconstructing the line's current mathematical state and processing actionable adversarial reviews.

Clues do not outrank the watch's own research judgment and do not force work every run. Prefer clues whose decisive test is tractable and whose outcome could materially change the line.

For each clue actually triaged:

1. verify it belongs to the watch's exact mathematical scope;
2. reconstruct the question independently from authoritative findings/sources it cites;
3. run the normal derivation, adversarial stress test, and serious prior-art/novelty check from `mathia-research-watch`;
4. decide whether the direction deserves continued research;
5. update only the clue's status/outcome consistently with this skill.

The Research Watch may also **produce** a clue when primary research or an owner-side response in a `.review.md` thread reveals a valuable question that is separate from the claim currently being established/defended.

A review-generated clue should normally cite both the finding and its sidecar in `based_on`. Do not turn the clue into a summary of the review. The clue must state a distinct research question.

A line-specific watch may propose local clues under its own `research/<line>/clues/**`. It may propose a global clue under `research/clues/**` only when the question is genuinely cross-line or a new-line candidate and the persisted basis makes that scope explicit.

### Accepting a clue

Set `status: accepted` only when the direction survives enough initial checking to justify continued investigation. Add a concise `## Research disposition` explaining what precise unresolved question remains.

Acceptance is not a substantive finding and must not create a canonical finding by itself.

### Rejecting a clue

Set `status: rejected` when the direction should not be pursued. Add a concise `## Research disposition` with the decisive reason.

If the rejection itself satisfies the Research Watch substantive-finding gate, also persist the corresponding durable finding normally and link it from the clue. If rejection is merely duplicate/out-of-scope/malformed, do not manufacture a finding.

### Resolving a clue

Set `status: resolved` when research has produced a durable accepted outcome under the normal finding gate. Add:

```text
## Research disposition
Outcome: supported | narrowed | classical | refuted

Resolved by:
- [[research/<line>/findings/<finding>]]
```

The linked finding, not the clue, is the mathematical evidence.

## Producer: Adversarial Research

When loaded with `mathia-research-adversarial`, the adversary may emit a clue only when auditing a finding or discussing an open `.review.md` exposes a **separate**, potentially fertile research question.

Good adversarial clues include:

- the same failure mode may apply to another research line and needs explicit testing;
- a defense reveals an invariant not required to settle the current review;
- the objection and defense together suggest a discriminating theorem/control outside the target claim;
- a review uncovers a possible cross-line equivalence whose truth is not needed for the verdict.

The adversary must not use clues to outsource an objection that should remain in the `.review.md`, and must not encode the review verdict as a clue.

It may create or materially strengthen only `proposed` clues. It must not set `accepted`, `rejected`, or `resolved`; those belong to the owning Research Watch.

For an existing local line, prefer `research/<line>/clues/**`. Use `research/clues/**` only for genuinely cross-line/new-line questions.

## Producer: Master Researcher

When loaded with `mathia-master-researcher`, the Master may emit a clue only when its current program-level analysis exposes a **concrete falsifiable question** that belongs back in mathematical research.

Good Master clues include:

- an established mechanism in one line may transfer to another and needs an exact test;
- several lines share one unresolved lemma/estimate/representation that can be attacked directly;
- an apparent cross-line redundancy needs an equivalence or counterexample before a merge recommendation is safe;
- a possible `pause-candidate` has one precise unresolved escape route worth killing or validating first;
- a `new-line-candidate` has a cheap decisive first test that no existing line can honestly own.

The Master must not use clues as project-management commands or encode `continue`, `pause`, `merge`, `split`, or scheduling decisions inside them. A clue remains a mathematical research question.

It may create or materially strengthen only `proposed` clues. It must not change Research Watch disposition states.

For an existing destination line, prefer `research/<line>/clues/**`. Use `research/clues/**` only when the question is genuinely cross-line or a new-line candidate.

## Ownership extension

When this skill is explicitly loaded, it extends writable paths only as follows.

### Mind

May create or strengthen `proposed` clues under:

```text
research/<discovered-line>/clues/**
research/clues/**
```

It may not change Research Watch disposition states.

### Graph Curator

May create or strengthen `proposed` clues under:

```text
research/<research-line>/clues/**
research/clues/**
```

It may not change Research Watch disposition states.

### Research Watch for `<line>`

May read/update lifecycle state for local clues and may create/strengthen `proposed` clues under:

```text
research/<line>/clues/**
```

It may additionally create/strengthen a `proposed` clue under:

```text
research/clues/**
```

only when the clue is genuinely cross-line or a new-line candidate. It must not modify another line's local clues.

### Adversarial Research

May create or materially strengthen only `proposed` clues under:

```text
research/<line>/clues/**
research/clues/**
```

It must not change `accepted`, `rejected`, or `resolved` dispositions and must not modify a clue merely to record that it reviewed it.

### Master Researcher

May create or materially strengthen only `proposed` clues under:

```text
research/<line>/clues/**
research/clues/**
```

It must not change Research Watch disposition states, create a clue solely to record a portfolio recommendation, or modify a clue merely because it appeared in `research/master/STATE.md`.

This exception does not grant access to any other caller-forbidden path.

## Publication and no-churn gate

A clue change may share the caller's normal direct-main publication path when all of these hold:

- every clue path is allowed for that caller above;
- the clue is materially new, materially better grounded, or its Research Watch disposition changed;
- any review-derived clue cites the persisted finding/review that motivated it;
- any Master-derived clue cites the current persisted findings/mind/graph/clues that motivated the cross-line question;
- no timestamps/run logs/status noise were added;
- the source revision remains coherent;
- the caller's normal diff review and publication gates pass.

Use the caller's normal commit prefix. Do not create a commit solely to restate an unchanged clue.

## Notification policy

Clue persistence and clue notification are separate thresholds.

- Producers (`Mind`, `Graph Curator`, `Adversarial Research`, `Master Researcher`, or a Research Watch proposing its own clue) do **not** notify merely because a clue is created or strengthened in `proposed` state, even if the clue appears consequential.
- A Research Watch notifies when it changes a clue to `status: accepted`.
- Do not notify merely because a clue becomes `rejected` or `resolved`. Any durable mathematical result produced while rejecting or resolving it is governed by the Research Watch's ordinary notification policy, not by clue status itself.

This is the shared default for all clue-producing/consuming research processes. Task prompts should normally inherit it rather than restating clue-specific notification rules.

## Reporting

Keep clue lifecycle changes durable in the repository, but surface a clue-specific user notification only for `accepted` as defined above.
