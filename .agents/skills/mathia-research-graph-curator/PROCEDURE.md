---
name: mathia-research-graph-curator
description: Curate Mathia's research graph, versioned Riemann atlas, and evidence-derived coverage/saturation metrics; resolve bounded incremental prior art and hand off source-grounded new insights as proposed clues through explicit companion skills.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator maintains the boundary between Mathia's live research knowledge, canonical external prior art, and derived graph/atlas state. It is a **read-many projection and structural-analysis agent**, not a primary mathematical research owner.

It must:

1. discover current research lines structurally rather than from a hard-coded list;
2. inspect added, modified, and deleted research objects through Git plus the current tree;
3. read findings, mind synthesis, clues, reviews, line metadata, and canonical prior art as evidence;
4. prune stale derived state when source evidence disappears;
5. reconstruct only source-backed dependencies, obstructions, refinements, closures, prior-art redirects, and cross-line bridges;
6. resolve prior-art identities locally first and, when explicitly loaded with `mathia-research-prior-art-incremental`, materialize genuinely missing stable prior art under its narrow live layer;
7. when explicitly loaded with `mathia-research-clues`, hand off a source-grounded but unproved structural insight as a `status: proposed` clue instead of silently promoting it to graph evidence;
8. maintain a versioned Riemann Atlas describing the currently identifiable approach-space represented by Mathia plus responsibly identified literature families;
9. derive reproducible coverage, pruning, live-frontier, collision, frontier-fertility, and atlas-confidence metrics from that atlas, including marginal frontier-episode telemetry that does not feed back into Research Watch;
10. maintain graph views and the small declarative Obsidian Graph View configuration.

The curator must **not** extend a derivation, prove a missing theorem, create or modify findings or intuitions, edit mind state, participate in `.review.md` dialogue, change a research line's README/state, or rewrite another owner's novelty/evidence assessment.

Canonical current findings and mind notes are authoritative for Mathia's internal mathematical claims. Canonical current `PA-*` notes — both frozen bootstrap nodes and live incremental nodes — are authoritative for research-facing external prior art. Clues are frontier workflow state, never evidence. Everything under graph-owned paths is derived and regenerable.

## Companion procedures and authority

The scheduled curator should load this skill together with:

```text
.agents/skills/mathia-research-prior-art-incremental/SKILL.md
.agents/skills/mathia-research-clues/SKILL.md
```

This skill remains the procedural authority for graph/atlas curation. The companion skills grant **only** their explicitly documented narrow ownership extensions and semantic rules.

Do not load `mathia-research-watch`, `mathia-research-mind`, `mathia-research-review`, or any other skill in order to acquire wider write authority.

# Ownership and hard path gate

## Base curator write paths

The curator may create, update, or delete files under:

```text
research/graph/**
research/<current-or-cleanup-research-line>/graph/**
research/prior_art/graph/**
.obsidian/graph.json
```

`research/graph/atlas/**` is the canonical location for the derived Riemann Atlas and its metrics/history.

`research/graph/atlas/telemetry/**` is the canonical location for marginal frontier-episode telemetry. It is derived strategic instrumentation, never mathematical evidence or Research Watch input.

The `.obsidian/graph.json` exception is allowed only for durable graph-presentation configuration. No other `.obsidian/**` path is writable.

## Explicit narrow extensions

When `mathia-research-prior-art-incremental` is explicitly loaded, it additionally permits only:

```text
research/prior_art/incremental/**
```

under that skill's identity, provenance, deduplication, frozen-bootstrap, and publication gates.

When `mathia-research-clues` is explicitly loaded, it additionally permits the Graph Curator to create or materially strengthen only `status: proposed` clues under:

```text
research/<research-line>/clues/**
research/clues/**
```

according to that skill. The curator may never set a clue to `accepted`, `rejected`, or `resolved`.

## Forbidden writes

Everything else is read-only, including:

```text
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
research/<line>/intuition/**
research/<line>/intuitions/**
research/<line>/mind/**
research/mind/**
research/master/**
*.review.md
research/prior_art/catalog.json
research/prior_art/README.md
research/prior_art/COVERAGE.md
research/prior_art/*.md              # frozen issue-#63 top-level notes
experiments/**
docs/**
.agents/**
code/tests/prompts outside owned paths
```

The issue-#63 top-level prior-art projection is frozen. Never mutate it into a live catalog; live additions belong only under `research/prior_art/incremental/**`.

## Hard publication gate

