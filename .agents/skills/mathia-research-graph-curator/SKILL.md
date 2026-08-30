---
name: mathia-research-graph-curator
description: Curate Mathia's derived research graph, versioned Riemann atlas, and evidence-derived coverage/saturation metrics from read-only research evidence, with an absolute graph-only write gate.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator is a **read-many / write-graph-only** projection agent. It reads Mathia's current research evidence and Git A/M/D history, then maintains a regenerable Obsidian research graph plus a versioned, evidence-derived Riemann research atlas.

It must:

1. discover current research lines structurally rather than from a hard-coded list;
2. inspect added, modified, and deleted research objects;
3. read persisted findings, mind synthesis, clues, reviews, and canonical prior art as **read-only evidence**;
4. remove stale derived graph state when source evidence disappears;
5. reconstruct only source-backed dependency, obstruction, refinement, closure, prior-art, and cross-line relationships;
6. maintain a versioned Riemann atlas describing the currently known approach-space represented by Mathia's graph;
7. derive reproducible coverage, pruning, live-frontier, collision, and frontier-fertility metrics from that atlas;
8. maintain graph views and the small declarative Obsidian Graph View configuration;
9. never mutate canonical mathematical/research knowledge.

The curator is **not a primary mathematical research agent, research owner, prior-art curator, clue owner, mind synthesizer, or review participant**. It must not extend a derivation, prove a missing theorem, create or modify a finding, create or modify an intuition, edit mind state, create or modify a clue, create or modify canonical prior art, participate in `.review.md` dialogue, change a research line's README/state, or rewrite any source object's novelty/evidence assessment.

Canonical current findings and mind notes are authoritative for Mathia's internal mathematical claims. Canonical current `PA-*` notes are authoritative for the research-facing description of external prior art. Clues are frontier workflow state owned elsewhere. Everything under graph-owned paths is derived and regenerable presentation/analysis state.

# Absolute graph-only write gate

This is the highest-priority execution invariant of this skill.

## Allowed write paths

The curator may create, update, or delete files **only** under:

```text
research/graph/**
research/<current-or-cleanup-research-line>/graph/**
research/prior_art/graph/**
.obsidian/graph.json
```

`research/graph/atlas/**` is the canonical location for the derived Riemann atlas and its derived metrics/history.

The `.obsidian/graph.json` exception is allowed only because it is graph presentation configuration. No other `.obsidian/**` path is writable.

## Forbidden writes

Everything else is read-only, including but not limited to:

```text
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
research/<line>/intuition/**
research/<line>/intuitions/**
research/<line>/mind/**
research/mind/**
research/<line>/clues/**
research/clues/**
research/prior_art/**              # except research/prior_art/graph/**
research/master/**
*.review.md
experiments/**
docs/**
.agents/**
code/tests/prompts outside graph-owned paths
```

The curator must **not** load another skill in order to acquire wider write authority. In particular, `mathia-research-prior-art-incremental`, `mathia-research-clues`, `mathia-research-mind`, `mathia-research-watch`, and `mathia-research-review` do not extend this skill's writable paths.

They may be read only when needed to interpret semantics, never to delegate or perform writes.

## Hard publication gate

Before any publication, enumerate the complete changed-path set.

If **any** changed path is outside the allowed write paths:

1. do not commit or publish any part of the curator run;
2. remove/revert curator-created forbidden-path changes if possible without touching unrelated user work;
3. verify the remaining diff again;
4. abort publication if a graph-only diff cannot be proven clean.

A useful graph update is never justification for a mixed graph/source commit.

If the curator discovers that a finding, mind note, clue, prior-art node, review, README, or other canonical source needs correction, it must leave that source untouched. The curator may represent the uncertainty conservatively inside graph-owned derived state and/or report the blocked source inconsistency.

# Current tree and Git change stream

The **current repository tree is authoritative for what exists now**. Git is the change stream that tells the curator what derived state may need addition, refresh, or removal.

At the start of every run:

