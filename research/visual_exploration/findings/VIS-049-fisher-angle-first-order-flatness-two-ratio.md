# VIS-049 — Fisher-angle first-order flatness allows a nondegenerate two-ratio family

## Claim

Let `Omega` be a fixed finite support, let `H` be a strictly positive probability gauge on `Omega`, and let `A,B` be fixed nonzero real residual tensors. Write

`kappa = kappa_H(A,B)`

for their Fisher-angle coefficient under `H`, and normalize the Fisher coordinates by

`u_x = A_x / (sqrt(H_x) ||A||_H)`,

`v_x = B_x / (sqrt(H_x) ||B||_H)`.

Thus

`sum_x u_x^2 = sum_x v_x^2 = 1`,

`kappa = sum_x u_x v_x`.

For an arbitrary real cell function `h=(h_x)`, perturb the positive gauge through

`G_x(t) = H_x exp(-t h_x) / Z(t)`,

where

`Z(t)=sum_y H_y exp(-t h_y)`.

Let `kappa_h(t)=kappa_(G(t))(A,B)`. Then the exact first-variation formula at the baseline gauge is

`kappa_h'(0) = sum_x h_x s_x`,

with the cellwise sensitivity tensor

`s_x = u_x v_x - (kappa/2)(u_x^2+v_x^2)`.

Consequently the Fisher cosine is stationary under **every infinitesimal positive gauge direction** if and only if

`2 u_x v_x = kappa (u_x^2+v_x^2)`

for every cell `x`.

This all-direction stationarity has an exact classification.

- If `kappa=0`, it forces `u_x v_x=0` in every cell, hence `A_x B_x=0` cellwise. This is the globally gauge-invariant orthogonal case already isolated by `VIS-048`.
- If `|kappa|=1`, equality in Cauchy-Schwarz gives `A=lambda B`; again the angle is globally gauge-invariant.
- If `0<|kappa|<1`, nonproportional all-direction stationary pairs **do exist**. On every common-support cell the ratio `u_x/v_x` must be one of the two reciprocal roots

`t_+ = [1+sqrt(1-kappa^2)]/kappa`,

`t_- = [1-sqrt(1-kappa^2)]/kappa = 1/t_+`.

Writing `t=t_+`, the two ratio classes must both occur in the nonproportional case. If

`P={x:u_x=t v_x}`,

`M={x:u_x=v_x/t}`,

then normalization forces

`sum_(x in P) v_x^2 = 1/(1+t^2)`,

`sum_(x in M) v_x^2 = t^2/(1+t^2)`.

Conversely any pair built from these two ratio classes with those squared-mass totals is stationary to first order in every positive gauge direction and has

`kappa = 2t/(1+t^2)`.

The flatness is genuinely only first order. Along the explicit contrast perturbation `h=+1` on `P` and `h=-1` on `M`, one gets the exact finite-gauge formula

`kappa_h(s) = kappa cosh(s) / sqrt(1+kappa^2 sinh(s)^2)`

and therefore

`kappa_h(s) = kappa + [kappa(1-kappa^2)/2] s^2 + O(s^4)`.

For every nondegenerate `0<|kappa|<1` case the quadratic coefficient is nonzero. Thus a Fisher residual orientation can have **zero gradient with respect to every infinitesimal positive gauge perturbation while still being gauge-dependent at second order**.

