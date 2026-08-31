---
id: RA-frontier-telemetry-v1
type: riemann-atlas-frontier-telemetry
atlas_version: 1
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

The retrospective vector is useful as a warning that unchanged Atlas state masses can coexist with substantial local barrier concentration. It is **not** a calibrated historical productivity score and must not be mixed silently with the prospective series.

## Prospective baseline

The clean prospective series starts with the first material Graph Curator delta after this telemetry was introduced. From that point onward the curator records each newly observed, source-backed frontier episode as `mode: prospective`, repairs or removes an episode if its canonical support is corrected/withdrawn, and leaves the telemetry unchanged when a run contains no material expansion outcome.

Until enough prospective episodes exist, report the sample size together with every ratio. For line-local interpretation, prefer a fixed trailing window of up to the latest 10 classifiable prospective episodes; for portfolio interpretation, prefer up to the latest 20. Never use the ratios alone to pause, merge, split, redirect, or create research lines.

## Interpretation boundary

A low frontier-fertility ratio can mean a line is successfully closing a difficult search space, not that the work is worthless. A high ratio can reflect productive extension without bringing RH closer to proof. The telemetry exists to distinguish **marginal frontier movement** from unchanged coarse Atlas states; canonical findings, review outcomes, prior art, and exact live questions remain the basis for mathematical and portfolio judgments.
