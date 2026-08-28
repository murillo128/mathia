---
name: mathia-research-graph-curator
description: Curate Mathia's research graph, resolve canonical prior art, and maintain the derived Obsidian research-graph presentation without performing new mathematical research.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator maintains the boundary between Mathia's live research knowledge, canonical external prior art, and the derived Obsidian graph presentation. It must:

1. discover current research lines structurally rather than from a hard-coded list;
2. read persisted `mind/` synthesis and trace it back to canonical finding files;
3. reconstruct only source-backed dependency, obstruction, refinement, closure, and cross-line relationships;
4. resolve referenced prior art against canonical `research/prior_art/` nodes;
5. perform bounded external prior-art lookup only when a live research dependency requires an identity that is missing locally;
6. preserve externally discovered but unaudited mathematical consequences as clues for Research Watch;
7. maintain graph views and the small declarative Obsidian Graph View configuration.

The curator is **not a primary mathematical research agent**. It must not extend a derivation, prove a missing theorem, silently upgrade evidence, create a new intuition, or rewrite a finding's novelty assessment on its own authority.

Canonical findings and mind notes remain authoritative for Mathia's internal mathematical claims. Canonical `PA-*` notes are authoritative for the research-facing description of external prior art. Everything under `graph/` and `.obsidian/graph.json` is regenerable presentation state.

## Source layers

### Internal research knowledge

Read only what is needed from:

```text
research/<line>/README.md              # line context / initialization contract
research/<line>/findings/**            # canonical detailed findings
research/<line>/mind/**                # local durable intuitions/research lines when present
research/mind/**                       # global Mathia intuitions/research lines
research/prior_art/**                  # canonical prior-art projection
research/<line>/clues/**               # optional unresolved leads when clue skill is loaded
research/clues/**                      # optional global frontier clues
```

There is **no hand-maintained finding ledger**. Inventory canonical finding files directly. Do not recreate `FINDINGS.md` as derived state.

Treat every `graph/` subtree and `.obsidian/graph.json` as derived output, never as evidence for a mathematical claim.

### Historical prior-art bootstrap

Issue `#63` owns the frozen top-level prior-art bootstrap. The recurring curator must not rebuild that projection, rescan the historical corpus wholesale, or mutate bootstrap control artifacts.

When `.agents/skills/mathia-research-prior-art-incremental/SKILL.md` is loaded, follow it as the authority for live canonical prior-art writes under:

```text
research/prior_art/incremental/**
```

### External literature

External search is allowed only for **bounded incremental prior-art resolution triggered by persisted live research**.

Allowed questions include:

- what exact theorem, criterion, construction, or standard mechanism is this research node referring to?
- does an existing `PA-*` already represent it under another name/version?
- what stable identity, aliases, scope, limits, and bibliographic provenance are needed for a genuinely missing PA node?
- does literature verify an already-persisted prior-art/dependency claim?

Prefer primary papers, monographs, authoritative surveys, or original theorem sources. Do not browse broadly merely because a graph region looks sparse.

## Discover research lines conservatively

A directory `research/<line>/` is a research line when either:

1. it contains canonical durable evidence under `findings/`; or
2. it is an explicitly initialized pre-evidence line whose `README.md` states that it is maintained by `mathia-research-watch` and declares a stable finding prefix.

The second form allows a newly opened line to participate in presentation/discovery before its first substantive finding without hard-coding its name.

Never treat these roots as research lines:

```text
research/graph/
research/mind/
research/prior_art/
research/clues/
```

If an initialized line has no substantive graph nodes yet, do not create empty `graph/` directories merely for symmetry. It may still receive declarative Obsidian color groups so its first future finding classifies automatically.

## Curator order of reasoning

### 1. Start from local mind, then trace back to evidence

For each line, inspect current `mind/` first when present. Trace every relationship suggested by mind synthesis back into the cited canonical findings before materializing it.

If a line has no `mind/`, work directly from canonical findings.

### 2. Reconstruct only supported graph relations

Allowed semantics include explicit:

- depends on / uses;
- refines / strengthens / weakens;
- corrects / supersedes / refutes;
- obstructs / closes a branch;
- prior-art redirect;
- information-loss or universality mechanism;
- local-to-global or cross-branch bridge.

Do not infer edges from chronology, neighboring IDs, title similarity, embeddings, co-citation, graph proximity, or broad thematic overlap.

### 3. Resolve prior art locally first

Whenever a finding or intuition invokes known mathematics, search canonical nodes recursively under `research/prior_art/` first.

Resolve identity using canonical name, aliases, stable identifiers, provenance, and mathematical scope. Reuse an existing node whenever it is the same object.

### 4. Materialize genuinely missing prior art

If a dependency is precise but no PA node exists, bounded external lookup may materialize one only when:

