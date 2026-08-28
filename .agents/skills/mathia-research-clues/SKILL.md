---
name: mathia-research-clues
description: Hand off speculative but source-motivated research clues from Mathia Mind or the Research Graph Curator to mathematical Research Watch tasks without treating clues as evidence or discoveries.
---

# Mathia Research Clues

## Responsibility

Use this skill together with `mathia-research-mind`, `mathia-research-graph-curator`, or `mathia-research-watch` when a recurring process needs to hand off a promising but unvalidated mathematical direction to research.

A **clue is not a finding, intuition, theorem, novelty claim, or accepted research result**. It is a compact, falsifiable research lead suggested by already-persisted repository structure or synthesis but still requiring the normal research-watch derivation, adversarial audit, literature check, and evidence gate.

This skill is an explicit narrow extension of the caller skill's path gate for clue files only. All other ownership restrictions of the caller remain unchanged.

## Storage

For a clue that clearly belongs to an existing research line, use:

```text
research/<line>/clues/CLUE-<slug>.md
```

This is the preferred form because the corresponding line-specific Research Watch can triage it without cross-line ownership ambiguity.

For a genuinely cross-line clue, a possible entirely new research line, or a clue that cannot yet be assigned honestly, use:

```text
research/clues/CLUE-<slug>.md
```

Global clues are a frontier inbox. Existing line-specific watches must not silently adopt or rewrite them unless the clue is explicitly reassigned into that line's local `clues/` directory by an authorized process.

Do not create a clue directory merely to show that a run happened.

## Stable identity and deduplication

Use a descriptive deterministic slug rather than a numeric sequence. Before creating a clue, search existing local and global clues for the same mathematical question.

Prefer updating an existing `proposed` clue with materially stronger persisted motivation over creating a near-duplicate. Do not merge two clues unless their research question and decisive test are genuinely the same.

Repository path is the clue identity.

## Minimal clue schema

Use compact frontmatter:

```yaml
---
id: CLUE-<scope>-<slug>
type: research-clue
status: proposed
origin: mind | graph-curator
target_line: <line> | global | new-line-candidate
based_on:
  - <repository path>
---
```

Then keep only these substantive sections:

