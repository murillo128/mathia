# XF-050 — finite endpoint Volterra transport crosses complex roots and collisions

**Status:** `EXACT-DERIVED` + `CLASSICAL-EXPLICIT-FORMULA-INPUT` + `FINITE-COMPLEX-TRANSPORT` + `SOURCE-SPECIFIC-BOUNDARY`. XF-048 supplies a prime-free endpoint Fourier selector, while XF-049 derives a one-sided Volterra law for finite real-simple heat-zero systems. The remaining upper-bound question immediately exposes a domain mismatch: under a hypothetical `Lambda>0`, the endpoint `t=0` is not in the all-real regime, so a transport mechanism that intrinsically requires ordered real-simple roots cannot carry endpoint arithmetic data toward the transition.

For finite polynomial heat flow, that mismatch is **not intrinsic to the Fourier zero observable**. The XF-049 Volterra law extends exactly to arbitrary complex roots and through multiple-root collisions when the zero sum is treated as a symmetric function of the polynomial coefficients. If

\[
P_t(z)=\prod_{j=1}^N(z-x_j(t)),
\qquad
\partial_tP_t=-\partial_z^2P_t,
\]

with the roots counted with multiplicity but not assumed real or simple, define

\[
Z_N(\xi,t):=\sum_{j=1}^N e^{-i\xi x_j(t)}.
\]

Then for every real `xi` and every real heat time,

\[
\boxed{
\partial_t Z_N(\xi,t)
=
\xi^2Z_N(\xi,t)
-
\xi\int_0^\xi
Z_N(\eta,t)Z_N(\xi-\eta,t)\,d\eta.
}
\tag{1}
\]

At a collision the individual root branches can have square-root singularities, but `Z_N` is analytic in the polynomial coefficients and (1) remains regular. Hence for `xi>0` the finite positive-frequency band is Volterra-triangular **even while roots are complex and while the flow crosses a collision time**.

There is a matching endpoint observation. The Guinand--Weil formula itself does not require RH: for a nontrivial zeta zero `rho`, the natural `H_0` coordinate

\[
x_\rho:=-2i(\rho-\tfrac12)
\tag{2}
\]

is simply complex when `rho` is off the critical line. Entire bandlimited test functions may be evaluated at these complex coordinates. Choosing a one-sided memory-scale test whose Fourier support is contained strictly between zero and the first prime-power line gives an endpoint statistic whose prime contribution vanishes **exactly**, not merely asymptotically. Thus the finite-model obstruction to using the endpoint selector in the `Lambda>0` direction is no longer root reality or collision singularity; it is the passage from the finite symmetric Volterra field to the renormalized infinite Xi zero system.

This does **not** prove that the actual Xi selector propagates, does not define the raw infinite Fourier sum, and does not imply an upper bound on `Lambda`. The remaining theorem is now sharper: construct a renormalized low-positive-frequency Xi field (or an equivalent bandlimited weak formulation) for which the finite collision-safe identity survives with `o(1)` error at the XF-048 memory scale.

## 1. Collision-safe Newton-sum hierarchy

Write

\[
p_m(t):=\sum_{j=1}^N x_j(t)^m,
\qquad p_0=N.
\tag{3}
\]

For simple roots, the usual algebraic heat-root law

\[
x_j'=2\sum_{k\ne j}\frac1{x_j-x_k}
\tag{4}
\]

holds over `C` just as it does over `R`; no ordering or conjugation is used. For `m>=2`, symmetrizing unordered pairs gives

\[
\begin{aligned}
p_m'
&=2m\sum_{j<k}
\frac{x_j^{m-1}-x_k^{m-1}}{x_j-x_k}\\
&=2m\sum_{j<k}\sum_{r=0}^{m-2}
 x_j^{m-2-r}x_k^r.
\end{aligned}
\tag{5}
\]

Because the full sum over `r` is symmetric in the two roots,

\[
\sum_{j<k}\sum_{r=0}^{m-2}x_j^{m-2-r}x_k^r
=
\frac12\sum_{r=0}^{m-2}\sum_{j\ne k}
 x_j^{m-2-r}x_k^r.
\tag{6}
\]

Therefore