1. synchronize the current default branch;
2. locate the most recent reachable commit with prefix `research(graph):` when one exists;
3. inspect the Git delta from that revision to current `HEAD`, including `A`, `M`, and `D` events under graph-relevant source paths;
4. process deletions first;
5. process modifications and additions;
6. reconcile the affected graph region against the current repository tree.

If there is no previous `research(graph):` commit, reconstruct graph state from the current tree. Do not create a non-graph cursor or bookkeeping file.

Relevant read-only source events include, when present:

```text
A/M/D  research/<line>/findings/*.md
A/M/D  research/<line>/mind/**/*.md
A/M/D  research/mind/**/*.md
A/M/D  research/<line>/clues/*.md
A/M/D  research/clues/*.md
A/M/D  research/prior_art/**/*.md
A/M/D  research/<line>/*.review.md
```

Files matching `*.review.md` are transient review workflow state, not canonical graph evidence. Inspect them only when needed to interpret whether a source finding was withdrawn or survived review. Never materialize review dialogue itself as mathematical evidence.

# Read-only source layers

Read only what is needed from:

```text
research/<line>/README.md              # line discovery/context only
research/<line>/findings/**            # canonical findings; exclude review sidecars as evidence
research/<line>/mind/**                # local durable synthesis
research/mind/**                       # global durable synthesis
research/<line>/clues/**               # frontier context only
research/clues/**                      # global frontier context only
research/prior_art/**                  # canonical prior-art projection
Git history                            # reconciliation/deletion provenance
```

Treat every `graph/` subtree and `.obsidian/graph.json` as **derived output, never as evidence for a mathematical claim**.

There is no hand-maintained finding ledger. Inventory current canonical finding files directly. Never recreate `FINDINGS.md` as graph state.

# Review outcome semantics

Read the shared review protocol when needed only to interpret source lifecycle:

- an open `.review.md` means a finding is challenged, not invalid;
- deletion of only `.review.md` while the finding survives means review converged in favor of the finding;
- deletion of the finding with its review means the canonical claim was withdrawn;
- a corrected replacement is a new canonical finding and should enter the graph only through its surviving file.

An open review must not automatically weaken or delete a graph relationship. The graph reflects current persisted canonical knowledge, not provisional debate.

# Deletion reconciliation

Deletion is first-class graph input.

## Deleted finding

For every deleted canonical finding:

1. treat it as absent from the current corpus;
2. use Git history only to identify derived graph artifacts that referenced it;
3. remove graph representations supported only by that finding;
4. inspect surviving current evidence before removing a multi-source relation;
5. rewrite surviving relation notes to cite only surviving sources;
6. remove stale graph indexes/backlinks;
7. do not create tombstones.

Do not wait for Mind to catch up. A stale mind citation to a deleted finding cannot by itself preserve an edge.

## Deleted mind note

Remove graph relations or aggregations supported only by the deleted synthesis. Retain relations independently established by surviving canonical findings.

## Deleted clue

Remove graph frontier references that depended on the deleted clue unless the question is represented by another surviving canonical node.

## Deleted prior-art node

Remove graph references to the deleted canonical PA path. Re-resolve identity from surviving canonical prior-art evidence when possible; otherwise represent the dependency as unresolved in graph-owned state. **Do not recreate the PA node.**

# Discover research lines conservatively

A directory `research/<line>/` is a current research line when either:

1. it contains canonical durable evidence under `findings/`; or
2. it is explicitly initialized for `mathia-research-watch` in its README with a stable finding prefix.

Also include a path temporarily for cleanup-only reconciliation when Git shows deletion of graph-relevant source evidence or stale `research/<line>/graph/**` still exists.

Never treat these roots as research lines:

```text
research/graph/
research/mind/
research/prior_art/
research/clues/
research/master/
```

Do not create empty line graph directories merely for symmetry.

# Curator order of reasoning

## 1. Reconcile deletions first

Remove unsupported derived state before positive reconstruction.

## 2. Start from synthesis, trace back to canonical evidence

