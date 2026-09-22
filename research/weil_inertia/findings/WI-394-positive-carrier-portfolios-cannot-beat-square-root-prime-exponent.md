# WI-394 — positive carrier portfolios cannot beat the square-root-prime exponent

**Status:** `EXACT-DERIVED + CLASSICAL-EXPLICIT-FORMULA + SOURCE-EXACT + STRUCTURAL-BARRIER + PRIOR-ART-AUDITED + NON-ESTABLISHED-RH`.

## Claim

WI-392 identifies the fixed-depth response of the source-exact moving carrier, while WI-393 identifies the absolute prime-side cost of pushing its phase separation out to scale `A`. The two exponents imply a coefficient-independent obstruction that survives arbitrary **positive multiscale portfolios** of the existing carrier channel.

Fix a carrier packet width `Delta`, a support width `L`, an integer `M>=1`, and an interior horizontal-depth cap

\[
0\le \delta_*<\frac12,
\qquad
\kappa:=\frac12-\delta_*>0.
\tag{1}
\]

For one large carrier ordinate `R`, take any finite positive portfolio of the WI-392 source-exact separated trials with separations

\[
A_j\ge A_0\ge1,
\qquad
w_j\ge0,
\qquad
W:=\sum_j w_j.
\tag{2}
\]

The portfolio is at the quadratic-form level: its zero-side value is the nonnegative linear combination `sum_j w_j T_rho(f_{A_j,R})`. This includes arbitrary scalar retuning of already constructed channels and arbitrary positive mixing across separation scales; it does **not** include coherent cross terms between different trials.

Define the normalized componentwise absolute-prime budget

\[
\boxed{
B_{\rm abs}(R)
:=
\frac1{\log R}
\sum_j w_j e^{A_j/2}.
}
\tag{3}
\]

This is exactly the scale obtained by multiplying WI-393's `O(e^{A/2})` shifted-prime envelope by the portfolio weights and normalizing by the local zero-density scale `log R`.

Then every nontrivial zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad
|\delta|\le\delta_*,
\qquad
|\gamma-R|\le\Delta,
\tag{4}
\]

obeys

\[
\boxed{
\begin{aligned}
\left|\sum_j w_j T_\rho(f_{A_j,R})\right|
\ll_{L,\Delta,M}
&\ e^{-\kappa A_0} B_{\rm abs}(R)\\
&+W\frac{e^{-(1-\delta_*)A_0}}{A_0^2}\\
&+e^{-\kappa A_0}B_{\rm abs}(R)\,\log R\,R^{-2M}.
\end{aligned}
}
\tag{5}
\]

Consequently, if

\[
A_0\to\infty,
\qquad
W=O(1),
\qquad
B_{\rm abs}(R)=O(1),
\qquad
R\to\infty,
\tag{6}
\]

then the entire positive portfolio is asymptotically blind at order-one scale to every **fixed interior depth**:

\[
\boxed{
\sup_{|\delta|\le\delta_*\atop |\gamma-R|\le\Delta}
\left|\sum_j w_j T_\rho(f_{A_j,R})\right|
\longrightarrow0.
}
\tag{7}
\]

The conclusion already holds when the absolute prime budget is merely bounded. In the stronger regime needed by a uniform WI-393-style proof in which the shifted-prime error is required to be negligible relative to the local-density main term, `B_abs=o(1)`, the obstruction is only stronger.

Equivalently, after the source-mask and `R^{-M}` terms are negligible, forcing one fixed-depth defect to contribute at least a constant `d_0>0` requires

\[
\boxed{
B_{\rm abs}(R)
\gg d_0 e^{\kappa A_0}.
}
\tag{8}
\]

Thus no choice of smaller scalar amplitudes, no distribution of positive weight over many larger separations, and no positive convex portfolio of the present channels can remove the exponent mismatch. At fixed depth, the defect grows like `e^{A|delta|}` whereas the componentwise absolute prime envelope grows like `e^{A/2}`. Since `|delta|<1/2`, the prime exponent wins by the fixed gap `kappa`.

This is a route barrier, not an impossibility theorem for the Weil form. It leaves open arithmetic cancellation in the shifted prime polynomial, Fourier shaping that zeros or cancels prime-power samples, coherent signed/matrix-valued couplings with cross terms, aggregation of many exceptional zeros, and zeros whose depth approaches the edge `|delta|=1/2` fast enough that `kappa A` stays bounded. No unconditional RH conclusion or improved simple-critical-zero proportion is claimed.

## 1. WI-392 gives the source-exact fixed-depth response

For one WI-392 trial, equation (31) there gives uniformly on (4)

\[
|T_\rho(f_{A,R})|
\ll_{L,\Delta,M}
\frac{e^{A\delta_*}}{\log R}
+
\frac{e^{-A(1-\delta_*)}}{A^2}
+
e^{A\delta_*}R^{-2M}.
\tag{9}
\]

