---
id: PA-chebyshev-psi-error-criterion
type: prior-art
canonical_name: "Chebyshev psi error criterion"
aliases:
  - "von Mangoldt summatory error criterion"
kind: criterion
topics:
  - riemann-hypothesis
  - prime-counting
  - von-mangoldt
---

# Chebyshev psi error criterion

## What it is

A quantitative prime-power counting statement controlling the error of the Chebyshev psi function at square-root scale with logarithmic loss. Mathia treats it as the main-term-error counterpart to Möbius sign cancellation.

## Relation to RH / Mathia research

The qwen atlas records the stated error bound as equivalent to RH. It is a canonical arithmetic target for explicit-formula routes.

## Known scope and limits

This criterion is distinct from the prime-counting Li(x) error form and from finite-range explicit inequalities. None of the retained evidence proves the bound or records a complete Lean formalization.

## Related prior art

- [Riemann explicit formula](riemann-explicit-formula.md) — `uses`
- [von Koch prime-counting error criterion](von-koch-prime-counting-error-criterion.md) — `equivalent_to`

## Evidence and provenance

- **Riemann–Mathia v2 accepted object:** `experiments/riemann_corpus/full_corpus_v2/objects.jsonl#mathia_interpretation_ff10988b73232ae17e7eb2749d2af47748bb4a5d16b0add22b18564106912fd6`; source `aim2004_resource`; unit `aim2004_u21_mangoldt_mobius_cancellation`.
- **qwen-lean Riemann atlas:** `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84:data/riemann/atlas/entries.jsonl#psi-error-criterion`; entry; source `titchmarsh-zeta`.
- **Projection decision:** `research/prior_art/catalog.json#PA-chebyshev-psi-error-criterion`.