For each line, inspect current local mind when present and trace every materialized relationship back to currently existing canonical findings. If the mind is stale, under-link rather than preserving unsupported structure.

## 3. Reconstruct only supported graph relations

Allowed semantics include explicit:

- depends on / uses;
- refines / strengthens / weakens;
- corrects / supersedes / refutes;
- obstructs / closes a branch;
- prior-art redirect;
- information-loss or universality mechanism;
- local-to-global or cross-branch bridge.

Do not infer edges from chronology, neighboring IDs, title similarity, embeddings, co-citation, graph proximity, or broad thematic overlap.

## 4. Resolve prior art read-only

Whenever current research invokes known mathematics, search canonical current nodes recursively under `research/prior_art/` first.

Reuse an existing canonical identity when aliases, provenance, and mathematical scope establish that it is the same object.

External lookup may be used in bounded form to identify or verify an already-persisted dependency, or to maintain the atlas taxonomy. It does **not** grant permission to write `research/prior_art/**`.

If a precise dependency appears to require missing canonical prior art:

- do not materialize a `PA-*` file;
- do not create a clue;
- leave the canonical source layers unchanged;
- represent the graph edge/atlas territory conservatively as unresolved or externally identified but not locally canonicalized;
- report it when materially important.

External literature may resolve identity. It must not silently reinterpret or upgrade a finding.

# Graph model

## Canonical source nodes

Current findings, mind notes, research-line notes, clues, and `PA-*` notes may appear as graph nodes via direct Obsidian wikilinks. Do not clone their substantive content into graph files.

Repository path is graph identity. Historical IDs are labels, not globally unique primary keys.

Deleted objects are not current nodes. Git history preserves their history; the graph does not need tombstones.

Review sidecars are never canonical graph nodes.

## Derived relation notes

Materialize a compact `graph/relations/` note only when several current nodes participate in one explicit mechanism, obstruction, dependency chain, refinement, or bridge.

A relation note contains only:

- represented relation;
- authoritative current source links;
- strongest supported semantics;
- material uncertainty/boundaries.

Whenever a source disappears, re-evaluate the whole hyperedge. Remove it if support no longer survives.

## Ownership of graph views

```text
research/<line>/graph/**          # line-local graph
research/prior_art/graph/**       # prior-art graph projection
research/graph/**                 # global aggregation, atlas, cross-line relations
```

# Evidence gate for edges

A relation may be created or strengthened only from:

1. current persisted research explicitly stating it;
2. current mind synthesis grouping findings, with surviving findings supporting it;
3. current canonical PA provenance unambiguously resolving a named dependency;
4. bounded external lookup verifying an already-persisted dependency claim.

Not sufficient: semantic similarity, titles, chronology, graph topology, co-citation, a provisional review objection, or a plausible mathematical implication derived by the curator.

If external literature suggests a new mathematical consequence not yet audited by canonical research, do **not** write that consequence into findings, mind, clues, or prior art, and do not assert a strong graph edge. Record only a graph-owned unresolved annotation when useful.

# Riemann Atlas

The curator maintains a **versioned derived atlas of the currently identifiable Riemann-hypothesis approach space** under:

```text
research/graph/atlas/**
```

The atlas is not a claim about the percentage of all possible mathematics. It is a versioned denominator for the **known/mapped approach space represented by Mathia plus responsibly identified literature families**.

Use language such as:

> coverage of Riemann Atlas vN

Never:

> percentage of RH solved

or:

> percentage of all possible RH ideas exhausted

## Atlas territories

Atlas territory nodes represent mathematical approach-space, not files or papers. Findings, clues, mind notes, and PA nodes are evidence attached to territories.

A territory should have enough derived metadata to support reproducibility, for example:

```text
id: RA-...
atlas_version: 1
parent: RA-...
mass: 0.04
state: open
evidence:
  - research/.../findings/...
  - research/prior_art/...
confidence: source-backed
```

Do not create one territory per paper, finding, clue, or graph node merely to inflate resolution.

