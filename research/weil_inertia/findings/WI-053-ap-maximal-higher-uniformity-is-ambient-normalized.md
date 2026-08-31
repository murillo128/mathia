# WI-053 — AP-maximal higher uniformity is ambient-normalized and does not close the Yang power-modulus fibers

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + PRIOR-ART-REDIRECTION + DECISIVE-NEGATIVE`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes a tempting repair route left open by WI-050--WI-052: the 2026 Matomäki--Radziwiłł--Shao--Tao--Teräväinen almost-all-short-interval theorem is substantially stronger than the 2019 MRT input, and its maximal norm already takes a supremum over arbitrary arithmetic progressions, but the estimate is normalized by the **ambient interval length**. On a Yang progression of step `r` containing `K` sampled points in an ambient span `H ~ rK`, the black-box theorem therefore gives an error of size `O(rK log^{-A} X)`, not `O(K log^{-A} X)`. For power-sized `r`, no fixed logarithmic saving yields relative cancellation on that progression.

The same source's generalized von Neumann lemma assumes all linear coefficients are bounded by a fixed parameter `L`, and its Hardy--Littlewood application explicitly allows replacing `0,1,...,ell-1` only by other **fixed** distinct integers. Hence the complexity-one observation of WI-051 cannot be combined directly with the 2026 Gowers theorem to obtain a coefficient-uniform asymptotic for the Yang forms `(m,m-rk,n,n-qk)` when `r,q=X^{Omega(1)}`.

A different prior-art direction is more relevant: Shao--Teräväinen's 2021 Bombieri--Vinogradov theorem for nilsequences gives an average-over-moduli, density-normalized twisted prime estimate up to `x^(1/4-epsilon)` when the nilsequence may vary with the modulus, and up to `x^(1/3-epsilon)` when it is fixed. This does suppress any **single coherent prime AP/Fourier mode** on a power-modulus subrange after Mertens weighting. It still does not control the nonzero pair-correlation fibers `A_r(t)` isolated by WI-051--WI-052, because those fibers are spectral-energy objects built from shifted-prime pairs rather than one twisted von Mangoldt progression. The shortest credible next step is therefore a bilinear/fiber square-function consequence of Bombieri--Vinogradov-nilsequence technology, not a direct citation of generic short-interval Gowers uniformity.

## 1. Exact 2026 theorem boundary

The primary source is

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen,
**Higher uniformity of arithmetic functions in short intervals II. Almost all intervals**, *Inventiones Mathematicae* 244 (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, arXiv:2411.05770.

For an interval `I`, their maximal-sum notation is

\[
\left|\sum_{n\in I}f(n)\right|^*
:=\sup_{P\subset I\cap\mathbb Z}
\left|\sum_{n\in P}f(n)\right|,
\tag{1}
\]

where the supremum is over **all arithmetic progressions** `P` in `I`. Thus the theorem already contains the kind of sparse progression selector that one might hope would bypass WI-051's quotient-localization problem.

Their Theorem 1.1(ii), in the prime case `theta=1/3`, gives for every fixed `A>0`, outside an exceptional set of `x` of logarithmically small measure,

\[
\sup_{g\in\operatorname{Poly}(\mathbb Z\to G)}
\left|
\sum_{x<n\le x+H}
(\Lambda(n)-\Lambda^\sharp(n))\overline{F(g(n)\Gamma)}
\right|^*
\le \frac{H}{(\log X)^A},
\tag{2}
\]

in the published short-interval range `X^(1/3+epsilon) <= H <= X^(1-epsilon)` (with the endpoint `H<=X` appearing in the abstract-level formulation). The precise approximant `Lambda^sharp` and nilsequence hypotheses are part of the theorem; they are not silently replaced here by the Yang four-prime local main.

The key point for the present audit is the normalization in (2): even after the supremum selects a very sparse progression, the right side remains `H log^{-A} X`, where `H` is the length of the **ambient interval**, not the cardinality of the selected progression.

Primary sources:

- https://doi.org/10.1007/s00222-026-01408-6
- https://arxiv.org/abs/2411.05770

## 2. Exact Yang scaling leaves a factor `r`

WI-051 reconstructs the dominant coprime Yang physical scales as

\[
M_m\asymp \frac{X}{b_2},
\qquad
M_n\asymp \frac{X}{b_1},
\qquad
K\asymp \frac{X}{b_1b_2},
\tag{3}
\]

with reduced coefficients

\[
r=\frac{b_1}{(b_1,b_2)},
\qquad
q=\frac{b_2}{(b_1,b_2)},
\tag{4}
\]

and, on the dominant coprime family,

\[
rK\asymp M_m,
\qquad
qK\asymp M_n.
\tag{5}
\]

Consider one leg of the source geometry,

\[
P=\{a+rk:1\le k\le K\},
\tag{6}
\]

inside an ambient interval of span

\[
H\asymp rK.
\tag{7}
\]

A Fourier mode in the `k` variable, say `e(theta k)`, is a degree-one nilsequence in `n=a+rk`:

\[
e(\theta k)
=e\!\left(\frac{\theta}{r}(n-a)\right).
\tag{8}
\]

Therefore, whenever the physical span lies in the admissible range of Theorem 1.1 (and likewise after subdividing a longer span into admissible pieces), the strongest direct use of the AP-maximal estimate (2) gives

\[
\left|
\sum_{k\le K}
(\Lambda(a+rk)-\Lambda^\sharp(a+rk))e(\theta k)
\right|
\ll_A
\frac{rK}{(\log X)^A}.
\tag{9}
\]

Dividing by the number `K` of sampled points yields

\[
\boxed{
\frac{\text{error}}{K}
\ll_A \frac{r}{(\log X)^A}.
}
\tag{10}
\]

This is the exact normalization wall. If

\[
r=(\log X)^B,
\]

choosing `A>B` gives `o(1)`, in agreement with the polylogarithmic regime already closed by WI-050. But if

\[
r=X^\alpha,
\qquad \alpha>0,
\tag{11}
\]

then for every fixed `A`,

\[
\frac{r}{(\log X)^A}\to\infty.
\tag{12}
\]

Thus the star-maximal theorem does **not** provide density-normalized cancellation on a power-sparse Yang progression. The fact that its supremum ranges over all arithmetic progressions does not recover the missing `1/r` density factor.

This is a black-box impossibility statement for this theorem, not a lower bound on the true prime error. A stronger theorem could of course have cancellation at the scale of the number of progression points.

## 3. The four-form Gowers route has the same coefficient boundary

WI-051 proves that the unsliced Yang system

\[
L_1=m,
\qquad
L_2=m-rk,
\qquad
L_3=n,
\qquad
L_4=n-qk
\tag{13}
\]

has Cauchy--Schwarz complexity exactly one. It is therefore natural to ask whether the 2026 short-interval `U^2`/higher-uniformity theorem plus generalized von Neumann now removes the coefficient wall.

The source-level answer is no. Lemma 8.4 of the 2026 paper states its generalized von Neumann theorem for affine-linear forms whose linear coefficients are bounded in modulus by a parameter `L`; the pseudorandomness parameter `D` is then required to be sufficiently large **depending on `L`** (as well as the fixed dimension/complexity data). The published theorem does not provide uniformity when

\[
L=L(X)\asymp\max(r,q)=X^{\Omega(1)}.
\tag{14}
\]

The application boundary is also explicit in the paper's Theorem 1.5. Its `ell`-point Hardy--Littlewood theorem is printed for the forms

\[
n,n+h,\ldots,n+(\ell-1)h,
\tag{15}
\]

and the authors note that the coefficients `0,1,...,ell-1` may be replaced by **any other fixed, distinct integers**. There is no claim there of uniformity for an `X`-dependent coefficient tuple.

Consequently the chain

\[
\boxed{
\text{Yang has CS complexity }1
+\text{2026 short-interval Gowers uniformity}
\Longrightarrow
\text{power-coefficient Yang four-form asymptotic}
}
\tag{16}
\]

is not justified by the published hypotheses. This sharpens WI-051: the latest broad higher-uniformity theorem still respects the same fixed/growing-coefficient distinction rather than bypassing it.

## 4. Bombieri--Vinogradov for nilsequences is a more relevant power-modulus input

A different theorem does interact correctly with a power-sized modulus. The primary source is

Xuancheng Shao and Joni Teräväinen,
**The Bombieri--Vinogradov theorem for nilsequences**, *Discrete Analysis* 2021:21, 55 pp., DOI `10.19086/da.29048`, arXiv:2006.05954.

Their Theorem 1.3 states, for fixed nilsequence complexity parameters and every fixed `A`,

\[
\sum_{d\le x^{1/4-\varepsilon}}
\max_{(c,d)=1}
\sup_{\psi\in\Psi_s(\Delta,\log x)}
|E_d(c,\psi)|
\ll
\frac{x}{(\log x)^A},
\tag{17}
\]

where `E_d(c,psi)` is the `Lambda(n) psi(n)` progression sum minus its explicit `W`-tricked local main. The nilsequence may vary with the modulus `d`. Their Theorem 1.4 increases the exponent to `1/3-epsilon` when `psi` is fixed independently of `d`.

Primary sources:

- https://doi.org/10.19086/da.29048
- https://arxiv.org/abs/2006.05954

This is structurally different from (2): the modulus average itself supplies the density normalization that the AP-maximal short-interval theorem lacks.

## 5. Exact Mertens-weighted consequence for one coherent mode

Let the physical prime-variable length be `M`, restrict for definiteness to prime moduli

\[
r\le R\le M^{1/4-\varepsilon},
\tag{18}
\]

and let `E_r` denote the maximum twisted progression discrepancy appearing in (17), with `x=M`. Define the progression-normalized amplitude

\[
F_r:=\frac rM E_r.
\tag{19}
\]

This normalization compares `E_r` with the natural number `M/r` of points in one residue class. On the prime-modulus Mertens weight used throughout the Yang coefficient analysis,

\[
w_r=\frac{\log r}{r},
\tag{20}
\]

Theorem 1.3 gives immediately

\[
\begin{aligned}
\sum_{r\le R\atop r\ \mathrm{prime}}w_rF_r
&=
\frac1M
\sum_{r\le R\atop r\ \mathrm{prime}}(\log r)E_r\\
&\le
\frac{\log R}{M}
\sum_{d\le R}E_d\\
&\ll_A (\log M)^{1-A}.
\end{aligned}
\tag{21}
\]

Hence

\[
\boxed{
\sum_{r\le R\atop r\ \mathrm{prime}}
\frac{\log r}{r}F_r=o(1)
}
\tag{22}
\]

for `A>1`. Using the trivial progression bound `F_r\ll\log M` and requesting a larger logarithmic exponent in (17) also gives

\[
\boxed{
\sum_{r\le R\atop r\ \mathrm{prime}}
\frac{\log r}{r}F_r^2=o(1).
}
\tag{23}
\]

Because the supremum in (17) includes all polynomial phases of fixed degree, (22)--(23) apply to any **single coherent linear Fourier mode** whose phase may depend on the modulus. This is a genuine power-modulus suppression mechanism that is absent from the direct use of (2).

No new theorem about primes is claimed in (21)--(23); they are elementary weighted consequences of Shao--Teräväinen Theorem 1.3.

## 6. Why this still does not close the WI-052 live fiber

The unresolved object from WI-051--WI-052 is not one normalized prime progression coefficient. On the natural localized groups WI-051 obtains a fiber representation of the schematic form

\[
\Lambda_{\rm loc}
=\sum_t A_r(t)A_q(-t),
\tag{24}
\]

where `A_r(t)` and `A_q(t)` are **pair-correlation/autocorrelation fibers**: each aggregates spectral products associated with translated prime pairs. WI-052 removes the `t=0` residue-class-constant quotient projection on fixed power-separated interiors by Barban--Davenport--Halberstam variance. The clue deliberately leaves `t\ne0` as the prime-specific open object.

Equations (22)--(23) suppress a single first-order Fourier/AP coefficient of the centered von Mangoldt function. They do not imply

\[
\sum_{t\ne0}|A_r(t)|^2=o(1)
\tag{25}
\]

or a source-weighted bound for

\[
\sum_{t\ne0}A_r(t)A_q(-t).
\tag{26}
\]

The distinction is information-theoretic: a spectrum may have every individual coefficient small while retaining substantial total `L^2` energy spread over many frequencies. In the prime setting the pair fibers also contain a shifted product before the final Fourier decomposition, so a one-prime twisted AP theorem cannot simply be substituted for the required bilinear square-function estimate.

Thus Shao--Teräväinen 2021 is a **redirection**, not a completed repair. It shows that the remaining power-modulus obstruction is narrower than “primes can carry an arbitrary coherent quotient mode”, but it does not yet discharge the locked four-prime covariance.

## 7. Prior-art and novelty audit

All analytic inputs used above are established literature:

- the AP-maximal nilsequence discorrelation and short-interval Gowers results are Matomäki--Radziwiłł--Shao--Tao--Teräväinen 2026;
- the fixed-coefficient generalized von Neumann framework is classical, with the exact coefficient dependence audited from their Lemma 8.4;
- the power-modulus nilsequence Bombieri--Vinogradov theorem is Shao--Teräväinen 2021;
- Bienvenu 2017 already supplies the polylogarithmic growing-coefficient finite-complexity regime used in WI-050.

No novelty or priority is claimed for those theorems, maximal sums, Fourier phases, or the weighted inequalities (21)--(23).

The durable Mathia contribution recorded here is the **source-faithful interface audit**:

1. insert the exact Yang physical relation `H~rK` into the 2026 star-maximal theorem and expose the surviving factor `r/log^A X`;
2. verify that the source generalized-von-Neumann/Hardy--Littlewood machinery retains fixed coefficient bounds and therefore does not directly cover `r,q=X^{Omega(1)}`;
3. identify Shao--Teräväinen's modulus-averaged nilsequence theorem as the relevant existing power-modulus input and derive its Mertens-weighted suppression of individual coherent modes;
4. separate that first-order suppression from the still-uncontrolled pair-fiber square function required by the exact Yang locked covariance.

This is a barrier/redirection finding, not a new prime-correlation theorem.

## 8. Decisive falsification / promotion gates

Narrow or retire the negative part of this finding if a source supplies any of the following with hypotheses matching the Yang power-coefficient region.

1. A short-interval nilsequence theorem maximal over progressions whose error is normalized by the **number of selected progression points**, e.g. `O((H/r) log^{-A}X)`, uniformly for `r=X^{Omega(1)}`.
2. A generalized von Neumann / prime linear-forms theorem uniform for coefficient bound `L=X^c` on the anisotropic Yang convex body, with an error strong enough relative to its volume.
3. A direct four-prime theorem for `(m,m-rk,n,n-qk)` with `r,q` in the source power range and the genuine local singular series of WI-049.

Promote the positive Shao--Teräväinen direction only after proving an estimate at the actual pair-fiber level, for example a source-weighted statement of the form

\[
\sum_r w_r\sum_{t\ne0}|A_r(t)|^2=o(1)
\tag{27}
\]

through a power-modulus subrange, or a bilinear estimate that directly makes (26) lower order. First-order twisted AP control alone is not enough.

## 9. Consequence for `weil_inertia`

This finding does not change the simple-critical zero bound. It does change where the one-sided fourth-moment audit should spend effort.

The route

\[
\boxed{
\text{cite latest short-interval higher uniformity}
\to
\text{apply complexity-one generalized von Neumann}
\to
\text{close power-sized Yang welding}
}
\tag{28}
\]

is closed as a black-box argument by the exact ambient normalization and fixed-coefficient hypotheses above.

The more credible route is now

\[
\boxed{
\text{power-modulus BV--nilsequence input}
\to
\text{pair-fiber / square-function upgrade}
\to
\text{nonzero }A_r(t)\text{ control}
\to
\text{locked covariance}.
}
\tag{29}
\]

This dovetails with the accepted `CLUE-yang-locked-covariance-leading-scale`: WI-052 already suppresses the pure quotient `t=0` component; the next evidence-changing target is whether modulus-averaged nilsequence technology can be lifted from individual prime Fourier modes to the **nonzero shifted-pair fibers** on a positive-mass power-modulus region. The shrinking short-shift boundary and the separately booked collision/analytic interface remain distinct.