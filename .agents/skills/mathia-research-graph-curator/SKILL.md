---
name: mathia-research-graph-curator
description: Curate Mathia's derived Obsidian research graph from persisted findings, mind notes, research lines, and canonical prior art without performing new mathematical or literature research.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator owns only the derived research graph. It turns already-persisted Mathia knowledge into navigable Obsidian graph views showing findings, durable intuitions, research lines, prior-art redirects, branch closures, dependencies, and source-backed cross-branch bridges.

The curator is **not a research agent**. It must not discover new mathematics, extend derivations, run a literature search, upgrade evidence, create new intuitions, or repair source knowledge by invention.

The authoritative knowledge remains in findings, mind notes, research-line notes, and canonical prior-art notes. Everything under `graph/` is regenerable presentation state.

## Read-only source knowledge

Read only as much source material as needed to refresh the graph accurately.

Primary inputs are:

```text
research/<line>/README.md              # branch context when needed
research/<line>/FINDINGS.md            # compact evidence index when present
research/<line>/findings/**             # canonical detailed findings
research/<line>/mind/**                 # local durable intuitions/research lines when present
research/mind/**                        # genuinely global Mathia intuitions/research lines
research/prior_art/**                   # canonical prior-art projection once materialized
```

Treat every `graph/` subtree as derived output, not as evidence for a new mathematical relation.

The corpus and discovery machinery under `experiments/`, including the Riemann corpus and OpenAlex artifacts, is **not** a normal input to this recurring watch. Issue `#63` owns the one-time/materialization work that turns existing corpus material into `research/prior_art/`. Do not duplicate that work.

Do not browse the web and do not perform a new literature search.

## Discover research lines conservatively

A research line is a directory under `research/` that contains durable research evidence such as `FINDINGS.md` or `findings/`.

Do not treat these roots as research lines:

```text
research/graph/
research/mind/
research/prior_art/
```

If a new legitimate research line appears and has no graph directory yet, the curator may create:

```text
research/<line>/graph/index.md
research/<line>/graph/relations/**
```

Do not create empty graph directories merely for symmetry when no durable source knowledge exists.

## Graph model

### Existing notes are the nodes

Findings, mind notes, research-line notes, and prior-art notes already are canonical graph nodes. Link to them with Obsidian wikilinks. Do not clone their mathematical content into graph files.

Use full repository paths in wikilinks when names or IDs could be ambiguous.

### Relation notes are derived hyperedges

When several source nodes participate in one explicitly justified mechanism, obstruction, refinement, dependency chain, or bridge, materialize a small derived relation note under the relevant `graph/relations/` directory.

A relation note should contain only enough information to explain:

- what relation is being represented;
- which authoritative source notes justify it;
- the strongest relation that those sources actually support;
- any explicit uncertainty or boundary that affects the edge.

Do not turn relation notes into new mathematical essays.

Prefer descriptive relation titles over a large fixed ontology. Useful relation semantics include dependencies, refinements, corrections, supersession, obstructions, prior-art redirects, information-loss mechanisms, and explicit cross-branch bridges, but only when the source text supports that meaning.

### Local and global views

Each research line owns its local view:

```text
research/<line>/graph/**
```

Prior art owns:

```text
research/prior_art/graph/**
```

Global aggregation and genuinely cross-line relation notes live under:

```text
research/graph/**
```

Local and global graphs are **views over the same canonical source notes**, not duplicated independent knowledge bases.

## Evidence gate for an edge

A graph relation may be created or strengthened only when its semantics are recoverable from persisted source knowledge.

Strong evidence includes:

1. one note explicitly naming another finding/intuition/prior-art node and stating the dependency, correction, obstruction, refinement, bridge, or consequence;
2. an explicit `Synthesis of evidence`, `Relation to earlier findings`, `Effect on existing findings`, `Research consequence`, status, or equivalent section that describes the relationship;
3. a durable mind note explicitly grouping findings into one proved/supported principle;
4. an unambiguous prior-art node whose provenance or aliases match the theorem/source/result named by the finding.

The following are **not sufficient** by themselves:

- similar titles or vocabulary;
- temporal proximity or consecutive IDs;
- embedding/semantic similarity;
- two notes discussing the same broad topic;
- the curator believing one theorem probably implies another;
- a plausible mathematical bridge not already persisted in source knowledge.

Do not create speculative edges merely to make the graph denser.

## Missing-information rule

When a desired relation cannot be established from persisted evidence, **stop that derivation rather than infer the missing mathematics**.

Examples:

- a finding names a paper but multiple prior-art nodes could match it;
- a mind note says two mechanisms are related but does not justify the direction needed for a stronger edge;
- a finding references an old ID whose exact source claim cannot be reconstructed;
- a source mentions prior art but there is no stable provenance sufficient to identify a canonical `PA-*` node.

For a local ambiguity, omit or preserve the unresolved edge and report exactly what provenance or source statement is missing. Continue unrelated graph refreshes only when doing so cannot hide or compound the ambiguity.

Abort publication entirely when the ambiguity affects node identity, could overwrite a valid existing relation, or makes the generated graph internally inconsistent.

Never solve missing information with a web search or a fresh mathematical derivation.

## Prior-art integration

`research/prior_art/` is the canonical research-facing projection of the pre-existing corpus once issue `#63` materializes it.

