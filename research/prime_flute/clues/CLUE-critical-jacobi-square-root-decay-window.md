---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical.md
  - research/prime_flute/findings/PF-249-positive-separation-preserves-free-jacobi-square-root-threshold.md
  - research/prime_flute/findings/PF-250-half-line-fractional-edge-powers-retain-supercritical-separated-window.md
  - research/prime_flute/findings/PF-251-exact-zero-edge-solutions-select-growing-inverse-square-jacobi-branch.md
  - research/prime_flute/findings/PF-252-zero-edge-ground-state-transform-has-bessel-four-scaling.md
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/findings/PF-254-normalized-noncommuting-robin-injection-splits-square-root-amplitude-from-polar-transport.md
  - research/prime_flute/findings/PF-255-hypercycle-compactification-transport-is-a-parity-local-flow-with-a-two-derivative-leakage-bound.md
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Can the fixed-axis actual relative seam and residual polar transport spend the Jacobi square-root margin?

## Observation

PF-247 reduces the fixed-axis compactification to two asymptotically constant parity Jacobi chains. PF-251--PF-253 identify the exact critical branch: the zero-edge positive solution grows like `j^{3/2}`, its ground-state transform has Bessel-four scaling, and for `0<\sigma<1` the actual parity chains satisfy

\[
\left|\langle e_i,J_\varepsilon^\sigma e_j\rangle\right|
\asymp
(i+1)^{3/2}(j+1)^{-5/2-2\sigma}
\]

in the separated cone, with the sharp fixed-output window

\[
E_dJ_\varepsilon^\sigma N^R\in\mathcal S_2
\iff R<2+2\sigma.
\]

In particular, a literal Jacobi square root has the proven window `R<3`, well above PF-243's required `R>1`.

PF-254 settles the algebraic Robin factorization. For any bounded positive regularization of a transverse operator `K` and seam normalizer `Q`, with relative seam

\[
\mathcal R=K^{-1/2}QK^{-1/2},
\]

the normalized Robin injection factors exactly as

\[
(K+Q)^{-1}Q^{1/2}
=K^{-1/2}h(\mathcal R)U,
\qquad
h(\lambda)=\frac{\sqrt\lambda}{1+\lambda},
\]

where `U` is the polar partial isometry of `K^{-1/2}Q^{1/2}`. Thus the positive relative amplitude always has a square-root zero edge; the only possible loss beyond that amplitude is spectral orientation.

PF-255 now removes a substantial geometric part of that orientation risk. PF-235's width-dependent hypercycle footpoint map becomes, after the fixed compactification, the exact half-density flow

