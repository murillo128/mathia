# VIS-239 — cumulative-intensity coordinates exactly quotient any specified iid one-point intensity

## Claim

Let `X_1,...,X_m` be independent draws from a continuous distribution on an interval with continuous strictly increasing CDF `F`. For `0<epsilon<=1/2`, define the cumulative-intensity tent statistic

`T_(m,F,epsilon) = sum_(i<j) (1-|F(X_i)-F(X_j)|/epsilon)_+`.

Then `U_i=F(X_i)` are iid `Uniform[0,1]`, so `T_(m,F,epsilon)` has **exactly** the fixed-count uniform tent law calibrated in `VIS-238` with width ratio `u=epsilon`. In particular, if

`a=epsilon-epsilon^2/3`,
`b=2 epsilon/3-epsilon^2/6`,
`c=epsilon^2-17 epsilon^3/30`,

then

`E[T_(m,F,epsilon)] = binom(m,2) a`

and

`Var[T_(m,F,epsilon)] = binom(m,2)(b-a^2) + 6 binom(m,3)(c-a^2)`.

Thus a fully specified **one-point nonuniform iid intensity** does not require a new collision calibration after transforming to its own cumulative-intensity coordinate: it is exactly the `VIS-238` fixed-count uniform null in that coordinate.

There is, however, a decisive degeneracy if `F` is replaced by the empirical CDF built from the same `m` points. For distinct order statistics `X_(1)<...<X_(m)`,

`F_m(X_(i))=i/m`.

Hence the transformed tent statistic is deterministic given only `m` and `epsilon`:

`T_emp = sum_(r=1)^q (m-r)(1-r/(m epsilon))`,

where

`q=min(m-1, ceil(m epsilon)-1)`.

Equivalently,

`T_emp`
` = q m - q(q+1)/2`
`   - [m q(q+1)/2 - q(q+1)(2q+1)/6]/(m epsilon)`.

