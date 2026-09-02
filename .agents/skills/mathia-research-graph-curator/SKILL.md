---
name: mathia-research-graph-curator
description: Curate Mathia's research graph, versioned Riemann atlas, and evidence-derived coverage/saturation metrics; resolve bounded incremental prior art and hand off source-grounded new insights as proposed clues through explicit companion skills.
---

# Mathia Research Graph Curator

This skill has two required parts. **Before doing any curator work, read `.agents/skills/mathia-research-graph-curator/PROCEDURE.md` in full.** `PROCEDURE.md` preserves the established Graph Curator procedure and remains authoritative except where this entrypoint adds the stricter topology invariants below. The invariants in this file are mandatory and override any weaker wording in the inherited procedure.

# Mandatory graph-topology invariants

## Structural finding membership

Line membership is the one graph edge derived mechanically from repository topology rather than semantic mathematical evidence.

For every current research line that has canonical findings, its **visible line hub MUST directly link every current canonical `research/<line>/findings/*.md` file**. Maintain those links inside a deterministic block delimited by:

```text
<!-- structural-membership:start -->
...
<!-- structural-membership:end -->
```

A structural membership edge means only **“this finding belongs to this research line.”** It MUST NOT be interpreted as support, dependence, refinement, contradiction, chronology, endorsement, or evidence for another finding. All semantic edges and relation nodes remain subject to the evidence gate in `PROCEDURE.md`.

Rebuild the structural-membership block from the current canonical tree on every curator run. Add newly created findings, remove links whose canonical findings disappeared, and ignore workflow sidecars such as `*.review.md`. Never recreate a hand-maintained `FINDINGS.md` or use one as the source of membership.

The exact invariant is:

```text
{targets in structural-membership block}
==
{current canonical research/<line>/findings/*.md files}
```

modulo path-preserving link syntax and aliases. A canonical finding may also have semantic edges; those do not replace the mandatory structural membership edge.

## Visible hub naming

Obsidian Graph identifies file nodes by their file basenames; a wikilink alias does not repair a generic node basename. Therefore every graph-visible hub MUST have a semantic, stable basename.

Do not publish graph-visible hubs as `index.md`, `overview.md`, `hub.md`, or another generic basename that loses the represented object. Use semantic kebab-case names, including line hubs such as `prime-circle.md`, `prime-flute.md`, `prime-lattice.md`, `weil-positivity.md`, `weil-inertia.md`, `arithmetic-fidelity.md`, and `mobius-cancellation.md`; use `prior-art.md` for the prior-art graph hub and `riemann-atlas.md` for the Atlas root.

When renaming a visible hub, update all graph-owned inbound wikilinks and delete the obsolete generic path in the **same publication**, so the derived graph never intentionally contains both the semantic hub and a stale `index` node.

## Orphan visibility is diagnostic

Keep orphan visibility enabled in the declarative Obsidian graph configuration. Do **not** hide topology defects by setting `showOrphans` to false or by filtering canonical findings out of the graph.

After structural membership has been rebuilt, a canonical finding that is still an orphan is a graph-curation defect: identify the missing or unresolved structural link and repair it. Genuine non-finding orphan nodes may remain when the source model intentionally leaves them disconnected, but canonical findings must always be attached to their owning research line.

# Curator-cycle integration

In addition to the cycle defined in `PROCEDURE.md`, every material curator pass MUST:

1. discover current research lines and inventory canonical finding files directly from the current tree;
2. reconcile each line hub's structural-membership block to that exact inventory before considering optional semantic graph changes;
3. verify that every current line hub and other graph-visible root hub uses a semantic basename rather than a generic one;
4. update inbound graph-owned wikilinks atomically when a hub path changes;
5. leave `showOrphans` enabled and use residual canonical-finding orphans as a validation failure, not as a presentation problem.

These topology operations are derived maintenance, not mathematical claims. They do not require the semantic evidence gate that governs relation edges, but they remain subject to every ownership, hard-path, publication, source-authority, prior-art, clue, Atlas, and notification rule in `PROCEDURE.md`.

# Publication validation

Before declaring graph curation successful, verify all of the following in addition to the checks in `PROCEDURE.md`:

- every canonical finding has a direct structural wikilink from its owning line hub;
- no `*.review.md` sidecar appears in structural membership;
- the membership set has neither stale nor unresolved finding targets;
- no graph-visible root/line hub uses a generic `index`, `overview`, or `hub` basename;
- no graph-owned inbound wikilink still points at an obsolete renamed hub path;
- `.obsidian/graph.json` still exposes canonical findings and keeps `showOrphans: true`.

If any of these checks fails, the graph update is incomplete even when its semantic relation changes are otherwise valid.
