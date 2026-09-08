# XF-114 — Vinogradov–Korobov creates a fixed Fejer-positive q-scale arc

**Status:** `LITERATURE+DERIVED` + `EXACT-DERIVED` + `XI-SPECIFIC-FEJER-FLATNESS` + `ZERO-FREE-REGION` + `TOEPLITZ-SOURCE-GATE`. XF-113 shows that the coarse q-scale restrictions through XF-112 still permit fixed-depth Fejer wells: a bad set of vanishing angular measure can remain much wider than the finite-section resolution `1/K` and can support a negative plane-wave Rayleigh quotient. For the actual mass-preserving Xi source, however, such Fejer-visible wells cannot approach the central angle at all. A triangular explicit-formula bridge plus the Vinogradov–Korobov zero-free region gives a fixed, `a`-independent angular neighborhood on which every degree-`K` Fejer average is positive.

Keep the q-scale normalization of XF-108--XF-113,

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
a:=N\Delta\asymp q^{1/2},\qquad
\Delta\asymp a^{-3},
\tag{1}
\]

and

\[
L=\log a+c,\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,\qquad
\ell:=(K+1)\Delta=L+O(\Delta),
\tag{2}
\]

with `c` fixed. Let `\widehat\mu_m` be the mass-preserving source moments of XF-108 and

\[
F_a(\theta)
=
1+2\sum_{m=1}^K\widehat\mu_m\cos(m\theta).
\tag{3}
\]

Define its exact order-`K` Fejer mean

\[
\boxed{
\mathfrak A_a(\theta)
:=
1+
2\sum_{m=1}^K
\left(1-\frac{m}{K+1}\right)
\widehat\mu_m\cos(m\theta)
=
\int_{\mathbb T}
F_a(\phi)\Phi_K(\theta-\phi)\,dm(\phi).
}
\tag{4}
\]

Then there is a fixed `\theta_0>0`, depending only on the deposition bump and on `c`, such that

\[
\boxed{
\mathfrak A_a(\theta)
=
1+O_{\psi,c}(|\theta|)+o(1)
\qquad
(|\theta|\le\theta_0),
}
\tag{5}
\]

uniformly as `a->infinity`. Consequently one may choose a fixed `\theta_*>0` for which

\[
\boxed{
\mathfrak A_a(\theta)\ge\frac12
\qquad
(|\theta|\le\theta_*)
}
\tag{6}
\]

for all sufficiently large `a`. In particular, every sequence `\theta_a->0` satisfies

\[
\boxed{
\mathfrak A_a(\theta_a)=1+o(1).
}
\tag{7}
\]

Thus a fixed-depth negative well visible at Fejer resolution cannot be centered at any angle tending to zero. Any such surviving well must sit at a genuinely mesh-scale angle `|\theta|\gg1`; equivalently its physical wave number `y=\theta/\Delta` must be a fixed positive fraction of the Nyquist scale `\Delta^{-1}\asymp a^3\asymp q^{3/2}`. This is a Fejer-scale statement, not a proof that the full Toeplitz section is positive: a negative eigenvector need not be a single plane wave and need not arise from one interval well.

## 1. Fejer averaging is exactly a triangularly tapered Xi source test

Put

\[
\tau_\ell(\xi)
=
\left(1-\frac{\xi}{\ell}\right)_+,
\qquad
y=\frac{\theta}{\Delta}.
\tag{8}
\]

XF-052 and XF-108 give the open-positive source carrier and its mass-preserving mesh deposition,

\[
\mathcal Z_0(\xi)
=
B(\xi)
-
\frac12
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\delta\!\left(\xi-\frac{\log n}{2}\right),
\tag{9}
\]

\[
\widehat\mu_m
=
\frac{\Delta}{a}B(m\Delta)
-
\frac1{2a}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\omega_\psi\!\left(
m,\frac{\lambda_n}{\Delta}
\right),
\qquad
\lambda_n=\frac12\log n,
\tag{10}
\]

with `\sum_m\omega_\psi(m,u)=1` and one-cell support. The taper in `(4)` is the grid sample of `(8)` because

