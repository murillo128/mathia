# XF-115 — cardinal alias decomposition flattens the full q-scale Fejer circle

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `XI-SPECIFIC-FEJER-FLATNESS` + `CARDINAL-ALIASING` + `TOEPLITZ-SOURCE-GATE`. XF-114 shows that the actual mass-preserving Xi source has positive order-`K` Fejer averages on one fixed central mesh-angle arc, but its source-to-grid comparison loses `O(|theta|)` because each prime atom is compared with its undiscretized phase separately. That loss is not intrinsic. The normalized deposition of XF-108 is a translation-invariant cardinal kernel, so Poisson summation decomposes the complete discrete response into rapidly decaying aliases of the **continuous** Xi source transform. Vinogradov--Korobov controls every polynomial-frequency alias, while smoothness of the deposition kernel kills the remaining aliases. Consequently the entire q-scale Fejer circle is asymptotically flat:

\[
\boxed{
\sup_{\theta\in[-\pi,\pi]}
\left|\mathfrak A_a(\theta)-1\right|
\longrightarrow0.
}
\tag{1}
\]

Here the normalization is that of XF-108--XF-114,

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
a:=N\Delta\asymp q^{1/2},\qquad
\Delta\asymp a^{-3},
\tag{2}
\]

\[
L=\log a+c,\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad
\ell=(K+1)\Delta=L+O(\Delta),
\tag{3}
\]

and

\[
\mathfrak A_a(\theta)
=
1+2\sum_{m=1}^K
\left(1-\frac{m}{K+1}\right)
\widehat\mu_m\cos(m\theta).
\tag{4}
\]

Thus the fixed-depth Fejer-well mechanism constructed in XF-113 cannot occur for the actual mass-preserving Xi source **at any mesh angle**, including the near-Nyquist sector left open by XF-114. This still does not prove that the full Toeplitz section is positive: a negative eigenvector need not be a plane wave and its Fourier mass may be a genuinely non-Fejer, multi-packet concentration.

## 1. The XF-108 deposition is secretly one cardinal translate

XF-108 fixes a nonnegative `psi in C_c^infinity([-1,1])`, positive on `[-1/2,1/2]`, and defines

\[
p_\psi(u)=\sum_{j\in\mathbf Z}\psi(j-u),
\qquad
\omega_\psi(m,u)=\frac{\psi(m-u)}{p_\psi(u)}.
\tag{5}
\]

For `x=m-u`, translation of the integer index gives

\[
p_\psi(u)
=
\sum_{k\in\mathbf Z}\psi(k+x).
\tag{6}
\]

Therefore, defining

\[
P_\psi(x)=\sum_{k\in\mathbf Z}\psi(k+x),
\qquad
\varphi_\psi(x)=\frac{\psi(x)}{P_\psi(x)},
\tag{7}
\]

one has the exact identity

\[
\boxed{
\omega_\psi(m,u)=\varphi_\psi(m-u).
}
\tag{8}
\]

The denominator is positive, smooth, and `1`-periodic. Hence

\[
\varphi_\psi\in C_c^\infty([-1,1]),
\qquad
\sum_{m\in\mathbf Z}\varphi_\psi(m-u)=1.
\tag{9}
\]

In particular `\int_R \varphi_\psi=1`, and its Fourier transform

\[
\widehat\varphi_\psi(s)
=
\int_{\mathbf R}\varphi_\psi(x)e^{-isx}\,dx
\tag{10}
\]

is Schwartz. This translation invariance is stronger than the one-cell localization used in XF-114: the mesh phase is not an arbitrary error at each atom but a coherent cardinal sampling operator.

## 2. Replace the archimedean sample by the same deposition operator

Separate the regular logarithmic source measure

\[
dS(\xi)
=
e^\xi\,d\xi
-
\frac12\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\delta_{\lambda_n},
\qquad
\lambda_n=\frac12\log n.
\tag{11}
\]

Its deposited coefficients are

\[
\nu_m
=
\frac1a
\int_0^\infty
\varphi_\psi\!\left(m-\frac{\xi}{\Delta}\right)
\,dS(\xi).
\tag{12}
\]

The prime part of `(12)` is **exactly** the prime part of the mass-preserving `\widehat\mu_m` from XF-108. For the regular background, compact support and `\int\varphi_\psi=1` give

