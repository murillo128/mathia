---
id: CLUE-weil-inertia-source-structured-proximal-mismatch-below-clipping
type: research-clue
status: proposed
origin: independent-review
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-179-offline-pair-count-caps-proximal-cancellation-rank.md
  - research/weil_inertia/findings/WI-180-full-gram-tail-is-screened-by-distinct-exception-count.md
  - research/weil_inertia/findings/WI-181-unit-trace-budget-gates-full-gram-tail-activation.md
  - research/weil_inertia/clues/CLUE-lamzouri-operator-schur-cancellation.md
---

# Can source geometry force a proximal mismatch even when the full-Gram rank tail vanishes?

## Observation

WI-181 imposes a quantitative activation gate on the extra full-Gram tail in WI-180. This suggests retaining the **actual source correction**, rather than continuing to optimize over every rank-allowed positive-semidefinite matrix. The distinction can be made exact and does not require an inverse horizontal Schur block.

Let `F: C^n -> M_0` synthesize the projected simple-real vectors `b_x`. Write `B=F*F`, `S=FF*`, and `U=F B^(-1/2)`, the unitary polar factor onto `M_0`. The positive definiteness of `B` is the finite independence property already used in WI-179. Let `A=G_s-B` and let `C` be the actual odd correction on `M_0`. Transport it to Gram coordinates:

\[
\widetilde C=U^*CU,\qquad Z=A+\widetilde C\succeq0.
\]

Here `Z` is a correction matrix, not the original multiset. Since `rank A<=r+k` and `rank C<=k`, `rank Z<=e=r+2k`. The pre-minimization remainder inequality becomes

\[
R\ge\|G_s-I-Z\|_{\rm HS}^2+2\operatorname{tr}Z.
\]

Put `Y=(G_s-2I)_+` and `Y_-=(2I-G_s)_+`. Completing the square gives

\[
\|G_s-I-Z\|_{\rm HS}^2+2\operatorname{tr}Z
=\operatorname{tr}\Psi(G_s)+\|Z-Y\|_{\rm HS}^2
+2\operatorname{tr}(Y_-Z).
\]

Consequently the source-specific excess over WI-180's rank-only relaxation is

\[
\Gamma_e:=\|Z-Y\|_{\rm HS}^2-\mathcal T_e(G_s)
+2\operatorname{tr}(Y_-Z)\ge0.
\]

Nonnegativity follows from low-rank approximation and positivity; no commutativity is assumed. A bound on `Gamma_e` would charge the source's distance from the relaxed optimizer, not merely another rank statistic. In particular, when `G_s <= (2-delta)I` with `delta>0`, the rank tail vanishes but

\[
\Gamma_e=\|Z\|_{\rm HS}^2+2\operatorname{tr}((2I-G_s)Z)
\ge\|Z\|_{\rm HS}^2+2\delta\operatorname{tr}Z.
\]

Thus there is an algebraic place for a source-forced charge below the eigenvalue-2 threshold. This observation alone does not furnish its source lower bound.

## Research question

Does the fact that `A` and `C` arise from the same conjugation-even/odd exponential feature system force a quantitative lower bound on `Gamma_e`, or on an appropriate part of it, which is unavailable after retaining only spectra and ranks? A useful target is an explicit lower bound derived from actual kernel overlaps, a coupled even/odd interpolation constraint, or a source-evaluable mixed moment. Specify whether the resulting charge concerns all exceptions, repeated critical zeros, or genuinely non-real pairs.

Do not repeat the resolved inverse-Schur proposal: that normalization collapses to an already known odd synthesis norm and has an isolated-pair counterexample. The present object uses no inverse horizontal block and asks about distance to the optimizer in the full, unit-trace Gram coordinates. It must still be compared with existing exact slack, affine-tax, and confluence barriers before promotion.

## Why it may matter

A source theorem for this mismatch could improve the finite budget even in the subcritical spectral regime where WI-180's additional tail is exactly zero. It therefore changes the missing source question rather than trying to force a small incremental gain through the WI-181 activation gate. The algebra also identifies the quantity that a source-realizable extremizer must make small; arbitrary rotations of positive-semidefinite matrices are not adequate controls.

## Decisive test

First reconstruct the polar-coordinate identity and verify that no conditioning bound on `B^(-1/2)` was silently used: `U` is unitary, but replacing it by an approximate source formula may introduce conditioning losses. Then evaluate the exact source-defined `Gamma_e` on the line's period-33 controls, real-double controls, isolated off-line pairs, and mixed simple-real/off-line configurations, preserving their actual test kernel and population normalization.

An initial non-certified numerical check used 160-point Gauss–Legendre quadrature for the unsmoothed Montgomery–Taylor weight `cos(sqrt(2)u)/(sqrt(2)sin(1/sqrt(2)))` on `[-1/2,1/2]`, twelve simple real points `-5.5,-4.5,...,5.5`, and one pair `0.25 +/- i a`. For depths `a=0.3,0.1,0.03,0.01`, the maximum simple-real Gram eigenvalue was approximately `1.086797`, so its supercritical tail was zero. The computed `Gamma_e` values were approximately `4.758860,3.083335,2.961282,2.951077`, with square-completion residuals below `9e-16`. These are **synthetic finite-source controls, not zeta zeros**. Their `Q/N` values were approximately `1.679595,1.450170,1.433375,1.431970`: they do not satisfy the ideal Montgomery–Taylor asymptotic budget and cannot be used as evidence of a zeta improvement.

The substantial test is to prove a lower bound in the admissible source class, or construct a source-compatible near-extremizing family with the required exceptional density and `Gamma_e/N -> 0`. An isolated pair only kills a proposed universal pair charge; it does not alone settle a claim with an explicitly stronger density/overlap hypothesis. Conversely, positive overlap with the simple-real sector may already survive when the pair collapses to a real double, so that overlap must not be mislabelled as exclusively off-critical information.

## Evidence boundary

The square completion is elementary candidate derivation in this clue; the finite quadrature checks are not interval-certified. No new source lower bound, percentage, proof of RH, or independent novelty claim is established. Generic positivity of `Gamma_e` is not the desired result. The required mathematical delta is a source-forced magnitude or a decisive source-compatible counterexample that survives all existing moment, multiplicity, support, and normalization constraints.
