# XF-106 — mesh-dilute source moments force collective Toeplitz obstructions

**Status:** `EXACT-DERIVED` + `TOEPLITZ-FEASIBILITY-BOUNDARY` + `SOURCE-MESH-DILUTION` + `COLLECTIVE-OBSTRUCTION`. XF-105 showed that the fixed raw-`ell^1` realization cone reaches a deterministic wall before the full natural arithmetic scale, and identified the Toeplitz/Caratheodory gate of XF-084 as the next less-lossy test. That gate cannot fail through any bounded-order or even moderately sparse principal minor. At the source mesh used in XF-102--XF-105, every *individual* normalized moment remains only `O(a^{-1})`, even after the cumulative raw `ell^1` mass has become order one or larger.

Keep

\[
N=2q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
a:=N\Delta\asymp q^{1/2},
\tag{1}
\]

and the distribution-safe endpoint moments

\[
Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{m\Delta-\lambda_n}{\Delta}\right),
\qquad
\lambda_n=\frac12\log n,
\tag{2}
\]

for `1<=m<=K=floor(L/Delta)`, with fixed bounded `psi` supported in `[-1,1]`. If, for some fixed `eta>0`,

\[
L\le\left(\frac32-\eta\right)\log a,
\tag{3}
\]

then

\[
\boxed{
\varepsilon_a
:=
\max_{1\le m\le K}\frac{|Q_m^\psi|}{N}
\ll_{\eta,\psi}\frac1a.
}
\tag{4}
\]

In particular `(4)` holds throughout the XF-105 boundary regime `L=log a+O(1)`, including the entire natural `a^2 asymp q` arithmetic scale.

Let `T_K` be the normalized Hermitian Toeplitz matrix of XF-084,

\[
(T_K)_{ij}=\mu_{i-j},
\qquad
\mu_0=1,
\qquad
\mu_m=\frac{Q_m^\psi}{N},
\qquad
\mu_{-m}=\overline{\mu_m}.
\tag{5}
\]

For every principal submatrix `T_I`, `I subset {0,...,K}`, of order `s=|I|`,

\[
\boxed{
\lambda_{\min}(T_I)
\ge
1-(s-1)\varepsilon_a.
}
\tag{6}
\]

Consequently every family with `s=o(a)` is uniformly positive definite:

\[
\boxed{
\lambda_{\min}(T_I)=1-o(1)
\quad\text{uniformly for }|I|=o(a).
}
\tag{7}
\]

Any negative Toeplitz principal minor, or any negative quadratic-form witness supported on `s` moment coordinates, therefore requires

\[
\boxed{
s=\Omega(a)=\Omega(q^{1/2}).}
\tag{8}
\]

Thus crossing the XF-105 raw-`ell^1` wall does **not** expose a local Caratheodory failure. Any genuine weighted-measure obstruction in the source-derived prefix must be a collective correlation among a diverging number of moment coordinates.

## 1. At this mesh scale one arithmetic atom is the most a cell can see

Fix `m` and put

\[
\xi_m=m\Delta.
\]

The atomic term in `(2)` can involve `n` only if

\[
|\lambda_n-\xi_m|\le\Delta,
\]

or equivalently

\[
e^{2(\xi_m-\Delta)}
\le n\le
e^{2(\xi_m+\Delta)}.
\tag{9}
\]

The length of this interval is

\[
\begin{aligned}
e^{2\xi_m}(e^{2\Delta}-e^{-2\Delta})
&\ll
\Delta e^{2\xi_m}\\
&\le
\Delta e^{2L}.
\end{aligned}
\tag{10}
\]

From `(1)`,

\[
\Delta\asymp a^{-3}.
\tag{11}
\]

Under `(3)`, equations `(10)`--`(11)` give

\[
\Delta e^{2L}
\ll
 a^{-3}a^{3-2\eta}
=a^{-2\eta}
\longrightarrow0.
\tag{12}
\]

Therefore, for all sufficiently large scales, the interval `(9)` contains at most one integer. This is stronger than the cell-counting estimate needed in XF-105: there an individual prime-power atom could affect several neighboring mesh sites, but the converse direction is now decisive -- one mesh site cannot collect a cluster of distinct prime powers anywhere in the whole band `(3)`.

For `n>=2`, the elementary bound