\[
\frac1a\int e^\xi
\varphi_\psi\!\left(m-\frac{\xi}{\Delta}\right)d\xi
=
\frac{\Delta}{a}e^{m\Delta}
+O_\psi\!\left(
\frac{\Delta^2}{a}e^{(m+1)\Delta}
\right).
\tag{13}
\]

Summing `(13)` through `m<=K` costs `O_c(Delta)`. The difference between `B(\xi)` and `e^\xi`,

\[
B(\xi)-e^\xi
=-\frac{e^{-5\xi}}{1-e^{-4\xi}}
=-\frac1{4\xi}+O(1),
\tag{14}
\]

costs only

\[
O\!\left(\frac{\log(1/\Delta)}a\right)
=o(1)
\tag{15}
\]

in coefficient `ell^1`, exactly as in XF-114. Thus

\[
\boxed{
\sum_{m=1}^K|\widehat\mu_m-\nu_m|
\ll_{\psi,c}
\Delta+
\frac{\log(1/\Delta)}a
=o(1).
}
\tag{16}
\]

This estimate is uniform in every later phase test, so no `O(|theta|)` loss is needed.

## 3. The tapered grid response has an exact Poisson alias decomposition

Let

\[
\tau_\ell(\xi)=\left(1-\frac{\xi}{\ell}\right)_+.
\tag{17}
\]

If `\varphi_\psi(m-\xi/\Delta)` is nonzero, then `|m\Delta-\xi|<=\Delta`. Hence

\[
|\tau_\ell(m\Delta)-\tau_\ell(\xi)|
\le\frac{\Delta}{\ell}.
\tag{18}
\]

Chebyshev's estimate and `e^\ell\asymp_c a` give total variation

\[
|S|([0,\ell+O(\Delta)])=O_c(a).
\tag{19}
\]

Thus replacing the grid taper by the continuous taper in the deposited source costs only `O(Delta/ell)`. Extending the resulting integer sum to all `m in Z` adds only the `m=0` regular-background sliver of size `O(Delta/a)`; the upper endpoint `m=K+1` already has zero taper.

Define the cardinal phase response

\[
D_\theta(u)
=
\sum_{m\in\mathbf Z}
\varphi_\psi(m-u)e^{im\theta}.
\tag{20}
\]

Poisson summation applied to `x mapsto varphi_psi(x)e^{itheta x}` gives the exact identity

\[
\boxed{
D_\theta(u)
=
\sum_{k\in\mathbf Z}
\widehat\varphi_\psi(2\pi k-\theta)
\,e^{i(\theta-2\pi k)u}.
}
\tag{21}
\]

Because `\widehat\varphi_\psi` is Schwartz,

\[
\sup_{\theta\in[-\pi,\pi]}
\sum_{k\in\mathbf Z}
|\widehat\varphi_\psi(2\pi k-\theta)|
<\infty.
\tag{22}
\]

Combining `(16)`--`(22)` yields, uniformly in `theta`,

\[
\mathfrak A_a(\theta)-1
=
2\operatorname{Re}
\sum_{k\in\mathbf Z}
\widehat\varphi_\psi(2\pi k-\theta)
\,G_a\!\left(\frac{\theta-2\pi k}{\Delta}\right)
+o(1),
\tag{23}
\]

where, after the same canonical endpoint correction used in XF-114,

\[
G_a(y)
=
\frac1a
\left\langle
\mathcal Z_0,
\tau_\ell(\xi)e^{iy\xi}
\right\rangle_{\rm can}.
\tag{24}
\]

The correction from `(11)` to `(24)` is again `O(log(1/Delta)/a)` uniformly in real `y`, since the oscillatory factor has modulus one. Equation `(23)` is the decisive improvement over XF-114: an order-one mesh angle is represented by aliases of the continuous Xi field rather than by an order-one pointwise phase error.

## 4. Vinogradov--Korobov flattens every polynomial-frequency continuous alias

For every fixed `C>0`,

\[
\boxed{
\sup_{|y|\le a^C}|G_a(y)|=o(1).
}
\tag{25}
\]

This extends the cosine `C=3` estimate of XF-114 but uses exactly the same zero-free-region mechanism. The complex triangular kernel is