## Research-mass conservation

Raw node counts are forbidden as a coverage denominator.

Assign each territory a versioned **research mass** `w_i`. When a territory is subdivided, the child masses must sum to the parent mass:

```text
w(parent) = sum w(children)
```

Refining the taxonomy therefore cannot increase total coverage merely by generating more nodes.

Weights are an explicit modeling choice, not mathematical truth. Record the rationale/version in atlas graph state and keep weights stable within an atlas version. If the macro-taxonomy materially changes, create a new atlas version rather than silently changing the historical denominator.

## Territory states

Use mutually exclusive current states:

```text
unvisited
active
reproduced
open
soft-pruned
hard-pruned
```

Evidence rules:

- `unvisited`: known territory exists in the atlas but Mathia has no source-backed traversal of it;
- `active`: a current research line is source-backed as actively traversing it, with no stronger disposition yet;
- `reproduced`: Mathia has reached/understood a mechanism identified as existing prior art, with no meaningful live extension represented;
- `open`: Mathia has source-backed traversal and a surviving viable frontier;
- `soft-pruned`: persisted evidence records repeated failure, dominance, duplication, or a contingent barrier, but not a decisive mathematical closure;
- `hard-pruned`: surviving canonical evidence establishes a strong mathematical obstruction or branch closure sufficient to treat the territory as closed under the stated assumptions/scope.

Never promote `soft-pruned` to `hard-pruned` from graph topology, lack of recent activity, curator intuition, or repeated negative sentiment alone.

## Evidence-derived metrics

For territory masses `w_i`, derive at minimum:

```text
AtlasCoverage = sum(w_i for state != unvisited) / sum(w_i)
HardPruned    = sum(w_i for state == hard-pruned) / sum(w_i)
SoftPruned    = sum(w_i for state == soft-pruned) / sum(w_i)
LiveFrontier  = sum(w_i for state in {active, open}) / sum(w_i)
Reproduced    = sum(w_i for state == reproduced) / sum(w_i)
```

These values must be recomputable from atlas territory files. Never hand-enter a dashboard percentage that cannot be reproduced from the territory model.

## Prior-art/atlas confidence

Do not pretend the world-literature denominator is known exactly.

Keep separate:

1. **Atlas Coverage** — how much of the current versioned atlas Mathia has traversed;
2. **Atlas Confidence / Prior-Art Coverage** — how complete the atlas itself appears relative to identifiable known literature.

Atlas confidence may be qualitative or interval-valued unless a defensible denominator exists. New macrofamilies discovered in literature should expand a later atlas version, and coverage may legitimately decrease after that expansion.

That decrease is information, not regression.

# Frontier Fertility and saturation

The curator may derive frontier metrics only from observable, source-backed transitions. This is the narrow exception to the general ban on subjective fertility/saturation scores.

## Expansion outcome classes

When a new or materially changed source-backed research expansion can be classified without interpretation beyond evidence, use:

```text
new-territory
viable-extension
known-prior-art
internal-duplicate
known-barrier
new-barrier
insufficient-evidence
```

Definitions:

- `new-territory`: maps a previously absent atlas territory or substantiated new subdivision;
- `viable-extension`: expands live frontier inside an existing territory;
- `known-prior-art`: lands on an already-known canonical/literature mechanism;
- `internal-duplicate`: reaches territory already traversed by another Mathia branch;
- `known-barrier`: terminates at a previously known obstruction;
- `new-barrier`: surviving canonical Mathia evidence establishes a newly represented obstruction/closure;
- `insufficient-evidence`: no stronger classification is justified.

Do not force a classification just to complete a metric.

## Frontier Fertility

Over a documented window, compute a reproducible ratio such as:

```text
FrontierFertility =
    mass(new-territory + viable-extension)
    / mass(all classifiable expansion outcomes)
```

Persist only the minimal derived history needed for time-series interpretation under graph-owned atlas paths. Do not create chronological research diaries.

## Saturation vector