**Evidence/status:** `EXACT-DERIVED + REPRESENTATION CONTROL + FIRST-VARIATION CLASSIFICATION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

No claim is made that the two-ratio configurations are generic in empirical residual tables, that a particular zeta/CUE comparison has this structure, that first-order flatness implies practical finite-radius robustness, or that the elementary calculus/classification is a new general theorem.

## 1. Positive gauge paths reduce to exponential cell reweighting

For the path above,

`H_x/G_x(t) = Z(t) exp(t h_x)`.

The common positive scalar `Z(t)` multiplies the Fisher numerator and both squared norms in exactly the way that cancels from the normalized angle coefficient. Hence

`kappa_h(t)`
` = [sum_x u_x v_x exp(t h_x)]`
`   / sqrt([sum_x u_x^2 exp(t h_x)] [sum_x v_x^2 exp(t h_x)]).`

Every real `h` defines a legitimate positive probability-gauge path through `H`. Constant `h` gives no actual gauge change after normalization, as expected; nonconstant directions describe the local projective reweighting freedom.

This representation makes the first variation a direct weighted-cosine calculation rather than a numerical sensitivity experiment.

## 2. The gradient is one explicit cellwise tensor

Let

`N(t)=sum_x u_x v_x exp(t h_x)`,

`Q_u(t)=sum_x u_x^2 exp(t h_x)`,

`Q_v(t)=sum_x v_x^2 exp(t h_x)`.

At `t=0`,

`N(0)=kappa`,  `Q_u(0)=Q_v(0)=1`.

Differentiating the normalized quotient gives

`kappa_h'(0)`
` = N'(0) - (kappa/2)[Q_u'(0)+Q_v'(0)]`
` = sum_x h_x [u_x v_x-(kappa/2)(u_x^2+v_x^2)]`.

Also

`sum_x s_x = kappa-(kappa/2)(1+1)=0`,

which is the differential expression of the irrelevant common scaling direction.

Because the gauge path permits arbitrary real `h`, the derivative vanishes for every direction exactly when every coefficient `s_x` vanishes. This yields the displayed cellwise stationarity equation.

The formula is useful operationally even away from the exact stationary locus: `s` is the complete first-order sensitivity field of the Fisher cosine with respect to log-gauge reweighting. A visually small or structured gradient is therefore interpretable only after distinguishing exact first-order geometry from finite-radius robustness.

## 3. Cellwise stationarity reduces to two reciprocal slopes

If `kappa=0`, the stationarity equation becomes

`u_x v_x=0`

cellwise, giving the disjoint-support global-invariance case of `VIS-048`.

Now assume `kappa!=0`. The stationarity equation immediately rules out one-sided support: if `u_x=0` and `v_x!=0`, or conversely, its right-hand side is nonzero. Hence every active cell is common support.

Set

`r_x=u_x/v_x`.

The cellwise equation becomes

`kappa r_x^2 - 2 r_x + kappa = 0`.

For `|kappa|<1`, the two real roots are precisely `t_+` and `t_-`, and their product is one. For `|kappa|=1` the roots coalesce to `+1` or `-1`, matching the proportional equality case of Cauchy-Schwarz.

Suppose now `0<|kappa|<1` and put `t=t_+`. Let

`p=sum_(P) v_x^2`,  `m=sum_(M) v_x^2`.

Since `v` is normalized,

`p+m=1`.

Since `u` is normalized and has ratios `t` and `1/t`,

`t^2 p + t^(-2) m = 1`.

Solving gives

`p=1/(1+t^2)`,  `m=t^2/(1+t^2)`.

The inner product is then

`kappa = t p + t^(-1) m = 2t/(1+t^2)`,

which is equivalent to the defining quadratic for `t`.

If only one ratio class were present, `u` would be globally proportional to `v`; equal unit norms would force the ratio to have magnitude one and hence `|kappa|=1`. Therefore a genuinely nonproportional stationary pair with `0<|kappa|<1` necessarily uses both reciprocal slope classes.

## 4. A two-cell model proves that zero first variation does not mean local invariance

The nondegenerate family is already visible on two cells. For example, take

`kappa=3/5`,  `t=3`,

and choose

`v=(sqrt(1/10), sqrt(9/10))`,

`u=(3 sqrt(1/10), (1/3) sqrt(9/10))`.

Both vectors have unit norm and their dot product is `3/5`. The cellwise sensitivity tensor `s` vanishes identically, so every infinitesimal log-gauge direction has zero first derivative at the baseline.

Nevertheless reweighting the first cell by `exp(s)` and the second by `exp(-s)` yields

`kappa(s) = (3/5) cosh(s) / sqrt(1+(9/25)sinh(s)^2)`,

which is strictly different from `3/5` for every sufficiently small nonzero `s`.

More generally, for the two-ratio decomposition the same group-contrast calculation gives

