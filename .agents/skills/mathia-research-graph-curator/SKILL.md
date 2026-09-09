---
name: mathia-research-graph-curator
description: Curate source-backed mathematical topology through stable membership, bounded semantic backfill, and reversible native links; maintain the Riemann atlas, evidence-derived metrics, and explicit prior-art/clue handoffs.
---

# Mathia Research Graph Curator

This skill has two required parts. **Before doing any curator work, read `.agents/skills/mathia-research-graph-curator/PROCEDURE.md` in full.** That procedure remains authoritative for research discovery, source evidence, Atlas/telemetry, companion skills, and publication. This entrypoint owns topology, presentation, bounded semantic reconciliation, and the exact reference-formatting exception below.

**Explicit precedence:** the stable-membership migration and reversible reference-formatting rules in this file supersede the inherited restrictions against relocating membership and making any finding-file change. In `PROCEDURE.md`, the responsibility, forbidden-write list, hard path gate, source-immutability cycle step, and final no-finding-change check must admit **only** that exact formatting exception. No permission to change mathematical content, evidence status, review state, or any other source layer is granted. All other inherited restrictions remain in force.

The objective is a faithful mathematical map, not maximum connectivity: structural membership, explicit relations between findings, and specific multi-source mechanisms have different meanings. A more connected or visually attractive graph is not evidence of research progress.

# Mandatory graph-topology invariants

## Research-line hubs exist from initialization

A current research line is a graph object from the moment it satisfies the discovery rule in `PROCEDURE.md`, including an initialized Research-Watch line that does not yet have a canonical finding.

Every current research line MUST therefore have one visible, semantically named hub under `research/<line>/graph/`, and that hub MUST be connected to the global graph. Do not wait for the first finding before materializing the hub. This keeps the structural parent older than or contemporaneous with the line's research objects whenever the curator first observes the line and prevents new research branches from appearing as anonymous islands.

Do not rewrite Git history or fabricate historical timestamps to repair old animation order. For already-existing lines, repair the topology prospectively; for future lines, create the structural hub on the first curator pass that observes initialization.

## Stable structural finding membership

Every current canonical `research/<line>/findings/*.md` file MUST be structurally attached to its owning line. Use **one stable line-owned projection**, `research/<line>/graph/<semantic-line-name>-membership.md`, which links the line hub. The hub links that projection rather than repeating the complete finding inventory in a second structural block.

This edge means only **“this finding belongs to this research line.”** It is derived mechanically from the current tree, not mathematical evidence. It MUST NOT be interpreted as support, dependence, refinement, contradiction, chronology, endorsement, or novelty. Semantic links neither replace membership nor make additional structural parents necessary.

Rebuild the sorted, deduplicated membership directly from the current canonical tree on every curator pass. Add current findings, remove disappeared targets, and exclude `*.review.md`. Never recreate a hand-maintained `FINDINGS.md` or use one as inventory authority. The invariant is:

```text
{finding targets in the stable line membership projection}
==
{current canonical research/<line>/findings/*.md files}
```

Do not create membership nodes for a run, commit, date, source window, recent frontier, or tail. These group workflow events rather than mathematical objects and can introduce artificial within-line and cross-line attraction.

When migrating existing hub blocks or `current-frontier-*`, `current-window-*`, `frontier-membership*`, or equivalent batch projections, first rebuild the stable line inventories from the **whole current tree**, not from the last delta. Then remove the redundant structural blocks/notes and repair inbound links in the same publication. A name alone is not deletion authority: inspect content, preserve any genuine source-backed semantic content in an appropriate existing mechanism note, and check inbound references across the repository. Do not silently rewrite a read-only source that points to an obsolete projection; defer that retirement and report the exact owner handoff if it cannot be completed within the path gate.

Migration may be bounded by line, but a shared batch projection must retain still-needed attachments until their stable replacements exist. Temporary duplication is acceptable only in explicitly unfinished regions, not as the final model. Never remove a sole attachment, publish dangling links, or describe a partial migration as globally complete.