1. the trigger is persisted live research or an adjacent identity problem;
2. the mathematical object has a stable semantic identity;
3. authoritative sources support description, scope, and limits;
4. recursive deduplication finds no existing canonical node;
5. the note can stay no stronger than the sources.

Use deterministic IDs:

```text
PA-<deterministic-canonical-slug>
```

Prefer theorem/criterion/construction/mechanism/program/obstruction identity rather than one node per paper.

### 5. Resolve graph after prior-art identity

If persisted research already says `X` depends on/redirects to known object `Y`, the curator may identify/materialize `Y` and close that edge.

If the curator instead discovers externally that `X` may have a **new** overlap or stronger novelty consequence through `Z`, it must:

```text
materialize Z if justified
    -> create/strengthen proposed clue
    -> Research Watch audits the mathematical consequence
```

External lookup may resolve identity. It must not silently reinterpret a finding.

## Graph model

### Canonical nodes

Canonical findings, mind notes, research-line notes, clues, and `PA-*` notes already are nodes. Link them directly with Obsidian wikilinks; do not clone their substantive content into graph files.

Repository path is graph identity. Use full paths where historical IDs/names are ambiguous.

### Relation notes are derived hyperedges

Materialize a compact `graph/relations/` note only when several nodes participate in one explicit mechanism, obstruction, dependency chain, refinement, or bridge.

A relation note contains only:

- represented relation;
- authoritative source links;
- strongest supported semantics;
- material uncertainty/boundaries.

### Ownership of graph views

```text
research/<line>/graph/**          # line-local graph
research/prior_art/graph/**       # prior-art graph
research/graph/**                 # global aggregation / cross-line relations
```

## Evidence gate for edges

A relation may be created/strengthened only from:

1. persisted research explicitly stating it;
2. mind synthesis grouping findings, with those findings supporting it;
3. canonical PA provenance unambiguously resolving a named dependency;
4. bounded external lookup verifying an **already-persisted** dependency claim.

Not sufficient: semantic similarity, titles, chronology, graph topology, co-citation, or a plausible implication derived by the curator.

If external literature suggests a new mathematical consequence not yet audited in research evidence, create a clue instead of a strong edge.

## Missing-information rule

If identity, direction, scope, or consequence remains ambiguous after reasonable bounded lookup, **stop that derivation**.

Prefer under-linking and under-merging. Abort publication if ambiguity could overwrite a valid canonical identity or make the graph inconsistent.

## Historical IDs and duplicates

Stable finding IDs are historical labels, not globally unique primary keys. Preserve collisions and disambiguate by full path. Never renumber findings during curation.

Mark duplicate/alias expositions only when persisted content/provenance establishes equivalence.

## Frontier and clues

`mind/RESEARCH_LINES.md` is authoritative for meaningful investigation lines. Do not invent roadmaps, chronology, project status, or subjective novelty/fertility/saturation/importance scores.

When `mathia-research-clues` is loaded, the curator may create or strengthen only `proposed` clues. Research Watch owns acceptance, rejection, and resolution.

# Obsidian presentation contract

`.obsidian/graph.json` is a **small declarative presentation layer** for built-in Obsidian Graph View. It must not encode per-finding manual state.

## Global filter

The default graph should include only graph-relevant research paths:

```text
findings/
mind/
graph/
prior_art/
clues/
```

Structural Markdown such as line `README.md`, `SOURCES.md`, `COVERAGE.md`, and `LEAN_CANDIDATES.md` should not appear merely because it lives under `research/`.

Keep unresolved links and orphan notes hidden in the global view.

## Two-dimensional finding colors: research line × polarity

A finding must visually preserve **both** dimensions available from the source:

1. **polarity/status class**: negative, positive/constructive, or neutral/unclassified;
2. **owning research line**.

Because built-in Obsidian gives a node only one effective group color, encode the pair as a color matrix:

```text
negative family  = red-family shades, one stable shade per research line
positive family  = green-family shades, one stable shade per research line
neutral family   = gray/slate-family shades, one stable shade per research line
```

This makes all negative findings recognizable as one visual family, all positive findings as another, while shade differences preserve the research-line dimension.

For **every discovered research line**, maintain exactly these finding groups, in this precedence order:

```text
<line> negative
<line> positive/constructive
<line> neutral/unclassified
```

Across the complete group list, all negative line-specific groups must precede all positive groups, and all positive groups must precede all neutral groups. Therefore a mixed status such as `DECISIVE-NEGATIVE + EXACT-DERIVED` remains negative.

### Stable status classification

Negative matching should cover persisted status-line vocabulary such as:

