---
id: CLUE-analytic-frontier-lean-residual-effective-triple-gap
type: research-clue
status: resolved
origin: independent-review
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/formalization/ANF087ZeroSetPacking.lean
  - research/analytic_frontier/findings/ANF-087-montgomery-taylor-equality-is-a-two-site-real-zero-set-packing.md
  - research/analytic_frontier/findings/ANF-032-sharp-montgomery-taylor-energy-forces-local-two-point-packing.md
  - research/analytic_frontier/findings/ANF-033-sharp-montgomery-taylor-order-interval-disjoint-from-finite-diffraction-closure.md
  - research/analytic_frontier/findings/ANF-100-montgomery-taylor-near-extremizers-require-linear-horizontal-span.md
---

# Can Lean's additive residual make the triple gap effective at the sharp fourth-power scale?

## Observation

The formalization published through [issue #130](https://github.com/murillo128/mathia/issues/130), at commit `cfe986b76ef2c26b6a5f6ca61407c6959b9f614a`, contains more quantitative structure than its final zero-set statement consumes. In `Mathia.ANF087.numerator_add_ne_zero`, the proof uses a direct addition-formula identity, not the localization and ordering of positive roots. Write

\[
N(t)=\cos(\pi t)-a t\sin(\pi t),\qquad
D(t)=1-2\pi^2t^2,\qquad
 a=\sqrt2\pi\cot(1/\sqrt2).
\]

The already-published `K_mul_denominator` proves `K(t) D(t)=N(t)` for every real `t`, including both removable points. When `N(u)=N(v)=0`, the other helper obtains

\[
N(u+v)=-[1+a^2(u^2+uv+v^2)]\sin(\pi u)\sin(\pi v).
\]

Lean consumes only nonvanishing. The positive factor and the trigonometric unit-circle constraint suggest a robust lower bound even when the two input residuals are small rather than zero. This is a different output from root localization or qualitative sum-freeness.

In `ANF-032`, with `R_MT=K^2`, the triple constant is defined by compact minimization and proved positive, without an explicit modulus in the physical scale. `ANF-033` already closes the historical finite-real diffraction separation problem by another argument: this clue must not reopen that resolved existence question. The residual target here is an effective, order-optimal finite-scale bound and its quantitative real-configuration consequences, not another proof of qualitative real separation. The neighboring five-point curvature-rigidity clue concerns a different curvature transform and disappearing nonreal pairs, not this all-real `K^2` triple gap.

## Research question

Validate and formalize the following candidate strengthening, then determine which current real-configuration estimates can consume it. For every `L>0`, is the constant in `ANF-032` bounded explicitly by

\[
\kappa_L:=\min_{u,v\ge0,\ u+v\le L}
\{K(u)^2+K(v)^2+K(u+v)^2\}
\ \ge\ \frac{1}{16(1+2\pi^2L^2)^2}?
\tag{1}
\]

There is a short hand-derived proof candidate, with no numerical root isolation. Put `U=au`, `V=av`, `p=N(u)`, `q=N(v)`, `s=sin(pi u)`, `t=sin(pi v)`, and `Q=1+U^2+UV+V^2`. Restoring the residuals discarded in the zero-set proof gives the exact identity

\[
N(u+v)=pq-Up t-Vq s-Qst.
\tag{2}
\]

Set `A=sqrt(1+U^2)` and `B=sqrt(1+V^2)`. The relevant algebraic certificate is

\[
Q^2-A^2B^2=(U+V)^2(1+U^2+V^2),
\qquad Q\ge AB.
\tag{3}
\]

The Euclidean triangle inequality applied to `(cos(pi u),sin(pi u))=(p,0)+s(U,1)` gives `1<=|p|+A|s|`, and similarly `1<=|q|+B|t|`. Moreover, because `uv>=0`, also `UV>=0`, and

\[
|U|A+|V|B\le1+U^2+V^2\le Q.
\tag{4}
\]

The first inequality follows termwise from `|x|sqrt(1+x^2)<=x^2+1/2`; squaring leaves the positive remainder `1/4`.

Suppose `|p|,|q|<=epsilon<1/2`. Both sines are nonzero, with `|s|>=(1-epsilon)/A` and `|t|>=(1-epsilon)/B`. Equations (3)--(4) imply

\[
Q|st|\ge(1-\epsilon)^2,
\quad
|Up t|+|Vq s|
\le\frac{\epsilon}{1-\epsilon}Q|st|.
\]

Consequently (2) yields

\[
|N(u+v)|\ge(1-\epsilon)(1-2\epsilon)-\epsilon^2.
\tag{5}
\]

At `epsilon=1/4`, the right side is `5/16>1/4`. Thus the three numerator residuals cannot all have absolute value at most `1/4`. Since `|D(w)|<=1+2pi^2 L^2` for all three arguments, the global identity `K(w)D(w)=N(w)` implies (1), without dividing by a potentially vanishing denominator. The constant `1/16` is only a convenient certified-target constant, not a proposed optimal constant.

The decay exponent has an exact control. At positive integers, `K(n)=(-1)^n/(1-2pi^2 n^2)`, so the admissible triple `u=v=n`, `L=2n` gives

\[
\kappa_{2n}\le
\frac{2}{(1-2\pi^2n^2)^2}
+\frac{1}{(1-8\pi^2n^2)^2}.
\tag{6}
\]

Using `n=floor(L/2)` for large `L`, (1) and (6) would establish `kappa_L` comparable to `L^(-4)`. In particular, a globally positive triple gap independent of `L` is impossible; the proposed gain is the explicit modulus, not uniform coercivity at infinity.

## Why it may matter

The deletion theorem of `ANF-032` would become the usable bound

\[
\frac{|X\setminus Y|}{|X|}
\le\min\{1,\ 32\Delta(X)(1+2\pi^2L^2)^2\},
\tag{7}
\]

where every interval of length strictly less than `L/2` contains at most two points of `Y`. Thus growing windows `L=L_j` are allowed whenever `Delta(X_j)(1+L_j^4)->0`; for positive excess tending to zero, one can take `L_j=o(Delta(X_j)^(-1/4))`. This removes an unspecified compactness constant from the estimate and supplies an analytic control for finite-box computations.

It also suggests a rate for the stronger dilution available in the simple-real subclass of `ANF-100`. For `N=|X|`, `delta=Delta(X)` with `0<delta<1/64`, choose

\[
L(\delta)=\sqrt{\frac{1/(8\sqrt\delta)-1}{2\pi^2}}.
\]

Then (7) deletes at most half the points. Ordering the survivors and using `y_(i+2)-y_i>=L/2` gives

\[
\operatorname{diam}(X)\ge\frac{N-4}{8}L(\delta)
\qquad(N\ge4).
\tag{8}
\]

For large `N` this is a lower bound on span per point of order `delta^(-1/4)`, stronger than merely a positive constant, but only for distinct real configurations. Integer-spaced sets `X={0,m,...,(N-1)m}`, with positive integer `m`, provide the matching order: directly from the integer formula for `K`,

\[
\Delta(X)\le
\frac{2}{(2\pi^2-1)^2m^4}\sum_{k=1}^{\infty}k^{-4}
\le\frac{8}{3(2\pi^2-1)^2m^4},
\]

while their span per point is comparable to `m`. This identifies the relevant fourth-power scale rather than just asserting an unspecified rate of escape.

## Decisive test

First reconstruct (2)--(5) independently, retaining the condition `uv>=0` in (4), and verify every inequality direction. A counterexample to the numerator threshold, or a failure to justify the two sine lower bounds, kills the proposed constant immediately. Formalization can reuse `K_mul_denominator` and the addition-formula algebra in the existing module; no root enumeration, compactness proof or tangent monotonicity is needed for the new lower bound. Keep the removable points and `u=0` or `v=0` as explicit regression cases.

Next verify the normalization `R_MT=K^2`, insert (1) into the exact two-partition deletion bound of `ANF-032`, and check the ordered-survivor argument in (8). Use (6) and the integer-spaced families to reject any claimed improvement of the decay exponents without additional hypotheses. Before promotion, check the bounded neighboring results and prior art for this quantitative modulus; its being absent from the inspected proofs is not a literature novelty claim.

Finally, identify a concrete consumer that needs an effective scale. For a proposed extension to nonreal configurations, explicitly replace the nonnegative real pair-energy step; neither (7) nor (8) transfers merely by invoking conjugation symmetry or `ANF-100`. Failure of that extension should narrow the scope, not invalidate a correct real-configuration estimate.

## Evidence boundary

The zero-set obstruction and the global product identity are in the published Lean artifact. Equations (1)--(8) above were supplied as hand-derived candidates for independent checking rather than as evidence. Research Watch has now reconstructed the algebra independently from canonical local findings, stress-tested the removable-point and boundary cases, verified the exact deletion normalization, and strengthened the lattice calibration with the matching lower bound `Delta(X)>=1/(4 pi^4 m^4)` for `N>=2`.

No arithmetic source budget, conditioning theorem, cancellation estimate for nonreal multisets, improved zero proportion, or RH consequence is established. In particular, the finite-real separation result of `ANF-033` was already known in the repository and is not claimed again here.

## Research disposition
Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-114-effective-montgomery-taylor-triple-gap-forces-optimal-defect-to-span-exponent.md]]