\[
\boxed{
p_m'
=
m\sum_{r=0}^{m-2}p_rp_{m-2-r}
-
m(m-1)p_{m-2},
\qquad m\ge2,
}
\tag{7}
\]

with `p_0'=p_1'=0`.

Equation (7) is already free of collision denominators. More importantly, it is not merely a formula obtained by taking a limit of labelled roots. Every `p_m` is a polynomial in the coefficients of the monic polynomial by Newton identities. Under `P_t=-P_{zz}`, the coefficient velocity is polynomial in those coefficients, so the left side of (7) is a polynomial function on coefficient space. The right side is also a symmetric polynomial in the roots, hence a polynomial in the coefficients. Since the two polynomial functions agree on the Zariski-open set of simple-root polynomials, they agree on **all** monic degree-`N` polynomials, including configurations with arbitrary multiplicities.

Thus (7) is the coefficient-level heat-flow law for the root power sums. It does not use a root labelling at a collision and does not extrapolate the singular particle ODE beyond its legitimate coordinate chart.

## 2. The exact Volterra law extends across the discriminant

For finite `N`, expand the symmetric exponential sum as

\[
Z_N(\xi,t)
=
\sum_{m=0}^\infty
\frac{(-i\xi)^m}{m!}\,p_m(t).
\tag{8}
\]

On every compact heat-time interval the roots remain bounded because the monic coefficients do, so (8) and its time derivative converge locally uniformly in `xi`. Inserting (7) into (8) is therefore legitimate.

The linear term in (7) generates

\[
\xi^2Z_N(\xi),
\]

while the quadratic term is identified by the beta integral

\[
\int_0^\xi \eta^a(\xi-\eta)^b\,d\eta
=
\frac{a!b!}{(a+b+1)!}\,\xi^{a+b+1}.
\tag{9}
\]

Coefficient matching gives exactly (1):

\[
\boxed{
\partial_t Z_N(\xi)
=
\xi^2Z_N(\xi)
-
\xi\int_0^\xi Z_N(\eta)Z_N(\xi-\eta)\,d\eta.
}
\tag{10}
\]

This proof is stronger than the real-simple derivation in XF-049 in one specific way: the identity is now a symmetric coefficient identity. For `xi>0`, its right side still uses only `0<=eta<=xi`, even when the roots are nonreal. Hence no positive/negative high-frequency down-conversion channel appears merely because a conjugate pair leaves the real axis.

The statement should not be confused with regularity of individual roots. Root branches can fail to be differentiable at a multiple root; only the symmetric statistic is collision-safe.

## 3. Exact control at the simplest real/complex transition

The degree-two heat flow

\[
P_t(z)=z^2-2t
\tag{11}
\]

has roots `+-sqrt(2t)`: real for `t>0`, double at `t=0`, and purely imaginary for `t<0`. The labelled roots have the expected square-root singularity at the transition, but

\[
Z_2(\xi,t)
=2\cos\!\bigl(\xi\sqrt{2t}\bigr)
=2\sum_{k=0}^\infty
\frac{(-1)^k(2t)^k\xi^{2k}}{(2k)!}
\tag{12}
\]

is entire in `t`. At the collision,

\[
\partial_tZ_2(\xi,0)=-2\xi^2.
\tag{13}
\]

Equation (10) gives the same value directly from `Z_2(eta,0)=2`:

\[
2\xi^2-\xi\int_0^\xi4\,d\eta
=-2\xi^2.
\tag{14}
\]

This is a minimal falsification control for the extension: the Volterra field passes continuously through exactly the point where the root-coordinate vector field blows up.

## 4. A one-sided bandlimited endpoint probe is unconditionally prime-free

The Gaussian in XF-048 was chosen for convenience, but its tiny Fourier tails are not essential. Fix a real even function

\[
\chi\in C_c^\infty((-1,1)),
\qquad \chi(0)=1,
\tag{15}
\]

and define

\[
g(u):=\frac1{2\pi}\int_{-1}^1\chi(s)e^{isu}\,ds,
\qquad \widehat g=\chi.
\tag{16}
\]

Then `g` is entire and rapidly decreasing on every bounded horizontal strip. Keep the XF-048 scales