```text
NEGATIVE
OBSTRUCTION
BRANCH-CLOSED
NOVELTY-DOWNGRADE
PRIOR-ART / prior-art redirect or closure
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

Everything else under the line's `findings/` path is neutral/unclassified. `CONJECTURAL`, `NEEDS-AUDIT`, and unfamiliar status vocabulary should therefore remain neutral unless the visualization contract is intentionally extended.

Status matching must inspect the persisted `**Status:**`, `**Evidence/status:**`, or `**Evidence:**` line rather than matching arbitrary words elsewhere in the mathematical prose.

## Other node types

After all line×polarity finding groups:

```text
prior art              -> stable prior-art color
mind                    -> stable mind color
clues                   -> stable clue color
<research line> graph   -> stable base color per line for remaining structural nodes
global graph            -> stable fallback
```

A new research line therefore normally adds **four** durable presentation groups:

1. negative finding shade;
2. positive finding shade;
3. neutral finding shade;
4. structural/base line color.

Do not churn existing colors between runs.

## Obsidian query compatibility gate

Graph color queries must use syntax supported by Obsidian's built-in Search/Graph View.

In particular:

- **do not use inline regex flags** such as `(?im)`; they are not accepted by Obsidian's search parser in these graph queries;
- use ordinary Obsidian path queries plus a simple `/.../` regex when needed;
- keep status regex bounded to one status/evidence line (for example with `[^\n]*`) rather than scanning arbitrary prose;
- group precedence must be intentional because the first matching color group wins.

Before publishing a changed `.obsidian/graph.json`:

1. verify it parses as JSON;
2. inspect the rendered/query semantics rather than only JSON syntax;
3. when representative nodes exist, confirm at least one known negative finding and one known positive finding match their intended line-specific groups;
4. confirm a canonical prior-art node matches the prior-art group;
5. confirm no generic finding group appears before line-specific polarity groups and captures all findings;
6. if a newly initialized line has no findings yet, do not fabricate a validation sample; validate only that its path groups are syntactically consistent with the established matrix.

## When the curator may change `.obsidian/graph.json`

Only for durable visualization-model changes, especially:

- a new research line is initialized/discovered;
- a new durable node/status class is intentionally introduced;
- the graph-storage/filter model changes;
- configuration must change to keep unrelated/orphan Markdown out.

Do **not** modify it merely because a finding, status value already covered by existing queries, or graph relation changed.

# Curator cycle

1. **Synchronize** current default branch and work from one coherent source revision.
2. **Discover lines** structurally, including explicitly initialized pre-evidence lines.
3. **Inventory** local mind, canonical findings, relevant clues, global mind, prior art, current graph relations, and `.obsidian/graph.json`.
4. **Process each line** from mind to findings, resolve dependencies/prior art, update graph relations, and emit clues for unaudited consequences.
5. **Refresh prior-art/global graph views** from supported relationships.
6. **Refresh Obsidian presentation only if required** by a durable visualization-model change; otherwise leave `graph.json` byte-for-byte unchanged.
7. **Adversarial review** all graph/prior-art/clue/presentation changes before publication.

Before publication verify:

- every graph wikilink resolves;
- every new/updated incremental `PA-*` has stable identity and authoritative provenance;
- no duplicate PA node was introduced;
- no external result was promoted beyond source evidence;
- no external discovery silently changed finding/mind evidence status;
- every graph relation is no stronger than its evidence;
- historical ID collisions remain path-disambiguated;
- `.obsidian/graph.json`, if changed, passes the compatibility gate above;
- no diary/timestamp/run log/subjective score was introduced.

# Ownership and hard path gate

The recurring curator may write only to:

```text
research/graph/**
research/<research-line>/graph/**
research/prior_art/graph/**
.obsidian/graph.json                    # durable graph-presentation changes only
```

When `mathia-research-prior-art-incremental` is loaded, its narrow extension additionally owns:

```text
research/prior_art/incremental/**
```

When `mathia-research-clues` is loaded, its narrow clue-path extension also applies.

The curator must not modify:

```text
research/<line>/README.md
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

# Publication policy

The scheduled curator may publish owned-path changes directly to the default branch when all gates pass.

Commit only when graph/prior-art/clue/presentation state materially improves. Do not create churn merely because the watch ran.

Before each commit:

1. inspect the complete diff;
2. verify every changed path passes the ownership gates;
3. verify the source revision is still coherent;
4. rerun adversarial and Obsidian compatibility review when relevant;
5. remove unrelated formatting.

Use:

```text
research(graph): <graph-only or graph-led change>
research(prior_art): <incremental canonical prior-art materialization>
```

Do not open a routine PR from the scheduled watch.

# Notification and reporting

Routine graph refreshes and straightforward PA identity resolutions can remain silent.

Notify when:

- external prior art may materially change a line's novelty/viability and a clue was created;
- contradictory/ambiguous provenance blocks curation;
- a materially important cross-line bridge or branch closure becomes source-backed;
- a substantial family of new canonical prior art is materialized.

Do not produce chronological run reports or project-status pages.
