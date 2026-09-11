# VIS-169 — growing support has a universal `sqrt(d)` collision bulk law

## Claim

Keep the anchored held-out-prime Haar control of `VIS-164`--`VIS-168`. For retained support dimension `d>=1`, let

`X_1,X_2,...` and `Y`

be independent Haar-uniform coordinates on `T`, and define

`S_d = sum_(j=1)^d sin^2(pi X_j)`,

`N = |sin(pi Y)|`,

`C_d = N/sqrt(S_d)`

away from the Haar-null set `S_d=0`, with any value assigned there.

Then under the natural product coupling,

`sqrt(d) C_d -> sqrt(2) N`

almost surely as `d->infinity`. Hence `sqrt(d) C_d` converges in distribution to a compactly supported law on `[0,sqrt(2)]` with cumulative distribution function

`G(t)=0` for `t<0`,

`G(t)=(2/pi) arcsin(t/sqrt(2))` for `0<=t<=sqrt(2)`,

`G(t)=1` for `t>=sqrt(2)`.

Equivalently, for every fixed quantile level `alpha in (0,1)`,

`q_alpha(C_d) ~ sqrt(2/d) sin(pi alpha/2)`.

A quantitative concentration sandwich also holds. For every `0<epsilon<1/2`, write

`delta_(d,epsilon)=2 exp(-2 d epsilon^2)`

and let

`F_N(x)=P(N<=x)`

with the convention `F_N(x)=0` for `x<0` and `F_N(x)=1` for `x>=1`. Then for every `t>=0`,

`F_N(t sqrt(1/2-epsilon)) - delta_(d,epsilon)`

`<= P(sqrt(d) C_d <= t)`

`<= F_N(t sqrt(1/2+epsilon)) + delta_(d,epsilon)`.

Thus growing support has **two distinct matched-null scales**. The bulk collision score is generically of order `d^(-1/2)` and becomes stable after multiplication by `sqrt(d)`, while the large-collision regime `C_d>=L` with `L>=1` studied in `VIS-168` lies far outside that bulk and is controlled by a high-dimensional small-ball event.

