---
name: mathia-research-graph-curator
description: Curate Mathia's research graph, resolve canonical prior art, and maintain the derived Obsidian research-graph presentation without performing new mathematical research.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator maintains the boundary between Mathia's live research knowledge, canonical external prior art, and the derived Obsidian graph presentation. Its job is to:

1. discover current research lines structurally rather than from a hard-coded list;
2. read persisted `mind/` synthesis and trace it back to authoritative findings;
3. reconstruct only source-backed dependency, obstruction, refinement, closure, and cross-line relationships;
4. resolve referenced prior art against the canonical `research/prior_art/` projection;
5. when a required prior-art object is missing, perform the bounded external lookup allowed below and materialize it through the incremental prior-art skill when loaded;
6. preserve genuinely new or unresolved mathematical consequences as research clues rather than silently changing findings;
7. maintain the derived graph views and the small declarative Obsidian Graph View configuration.

The curator is **not a primary mathematical research agent**. It must not extend a derivation, prove a missing theorem, silently upgrade evidence, create a new intuition, or rewrite a finding's novelty assessment on its own authority.

Findings and mind notes remain authoritative for Mathia's internal mathematical claims. Canonical `PA-*` notes are authoritative for the research-facing description of external prior art. Everything under `graph/` and the committed `.obsidian/graph.json` are regenerable presentation state.

## Source layers

### Internal research knowledge

Primary internal inputs are:

```text
research/<line>/README.md              # branch context when needed
research/<line>/FINDINGS.md            # compact evidence index when present
research/<line>/findings/**            # canonical detailed findings
research/<line>/mind/**                # local durable intuitions/research lines when present
research/mind/**                       # genuinely global Mathia intuitions/research lines
research/prior_art/**                  # canonical prior-art projection
research/<line>/clues/**               # optional unresolved leads when clue skill is loaded
research/clues/**                      # optional global frontier clues
```

Treat every `graph/` subtree and `.obsidian/graph.json` as derived output, never as evidence for a new mathematical claim.

### Historical prior-art bootstrap

Issue `#63` owns the one-time bulk projection from retained Mathia/qwen evidence into the top-level `research/prior_art/` bootstrap.

The recurring curator must not redo #63, rescan the full historical corpus, rebuild the bootstrap catalog, or mutate its frozen generated notes. When `.agents/skills/mathia-research-prior-art-incremental/SKILL.md` is loaded, follow it as the authority for live prior-art writes under `research/prior_art/incremental/**`.

### External literature

The recurring curator **may use web/literature search**, but only for bounded incremental prior-art resolution triggered by persisted live research.

Allowed questions include:

- what exact theorem, criterion, construction, or standard mechanism is this finding or intuition referring to?
- does an existing `PA-*` already represent the same object under another name or version?
- what stable identity, aliases, scope, limits, and bibliographic provenance are required for a missing canonical prior-art node?
- does external literature verify an already-persisted dependency or prior-art redirect?

Prefer primary papers, monographs, authoritative surveys, or original theorem sources. Search by mathematical structure and equivalent terminology, not wording alone.

Do **not** browse broadly for interesting mathematics merely because a graph region looks sparse. External search must remain anchored to a persisted finding, intuition, research line, clue, or directly adjacent prior-art identity problem.

## Discover research lines conservatively

A research line is a directory under `research/` that contains durable research evidence such as `FINDINGS.md` or `findings/`.

Do not treat these roots as research lines:

```text
research/graph/
research/mind/
research/prior_art/
research/clues/
```

If a new legitimate research line appears and has no graph directory yet, the curator may create:

```text
research/<line>/graph/index.md
research/<line>/graph/relations/**
```

Do not create empty graph directories merely for symmetry.

## Curator order of reasoning

### 1. Start from local mind, then trace back to evidence

For each discovered line, inspect its current `mind/` first when present. Durable intuitions and `RESEARCH_LINES.md` are the highest-density statement of what the line currently considers structurally important.

For every relation suggested by mind synthesis, trace backward into the cited findings before materializing a graph relation. Mind may organize evidence; it does not excuse missing support.

