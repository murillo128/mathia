---
id: PA-lagarias-criterion
type: prior-art
canonical_name: "Lagarias criterion"
aliases:
  - "Lagarias elementary criterion"
kind: criterion
topics:
  - riemann-hypothesis
  - divisor-sums
  - harmonic-numbers
---

# Lagarias criterion

## What it is

An inequality involving the divisor-sum function and harmonic numbers, required for every positive integer with a specified equality case. The retained Mathia analysis emphasizes the move from zeta zeros to elementary-looking arithmetic observables.

## Relation to RH / Mathia research

The qwen atlas and Mathia source both record the inequality as equivalent to RH. It is a useful stress test for whether a change of surface representation has actually reduced difficulty.

## Known scope and limits

The criterion is not an elementary proof of RH; its equivalence runs through Robin's criterion and deeper analytic results. No Lean proof of the equivalence is recorded.

## Related prior art

- [Robin criterion](robin-criterion.md) — `uses`

## Evidence and provenance

- **Riemann–Mathia v2 accepted object:** `experiments/riemann_corpus/full_corpus_v2/objects.jsonl#mathia_interpretation_d4cba222ec15eb773f51dc5704d2440c423a9dc3b4f46da8fa373f94cc2e12ad`; source `lagarias2002_elementary`; unit `lagarias2002_u01_elementary_equivalence_v1`.
- **qwen-lean Riemann atlas:** `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84:data/riemann/atlas/entries.jsonl#lagarias-criterion`; entry; source `lagarias-2002`.
- **Projection decision:** `research/prior_art/catalog.json#PA-lagarias-criterion`.