The same pairwise differences arise from midranks. Therefore same-sample empirical-CDF flattening is not a valid discovery control for this branch: it erases the one-dimensional spacing geometry whose residual the tent statistic is intended to test.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-TRANSFORM + NEGATIVE/CALIBRATION + NO-NOVELTY-CLAIM`.

## 1. A specified iid intensity reduces exactly to the fixed-count uniform law

The probability-integral transform gives

`U_i=F(X_i) ~ Uniform[0,1]`

independently for `i=1,...,m`. Therefore

`T_(m,F,epsilon) = sum_(i<j) (1-|U_i-U_j|/epsilon)_+`

is not merely asymptotically comparable to the `VIS-238` statistic; it is equal in distribution to it for every finite `m` and every `0<epsilon<=1/2`.

The exact moment formulas in the claim therefore follow immediately from `VIS-238`. Under the critical scaling `epsilon_m=kappa/m` with fixed `kappa`, the same extensive calibration follows:

`E[T_(m,F,epsilon_m)] = m kappa/2+O(1)`,

`Var[T_(m,F,epsilon_m)] = m kappa/3+O(1)`.

The important point is structural rather than numerical. If a candidate null differs from uniformity only through a known one-point density, cumulative intensity is an exact gauge that removes that heterogeneity before the short-range pair functional is evaluated. A residual in this coordinate cannot be attributed merely to the specified marginal intensity.

## 2. Inhomogeneous Poisson interpretation

Let an inhomogeneous Poisson process on an interval have deterministic intensity `lambda(x)`, cumulative intensity

`Lambda(x)=integral lambda(t) dt`,

and finite total mass `Lambda_tot`. Conditional on observing exactly `m` points, their unordered locations are iid with density `lambda/Lambda_tot`. Hence

`F(x)=Lambda(x)/Lambda_tot`

maps the conditional point configuration to `m` iid uniform points and reduces the transformed tent statistic exactly to the fixed-count law above.

Without conditioning on the total count, the ordinary time-rescaling theorem instead maps cumulative-intensity coordinates to a homogeneous Poisson process. This preserves the distinction isolated by `VIS-238`: a fixed-count confirmation question should use the conditional fixed-count law, while an unconditioned point-process question retains the additional count-fluctuation channel.

## 3. The same-sample empirical CDF destroys the tested geometry

For a sample with no ties, the empirical CDF satisfies

`F_m(X_(i))=i/m`.

Therefore the transformed separation of the `i`th and `j`th order statistics is

`|F_m(X_(j))-F_m(X_(i))|=(j-i)/m`.

Grouping pairs by rank distance `r=j-i`, of which there are `m-r`, gives

`T_emp=sum_(r=1)^(m-1) (m-r)(1-r/(m epsilon))_+`.

Only ranks `r<m epsilon` contribute, which yields the cutoff `q` and the closed form in the claim. No original gap, local density fluctuation, clustering, exclusion, or other spacing information survives.

This is stronger than saying that an empirical-CDF transform introduces estimation error. When the same points both estimate the CDF and supply the test statistic, the transform is an exact rank projection for this one-dimensional geometry. The statistic has zero conditional freedom once `m` and `epsilon` are fixed.

An intensity model estimated from independent training data or through an explicitly held-out/cross-fitted procedure is different: its transformed points need not lie on the deterministic rank lattice. Such a procedure may be useful, but its estimation error becomes part of the null calibration and is not covered by the exact fixed-`F` law above.

## 4. Consequence for the critical prime-phase collision branch

The accepted clue `CLUE-prime-phase-critical-logarithmic-occupancy` asks for a stronger fixed-count monotone control that admits nonuniform local intensity without conditioning away the triangular pair statistic. This finding separates two cases.

A predeclared one-point intensity model can be handled cleanly: transform the ordered prime-coordinate points by that model's cumulative intensity and compare the resulting tent statistic with the exact `VIS-238` fixed-count uniform calibration. If the transformed residual survives, the specified one-point intensity is not its explanation.

But estimating the CDF from the same confirmation points and then testing their rank-coordinate tent statistic is inadmissible: it forces a deterministic answer and removes exactly the spacing geometry under investigation. Any stronger control must therefore obtain its intensity independently enough to leave the statistic nondegenerate, or move beyond one-point intensity and model genuinely short-range dependence/exclusion.

This narrows the live null-model frontier. After `VIS-237` quotients grid origin, `VIS-238` removes total-count randomization, and the present result quotients any externally specified iid one-point intensity, the next unresolved source-specific structure is pair/higher-order geometry, intensity-model misspecification, or estimation uncertainty — not nonuniformity by itself.

## Prior-art / novelty audit

The probability-integral transformation is classical. A standard reference is A. W. van der Vaart, *Asymptotic Statistics*, Cambridge University Press (1998), Chapter 21, "Quantiles and Order Statistics", DOI `10.1017/CBO9780511802256.022`; the rank collapse used for the empirical-CDF warning is likewise standard rank/order-statistic structure, treated for example in Chapter 13, DOI `10.1017/CBO9780511802256.014`.

For point processes, cumulative-intensity time rescaling to a homogeneous Poisson process is classical; see E. N. Brown, R. Barbieri, V. Ventura, R. E. Kass, and L. M. Frank, "The Time-Rescaling Theorem and Its Application to Neural Spike Train Data Analysis", *Neural Computation* 14(2), 325–346 (2002), DOI `10.1162/08997660252741149`.

No novelty is claimed for either transform. The branch-specific content here is the exact consequence for the `VIS-237`/`VIS-238` tent calibration and the identification of same-sample empirical-CDF flattening as a degenerate control for the current geometry question.

## Boundaries

This finding does **not** establish that the prime-coordinate points are iid under any nonuniform intensity, identify a faithful prime intensity model, prove that a prime residual survives cumulative-intensity normalization, or give an RH consequence.

The exact fixed-`F` reduction assumes independent draws from a specified continuous distribution. For a dependent point process, applying a marginal CDF makes one-point marginals uniform but does not remove dependence; that surviving dependence is precisely part of the next research frontier.

The result also does not make an independently estimated or cross-fitted intensity exact. Such procedures require their own finite-sample or asymptotic calibration for estimation uncertainty.