If a line has no `mind/`, work directly from its findings and compact index.

### 2. Reconstruct the dependency graph

Identify only relations explicit or mechanically recoverable from persisted source knowledge, including:

- depends on / uses;
- refines / strengthens / weakens;
- corrects / supersedes / refutes;
- obstructs / closes a branch;
- prior-art redirect;
- information-loss or universality mechanism;
- explicit local-to-global or cross-branch bridge.

Do not infer edges from chronology, ID proximity, title similarity, embeddings, co-citation, graph proximity, or broad thematic overlap.

### 3. Resolve prior art locally first

Whenever a finding or intuition names, invokes, redirects to, or contrasts with known mathematics, search all canonical nodes recursively under `research/prior_art/` first.

Resolve identity from canonical name, aliases, stable identifiers, provenance, and mathematical scope. If one existing `PA-*` is an unambiguous match, reuse it.

Do not create a duplicate merely because the research note uses different terminology.

### 4. Materialize genuinely missing prior art

If the research dependency is sufficiently precise but no canonical `PA-*` exists, perform the bounded external lookup above.

Materialize a missing prior-art node only when all of these hold:

1. the trigger is tied to persisted live research or an adjacent identity problem;
2. the external mathematical object has a stable enough semantic identity;
3. authoritative sources support its description, scope, and limits;
4. recursive deduplication finds no existing canonical node;
5. the note can state the mathematics without making a stronger claim than the sources.

Canonical IDs use:

```text
PA-<deterministic-canonical-slug>
```

Prefer theorem/criterion/construction/mechanism/program/obstruction identity rather than one node per paper.

When the incremental prior-art skill is loaded, all live materialization must use its path and schema rules rather than editing the frozen #63 bootstrap.

### 5. Resolve the graph after prior-art materialization

Once a missing prior-art identity is established, connect the triggering research node to it using only the strongest relation already supported by persisted research evidence.

Critical distinction:

```text
persisted research says X depends on known object Y
    -> curator may identify/materialize Y and close that dependency edge

curator discovers externally that X may actually be classical because of Z
    -> materialize Z if justified
    -> create/strengthen a proposed clue
    -> Research Watch decides the mathematical consequence
```

External lookup may resolve identity. It must not silently rewrite the mathematical interpretation of a finding.

## Graph model

### Canonical nodes

Findings, mind notes, research-line notes, clues, and `PA-*` notes already are graph nodes. Link them with Obsidian wikilinks. Do not clone their substantive content into graph files.

Use full repository paths whenever IDs or names are ambiguous.

### Relation notes as derived hyperedges

When several canonical nodes participate in one explicit mechanism, obstruction, refinement, dependency chain, or bridge, materialize a compact relation note under the relevant `graph/relations/` directory.

A relation note should contain only:

- the represented relation;
- authoritative source links;
- the strongest semantics actually supported;
- material uncertainty or boundaries.

Do not turn graph relation notes into mathematical essays.

### Local and global ownership

```text
research/<line>/graph/**          # line-local graph
research/prior_art/graph/**       # prior-art graph
research/graph/**                 # global aggregation / cross-line relations
```

These are views over one canonical knowledge set, not duplicated knowledge bases.

## Evidence gate for graph edges

A graph relation may be created or strengthened when its semantics are supported by one of:

1. persisted research knowledge explicitly stating the relation;
2. mind synthesis explicitly grouping findings into the relation, with those findings supporting it;
3. an existing canonical prior-art node whose provenance unambiguously resolves the named dependency;
4. bounded external prior-art lookup verifying an **already-persisted dependency claim** without adding a new mathematical interpretation.

Not sufficient:

- semantic similarity;
- matching vocabulary or titles;
- chronology or neighboring IDs;
- graph topology or co-citation alone;
- a plausible implication derived by the curator;
- an external source suggesting a new overlap whose consequence has not been audited by Research Watch.

For the last case, create a clue instead of a strong edge.

## Missing-information rule

If identity, direction, scope, or mathematical consequence remains ambiguous after reasonable bounded lookup, **stop that derivation**.

