# Prior-art projection coverage

This ledger records what issue #63 inspected, selected, merged, and left out. It is rendered from `catalog.json` plus the frozen Mathia interchange metadata; it does not claim bibliographic completeness or add new literature analysis.

## Frozen evidence bindings

| Family | Frozen binding | Records inspected | Projection disposition |
| --- | --- | ---: | --- |
| Riemann–Mathia v2 accepted object | `riemann_mathia_v2_cd92907b9bc4565cffc138110faceb21c77d4bf71388d75536a8e640af3ba5f0` | 8,264 objects; 8,003 accepted | 34 accepted semantic objects bind emitted notes |
| Agnostic Mathia v1 accepted object | `freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f` | 222 objects; 214 accepted | 4 accepted semantic objects bind emitted notes |
| Agnostic Mathia OpenAlex supplement accepted object | `agnostic_openalex_supplement_a1aa591df034db64d5ce0271df0da570e3aaf470ac49e5cc4014b66181bf0e33` | 600 objects; 595 accepted | 2 accepted semantic objects bind emitted notes |
| qwen-lean Riemann atlas | `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84` | 234 entries; 226 relations; 18 sources | 24 entries and 1 source record bind emitted notes |
| OpenAlex Riemann graph | `experiments/openalex_discovery/run_v1/graph_summary.json` | 11,753 accepted discovery candidates; 37,943 edges; 104 duplicate groups | Identity, citation, discovery, and version evidence only |
| Riemann–Mathia v1 parent | `riemann_mathia_full_e9f9f663e6f3a777ab7545f088f39d0662462f5da622364204e52be6fcf42cd6` | 568 immutable objects | Governed by v2 for overlaps and corrections |
| OpenAlex Riemann handoff | `openalex_handoff_89e50c9a268c116f9ca85d457e4cae8e3efa6f7feed64fbd1f815f0ded9d0dc6` | 25 records | Source identity and v2 handoff lineage |

The qwen paths are additionally pinned by Git blobs: entries `3c02d9d01ee667f6136185d49f0d6367818362c6`, relationships `42577705e28924d26f7fe552646ee71424621d78`, and sources `ec66ed63fc039b6ab991089303041d4c960b13ca`.

## Selection and disposition accounting

| Mathia family | Accepted source objects retained as provenance, not standalone notes | Accepted derived objects selected | Accepted derived objects not selected as standalone notes |
| --- | ---: | ---: | ---: |
| Riemann–Mathia v2 accepted object | 3,694 | 34 | 4,275 |
| Agnostic Mathia v1 accepted object | 98 | 4 | 112 |
| Agnostic Mathia OpenAlex supplement accepted object | 300 | 2 | 293 |

The projection emits **45 canonical notes** from **68 evidence bindings** referring to **65 unique retained records**. The decision catalog marks **21 manual identity merges** and **19 Mathia/qwen cross-status merges** for exhaustive review.

Of the 234 qwen atlas entries, 24 are direct positive evidence and 210 are not emitted as standalone nodes. The latter are predominantly formalization prerequisites/components or records already represented at a coarser canonical granularity. All 11 entries classified `equivalent-to-RH` in the pinned atlas are represented. One qwen source record is used directly to bind a preprint/publication identity.

Across Mathia, accepted source-role objects remain provenance parents rather than one-note-per-source candidates. Accepted interpretations and syntheses not selected above repeat a canonical entity, operate below research-facing granularity, or fall outside the bounded Riemann/reusable-mechanism projection. Rejected, quarantined, evaluation-only, and superseded records are never positive evidence.

The OpenAlex graph's accepted works were considered as the discovery/identity universe. Its mathematical claims were not projected directly; only later accepted Mathia semantic objects can support note prose. The graph's 104 duplicate groups are retained as duplicate/version evidence, not converted into mathematical relations.

## Local artifact availability

The following manifest-derived roots were present at Checkpoint A. They were used only within the issue's identity/citation ambiguity boundary and are not required to read or recheck the committed projection:

- `/workspace/mathia-artifacts/riemann-corpus-v0`
- `/workspace/mathia-artifacts/riemann-corpus-v2`
- `/workspace/mathia-artifacts/agnostic-mathia-openalex-supplement-v1`
- `/mnt/openalex/openalex/handoffs/riemann_fulltext_v2`
- `/mnt/openalex/openalex/handoffs/agnostic_mathia_fulltext_v2`

No referenced evidence family was unavailable during this execution.

## Unresolved canonicalization

- **Vasyunin-sum identity for the retained generalized Dedekind-sum correlation — not merged.** The accepted object supports a modified generalized Dedekind sum and its reciprocity law but does not bind that convention to every Vasyunin-sum identity.
- **Grunsky-Schiffer theory — not emitted.** The issue lists it only as a granularity example; the selected accepted projection evidence does not support a stable standalone note without fresh analysis.

## Known blind spots

- This is a projection of retained accepted analyses, not a claim of bibliographic or mathematical completeness.
- The OpenAlex discovery graph contributes identity and citation coverage, but graph membership alone cannot support mathematical prose.
- Unprocessed or unavailable source text was not reacquired or mined for new claims; formula-damaged accepted units were summarized only at their audited prose-level boundary.
- qwen formalization status is pinned to one repository revision and records availability/status, not independent proof verification by this projection.

No new acquisition, API crawl, web search, or analysis of previously unprocessed source text was performed. No raw full-text payload is included in this projection.

## Independent-review census

The metadata places 41 notes in the exhaustive cohort because they carry a strong RH relation, a proof-status statement, an ambiguous/manual merge, or a Mathia/qwen cross-status merge. The remaining 4 notes are all selected for the deterministic sample, so the sample is 100% of the remainder (and therefore at least 20%):

- [Bost-Connes system](bost-connes-system.md) (`PA-bost-connes-system`)
- [Completed xi and Hardy Z representations](completed-xi-and-hardy-z-representations.md) (`PA-completed-xi-and-hardy-z-representations`)
- [Morita equivalence as geometry-preserving presentation](morita-equivalence-as-geometry-preserving-presentation.md) (`PA-morita-equivalence-as-geometry-preserving-presentation`)
- [Multiparameter persistence classification obstruction](multiparameter-persistence-classification-obstruction.md) (`PA-multiparameter-persistence-classification-obstruction`)

Together these cohorts require the fresh reviewer to inspect all emitted notes, which necessarily spans Mathia, qwen, cross-domain sources, topics, and both single- and multi-evidence nodes.
