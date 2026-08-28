---
name: mathia-research-graph-curator
description: Curate Mathia's research graph and incrementally materialize missing canonical prior art needed to resolve source-backed research dependencies, without performing new mathematical research.
---

# Mathia Research Graph Curator

## Responsibility

Use this skill for the recurring or scheduled **Research Graph Curator watch**.

The curator maintains the boundary between Mathia's live research knowledge and the external mathematical literature. Its job is to:

1. read persisted findings and mind synthesis;
2. reconstruct the source-backed dependency/obstruction/refinement structure they already imply;
3. resolve referenced prior art against the canonical `research/prior_art/` projection;
4. when a required prior-art object is missing, perform a **bounded external prior-art lookup**, materialize the canonical `PA-*` note when identity and evidence are sufficient, and then resolve the graph relation;
5. preserve unresolved or genuinely new mathematical questions as clues rather than inventing research conclusions.

The curator is **not a primary mathematical research agent**. It must not extend a derivation, prove a missing theorem, silently upgrade evidence, create a new intuition, or rewrite a finding's novelty assessment on its own authority.

Findings and mind notes remain authoritative for Mathia's internal mathematical claims. Canonical `PA-*` notes are authoritative for the curator's research-facing description of external prior art. Everything under `graph/` is regenerable presentation state.

## Source layers

### Internal research knowledge

Primary internal inputs are:

```text
research/<line>/README.md              # branch context when needed
research/<line>/findings/**             # canonical detailed findings
research/<line>/mind/**                 # local durable intuitions/research lines when present
research/mind/**                        # genuinely global Mathia intuitions/research lines
research/prior_art/**                   # canonical prior-art projection
```

There is no separate hand-maintained finding ledger. Inventory canonical finding files directly and derive navigation/index views from them.

Treat every `graph/` subtree as derived output, never as evidence for a new mathematical claim.

### Historical corpus material

Issue `#63` owns the one-time bulk projection from the retained Mathia/qwen corpus into `research/prior_art/`.

The recurring curator must not redo #63, rescan the full historical corpus, crawl OpenAlex, or rebuild the prior-art projection wholesale. The corpus under `experiments/` is not a normal recurring input.

### External literature

Unlike the one-time #63 bootstrap, the recurring curator **may use web/literature search**, but only for bounded incremental prior-art resolution triggered by live research knowledge.

External search is allowed to answer questions such as:

- what exact theorem/criterion/construction is this finding or intuition referring to?
- does an existing `PA-*` already represent the same mathematical object under another name?
- what canonical bibliographic identity, aliases, scope, and limits are needed to materialize a missing prior-art node?
- is the dependency explicitly suggested by the research note genuinely the same known object?

Prefer primary papers, monographs, authoritative surveys, or original theorem sources. Search by mathematical structure and equivalent terminology, not wording alone.

Do **not** browse broadly for interesting mathematics merely because a graph region looks sparse. External research must remain anchored to a persisted finding, intuition, research line, clue, or directly adjacent prior-art identity problem.

## Discover research lines conservatively

A research line is a directory under `research/` that contains canonical durable research evidence under `findings/`.

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

### 1. Start from the local mind, then trace back to evidence

For each discovered research line, inspect its current `mind/` first when present. Durable intuitions and `RESEARCH_LINES.md` are the highest-density statement of what the line currently believes is structurally important.

For every relation suggested by the mind, trace backward into the cited findings before materializing a graph relation. Mind synthesis may organize evidence, but it does not excuse missing support.

If a line has no mind yet, work directly from its canonical findings.

### 2. Reconstruct the dependency graph

Identify only relations that are explicit or mechanically recoverable from persisted source knowledge, including:

- depends on / uses;
- refines / strengthens / weakens;
- corrects / supersedes / refutes;
- obstructs / closes a branch;
- prior-art redirect;
- information-loss or universality mechanism;
- explicit local-to-global or cross-branch bridge.

Do not infer edges from chronology, ID proximity, title similarity, embeddings, co-citation, or broad thematic overlap.

### 3. Resolve prior-art dependencies locally first

Whenever a finding or intuition names, invokes, redirects to, or contrasts with known mathematics, search `research/prior_art/` first using canonical names, aliases, bibliographic identifiers, topics, and provenance.

If one existing `PA-*` is an unambiguous match, reuse it and resolve the graph edge.

Do not create a duplicate merely because the research note uses different terminology.

### 4. Materialize missing prior art when needed

If the research dependency is sufficiently precise but no canonical `PA-*` exists, perform a bounded external prior-art lookup.

Create a new canonical note only when all of these hold:

1. the trigger is tied to an existing persisted research node or a directly adjacent identity problem;
2. the external mathematical object can be identified unambiguously enough for a stable canonical identity;
3. authoritative sources support the description, scope, and relationship being materialized;
4. no existing `PA-*` is actually the same object under an alias/version;
5. the note can state the relevant mathematics without making a claim stronger than the sources.

Use deterministic IDs:

```text
PA-<canonical-slug>
```