Do not force canonicalization when:

- several different mathematical objects plausibly match;
- the source research note is too vague to determine the intended dependency;
- authoritative sources disagree materially on the needed scope;
- resolving the relation would require new mathematics rather than identifying prior art.

For local ambiguity, omit the edge and report or clue the exact missing information. Abort publication if ambiguity could overwrite a valid canonical identity or make the graph internally inconsistent.

## Historical IDs and duplicates

Stable finding IDs are historical labels, not globally unique primary keys. **Repository path is graph identity.**

Preserve legacy collisions and disambiguate by full path. Never renumber findings during curation.

Mark duplicate/alias expositions only when persisted content/provenance supports equivalence.

## Frontier and clues

`mind/RESEARCH_LINES.md` is authoritative for meaningful investigation lines. The graph may connect research lines to findings, intuitions, clues, and prior art only where evidence supports the relation.

Do not invent roadmaps, TODO queues, chronology, project status, or subjective novelty/fertility/saturation/importance scores.

When external prior-art resolution exposes a potentially important **new mathematical consequence**, use `mathia-research-clues` when loaded. The curator may create or strengthen only `proposed` clues; Research Watch owns acceptance, rejection, and resolution.

## Obsidian presentation contract

`.obsidian/graph.json` is a **small declarative presentation layer** for the built-in Obsidian Graph View. It is not mathematical evidence and must not encode per-finding manual state.

### Global filter

The committed global graph should show only graph-relevant research notes:

```text
findings/
mind/
graph/
prior_art/
clues/
```

Structural Markdown such as `README.md`, `FINDINGS.md`, `SOURCES.md`, `COVERAGE.md`, and `LEAN_CANDIDATES.md` should not appear merely because it lives under `research/`.

Keep unresolved links hidden and orphan notes hidden in the global view. A canonical research note that has no graph relationship should therefore not clutter the default research map.

### Color-group semantics

Obsidian gives a node one effective group color, so group order must express precedence rather than trying to encode multiple simultaneous dimensions.

Use this precedence:

1. **finding polarity/status**;
2. **canonical prior art**;
3. **mind / clues**;
4. **research-line base color** for remaining structural graph nodes;
5. global graph fallback.

The current semantic classes are:

```text
negative finding
positive/constructive finding
neutral/unclassified finding
prior art
mind
clue
research-line structural node
global structural node
```

Negative finding queries should cover persisted status vocabulary such as `NEGATIVE`, `OBSTRUCTION`, `BRANCH-CLOSED`, `NOVELTY-DOWNGRADE`, and decisive prior-art closures. Positive/constructive queries may cover vocabulary such as `POSITIVE`, `EXACT-DERIVED`, `LITERATURE+DERIVED`, and `PROVED`, but must come after the negative group so mixed-status negative findings remain visually negative.

A finding whose vocabulary does not match a stable status class falls into the neutral finding group. **Do not edit `.obsidian/graph.json` for each new finding.** Ordinary new findings must classify automatically from their path and persisted status text.

### Research-line colors

Each current research line may have a stable base-color query keyed by its path. The curator should add a new base-color group only when a **genuinely new research line** is discovered and should be visually distinguishable.

Do not churn colors between runs. Existing line colors are durable UI identity, not an optimization target.

### When the curator may modify `.obsidian/graph.json`

Only modify it for a material, durable visualization-model change, for example:

- a new research line needs a base-color group;
- a new durable node/status class is intentionally introduced;
- the default graph filter no longer matches the canonical graph-storage model;
- an Obsidian configuration change is required to keep unrelated/orphan Markdown out of the research map.

Do **not** modify it merely because:

- a finding was added;
- a finding changed status but still matches existing declarative queries;
- a relation was added or removed;
- a curator run happened.

Before changing `.obsidian/graph.json`, preserve the existing stable groups unless the graph model itself changed and verify that the configuration remains valid JSON and uses only built-in Obsidian Graph View features.

## Curator cycle

### 1. Synchronize source revision

Start from the current default branch and a clean worktree. The graph must correspond to one coherent source revision. If Research Watch or Mind output lands while curating and materially affects active nodes, refresh before publishing.

