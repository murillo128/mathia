---
id: RA-metrics-v1
type: riemann-atlas-metrics
atlas_version: 1
source_revision: f29d898a0bc9fcda6e175d5bad80bc3dc1bd353c
derived: true
---

# Riemann Atlas v1 metrics

## State mass

| State | Mass |
| --- | ---: |
| unvisited | **22.5%** |
| active | **10.0%** |
| open | **36.8%** |
| reproduced | **16.5%** |
| soft-pruned | **3.0%** |
| hard-pruned | **11.2%** |

Thus:

- **AtlasCoverage = 77.5%**
- **LiveFrontier = 46.8%**
- **TotalPruned = 14.2%**
- live share of visited mass = **60.4%**
- pruned share of visited mass = **18.3%**
- hard-pruned share of all pruned mass = **78.9%**

The v1 denominator and territory states are unchanged by membership reconciliation and the scoped smooth-test conditional transfer refinement. Recomputed masses retain the values above. Complete membership is not complete semantic traversal, and no new territory state is inferred from added links.

## Atlas scope and confidence

The atlas retains 10 macro-families and 37 leaf territories. Its known-space taxonomy and masses are versioned modeling choices, not a percentage of RH solved. The world-literature denominator remains unknown; see [[research/graph/atlas/v1|v1 model and calibration]].

The five hard-pruned interfaces retain their existing scoped canonical evidence: ordinary Prime-Flute global Selberg/Ruelle machinery (3.0%), ordinary positive-calculus closures (2.5%), standard prime-shift covariance (2.5%), single-profile Gram compression (2.0%), and symmetric full-cover uniformization (1.2%). The Euler sampling refinement does not alter those closures.

## Structural and semantic scope

The exact tree projections contain 13 research lines, 5,007 findings, 828 durable intuitions and 64 prior-art notes. Membership changes and reversible source-reference formatting are graph maintenance, never frontier episodes. Semantic inspection remains selective as recorded in `research/graph/semantic-inspection.json`; uninspected source changes do not justify Atlas transitions.

## Frontier fertility

The retained prospective series contains **20** classifiable episodes and **0** insufficient-evidence episodes. MC-521 adds one conditional smooth-test transfer refinement; its full variance premise remains unproved unconditionally. MC-177's method-specific optimum and MC-520's RH converse are retained. The oldest retained episode leaves the fixed trailing window and remains in Git. This is a selected episode sample, not a census of the source window.

- **FrontierFertilityEpisodes = 35.0%**
- **BarrierRate = 50.0%**
- **PriorArtCollisionRate = 15.0%**
- **InternalDuplicateRate = 0.0%**

See [[research/graph/atlas/telemetry/frontier-summary|frontier telemetry]] for per-line sample sizes and [[research/graph/atlas/telemetry/frontier-events.jsonl|the event set]] for exact source provenance. Retrospective and prospective evidence are separate, and no metric alone justifies a portfolio decision.