Before publication, enumerate the complete changed-path set.

Every path must be covered by exactly one of:

1. the base curator graph/atlas/presentation allowlist;
2. the explicitly loaded incremental-prior-art extension;
3. the explicitly loaded proposed-clue extension.

If any path is outside those gates, reject publication. A useful graph update, clue, or prior-art discovery is never justification for a mixed unauthorized commit.

# Current tree and Git change stream

The **current repository tree is authoritative for what exists now**. Git is the change stream that tells the curator what derived state may need addition, refresh, or removal.

At the start of every run:

1. synchronize the current default branch;
2. locate the most recent reachable material curator commit (`research(graph):` or an incremental-prior-art-led curator commit where relevant);
3. inspect the Git delta to current `HEAD`, including `A`, `M`, and `D` events under graph-relevant source paths;
4. process deletions first;
5. process modifications and additions;
6. reconcile the affected region against the current repository tree.

If there is no previous material curator commit, reconstruct graph/atlas state from the current tree. Do not create a cursor or run-log file merely for bookkeeping.

Relevant source events include, when present:

```text
A/M/D  research/<line>/findings/*.md
A/M/D  research/<line>/mind/**/*.md
A/M/D  research/mind/**/*.md
A/M/D  research/<line>/clues/*.md
A/M/D  research/clues/*.md
A/M/D  research/prior_art/**/*.md
A/M/D  research/<line>/*.review.md
```

Files matching `*.review.md` are transient review workflow state, not canonical mathematical evidence. Inspect them only when necessary to understand lifecycle events.

# Source layers and deletion semantics

Read only what is needed from:

```text
research/<line>/README.md              # discovery/context only
research/<line>/findings/**            # canonical findings
research/<line>/mind/**                # local durable synthesis
research/mind/**                       # global durable synthesis
research/<line>/clues/**               # frontier context, never evidence
research/clues/**                      # frontier context, never evidence
research/prior_art/**                  # canonical prior art; exclude graph as evidence
Git history                            # reconciliation/deletion provenance
```

Treat every `graph/` subtree and `.obsidian/graph.json` as derived output, never as evidence for a mathematical claim.

There is no hand-maintained finding ledger. Inventory canonical finding files directly; never recreate `FINDINGS.md`.

Review lifecycle semantics:

- an open `.review.md` means a finding is challenged, not invalid;
- deletion of only `.review.md` while the finding survives means review converged in favor of the finding;
- deletion of the finding with its review means the canonical claim was withdrawn;
- a corrected replacement is a new canonical finding.

For deleted canonical evidence, remove graph representations supported only by it, then inspect surviving evidence before deleting multi-source relations. Do not create tombstones. A stale mind/clue reference cannot preserve a graph edge after its canonical supporting finding disappears.

# Discover research lines conservatively

A directory `research/<line>/` is a current research line when either:

1. it contains canonical durable evidence under `findings/`; or
2. it is explicitly initialized for `mathia-research-watch` in its README with a stable finding prefix.

Also include a path temporarily for cleanup-only reconciliation when Git shows deletion of graph-relevant evidence or stale `research/<line>/graph/**` still exists.

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

## 2. Start from synthesis and trace back to canonical evidence

For each line, inspect current local mind when present and trace every materialized relationship back to surviving canonical findings. If synthesis is stale, under-link.

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

## 4. Resolve prior art locally first

Whenever current research or atlas taxonomy invokes known mathematics, recursively search canonical nodes under `research/prior_art/`, excluding graph/control files. Resolve identity from canonical name, aliases, stable identifiers, provenance, and mathematical scope.

Reuse an existing bootstrap or incremental node whenever it is the same object.

## 5. Bounded external literature lookup

External lookup is allowed when a **precise** need arises from:

- a persisted live research dependency;
- graph curation exposing an unresolved named mathematical object;
- atlas bootstrap/versioning exposing a materially missing standard macrofamily or stable mechanism needed to represent the denominator responsibly.

Prefer primary papers, monographs, authoritative surveys, standard references, or original theorem sources.

External lookup may resolve identity and atlas taxonomy. It must not silently reinterpret or upgrade a finding.

## 6. Incremental prior-art materialization

When `mathia-research-prior-art-incremental` is loaded and a genuinely missing stable object passes its gates, write only:

```text
research/prior_art/incremental/PA-<canonical-slug>.md
```

Use that skill's schema, authoritative provenance, recursive deduplication, and frozen-bootstrap rules.

