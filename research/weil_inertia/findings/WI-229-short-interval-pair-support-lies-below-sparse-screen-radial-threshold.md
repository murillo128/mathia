# WI-229 — short-interval pair support lies below the sparse-screen radial threshold

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + SUPPORT-BARRIER + PRIOR-ART-REDIRECT`.

WI-226 identifies Biao Wang's short-interval Montgomery theorem as a potentially reusable local input on the physical scale of a fixed-power Maynard--Pratt bow, even though its standalone simple/distinct-zero proportions are vacuous on the surviving bow range. WI-228 then identifies the exact count-tail interface that would kill the remaining deep radial-screen branch: at reciprocal harmonic `k`, a bow-normalized local horizontal-depth tail must decay with exponent strictly larger than `k/d`.

These two interfaces do **not** meet for the explicit strip-admissible sparse screen of WI-211. The obstruction is exact and occurs already at the first reciprocal harmonic.

Let

\[
M=T^{\vartheta+o(1)},
\qquad
2<d<3,
\qquad
L=\log T,
\tag{1}
\]

and consider the WI-211 two-pair screen. Its screening depth satisfies

\[
a=\log M+O(1),
\qquad
Y:=da,
\tag{2}
\]

while critical-strip admissibility requires

\[
\boxed{d\vartheta<\frac12.}
\tag{3}
\]

Wang's short-interval pair formula at bow exponent `vartheta` is available only for fixed Fourier support

\[
\boxed{0<\lambda<\vartheta.}
\tag{4}
\]

In the Fourier convention used in the unconditional Montgomery formula, a same-ordinate functional-equation mirror pair at normalized horizontal depth

\[
Y=(\beta-\tfrac12)L
\tag{5}
\]

enters a support-`lambda` test through

\[
\widehat g\!\left(\frac{i(\rho-\rho^*)L}{2\pi}\right)
=
\int_{-\lambda}^{\lambda}g(u)e^{2uY}\,du.
\tag{6}
\]

Hence, for every fixed admissible test profile,

\[
\boxed{
\left|
\widehat g\!\left(\frac{i(\rho-\rho^*)L}{2\pi}\right)
\right|
\le \|g\|_1 e^{2\lambda Y}.
}
\tag{7}
\]

The rational weight `4/(4-(rho-rho')^2)` in Wang's theorem is uniformly bounded on a functional-equation mirror pair inside the critical strip and supplies no additional exponential depth. Thus the strongest positive horizontal-depth exponent available from the support of this pair statistic is `2 lambda`.

But (3)--(4) give

\[
\boxed{2\lambda<2\vartheta<\frac1d.}
\tag{8}
\]

At the first reciprocal harmonic `k=1`, WI-228 requires a local tail exponent

\[
\boxed{\kappa>\frac1d.}
\tag{9}
\]

Therefore **even if one grants an ideal positive extraction of the deepest possible horizontal exponential moment from Wang's pair statistic, its support is on the wrong side of the exact WI-228 radial threshold**. In particular, granting the optimistic estimate

\[
\sum_{\rho\in\mathcal S}
\mu_\rho e^{2\lambda Y_\rho}
\ll M
\tag{10}
\]

for the source-relevant local screen would yield at best

\[
C_{\rm loc}(Y)
\ll M e^{-2\lambda Y},
\tag{11}
\]

whose slope `2 lambda` is strictly smaller than `1/d`. Equation (10) is deliberately stronger than what Wang's signed pair formula itself supplies; the theorem does not isolate complementary mirror terms as a positive sub-sum. The barrier therefore survives after giving the pair-correlation route this additional positivity for free.

The endpoint does not rescue the mechanism. Even if one hypothetically granted both unsupported endpoints `lambda=vartheta` and `d vartheta=1/2`, one would obtain only `2 lambda=1/d`, whereas WI-228 proves that the count-tail threshold is **strict**: slope `kappa=1/d` can still carry order-`M` first-harmonic radial source at arbitrarily large normalized depth.

Thus the route

\[
\text{bow-scale Wang pair correlation}
\longrightarrow
\text{positive local horizontal-depth tail}
\longrightarrow
\text{kill WI-228 deep screen}
\]

is closed for the WI-211 strip-admissible sparse-screen regime unless genuinely new arithmetic enlarges the effective short-interval support or a different observable uses information not captured by a positive pair-depth moment.

This is a route barrier, not a claim that Wang's local pair formula is useless. A source-fixed signed covariance, mixed/higher correlation, or another observable may exploit phases and cross terms that are explicitly discarded by the optimistic positive-moment reduction above.

## 1. The exact short-interval support budget

Wang's Theorem 2.2 fixes

\[
0<\lambda<\theta<1,
\tag{12}
\]

an even real `g in C_c^infty(R)` supported in `[-lambda,lambda]`, and `H=T^theta`. With `I=(T,T+H]` and `L=log T`, it proves

\[
\sum_{\gamma,\gamma'\in I}
\widehat g\!\left(\frac{i(\rho-\rho')L}{2\pi}\right)
\frac{4}{4-(\rho-\rho')^2}
=
\frac{HL}{2\pi}
\left(g(0)+\int_{\mathbb R}|u|g(u)\,du\right)
+O_g(H+T^\lambda L^2).
\tag{13}
\]

WI-226 checks from the displayed proof errors that the same limiting identity remains valid for

\[
H=T^{\theta+o(1)}
\tag{14}
\]

when `lambda<theta` remains fixed. This is the relevant form for a logarithmically shortened fixed-power bow. Nothing in the present finding strengthens Wang's theorem or lets `lambda` approach or exceed `theta` as a function of `T`.

The support restriction has an arithmetic meaning. Wang's Proposition 2.6 keeps the prime-length parameter uniformly in

\[
1\le x\le T^\lambda
\tag{15}
\]

and its displayed error contains an `x L^3` term. After the usual `x=T^u` integration, the normalized short-interval error is negligible because `lambda<theta`; crossing to `lambda>theta` would put the prime length beyond the interval scale `H=T^theta` and the printed error no longer gives the required asymptotic. Thus extending the support past the threshold needed below is not a matter of choosing a cleverer `g` inside the existing theorem. It requires new short-interval arithmetic.

## 2. Compact Fourier support caps horizontal exponential type

Use the Fourier convention inherited from Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh and used by Wang,

\[
\widehat g(z)
=
\int_{\mathbb R}g(u)e^{-2\pi i z u}\,du.
\tag{16}
\]

For a zero

\[
\rho=\frac12+\delta+i\gamma,
\qquad
0<\delta<\frac12,
\tag{17}
\]

its same-ordinate functional-equation mirror is

\[
\rho^*=1-\overline\rho
=\frac12-\delta+i\gamma.
\tag{18}
\]

Therefore

\[
\rho-\rho^*=2\delta,
\qquad
Y=\delta L,
\tag{19}
\]

and substitution into (16) gives exactly (6). Compact support now gives (7) by the triangle inequality. This is the elementary exponential-type bound; no Paley--Wiener converse is required.

The remaining pair weight is

\[
w(\rho-\rho^*)
=
\frac{4}{4-4\delta^2}
=
\frac1{1-\delta^2}.
\tag{20}
\]

Inside the critical strip `0<delta<1/2`,

\[
1<w(\rho-\rho^*)<\frac43.
\tag{21}
\]

Consequently the full mirror-pair factor is bounded by a fixed multiple of `e^{2 lambda Y}`. No choice of a fixed support-`lambda` test profile can change that exponential slope. Derivatives, finite linear combinations, or polynomial factors in `Y` would not change the slope either; Wang's theorem in any case is stated for a fixed smooth test with an `O_g` constant, not for an uncontrolled `T`-dependent family.

For two arbitrary strip zeros, the imaginary evaluation of `hat g` is governed by their horizontal difference and is likewise bounded by the exponential type determined by `lambda`. The functional-equation mirror gives the maximal horizontal separation associated with one depth and therefore already grants the strongest single-label exponential response relevant to a positive depth-tail estimate.

## 3. The explicit sparse screen sits beyond that support budget

WI-211 constructs, for `2<d<3`, an equal-depth selected bow of `M` right-half-plane labels and only two further right-half-plane off-line screening zeros together with their mirrors. The two screening pairs cancel the full reciprocal packet at

\[
\frac1d,
\qquad
\frac2d,
\tag{22}
\]

and their normalized radial parameter obeys

\[
a=\log M+O(1).
\tag{23}
\]

In physical horizontal coordinates their right-half-plane real part is

\[
\beta'
=\frac12+\frac{da}{L}
=\frac12+d\vartheta+o(1).
\tag{24}
\]

This is inside the critical strip exactly in the asymptotic regime (3). Its normalized horizontal depth in the present notation is

\[
Y=da
=d\log M+O(1)
=d\vartheta L+o(L).
\tag{25}
\]

The first reciprocal-harmonic radial weight of one such pair is

\[
\cosh a
\asymp e^a
\asymp M.
\tag{26}
\]

By contrast, even pushing Wang's allowed support arbitrarily close to `vartheta`, its maximal mirror-pair horizontal exponential is

\[
e^{2\lambda Y}
=
M^{2d\lambda+o(1)}.
\tag{27}
\]

Since

\[
2d\lambda<2d\vartheta<1,
\tag{28}
\]

we obtain

\[
\boxed{e^{2\lambda Y}=o(M).}
\tag{29}
\]

Thus an `O(1)` collection of WI-211 screening pairs can carry `Theta(M)` first-harmonic radial source while every admissible support-`lambda` positive mirror-depth charge is sub-main-scale. This is the same obstruction as (8)--(11) seen directly on the matched sparse screen.

Equation (29) must not be misread as saying that the **entire** Wang pair statistic is `o(M)` in the presence of the bow. There are cross terms between screen, bow, and complementary zeros, and they are not positive pieces that can be independently discarded. Such cross terms are precisely where a future source-fixed signed or covariance argument could carry additional information. The claim here concerns the positive depth-control route that attempts to extract a local tail from the support-limited pair statistic.

## 4. The slope mismatch remains even under ideal positive extraction

To remove any dependence on the sign structure of (13), grant a hypothetical theorem stronger than Wang in the direction most favorable to WI-228. Suppose the source-relevant screen itself satisfied, for every fixed `lambda<vartheta`,

\[
\sum_\rho \mu_\rho e^{2\lambda Y_\rho}
\le C_\lambda M.
\tag{30}
\]

Markov's inequality would give

\[
C_{\rm loc}(A)
:=\sum_{Y_\rho>A}\mu_\rho
\le
C_\lambda M e^{-2\lambda A}.
\tag{31}
\]

WI-228's exact count-tail calculation says that a tail

\[
C_{\rm loc}(A)\ll M e^{-\kappa A}
\tag{32}
\]

can make the first-harmonic weighted tail

\[
\sum_{Y_\rho>A}
\mu_\rho\cosh(Y_\rho/d)
\tag{33}
\]

negligible after a fixed cutoff only when

\[
\kappa>\frac1d.
\tag{34}
\]

But (31) has only `kappa=2 lambda`, and (8) places this strictly below `1/d` throughout the strip-admissible sparse-screen regime.

The mismatch is not an artifact of Markov's inequality. Fix any

\[
2\lambda\le\alpha:=\frac1d
\tag{35}
\]

and a large depth `Y_*`. Put

\[
q=
\left\lfloor cM e^{-\alpha Y_*}\right\rfloor
\tag{36}
\]

labels at that depth, with `Y_*` chosen so that `q>=1`. Then

\[
q\cosh(\alpha Y_*)\asymp M,
\tag{37}
\]

while for every `s<=2 lambda`,

\[
q e^{sY_*}
\ll M e^{-(\alpha-s)Y_*}
\le M.
\tag{38}
\]

Thus even simultaneous `O(M)` control of **all** positive exponential moments with slopes `s<2 vartheta` is logically compatible with order-`M` deep radial source whenever `2 vartheta<=1/d`. The actual strict strip condition gives room to spare.

At the formal boundary `2 vartheta=1/d`, a tail at slope exactly `1/d` still admits the same order-`M` construction, agreeing with WI-228's sharp strict threshold. Hence neither endpoint limiting nor a continuum of subcritical pair-support tests closes the branch.

## 5. Prior art and novelty audit

The literature-backed inputs are kept separate from the derived obstruction.

**Biao Wang, short-interval Montgomery theorem.** Wang, *Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals*, arXiv:2609.07918v1 (7 Sep 2026), proves (13) for `H=T^theta` and fixed `lambda<theta`, adapting the unconditional Montgomery method to short intervals. WI-226 independently checks the displayed errors needed for the `T^{theta+o(1)}` bow-scale extension. Wang's paper does not state the WI-228 radial-tail criterion or the comparison (8).

**Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh.** Their *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376; arXiv:2306.04799, is the unconditional pair-correlation framework underlying Wang's adaptation and fixes the Fourier convention used in (16). Their global results and zero-density hypotheses are not a local bow-normalized radial-tail theorem.

**Elementary Fourier analysis.** The exponential-type ceiling (7) follows directly from the compact support of `g`; no novelty is claimed for this fact, Markov's inequality, or the principle that an exponential moment of slope `s` controls at most an `e^{-sY}` count tail without additional information.

**Mathia deduction.** The new content is the exact conjunction of three already-audited interfaces: WI-211's strip-admissibility inequality `d vartheta<1/2`, Wang/WI-226's local support inequality `lambda<vartheta`, and WI-228's sharp first-harmonic requirement `kappa>1/d`. Their combination gives the strict impossible chain

\[
\boxed{
\kappa_{\rm pair}\le2\lambda
<2\vartheta
<\frac1d
<\kappa_{\rm needed}.
}
\tag{39}
\]

A bounded prior-art search around Wang's new preprint, unconditional Montgomery pair correlation, short-interval support barriers, and horizontal/off-critical zero control found the Wang and Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh sources but no theorem asserting this bow-specific support-versus-radial comparison. Absence of a search hit is not evidence of priority, and no priority claim is made.

## 6. Boundary conditions and failure modes

This finding deliberately closes only a specific natural route.

First, it concerns **positive local depth control extracted from Wang's support-limited pair statistic**. The pair formula is signed before its full sum is assembled; a future theorem could exploit correlations between the selected bow and complementary screen rather than attempt to isolate a positive mirror-pair sub-sum. Such a source-fixed covariance is outside (30)--(39).

Second, it does not prohibit higher correlations, mixed moments, matrix-valued tests, or another source observable from producing a stronger horizontal response. They must, however, genuinely change the arithmetic/support budget or use additional structure rather than repackage the same positive pair-depth moment.

Third, a new short-interval Montgomery theorem with effective support beyond the current interval exponent could escape the inequality `2 lambda<2 vartheta`. For the first harmonic one would need at least

\[
2\lambda>\frac1d,
\qquad\text{equivalently}\qquad
\lambda>\frac1{2d},
\tag{40}
\]

whereas the strip-admissible sparse screen has

\[
\vartheta<\frac1{2d}.
\tag{41}
\]

So the required support necessarily lies **past the bow interval exponent**. Wang's printed `xL^3` error explains why his present theorem does not reach that regime. An advance here would be genuinely new arithmetic, not test-function optimization within the existing support.

Fourth, the comparison uses the WI-211 sparse deep screen as a matched structural countermodel. It does not assert that those added zeros occur for zeta, nor that actual zeta zeros can realize arbitrary tails such as (36). The countermodel is sufficient only to show that the abstract positive-moment information class cannot by itself rule out the screen architecture.

Fifth, polylogarithmic normalization changes do not repair a fixed strict exponent gap. The argument grants the ideal bow-scale prefactor `M` in (30); any extra logarithmic loss in extracting a local moment only weakens the prospective tail bound.

## Research consequence

WI-226 left open the possibility that Wang's bow-scale pair identity, though useless through its standalone proportion corollaries, might feed the radial localization program as a local horizontal-density estimate. WI-229 closes that **source-independent positive-tail** version of the idea. On the exact sparse-screen regime that still matters, short-interval support `lambda<vartheta` implies maximum horizontal slope `2lambda`, while critical-strip admissibility forces that slope below the first reciprocal radial weight `1/d`.

The next useful use of Wang's theorem therefore cannot be “optimize `g` harder and insert the resulting positive depth tail into WI-228.” Progress must instead obtain a source-fixed signed/covariant constraint, a genuinely stronger local arithmetic theorem with effective prime length beyond the bow interval, or a different higher/mixed invariant whose horizontal-depth leverage is not capped by `2 vartheta`. The global simple-critical proportion is unchanged.