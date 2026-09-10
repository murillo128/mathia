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
  - research/prime_flute/findings/PF-256-variable-corridor-graph-equivalence-transfers-two-derivative-locality-to-the-actual-transverse-scale.md
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

PF-255 removes the width-dependent hypercycle map as an arbitrary orientation risk. After fixed compactification its half-density transport `V_c` is a parity-local flow and has two derivatives of high-to-low protection relative to `K_0=A^{1/2}`.

PF-256 now closes the separate `A\leftrightarrow T_a` transport caveat for such already graph-local factors. With `P_a=s^{-2}T_a`, the canonical hypercycle width gives

\[
\operatorname{Dom}(P_a)=\operatorname{Dom}(A),
\qquad
\|P_ay\|\asymp\|Ay\|
\]

uniformly on the tail, and the fixed-axis/actual-corridor change of spectral basis has an order-two separated leakage bound. Consequently PF-255's `V_c` and its scalar density factors obey the same two-derivative high-to-low bound directly in the actual `K_a=T_a^{1/2}` modes. The passage from `A` to `T_a` therefore costs constants but no derivative order for those factors.

The live uncertainty is now narrower still: the **fixed-axis intrinsic seam itself**, expressed relative to `K_a`, and the polar orientation in PF-254. Neither the canonical hypercycle coordinate/density transport nor the variable-corridor spectral-basis change is any longer an independent candidate for PF-244's catastrophic high-to-low mixing.

## Research question

For the actual fixed-axis complete-lift seam, what are the exact relative operator and residual polar transport

\[
\mathcal R_w=K_a^{-1/2}Q_w^{\rm act}K_a^{-1/2},
\qquad
K_a^{-1/2}(Q_w^{\rm act})^{1/2}=\mathcal R_w^{1/2}U_w,
\]

after factoring out the PF-255/PF-256-controlled hypercycle coordinate/density transport?

Can the remaining fixed-axis seam be reduced to PF-247's parity-Jacobi structure strongly enough that PF-253 controls the square-root edge of `h(\mathcal R_w)`, and can the **residual seam polar factor** preserve some exponent `R>1` in the actual `K_a` modes? The missing bridge is no longer generic `A\leftrightarrow T_a` graph equivalence; PF-256 supplies that for operators already possessing two-derivative `A` graph locality. What remains is to prove that the seam/Jacobi functional factor and its polar orientation possess the required locality in the first place.

## Why it may matter

PF-243 reduces the remaining high-high shear gate to one-sided separated Robin-Poisson smoothing of any fixed order `R>1`. PF-254 gives a square-root positive-amplitude mechanism with an `R<3` Jacobi budget. PF-255 and PF-256 together show that the prime-dependent hypercycle transport preserves a concrete `1<R<2` supercritical window all the way to the actual variable-corridor `K_a` scale.

A positive theorem can therefore concentrate on one genuinely noncommutative source of unsmoothed orientation: the fixed-axis actual seam relative to `K_a`. A negative result is equally decisive. If that seam/Jacobi functional calculus or its polar factor creates a non-summable high-to-low tail, then the present local transfer route fails even though the Jacobi square-root kernel, hypercycle geometry, and `A\leftrightarrow T_a` transport separately have enough margin.

## Decisive test

Work in the fixed-axis `L^2((0,\pi),d\theta)` realization. Factor the actual seam/corridor source map so that PF-255's hypercycle coordinate/density operators are outside the unresolved polar block, and use PF-256 to transfer their already-proved graph locality to `K_a`; do not re-open either issue through form comparison.

For the residual fixed-axis seam, derive `\mathcal R_w` and `U_w` directly from PF-233/PF-238/PF-243. Establish one of the following:

- an exact operator dictionary from the seam relative variable to PF-247's `J_\varepsilon` (or a controlled functional perturbation of it) that is strong enough to transport PF-253's square-root kernel and to bound the residual polar orientation; or
- a direct estimate showing that `h(\mathcal R_w)U_wK_a^RP_Z` remains controlled for some uniform `R>1` before separated propagation.

If PF-253 supplies the square-root term, account explicitly for every conjugation surrounding it and use PF-256 only for factors that satisfy its two-sided graph-locality hypothesis. Form order or eigenvalue comparability alone still does not authorize a fractional-kernel transfer.

Kill the route if the fixed-axis relative seam has a different low-edge mechanism that invalidates the PF-253 comparison, if the residual `U_w` creates a non-summable high-to-low tail defeating every `R>1`, or if the full unbounded/form realization loses the finite-regularization factorization. Do not reopen the literal `J_\varepsilon^{1/2}` decay, PF-235 hypercycle leakage, or the `A\leftrightarrow T_a` transfer for already graph-local factors.

## Evidence boundary

PF-253 proves the actual parity-Jacobi fractional kernel and the sharp square-root window `R<3`. PF-254 proves, on bounded positive regularizations, that the positive normalized Robin injection is universally `h(\mathcal R)=\mathcal R^{1/2}(I+\mathcal R)^{-1}` followed by a polar transport `U`. PF-255 proves two-derivative `A`-graph locality for the width-dependent hypercycle coordinate/density transport. PF-256 proves that the canonical variable corridor has the same operator domain as `A` after scale normalization, with uniformly equivalent graph norms, and therefore transfers that already-established two-derivative locality to the actual `K_a` modes without derivative loss.

None of these findings proves that the actual fixed-axis complete-lift relative seam `\mathcal R_w` equals or is a sufficiently controlled function/perturbation of `J_\varepsilon`, that PF-253's fractional kernel survives the exact seam dictionary, or that the residual `U_w` is graph-local enough in the actual `K_a` modes. PF-254 also does not by itself justify the full unbounded form limit. No separated smoothing theorem for the complete PF-243 Poisson map, and no new theorem about zeta zeros or RH, is established yet.

## Research disposition

Accepted for continued investigation. The clue has narrowed materially again: the positive Robin edge is square-root; the prime-dependent hypercycle transport has an explicit two-derivative leakage barrier; and PF-256 transports that barrier to the actual variable-corridor spectral scale. The unresolved theorem is now the **fixed-axis seam/Jacobi functional dictionary plus the residual polar orientation of that seam relative to `K_a`**. Resolution requires either a uniform `R>1` estimate for that residual combined factor or an actual-seam obstruction showing that such an estimate cannot hold.