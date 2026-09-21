# PL-406 — The cubic source test kills the Ramanujan energy diagonal but moves the live bridge into the prime-variance / zero-pair sector

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BASED + PRIOR-ART-REDIRECT + QUANTITATIVE-OBSTRUCTION`.

**Parent findings:** `PL-404`, `PL-405`.

## Claim

`PL-405` identifies the singular-series source in `PL-404` as the critical boundary of a Ramanujan covariance family whose `B^2` energy diverges logarithmically at lag zero. That divergence is real, but it is **not itself present in the final cubic source test**: the shifted Abel weight

\[
w_\eta^{[2]}(u)
=u e^{-\eta u^3}\sin(\pi u^3/6)
\tag{1}
\]

satisfies

\[
w_\eta^{[2]}(0)=0,
\qquad
w_\eta^{[2]}(u)=\frac\pi6u^4+O_\eta(u^7)
\quad(u\downarrow0).
\tag{2}
\]

Thus the tested statistic annihilates the divergent zero-lag covariance exactly. The endpoint problem from `PL-405` does not disappear — ordinary `B^2` convergence still fails, so one may not interchange the Ramanujan and arithmetic limits by Parseval — but the surviving obstruction is **off-diagonal**.

More precisely, after the natural even extension

\[
K_\eta(x)
:=|x|e^{-\eta|x|^3}\sin(\pi|x|^3/6),
\tag{3}
\]

any finite arithmetic sequence has an exact representation of the corresponding weighted shift-correlation as both

1. a quadratic additive Fourier statistic, and
2. a signed superposition of triangular short-interval second moments.

Consequently the actual source-replacement target in `PL-405` lies in the classical **prime short-interval variance / zero pair-correlation sector**, not in an ordinary finite-energy Ramanujan-covariance theorem.

This is a useful redirect because current theorems on averaged prime-pair correlations do reach the relevant growing-shift regime, but their precision is far too coarse for the `PL-404` zero layer. The `PL-404` normalization requires an error

\[
o(H^{-7/4})
\tag{4}
\]

in the weighted source average. Existing almost-all-shift Hardy--Littlewood results provide qualitative `o(1)` or arbitrary **fixed logarithmic** savings in polynomial shift ranges. Such bounds cannot preserve (4): for every fixed `A>0` and every fixed `theta>0`,

\[
H=X^\theta
\quad\Longrightarrow\quad
(\log X)^{-A}\gg H^{-7/4}.
\tag{5}
\]

This is not an impossibility theorem for the special cubic weight. Its sign changes may create cancellation that average absolute-error estimates throw away. The live route is therefore sharper: exploit the specific quadratic kernel, plausibly through explicit-formula / zero-pair machinery, rather than expect a generic averaged Hardy--Littlewood theorem to descend automatically to the `H^{-7/4}` layer.

## 1. The PL-404 weight removes the infinite-energy diagonal exactly

For `delta>0`, `PL-405` has the rigorous finite-energy covariance

\[
\mathfrak S_\delta(h)
=
\lim_{X\to\infty}\frac1X
\sum_{n\le X}L_\delta(n)L_\delta(n+h),
\tag{6}
\]

while

\[
\mathfrak S_\delta(0)
=\|L_\delta\|_{B^2}^2
\sim\frac1{2\delta}
\quad(\delta\downarrow0).
\tag{7}
\]

The cubic source statistic, however, tests only positive lags and has the fourth-order zero (2). On symmetrizing the lag variable, the coefficient of the lag-zero covariance is exactly

\[
K_\eta(0)=0.
\tag{8}
\]

Thus the divergent term (7) is absent from the tested functional for every `delta`, before taking any limit.

There is a second way to see the same cancellation below. The triangular-moment representation expresses the tested functional as an integral of positive-scale second moments against the **signed** measure `K_eta''(t)dt`. Every triangular second moment contains its diagonal energy, but the total diagonal coefficient is

\[
\int_0^\infty tK_\eta''(t)\,dt
=K_\eta(0)
=0,
\tag{9}
\]

where the boundary terms vanish because `K_eta` and `K_eta'` decay exponentially. The endpoint energy is therefore canceled by the declared arithmetic test itself, not by an auxiliary subtraction added after the fact.

This does **not** validate the formal `delta=0` Wiener--Khintchine step. Lack of `B^2` convergence can still obstruct passage from the regulated functions `L_delta` to the actual modified Mangoldt function. What (8)--(9) show is narrower: any final obstruction has to survive after the zero-lag energy has been projected out.