\[
\frac{\Lambda(n)}{\sqrt n}
\le
\frac{\log n}{\sqrt n}
\le\frac2e
\tag{13}
\]

holds because `log x/sqrt x` is maximized at `x=e^2`. Hence the normalized atomic contribution at any one mesh site obeys

\[
\begin{aligned}
\frac1N
\left|
\frac1{2\Delta}
\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
\psi\!\left(\frac{\xi_m-\lambda_n}{\Delta}\right)
\right|
&\le
\frac{\|\psi\|_\infty}{2N\Delta}\frac2e\\
&=
O_\psi(a^{-1}),
\end{aligned}
\tag{14}
\]

because `N Delta=a`. No prime number theorem, Chebyshev estimate, zero-free region, or hypothesis on zeta zeros enters this pointwise estimate.

## 2. The archimedean background is pointwise dilute for a different reason

XF-052 gives the exact background

\[
B(\xi)
=e^\xi-
\frac{e^{-5\xi}}{1-e^{-4\xi}}.
\tag{15}
\]

For `0<xi<=1`,

\[
|B(\xi)|\ll \xi^{-1}.
\tag{16}
\]

Since the first sampled frequency is `xi=Delta`,

\[
\max_{0<\xi_m\le1}
\frac{|B(\xi_m)|}{N}
\ll
\frac1{N\Delta}
=
\frac1a.
\tag{17}
\]

For `1<=xi<=L`, equation `(15)` instead gives

\[
|B(\xi)|\ll e^\xi,
\]

so

\[
\max_{1\le\xi_m\le L}
\frac{|B(\xi_m)|}{N}
\ll
\frac{e^L}{N}
=
\frac{\Delta e^L}{a}.
\tag{18}
\]

Under `(3)` and `(11)`, the right side of `(18)` is

\[
O_\eta(a^{-5/2-\eta}),
\tag{19}
\]

which is much smaller than `a^{-1}`. Combining `(14)`, `(17)`, and `(19)` proves `(4)`.

This explains the apparent tension with XF-105. Its raw `ell^1` wall is produced by summing an enormous number of tiny smooth-background coordinates. No single normalized coefficient approaches the unit-circle moment boundary `|mu_m|=1`; the obstruction in the sufficient `ell^1` cone is cumulative from the outset.

## 3. Every sparse Toeplitz test remains deep inside the positive cone

Let `I subset {0,...,K}` have `s` elements. Every off-diagonal entry of the principal matrix `T_I` has magnitude at most `epsilon_a`. Therefore

\[
\|T_I-I_s\|_{\rm op}
\le
\max_{i\in I}
\sum_{\substack{j\in I\\j\ne i}}
|\mu_{i-j}|
\le
(s-1)\varepsilon_a.
\tag{20}
\]

Weyl's inequality, or the same estimate applied directly to the Rayleigh quotient, yields `(6)`. In particular, if `s=o(a)`, then `(4)` and `(20)` give `(7)` uniformly over **all** choices of the principal coordinates, not just consecutive minors.

Equivalently, let

\[
p(z)=\sum_{j=0}^{K}c_jz^j
\tag{21}
\]

have `s` nonzero coefficients. The Toeplitz moment quadratic form is

\[
c^*T_Kc.
\]

Writing `I=supp(c)`, equation `(6)` gives

\[
\boxed{
c^*T_Kc
\ge
\bigl(1-(s-1)\varepsilon_a\bigr)\|c\|_2^2.
}
\tag{22}
\]

Thus a negative Caratheodory/Toeplitz certificate cannot be encoded by a fixed-degree test, a bounded collection of separated frequencies, or even an `o(a)`-sparse polynomial. If `c^*T_Kc<0`, then necessarily

\[
(s-1)\varepsilon_a>1,
\]

which with `(4)` proves `(8)`. More generally, depressing the Rayleigh quotient by any fixed amount `delta_0>0` already requires `s=Omega_{delta_0}(a)`.

For a fixed order `s`, `(20)` also gives

\[
\det T_I=1+O_{s,\eta,\psi}(a^{-1}),
\tag{23}
\]

so all bounded-order principal minors converge to the identity determinant rather than merely remaining nonnegative.

## 4. The result persists beyond the natural q arithmetic scale

The natural interface in XF-104--XF-105 takes

\[
L=\log a+O(1),
\]