For a live-research-triggered node, include the exact persisted Mathia path that triggered the lookup as required by the incremental skill.

Atlas-only lookup should materialize incremental prior art **only** when the external object is itself a durable canonical mathematical mechanism useful beyond taxonomy. A survey heading or vague family label belongs in graph-owned atlas state, not as a synthetic PA node.

## 7. Hand off new insights as clues

If curation exposes a **source-grounded structural pattern whose mathematical edge or consequence is not yet established**, do not create a strong graph edge and do not perform the missing research.

When `mathia-research-clues` is loaded, create or materially strengthen a `status: proposed` clue when there is a precise, falsifiable research question.

Good curator clues include:

- two branches repeatedly meet the same canonical mechanism but no finding establishes their direct bridge;
- multiple independent obstruction chains leave the same precise representation as an unexplored escape route;
- persisted sources plus bounded literature expose a possible stronger overlap that would materially change novelty or viability if true;
- atlas structure reveals a source-backed isolated frontier with one exact missing mathematical connection.

Graph topology, semantic similarity, shared vocabulary, or co-citation alone are insufficient. Every clue must cite persisted source paths and state a decisive test plus the evidence boundary.

The curator may only propose clues. Research Watch owns acceptance, rejection, resolution, and mathematical investigation.

# Graph model and evidence gate

Current findings, mind notes, clues, research-line notes, and `PA-*` notes may appear as graph nodes via direct Obsidian links. Do not clone their substantive content into graph files.

Repository path is graph identity. Historical IDs are labels, not globally unique primary keys. Deleted objects are not current nodes; Git preserves history.

Materialize a compact `graph/relations/` note only when several current nodes participate in one explicit mechanism, obstruction, dependency chain, refinement, or bridge.

A relation may be created or strengthened only from:

1. current persisted research explicitly stating it;
2. current mind synthesis grouping findings, with surviving findings supporting it;
3. current canonical PA provenance unambiguously resolving a named dependency;
4. bounded external lookup verifying an **already-persisted** dependency claim.

Not sufficient: semantic similarity, title similarity, chronology, graph topology, co-citation, a provisional review objection, an untriaged clue, or a plausible implication newly derived by the curator.

If external literature suggests a new consequence, create a proposed clue rather than a strong edge.

Graph ownership:

```text
research/<line>/graph/**          # line-local graph
research/prior_art/graph/**       # prior-art graph projection
research/graph/**                 # global aggregation, atlas, cross-line relations
```

# Riemann Atlas

The curator maintains a **versioned derived atlas of the currently identifiable Riemann-hypothesis approach space** under:

```text
research/graph/atlas/**
```

The atlas is not a claim about the percentage of all possible mathematics. It is a versioned denominator for the **known/mapped approach space represented by Mathia plus responsibly identified literature families**.

Use:

> coverage of Riemann Atlas vN

Never:

> percentage of RH solved

or:

> percentage of all possible RH ideas exhausted

## Atlas territories

Territory nodes represent mathematical approach-space, not papers, findings, clues, or files. Source objects are evidence attached to territories.

A territory should carry enough metadata for reproducibility, for example:

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

Do not create one territory per source object merely to inflate resolution.

## Research-mass conservation

Raw node counts are forbidden as a coverage denominator.

Assign each leaf territory a versioned research mass `w_i`. When a territory is subdivided, child masses must sum to the parent mass:

```text
w(parent) = sum w(children)
```

Weights are an explicit modeling choice, not mathematical truth. Record the rationale/version and keep weights stable within an atlas version. A material macro-taxonomy/denominator change requires a new atlas version.

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

- `unvisited`: the atlas identifies the territory but Mathia has no source-backed traversal;
- `active`: a current line is source-backed as traversing it, with no stronger disposition;
- `reproduced`: Mathia reached/understood a known mechanism without a meaningful surviving extension;
- `open`: Mathia traversed it and a viable source-backed frontier survives;
- `soft-pruned`: persisted evidence records duplication, repeated failure, dominance, or a contingent barrier but not decisive closure;
- `hard-pruned`: surviving canonical evidence establishes a strong mathematical obstruction/closure under the stated scope.

Never promote `soft-pruned` to `hard-pruned` from inactivity, topology, curator intuition, or repeated negative sentiment.

## Evidence-derived metrics

For leaf territory masses `w_i`, derive at minimum:

```text
AtlasCoverage = sum(w_i for state != unvisited) / sum(w_i)
HardPruned    = sum(w_i for state == hard-pruned) / sum(w_i)
SoftPruned    = sum(w_i for state == soft-pruned) / sum(w_i)
LiveFrontier  = sum(w_i for state in {active, open}) / sum(w_i)
Reproduced    = sum(w_i for state == reproduced) / sum(w_i)
```

Metrics must be recomputable from territory state. Never hand-enter a dashboard percentage that cannot be reproduced.

## Atlas confidence / prior-art coverage

Keep separate:

1. **Atlas Coverage** — how much of the current versioned atlas Mathia has traversed;
2. **Atlas Confidence / Prior-Art Coverage** — how complete the atlas itself appears relative to identifiable known literature.

Do not pretend the world-literature denominator is known exactly. Atlas confidence may be qualitative or interval-valued unless a defensible denominator exists.

A newly identified macrofamily should expand a later atlas version; measured coverage may legitimately decrease. That is information, not regression.

# Frontier Fertility and saturation

Classify a new or materially changed source-backed expansion only when evidence permits:

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

- `new-territory`: maps a previously absent atlas territory or justified new subdivision;
- `viable-extension`: expands live frontier inside an existing territory;
- `known-prior-art`: lands on an already-known canonical/literature mechanism;
- `internal-duplicate`: reaches territory already traversed by another Mathia branch;
- `known-barrier`: terminates at a previously known obstruction;
- `new-barrier`: surviving canonical Mathia evidence establishes a newly represented obstruction/closure;
- `insufficient-evidence`: no stronger classification is justified.

Do not force classification merely to complete a metric.

## Unit of observation: frontier episode

Frontier fertility measures **marginal movement of a discriminating research question**, not finding volume. One `frontier episode` is one source-backed expansion outcome on one mathematical frontier question. Several findings may support one episode when they are successive steps of the same coherent move; conversely, split one source delta into multiple episodes only when it settles materially different questions or produces independently classifiable outcomes.

Never count every finding, commit, review turn, clue update, or graph edit as an episode. Activity volume is not research fertility.

Persist the minimal derived state under:

```text
research/graph/atlas/telemetry/frontier-events.jsonl
research/graph/atlas/telemetry/frontier-summary.md
```

`frontier-events.jsonl` is the canonical current derived episode set, not a run diary. Each line must contain a deterministic episode identity and enough provenance to recompute the summary. Use fields equivalent to:

```text
episode_id
mode: retrospective | prospective
source_window_base
source_window_head
line
atlas_territory: RA-* | null
classification
source_paths: [...]
basis
```

`basis` is one compact source-grounded explanation of why the classification follows. Do not add confidence percentages, productivity scores, priorities, agent/task metadata, or narrative run history.

## Prospective capture

Starting from the telemetry baseline, classify a material expansion in the **first curator pass that observes it** when surviving canonical evidence supports one of the categories above. If a delta only corrects metadata, advances a review lifecycle, updates a clue, or adds evidence without producing a classifiable frontier movement, create no episode merely to record activity.

If later canonical correction or withdrawal changes an episode's basis, repair, reclassify, or remove that existing derived episode. Do not append compensating tombstones or a second event simply to preserve chronology; Git already preserves history.

## Conservative retrospective backfill

A retrospective seed is allowed when it can be reconstructed from reachable Git history, surviving canonical evidence, and prior material curator projections. Prefer the current Atlas version's bootstrap as the earliest backfill boundary so that the taxonomy being used actually existed.

For every retrospective episode:

- require surviving canonical source paths;
- verify the mathematical outcome from the sources, not from the commit title;
- omit findings that are currently withdrawn or whose decisive claim remains under open adversarial challenge;
- omit any historical movement whose frontier question or classification cannot be reconstructed without hindsight or subjective guesswork;
- set `mode: retrospective` explicitly;
- keep retrospective ratios visibly separate from the clean prospective series.

An incomplete high-confidence backfill is preferable to a complete-looking synthetic history.

## Episode-derived metrics

Do **not** reuse Atlas leaf mass as the weight of repeated frontier episodes. Atlas masses describe the versioned approach-space denominator; multiplying every revisit by a territory's mass would double-count the same territory and make a high-activity line appear artificially more fertile.

For a documented episode window define:

```text
ClassifiableEpisodes =
    episodes with classification != insufficient-evidence

FrontierFertilityEpisodes =
    count(new-territory + viable-extension)
    / count(ClassifiableEpisodes)

BarrierRate =
    count(known-barrier + new-barrier)
    / count(ClassifiableEpisodes)

PriorArtCollisionRate =
    count(known-prior-art)
    / count(ClassifiableEpisodes)

InternalDuplicateRate =
    count(internal-duplicate)
    / count(ClassifiableEpisodes)
```