## Structural prior-art membership

Every canonical prior-art Markdown node that is intentionally visible in the default Graph View MUST have a structural parent even when no current finding cites it semantically. Maintain a derived prior-art membership projection under `research/prior_art/graph/` that links the semantic `prior-art.md` hub and inventories current canonical prior-art notes from the frozen top-level corpus plus `research/prior_art/incremental/**`, excluding control files and graph-owned files.

This edge means only **“this note belongs to the canonical prior-art corpus.”** It does not assert relevance to a current research line. Semantic finding-to-prior-art redirects remain separately evidence-gated.

## Structural durable-intuition membership

Every graph-visible durable intuition `MI-*` note under `research/**/mind/intuition/` MUST have a structural parent independently of whether the curator has inferred any semantic relation for it.

Maintain `research/graph/intuition-membership.md` as a deterministic global membership projection. It MUST link the global graph and MUST inventory every current `research/**/mind/intuition/MI-*.md` file, including global intuitions under `research/mind/intuition/`. `RESEARCH_LINES.md` and other mind workflow/synthesis files are not members of this projection.

This edge means only **“this note is a durable Mathia intuition.”** It MUST NOT be interpreted as mathematical support, dependence, refinement, contradiction, chronology, endorsement, or evidence. Line hubs and semantic relation nodes may also link an intuition when justified, but those optional links do not replace structural membership.

The exact invariant is:

```text
{MI targets in research/graph/intuition-membership.md}
==
{current research/**/mind/intuition/MI-*.md files}
```

modulo the required backlink to `research/graph/global.md`, path-preserving link syntax, headings, and aliases. Rebuild this projection from the current tree on every curator run so newly created or removed `MI-*` notes cannot remain as silent graph islands.

## Source-backed semantic reconciliation

For each selected source, inspect its actual dependency, proof, correction, limitation, and consequence passages. Materialize missing relations when the current persisted text explicitly identifies both the target and the relationship. Suitable relations include use/dependence, refinement, strengthening/weakening, correction/supersession/refutation, a scoped obstruction or closure, a prior-art dependency, and an established cross-line bridge. Preserve hypotheses, direction, and every limiting qualifier; the evidence gate in `PROCEDURE.md` remains mandatory.

A bare identifier, bibliography entry, co-citation, shared term, common research line, chronology, graph proximity, color, centrality, or embedding similarity is **not** evidence of a semantic edge. Orphan status may identify a repair candidate but cannot justify its connection. Do not derive new implications or add transitive closure. When two findings use the same prior-art theorem, link each documented use to that theorem; do not infer a direct relation between the findings.

Distinguish “obstructs this proof strategy” from “refutes this theorem.” An abstract countermodel to the sufficiency of assumptions must not become a refutation of the source-specific conjecture. An open question or speculative transfer remains unproved; use a proposed clue only when there is a genuine mathematical question under the companion clue skill, not as a generic request to add hyperlinks.

### Incremental operation and bounded retrospective repair

Normal passes reconcile explicit relations in the added/modified source set and the exact surviving sources needed to validate it. Older surviving findings are **not excluded merely because they predate the current Git window**.

A caller-requested topology migration or a precisely scoped persisted repair may also perform a retrospective semantic pass. Select one named mechanism/subbranch and its explicit references, not the entire historical corpus. Default to at most **24 canonical source documents, including target verification reads**, per retrospective batch; tree/link inventory does not require full mathematical rereading and is not subject to that count. Stop expansion rather than skipping target verification when the budget is exhausted. A larger migration proceeds through bounded, explicitly scoped handoffs; routine scheduled work must not restart an unbounded historical scan.

Start from surviving canonical text, not an old graph summary. Resolve each identifier to its unique current repository path and verify the referenced scope in the target. Historical Git content may resolve provenance but cannot resurrect withdrawn evidence. Ambiguous identity, missing evidence, or an unproved bridge means defer or under-link. Backfill recovers already documented structure; it does not discover or endorse new mathematics.