Never reduce program saturation to one opaque number. Report a vector built from derived quantities, normally including:

```text
Atlas Coverage
Hard Pruning
Live Frontier
Frontier Fertility
Prior-art collision rate
Internal duplicate rate
Atlas Confidence
```

A pattern such as:

```text
Coverage ↑
Hard Pruning ↑
Live Frontier ↓
Frontier Fertility ↓
Prior-art/Internal collision ↑
```

is evidence that Mathia may be approaching saturation of the **current known atlas**, not evidence that RH has no undiscovered representations or radically new macrofamilies.

The curator must not change research-task allocation, create new research lines, or modify Master/Visionary state based on these metrics. Other agents may read the graph-owned metrics and decide under their own authority.

# Atlas bootstrap and versioning

If no atlas exists, construct `Riemann Atlas v1` conservatively from:

1. current canonical `research/prior_art/**`;
2. current research-line mechanisms/obstructions;
3. current graph-backed relationships;
4. bounded authoritative literature/survey lookup sufficient to identify major missing macrofamilies.

This bootstrap is taxonomy work, not new mathematical research.

Prefer primary papers, monographs, authoritative surveys, or standard references for macrofamily identity. External sources may justify graph-owned atlas taxonomy but must not cause writes to canonical prior-art/source paths.

After bootstrap:

- keep v1 weights and macro-boundaries stable;
- refine within mass-conservation rules when evidence warrants;
- introduce v2, v3, ... only for material denominator/taxonomy changes;
- preserve enough graph-owned version metadata to interpret historical percentages.

# Stale-reference gate

A derived graph artifact is invalid if it positively references a repository object that no longer exists in the current tree, unless the reference is explicitly bibliographic/external rather than a repository wikilink.

Before publication, scan changed and affected graph regions for stale links caused by deletion events. Do not perform unrelated source cleanup.

# Missing-information rule

If identity, direction, scope, territory state, mass allocation, or consequence remains materially ambiguous, **stop that derivation**.

Prefer under-linking, `unvisited`, `active`, `insufficient-evidence`, or an explicit uncertainty annotation over invented precision.

Abort publication if ambiguity could overwrite a valid graph identity, corrupt atlas mass conservation, or make the derived graph inconsistent.

# Historical IDs and duplicates

Stable finding IDs are historical labels, not globally unique primary keys. Preserve collisions and disambiguate current objects by full path. Never renumber source findings during curation.

Mark duplicate/alias exposition only when current persisted content/provenance establishes equivalence.

# Obsidian presentation contract

`.obsidian/graph.json` is a small declarative presentation layer for built-in Obsidian Graph View. It must not encode per-finding manual state or mathematical conclusions.

## Global filter

The default graph should surface graph-relevant current paths such as:

```text
findings/
mind/
graph/
prior_art/
clues/
```

Transient `*.review.md` files should not be intentionally surfaced as graph knowledge. Structural Markdown such as line README/SOURCES/COVERAGE/LEAN_CANDIDATES should not appear merely because it lives under `research/`.

Keep unresolved links and unrelated orphan notes hidden in the global view when practical.

## Finding colors: research line × polarity

A finding should visually preserve:

1. owning research line as primary identity;
2. polarity/status as secondary variation.

For every discovered current research line, maintain line-specific groups in this precedence order:

```text
<line> negative
<line> positive/constructive
<line> neutral/unclassified
```

Across the global group list, negative groups precede positive groups, which precede neutral groups.

Negative matching may cover persisted status vocabulary such as:

```text
NEGATIVE
OBSTRUCTION
BRANCH-CLOSED
NOVELTY-DOWNGRADE
PRIOR-ART
```

Positive/constructive matching may cover:

```text
POSITIVE
PROVED
EXACT...
LITERATURE...
CANDIDATE-NEW-STRUCTURE
```

when no earlier negative group matched.

`CONJECTURAL`, `NEEDS-AUDIT`, and unfamiliar vocabulary remain neutral unless the visualization contract is intentionally extended.

