# WI-320 — A short positive witness closes the adaptive scalar-localization bootstrap

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-AUDITED`.

**Parent findings:** WI-304, WI-311, WI-317, WI-318, WI-319.

WI-317 showed that a fixed finite portfolio of source-exact smooth localizations cannot improve a scalar lower semibound merely by feeding that same scalar semibound into the localized copies. WI-318 extended the obstruction to arbitrary adaptive families with a uniform `H^1` budget, while WI-319 showed that the common high-frequency recurrence witness used there becomes non-uniform at the sharp complexity scale `M_t \asymp t^2/\log t`. That left open the logical possibility that an arbitrarily oscillatory localizer, selected after seeing the test vector, could produce a strict scalar contraction.

That loophole is not real. A different test vector closes it without any regularity, frequency, cardinality, or complexity bound on the localization family. The source-exact defect has an archimedean coefficient that is strictly positive on the entire interval `(0,h_0)`, where

\[
h_0=\log\rho,
\qquad \rho^3-\rho-1=0,
\]

and `h_0<\log2`. A nonnegative smooth test function supported in an interval of diameter less than `h_0` has nonnegative autocorrelation only in that positive archimedean zone and has zero autocorrelation at every prime-power lag. Since every normalized real multiwindow localizer has aggregate autocorrelation at most one, its localization defect on this one test vector is nonnegative.

Consequently, for the complete class of admissible smooth real source-exact multiwindow localizers of WI-311, even when the localizer is chosen adaptively after seeing `f`, reusing only the same scalar lower semibound on all localized pieces can never improve that scalar constant by any uniform positive amount. The escape identified in WI-319 defeats one recurrence falsifier, not the scalar-bootstrap obstruction itself.

## 1. Exact scalar-contraction criterion

Fix an outer aperture `L>0`, and let `Q` denote the source-exact Weil quadratic form on the corresponding compact-support domain. For every admissible localization family `r`, let

\[
\{g^{(r)}_\nu\}_{\nu=1}^{J_r}
\subset C_c^\infty((-1/2,1/2);\mathbb R)
\]

be a finite real multiwindow family satisfying

\[
\sum_{\nu=1}^{J_r}\|g^{(r)}_\nu\|_2^2=1.
\tag{1}
\]

Write

\[
R_r(a)
:=
\sum_{\nu=1}^{J_r}
\int_{\mathbb R}g^{(r)}_\nu(u+a)g^{(r)}_\nu(u)\,du
\tag{2}
\]

for its aggregate autocorrelation. WI-311 gives the exact localization identity

\[
Q(f)=\operatorname{Loc}_r(f)-\mathcal E_r(f),
\tag{3}
\]

with the normalization

\[
\sum_\nu\int\|g^{(r)}_\nu(\cdot)f(\cdot+y)\|_2^2\,dy
=\|f\|_2^2.
\tag{4}
\]

Suppose the only estimate fed into every localized source term is the same scalar semibound

\[
Q(h)\ge-c\|h\|_2^2.
\tag{5}
\]

Then (4)--(5) imply

\[
\operatorname{Loc}_r(f)\ge-c\|f\|_2^2,
\]

and hence

\[
Q(f)\ge-c\|f\|_2^2-\mathcal E_r(f).
\tag{6}
\]

If an arbitrary class `\mathcal R` of admissible localizers is available and `r` may be chosen after observing `f`, a uniform contraction from `c` to `c-\kappa_0`, with `\kappa_0>0`, can follow from (6) only if

\[
\boxed{
\inf_{r\in\mathcal R}\mathcal E_r(f)
\le-\kappa_0\|f\|_2^2
\quad\text{for every }f.
}
\tag{7}
\]

This is the same necessary condition isolated in WI-317/WI-318, now with no restriction on the cardinality or complexity of `\mathcal R`.

## 2. The source-exact archimedean defect is positive up to the plastic-constant scale

The exact defect formula audited in WI-304 and extended to multiwindows in WI-311 is

\[
\mathcal E_r(f)
=
\int_0^{2L}
(1-R_r(a))K(a)H_f(a)\,da
+
\sum_{\log n<2L}
\frac{2\Lambda(n)}{\sqrt n}
(1-R_r(\log n))H_f(\log n),
\tag{8}
\]

where

\[
H_f(a)=\operatorname{Re}\int_{\mathbb R}f(u+a)\overline{f(u)}\,du
\tag{9}
\]

and

\[
K(a)
=
\frac{2e^{-a/2}}{1-e^{-2a}}
-4\cosh(a/2).
\tag{10}
\]

The sign of `K` is elementary and exact. Since

\[
\frac{2e^{-a/2}}{1-e^{-2a}}
=
\frac{e^{a/2}}{\sinh a},
\]

for `a>0` we have

\[
K(a)>0
\iff
 e^{a/2}>4\sinh(a)\cosh(a/2).
\tag{11}
\]

Put `x=e^a>1`. Using `\sinh a=2\sinh(a/2)\cosh(a/2)`, (11) is equivalent to

\[
x^2>(x-1)(x+1)^2
\iff
x^3-x-1<0.
\tag{12}
\]

Let `\rho>1` be the unique real root of `x^3-x-1=0` and put

\[
h_0:=\log\rho
=0.2811995743\ldots.
\tag{13}
\]

It follows that

\[
\boxed{K(a)>0\quad(0<a<h_0).}
\tag{14}
\]

Moreover `\rho<2`, so

\[
\boxed{h_0<\log2.}
\tag{15}
\]

The same plastic-constant scale appears in WI-268 through the sign of Suzuki's continuous cross kernel, but the use here is different: (14) is a direct positivity region of the localization *defect* in (8).

## 3. One short nonnegative bump defeats every adaptive localizer

Fix any `L>0`. Choose

\[
0<d<\min\{2L,h_0\}
\tag{16}
\]

and a nonzero real nonnegative function

\[
f\in C_c^\infty((-L,L))
\tag{17}
\]

whose support is contained in an interval of diameter strictly smaller than `d`. Then its autocorrelation satisfies

\[
H_f(a)=\int f(u+a)f(u)\,du\ge0
\quad(a\ge0),
\tag{18}
\]

and, by support separation,

\[
H_f(a)=0
\quad(a\ge d).
\tag{19}
\]

Because `d<h_0<\log2`, every prime-power lag satisfies

\[
\log n\ge\log2>d,
\]

so (19) gives

\[
H_f(\log n)=0
\qquad(n\ge2).
\tag{20}
\]

Thus the entire discrete arithmetic sum in (8) vanishes exactly, regardless of which prime powers are active at the outer aperture `L`.

Now fix an arbitrary admissible multiwindow family `r`. Bundle its windows as the vector-valued function

\[
G_r=(g^{(r)}_1,\ldots,g^{(r)}_{J_r}).
\]

By (1), `\|G_r\|_2=1`, while (2) is

\[
R_r(a)=\langle T_aG_r,G_r\rangle.
\]

Cauchy--Schwarz therefore gives

\[
R_r(a)\le1
\qquad(a\in\mathbb R),
\tag{21}
\]

so

\[
1-R_r(a)\ge0.
\tag{22}
\]

Combining (14), (18)--(22), the exact defect reduces to

\[
\begin{aligned}
\mathcal E_r(f)
&=
\int_0^d(1-R_r(a))K(a)H_f(a)\,da\\
&\ge0.
\end{aligned}
\tag{23}
\]

Nothing in this argument depends on a derivative bound, carrier-frequency bound, finite portfolio, recurrence theorem, or a uniform estimate over `r`. The same fixed test vector `f` works pointwise for **every** admissible localization family. Hence for an arbitrary class `\mathcal R`, including the entire admissible class,

\[
\boxed{
\inf_{r\in\mathcal R}\mathcal E_r(f)\ge0.
}
\tag{24}
\]

Equation (24) contradicts the necessary contraction condition (7) for every `\kappa_0>0`.

Therefore

\[
\boxed{
\text{source-exact adaptive localization cannot strictly contract a scalar Weil semibound}
}
\tag{25}
\]

when the only information supplied on the localized pieces is that same scalar semibound.

## 4. What this closes, and what remains open

The result strictly strengthens the architectural conclusions of WI-317--WI-319.

WI-317 used a common high-frequency recurrence sequence to defeat fixed finite portfolios. WI-318 made the recurrence argument uniform over infinite adaptive families under a bounded total `H^1` budget. WI-319 then proved that this particular recurrence obstruction has a sharp complexity boundary: localizers with derivative energy of order `t^2/\log t` can make the continuous defect survive on the recurrent high-frequency witness and can defeat that witness.

Equation (24) shows that crossing the WI-319 complexity threshold does **not** reopen scalar contraction. Arbitrarily oscillatory localizers still fail the universal quantifier in (7), because a short nonnegative prime-free bump has nonnegative defect for every localizer. Thus the `t^2/\log t` scale is sharp for the recurrence falsifier, not for the scalar-bootstrap architecture.

The no-go is specific and does not say localization is useless. It leaves open mechanisms that add information absent from the scalar premise (5), including:

- localized lower bounds genuinely stronger than the global scalar constant and justified by new arithmetic or spectral input;
- vector-, matrix-, mode-, or prime-dependent state carried between scales instead of one scalar defect;
- another source-exact decomposition whose correction is not constrained by the sign structure (8);
- direct coercivity or inertia control that does not attempt to bootstrap the same scalar semibound through localized copies.

Those are now necessities rather than optional refinements if this localization program is to contribute to defect elimination.

## 5. Stress tests and validation boundary

**No hidden prime term.** The witness is chosen with support diameter `d<h_0<\log2`. Its autocorrelation therefore vanishes at every `\log n`, not merely at the first few active lags. The arithmetic sum is exactly zero even when the outer aperture is arbitrarily large.

**No sign assumption on the localizer.** The windows themselves may change sign and may oscillate arbitrarily rapidly. The proof uses only the normalized aggregate autocorrelation bound `R_r(a)\le1`. It does not require `R_r(a)\ge0`.

**No compactness of the adaptive family.** Unlike WI-317/WI-318, there is no interchange of an infimum with a limit and no uniform Riemann--Lebesgue step. The defect is nonnegative for each `r` on the same fixed vector before any infimum is taken.

**Complexity is unrestricted but each localization is source-admissible.** The statement applies to the smooth finite real multiwindow families for which the WI-311 source-exact identity holds. It does not assert an identity for an arbitrary distributional or non-source-admissible localization rule.

**The result is a no-go for scalar feedback, not RH.** It gives no new zero-density estimate and does not imply positivity of the Weil form. It says only that a strict lower-semibound improvement cannot be generated autonomously by reusing the same scalar lower bound through this localization identity.

## 6. Prior-art and novelty audit

The source-exact defect identity is literature-backed through Vincent Liu's 2026 manuscript **Certified Weil Positivity Beyond the Unit Window: Source-Exact Block-Schur and Tail-Compensation Bounds for the Riemann Zeta Function**, frozen at source commit `b6cd2183c1e79c6c27a34267812a7b2d73ed1b59`, and was audited in WI-304. WI-311 established the exact normalized multiwindow extension used here. The scalar-feedback algebra behind (7) is the standard localization/IMS pattern and was already isolated in WI-317.

The new step is the source-specific short-support witness (16)--(24): the positive archimedean defect interval lies strictly below the first arithmetic lag, so one fixed nonnegative bump simultaneously removes all prime terms and makes every admissible localization correction nonnegative. A targeted audit around Weil-form localization, source-exact autocorrelation defects, IMS lower-semibound bootstraps, and adaptive localization found Liu's localization formula and generic IMS semibound machinery but no source stating this all-adaptive scalar-feedback obstruction. Search absence is not a priority claim.

Within the local corpus this is not a restatement of WI-255 or WI-268. WI-255 concerns the first subleading small-aperture expansion of a hypothetical Suzuki zero mode; WI-268 uses the opposite-side sign change of a related continuous kernel to obstruct positivity-preserving semigroups. WI-317--WI-319 concern the same scalar-localization architecture but leave, then quantify, the high-complexity adaptive loophole. The present finding closes that loophole by changing the falsifying direction rather than by strengthening the recurrence estimate.

## 7. Consequence for the Weil-inertia program

The current source-exact localization chain can still reorganize the Weil form and expose finite-sector structure, but it cannot by itself create the nonvanishing scalar defect contraction required after WI-316. The remaining RH-facing route must preserve more than the bottom scalar semibound: it needs new arithmetic information, a non-scalar invariant, or a genuinely different coercivity mechanism.

This is a decisive closure of one natural bootstrap architecture. It does not close localization-based research generally; it sharply identifies the information that any surviving localization mechanism must add.