\[
q\asymp\log^2T,
\qquad M=q^2,
\qquad W=M\sigma_T\asymp\log^3T,
\qquad
\omega=\frac{2\pi}{q\sigma_T}=\Theta(1/\log T),
\tag{17}
\]

so `W omega=2 pi q`. For `varphi=phi-theta/2`, set

\[
f_T(x)
:=
g\!\left(\frac{x-T}{W}\right)
 e^{-i(\omega(x-T)+\varphi)}.
\tag{18}
\]

With the Fourier convention of XF-048,

\[
\boxed{
\widehat f_T(\xi)
=
W e^{-iT\xi-i\varphi}
\chi\!\bigl(W(\xi+\omega)\bigr).
}
\tag{19}
\]

Hence

\[
\operatorname{supp}\widehat f_T
\subset
[-\omega-W^{-1},-\omega+W^{-1}].
\tag{20}
\]

For all sufficiently large `T`, this interval lies strictly below zero and satisfies

\[
\omega+W^{-1}<\frac{\log2}{2}.
\tag{21}
\]

Therefore every prime-power sample `+-log n/2` in the Guinand--Weil formula misses the support exactly. The constant archimedean density also vanishes exactly because

\[
\widehat f_T(0)=W e^{-i\varphi}\chi(W\omega)=0
\tag{22}
\]

once `2 pi q>1`.

The remaining archimedean variation is still

\[
O(W^2/T)+O(W/T^2)=o(1),
\tag{23}
\]

using the rapid decay of `g`; the distant part of the integral is smaller than any power of `T/W`. Likewise the pole terms `f_T(+-i)` are `o(1)` by repeated integration by parts in (16).

Crucially, the zero side of Guinand--Weil is meaningful without assuming RH. For every nontrivial zero `rho`, use the complex coordinate (2). The standard zero argument of the explicit formula is exactly `x_rho/2`, so the scaled formula underlying XF-048 sums `f_T(x_rho)` over all nontrivial zeros with multiplicity. Thus

\[
\boxed{
\sum_\rho f_T(x_\rho)=o(1)
}
\tag{24}
\]

is an unconditional **complex-zero** endpoint statistic. What requires real-rootedness is interpreting these points as an ordered real gap configuration, not the explicit-formula identity itself.

Bandlimited explicit-formula test functions are classical technology; no novelty is claimed for that device. The useful point here is the alignment of its support with the XF-047 memory band and the collision-safe positive-frequency transport above.

## 5. The bandlimited probe still detects the critical coherent memory wave

The exact spectral cutoff does not lose the XF-048 signal. On the coherent lattice control write

\[
z_j=T+j\sigma_T+a\sin(\theta j+\varphi),
\qquad
\theta=\frac{2\pi}{q},
\qquad
\varepsilon=\frac\kappa{q^2},
\qquad
 a=\frac{\sigma_T\varepsilon}{2\sin(\theta/2)}.
\tag{25}
\]

At the unperturbed lattice points, Poisson summation and `supp chi subset (-1,1)` give, for all sufficiently large `q`,

\[
\sum_{j\in\mathbb Z}
 g(j/M)e^{-i\theta j}=0,
\qquad
\sum_j g(j/M)=M,
\qquad
\sum_j g(j/M)e^{-2i\theta j}=0.
\tag{26}
\]

The corresponding identities with `g'` also vanish at the zero and second harmonics because the Fourier transform of `g'` is `is chi(s)`.

Taylor expansion of `f_T(z_j)` about `T+j sigma_T` therefore has a particularly clean linear term:

\[
\sum_j f_T'(T+j\sigma_T)\,
 a\sin(\theta j+\varphi)
=
-\frac{\omega aM}{2}.
\tag{27}
\]

Since

\[
\omega aM
=
\kappa\,\frac{\pi}{q\sin(\pi/q)}
\longrightarrow\kappa,
\tag{28}
\]

while the quadratic remainder is

\[
O\!\left(Ma^2(\omega^2+\omega/W+W^{-2})\right)
=O(\kappa^2/q^2)=o(1),
\tag{29}
\]

we obtain

