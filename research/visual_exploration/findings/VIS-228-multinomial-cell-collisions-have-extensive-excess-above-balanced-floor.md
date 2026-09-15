# VIS-228 — multinomial cell collisions have extensive excess above the balanced floor

## Claim

Let `m` labelled points be assigned independently and uniformly to `J>=1` cells, let `n_1,...,n_J` be the occupancies, and define

`S = sum_j binom(n_j,2)`.

Then

`E[S] = binom(m,2)/J`

and

`Var(S) = binom(m,2) (1/J)(1-1/J)`.

If `m=qJ+r` with `0<=r<J`, the deterministic balanced-occupancy minimum from `VIS-227` is

`S_min(m,J)=J binom(q,2)+rq`,

and the uniform random-allocation null has the exact expected excess

`E[S-S_min] = q(J-1)/2 + r(r-1)/(2J)`.

Consequently, if `m/J -> rho>0` and `rho=q+alpha` with `q=floor(rho)` and `0<=alpha<1`, then

`E[S-S_min]/J -> (q+alpha^2)/2 > 0`,

while `sd(S)=Theta(sqrt(J))`.

Thus an extensive positive value of `S-S_min` is itself **generic under the simplest independent matched occupancy null**. Subtracting only the balanced floor does not isolate prime-specific clustering at the critical phase-cell scale. Any arithmetic discriminator based on pair collisions must at least center against an appropriate stochastic occupancy model, and stronger claims must survive controls preserving the intended one-point density and other admitted local structure.

For the critical phase cells of `VIS-227`, where

`m/J -> rho_lambda = eta_v/(8lambda)`,

the same conclusion holds for every fixed `lambda>0`: the independent equal-cell null already produces `Theta(J)=Theta(y/log y)` expected excess above `S_min`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-OCCUPANCY CONTROL + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

## 1. Pair-indicator representation

Let `X_1,...,X_m` be independent uniform cell labels in `{1,...,J}`. For each unordered pair `a<b`, put

`I_ab = 1_{X_a=X_b}`.

Every same-cell unordered pair of points contributes once to `S`, so

`S = sum_(a<b) I_ab`.

Since `P(X_a=X_b)=1/J`, linearity of expectation gives

`E[S] = binom(m,2)/J`.

For two distinct pair indicators, the covariance is zero. If the pairs are disjoint, this is ordinary independence. If they share one point, for example `(a,b)` and `(a,c)`, then

`P(X_a=X_b=X_c)=1/J^2=P(I_ab=1)P(I_ac=1)`.

Hence the family is pairwise independent even though it is not jointly independent, and therefore

`Var(S)=sum_(a<b) Var(I_ab)=binom(m,2)(1/J)(1-1/J)`.

No asymptotic approximation enters these identities.

## 2. Exact gap above the balanced floor

Write `m=qJ+r`, `0<=r<J`. Using `VIS-227`,

`S_min = J q(q-1)/2 + rq`.

Direct subtraction gives

`E[S]-S_min`
` = m(m-1)/(2J) - Jq(q-1)/2 - rq`
` = q(J-1)/2 + r(r-1)/(2J)`.

This is nonnegative, as it must be, but more importantly it is typically macroscopic. If `m/J -> rho=q+alpha` away from or through an integer threshold, the normalized expression has the continuous limit

`(E[S]-S_min)/J -> (q+alpha^2)/2`.

At integer `rho=k`, this equals `k/2`; approaching the same point from below gives the same limit because `(k-1+1^2)/2=k/2`.

Meanwhile

`Var(S) ~ (rho^2/2)J`,

so the random fluctuation scale is only `Theta(sqrt(J))`. The balanced minimum therefore sits an order-`J` distance below the center of the independent occupancy distribution.

## 3. Consequence for the critical prime-phase clue

At `H=lambda y/log y`, `VIS-227` gives

`J=(4lambda/eta_v+o(1)) y/log y`

and

`m/J -> rho_lambda=eta_v/(8lambda)`.

The previous clue correctly removed `S_min` as a deterministic balls-in-cells artifact, but the exact random-allocation calculation shows that this is not yet a stochastic null. Even a completely independent equal-cell allocation has a positive linear excess above that floor, with standard deviation only of square-root order.

A first calibrated statistic for the equal-cell null is therefore

`Z = [S-binom(m,2)/J] / sqrt[binom(m,2)(1/J)(1-1/J)]`,

not `S-S_min`. This `Z` is only a preliminary control: the actual critical prime comparison may require nonuniform cell probabilities, fixed cell-origin perturbations, logarithmic-gap structure, or another matched model. For a general independent categorical allocation with cell probabilities `p_j`, the mean already changes to

`E[S]=binom(m,2) sum_j p_j^2`,

so the one-point occupancy law must be part of the control specification rather than silently assumed uniform.

## Evidence boundary

This finding does **not** establish that prime occupancies follow the independent multinomial null, that the standardized prime residual is nonzero or zero, that a central-limit theorem applies to the chosen prime statistic, or that any critical-scale worst-start energy separates from its Haar-average scale.

It closes only one candidate discriminator: positivity or linear growth of `S-S_min` cannot by itself be interpreted as prime-specific organization because the simplest independent equal-cell null already has exactly that behavior.

The pair-collision calculation is classical balls-in-cells / birthday-collision mathematics. Classical random-allocation literature covers the multinomial occupancy model; no novelty is claimed for the probability identities. The durable Mathia contribution is their exact specialization as the next control boundary for the current critical prime-phase representation.

## Research consequence

The live critical question should compare the prime statistic against a stochastic baseline rather than the deterministic optimum. If pair collisions remain interesting, test a centered/standardized residual against controls that preserve the intended one-point density and then progressively stronger local structure. If that residual is generic, move to a genuinely different phase-cell observable such as multiscale occupancy persistence or a direction-sensitive energy statistic rather than repeatedly renormalizing the same raw collision count.