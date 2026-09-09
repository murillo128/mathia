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
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Can the actual relative seam and polar transport spend the Jacobi square-root margin?

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

PF-254 now settles the first algebraic part of the Robin-factor question. For any bounded positive regularization of a transverse operator `K` and seam normalizer `Q`, with relative seam

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

where `U` is the polar partial isometry of `K^{-1/2}Q^{1/2}`. Thus the positive relative amplitude **always** has a square-root zero edge. The live uncertainty is no longer the scalar edge exponent. It is whether the actual complete-lift relative seam `\mathcal R_w` is controlled by PF-247's `J_\varepsilon`, and whether the accompanying polar transport `U_w` preserves enough transverse locality before separated propagation begins.

## Research question

For the actual fixed-axis complete-lift seam, what are the exact relative operator and polar transport

\[
\mathcal R_w=K_a^{-1/2}Q_w^{\rm act}K_a^{-1/2},
\qquad
K_a^{-1/2}(Q_w^{\rm act})^{1/2}=\mathcal R_w^{1/2}U_w,
\]

in the correct form/spectral realization?

Can `\mathcal R_w` be reduced to or compared with PF-247's parity Jacobi operator strongly enough that PF-253 controls `h(\mathcal R_w)`, and can the high-to-low blocks of `U_w` be bounded strongly enough that some separated exponent `R>1` survives? The target is not a general theorem for arbitrary noncommuting Robin data; it is the actual complete-lift seam after fixed-axis compactification.

## Why it may matter

PF-243 reduces the remaining high-high shear gate to one-sided separated Robin-Poisson smoothing of any fixed order `R>1`. PF-254 removes a major ambiguity in that gate: Robin normalization itself does not introduce a worse positive edge than a square root. If the actual relative seam inherits the PF-247/PF-253 Jacobi edge and `U_w` is spectrally local enough, the available positive-amplitude budget is the sharp `R<3` square-root window, leaving substantial room for the later `K_a` replacement, Hardy ends, and PF-235 `O(w^2)` geometric defect.

A negative result is equally decisive. PF-244 already proves that an uncontrolled noncommuting square root can rotate high input into low modes before propagation. PF-254 localizes that risk: if the actual `U_w` has sufficiently large high-to-low blocks, or if `\mathcal R_w` is not Jacobi-controlled at the relevant edge, the present fixed-axis transfer route fails even though PF-253 remains true.

## Decisive test

Derive `(\mathcal R_w,U_w)` directly from the PF-238/PF-243 actual seam, without replacing it by the commuting matched seam. Work first on the canonical finite spectral/form regularizations where PF-254 is exact, then prove the uniform estimates needed to pass to the actual realization.

Establish an explicit low-edge comparison between `\mathcal R_w` and `J_\varepsilon` and an off-diagonal/locality estimate for `U_w` sufficient to control

\[
E_d\,h(\mathcal R_w)U_wK_a^RP_Z
\]

for some uniform `R>1`. If the Jacobi comparison carries the square-root term, use PF-253's `R<3` window as the exponent budget and quantify what is consumed by all remaining fixed-axis factors before spending margin on geometric perturbations.

Kill the route if the actual relative seam has a different low-edge mechanism that invalidates the PF-253 comparison, if `U_w` creates a non-summable high-to-low tail defeating every `R>1`, or if the required unbounded/form limit loses the finite-regularization estimate. Do not reopen the already settled question of whether literal `J_\varepsilon^{1/2}` has enough separated decay.

## Evidence boundary

PF-253 proves the actual parity-Jacobi fractional kernel and the sharp square-root window `R<3`. PF-254 proves, on bounded positive regularizations, that the positive normalized Robin injection is universally `h(\mathcal R)=\mathcal R^{1/2}(I+\mathcal R)^{-1}` followed by a polar transport `U`.

Neither finding proves that the actual complete-lift relative seam `\mathcal R_w` equals or is asymptotically equivalent to `J_\varepsilon`, nor that `U_w` is local, banded, pseudolocal, order zero, or harmless for high-to-low conversion. PF-254 also does not by itself justify the full unbounded form limit. No separated smoothing theorem for the actual PF-243 Poisson map, and no new theorem about zeta zeros or RH, is established yet.

## Research disposition

Accepted for continued investigation. The clue has narrowed materially: the positive Robin edge is now known to be square-root in the relative seam variable, so the unresolved work is the **actual relative-seam/Jacobi comparison plus polar-transport locality**. Resolution requires either a uniform `R>1` estimate for that combined factor in the complete-lift realization or an actual-seam obstruction showing that such an estimate cannot hold.