Do not persist chronological batch nodes, semantic-orphan scoreboards, centrality metrics, or a new hand-maintained finding catalog. An optional compact, graph-owned JSON cache may retain current source/target fingerprints and completed inspection scope solely to avoid rereading unchanged sources during a multi-pass repair. It must be invalidated by source/target changes, must not hold mathematical claims or research priorities, and is not a graph node, research finding, telemetry episode, or reason for an otherwise empty commit.

### Native links preserve actual topology

Obsidian's native graph draws note-to-note internal links, not implications described in prose. A third note containing links to A and B creates connections from that note to A and B; writing a textual arrow there does **not** create a direct A-to-B edge. Its displayed arrows indicate link direction, not logical entailment.

Where a finding itself explicitly states its relationship to another finding or named prior-art object, prefer a direct internal link at that existing reference under the narrow formatting exception below. The surrounding source sentence carries the relation type and scope. Do not insert reciprocal links simply to make the graph undirected, and do not repeat the same source/target link throughout a note merely to increase apparent weight. Existing valid links already satisfy that adjacency.

Keep compact `graph/relations/` notes for a **specific shared mechanism, obstruction, or proof obligation** involving several current sources. Name them after that mechanism, not a run or a broad theme such as “regularity” or “arithmetic information.” Explain each source's role and scope. Reuse an existing suitable mechanism note; do not create one note per binary edge or a second copy of every source.

A mechanism note supplements direct source links; it must not be used to claim that a dependency chain has been materialized when only a summary star exists. Conversely, if a relationship is documented only in a third canonical source and neither endpoint contains an eligible reference, preserve that qualified source-backed relation in the mechanism note and leave direct-link editing to the source owner. Never invent a sentence in an endpoint to manufacture the desired topology.

Keep global and line hubs as navigation roots, not duplicate inventories of every semantic neighbor. Preserve independently meaningful relations even when a shorter path already exists. There is no minimum degree, maximum-neighbor quota, target edge density, or requirement to connect every pair within a mechanism; sparsity follows from evidence and deduplication, not from hiding true relationships.

## Narrow reference-formatting exception

In addition to the base graph paths and the two explicit companion extensions, the curator may make **reversible reference-formatting edits only** to existing canonical `research/<current-line>/findings/*.md` files. This is the sole additional source-file write authority and is available in incremental and explicitly scoped retrospective reconciliation.

All of these gates are mandatory:

1. The reference is already present in ordinary prose, and its surrounding persisted sentence states an eligible relationship. For additions, both endpoints resolve uniquely to surviving canonical finding or prior-art paths; a label alone is not identity. Provenance-checked cleanup under gate 6 replaces only the target-existence requirement, not the source or review gates. Skip self-links, speculative/merely thematic references, and any source or target with an active finding-review sidecar or other explicit active-edit lock. A skipped challenged finding is not thereby withdrawn or false.
2. Replace only the existing visible reference with a full vault-root-relative wikilink whose alias is **exactly the original text**, for example the syntax `[[research/<line>/findings/<basename>|<original reference>]]`. Prefer one context-bearing occurrence per target. Do not change an existing valid link, add a sentence, a relationship block, a backlink list, metadata, tags, or a new claim. Gate 6 is the only exception for removing an existing curator-introduced wrapper.
3. Do not edit headings, frontmatter, status/evidence fields, code (including inline code), mathematics, equations, tables, citation definitions, existing link destinations, or quoted source text. Leave an ineligible reference untouched rather than weakening this boundary. Never create, rename, delete, or reclassify a canonical source file.
4. Record the exact changed spans in the working validation and mechanically restore **only those new wrappers** to their original aliases. The restored bytes MUST equal the pre-edit file byte-for-byte. For gate-6 removals, reverse only the approved removals by reinstating their exact original wrappers to reconstruct the pre-edit bytes. Do not use a permissive strip-all-links or rendered-text comparison that could conceal unrelated changes. Failure to perform or pass this check blocks the source edit.
5. Read from one pinned source revision. Immediately before publication, recheck the source blobs, target identities/content, review sidecars, inbound references affected by migration, and every touched graph file against the current default branch. On a conflict, reload and revalidate; never overwrite concurrent mathematical edits or force-push. The final changed-path set and source-byte checks must match the exact publication candidate.
6. If a target later disappears, remove only a wrapper proven by Git history to have been introduced by this exception, restoring the identical original reference text. This removes the stale navigational edge without deleting or rewriting the historical mathematical sentence. Repairing other source links or changing the historical claim belongs to its owner.