## 2. Exact quadratic Fourier representation

Let `f: Z -> C` have finite support and define

\[
C_f(h)
:=\sum_{n\in\mathbb Z}f(n)\overline{f(n+h)}.
\tag{10}
\]

For an even summable kernel `K`, put

\[
Q_{K,H}(f)
:=\sum_{h\in\mathbb Z}K(h/H)C_f(h).
\tag{11}
\]

Writing

\[
F(\alpha)=\sum_n f(n)e^{2\pi i n\alpha},
\qquad
\Theta_{K,H}(\alpha)
=\sum_h K(h/H)e^{-2\pi i h\alpha},
\tag{12}
\]

ordinary Fourier orthogonality gives the exact identity

\[
\boxed{
Q_{K,H}(f)
=
\int_0^1 |F(\alpha)|^2\Theta_{K,H}(\alpha)\,d\alpha.
}
\tag{13}
\]

No zeta continuation, Hardy--Littlewood conjecture, or limiting argument enters (13). The weighted lag statistic is intrinsically quadratic on the additive Fourier side.

For real `f`, `C_f(-h)=C_f(h)`. Since `K_eta(0)=0`, the one-sided cubic statistic is exactly half of (11):

\[
\sum_{d\ge1}w_\eta^{[2]}(d/H)C_f(d)
=\frac12 Q_{K_\eta,H}(f).
\tag{14}
\]

This places the arithmetic source requested by `PL-405` in an additive quadratic spectrum even though its model source was discovered through Ramanujan harmonics.

## 3. Exact triangular / short-interval-moment representation

Assume now that `K` is even, `C^2` on `[0,infinity)`, and that `K(t),K'(t)->0` as `t->infinity`. For `x>=0`, twice integrating from infinity gives

\[
K(x)=\int_x^\infty (t-x)K''(t)\,dt.
\tag{15}
\]

Define the triangular correlation functional

\[
T_f(L)
:=\sum_{h\in\mathbb Z}(L-|h|)_+C_f(h).
\tag{16}
\]

Substituting (15) into (11) and interchanging the finite correlation sum with the integral yields

\[
\boxed{
Q_{K,H}(f)
=\frac1H\int_0^\infty K''(t)T_f(Ht)\,dt.
}
\tag{17}
\]

For integer `L`, (16) is exactly a moving-window second moment:

\[
T_f(L)
=\sum_{x\in\mathbb Z}
\left|\sum_{j=1}^{L}f(x+j)\right|^2.
\tag{18}
\]

The kernel `K_eta` in (3) satisfies the hypotheses of (15)--(17): it is sufficiently smooth at zero because of the fourth-order vanishing in (2), and it decays exponentially at infinity.

Equations (17)--(18) are the precise bridge to the classical short-interval variance literature. For a centered prime sequence, the triangular quantities are Selberg-type variances. Goldston--Montgomery and later quantitative refinements relate asymptotics of such prime variances, under RH and suitable uniformity, to pair-correlation asymptotics for the nontrivial zeta zeros. Languasco--Perelli--Zaccagnini make the transfer between quantitative error terms explicit.

The conclusion must be kept at the right strength: **one fixed cubic kernel is not equivalent to the full strong pair-correlation conjecture**. Equation (17) only proves that it is a signed test functional of the same family of prime variances. Recovering an entire variance function from one such test would require additional information not supplied here.

## 4. The modified Mangoldt factor is not the precision bottleneck

The source in `PL-405` uses

\[
\Lambda_1(n)=\frac{\phi(n)}n\Lambda(n).
\tag{19}
\]

The strongest modern averaged prime-pair theorems are normally stated for `Lambda`, but passing from `Lambda` to `Lambda_1` is quantitatively cheap at the level relevant here.

Since both functions are supported on prime powers,

\[
D(n):=\Lambda(n)-\Lambda_1(n)
\]

satisfies exactly

\[
D(p^k)=\frac{\log p}{p}.
\tag{20}
\]

Hence, for `Y>=3`,

\[
\sum_{n\le Y}D(n)
\le
\log Y\sum_{p\le Y}\frac1p
=O(\log Y\log\log Y).
\tag{21}
\]

Uniformly for `1<=h<=X`, using `Lambda(n),Lambda_1(n)<=log(2X)` on the relevant range,

\[
\sum_{n\le X}
\left|
\Lambda_1(n)\Lambda_1(n+h)
-
\Lambda(n)\Lambda(n+h)
\right|
=
O(\log^2X\log\log X).
\tag{22}
\]

