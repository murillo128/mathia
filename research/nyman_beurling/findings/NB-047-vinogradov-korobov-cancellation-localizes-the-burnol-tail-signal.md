# NB-047 — Vinogradov--Korobov cancellation localizes the Burnol tail signal at a doubly logarithmic scale

**Status:** `EXACT-DERIVED + VINOGRADOV-KOROBOV-TRANSFER + SUBEXPONENTIAL-DUAL-NORM + DOUBLE-LOG-CUTOFF-LOCALIZATION + BURNOL-SCALE-POSITIVE-WITNESS + LOGARITHMIC-OCCUPATION + ORACLE-BOUNDARY-REFINEMENT`. `NB-041` constructs the logarithmic tail dual `Omega_M` and proves the coarse unconditional estimate `||Omega_M|| << 1/log M`. `NB-046` consequently localizes the Burnol-scale directional mass below every predeclared cutoff with `log M_N / sqrt(log N) -> infinity`. The exact shell formula of `NB-041` in fact transfers the classical Vinogradov--Korobov cancellation of the Mertens function to the same dual without polynomializing it.

Put
\[
V(x):=(\log x)^{3/5}(\log\log x)^{-1/5}
\qquad(x\ge e^e).
\tag{1}
\]
Then there are absolute constants `c,C>0` such that
\[
\boxed{
\|\Omega_M\|\le C\exp(-cV(M))
}
\qquad(M\to\infty).
\tag{2}
\]
Consequently, if `M_N<=N`, `M_N->infinity`, and
\[
\boxed{
\frac{V(M_N)}{\log\log N}\longrightarrow\infty,
}
\tag{3}
\]
then the prefix mass from `NB-046`,
\[
S_{M,N}:=
\sum_{L=1}^{M-1}
\log\frac{L+1}{L}\,D_{L,N},
\qquad
D_{L,N}:=
 m(L)-\sum_{n=L+1}^{N}\frac{a_{N,n}}n,
\tag{4}
\]
satisfies
\[
\boxed{
S_{M_N,N}=(1+o(1))d_N^2.
}
\tag{5}
\]
A simple concrete choice is
\[
\boxed{
M_N=
\left\lceil
\exp\big((\log\log N)^{5/3+\varepsilon}\big)
\right\rceil,
\qquad \varepsilon>0,
}
\tag{6}
\]
for which `M_N=N^{o(1)}` and (3) holds. Thus the `exp(omega(sqrt(log N)))` localization threshold of `NB-046` is not intrinsic to the directional family: it came from deliberately using only the coarse `O(1/log M)` form of the unconditional Möbius estimate.

## 1. Vinogradov--Korobov cancellation transfers to `m` and `Theta`

Write
\[
\mathcal M(x):=\sum_{n\le x}\mu(n).
\tag{7}
\]
The classical Vinogradov--Korobov zero-free region gives
\[
\mathcal M(x)
\ll
x\exp(-c_0V(x))
\tag{8}
\]
for some absolute `c_0>0`; Lee and Leong give explicit versions of this asymptotic shape. This input is unconditional and substantially weaker than every fixed power saving `M(x)=O(x^{1-\delta})`.

Recall the two arithmetic functions already used in `NB-041`,
\[
m(x)=\sum_{n\le x}\frac{\mu(n)}n,
\qquad
\Theta(x)=1-
\sum_{n\le x}\frac{\mu(n)}n\log\frac xn.
\tag{9}
\]
Partial summation and the PNT consequence `sum mu(n)/n=0` give
\[
m(x)
=
\frac{\mathcal M(x)}x
-
\int_x^\infty\frac{\mathcal M(t)}{t^2}\,dt.
\tag{10}
\]
With `u=log t`, the integral in (10) is bounded by
\[
\int_{\log x}^{\infty}
\exp\!\left(
-c_0u^{3/5}(\log u)^{-1/5}
\right)du.
\tag{11}
\]
The usual tail estimate for this stretched exponential contributes only a polynomial factor in `log x`, which is absorbed after decreasing the exponent constant. Hence, for some `c_1>0`,
\[
\boxed{
|m(x)|\ll\exp(-c_1V(x)).
}
\tag{12}
\]