`kappa(s)=kappa cosh(s)/sqrt(1+kappa^2 sinh(s)^2)`.

Its Taylor expansion has nonzero quadratic term whenever `0<|kappa|<1`. For positive `kappa` the cosine increases to second order along this contrast; for negative `kappa` it decreases. Either way the full angle changes even though its complete first-order gauge gradient vanishes.

This is compatible with `VIS-048`, not an exception to it. `VIS-048` says exact constancy on any open positive-gauge neighborhood is possible only for proportional or cellwise-disjoint residuals. The present two-ratio pairs are not constant on a neighborhood; they are isolated first-order-flat configurations with nonzero higher-order sensitivity.

## 5. Prior-art and novelty boundary

The general dependence of vector angles on the chosen inner product is classical. The closest persisted specialized anchor remains Lin and Sinnamon's generalized Wielandt inequality in `SOURCES.md`, used by `VIS-045` to give sharp finite angle-distortion bounds between two inner products. `VIS-046` and `VIS-047` then specialize positive diagonal Fisher reweighting to exact sign geometry, while `VIS-048` classifies exact full-angle invariance on a gauge neighborhood.

A targeted check of weighted-cosine sensitivity, metric perturbation, and diagonal-gauge cosine literature found established neighboring gauge-sensitivity phenomena, including modern embedding results in which diagonal reparameterizations can alter cosine similarities. Those settings act on learned embedding factorizations rather than on fixed residual tensors with a varying common Fisher metric, and they do not supply the first-variation classification above.

No novelty is claimed for differentiating a normalized weighted inner product, for the quadratic two-root algebra, or for the existence of stationary points of a metric-dependent cosine. The durable Mathia content is the exact control boundary for the current residual-direction program: **all-direction first-order flatness is strictly weaker than finite-neighborhood gauge robustness**, and its exceptional nondegenerate locus can be written explicitly.

## 6. Boundary conditions and falsification

The support, residual tensors, and baseline gauge must remain fixed while the gauge varies. Rebinning, trimming cells, recomputing the Markov closure, refitting a residual, or changing the support simultaneously is a different perturbation problem.

Every gauge along the path must remain strictly positive. The exponential parameterization guarantees this locally for every finite `h`; structural zeros are outside the theorem.

The classification concerns stationarity of the normalized Fisher cosine. For `|kappa|<1`, stationarity of the angle itself is equivalent because `arccos` has nonzero finite derivative there. At `kappa=+/-1`, the vectors are already proportional and globally invariant, so no separate endpoint-angle issue arises.

The nondegenerate stationary locus is highly constrained: it requires exactly two reciprocal normalized cellwise slopes with the specified squared-mass totals. Small empirical gradient estimates near zero do not establish this exact algebraic condition, especially under sampling noise.

Falsify the claim by exhibiting fixed finite nonzero `A,B`, a positive `H`, and a gauge direction `h` that violates the derivative formula; or by finding an all-direction stationary pair whose normalized cellwise ratios are not in the classified zero/proportional/two-root cases. For the nondegenerate branch, a counterexample to the displayed finite contrast formula would also invalidate the second-order conclusion.

## Research consequence

The common-gauge residual program should not use a vanishing or numerically tiny first-order gauge gradient as a certificate that a measured zeta/CUE orientation is representation-robust. Even exact vanishing in **every** infinitesimal gauge direction admits a nonproportional two-ratio family whose cosine moves immediately at quadratic order.

Finite-radius controls therefore remain necessary. Freeze the scientifically justified primary gauge before inspecting the target comparison, use `VIS-045` for finite angle-distortion envelopes and `VIS-047` for exact bounded-family sign robustness, and treat the first-variation field `s_x` only as a local diagnostic. If an empirical residual pair appears first-order flat, test whether it is near the explicit two-ratio locus and then challenge it with predeclared finite gauge changes rather than promoting the flat gradient itself as an invariant.

This closes one coherent representation-control question exposed by `VIS-048`. Pursuing second-order Hessian classification beyond the explicit witness, or applying the criterion to actual zeta/CUE residual tables, is a separate next question and is intentionally left for a later invocation.
