# VIS-178 — prime-power effective dimension sharpens the polynomial moment wedge

## Claim

Keep the notation of `VIS-177` and take all primes `p<=y` with fixed prime-power weights

`w_p=p^(-alpha)`, `0<=alpha<=1/2`.

Write

`W_y=sum_(p<=y) p^(-alpha)`,

`Q_y=sum_(p<=y) p^(-2alpha)`,

and

`D_2(y)=W_y^2/Q_y`.

For every fixed `0<=alpha<1/2`, the prime number theorem plus partial summation gives

`W_y ~ y^(1-alpha)/((1-alpha) log y)`,

`Q_y ~ y^(1-2alpha)/((1-2alpha) log y)`,

hence

`D_2(y) ~ [(1-2alpha)/(1-alpha)^2] y/log y`.

At the endpoint `alpha=1/2`, the same weighted-prime estimate for `W_y` together with Mertens' reciprocal-prime theorem gives

`W_y ~ 2 sqrt(y)/log y`,

`Q_y ~ log log y`,

and therefore

`D_2(y) ~ 4y/[(log y)^2 log log y]`.

Insert these effective-dimension asymptotics into the balanced-character transfer bound of `VIS-177`. Define

`e_k=floor(k/2)+k/2`,

so `e_k=k` for even `k` and `e_k=k-1/2` for odd `k`. Then for every fixed integer `k>=1`, uniformly in the interval start,

- if `0<=alpha<1/2`, the `k`th deterministic/Haar moment error is

  `O_(alpha,k)( y^e_k / [H (log y)^(k/2)] )`;

- if `alpha=1/2`, it is

  `O_k( y^e_k / [H (log y)^k (log log y)^(k/2)] )`.

Consequently, for a fixed polynomial support law

`y=H^delta`, `delta>0`,

the `k`th moment transfers whenever

`delta <= 1/e_k`.

The equality case is included because the residual logarithmic denominator still tends to infinity. More generally, a predeclared panel of all moments through order `K` transfers whenever

`delta <= 1/e_K`.

Thus the crude corollary `delta<1/K` recorded after `VIS-177` can be sharpened for the prime-power family: if `K` is even, the same power threshold is closed at equality, `delta<=1/K`; if `K` is odd, the sufficient wedge expands to

`delta <= 1/(K-1/2)`.

