---
id: RA-frontier-telemetry-v1
type: riemann-atlas-frontier-telemetry
atlas_version: 1
prospective_source_cutoff: 7a97f9e03e220ef24ef454890e1899b047326b3f
derived: true
---

# Frontier fertility telemetry

This is **derived strategic telemetry, not mathematical evidence**. It measures the marginal character of source-backed research expansions without changing Research Watch scope, finding gates, clue disposition, or task allocation. Atlas territory mass continues to measure the map; frontier episodes measure marginal research outcomes and are never multiplied by territory mass merely because the same territory is revisited.

The canonical event set is [[research/graph/atlas/telemetry/frontier-events.jsonl|frontier-events.jsonl]]. Each event is one source-backed movement on one discriminating frontier question, and may cite several findings when those findings form one coherent episode. Raw finding counts are deliberately not used.

## Retrospective seed

A conservative retrospective backfill covers only high-confidence episodes reconstructable from surviving canonical findings and material Graph Curator windows after the Riemann Atlas v1 bootstrap. It is intentionally incomplete: ambiguous historical moves, withdrawn/challenged claims, and outcomes that cannot be classified without hindsight are omitted rather than guessed.

| Line | Episodes | Viable extension | Known prior art | New barrier |
| --- | ---: | ---: | ---: | ---: |
| `arithmetic_fidelity` | 1 | 0 | 0 | 1 |
| `prime_circle` | 2 | 0 | 0 | 2 |
| `prime_flute` | 2 | 2 | 0 | 0 |
| `prime_lattice` | 2 | 0 | 1 | 1 |
| `weil_inertia` | 3 | 0 | 1 | 2 |
| `weil_positivity` | 4 | 1 | 0 | 3 |
| **Total** | **14** | **3** | **2** | **9** |

For this **retrospective partial sample only**:

- `FrontierFertilityEpisodes = 3 / 14 = 21.4%`
- `BarrierRate = 9 / 14 = 64.3%`
- `PriorArtCollisionRate = 2 / 14 = 14.3%`
- `InternalDuplicateRate = 0 / 14 = 0%`

No `new-territory`, `known-barrier`, `internal-duplicate`, or `insufficient-evidence` episode was persisted in this deliberately small backfill. That absence is not evidence that those outcomes did not occur historically.

## Prospective series

The clean prospective series starts strictly **after** `prospective_source_cutoff`. Source mutations at or before that revision are never relabeled as prospective merely because a later Graph Curator pass first sees them. Any gap between the conservative retrospective seed and the cutoff remains unclassified unless a later high-confidence backfill adds those outcomes explicitly as `mode: retrospective`.

The first prospective curator window, from the previous material curator state through source revision `864892d112c83929158a3a99aaf07ab962e5a288`, contains the following classifiable episodes:

| Line | Episodes | Viable extension | Known prior art | New barrier |
| --- | ---: | ---: | ---: | ---: |
| `arithmetic_fidelity` | 2 | 2 | 0 | 0 |
| `prime_circle` | 2 | 0 | 1 | 1 |
| `prime_flute` | 2 | 2 | 0 | 0 |
| `prime_lattice` | 3 | 0 | 1 | 2 |
| `weil_inertia` | 2 | 0 | 0 | 2 |
| `weil_positivity` | 2 | 0 | 0 | 2 |
| **Total** | **13** | **4** | **2** | **7** |

For this **prospective sample**:

- `FrontierFertilityEpisodes = 4 / 13 = 30.8%`
- `BarrierRate = 7 / 13 = 53.8%`
- `PriorArtCollisionRate = 2 / 13 = 15.4%`
- `InternalDuplicateRate = 0 / 13 = 0%`
- `InsufficientEvidence = 0`

The prospective unit is deliberately coarser than a finding. For example, PL-083--PL-085 are one critical-bulk episode, PF-143--PF-145 are one collar-interface episode, and WP-078--WP-080 are one Möbius/coinvariant repair episode. This prevents activity volume from masquerading as fertility.

The current window is **barrier-heavy but mixed**: Arithmetic Fidelity and Prime Flute account for all four viable extensions, while Prime Circle, Prime Lattice, Weil Inertia and Weil Positivity mostly narrow or classicalize already-live routes. With only 13 prospective classifiable episodes, this is an early signal rather than a stable portfolio trend.

## Interpretation boundary

A low frontier-fertility ratio can mean a line is successfully closing a difficult search space, not that the work is worthless. A high ratio can reflect productive extension without bringing RH closer to proof. The telemetry exists to distinguish **marginal frontier movement** from unchanged coarse Atlas states; canonical findings, review outcomes, prior art, and exact live questions remain the basis for mathematical and portfolio judgments.

The telemetry must not feed Research Watch. It may be consumed by the Master Researcher only as derived strategic context under its own rules, and no ratio alone can justify pausing, merging, splitting, redirecting, or creating research lines.