### 2. Discover and inventory

Discover current research lines. Inventory local mind/research lines, detailed findings, relevant clues, global mind, canonical prior art, existing graph relations, and the current Obsidian graph configuration.

### 3. Process each line

For each line in deterministic order:

1. read local mind/research lines when present;
2. trace cited findings;
3. reconstruct explicit dependencies/obstructions/refinements;
4. resolve referenced prior art locally;
5. perform bounded external lookup only for missing identities that matter to those relationships;
6. materialize incremental `PA-*` only when its skill gate passes;
7. update local graph relations;
8. emit clues for externally discovered consequences requiring Research Watch.

### 4. Refresh prior-art and global views

Update `research/prior_art/graph/**` from canonical prior-art relationships and `research/graph/**` from refreshed local views and genuine cross-line relations.

### 5. Refresh Obsidian presentation only if required

Check whether discovered research lines and the durable node/status model are still covered by `.obsidian/graph.json`. If yes, leave it byte-for-byte unchanged. If not, make the smallest declarative configuration update.

### 6. Adversarial consistency review

Before publication verify:

- every graph wikilink resolves;
- every new/updated `PA-*` has stable identity and authoritative provenance;
- no duplicate canonical prior-art node was introduced;
- no external result was promoted beyond its source;
- no external discovery silently changed a finding/mind evidence status;
- every graph relation is no stronger than its evidence;
- uncertain/conjectural claims were not upgraded;
- historical ID collisions remain path-disambiguated;
- local/global relation ownership is correct;
- no diary/timestamp/run log/subjective score was introduced;
- `.obsidian/graph.json`, if changed, contains only durable declarative presentation rules and no per-finding manual maintenance;
- no copyrighted full-text payload was copied.

Remove unsupported edges or presentation rules rather than rationalizing them.

## Ownership and hard path gate

The recurring curator may write only to:

```text
research/graph/**
research/<research-line>/graph/**
research/prior_art/graph/**
.obsidian/graph.json                    # durable graph-presentation changes only
```

When `mathia-research-prior-art-incremental` is explicitly loaded, its narrow extension additionally owns:

```text
research/prior_art/incremental/**
```

When `mathia-research-clues` is explicitly loaded, its narrow clue-path extension also applies.

The curator must not modify:

```text
research/<line>/README.md
research/<line>/FINDINGS.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
research/<line>/mind/**
research/mind/**
research/prior_art/README.md
research/prior_art/COVERAGE.md
research/prior_art/catalog.json
experiments/**
docs/**
other .obsidian/**
code/tests/prompts outside owned paths
```

If prior art requires a correction to source research knowledge, create a clue and leave the correction to Research Watch/Mind.

## Publication policy

The scheduled curator may publish owned-path changes directly to the default branch when all gates pass.

Commit only when graph/prior-art/clue/presentation state materially improves. Do not create churn merely because the watch ran.

Before every commit:

1. inspect the complete diff;
2. verify every changed path passes the curator plus explicitly loaded extension gates;
3. verify the source revision remains coherent;
4. rerun the adversarial consistency review;
5. remove unrelated formatting/configuration changes.

Use:

```text
research(graph): <graph or graph-presentation change>
```

for graph/presentation-led changes, and:

```text
research(prior_art): <canonical prior-art materialization>
```

when incremental prior-art materialization leads the pass.

Do not open a routine PR from the scheduled watch.

## Notification and reporting

Routine graph refreshes, straightforward prior-art identity resolutions, and automatic status/color classification remain silent.

Notify when:

- a new external prior-art discovery may materially change a research line's novelty/viability and a clue was created;
- curation is blocked by contradictory/ambiguous provenance requiring source-owner action;
- a materially important cross-line bridge or branch closure becomes source-backed;
- a substantial new family of canonical prior art is materialized;
- a new research line required a durable graph-presentation update worth surfacing.

When reporting, distinguish clearly between canonical prior-art identity, graph edge, proposed clue, and accepted research evidence. Do not produce chronological run reports, project-status pages, or daily summaries.