\[
(V_cf)(\theta)=\sqrt{F_c'(\theta)}f(F_c(\theta)),
\qquad
\cot F_c(\theta)=e^{-c}\cot\theta,
\qquad
c=\tfrac12\log(1+w^2),
\]

whose generator is parity tridiagonal in the PF-247 Gegenbauer basis. With `K_0=A^{1/2}`, PF-255 proves

\[
\|E_{\le M}V_cE_{\ge N}\|
\le(1+w^2)^3(M/N)^2
\]

and therefore

\[
K_0e^{-dK_0}V_cK_0^R E_{>Z}\in\mathcal B
\qquad(0\le R\le2).
\]

The accompanying scalar-trace and physical-density factors have the same order-two graph locality. Hence the canonical `O(w^2)` hypercycle transport cannot itself realize PF-244's arbitrary high-to-low leakage. The live uncertainty is now narrower: the **fixed-axis intrinsic seam relative to the actual corridor operator `K_a`**, together with the transfer of locality from the PF-247 `A/J` calculus to `T_a=K_a^2`.

## Research question

For the actual fixed-axis complete-lift seam, what are the exact relative operator and residual polar transport

\[
\mathcal R_w=K_a^{-1/2}Q_w^{\rm act}K_a^{-1/2},
\qquad
K_a^{-1/2}(Q_w^{\rm act})^{1/2}=\mathcal R_w^{1/2}U_w,
\]

after factoring out the PF-255-controlled hypercycle coordinate/density transport?

Can the remaining fixed-axis seam be reduced to or compared with PF-247's parity Jacobi operator strongly enough that PF-253 controls `h(\mathcal R_w)`, and can the residual orientation relative to `K_a` preserve some exponent `R>1`? In particular, can one prove a graph-domain/commutator bridge between `T_a` and `A` strong enough to transfer the locality that form comparison alone cannot provide?

## Why it may matter

PF-243 reduces the remaining high-high shear gate to one-sided separated Robin-Poisson smoothing of any fixed order `R>1`. PF-254 gives a sharp square-root positive-amplitude mechanism with an `R<3` Jacobi budget, while PF-255 proves that the prime-dependent hypercycle reparameterization itself preserves a concrete `1<R<2` supercritical window relative to the fixed-axis transverse scale. Therefore the width-dependent geometric transport no longer has to be treated as an arbitrary polar factor consuming the entire margin.

A positive theorem can now focus on fewer genuinely noncommuting objects: the intrinsic seam after fixed compactification, PF-247's `A/L/J` structure, and PF-233's actual `T_a`. A negative result is equally decisive: if the passage from this fixed-axis seam to `K_a` creates a PF-244-type high-to-low tail, then the present local transfer route fails even though both the Jacobi square-root kernel and the hypercycle transport separately have enough margin.

## Decisive test

Work first in the fixed-axis `L^2((0,\pi),d\theta)` realization and explicitly factor the actual seam/corridor source map so that all PF-255 hypercycle coordinate and density operators are outside the unresolved polar block. Do not re-estimate those factors abstractly; use PF-255's order-two graph locality.

For the residual block, derive the relative seam against `K_a=T_a^{1/2}` directly from PF-233/PF-238/PF-243. Establish either:

- a graph-domain/commutator comparison strong enough to transfer high-to-low estimates between `A^{1/2}` and `K_a`; or
- a direct fixed-axis factorization showing that `h(\mathcal R_w)U_wK_a^RP_Z` remains controlled for some uniform `R>1` before separated propagation.

If the Jacobi comparison carries the square-root term, use PF-253's `R<3` window as the positive-amplitude budget and account explicitly for what the `A\leftrightarrow T_a` bridge consumes. PF-255 already shows that the later canonical hypercycle coordinate/density transport need not consume more than the available supercritical margin at the pure-transport level.

Kill the route if the fixed-axis relative seam has a different low-edge mechanism that invalidates the PF-253 comparison, if the residual polar factor relative to `K_a` creates a non-summable high-to-low tail defeating every `R>1`, or if the required unbounded/form limit loses the finite-regularization estimate. Do not reopen either the already settled literal `J_\varepsilon^{1/2}` decay question or the now-controlled PF-235 hypercycle-transport leakage question.

## Evidence boundary

PF-253 proves the actual parity-Jacobi fractional kernel and the sharp square-root window `R<3`. PF-254 proves, on bounded positive regularizations, that the positive normalized Robin injection is universally `h(\mathcal R)=\mathcal R^{1/2}(I+\mathcal R)^{-1}` followed by a polar transport `U`. PF-255 proves that the PF-235 width-dependent hypercycle coordinate/density transport is parity-preserving, graph-local to two `A^{1/2}` derivatives, and harmless for pure separated propagation through every `R\le2`.

None of these findings proves that the actual fixed-axis complete-lift relative seam `\mathcal R_w` equals or is asymptotically equivalent to `J_\varepsilon`, that PF-233's form comparison `T_a\asymp s^2A` transfers spectral off-diagonal locality, or that the **residual** `U_w` is local enough in the actual `K_a` modes. PF-254 also does not by itself justify the full unbounded form limit. No separated smoothing theorem for the complete PF-243 Poisson map, and no new theorem about zeta zeros or RH, is established yet.

## Research disposition

Accepted for continued investigation. The clue has narrowed again: the positive Robin edge is square-root, and the prime-dependent hypercycle footpoint/density transport now has an explicit two-derivative leakage barrier. The unresolved theorem is the **fixed-axis actual-seam/Jacobi comparison plus transfer of polar locality from `A` to the actual `K_a` realization**. Resolution requires either a uniform `R>1` estimate for that residual combined factor or an actual-seam/`K_a` obstruction showing that such an estimate cannot hold.