---
id: PA-de-bruijn-newman-deformation
type: prior-art
canonical_name: "De Bruijn-Newman deformation"
aliases:
  - "De Bruijn-Newman constant"
  - "De Bruijn-Newman criterion"
kind: criterion-and-partial-result
topics:
  - riemann-hypothesis
  - heat-flow
  - xi-function
---

# De Bruijn-Newman deformation

## What it is

A one-parameter heat-flow deformation of the completed xi function with a threshold Λ separating the real-rooted regime from the regime containing nonreal zeros. The deformation turns a static zero-location question into a boundary problem in function space.

## Relation to RH / Mathia research

RH is equivalent to Λ ≤ 0, while the Rodgers–Tao result recorded in both retained views proves the complementary bound Λ ≥ 0. The Mathia analysis treats the contradiction mechanism as a clash between forced local equilibrium under Λ < 0 and known local zero statistics.

## Known scope and limits

The proved lower bound does not prove RH; together with RH it would force Λ = 0. Historical numerical bounds in older source units are not treated as current evidence, and no Lean formalization is claimed.

## Related prior art

- [Montgomery pair correlation](montgomery-pair-correlation.md) — `uses`

## Evidence and provenance

- **Riemann–Mathia v2 accepted object:** `experiments/riemann_corpus/full_corpus_v2/objects.jsonl#mathia_interpretation_18a74509476a3a7765ae396d450fe89f5d4d423b6002d5b7800abab1d46f5a12`; source `rodgers_tao2020_newman`; unit `rodgers2020_u01_heat_flow_boundary`.
- **qwen-lean Riemann atlas:** `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84:data/riemann/atlas/entries.jsonl#debruijn-newman`; entry; source `rodgers-tao-2018`.
- **Projection decision:** `research/prior_art/catalog.json#PA-de-bruijn-newman-deformation`.