Connect a finding or intuition to a prior-art node only when the mapping is unambiguous from persisted provenance, for example:

- the source note already names the stable `PA-*` ID;
- the prior-art note declares the exact theorem/source/title cited by the research note;
- a previously audited mapping is already persisted and remains valid.

Do not fuzzy-match a finding to a prior-art node solely from semantic similarity.

A finding may validly remain a `prior-art redirect` without an exact `PA-*` edge until provenance is sufficient.

The curator must never modify canonical prior-art notes. It may modify only `research/prior_art/graph/**`.

## Historical IDs and duplicates

Stable finding IDs are historical labels, not globally unique primary keys. **Repository path is the graph identity.**

When legacy collisions exist, such as multiple notes carrying the same `PC-NNN` or `PF-NNN`, preserve every source note and disambiguate it by full path. Never renumber historical findings during graph curation.

Mark two notes as duplicate/alias expositions only when their persisted content or provenance makes that equivalence explicit enough to audit. Similar subject matter is not enough.

Historical finding backfill or correction is outside the recurring curator role. The initial graph migration may have repaired missing historical notes, but scheduled curator runs must not write to `findings/` or `FINDINGS.md`.

## Research lines and frontier representation

`mind/RESEARCH_LINES.md` files are authoritative descriptions of currently meaningful investigation lines. The graph may link findings and intuitions to those research-line nodes when the source explicitly names the linked intuition or evidence.

Do not invent a roadmap, TODO queue, chronology, or project status from those lines.

A branch closure, obstruction, redirect, or open frontier may appear in the graph only when it is already stated in source knowledge.

Do not assign subjective numeric scores for novelty, fertility, saturation, importance, confidence, or percentage of mathematics explored.

Exact derived counts are allowed only when they materially improve navigation and cannot be mistaken for scientific scores; prefer not to persist them unless needed.

## Curator cycle

### 1. Synchronize the source revision

Start from the current repository default branch and a clean worktree.

The graph should correspond to one coherent observed source revision. If the default branch advances materially while the curator is working, especially through a research-watch or mind update, refresh to the new head and recompute affected graph output before publishing.

### 2. Inventory source nodes

For every research line, inventory:

- detailed findings;
- compact finding index entries when useful for status or historical context;
- local durable intuitions;
- local research lines.

Also inventory global mind notes and canonical prior-art notes.

Do not infer that a missing note exists merely because an ID is referenced somewhere.

### 3. Preserve existing valid relations

Treat current graph content as derived state that may help incremental work, but revalidate changed or newly relevant relations against source notes.

Do not retain an edge merely because it existed previously if the source note was corrected, weakened, superseded, or removed.

### 4. Add only source-backed deltas

Refresh line hubs and global aggregation, then add/update/delete relation notes only as required by changed authoritative source knowledge.

Prefer updating an existing relation note over creating a near-duplicate cluster.

### 5. Adversarial consistency review

Before publication check:

- every linked source path exists;
- no relation is stronger than its cited source evidence;
- uncertain/conjectural source claims were not silently promoted;
- historical ID collisions remain path-disambiguated;
- local relation notes stay in the correct line;
- cross-line relationships live under `research/graph/**` unless a local view merely links to them;
- prior-art links are provenance-backed;
- no status diary, timestamps, run log, or subjective scores were introduced;
- Obsidian wikilinks resolve without requiring community plugins.

If the review finds an unsupported edge, remove it rather than rationalizing it.

## Ownership and hard path gate

The recurring curator may write **only** to graph-owned paths:

```text
research/graph/**
research/prior_art/graph/**
research/<research-line>/graph/**
```

It must not modify:

```text
research/<line>/README.md
research/<line>/FINDINGS.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
research/<line>/mind/**
research/mind/**
research/prior_art/**          # except research/prior_art/graph/**
experiments/**
docs/**
code/tests/prompts outside graph ownership
```

If a missing relation can only be fixed by changing source knowledge, report the missing source information and leave that change to the owning research-watch, mind, or prior-art process.

## Publication policy

A scheduled curator watch is the owner of derived graph paths and may publish graph-only improvements **directly to the repository default branch**, analogous to the direct-main ownership of mathematical research watches.

Commit only when the derived graph materially changes. Do not create churn merely to record that the watch ran.

Before every commit:

1. inspect the complete diff;
2. verify every changed path passes the graph ownership gate;
3. verify the source revision is still current enough that the graph is not stale at publication time;
4. rerun the adversarial consistency review;
5. remove unrelated formatting changes;
6. use the commit prefix:

```text
research(graph): <derived graph change>
```

Examples:

```text
research(graph): connect new prime-flute obstruction chain
research(graph): add canonical prior-art mappings
research(graph): integrate prime-lattice mind relations
```

Do not open a routine PR from the scheduled watch.

## Notification and reporting

The curator should normally be quiet when it merely refreshes expected graph links.

Notify the user when:

- curation is blocked by missing or contradictory provenance that requires source-owner action;
- a source correction forces removal of a materially important graph bridge;
- a new source-backed cross-branch convergence or branch closure materially changes the research map;
- a new prior-art projection from `#63` enables a substantial canonical mapping pass.

When reporting a blocker, state the exact missing information and affected source paths. Do not attempt to fill the gap with speculation.

Do not produce a chronological run report, project-status page, or daily summary.