\[
1-\frac{m}{K+1}
=
\tau_\ell(m\Delta).
\tag{11}
\]

Define the canonical continuous triangular source observable

\[
\mathfrak C_a(y)
:=
1+
\frac2a
\left\langle
\mathcal Z_0,\,
\tau_\ell(\xi)\cos(y\xi)
\right\rangle_{\rm can}.
\tag{12}
\]

The subscript only recalls the canonical endpoint extension of XF-051/XF-088. The leading `Delta N/2` endpoint mass in XF-088 is exactly the separately written diagonal `1` in `(12)`; the additional logarithmic pole counterterm is only `O(log(1/Delta)/a)` after q-scale normalization. The singular remainder

\[
B(\xi)-e^\xi
=
-\frac{e^{-5\xi}}{1-e^{-4\xi}}
=
-\frac1{4\xi}+O(1)
\tag{13}
\]

has total normalized size `O(log(1/Delta)/a)=o(1)` on this taper, so it never contributes at order one.

For the regular `e^\xi` background, the weighted Riemann-sum error is controlled by total variation:

\[
\frac{\Delta}{a}
\left|
\sum_{m=1}^K
\tau_\ell(m\Delta)e^{m\Delta}\cos(m\theta)
-
\Delta^{-1}
\int_0^\ell
\tau_\ell(\xi)e^\xi\cos(y\xi)\,d\xi
\right|
\ll_c
\Delta+|\theta|.
\tag{14}
\]

Indeed the derivative cost is `O(e^\ell(1+|y|))`, and `e^\ell/a=O_c(1)` while `\Delta |y|=|\theta|`.

The prime atoms obey the same scale without any derivative of the prime measure. If `\omega_\psi(m,\lambda/\Delta)` is nonzero, then `|m\Delta-\lambda|\le\Delta`, so

\[
\left|
\sum_m
\tau_\ell(m\Delta)
\omega_\psi\!\left(m,\frac{\lambda}{\Delta}\right)
\cos(m\theta)
-
\tau_\ell(\lambda)\cos(y\lambda)
\right|
\ll_\psi
|\theta|+\frac{\Delta}{\ell}.
\tag{15}
\]

The upper endpoint causes no larger error because both the continuous taper and the last occupied grid weights are `O(Delta/ell)`. The Chebyshev mass estimate already used in XF-104/XF-109,

\[
\sum_{\lambda_n\le\ell+O(\Delta)}
\frac{\Lambda(n)}{\sqrt n}
\ll e^\ell
\asymp_c a,
\tag{16}
\]

allows `(15)` to be summed before normalization. Combining `(13)`--`(16)` gives the uniform bridge

\[
\boxed{
\mathfrak A_a(\theta)
=
\mathfrak C_a(\theta/\Delta)
+
O_{\psi,c}(|\theta|+\Delta)
+
O\!\left(\frac{\log(1/\Delta)}a\right).
}
\tag{17}
\]

The important point is that `(17)` remains useful for a **fixed small mesh angle**. The physical frequency can then be as large as `y=Theta(Delta^{-1})=Theta(a^3)`; no smooth-PNT approximation of the raw symbol is being asserted.

## 2. The triangular carrier has an absolutely convergent zero-kernel representation

XF-051 identifies `\mathcal Z_0` with the canonical positive-frequency zero field. For a nontrivial zeta zero

\[
\rho=\beta+i\gamma,
\qquad
x_\rho
=
2\gamma+i(1-2\beta),
\tag{18}
\]

the zero coordinates are symmetric under `x->-x` and conjugation. The triangular cosine transform is elementary:

\[
\boxed{
K_\ell(z)
:=
\int_0^\ell
\left(1-\frac{\xi}{\ell}\right)
\cos(z\xi)\,d\xi
=
\frac{1-\cos(\ell z)}{\ell z^2},
}
\tag{19}
\]

with the removable value `K_\ell(0)=\ell/2`.

Choose one representative from each `+-` pair of zero coordinates. The paired Hadamard expansion from XF-051 then gives