\[
\boxed{
\sum_j f_T(z_j)
=-\frac\kappa2+o(1).
}
\tag{30}
\]

Thus exact Fourier compactness preserves the order-one discrimination between the actual endpoint statistic (24) and the XF-047 coherent memory wave. The Gaussian constant `-sqrt(2 pi) kappa/2` from XF-048 is replaced only because the envelope normalization has changed.

## 6. Finite endpoint transport no longer needs a real-simple interval

For a finite polynomial zero system, Fourier inversion writes the probe statistic as

\[
S_{T,N}(t)
:=\sum_{j=1}^N f_T(x_j(t))
=
\frac1{2\pi}\int_{\mathbb R}
\widehat f_T(-\xi)Z_N(\xi,t)\,d\xi.
\tag{31}
\]

By (20), `hat f_T(-xi)` is supported entirely in

\[
[\omega-W^{-1},\omega+W^{-1}]
\subset(0,\log2/2)
\tag{32}
\]

for large `T`. Differentiating (31) and using the collision-safe equation (10) invokes only `Z_N(eta,t)` with

\[
0\le\eta\le\xi\le\omega+W^{-1}.
\tag{33}
\]

So in the finite control there is **no cross-Hardy localization leakage at all** for this probe, and no need to stop the identity when roots become complex or collide. A hypothetical positive finite transition time does not separate the endpoint arithmetic statistic from the one-sided spectral evolution.

This is stronger than saying that a Gaussian tail is negligible: the support statement is exact. It also identifies what the finite result does *not* provide. A single scalar `S_{T,N}` is not closed by itself; its derivative depends on the full low-positive band. Moreover `Z_N(0)=N`, so the finite low-frequency field has a diverging background as `N` tends to infinity. These are the genuine normalization/closure issues left for Xi.

## 7. Prior-art and evidence boundary

XF-049 already calibrates the Burgers/Calogero and polynomial heat-flow prior-art class. Contemporary polynomial heat-flow work explicitly treats complex-root distributions and Burgers equations, so neither complex roots under heat flow nor the Burgers correspondence is claimed as new. The targeted literature check also finds routine use of bandlimited extremal functions together with Guinand--Weil explicit formulas. The present derivation therefore makes no novelty claim for Newton identities, compact Fourier support, Guinand--Weil, or complex Burgers.

The durable Mathia-specific content is narrower: **the exact XF-049 Fourier hierarchy is a symmetric coefficient identity and therefore survives both loss of reality and the collision discriminant; simultaneously, an XF-048-scale bandlimited probe can be made exactly prime-free and one-sided without losing order-one sensitivity to the critical memory wave.** This removes the finite-model real-simple/localization barrier from the accepted endpoint-transport clue.

Nothing here defines

\[
\sum_\rho e^{-i\xi x_\rho}
\]

as an ordinary infinite function. The Guinand--Weil side only defines suitably tested endpoint combinations, and the finite Volterra equation contains the divergent quantity `Z_N(0)=N`. Passing to Xi requires a renormalized analogue that subtracts the archimedean background and controls the quadratic term uniformly on the shrinking band `xi=Theta(1/log T)`.

Nor does collision-safety of `Z_N` imply collision-safety of ordered gaps or of the particle labels. It sidesteps those coordinates rather than repairing them. In particular, XF-001's warning about root analyticity at a collision remains intact.

## Research consequence

The accepted endpoint-transport direction can now be posed without an artificial real-simple finite-model restriction. At `t=0`, use the unconditional complex-zero Guinand--Weil functional with a one-sided compact Fourier band around the XF-047 memory frequency. In every finite polynomial heat control, that band evolves by the same Volterra law across real roots, complex roots, and collisions, with no high-to-low convolution and no taper-induced opposite-frequency leakage.

The next gate is therefore genuinely infinite-dimensional: construct a renormalized Xi low-frequency field or weak bandlimited evolution whose quadratic Volterra term is finite after subtracting the archimedean density, and prove that truncation/buffer errors contribute `o(1)` to the matched statistic over the time interval needed for an upper-bound argument. A decisive negative should exhibit an order-one term created specifically by that infinite renormalization; finite collision geometry and ordinary localization can no longer serve as the escape mechanism.