Match the #63 canonical format and granularity. Prefer the mathematical theorem, criterion, construction, mechanism, program, obstruction, or reusable object as identity rather than a particular paper or author.

A new `PA-*` note should normally contain minimal frontmatter such as:

```yaml
---
id: PA-<canonical-slug>
type: prior-art
canonical_name: <canonical mathematical name>
aliases:
  - <supported alias>
kind: <small descriptive kind>
topics:
  - <topic>
---
```

and a concise body:

```text
# <canonical name>

## What it is
Source-grounded mathematical description.

## Relation to RH / Mathia research
Why this object is relevant to the triggering research node, without changing that node's evidence status.

## Known scope and limits
What the result does and does not establish.

## Related prior art
Only source-backed canonical relations.

## Evidence and provenance
Primary/authoritative bibliographic sources, stable DOI/arXiv/other identifiers when available, and the Mathia research paths that triggered materialization.
```

Do not copy long copyrighted passages or use the note as a substitute for the source literature.

### 5. Resolve the graph after prior-art materialization

Once the missing prior-art identity has been established, connect the triggering finding/intuition/research-line node to the canonical `PA-*` using the strongest relationship actually supported.

If the source research note already says, for example, that the mechanism is classical, is an application of a named theorem, or is blocked by a standard result, external verification may close that exact dependency edge.

If the external lookup instead discovers a **new overlap or stronger prior-art fact not already represented in the research evidence**, do not silently rewrite the research interpretation and do not promote the new relationship as an accepted research conclusion. Materialize the canonical `PA-*` if justified, then create or strengthen a research clue for the owning Research Watch to audit the novelty/consequence.

This distinction is critical:

```text
persisted research says X depends on known object Y
    -> curator may identify/materialize Y and close the edge

curator discovers externally that X may actually be classical because of Z
    -> materialize Z + create clue
    -> Research Watch decides the mathematical consequence
```

## Graph model

### Existing notes are canonical nodes

Findings, mind notes, research-line notes, and `PA-*` notes already are graph nodes. Link to them with Obsidian wikilinks. Do not clone their substantive content into graph files.

Use full repository paths when names or IDs could be ambiguous.

### Relation notes are derived hyperedges

When several canonical nodes participate in one explicit mechanism, obstruction, refinement, dependency chain, or bridge, materialize a compact derived relation note under the relevant `graph/relations/` directory.

A relation note should explain only:

- what relation is represented;
- which authoritative notes/evidence justify it;
- the strongest semantics actually supported;
- material uncertainty or boundaries.

Do not turn graph relation notes into mathematical essays.

### Local and global views

Each research line owns:

```text
research/<line>/graph/**
```

Prior-art graph presentation owns:

```text
research/prior_art/graph/**
```

Global aggregation and genuinely cross-line graph relations live under:

```text
research/graph/**
```

These are views over one canonical knowledge set, not duplicated knowledge bases.

## Evidence gate for graph edges

A graph relation may be created or strengthened when its semantics are supported by one of:

1. persisted research knowledge explicitly stating the relation;
2. a mind synthesis explicitly grouping findings into the relation, with the cited findings supporting it;
3. an existing canonical prior-art node and provenance that unambiguously resolves the named dependency;
4. a bounded external prior-art lookup that verifies the **already-persisted dependency claim** without adding a new mathematical interpretation.

The following are not sufficient:

- semantic similarity;
- similar titles/vocabulary;
- graph proximity;
- co-citation alone;
- chronological proximity;
- a plausible theorem implication the curator derived itself;
- an external paper suggesting a new overlap whose consequence has not yet been audited by Research Watch.

When the last case occurs, create a clue instead of a strong graph edge.

## Missing-information rule

If identity, direction, scope, or mathematical consequence remains ambiguous after reasonable bounded lookup, **stop that derivation**.

Do not force a `PA-*` canonicalization when:

- several different mathematical objects plausibly match the reference;
- the source research note is too vague to determine what dependency was intended;
- authoritative sources disagree materially on the scope needed by the graph;
- resolving the edge would require proving or deriving new mathematics rather than identifying prior art.

For a local ambiguity, omit the edge and report or clue the exact missing information. Continue unrelated curation only when this cannot hide or compound the ambiguity.

Abort publication when ambiguity could overwrite a valid canonical identity or make the graph internally inconsistent.

## Prior-art identity and deduplication

Canonical `PA-*` identity is semantic, not bibliographic.

Merge aliases, preprint/published versions, and duplicate bibliographic records only when they clearly describe the same mathematical object. Prefer under-merging when uncertain.

Do not create one `PA-*` per paper if several papers are sources for one theorem/mechanism. Conversely, do not merge distinct criteria/programs merely because they are often discussed together.

When a newly discovered source materially improves provenance or clarifies aliases/scope for an existing `PA-*`, the curator may update that canonical note without changing its mathematical identity.

## Historical IDs and duplicates

Stable finding IDs are historical labels, not globally unique primary keys. **Repository path is graph identity.**