\[
\boxed{
\left\langle
\mathcal Z_0,\,
\tau_\ell(\xi)\cos(y\xi)
\right\rangle_{\rm can}
=
\sum_{x}
\left[
K_\ell(y-x)+K_\ell(y+x)
\right].
}
\tag{20}
\]

For a finite real-rooted control this is simply the identity obtained by integrating

\[
2\cos(x\xi)\cos(y\xi)
=
\cos((y-x)\xi)+\cos((y+x)\xi).
\tag{21}
\]

For the Xi field, `(20)` is also absolutely convergent after the `+-` pairing because the `1/z` terms cancel and `K_\ell(z)=O_\ell(|z|^{-2})`. This is precisely why the triangular taper is better suited to the Fejer gate than an untapered sharp source cutoff.

A convenient uniform complex bound follows directly from `(19)`. Writing `z=u+iv`,

\[
\boxed{
|K_\ell(u+iv)|
\ll
\ell\,
\frac{e^{\ell|v|}}
{1+\ell^2u^2}.
}
\tag{22}
\]

For `|u|\le1/\ell` this is the trivial integral bound; for `|u|>1/\ell` it follows from `|1-\cos(\ell z)|\ll e^{\ell|v|}`.

## 3. Vinogradov–Korobov makes the entire zero contribution `o(a)` up to physical frequency `O(a^3)`

The load-bearing arithmetic input is now a zero-free region, not merely PNT smoothing. A Vinogradov–Korobov region gives, for every sufficiently high nontrivial zero,

\[
\min\{\beta,1-\beta\}
\gg
\frac1{
(\log(2+|\gamma|))^{2/3}
(\log\log(3+|\gamma|))^{1/3}
}.
\tag{23}
\]

By `(18)` this becomes

\[
1-|\operatorname{Im}x_\rho|
=
2\min\{\beta,1-\beta\}.
\tag{24}
\]

Fix any constant `\theta_0<1`. For `|y|\le\theta_0/\Delta=O(a^3)`, split the zero sum at `|\gamma|=a^4`. For the zeros below that height, `(23)`--`(24)` imply

\[
|\operatorname{Im}x_\rho|
\le
1-d_a,
\qquad
d_a
\gg
\frac1{
(\log a)^{2/3}
(\log\log a)^{1/3}
}.
\tag{25}
\]

The finitely many low zeros are absorbed by reducing the implicit constant. The standard Riemann--von Mangoldt local count gives

\[
N(T+1)-N(T)=O(\log(2+T)).
\tag{26}
\]

Partitioning the real zero coordinate into unit intervals and using `(22)` therefore yields, uniformly for `|y|\le\theta_0/\Delta`,

\[
\frac1a
\sum_{|\gamma|\le a^4}
\left(
|K_\ell(y-x_\rho)|
+
|K_\ell(y+x_\rho)|
\right)
\ll
\ell\log a\,
\frac{e^{(1-d_a)\ell}}a.
\tag{27}
\]

Because `\ell=\log a+O(1)`,

\[
\frac{e^{(1-d_a)\ell}}a
\ll_c
e^{-d_a\ell}
\le
\exp\!\left(
-c_1
\left(
\frac{\log a}{\log\log a}
\right)^{1/3}
\right),
\tag{28}
\]

and the right-hand side of `(27)` is `o(1)`.

For `|\gamma|>a^4`, no zero-free region is needed. Since `|y|=O(a^3)`, the real separation is comparable to `|\gamma|`; the critical strip gives `|\operatorname{Im}x_\rho|<1`, and `(22)` reduces after division by `a` to the summable tail

\[
\frac1a
\sum_{|\gamma|>a^4}
\left(
|K_\ell(y-x_\rho)|
+
|K_\ell(y+x_\rho)|
\right)
\ll
\frac1\ell
\sum_{|\gamma|>a^4}
\frac1{\gamma^2}
=
o(1).
\tag{29}
\]

Here Riemann--von Mangoldt gives `\sum_{|\gamma|>R}\gamma^{-2}=O((\log R)/R)`.

Equations `(20)` and `(27)`--`(29)` prove the stronger uniform statement