so the fully included arithmetic cutoff is

\[
X=e^{2L+O(\Delta)}\asymp a^2\asymp q.
\tag{24}
\]

Equation `(4)` is therefore uniform across every fixed multiplicative fraction or fixed multiplicative enlargement of the `q` scale. The stronger hypothesis `(3)` actually allows

\[
X\le a^{3-2\eta},
\tag{25}
\]

while retaining the same `O(a^{-1})` coordinate bound. This extension does **not** restore the XF-104 collision-crystal construction outside its fixed-margin realization cone; it concerns only the first Toeplitz/weighted-measure feasibility gate. It shows that local positivity remains insensitive well after coefficientwise `ell^1` control has ceased to be useful.

The scale `3/2 log a` has a transparent source meaning rather than a claimed sharp phase transition. It is where a width-`Delta` frequency cell first becomes wide enough in the integer variable `n` to contain order-one multiple integers because `Delta e^{2L}` ceases to vanish. Above that scale, `(14)` needs a genuine short-interval estimate for the von Mangoldt mass instead of the one-atom argument.

## 5. Stress tests and evidence boundary

The compact support of `psi` at one mesh width is load-bearing for the one-atom estimate. A smoothing kernel whose physical support grows with the scale can combine many prime powers in one coordinate and need not obey `(14)`. For every fixed bounded bump supported in `[-1,1]`, however, its sign is irrelevant; only `||psi||_infty` enters.

The finding proves no global Toeplitz PSD statement. The full matrix has dimension

\[
K+1\asymp \frac{L}{\Delta}\asymp a^3\log a,
\tag{26}
\]

so the lower bound `Omega(a)` in `(8)` still leaves a huge range of collective witnesses. Correlations among many tiny coefficients can make a Toeplitz matrix indefinite even when every small principal section is close to identity. The theorem therefore does **not** establish a weighted representing measure, an equal-weight real-divisor carrier, or transition nonidentifiability beyond the XF-104 cone.

Conversely, failure of the raw `ell^1` condition in XF-105 is not evidence of Toeplitz indefiniteness. Equations `(4)`--`(8)` quantify that distinction: the Gershgorin cone fails because it sums all moment magnitudes globally, while every `o(a)`-coordinate PSD test still has asymptotic margin one.

No assumption on RH is used. The prime input in `(14)` is only `Lambda(n)<=log n` plus the source mesh geometry, and the archimedean input is the exact XF-052 formula.

## 6. Prior art and consequence for the live frontier

The Gram/Toeplitz moment criterion and Caratheodory--Fejer theory used to interpret `(5)` are classical and already anchored by XF-084. The matrix estimate `(20)` is elementary Gershgorin/Rayleigh control. A targeted search also found recent Toeplitz/RH constructions -- notably Alain Connes and Walter D. van Suijlekom, **Quadratic Forms, Real Zeros and Echoes of the Spectral Action**, *Communications in Mathematical Physics* 406 (2025), article 312, DOI `10.1007/s00220-025-05493-1`, and Wojciech Michalowski, **An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients**, arXiv:2607.16795 (2026) -- but these concern different Toeplitz objects and directions of implication. No source located the mesh-scale estimate `(4)` or the `Omega(a)` witness threshold for the Guinand--Weil/Vieta moment vector `(2)`. No novelty is claimed for Gershgorin, Caratheodory--Fejer, the explicit formula, or the scalar bound `log n/sqrt n<=2/e`; no new external theorem is load-bearing, so `SOURCES.md` needs no change.

The durable line-specific conclusion is narrower and useful. XF-105 correctly redirects the source-interface problem from raw `ell^1` control to Toeplitz feasibility, but **that next gate is necessarily collective**. At `L=log a+O(1)`, no finite list of moments and no `o(q^{1/2})`-sparse Toeplitz test can produce a real-divisor obstruction. Any successful negative certificate must coordinate at least `Omega(q^{1/2})` moment indices, while any positive construction must control comparably global signed correlations rather than merely sharpen coefficientwise bounds.

This does not advance the separate positive-`Lambda` coercivity gate. It sharpens the source-side task: the next informative Toeplitz analysis should study genuinely high-dimensional quadratic forms or a continuum limit of `(5)`, not search for a small principal minor hidden just beyond the XF-105 one-quarter `ell^1` ceiling.