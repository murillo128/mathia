---
name: mathia-research-graph-curator
description: Curate Mathia's research graph, versioned Riemann atlas, and evidence-derived coverage/saturation metrics; resolve bounded incremental prior art and hand off source-grounded new insights as proposed clues through explicit companion skills.
---

# Mathia Research Graph Curator

This skill has two required parts. **Before doing any curator work, read `.agents/skills/mathia-research-graph-curator/PROCEDURE.md` in full.** `PROCEDURE.md` preserves the established Graph Curator procedure and remains authoritative except where this entrypoint adds the stricter topology and presentation invariants below. The invariants in this file are mandatory and override any weaker wording in the inherited procedure.

# Mandatory graph-topology invariants

## Research-line hubs exist from initialization

A current research line is a graph object from the moment it satisfies the discovery rule in `PROCEDURE.md`, including an initialized Research-Watch line that does not yet have a canonical finding.

Every current research line MUST therefore have one visible, semantically named hub under `research/<line>/graph/`, and that hub MUST be connected to the global graph. Do not wait for the first finding before materializing the hub. This keeps the structural parent older than or contemporaneous with the line's research objects whenever the curator first observes the line and prevents new research branches from appearing as anonymous islands.

Do not rewrite Git history or fabricate historical timestamps to repair old animation order. For already-existing lines, repair the topology prospectively; for future lines, create the structural hub on the first curator pass that observes initialization.

## Structural finding membership

Line membership is the one graph edge derived mechanically from repository topology rather than semantic mathematical evidence.

Every current canonical `research/<line>/findings/*.md` file MUST be structurally attached to its owning line. Structural membership may be materialized in the line hub's deterministic `structural-membership` block and/or in one semantically named line-owned membership projection such as `research/<line>/graph/<line>-membership.md`, provided that the membership projection itself links the line hub.

A structural membership edge means only **“this finding belongs to this research line.”** It MUST NOT be interpreted as support, dependence, refinement, contradiction, chronology, endorsement, or evidence for another finding. All semantic edges and relation nodes remain subject to the evidence gate in `PROCEDURE.md`.

Rebuild structural membership from the current canonical tree on every curator run. Add newly created findings, remove links whose canonical findings disappeared, and ignore workflow sidecars such as `*.review.md`. Never recreate a hand-maintained `FINDINGS.md` or use one as the source of membership.

The exact invariant is:

```text
union({finding targets in the line hub structural block},
      {finding targets in the line-owned membership projection})
==
{current canonical research/<line>/findings/*.md files}
```

modulo path-preserving link syntax and aliases. Duplicate structural links are harmless during migration, but the curator should avoid unnecessary duplication. A canonical finding may also have semantic edges; those do not replace structural membership.

## Structural prior-art membership

Every canonical prior-art Markdown node that is intentionally visible in the default Graph View MUST have a structural parent even when no current finding cites it semantically. Maintain a derived prior-art membership projection under `research/prior_art/graph/` that links the semantic `prior-art.md` hub and inventories current canonical prior-art notes from the frozen top-level corpus plus `research/prior_art/incremental/**`, excluding control files and graph-owned files.

This edge means only **“this note belongs to the canonical prior-art corpus.”** It does not assert relevance to a current research line. Semantic finding-to-prior-art redirects remain separately evidence-gated.

## Visible hub naming

Obsidian Graph identifies file nodes by their file basenames; a wikilink alias does not repair a generic node basename. Therefore every graph-visible hub or structural membership root MUST have a semantic, stable basename.

Do not publish graph-visible hubs as `index.md`, `overview.md`, `hub.md`, or another generic basename that loses the represented object. Use semantic kebab-case names such as `prime-circle.md`, `xi-flow.md`, `prior-art.md`, `prior-art-membership.md`, or `<line>-membership.md`; use `riemann-atlas.md` for the Atlas root.

When renaming a visible hub, update graph-owned inbound wikilinks and delete the obsolete generic path in the **same publication**, so the derived graph never intentionally contains both the semantic hub and a stale generic node.

## Default Graph View is mathematical, not workflow state

The default Obsidian Graph View MUST show the mathematical knowledge projection, not transient research workflow state.

Keep visible by default:

```text
findings/
mind/intuition/
graph/
prior_art/
```

Exclude from the default Graph View:

```text
clues/
**/RESEARCH_LINES.md
*.review.md
README.md
SOURCES.md
COVERAGE.md
LEAN_CANDIDATES.md
```

Clues and `RESEARCH_LINES.md` remain first-class repository inputs for the agents that own them; they are merely hidden from the default graph presentation. This section explicitly overrides the inherited `PROCEDURE.md` wording that allowed `clues/` to be surfaced by default.

## Orphan visibility is diagnostic

Keep orphan visibility enabled in the declarative Obsidian graph configuration. Do **not** hide topology defects by setting `showOrphans` to false or by filtering canonical findings or canonical prior-art nodes out merely because they lack links.

After structural membership has been rebuilt, a visible canonical finding or prior-art note that is still an orphan is a graph-curation defect: identify the missing or unresolved structural link and repair it. Other intentionally standalone derived nodes may remain when the model requires it.

# Curator-cycle integration

In addition to the cycle defined in `PROCEDURE.md`, every material curator pass MUST:

1. discover current research lines, including initialized zero-finding lines, and ensure each has a semantic visible hub;
2. inventory canonical finding files directly from the current tree and reconcile the union of line-hub and line-membership structural links to that exact inventory before optional semantic changes;
3. inventory graph-visible canonical prior-art notes and reconcile the prior-art membership projection;
4. verify that every current line hub and other graph-visible root/membership hub uses a semantic basename rather than a generic one;
5. update graph-owned inbound wikilinks atomically when a hub path changes;
6. keep `clues/` and `RESEARCH_LINES.md` out of the default Graph View while retaining them unchanged as source workflow state;
7. leave `showOrphans` enabled and use residual canonical-finding or prior-art orphans as validation failures, not as presentation problems.

These topology operations are derived maintenance, not mathematical claims. They do not require the semantic evidence gate that governs relation edges, but they remain subject to every ownership, hard-path, publication, source-authority, prior-art, clue, Atlas, and notification rule in `PROCEDURE.md`.

# Publication validation

Before declaring graph curation successful, verify all of the following in addition to the checks in `PROCEDURE.md`:

- every current initialized research line has a semantic graph hub connected to the global graph;
- every canonical finding is structurally attached to its owning line through the hub/membership union;
- no `*.review.md` sidecar appears in structural membership;
- the structural finding membership set has neither stale nor unresolved targets;
- every graph-visible canonical prior-art note is attached to the prior-art structural membership projection;
- no graph-visible root/line/membership hub uses a generic `index`, `overview`, or `hub` basename;
- no graph-owned inbound wikilink still points at an obsolete renamed hub path;
- `.obsidian/graph.json` exposes canonical findings, mind intuitions, graph state and prior art, excludes `clues/` and `RESEARCH_LINES.md`, and keeps `showOrphans: true`.

If any of these checks fails, the graph update is incomplete even when its semantic relation changes are otherwise valid.