**Evidence/status:** `LITERATURE+DERIVED + EXACT ASYMPTOTIC SPECIALIZATION + POLYNOMIAL-SUPPORT NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is a sufficient fixed-order transfer theorem. It does not prove a Gaussian full law for any fixed `delta>0`, does not prove the displayed thresholds necessary or sharp, and does not address discrete/Gram sampling, rare events, unbounded functionals, hybrid prime/zero variables, or RH.

## 1. Weighted prime sums determine the effective dimension

For fixed `0<=beta<1`, partial summation writes

`sum_(p<=y) p^(-beta)`
` = y^(-beta) pi(y) + beta int_2^y pi(t) t^(-beta-1) dt`.

Using the prime number theorem `pi(t)~t/log t`, the integral has the standard leading term

`sum_(p<=y) p^(-beta) ~ y^(1-beta)/((1-beta) log y)`.

Apply this first with `beta=alpha`. For fixed `alpha<1/2`, apply it again with `beta=2alpha`. Dividing the resulting square of `W_y` by `Q_y` gives

`D_2(y) ~ c_alpha y/log y`,

where

`c_alpha=(1-2alpha)/(1-alpha)^2`.

This includes `alpha=0`, where `D_2(y)=pi(y)~y/log y` exactly at the level of the definition.

At `alpha=1/2`, the denominator changes regime. The numerator still satisfies

`W_y=sum_(p<=y) p^(-1/2) ~ 2 sqrt(y)/log y`,

while

`Q_y=sum_(p<=y) 1/p ~ log log y`

by Mertens' theorem for reciprocal primes. Hence

`D_2(y) ~ 4y/[(log y)^2 log log y]`.

The transition at `alpha=1/2` is therefore visible not in the leading power of `y` in `D_2`, which remains linear, but in the slowly varying factor.

## 2. The balanced-character bound keeps a parity-dependent support exponent

`VIS-177` gives, for every fixed `k`,

`|time_k-Haar_k|`
` <= 2^(2-k) y^floor(k/2) D_2(y)^(k/2)/H`.

For fixed `alpha<1/2`, substitution of `D_2(y)~c_alpha y/log y` yields

`|time_k-Haar_k|`
` = O_(alpha,k)( y^[floor(k/2)+k/2] / [H (log y)^(k/2)] )`.

For `alpha=1/2`, substitution instead gives

`|time_k-Haar_k|`
` = O_k( y^[floor(k/2)+k/2] / [H (log y)^k (log log y)^(k/2)] )`.

The exponent

`e_k=floor(k/2)+k/2`

retains the balance improvement from `VIS-177`: even moments pay `y^k`, while odd moments pay only `y^(k-1/2)`. The earlier bound `D_2(y)<=y` erased both the prime-density logarithm and the odd-order half-power distinction when it was summarized uniformly as `y^k/H`.

## 3. Polynomial support reaches the critical power boundary

Let `y=H^delta` with fixed `delta>0`. For `alpha<1/2`, the preceding estimate becomes

`O_(alpha,k)( H^(delta e_k-1) / (log H)^(k/2) )`,

up to an irrelevant fixed power of `delta` in the logarithm. At `alpha=1/2` it becomes

`O_k( H^(delta e_k-1) / [(log H)^k (log log H)^(k/2)] )`.

Therefore the error tends to zero whenever

`delta e_k<1`,

and also on the critical boundary

`delta e_k=1`,

because the denominator still diverges. This proves the sufficient condition

`delta<=1/e_k`.

Since `e_k` is strictly increasing with `k`, all moments in a fixed panel `1<=k<=K` transfer once the top order does. Hence the whole panel is controlled for

`delta<=1/e_K`.

For even `K`, `e_K=K`. For odd `K`, `e_K=K-1/2`. This is the exact improvement available from combining the elementary character separation of `VIS-177` with the actual prime-power effective dimension.

## 4. Why this still does not give a polynomial-support full law

The gain is fixed-order. For any fixed `delta>0`, the condition `delta<=1/e_k` eventually fails as `k` grows. Thus this argument cannot transfer all fixed moments simultaneously along one positive-power support law, and the Frechet--Shohat full-law step used in `VIS-176` does not follow.

Likewise, failure of the sufficient condition says only that the present absolute-character estimate stops proving transfer. It does not imply that the moment actually separates from Haar. Average cancellation among nonresonant characters, sharper multiplicative spacing, or a characteristic-function argument could extend the null further.

The result therefore sharpens the finite-complexity boundary without closing the genuinely polynomial-support full-law question.

## 5. Prior art and novelty boundary

The weighted-prime asymptotics used here are classical consequences of the prime number theorem by Abel/partial summation. NIST DLMF §27.11 records the prime-number-theorem asymptotic framework for prime partial sums. The endpoint `sum_(p<=y)1/p~log log y` is the classical Mertens reciprocal-prime asymptotic already anchored in `research/visual_exploration/SOURCES.md`.

No novelty is claimed for either weighted-prime asymptotic, for partial summation, or for the slowly varying factors. The Mathia-specific content is only their insertion into the already persisted `VIS-177` moment-transfer inequality, which turns the active clue's coarse `delta<1/K` polynomial-support control into the parity-sensitive closed wedge above.

This calculation does not use a quantitative prime-number-theorem error term. Leading asymptotics suffice because the target is a strict decay statement with a surviving logarithmic factor at the power boundary.

## 6. Boundaries and falsification

The parameter `alpha` is fixed as `H,y->infinity`; no uniformity is claimed when `alpha` itself approaches `1/2` with the support scale.

The result concerns the prime-power family over all primes `p<=y`. It does not automatically apply to sparse prime subsets, adaptive weights, signed/complex weights, or other tapers whose effective dimension has different asymptotics.

The polynomial law is exactly `y=H^delta` with fixed `delta`. Slowly varying modifications can matter on the critical boundary and must be inserted into the displayed error term rather than hidden inside the power notation.

The transfer remains for continuous vertical averaging and fixed moment order. It says nothing directly about Gram/discrete sampling, moving thresholds, shrinking targets, extreme tails, or hybrid source variables.

Falsify the finding by finding an error in the weighted-prime asymptotics, the endpoint `D_2` calculation, the parity exponent `e_k`, or the substitution into the `VIS-177` bound.

## Research consequence

The accepted prime-phase clue should no longer use the coarse rule `delta<1/K` as the best available finite-order polynomial-support null for prime-power weights. A fixed panel through order `K` remains representation-matched throughout the larger closed wedge `delta<=1/e_K`, with the odd-order improvement and the critical equality supplied by actual prime density.

The remaining positive-power opportunity is therefore not merely to cross `delta=1/K`. A candidate must exceed the appropriate order-dependent boundary, use complexity growing with support, require a stronger-than-moment functional, change the sampling regime, or introduce genuinely source-bearing information.