```text
# <research question>

## Observation
What persisted findings/intuitions/graph structure suggested the clue.

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

- `proposed`: a producer has identified a research-worthy question, but Research Watch has not triaged it.
- `accepted`: the owning Research Watch has checked scope and basic plausibility/prior-art fit and considers it worth active investigation. This does **not** assert truth or novelty.
- `rejected`: Research Watch found a reason not to pursue it as a research direction, such as duplication, known prior art with no residual question, an exact obstruction, malformed premise, or mismatch with the line's mathematical object.
- `resolved`: research produced a durable outcome. Link the resulting finding(s) and state whether the outcome supported, narrowed, classicalized, or refuted the clue.

Status is workflow metadata for the clue handoff only. It must never be used as mathematical evidence.

## Producer: Mathia Research Mind

When loaded with `mathia-research-mind`, the Mind may emit a clue when its synthesis exposes a precise potentially fertile direction that **cannot yet be promoted to a durable intuition or research line from persisted evidence alone**.

Good Mind clues include:

- two local intuitions suggesting a possible exact bridge whose proof is missing;
- several findings suggesting a deeper ordered-memory coefficient not yet derived;
- an apparent cross-line common invariant that needs an explicit equivalence or counterexample;
- a plausible escape from a known impossibility principle that requires new mathematical work.

The Mind must not use a clue to smuggle unsupported claims into the repository. The `Evidence boundary` must make the missing premise explicit.

For an existing local line, write only under that line's `clues/**`. For a genuinely cross-line or new-line candidate, write under `research/clues/**`.

The Mind may create a new clue or strengthen the motivation of an existing `proposed` clue. It must not set `accepted`, `rejected`, or `resolved`; those states belong to Research Watch evaluation.

## Producer: Research Graph Curator

When loaded with `mathia-research-graph-curator`, the Curator may emit a clue only when graph curation reveals a **source-grounded structural pattern that is interesting precisely because the required mathematical edge is not yet established**.

Examples:

- two branches repeatedly touch the same canonical prior-art node but no persisted finding proves a direct bridge;
- multiple independent obstruction chains terminate at the same unexplored representation;
- a cluster of findings and intuitions suggests an untested cross-line equivalence or control;
- the graph exposes an isolated frontier component whose missing connection can be stated as a precise mathematical question.

Graph topology, semantic proximity, co-citation, or shared vocabulary alone are not enough. A clue needs explicit persisted source nodes and a falsifiable mathematical question.

The Curator must not create a graph edge for the unproved relation. The clue is the correct place to hand that uncertainty to research.

The Curator may create or strengthen only `proposed` clues. It must not perform the research needed to accept or reject them.

## Consumer: Mathia Research Watch

When loaded with `mathia-research-watch`, a line-specific Research Watch should inspect:

```text
research/<line>/clues/**
```

as optional candidate input after reconstructing the line's current mathematical state.

Clues do not outrank the watch's own research judgment and do not force work every run. Prefer clues whose decisive test is tractable and whose outcome could materially change the line.

For each clue actually triaged:

1. verify it belongs to the watch's exact mathematical scope;
2. reconstruct the question independently from the authoritative findings it cites;
3. run the normal derivation, adversarial stress test, and serious prior-art/novelty check from `mathia-research-watch`;
4. decide whether the direction is worth continued research;
5. update only that local clue's status/outcome consistently with the rules below.

### Accepting a clue

Set `status: accepted` only when the direction survives enough initial checking to justify continued investigation. Add a concise `## Research disposition` explaining what precise unresolved question remains.

Acceptance is not a substantive finding and must not create a canonical finding by itself.

### Rejecting a clue

Set `status: rejected` when the direction should not be pursued. Add a concise `## Research disposition` with the decisive reason.

If the rejection itself satisfies the research-watch substantive-finding gate — for example a reusable impossibility theorem or a material prior-art redirect — also persist the corresponding durable finding normally and link it from the clue. If rejection is merely duplicate/out-of-scope/malformed, do not manufacture a finding.

### Resolving a clue

Set `status: resolved` when research has produced a durable accepted outcome under the normal finding gate. Add:

```text
## Research disposition
Outcome: supported | narrowed | classical | refuted

Resolved by:
- [[research/<line>/findings/<finding>]]
```

The linked finding, not the clue, is the mathematical evidence.

## Ownership extension

When this skill is explicitly loaded with one of the caller skills, it extends writable paths only as follows:

### Mind

May additionally create or update `proposed` clues under:

```text
research/<discovered-line>/clues/**
research/clues/**
```

It may not change Research Watch disposition states.

### Graph Curator

May additionally create or update `proposed` clues under:

```text
research/<research-line>/clues/**
research/clues/**
```

It may not change Research Watch disposition states.

### Research Watch for `<line>`

May additionally read and update only:

```text
research/<line>/clues/**
```

It must not modify another line's clues or `research/clues/**`.

This exception does not grant access to any other caller-forbidden path.

## Publication and no-churn gate

A clue change may share the caller's normal direct-main publication path when all of these hold:

- every clue path is allowed for that caller above;
- the clue is materially new, materially better grounded, or its Research Watch disposition changed;
- no timestamps/run logs/status noise were added;
- the source revision remains coherent;
- the caller's normal diff review and publication gates pass.

Use the caller's normal commit prefix. Do not create a commit solely to restate an unchanged clue.

## Reporting

Mind or Curator should notify only when a clue is unusually consequential or when it represents a genuinely new cross-line/new-line candidate worth user attention. Routine local clue creation can remain silent.

Research Watch should report a clue only when it is accepted, rejected for a substantive mathematical reason, or resolved into a material finding under its normal notification policy.