Preserve every legacy collision and disambiguate by full path. Never renumber findings during graph curation.

Mark duplicate/alias expositions only when source content/provenance supports that conclusion.

Historical finding backfill or correction is outside the recurring curator role.

## Research lines, frontier, and clues

`mind/RESEARCH_LINES.md` files are authoritative descriptions of meaningful investigation lines. The graph may connect them to findings/intuitions/prior art only where source evidence supports the relationship.

Do not invent roadmaps, TODO queues, chronology, project status, or subjective numeric novelty/fertility/saturation scores.

When external prior-art resolution exposes a potentially important **new mathematical consequence** for a live research line, use `mathia-research-clues` when available:

```text
research/<line>/clues/CLUE-<slug>.md
```

or the global clue inbox when it genuinely spans lines or suggests a new line.

The clue must name the triggering research node, the canonical `PA-*`, the external evidence, the exact question for Research Watch, and what has not yet been established.

The curator may create/strengthen only `proposed` clues; Research Watch owns acceptance/rejection/resolution.

## Curator cycle

### 1. Synchronize source revision

Start from the current default branch and a clean worktree. If research-watch/mind output lands while curating and materially affects the active nodes, refresh before publishing.

### 2. Discover lines and inventory nodes

For each line, inventory findings, mind notes, and research lines. Also inventory global mind, canonical prior art, existing clues relevant to curation, and current derived graph state.

### 3. Process each line from mind to evidence

For each line in deterministic order:

1. read local mind/research lines when present;
2. trace their cited findings;
3. reconstruct explicit dependencies/obstructions/refinements;
4. resolve referenced prior art locally;
5. perform bounded external lookup only for missing/ambiguous prior-art identities that matter to those relationships;
6. materialize/update `PA-*` when the prior-art gate passes;
7. update local graph relations;
8. emit clues for externally discovered mathematical consequences that Research Watch must audit.

### 4. Refresh prior-art and global graph views

Update `research/prior_art/graph/**` from canonical PA relationships and update `research/graph/**` from the refreshed local views and genuine cross-line relations.

### 5. Adversarial consistency review

Before publication check:

- every graph wikilink resolves;
- every new/updated `PA-*` has stable identity and authoritative provenance;
- no PA note is a duplicate under another alias/version;
- no external search result was promoted beyond what its source establishes;
- no external prior-art discovery silently changed a finding/mind evidence status;
- every graph relation is no stronger than its research/prior-art evidence;
- uncertain/conjectural research claims were not upgraded;
- ID collisions remain path-disambiguated;
- local/global relation ownership is correct;
- no diary/timestamp/run log/subjective score was introduced;
- no copyrighted full-text payload was copied.

Remove unsupported edges or PA claims rather than rationalizing them.

## Ownership and hard path gate

The recurring curator may write only to:

```text
research/graph/**
research/<research-line>/graph/**
research/prior_art/graph/**
research/prior_art/PA-*.md
```

When `mathia-research-clues` is explicitly loaded, its narrow clue-path extension also applies.

The curator must not modify:

```text
research/<line>/README.md
research/<line>/SOURCES.md
research/<line>/LEAN_CANDIDATES.md
research/<line>/findings/**
research/<line>/mind/**
research/mind/**
research/prior_art/README.md            # bootstrap/coverage authority remains separate
experiments/**
docs/**
code/tests/prompts outside owned paths
```

If external prior art requires a correction to source research knowledge, create a clue and leave the correction to Research Watch/Mind.

## Publication policy

The scheduled curator owns its derived graph and incremental `PA-*` projection and may publish those changes directly to the default branch when all gates pass.

Commit only when graph/prior-art/clue state materially improves. Do not create churn merely because the watch ran.

Before every commit:

1. inspect the complete diff;
2. verify every changed path passes the curator/clue ownership gates;
3. verify the source revision remains coherent;
4. rerun the adversarial consistency review;
5. remove unrelated formatting changes.

Use:

```text
research(graph): <graph-only or graph-led change>
```

for graph-only curation, and:

```text
research(prior_art): <canonical prior-art materialization>
```

when adding/updating canonical `PA-*` nodes. A pass that materializes a PA and then connects it may use separate focused commits or one `research(prior_art): ...` commit when the graph update is inseparable from the materialization.

Do not open a routine PR from the scheduled watch.

## Notification and reporting

Routine expected graph refreshes and straightforward PA identity resolutions can remain silent.

Notify when:

- a new external prior-art discovery appears likely to materially change a research line's novelty or viability and a clue was created;
- curation is blocked by contradictory/ambiguous provenance requiring source-owner action;
- a materially important cross-line bridge or branch closure becomes source-backed;
- a substantial new family of canonical prior art is materialized beyond simple identity completion.

When reporting, distinguish clearly between:

- canonical prior-art identity resolved;
- graph edge resolved;
- externally discovered possible mathematical consequence awaiting Research Watch;
- actual accepted research evidence.

Do not produce a chronological run report, project-status page, or daily summary.