\[
J_\ell(z)
:=
\int_0^\ell
\left(1-\frac{\xi}{\ell}\right)e^{iz\xi}\,d\xi
=
\frac{1+i\ell z-e^{i\ell z}}{\ell z^2},
\tag{26}
\]

with removable value `J_ell(0)=ell/2`. If

\[
x_\rho=2\gamma+i(1-2\beta)
\tag{27}
\]

is the Xi zero coordinate and one representative is chosen from each `+-` pair, the paired Hadamard formula gives

\[
\left\langle
\mathcal Z_0,
\tau_\ell e^{iy\xi}
\right\rangle_{\rm can}
=
\sum_x
\left[J_\ell(y-x)+J_\ell(y+x)\right].
\tag{28}
\]

A convenient bound is

\[
|J_\ell(u+iv)|
\ll
\ell\,
\frac{e^{\ell|v|}}
{1+\ell|u|}.
\tag{29}
\]

Fix `C` and split the zero sum at `R=a^{C+2}`. For `|gamma|<=R`, the Vinogradov--Korobov zero-free region used in XF-114 gives

\[
|\operatorname{Im}x_\rho|
\le1-d_a,
\qquad
d_a
\gg_C
\frac1{(\log a)^{2/3}(\log\log a)^{1/3}}.
\tag{30}
\]

Partitioning the real zero coordinates into unit intervals and using the Riemann--von Mangoldt local count with `(29)` gives, uniformly for `|y|<=a^C`,

\[
\frac1a
\sum_{|\gamma|\le R}
\left(
|J_\ell(y-x_\rho)|+|J_\ell(y+x_\rho)|
\right)
\ll_C
(\log a)^2e^{-d_a\ell}
=o(1).
\tag{31}
\]

For the tail, pairing is essential. From `(26)`, when `|x|>2|y|+2`, the `i/z` terms cancel to first order and

\[
J_\ell(y-x)+J_\ell(y+x)
\ll
\frac{|y|}{|x|^2}
+
\frac{e^{\ell|\operatorname{Im}x|}}
{\ell|x|^2}.
\tag{32}
\]

The critical strip gives `|Im x|<1`, while Riemann--von Mangoldt gives

\[
\sum_{|\gamma|>R}\frac1{\gamma^2}
=O\!\left(\frac{\log R}{R}\right).
\tag{33}
\]

With `R=a^{C+2}` and `e^ell=O_c(a)`, equations `(32)`--`(33)` make the normalized tail `o(1)` uniformly for `|y|<=a^C`. This proves `(25)`.

Notice that the argument does not assume RH. The zero-free region controls the off-critical amplification, while pairing controls the far real tail.

## 5. Rapid alias decay closes the entire mesh-angle circle

The source measure `(11)` has normalized total variation `O_c(1)` on the tapered interval, so the endpoint-corrected transform also satisfies the crude uniform bound

\[
\sup_{y\in\mathbf R}|G_a(y)|=O_{\psi,c}(1).
\tag{34}
\]

Split the alias sum `(23)` into `|k|<=a` and `|k|>a`. For the first part,

\[
\left|
\frac{\theta-2\pi k}{\Delta}
\right|
\ll a^4
\qquad
(\theta\in[-\pi,\pi],\ |k|\le a),
\tag{35}
\]

so `(25)` with `C=4`, together with `(22)`, makes the complete finite alias block `o(1)` uniformly in `theta`.

For the tail, Schwartz decay gives for every `M>2`

\[
\sup_{\theta\in[-\pi,\pi]}
\sum_{|k|>a}
|\widehat\varphi_\psi(2\pi k-\theta)|
=O_{\psi,M}(a^{1-M}).
\tag{36}
\]

Equation `(34)` therefore makes the infinite alias tail `o(1)`. Substitution into `(23)` proves `(1)`.

The same argument works with any fixed polynomial alias cutoff `a^A`; the choice `A=1` only keeps the bookkeeping concrete.

## 6. Consequence: the XF-113 interval-well control is impossible for Xi

XF-113 constructs a matched symbol satisfying all coarse q-scale gates while retaining a negative plane-wave Rayleigh quotient. Its obstruction is exactly a fixed-depth Fejer-visible well: for a center `theta_c`, the normalized plane wave

\[
u_j^{(\theta_c)}=(K+1)^{-1/2}e^{-ij\theta_c}
\tag{37}
\]

