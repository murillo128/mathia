# XF-010 — smooth fixed-radius averages see mesoscopic phase only at the `h^4` scale

**Status:** `EXACT-DERIVED` + `CROSS-LINE-OBSTRUCTION` + `CLASSICAL-EXPANSION`. XF-009 proved a general `O(h^2)` frozen-stencil bound for fixed-radius translation averages on the mesoscopic coordinate `X=h^2 j`. The new result is a strict sharpening for smooth local observables: after translation averaging, the entire `O(h^2)` correction is a periodic coboundary and cancels. The first generic phase-sensitive term is therefore `O(h^4)`, with an explicit Hessian/gradient formula. At Xi height `T`, this means `O(log^-4 T)`, one full factor `log^-2 T` below the `O(log^-2 T)` exterior-field defect that drives the fixed-time Cauchy flow in XF-008.

## 1. Claim

Use the perturbative lattice scaling of XF-008--XF-009. Put

\[
\delta:=h^2,
\qquad
X_j=\delta j,
\qquad
v(X):=1+\varepsilon U(X),
\]

on the torus `T=R/(2pi Z)`, and take a subsequence `delta=2pi/N`. Let `r>=1` be fixed and let `F` be a `C^6` function on a compact neighborhood of the diagonal gap range. Define

\[
A_h[F,U]
:=\frac1N\sum_{j=0}^{N-1}
F\bigl(v(X_j),v(X_j+\delta),\ldots,v(X_j+(r-1)\delta)\bigr).
\tag{1}
\]

Assume `U` is `C^6` and periodic, with all relevant derivatives bounded independently of `h`. For `s` in the gap range write

\[
K_F(s)
:=\sum_{m,n=0}^{r-1}(m-n)^2
\,\partial_{mn}F(s,\ldots,s).
\tag{2}
\]

Then