\[
\boxed{
\sup_{|y|\le\theta_0/\Delta}
|\mathfrak C_a(y)-1|
=o(1).
}
\tag{30}
\]

No RH, zero-density conjecture, or real-root assumption enters. The role of the zero-free region is geometric: a zero at horizontal Xi-coordinate height `|Im x|` is amplified by at most `e^{\ell|Im x|}`, while the q-scale normalization contributes `a^{-1}\asymp e^{-\ell}`. Vinogradov–Korobov makes the remaining exponent gap `d_a\ell` diverge even when the real zero height is polynomial in `a`.

Combining `(17)` and `(30)` proves `(5)`--`(7)`.

## 4. Consequence for the XF-113 Fejer-well obstruction

XF-113 showed that if the actual source symbol contains a fixed-depth interval well

\[
F_a(\theta)\le-\eta
\qquad
(|\theta-\theta_c|\le w),
\tag{31}
\]

with fixed `\eta>0`, global `|F_a|\le M`, and `Kw->infinity`, then its plane-wave Rayleigh quotient satisfies

\[
\mathfrak A_a(\theta_c)
\le
-\eta
+
O\!\left(\frac{M+\eta}{Kw}\right)
<0
\tag{32}
\]

for all sufficiently large scales. Equation `(6)` rules this out whenever `|\theta_c|\le\theta_*`.

Therefore the matched Fejer-well counterexample of XF-113 is sharp about **where** the remaining coarse theory can fail: its wells at `+-pi/2` live in the genuinely lattice-scale angular sector that `(6)` does not touch. The actual Xi source cannot realize the same mechanism at any angle that drifts toward zero, nor anywhere in one fixed central arc. Any surviving fixed-depth, super-`1/K` well must be noncentral at order one.

In physical wave number,

\[
|\theta_c|\ge\theta_*
\quad\Longrightarrow\quad
|y_c|
=
\frac{|\theta_c|}{\Delta}
\gg
\Delta^{-1}
\asymp
a^3
\asymp
q^{3/2}.
\tag{33}
\]

Thus the next source theorem is no longer a generic high-frequency PNT refinement. It must address the **near-Nyquist arithmetic sector** where one mesh step already carries order-one phase. At that scale the mass-preserving deposition of XF-108 controls total atom mass but does not approximate the canonical continuum phase with a vanishing error. A proof of full q-scale Toeplitz positivity must either obtain an Xi-specific estimate directly in this lattice-scale sector, prove a stronger interface invariance there, or show that destination-relevant negative witnesses cannot use it.

## 5. Boundaries, stress tests, and prior-art status

The conclusion is deliberately narrower than Toeplitz PSD. Positivity of every plane-wave Fejer average in a central arc does not exclude a negative finite-section eigenvector assembled from several angular packets. Nor does `(5)` say that the raw symbol `F_a(\theta)` is pointwise close to one on a fixed arc; XF-109's raw-symbol PNT-flat window is much smaller. The smoothing in `(4)` is essential.

The fixed-angle restriction in `(5)` is also real. The grid/source bridge `(17)` loses `O(|\theta|)` because a deposited prime atom may move by one mesh cell, changing its phase by `O(|\theta|)`. Once `|\theta|` is order one, the canonical continuous explicit formula no longer controls the discrete symbol without a new arithmetic or interface theorem. This is exactly the sector left open by `(33)`.

The ingredients behind `(19)`--`(20)` are classical Fejer/triangle Fourier analysis and the Guinand--Weil explicit formula already anchored for the line. The new load-bearing external theorem is the Vinogradov--Korobov zero-free region; Mathia anchors a modern peer-reviewed explicit form in `SOURCES.md`. A directed prior-art audit also checked the Weil-positivity and compact-window literature. Those works study positivity of the full Weil quadratic form on prescribed test spaces; they do not by themselves supply the q-dependent statement `(5)` for the mass-preserving source grid with `K\asymp a^3\log a`. XF-114 therefore makes no novelty claim for the explicit formula, the triangular kernel, or the zero-free region. Its durable contribution is the scale bridge: **Fejer-visible q-source negativity is forced out of an entire fixed central mesh-angle arc and into the lattice-scale sector.**