`NB-041` proves the exact continuous relation
\[
\Theta(x)-\Theta(y)
=-\int_y^x m(u)\,\frac{du}{u}.
\tag{13}
\]
Since `Theta(x)->0`, letting the upper endpoint tend to infinity gives
\[
\Theta(x)=\int_x^\infty m(u)\,\frac{du}{u}.
\tag{14}
\]
A second application of the same stretched-exponential tail estimate therefore yields, after another harmless decrease of the constant,
\[
\boxed{
|\Theta(x)|\ll\exp(-c_2V(x)).
}
\tag{15}
\]
No Nyman approximation hypothesis enters (8)--(15).

## 2. The exact shell formula gives a subexponential dual norm

For
\[
I_t=\left(\frac1{t+1},\frac1t\right],
\tag{16}
\]
`NB-041` gives the exact shell value
\[
\Omega_M|_{I_t}
=
\Theta(M/t)
+t\left[
\Theta(M/t)-\Theta(M/(t+1))
\right]
\qquad(1\le t<M),
\tag{17}
\]
and `Omega_M=1` on `(0,1/M]`. Using (13), for `t<=sqrt(M)` one obtains
\[
\begin{aligned}
|\Omega_M|_{I_t}|
&\le
|\Theta(M/t)|
+t\int_{M/(t+1)}^{M/t}|m(u)|\,\frac{du}{u}\\
&\ll
\exp(-c_3V(M)),
\end{aligned}
\tag{18}
\]
where `t log((t+1)/t)<=1` and `V(M/(t+1))` is a fixed positive multiple of `V(M)` uniformly in this range, after adjusting `c_3`.

The global shell bound from `NB-041` remains available for the complementary range. Since `|I_t|=1/(t(t+1))`, splitting at `sqrt(M)` gives
\[
\begin{aligned}
\|\Omega_M\|^2
&\ll
\exp(-2c_3V(M))
\sum_{t\le\sqrt M}\frac1{t(t+1)}
+
\sum_{\sqrt M<t<M}\frac1{t(t+1)}
+
\frac1M\\
&\ll
\exp(-2c_3V(M))+M^{-1/2}.
\end{aligned}
\tag{19}
\]
Because `V(M)=o(log M)`, the polynomial remainder is eventually smaller than the stretched-exponential term. Taking square roots proves (2), possibly with a smaller positive `c`.

The same argument strengthens the scalar lock of `NB-041`. For the optimal residual `r_N` and logarithmic coefficient coordinate `sigma_{M,N}`,
\[
\Theta(M)-\sigma_{M,N}
=\langle r_N,\Omega_M\rangle,
\tag{20}
\]
so uniformly for `N>=M`,
\[
\boxed{
\sigma_{M,N}
=
\Theta(M)
+O\!\left(d_Ne^{-cV(M)}\right),
\qquad
\sup_{N\ge M}|\sigma_{M,N}|
\ll e^{-cV(M)}.
}
\tag{21}
\]
The exact support lower bound `||Omega_M||>=M^{-1/2}` from `NB-041` is untouched.

## 3. Burnol localization moves from `sqrt(log N)` to `log log N`

For the canonical best residual, `NB-046` proves the exact partial-flow identity
\[
S_{M,N}=d_N^2-\langle r_N,\Omega_M\rangle.
\tag{22}
\]
Combining (2) with Cauchy--Schwarz gives
\[
\frac{|S_{M,N}-d_N^2|}{d_N^2}
\ll
\frac{e^{-cV(M)}}{d_N}.
\tag{23}
\]
Burnol's unconditional bound
\[
\liminf_{N\to\infty}d_N^2\log N
\ge\mathfrak B_\zeta>0
\tag{24}
\]
therefore yields
\[
\frac{|S_{M,N}-d_N^2|}{d_N^2}
\ll
\sqrt{\log N}\,e^{-cV(M)}.
\tag{25}
\]
Condition (3) makes the right side tend to zero and proves (5).

For the concrete choice (6),
\[
V(M_N)
\asymp
\frac{(\log\log N)^{1+3\varepsilon/5}}
     {(\log\log\log N)^{1/5}},
\tag{26}
\]
so (3) follows. This cutoff is much smaller than every `exp((log N)^delta)` with fixed `delta>0`, while still diverging faster than any fixed power of `log N`.

The positive-witness consequence of `NB-046` therefore localizes to the same window:
\[
\boxed{
\liminf_{N\to\infty}
(\log N)(\log M_N)
\max_{1\le L<M_N}D_{L,N}
\ge\mathfrak B_\zeta.
}
\tag{27}
\]
For (6),
\[
\boxed{
\liminf_{N\to\infty}
(\log N)(\log\log N)^{5/3+\varepsilon}
\max_{1\le L<M_N}D_{L,N}
\ge\mathfrak B_\zeta.
}
\tag{28}
\]
Thus the forced positive discrepancy is simultaneously larger and confined to a dramatically smaller predeclared cutoff window than in the concrete `NB-046` corollary.