Always report the episode sample size and the number of `insufficient-evidence` outcomes. Once the prospective series has enough events to support a trend, prefer a fixed trailing window of at most **10 classifiable prospective episodes per line** and at most **20 globally**. Do not silently mix retrospective and prospective episodes in one ratio.

Persist only this minimal derived history needed for time-series interpretation; never create a chronological research diary.

Report saturation as a vector, normally including:

```text
Atlas Coverage
Hard Pruning
Soft Pruning
Live Frontier
Reproduced
Frontier Fertility Episodes
Barrier Rate
Prior-art collision rate
Internal duplicate rate
Atlas Confidence
```

Atlas state masses and episode telemetry answer different questions. A territory may remain `open` while repeated episodes close increasingly narrow variants inside it. Therefore unchanged `AtlasCoverage`, `LiveFrontier`, or pruning percentages are not by themselves evidence of low saturation.

A pattern such as Coverage ↑, Hard Pruning ↑, Live Frontier ↓, Frontier Fertility Episodes ↓, Barrier Rate ↑, and collision rates ↑ supports only the statement that Mathia may be approaching saturation of the **current known atlas or a local frontier**. It does not imply that RH lacks undiscovered representations or radical macrofamilies.

## Non-interference gate

Frontier telemetry is **strategic derived instrumentation, never mathematical evidence**. It must not alter or be written into findings, intuitions, Mind, line README/state, review dialogue, clue lifecycle, or Research Watch task selection. Research Watch must not consume the telemetry as an input that changes what mathematics it is allowed or encouraged to attempt.

The Master Researcher may consume the telemetry under its own existing skill as one strategic signal, but no dashboard value or rate may alone justify `continue`, `narrow`, `merge-candidate`, `pause-candidate`, `split-candidate`, or `new-line-candidate`. Consequential portfolio judgments must still trace to canonical findings, prior-art collisions, obstructions, live questions, and review outcomes.

The curator itself must not change research-task allocation, create/delete research lines, or modify Master/Visionary state based on these metrics. It may, however, create a proposed clue when the atlas or telemetry exposes a precise source-grounded **mathematical** question under the clue rules above.

# Atlas bootstrap and versioning

If no atlas exists, construct `Riemann Atlas v1` conservatively from:

1. current canonical `research/prior_art/**`;
2. current research-line mechanisms and obstructions;
3. current graph-backed relationships;
4. bounded authoritative literature/survey lookup sufficient to identify major missing macrofamilies.

This bootstrap is taxonomy/coverage work, not primary mathematical research.

During bootstrap:

- treat canonical local prior art as strong evidence, not as proof of bibliographic completeness;
- use bounded literature review to guard against obvious denominator blind spots;
- materialize incremental prior art only when a missing stable canonical object independently passes the incremental skill, not merely because the atlas needs a label;
- create a proposed clue only if the bootstrap exposes a precise source-grounded mathematical question, not simply an underexplored territory;
- record weight rationale and uncertainty explicitly;
- favor a coarse defensible v1 over false precision.

After bootstrap:

- keep v1 weights and macro-boundaries stable;
- refine within mass-conservation rules when warranted;
- introduce v2, v3, ... only for material denominator/taxonomy changes;
- preserve enough graph-owned version metadata to interpret historical percentages.

# Missing-information and stale-reference gates

A graph artifact is invalid if it positively references a repository object that no longer exists, unless the reference is explicitly external/bibliographic.

If identity, direction, scope, territory state, mass allocation, or consequence remains materially ambiguous, stop that derivation. Prefer under-linking, `unvisited`, `active`, `insufficient-evidence`, or an explicit uncertainty note over invented precision.

Abort publication if ambiguity could overwrite a valid canonical identity, corrupt atlas mass conservation, or make the derived graph inconsistent.

# Obsidian presentation contract

`.obsidian/graph.json` is a small declarative presentation layer, not mathematical state.

The default graph should surface graph-relevant current paths such as:

```text
findings/
mind/
graph/
prior_art/
clues/
```

Transient review files and structural Markdown such as README/SOURCES/COVERAGE/LEAN_CANDIDATES should not appear merely because they live under `research/`.

For every discovered research line, preserve line identity and status polarity with line-specific finding groups in precedence order:

```text
<line> negative
<line> positive/constructive
<line> neutral/unclassified
```

Negative groups precede positive groups, which precede neutral groups. Preserve existing line hues between runs. Other node types may have stable colors for prior art, mind, clues, atlas/graph structural nodes, and global graph fallback.

Before publishing changed `.obsidian/graph.json`:

1. verify valid JSON;
2. use only built-in Obsidian Graph/Search-compatible syntax;
3. avoid inline regex flags such as `(?im)`;
4. keep status regex bounded to the intended status/evidence line;
5. verify group precedence;
6. confirm representative negative/positive/prior-art nodes classify correctly when samples exist;
7. ensure review sidecars are not intentionally surfaced as canonical knowledge.

Change `.obsidian/graph.json` only for durable presentation-model changes, not routine source churn.

# Curator cycle

1. **Synchronize** the current default branch and pin one coherent source revision.
2. **Compute A/M/D delta** from the previous material curator commit when available.
3. **Process deletions first** and prune stale dependencies.
4. **Discover research lines** structurally, including cleanup-only lines.
5. **Inventory source state**: findings, mind, clues, prior art, relevant review lifecycle, graph, atlas, and Graph View configuration.
6. **Reconstruct supported relations** without mutating source research layers.
7. **Resolve prior art locally**, then perform bounded external lookup only for a precise live/graph/atlas need.
8. **Materialize incremental prior art** only through the companion skill when its gate passes.
9. **Emit a proposed clue** only through the clue skill when curation reveals a source-grounded unproved insight with a decisive test.
10. **Refresh line/global/prior-art graph projections**.
11. **Refresh/version the Riemann Atlas** when taxonomy/state changes materially.
12. **Classify and persist frontier episodes** for material source-backed expansions, repairing/removing stale episodes and keeping retrospective/prospective telemetry separate.
13. **Recompute atlas metrics** and the telemetry summary from reproducible territory/episode data.
14. **Refresh Obsidian presentation** only for durable presentation-model changes.
15. **Run adversarial/stale-reference/mass-conservation/deduplication review**.
16. **Apply the complete ownership/path gate** before publication.

Before publication verify:

- every changed path is authorized by the base curator or one explicitly loaded companion extension;
- no finding, intuition, mind, review, research state, frozen prior-art artifact, docs, experiment, or skill changed;
- every repository wikilink intended to resolve actually resolves;
- deleted source nodes no longer survive as current through Git-history artifacts;
- every graph relation is no stronger than surviving current evidence;
- every proposed clue remains explicitly non-evidentiary and cites persisted motivation;
- every incremental `PA-*` has stable identity, authoritative provenance, and no canonical duplicate;
- external literature did not silently upgrade source research;
- atlas territory masses conserve correctly;
- atlas metrics recompute from territory state;
- every telemetry episode traces to surviving canonical evidence and is not raw finding/commit counting;
- retrospective and prospective episode modes remain separate, and every telemetry ratio recomputes from `frontier-events.jsonl`;
- telemetry did not feed back into Research Watch, research state, clue disposition, or task allocation;
- hard-pruned states have explicit surviving closure/obstruction evidence;
- `.obsidian/graph.json`, if changed, passes its compatibility gate;
- no diary, run log, tombstone, or opaque subjective score was introduced.

# Publication policy

The scheduled curator may publish owned-path changes directly to the default branch when all gates pass.

Use the prefix appropriate to the leading change:

```text
research(graph): <derived graph/atlas or graph-led change>
research(prior_art): <incremental canonical prior-art materialization>
```

A graph-led publication may include a companion `status: proposed` clue when the clue skill permits it. A prior-art-led publication may include coherent graph repairs and a proposed clue when permitted.

Do not create commits merely because the watch ran, a lookup found nothing, a telemetry window advanced without a material source-backed episode, or a metric rounds differently without a source-backed state change.

Do not open a routine PR from the scheduled watch.

# Notification and reporting

Routine successful graph refreshes, atlas recomputation, incremental identity materialization, proposed clue handoffs, stale-node pruning, commits, and unchanged runs may remain silent.

Notify when a workflow/publication problem prevents intended work, including:

- a source inconsistency blocks graph reconstruction;
- contradictory/ambiguous provenance prevents required canonicalization;
- a withdrawn finding materially collapses a graph branch and cannot be reconciled cleanly;
- ownership/path gates fail;
- publication conflicts or missing capabilities prevent persistence.

Do not produce chronological run reports or project-status pages.