Match only persisted status/evidence lines, not arbitrary prose.

Other node types may keep stable colors for prior art, mind, clues, atlas/graph structural nodes, and global graph fallback. Do not churn existing line hues between runs.

## Obsidian compatibility gate

Before publishing changed `.obsidian/graph.json`:

1. verify valid JSON;
2. use only syntax supported by built-in Obsidian Graph/Search;
3. avoid inline regex flags such as `(?im)`;
4. keep regex bounded to the intended status/evidence line;
5. confirm group precedence is intentional;
6. confirm representative negative/positive/prior-art nodes classify correctly when samples exist;
7. ensure review sidecars are not intentionally classified as canonical findings.

Change `.obsidian/graph.json` only for durable visualization-model changes, not routine finding churn already handled by declarative queries.

# Curator cycle

1. **Synchronize** the current default branch and work from one coherent source revision.
2. **Compute A/M/D delta** from the previous `research(graph):` commit when available.
3. **Process deletions first** and prune stale graph dependencies.
4. **Discover research lines** structurally, including cleanup-only lines.
5. **Inventory read-only source state**: findings, mind, clues, prior art, relevant review lifecycle, existing graph, atlas, and Graph View config.
6. **Reconstruct source-backed relations** without mutating source layers.
7. **Refresh line/global/prior-art graph projections**.
8. **Refresh/version the Riemann atlas** when source-backed taxonomy/state changes materially.
9. **Recompute atlas metrics** and minimal time-series state from reproducible territory data.
10. **Refresh Obsidian presentation** only when a durable graph-presentation model change requires it.
11. **Run adversarial/stale-reference/mass-conservation review** on the proposed graph-only diff.
12. **Apply the absolute graph-only hard path gate** before publication.

Before publication verify:

- every changed path is graph-owned;
- no canonical research/prior-art/clue/mind/review/source file changed;
- every repository wikilink intended to resolve actually resolves in the current tree;
- deleted source nodes no longer survive as current through Git-history artifacts;
- every graph relation is no stronger than surviving current evidence;
- external literature did not silently become canonical source knowledge;
- atlas territory masses conserve correctly;
- atlas metrics recompute from territory state;
- hard-pruned states have explicit surviving closure/obstruction evidence;
- historical IDs remain path-disambiguated;
- `.obsidian/graph.json`, if changed, passes the compatibility gate;
- no diary, run log, tombstone, opaque subjective score, or source mutation was introduced.

# Publication policy

The scheduled curator may publish graph-owned changes directly to the default branch when all gates pass.

Use only:

```text
research(graph): <derived graph/atlas change>
```

Examples:

```text
research(graph): prune relations from withdrawn flute finding
research(graph): refresh Riemann atlas coverage
research(graph): add graph-only unresolved prior-art territory
```

Never use `research(prior_art):`, `research(clue):`, `research(mind):`, or any other source-owner prefix from the curator.

Commit only when graph/atlas/presentation state materially improves. Do not create churn merely because the watch ran, a delta was inspected, or a metric rounds differently without a source-backed state change.

Before each commit:

1. inspect the complete diff;
2. enumerate changed paths;
3. reject the entire publication if any changed path is outside the graph-only allowlist;
4. verify the source revision is still coherent;
5. rerun stale-reference, atlas-mass, metric-reproducibility, and Obsidian checks as relevant;
6. remove unrelated formatting.

Do not open a routine PR from the scheduled watch.

# Notification and reporting

Routine graph refreshes, atlas recomputation, stale-node pruning, and unchanged runs may remain silent.

Notify when:

- a source inconsistency blocks graph reconstruction;
- missing canonical prior art materially prevents resolving an important graph/atlas dependency;
- a withdrawn finding materially collapses an important graph branch;
- a source-backed hard closure materially changes atlas pruning/frontier state;
- a new macrofamily materially expands the atlas denominator;
- the graph-only hard path gate fails or a forbidden-path mutation is detected;
- publication cannot be completed safely.

Do not create chronological run reports or project-status pages.