---
name: mathia-research-prior-art-incremental
description: Extend the Mathia Research Graph Curator with a safe incremental prior-art layer that coexists with the frozen issue #63 bootstrap projection.
---

# Mathia Incremental Prior Art

## Responsibility

Load this skill together with `mathia-research-graph-curator` whenever the recurring curator may materialize external prior art that is missing from the issue #63 bootstrap.

Issue #63 owns a deterministic historical bootstrap under `research/prior_art/`: its top-level generated notes, `catalog.json`, `README.md`, `COVERAGE.md`, and projection checker describe the retained Mathia/qwen evidence available at that frozen execution. The recurring curator must not mutate that bootstrap into a live catalog.

This skill provides the live incremental layer while preserving one logical prior-art namespace:

```text
research/prior_art/
  <issue-63 bootstrap notes>.md
  catalog.json
  README.md
  COVERAGE.md
  graph/**
  incremental/
    PA-<canonical-slug>.md
```

Both the bootstrap notes and `incremental/**` are canonical prior-art nodes for research and graph purposes. The directory distinction is provenance/ownership, not a mathematical distinction.

## Lookup order

Before any external search or write:

1. search all canonical nodes recursively under `research/prior_art/`, excluding `graph/**` and control files;
2. resolve identity using frontmatter `id`, canonical name, aliases, stable bibliographic identifiers, and provenance;
3. reuse an existing bootstrap or incremental node whenever it is the same mathematical object;
4. only if no canonical node exists may the curator perform the bounded external lookup allowed by `mathia-research-graph-curator`.

Never create an incremental node merely because the bootstrap uses a different filename convention.

The canonical identity is the frontmatter ID:

```text
PA-<canonical-slug>
```

not the repository filename.

## Incremental materialization

When the graph-curator prior-art gate passes for a genuinely missing object, write:

```text
research/prior_art/incremental/PA-<canonical-slug>.md
```

Use the same semantic granularity and minimal note schema as issue #63:

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

The body should contain:

```text
# <canonical name>

## What it is

## Relation to RH / Mathia research

## Known scope and limits

## Related prior art

## Evidence and provenance
```

For incremental nodes, `Evidence and provenance` must include authoritative external bibliographic provenance and the exact persisted Mathia finding/intuition/research-line path that triggered the lookup. Prefer DOI, arXiv, stable publisher/authoritative URLs, theorem names, or equivalent durable identifiers.

Do not copy long source text.

## Bootstrap immutability

The recurring curator must treat the issue #63 bootstrap artifacts as read-only:

```text
research/prior_art/catalog.json
research/prior_art/README.md
research/prior_art/COVERAGE.md
research/prior_art/*.md              # issue-63 top-level generated canonical notes
experiments/prior_art_projection.py
tests/test_prior_art_projection.py
```

The #63 renderer/checker intentionally validates the frozen bootstrap. Incremental nodes live below `research/prior_art/incremental/`, so they are outside that top-level generated-note census.

Do not add incremental discoveries to `catalog.json`, and do not rerender the #63 bootstrap merely to register live knowledge.

If the curator finds better or newer provenance for an existing bootstrap node, reuse the existing canonical node. Do not create a duplicate incremental node with the same `PA-*` ID. A materially important external fact that changes the interpretation of live research belongs in a Research Watch clue according to `mathia-research-clues`; it does not require rewriting the frozen bootstrap note.

## Updating incremental nodes

The curator may update an existing file under:

```text
research/prior_art/incremental/**
```

when authoritative evidence clarifies aliases, identity, scope, limits, or provenance without changing the canonical mathematical object.

If new evidence shows that two incremental nodes are actually the same object, under-merge until identity is certain, then consolidate carefully and repair graph links in the same coherent publication pass.

Never silently merge an incremental node into a frozen bootstrap node. Reuse the bootstrap identity for future graph relationships and remove the redundant incremental node only when the duplicate identity is explicit and all references are repaired.

## Graph integration

The graph curator treats bootstrap and incremental PA notes identically as graph nodes.

Use full repository paths in wikilinks when needed. A graph relation may point directly to either:

```text
research/prior_art/<bootstrap-note>.md
research/prior_art/incremental/PA-<canonical-slug>.md
```

Do not create graph aliases or duplicate wrapper nodes merely to hide the directory distinction.

The existing evidence gates from `mathia-research-graph-curator` remain unchanged: external lookup may resolve an already-persisted dependency, but a newly discovered mathematical consequence for a live finding must be handed to Research Watch as a clue rather than silently promoted.

## Ownership extension

When this skill is explicitly loaded with `mathia-research-graph-curator`, it narrows recurring prior-art writes to the live layer and extends the curator's writable paths with:

```text
research/prior_art/incremental/**
```

For recurring runs, prefer this path over the curator skill's older top-level `research/prior_art/PA-*.md` allowance. Treat the issue #63 top-level projection as frozen even though the generic curator skill predates this compatibility split.

All other curator and clue ownership restrictions remain in force.

## Publication and no-churn gate

Incremental PA changes may use the curator's direct-main publication exception only when:

- the lookup was triggered by persisted live research;
- canonical identity and authoritative provenance are sufficient;
- recursive deduplication found no existing canonical node;
- the complete diff stays within curator/graph/clue ownership;
- graph links are repaired coherently;
- no bootstrap artifact was modified;
- no unsupported mathematical consequence was promoted.

Use the curator's `research(prior_art): ...` commit prefix for materialization-led changes.

Do not commit merely to record that a lookup found nothing.