Therefore a bounded `H`-scale lag weight contributes only

\[
O\!\left(\frac{\log^2X\log\log X}{X}\right)
\tag{23}
\]

after the `1/(XH)` normalization of the `PL-405` target. In particular, if

\[
H=o\!\left(
\frac{X^{4/7}}{(\log X)^{8/7}(\log\log X)^{4/7}}
\right),
\tag{24}
\]

then (23) is `o(H^-7/4)`.

Thus there is a substantial polynomial window — including choices `H=X^theta` with `theta<4/7` — in which replacing `Lambda_1` by the ordinary von Mangoldt function costs less than the zero-sensitive scale. The hard issue is not the harmless factor `phi(n)/n`; it is the precision of the off-diagonal prime-pair statistic itself.

## 5. Current averaged Hardy--Littlewood theorems are far above the required layer

Matomäki--Radziwill--Tao prove that

\[
\sum_{X<n\le2X}\Lambda(n)\Lambda(n+h)
\]

has the expected Hardy--Littlewood asymptotic for almost all `|h|<=H` when

\[
X^{8/33+\varepsilon}\le H\le X^{1-\varepsilon},
\tag{25}
\]

with an error saving **on average an arbitrary fixed power of `log X`** over the trivial bound.

The 2026 theorem of Matomäki--Radziwill--Shao--Tao--Teräväinen reaches all fixed `ell`-point prime correlations with one averaging variable. For `ell=2`, it gives

\[
\sum_{n\le X}\Lambda(n)\Lambda(n+h)
=(1+o(1))\mathfrak S(h)X
\tag{26}
\]

for a proportion `1-o(1)` of `1<=h<=H` whenever

\[
X^{1/3+\varepsilon}\le H\le X^{1-\varepsilon}.
\tag{27}
\]

Its underlying short-interval uniformity estimates also furnish arbitrary fixed logarithmic savings against the structured prime approximant in their stated range, but the correlation theorem (26) is qualitative at the final almost-all-shift level.

By contrast, write

\[
E_X(h)
:=\sum_{n\le X}\Lambda(n)\Lambda(n+h)-X\mathfrak S(h).
\tag{28}
\]

For a bounded cubic weight, preserving the normalized `PL-404` remainder requires

\[
\frac1{XH}\sum_{h\ge1}w_\eta^{[2]}(h/H)E_X(h)
=o(H^{-7/4}),
\tag{29}
\]

or equivalently

\[
\sum_{h\ge1}w_\eta^{[2]}(h/H)E_X(h)
=o(XH^{-3/4}).
\tag{30}
\]

An average absolute-error estimate of the form

\[
\sum_{h\le H}|E_X(h)|
\ll_A XH(\log X)^{-A}
\tag{31}
\]

would normalize only to `O_A((log X)^-A)`. In every polynomial regime `H=X^theta` with fixed `theta>0`,

\[
\frac{(\log X)^{-A}}{H^{-7/4}}
=
\frac{H^{7/4}}{(\log X)^A}
\longrightarrow\infty
\tag{32}
\]

for each fixed `A`. Thus even arbitrarily high **fixed** logarithmic savings do not reach the source precision required by `PL-404`.

One must not let `A=A(X)` in such theorems: their constants and exceptional-set bounds are asserted for each fixed `A`, not uniformly for a growing parameter. Nor can one evade (32) by taking `X` super-exponential in `H` while invoking (25) or (27), because those theorems themselves impose a positive-power lower bound on `H` in terms of `X`.

## 6. Matched control: the singular series is accessible before the zero-sensitive residual is

The 2026 short-interval uniformity theory separates the primes into a structured approximant `Lambda^sharp` and a uniform residual. In the proof of its Hardy--Littlewood application, the structured/sieve component recovers the usual singular series for almost all shifts, while the residual is controlled through Gowers/nilsequence estimates.

This is a particularly apt control for `PL-404`--`PL-405`. It shows that modern unconditional machinery can already recover the same local-density main term whose Mellin continuation carries the model zero layer. What it does **not** provide is a power-small signed error on the scale (29).

The gap is therefore not “derive the singular series somehow.” The singular series is already the established main term in strong averaged prime-correlation theorems. The missing step is to retain a much finer **signed quadratic residual** after that main term has been removed.

## 7. Prior-art and novelty audit

