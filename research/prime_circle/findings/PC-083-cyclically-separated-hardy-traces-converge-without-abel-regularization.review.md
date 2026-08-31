---
type: adversarial-review
target: research/prime_circle/findings/PC-083-cyclically-separated-hardy-traces-converge-without-abel-regularization.md
---

# Adversarial review

## Adversary

The root-channel theorem is quantified over `alpha_1,...,alpha_k` without a lower bound on `k`, so as written it includes `k=1`. That case is a counterexample to the displayed identification with an ordinary operator trace. Take, for example, a primitive cubic root `alpha`; then the stated cyclic-separation condition is `alpha^2 != 1`, which holds, and the finite diagonal sums

\[
\operatorname{Tr}(P_N\mathcal H_\alpha P_N)
=\sum_{j=0}^N\frac{\alpha^{2j+1}}{2j+1}
\]

indeed converge conditionally by the same geometric/Dirichlet mechanism. But

\[
\mathcal H_\alpha=\alpha D_\alpha H D_\alpha
\]

with `D_alpha` unitary, so `mathcal H_alpha` has the same singular values as the classical Hilbert matrix `H`; in particular it is not trace class (indeed the Hilbert matrix is not compact). Hence `Tr(mathcal H_alpha)` is not an ordinary trace, even though the finite-section scalar limit and the one-dimensional cube integral exist.

This is material because the headline and boxed root-channel statement say that *every* cyclically separated root word converges to `Tr(product)`, while the proof only establishes a finite-section scalar limit unless trace-classness of the limiting product is available. If the intended theorem is only for words of length `k>=2` (which is consistent with the distinct-shell application), that hypothesis needs to be made explicit and the trace-class bridge for that domain should be the one being invoked. Alternatively, if `k=1` is intentionally included, the right-hand side cannot be called the ordinary operator trace without a separately defined conditional trace notion.