\[
\boxed{
A_h[F,U]
=
\frac1{2\pi}\int_0^{2\pi}F(v(X),\ldots,v(X))\,dX
-
\frac{h^4}{4}\,
\frac1{2\pi}\int_0^{2\pi}
K_F(v(X))\,(v'(X))^2\,dX
+O(h^6).
}
\tag{3}
\]

The implicit constant is uniform for fixed `r` and bounded `C^6` norms on the stated compact range.

Thus the `O(h^2)` error in XF-009 is a valid general Lipschitz bound but is not the first generic correction for a **smooth translation-averaged** fixed stencil. The first-order spatial variation cancels after averaging, and mesoscopic ordering enters generically through a quadratic-gradient term at order `h^4`.

For the equimeasurable cosine controls

\[
U_k(X)=a\cos(kX),
\qquad k\in\mathbb N,
\tag{4}
\]

the leading diagonal term in (3) is independent of `k`, while the first possible frequency-sensitive correction is proportional to `h^4 k^2`. More precisely, with

\[
C_F(a,\varepsilon)
:=\frac1{2\pi}\int_0^{2\pi}
K_F(1+\varepsilon a\cos X)
\,(\varepsilon a\sin X)^2\,dX,
\tag{5}
\]

one has for fixed positive integers `k,ell`

\[
\boxed{
A_h[F,U_k]-A_h[F,U_\ell]
=-\frac{h^4}{4}(k^2-\ell^2)
C_F(a,\varepsilon)+O(h^6).
}
\tag{6}
\]

If `C_F=0`, the observable is even less sensitive and the first distinction occurs at still higher order.

## 2. Exact cancellation of the `h^2` term

For brevity set `v=v(X)` and evaluate all partial derivatives of `F` at the diagonal point `(v,...,v)`. Taylor-expand each shifted argument,

\[
v(X+m\delta)
=v+m\delta v'
+\frac{m^2\delta^2}{2}v''
+O(\delta^3).
\tag{7}
\]

Multivariable Taylor expansion gives

\[
F(v(X),\ldots,v(X+(r-1)\delta))
=f(v)
+\delta A(v)v'
+\frac{\delta^2}{2}
\bigl(B(v)v''+C(v)(v')^2\bigr)
+O(\delta^3),
\tag{8}
\]

where

\[
f(v)=F(v,\ldots,v),
\quad
A(v)=\sum_m mF_m,
\quad
B(v)=\sum_m m^2F_m,
\quad
C(v)=\sum_{m,n}mnF_{mn}.
\tag{9}
\]

The apparent first-order phase term is

\[
A(v(X))v'(X).
\]

But `A` is a scalar function of the single diagonal value `v`, so if `P'=A` then

\[
A(v)v'=\frac{d}{dX}P(v(X)).
\tag{10}
\]

Its torus integral vanishes exactly. This is the cancellation missed by the coarse frozen-stencil estimate in XF-009.

At second order, integration by parts gives

\[
\int B(v)v''\,dX
=-\int B'(v)(v')^2\,dX.
\tag{11}
\]

Because differentiation along the diagonal yields

\[
B'(v)=\sum_{m,n}m^2F_{mn},
\tag{12}
\]

symmetry of the Hessian implies

\[
C(v)-B'(v)
=-\frac12\sum_{m,n}(m-n)^2F_{mn}.
\tag{13}
\]

Substituting into (8) gives the coefficient in (3).

Finally, the uniform periodic lattice average may be replaced by the torus integral to the displayed order. This is a standard periodic trapezoidal/Euler--Maclaurin fact: with sufficient smoothness, all endpoint Bernoulli terms cancel because the integrand and its derivatives are periodic, leaving an error smaller than the `delta^2=h^4` term. The `C^6` hypothesis above is deliberately stronger than necessary so the remainder can safely be written `O(delta^3)=O(h^6)`.

## 3. The local/nonlocal symbol mismatch

Equation (3) has a second interpretation that is more important for the Xi-flow program. A fixed-radius smooth local observable has a finite-stencil Fourier response. Its small-index-frequency symbol is therefore analytic near `theta=0`; after translation averaging the first spatially sensitive term is quadratic,

\[
\text{local fixed stencil:}\qquad
\Delta A\sim c_F\,\theta^2.
\tag{14}
\]

On the fixed-time mesoscopic scale of XF-008,

\[
\theta=\kappa h^2,
\]

so this becomes

\[
\Delta A\sim c_F h^4\kappa^2.
\tag{15}
\]

The actual linearized gap dynamics are different. XF-008 gives

\[
\partial_tU=-2\pi|D_X|U,
\qquad
\lambda(\kappa)=-2\pi|\kappa|,
\tag{16}
\]

and the normalized exterior-field defect obeys

\[
R-2=\pi h^2|\kappa|U+O(h^4\kappa^2U).
\tag{17}
\]

The nonanalytic `|kappa|` is the signature of the long-range `1/m^2` zero interaction. A smooth finite stencil has only an analytic long-wave expansion and therefore cannot reproduce that first-order fractional symbol. It sees a `kappa^2` gradient energy only one scale later.

This locality/nonlocality distinction is classical in lattice continuum limits: short-range interactions produce local integer-order dispersion, whereas sufficiently long-range kernels produce fractional symbols. Kirkpatrick--Lenzmann--Staffilani prove this dichotomy in a different lattice evolution, and Ciaurri--Roncal--Stinga--Torrea--Varona develop the corresponding discrete fractional-diffusion framework. Those works do not contain the Xi-specific coefficient (3); they delimit the prior-art universality class of the symbol mismatch.

## 4. Consequence at Xi height

The Xi spacing normalization is

\[
h_T\sim\frac{4\pi}{\log T}.
\tag{18}
\]

Therefore

\[
h_T^2\asymp\frac1{(\log T)^2},
\qquad
h_T^4\asymp\frac1{(\log T)^4}.
\tag{19}
\]

XF-008 showed that a fixed-time Cauchy mode can be driven by an exterior-field defect of size only `O(log^-2 T)`. XF-009 showed that a general fixed-radius statistic loses mesoscopic phase at leading order and gave a coarse `O(log^-2 T)` observation error. Equation (3) now shows that for the large and natural class of **smooth translation-averaged** local observables, phase information is actually suppressed to `O(log^-4 T)`.

So a theorem giving only the limiting value of a smooth fixed-block statistic is two asymptotic orders removed from the fixed-time field: it first loses the phase at leading order, and translation averaging then kills the entire first derivative correction. Recovering the Cauchy driver from such an observable would require resolving a `log^-4 T` correction and then relating its local `kappa^2` content to a nonlocal `|kappa|` quantity. That is substantially stronger than merely proving an `o(1)` local-gap asymptotic.

This does **not** upgrade the requirement for every possible statistic to `log^-4 T`. Nonsmooth observables can evade the cancellation. For example, a local absolute difference behaves as

\[
|v(X+\delta)-v(X)|
=\delta|v'(X)|+O(\delta^2),
\]

so its translation average can contain genuine `O(h^2)` phase information. Likewise an `h`-dependent functional with derivatives blowing up as `h->0`, a radius growing like `h^-2`, or a genuinely nonlocal statistic falls outside (3).

## 5. Stress tests and boundary conditions

The cancellation uses **translation averaging**. A statistic tied to absolute mesoscopic location can retain the pointwise `O(h^2)` derivative term before integration. This is relevant because most zeta-zero asymptotics average over height or blocks, but the present theorem should not be applied automatically to a localized weighted statistic.

Smoothness also matters. XF-009 was intentionally stated for Lipschitz `F`; the cusp in a nonsmooth local observable can turn a signed first derivative into an absolute one and prevent the coboundary cancellation. Thus XF-009's general `O(h^2)` bound remains valid, while XF-010 identifies a stronger obstruction for the smooth subclass.

The result remains perturbative and mesoscopic. It does not assert that actual Xi gaps form a globally smooth modulation, nor that large Lehmer pairs, collision cascades, or other nonlinear defects obey this expansion. The synthetic profiles are controls for the universal lattice linearization, not claimed complete zero sets of an admissible Xi-type entire function.

Aliasing is excluded by holding the mesoscopic profile and its frequencies fixed as `h->0`. Frequencies growing with `1/h` leave the smooth fixed-time continuum regime and require a separate scaling analysis.

Finally, (3) is an observation theorem, not an upper bound on `Lambda`. It identifies what information a broad class of local statistics provably cannot carry at the order where the candidate fixed-time mechanism lives.

## 6. Prior art and novelty boundary

The multivariable Taylor expansion, integration-by-parts cancellation, and periodic trapezoidal/Euler--Maclaurin control are classical. Javed and Trefethen, **A trapezoidal rule error bound unifying the Euler--Maclaurin formula and geometric convergence for periodic functions**, *Proceedings of the Royal Society A* 470 (2014), 20130571, provide a modern authoritative treatment of periodic trapezoidal accuracy.

The local-versus-fractional continuum-limit boundary is also classical. Kay Kirkpatrick, Enno Lenzmann and Gigliola Staffilani, **On the continuum limit for discrete NLS with long-range lattice interactions**, *Communications in Mathematical Physics* 317 (2013), 563--591, rigorously show in their setting that long-range interactions generate fractional dispersion while short-range interactions produce the ordinary Laplacian. Ciaurri et al. remain the direct stored anchor for discrete nonlocal diffusion and fractional limits.

No novelty is claimed for Taylor expansion, periodic quadrature, finite-stencil analyticity, or the abstract fact that fractional operators require nonlocal information. The Mathia-specific contribution is the exact combination with the Xi normalization and XF-008: the first-order fixed-stencil correction is a translation coboundary, the surviving smooth local signal is `h^4 kappa^2`, while the Xi zero-flow driver is already `h^2|kappa|`. This sharpens the observation-side scale mismatch from XF-009 by a full factor of `h^2` for smooth local averages.

## 7. Consequence for `xi_flow`

The perturbative fixed-time route now has a more precise information hierarchy. The dynamics keep order-one heat-time memory only on `Theta(log^2 T)` gaps (XF-007), converge there to a nonlocal Cauchy field driven by a `log^-2 T` equilibrium defect (XF-008), and fixed-radius averages lose that field's phase at leading order (XF-009). XF-010 shows that **smooth translation averaging additionally annihilates the entire `log^-2 T` first correction**, leaving only a generic `log^-4 T` local-gradient signal.

A credible fixed-time statistical input should therefore prefer a genuinely mesoscopic/nonlocal observable, or at least a deliberately nonsmooth/local statistic whose `O(log^-2 T)` term can be controlled unconditionally and shown to couple to the `|D|` field. Merely obtaining a more accurate smooth fixed-block constant is structurally mismatched: its long-wave response is local and quadratic exactly where the Xi flow is nonlocal and first-order fractional.