The quadratic Fourier identity (13), the triangular identity (17)--(18), and the connection between prime short-interval variances and zero pair correlation are classical harmonic/analytic-number-theory structures. **No novelty is claimed for them.** The line-specific result is the exact placement of the `PL-405` cubic source test inside that structure and the quantitative comparison with the `H^-7/4` layer already forced by `PL-404`.

Primary/current anchors checked in this audit are:

- **Kaisa Matomäki, Maksym Radziwill, Terence Tao**, “Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges,” *Proceedings of the London Mathematical Society* **118** (2019), 284--350, arXiv:1707.01315, https://arxiv.org/abs/1707.01315 . This is the prime-pair almost-all-shift theorem with the range (25) and arbitrary fixed logarithmic saving on average.
- **Kaisa Matomäki, Maksym Radziwill, Xuancheng Shao, Terence Tao, Joni Teräväinen**, “Higher uniformity of arithmetic functions in short intervals II. Almost all intervals,” *Inventiones Mathematicae* **244** (2026), 967--1091, DOI https://doi.org/10.1007/s00222-026-01408-6 , arXiv:2411.05770. Theorem 1.5 gives (26)--(27); the paper's structured approximants and Gowers-uniform residual provide the matched control in Section 6.
- **Alessandro Languasco, Alberto Perelli, Alessandro Zaccagnini**, “Explicit relations between pair correlation of zeros and primes in short intervals,” *Journal of Mathematical Analysis and Applications* **394** (2012), 761--771, DOI https://doi.org/10.1016/j.jmaa.2012.04.058 . This gives quantitative forms of the Goldston--Montgomery transfer between prime short-interval mean squares and zeta-zero pair correlation.

Targeted local searches found no existing `PL-*` finding that makes this source-test / prime-variance identification or the `H^-7/4` versus logarithmic-saving comparison. The general identities and pair-correlation correspondence are prior art; the present finding is therefore classified as a **prior-art redirect plus line-specific quantitative obstruction**, not as a new general theorem in prime correlations.

## 8. Boundary and falsification audit

- **The diagonal cancellation is exact but not a `B^2` convergence theorem.** `K_eta(0)=0` removes the divergent zero-lag term from the tested functional. It does not prove that `L_delta` converges to `Lambda_1` in a topology strong enough to exchange `delta->0`, `X->infinity`, and `H->infinity`.
- **One cubic test does not imply full zero pair correlation.** The signed representation (17) places the statistic in the variance sector but does not invert that sector from one kernel.
- **Almost-all-shift theorems may discard useful sign cancellation.** Bounds such as (31) take absolute values. The special oscillation `sin(pi u^3/6)` could in principle yield a much stronger aggregate estimate than any pointwise or absolute-average theorem. No obstruction to such a special estimate is proved here.
- **The recent Hardy--Littlewood theorem is for `Lambda`.** Section 4 shows that `Lambda_1` versus `Lambda` is negligible below the critical source scale in the nonempty polynomial range (24), but a proposed theorem outside that range must redo this check.
- **Window boundaries need to be declared.** Identities (13)--(18) are exact for a finitely supported sequence. Applying them to prime data with a sharp interval requires the usual endpoint bookkeeping, or more cleanly a smooth `n/X` cutoff. No boundary term is being hidden inside an RH claim.
- **The precision comparison is a theorem-capability statement, not a lower bound on the true error.** Equation (32) says the published logarithmic estimates cannot certify (29) in their polynomial ranges. It does not assert that the actual cubic-weighted error is of logarithmic size.

## Consequence for the line

`PL-405` left the arithmetic bridge as a joint critical-endpoint covariance problem. The cubic source itself now sharpens that diagnosis in two ways.

First, its fourth-order zero projects out the only explicit infinite-energy diagonal, so the final observable does not need to carry the `1/(2delta)` Ramanujan energy blow-up. Second, the remaining off-diagonal test has an exact additive quadratic / short-interval-variance representation. That representation connects the source-replacement problem to a classical zero-sensitive sector where the relevant arithmetic input is known to be much finer than ordinary first-order prime distribution.

The next useful attack should therefore not be another generic `B^2` endpoint argument or another generic almost-all-shift Hardy--Littlewood estimate. It should use the **specific signed cubic kernel** in (13) or (17), and ask whether explicit-formula / pair-correlation analysis can evaluate that one test with error `o(H^-7/4)` after the singular-series main layers are subtracted. A proof at that precision would be genuinely aligned with the zero layer already isolated in `PL-404`; a merely logarithmic source-replacement theorem would not.