---
id: PA-riemann-explicit-formula
type: prior-art
canonical_name: "Riemann explicit formula"
aliases:
  - "von Mangoldt explicit formula"
kind: theorem-family
topics:
  - riemann-hypothesis
  - explicit-formula
  - prime-zero-duality
---

# Riemann explicit formula

## What it is

A family of exact identities expressing weighted prime-counting data through the pole and zeros of zeta together with local correction terms. In the retained Mathia view, a transform places the same test function on the prime and zero sides; the function-field analogue admits a Lefschetz trace interpretation.

## Relation to RH / Mathia research

The explicit formula is a central bridge rather than an RH equivalence by itself. It makes proposed spectral, positivity, and geometric mechanisms answerable against the exact arithmetic terms they must reproduce.

## Known scope and limits

The identity does not force critical-line zero location. Test-function hypotheses, smoothing, local terms, signs, and convergence cannot be dropped, and qwen reports no located complete Lean proof of the theorem family.

## Related prior art

- [Weil positivity criterion](weil-positivity-criterion.md) — `used_by`
- [Connes adele-class trace program](connes-adele-class-trace-program.md) — `used_by`

## Evidence and provenance

- **Riemann–Mathia v2 accepted object:** `experiments/riemann_corpus/full_corpus_v2/objects.jsonl#mathia_interpretation_e6e5530160066dd21f70f6142869ef61feb8145f9476c88b9e371df0e193d7c4`; source `bombieri2000_clay`; unit `bombieri2000_u02_explicit_trace_dictionary`.
- **qwen-lean Riemann atlas:** `murillo128/qwen-lean@3364b508595a71b34a2efcf964ba1200f153ad84:data/riemann/atlas/entries.jsonl#explicit-formula`; entry; source `riemann-1859`, `titchmarsh-zeta`.
- **Projection decision:** `research/prior_art/catalog.json#PA-riemann-explicit-formula`.