This exception does **not** authorize editing intuitions, mind, clues, reviews, README/state, frozen prior art, `.agents/**`, or other non-owned files. Source-derived conclusions and workflow state remain read-only. A need for any broader change is an owner handoff, not permission to enlarge the exception.

For the inherited hard publication gate, classify a finding-file change under this exception separately from base graph paths, incremental prior art, and proposed clues. For the inherited source-immutability checks, require exact byte preservation after restoring the approved reference wrappers; every other source change remains forbidden. Curator link formatting uses the normal `research(graph):` publication prefix and MUST NOT count as a new finding, mathematical correction, novelty upgrade, or frontier-fertility episode.

## Visible hub naming

Obsidian Graph identifies file nodes by their file basenames; a wikilink alias does not repair a generic node basename. Therefore every graph-visible hub or structural membership root MUST have a semantic, stable basename.

Do not publish graph-visible hubs as `index.md`, `overview.md`, `hub.md`, or another generic basename that loses the represented object. Use semantic kebab-case names such as `prime-circle.md`, `xi-flow.md`, `prior-art.md`, `prior-art-membership.md`, `intuition-membership.md`, or `<line>-membership.md`; use `riemann-atlas.md` for the Atlas root.

When renaming a visible hub, inspect all inbound references, update graph-owned inbound links, and delete the obsolete generic path in the **same publication**. If a required inbound edit is outside ownership, defer that retirement and report the owner handoff; do not knowingly break the source or invent a permanent alias hub. A completed migration must not retain both the semantic hub and a stale generic node.

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

Keep orphan visibility enabled in the declarative Obsidian graph configuration. Do **not** hide topology defects by setting `showOrphans` to false or by filtering canonical findings, durable intuitions, or canonical prior-art nodes out merely because they lack links.

After structural membership has been rebuilt, a visible canonical finding, `MI-*` intuition, or prior-art note that is still an orphan is a graph-curation defect: identify the missing or unresolved structural link and repair it. Distinguish this from a structurally attached note with no established semantic neighbors, which is legitimate, and from a note isolated only by a user-selected filter. Do not manufacture semantic relations to eliminate either appearance. Other intentionally standalone derived nodes may remain when the model requires it.

Repair topology before tuning forces, labels, or node sizes. Preserve the existing line hues and status-group precedence. Do not hide canonical sources or remove legitimate membership merely to make a semantic view look denser. Native Graph View does not become a typed proof graph through color or arrow settings; relation meaning remains in the source text and mechanism notes.

# Curator-cycle integration

In addition to `PROCEDURE.md`, every material curator pass MUST:

1. pin a coherent source revision, process deletions, discover initialized lines, and ensure each has a semantic hub connected to the global graph;
2. rebuild whole-tree line membership and the canonical prior-art/MI membership sets; consolidate batch projections under the atomic migration rules rather than append another delta hub;
3. reconcile explicit semantic relations in the selected current sources; when retrospective repair was requested, bound it by mechanism and source budget;
4. resolve identities and verify source passages, endpoints, qualifications, review state, and whether a direct link already exists;
5. materialize eligible native reference links through the reversible formatting gate and maintain only useful, source-backed mechanism notes;
6. validate the resulting note-to-note adjacency, not just the presence of identifiers or textual arrows in summaries;
7. keep workflow files out of the default Graph View, preserve canonical-node visibility and `showOrphans: true`, and retain semantic hub names;
8. rerun path, exact-byte, current-ref, stale-link, source-evidence, Atlas, and telemetry gates on the exact publication candidate.