The logarithmic occupation statement also transfers unchanged in strength. If
\[
A_{M,N}=S_{M,N}/\log M,
\qquad
\mathcal G_{M,N}
=
\{L<M:D_{L,N}\ge A_{M,N}/2\},
\tag{29}
\]
then the uniform selector bound `|D_{L,N}|<=C_*d_N` from `NB-035` gives
\[
\sum_{L\in\mathcal G_{M,N}}
\log\frac{L+1}{L}
\ge
\frac{S_{M,N}}{2C_*d_N}.
\tag{30}
\]
Hence every sequence satisfying (3) obeys
\[
\boxed{
\liminf_{N\to\infty}
\sqrt{\log N}
\sum_{L\in\mathcal G_{M_N,N}}
\log\frac{L+1}{L}
\ge
\frac{\sqrt{\mathfrak B_\zeta}}{2C_*}.
}
\tag{31}
\]
The same positive logarithmic mass from `NB-045`--`NB-046` is therefore forced entirely below the doubly logarithmic stretched-exponential cutoff (6).

## 4. Adversarial checks and boundary

The improvement is **not** a polynomial norm estimate. For every fixed `alpha>0`,
\[
e^{-cV(M)}=M^{-o(1)}\gg M^{-\alpha}
\tag{32}
\]
as `M->infinity`. Thus (2) is fully consistent with `NB-043`--`NB-044`, which show that any fixed power decay of `||Omega_M||` already encodes a fixed zero-free strip and that the optimal power exponent is exactly `1-Theta_zeta`. This finding uses only the classical unconditional zero-free-region scale already known for zeta; it does not sneak in an RH-strength estimate.

Condition (3) is sufficient, not claimed necessary. The constant in (2) can be made effective using an explicit Vinogradov--Korobov Mertens bound, which would replace (3) by a constant-sensitive threshold. The constant-free formulation deliberately asks `V(M_N)` to dominate `log log N`, so it survives any positive exponent constant.

Nothing here computes the winning cutoff `L` from source data alone. Each `D_{L,N}` still contains the optimal coefficient tail. The theorem localizes where a positive source-selected directional signal **must exist**; it does not turn that signal into a projector-free algorithm, prove `d_N->0`, or resolve the accepted weighted-skeleton oracle clue. Likewise, (21) predicts the scalar logarithmic coordinate more sharply but does not compute the geometric repair line `P_W e`.

The square-root-log boundary in `NB-046` should therefore be read as a boundary of its coarse `O(1/log M)` estimate, not as a structural lower bound on localization. A genuinely new barrier would have to concern source access to one of the localized discrepancies, a directional estimate beyond Cauchy--Schwarz, or the projected repair geometry itself.

## 5. Prior art and research consequence

The load-bearing external input is classical. Ethan S. Lee and Nicol Leong, *New explicit bounds for Mertens function and the reciprocal of the Riemann zeta-function* ([arXiv:2208.06141](https://arxiv.org/abs/2208.06141)), give explicit bounds of the Vinogradov--Korobov form (8). The exponent shape and its zero-free-region provenance are prior art; no novelty is claimed for (8), for partial summation from `M(x)` to reciprocal-Möbius sums, or for stretched-exponential tail estimates.

A targeted audit around Nyman--Beurling zero-free-region approximation, Möbius approximants, and Burnol-scale distance bounds found the expected literature relating approximation quality to zero-free regions, including the already anchored contemporary weighted-space boundary, but no source stating the specific transfer from a Vinogradov--Korobov Mertens estimate through the `NB-041` shell selector to (2), nor the resulting cutoff localization (3)--(31). Search absence is not a priority claim.

The durable program consequence is narrower and useful. `NB-045` first showed that the complete step-tail family contains the finite distance; `NB-046` showed the Burnol-scale part is already in a subpolynomial prefix; this finding pushes that prefix down to a predeclared window controlled only by `log log N`. The remaining obstacle is no longer late-cutoff hiding. It is **source access inside an extremely small directional window**: predict one useful `L`, control a sparse subfamily, or transfer its positive logarithmic occupation into the weighted-skeleton repair without reconstructing the optimal coefficients.