The three terms have distinct origins. The first is the deliberately diluted moving carrier; the second is exact source-slot perforation leakage; the third is the rapidly decaying fixed-base Fourier tail. The estimate is unconditional for the individual zero once that zero is given: RH is not used in deriving the off-line Hermitian product bound.

Positive weighting and the triangle inequality give

\[
\begin{aligned}
\left|\sum_jw_jT_\rho(f_{A_j,R})\right|
\ll
&\frac1{\log R}\sum_jw_je^{A_j\delta_*}\\
&+\sum_jw_j\frac{e^{-A_j(1-\delta_*)}}{A_j^2}\\
&+R^{-2M}\sum_jw_je^{A_j\delta_*}.
\end{aligned}
\tag{10}
\]

No cancellation between functional-equation partners or between portfolio components is assumed.

## 2. The carrier term is an exponentially damped square-root-prime budget

For every `A_j>=A_0`,

\[
e^{A_j\delta_*}
=
e^{A_j/2}e^{-\kappa A_j}
\le
e^{-\kappa A_0}e^{A_j/2}.
\tag{11}
\]

Therefore

\[
\boxed{
\frac1{\log R}\sum_jw_je^{A_j\delta_*}
\le
e^{-\kappa A_0}B_{\rm abs}(R).
}
\tag{12}
\]

The same identity controls the fixed-base tail:

\[
R^{-2M}\sum_jw_je^{A_j\delta_*}
\le
e^{-\kappa A_0}B_{\rm abs}(R)\,\log R\,R^{-2M}.
\tag{13}
\]

Since `A>=1 -> e^{-A(1-delta_*)}/A^2` is decreasing,

\[
\sum_jw_j\frac{e^{-A_j(1-\delta_*)}}{A_j^2}
\le
W\frac{e^{-A_0(1-\delta_*)}}{A_0^2}.
\tag{14}
\]

Equations (10)--(14) prove (5). Under (6), the first two terms tend to zero exponentially in `A_0`; the last does as well because `log R R^{-2M}->0`. This proves (7).

The core inequality (12) has a useful measure form. Let a positive measure `mu` encode a continuum portfolio of carrier separations and define the square-root-prime measure

\[
d\nu(A)=\frac{e^{A/2}}{\log R}\,d\mu(A).
\tag{15}
\]

Then its fixed-depth carrier response is

\[
\frac1{\log R}\int e^{A\delta_*}\,d\mu(A)
=
\int e^{-\kappa A}\,d\nu(A).
\tag{16}
\]

So fixed-depth observation is literally a Laplace transform of the absolute-prime budget measure. If the total `nu`-mass stays bounded while its support escapes to `A>=A_0->infinity`, (16) vanishes uniformly. The obstruction is therefore not tied to choosing one separation parameter or to a finite number of components.

## 3. WI-393 identifies `B_abs` as the no-cancellation arithmetic cost

WI-393 tests the phase factor with a fixed Beurling--Selberg minorant

\[
H_{R,A}(t)=m(t-R)\sin^2(At/2).
\]

Its Fourier transform has shifted bands near `+-A`. In the Guinand--Weil explicit formula those bands sample prime powers with `log n=A+O(1)`. Without exploiting cancellation, Chebyshev plus partial summation gives

\[
\mathcal P(H_{R,A})=O(e^{A/2}),
\tag{17}
\]

while the local zero-density main term is of order `log R`. Scaling the test by a positive coefficient `w_j` scales both terms linearly. Summing componentwise absolute estimates therefore costs precisely the budget (3), up to the fixed constants attached to the minorant.

This explains why scalar amplitude retuning cannot help. Multiplying one component by a small positive factor reduces both its fixed-depth defect response and its absolute prime cost by the same factor. The ratio remains

\[
\frac{e^{A\delta_*}}{e^{A/2}}
=
e^{-\kappa A}.
\tag{18}
\]

Spreading the mass over many separations cannot improve that ratio either: positivity makes the best ratio occur at the smallest separation in the portfolio, which is exactly (12).

If a WI-393-style argument is to retain a uniform positive critical-line reserve by treating every shifted prime band in absolute value, its normalized total prime error must remain controlled. Equation (7) then says that moving all positive carrier mass to larger and larger separations necessarily destroys order-one sensitivity to any fixed interior off-line zero. Conversely, an order-one fixed-depth charge forces the componentwise absolute prime budget to grow exponentially by (8), swamping the very main term that the absolute-envelope proof is meant to protect.

## 4. What this closes

The result closes a natural continuation of WI-393 in which one tries to repair sparse-defect blindness **without adding arithmetic information** by changing only scalar weights or by mixing many copies of the same carrier geometry.

In particular, none of the following changes the exponent balance:

- replacing the standard carrier coefficient by any smaller positive scalar and compensating with larger `A`;
- distributing a bounded total quadratic weight over finitely many separations `A_j`;
- taking countably many or continuously distributed positive scales with bounded square-root-prime budget;
- letting the number of positive components grow, provided the total portfolio weight and componentwise absolute-prime budget remain bounded.