**Evidence/status:** `EXACT-DERIVED + HIGH-DIMENSIONAL-MATCHED-NULL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is a Haar-population theorem. It is not a growing-dimensional equidistribution theorem for the deterministic prime-log orbit, a source-sensitive zeta separation, an extreme-value law, or an RH consequence.

## 1. The retained-phase denominator obeys a law of large numbers

Set

`U_j = sin^2(pi X_j)`.

The `U_j` are independent, identically distributed, bounded in `[0,1]`, and

`E[U_j]=int_0^1 sin^2(pi x) dx = 1/2`.

Therefore the strong law of large numbers gives

`S_d/d -> 1/2`

almost surely.

Since `N` does not depend on `d`, on the same probability-one event,

`sqrt(d) C_d`
` = N / sqrt(S_d/d)`
` -> sqrt(2) N`.

The denominator concentration is therefore not a prime-specific effect. It is the ordinary high-dimensional averaging of the retained Haar phases.

## 2. The limiting bulk law is explicit

For `0<=x<=1`,

`P(N<=x)`
` = P(|sin(pi Y)|<=x)`
` = (2/pi) arcsin x`.

The almost-sure limit from the previous section immediately gives

`P(sqrt(2) N <= t)`
` = (2/pi) arcsin(t/sqrt(2))`

for `0<=t<=sqrt(2)`, with the obvious zero and one extensions outside that interval.

Because this limiting distribution is continuous, the distribution functions of `sqrt(d) C_d` converge at every real `t`. Its quantile function on `(0,1)` is

`G^(-1)(alpha)=sqrt(2) sin(pi alpha/2)`.

Hence every fixed interior quantile of the unscaled collision score satisfies

`q_alpha(C_d) ~ d^(-1/2) G^(-1)(alpha)`
` = sqrt(2/d) sin(pi alpha/2)`.

This supplies an explicit matched-support normalization for bulk visual summaries such as medians, interquantile bands, and fixed interior quantiles.

## 3. Hoeffding concentration gives a finite-dimensional sandwich

For `0<epsilon<1/2`, define the good event

`E_(d,epsilon) = {|S_d/d - 1/2| <= epsilon}`.

Since `0<=U_j<=1`, Hoeffding's bounded-sum inequality gives

`P(E_(d,epsilon)^c) <= 2 exp(-2d epsilon^2)`.

On `E_(d,epsilon)`,

`1/2-epsilon <= S_d/d <= 1/2+epsilon`,

so

`N/sqrt(1/2+epsilon)`
` <= sqrt(d) C_d`
` <= N/sqrt(1/2-epsilon)`.

Therefore the event

`N <= t sqrt(1/2-epsilon)`

implies `sqrt(d)C_d<=t` on `E_(d,epsilon)`, while `sqrt(d)C_d<=t` on `E_(d,epsilon)` implies

`N <= t sqrt(1/2+epsilon)`.

Adding the probability of `E_(d,epsilon)^c` gives the claimed CDF sandwich.

For example, choosing any deterministic `epsilon_d->0` with `d epsilon_d^2->infinity` makes both the denominator perturbation and the concentration error vanish. No central-limit approximation is needed for the bulk law.

## 4. Bulk normalization and rare-collision normalization are different questions

`VIS-168` studies thresholds `L>=1`. At growing support, the present result says that a typical collision score is only of size `d^(-1/2)`. Therefore a fixed event such as

`C_d > 1`

corresponds after bulk normalization to

`sqrt(d) C_d > sqrt(d)`,

which escapes to infinity relative to the compact limiting bulk law. Such an event cannot be understood from denominator concentration around `d/2`; it requires the denominator to make an exceptional excursion toward its simultaneous zero.

That is exactly the small-ball geometry quantified in `VIS-168`, where

`log P(C_d>L)=-(d/2)log d-d log L+O(d)`

for `L>=1`.

The two findings therefore describe complementary regimes rather than competing normalizations:

- `sqrt(d) C_d` is the correct first-order coordinate for the **bulk** of the matched Haar null;
- `Q mu_d(L)` or an equivalent dimension-rescaled tail coordinate is required for **rare large collisions**.

A visual comparison that changes support dimension but plots raw `C_d` values can manufacture an apparent collapse toward zero even under the exact held-out-prime null. Conversely, multiplying by `sqrt(d)` does not normalize the extreme small-ball tail addressed by `VIS-168`.

## 5. Consequence for source-sensitive visual tests

The accepted prime-phase clue asks for a zeta-facing statistic that separates from matched omitted-prime controls after support, recurrence geometry, normalization, decoder class, and finite-window complexity are matched.

For any candidate based on the ordinary body of the collision distribution, support matching must now include the `sqrt(d)` bulk normalization. A shrinking raw median, interquantile width, or fixed-quantile collision score is not source evidence; it is forced by the retained-phase denominator concentration.

A candidate may still use tail exceedances, extremes, or singular losses, but then the bulk law is not the relevant null. Such a test must instead pass the `VIS-164`--`VIS-168` tail, moment, growing-cap, and population-mass gates.

This separates two failure modes that can otherwise look contradictory in plots: most collision scores shrink like `d^(-1/2)` while sufficiently high moments or extremes remain controlled by the rare near-zero denominator geometry. Both behaviors are generic consequences of the same matched Haar control.

## 6. Prior art and novelty boundary

The probabilistic ingredients are classical. The strong law of large numbers applied to bounded i.i.d. variables gives `S_d/d->1/2`, and the displayed finite-dimensional concentration estimate is Hoeffding's inequality. A standard original source is W. Hoeffding, **Probability Inequalities for Sums of Bounded Random Variables**, *Journal of the American Statistical Association* 58 (1963), 13--30, DOI `10.1080/01621459.1963.10500830`.

The distribution of `|sin(pi Y)|` and its arcsine CDF are elementary changes of variables. No new probability, concentration, or high-dimensional limit theorem is claimed.

The Mathia-specific content is the specialization to the anchored held-out-prime collision null and the resulting experimental-design control: after support grows, raw bulk collision shrinkage is a universal null effect with an explicit support normalization, distinct from the rare-event mass barrier already isolated in `VIS-168`.

## 7. Boundaries and falsification

The result concerns the Haar population with independent retained coordinates and held-out numerator coordinate. It does not by itself justify replacing the Haar law with a deterministic prime-log sample when `d=d(Q)` grows. Such a transfer still requires the changing-dimensional discrepancy control that remains open after `VIS-168`.

The `sqrt(d)` law describes fixed bulk quantiles and bounded distributional scales. It does not describe thresholds that diverge with `d`, the maximum over `Q` deterministic samples, or moments whose order grows with support. Those live in the tail regimes of `VIS-164`--`VIS-168`.

Falsify the bulk law by finding an error in `E[sin^2(pi X)]=1/2`, failure of independence in the stated Haar null, or a violation of the strong-law reduction `S_d/d->1/2`. Falsify the concentration statement by exhibiting a violation of Hoeffding's inequality for the bounded independent variables `U_j`.

## Research consequence

Growing support generically drives the ordinary collision cloud toward zero at rate `d^(-1/2)`. Future support-varying visualizations should therefore compare bulk collision geometry in the coordinate `sqrt(d) C_d`, not in raw `C_d`.

This does not solve the accepted prime-phase clue. It removes another false positive: apparent bulk stabilization or shrinkage caused solely by adding retained prime coordinates. A surviving zeta-facing effect must separate from the explicit arcsine bulk law after this normalization, or operate in a tail regime and pass the stronger `VIS-164`--`VIS-168` rare-event controls.