Membership repair and source-link formatting are graph maintenance, not mathematical progress. Atlas weights/states, research priorities, source claims, and clue dispositions must not change merely because topology or link count changed. The scheduled publication and notification rules in `PROCEDURE.md` remain in force.

# Publication validation

Before declaring graph curation successful, verify all of the following in addition to the inherited checks as narrowly amended above:

- every initialized line has a semantic graph hub connected to the global graph, and every canonical finding is attached through its stable line membership projection;
- membership target sets exactly match the current tree, with no review sidecars, duplicates inside a projection, missing targets, or stale targets;
- completed migration regions contain no redundant run/window/frontier membership nodes or duplicate complete hub inventories; every retirement preserves necessary attachments and resolves all affected inbound references;
- `research/graph/intuition-membership.md` links the global graph and its MI set exactly equals the current `research/**/mind/intuition/MI-*.md` inventory, excluding `RESEARCH_LINES.md` and other non-intuition mind files;
- every graph-visible canonical prior-art note has its structural parent independently of semantic use;
- every semantic relation traces to current canonical source text with exact target identity, relation scope, and surviving qualifications; no similarity-based, co-citation-based, chronological, or transitively invented edge was added;
- eligible direct source relations are actual internal links in the source note, not just strings or arrows inside a summary; missing ineligible direct links are not falsely reported as materialized;
- each finding-file edit is exclusively an approved reference wrapper (or its provenance-checked removal), passes the exact-byte restoration test, and has unchanged math/status/review content;
- sources, targets, and review state were rechecked against concurrent updates; no active-review source was silently rewritten;
- no graph-visible root/line/membership hub uses a generic `index`, `overview`, or `hub` basename, and no completed rename leaves unresolved inbound links;
- `.obsidian/graph.json` exposes canonical findings, mind intuitions, graph state and prior art, excludes clues/workflow files, preserves line/status colors, and keeps `showOrphans: true`;
- no graph-maintenance operation was counted as mathematical progress, and repeating reconciliation on unchanged sources produces no new links, mechanism duplicates, batch nodes, or other material diff.

If any check fails, the affected update is incomplete. A bounded repair may report its exact validated scope and remaining blockers, but must not claim global completion or publish a dangling/inconsistent region to fit a time budget.

## Required adversarial cases

Use these cases when reviewing a curator change or executing a migration; they are acceptance scenarios, not claims that a test harness has run:

- **Explicit dependency:** A already says it uses the uniquely identified B. Link that occurrence in A to B; do not invent the reverse edge or add another prose claim.
- **Shared prior art:** A and B each use P, but neither establishes a bridge. Preserve A-to-P and B-to-P without manufacturing A-to-B.
- **Scoped countermodel:** C says B's bound is insufficient for the strategy proposed in A, while explicitly not refuting A. Preserve those qualified references; never label the graph relation “A is false.”
- **Identity/review barrier:** a reused finding ID, a missing target, or an active review prevents automatic source-link editing. Do not guess the endpoint or change status to clear the gate.
- **Membership migration:** replacing a batch star must retain every current finding's stable parent and every legitimate semantic relation, with no stale inbound link to the removed projection.
- **Genuine semantic isolation:** a canonical finding with no established relation gets structural membership only. No neighbor quota or aesthetic requirement may create an edge.
- **Preservation and idempotence:** changing one qualifier, status, equation, heading, or unrelated link fails the byte-restoration gate; a second pass over unchanged inputs must make no further material change.