The last statement follows from monotone convergence applied to (16); finite portfolios were used above only to avoid measure-theoretic notation in the source-mask terms.

This barrier is stronger than the single-channel crossover statement in WI-393. WI-393 says that one carrier reaches its absolute-prime wall before it robustly amplifies a fixed-depth defect. The present result says that **positive multiscale diversification does not average that wall away**: the whole positive cone has exponentially vanishing operator norm from the square-root-prime budget to fixed-depth defect observations once its separation support moves to infinity.

## 5. Boundaries and escape routes

The hypotheses are deliberately narrow enough that the conclusion is exact.

First, `B_abs` is an **absolute-envelope proof budget**, not the actual signed prime polynomial. Equation (17) is an upper bound. The argument does not prove that the true prime term is large. If arithmetic cancellation makes the shifted prime polynomial much smaller at defect-anchored ordinates, the budget (3) is no longer the right cost and the barrier can be bypassed. This is precisely the arithmetic gate left open by WI-393.

Second, positivity is essential. A coherent trial combining several Fourier lobes can generate cross terms before the quadratic form is evaluated; a signed or matrix-valued certificate can exploit cancellations that are erased by the componentwise triangle inequality in (10). Such constructions are not positive portfolios in the sense of (2) and are not ruled out here.

Third, the fixed interior-depth hypothesis is essential. If

\[
\delta_* = \frac12-\kappa_R,
\qquad
\kappa_R A_0=O(1),
\]

then the damping factor `e^{-kappa_R A_0}` need not vanish. Known zero-free regions do not supply a uniform positive `kappa` for every possible off-critical zero at growing height, so (7) cannot by itself exclude all RH failures.

Fourth, the result concerns one selected zero or a packet whose total multiplicity is small enough that multiplying (5) by that multiplicity still tends to zero. A sufficiently large exceptional population can overcome the per-zero damping. That is an aggregation mechanism, not individual-defect detection, and remains logically separate.

Finally, this is a statement about the moving-frequency carrier branch. Bombieri's cofinal finite-inertia theorem and the localized Suzuki/Bombieri witnesses remain capable of detecting finite RH failure by other tests; WI-236, WI-247, and the later source-exact program already distinguish completeness from uniform spectral margin.

## 6. Prior art and novelty boundary

The ingredients on the explicit-formula side are classical. Beurling--Selberg interval minorants and compact Fourier support are standard; WI-393 anchors Jeffrey Vaaler's 1985 extremal-function survey and Emanuel Carneiro's 2011 survey. Guinand--Weil converts the shifted Fourier bands into prime-power sums, and the square-root weight `Lambda(n)/sqrt(n)` gives the `e^{A/2}` absolute scale by Chebyshev and partial summation. Landau--Gonek formulas, including Farzad Aryan's 2022 extension, provide neighboring classical formulations of the same prime-power sensitivity.

The off-line exponent `e^{A|delta|}` is not imported from prior art here; it is the exact centered-coordinate separation law derived in WI-392 for the source-exact Mathia carrier. A targeted prior-art audit around bandlimited explicit formulas, Beurling--Selberg modulation, Paley--Wiener/exponential-type bounds, and weighted prime sums found the classical ingredients but no source stating this exact positive-portfolio cone inequality for the WI-392/WI-393 interface. This is not a priority claim. The durable contribution recorded here is the exact Mathia-internal consequence (5)--(8) and the resulting route closure.

## Decisive audit test

The claim can be falsified only by breaking one of its explicitly stated interfaces. For each positively weighted component, verify independently that:

1. the source-exact fixed-depth zero contribution satisfies WI-392 equation (31) with a constant uniform in `A` over the stated support/packet class;
2. the no-cancellation shifted-prime envelope scales linearly with the same positive portfolio weight and as `e^{A/2}`, as in WI-393;
3. no coherent cross term is silently included in a portfolio that has been declared componentwise positive.

Given those three interfaces, (11)--(16) are exact algebra. A new arithmetic theorem lowering the actual shifted-prime polynomial below its absolute envelope, or a coherent construction whose defect response is not a positive sum of the WI-392 channels, would not falsify this finding; it would leave its hypothesis class.

## Research consequence

The next sparse-defect step cannot be obtained by scalar retuning or positive multiscale diversification of the existing dilute carrier while the prime side is controlled componentwise in absolute value. For every fixed interior depth, that entire cone loses defect sensitivity exponentially faster than it can keep the square-root-prime budget under control.

The live routes are therefore the ones already suggested qualitatively by WI-393 but now separated from this closed family: prove cancellation or structured subtraction in the defect-anchored shifted prime polynomial; build a genuinely coherent/sign-sensitive carrier whose quadratic cross terms change the exponent law; aggregate exceptional mass before per-zero dilution kills it; or obtain information that prevents RH failure from approaching the strip edge on the carrier scale.