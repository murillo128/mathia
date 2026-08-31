---
type: adversarial-review
target: research/prime_circle/findings/PC-082-higher-hardy-cyclic-traces-are-critical-cyclotomic-cone-periods.md
---

# Adversarial review

## Adversary

The boxed identity in §2 identifies the Abel limit of the radial traces with the ordinary operator trace
`Tr(H_{alpha_1} ... H_{alpha_k})`. The displayed argument does not currently establish that identification. Dominated convergence applies to the scalar cube integrals for `r < 1` and proves that those **radial trace values** have the stated limit, while PC-080/PC-081 establish that the boundary product itself is trace class. What is missing is a trace-continuity bridge between those two facts: for example,

`H_{alpha_1,r} ... H_{alpha_k,r} -> H_{alpha_1} ... H_{alpha_k}` in `S_1`,

or an equivalent factorization/approximation theorem that implies convergence of the traces. Strong convergence of the bounded radial cutoffs, even together with trace-classness of the limiting product, is not by itself enough to justify trace convergence, and PC-080's proof of trace-classness for separated boundary channels does not state this radial `S_1` convergence.

This is material because the finding labels the cube period and the subsequent shell sums as exact **ordinary cyclic traces**, not merely Abel-regularized traces. To resolve the objection, prove a trace-norm (or otherwise trace-continuous) passage from the radial products to the separated boundary product, possibly by strengthening the smooth-kernel argument behind PC-080, or weaken the affected statements to Abel-regularized trace identities until such a bridge is supplied.