has

\[
(u^{(\theta_c)})^*\widehat T_Ku^{(\theta_c)}
=
\mathfrak A_a(\theta_c).
\tag{38}
\]

Equation `(1)` now gives

\[
\boxed{
\inf_{\theta\in[-\pi,\pi]}
(u^{(\theta)})^*\widehat T_Ku^{(\theta)}
=1-o(1)>0.
}
\tag{39}
\]

Hence no plane-wave direction can witness q-scale nonpositivity for the actual Xi source, at central, intermediate, or Nyquist mesh angle. In particular, under the bounded-symbol hypothesis already available in the q-scale analysis, no fixed-depth interval well of width `w` with `Kw->infinity` can survive anywhere on the circle: XF-113 would turn such a well into a negative value of `(38)`, contradicting `(39)`.

This closes the specific scale mismatch exposed by XF-113. The obstruction there was not that the arithmetic source could genuinely sustain a near-Nyquist Fejer well; it was that pointwise one-cell comparison threw away the coherent alias structure of the mass-preserving deposition.

## 7. What remains open

Full Toeplitz positivity does **not** follow from `(39)`. For a general unit vector `v`,

\[
v^*\widehat T_Kv
=
\int_{\mathbb T}
F_a(\theta)|P_v(e^{i\theta})|^2\,dm(\theta),
\qquad
P_v(e^{i\theta})=\sum_{j=0}^Kv_je^{ij\theta}.
\tag{40}
\]

The Fejer family in `(38)` is only the special family generated by flat coefficient vectors with one linear phase. A negative eigenvector could use a nonuniform amplitude profile, several separated angular packets, or another degree-`K` concentration pattern whose positive density `|P_v|^2` is not a single Fejer translate. XF-110--XF-112 still require any such witness to be broad in coefficient space and to concentrate fixed Fourier mass on the rare low-symbol set.

The live source-side gate is therefore sharper than after XF-114: **any q-scale Toeplitz negativity must be genuinely non-plane-wave.** A further theorem must control the full cone of degree-`K` positive trigonometric densities, or identify an Xi-specific restriction on the subset capable of concentrating on the arithmetic low-symbol set. Merely extending the central explicit-formula arc or excluding individual negative wells is no longer the missing step.

## 8. Stress tests and prior-art boundary

The first control is the integer-phase limit. At `theta=0`, partition of unity in `(9)` gives `D_0(u)=1`; equivalently `(21)` reduces to `widehat varphi_psi(2 pi k)=0` for nonzero integers `k` and `widehat varphi_psi(0)=1`. Thus the alias formula recovers the mass-preservation mechanism of XF-108 rather than introducing a new normalization.

The second control is deposition-bump asymmetry. No symmetry of `psi` was assumed. The proof keeps the complex response `(21)` and uses the complex source transform `(24)` before taking the real part, so an asymmetric one-cell bump cannot reintroduce an order-one mesh phase.

The third control is the far-alias regime. Equation `(25)` is asserted only on polynomial physical frequencies; the proof does not silently extend Vinogradov--Korobov to arbitrary frequency. Instead `(36)` places all super-polynomial aliases under the Schwartz tail of the cardinal kernel and needs only the crude source bound `(34)` there.

Poisson aliasing for cardinal kernels, Fejer averaging, and the Guinand--Weil explicit formula are classical mechanisms. A directed prior-art search also checked Schoenberg-type cardinal interpolation and the modern Fourier-interpolation literature connecting zeta zeros and logarithmic integer frequencies, including Bondarenko--Radchenko--Seip, *Fourier Interpolation with Zeros of Zeta and L-Functions* (Constructive Approximation 57, 2023). Those works do not supply the q-dependent mass-preserving deposition theorem `(1)`. The only external theorem that is load-bearing for the new asymptotic is the Vinogradov--Korobov zero-free region already anchored in `SOURCES.md` for XF-114. No new source entry is therefore required.

The durable Mathia delta is the alias-scale conclusion, not any claim that cardinal interpolation, Poisson summation, Fejer kernels, or the explicit formula are new: **the normalized XF-108 mesh operator preserves enough coherent phase that every order-`K` plane-wave test is asymptotically blind to q-scale source negativity, uniformly across the full mesh-angle circle.**