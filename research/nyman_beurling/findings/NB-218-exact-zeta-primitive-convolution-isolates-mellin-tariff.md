# NB-218 — Exact zeta-primitive convolution isolates the Mellin tariff at absolute-value decoupling

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + METHOD-REDUCTION + OSCILLATORY-CORRELATION + FOURIER-DUALITY + ZETA-PRIMITIVE + NB-217-REFINEMENT`.

`NB-213`--`NB-217` show that ordinary Mellin primitivization does not improve the source-side Vinogradov--Korobov growth class if the primitive is separated from the reconstruction kernel by an absolute-value estimate. The final open branch in `NB-217` is therefore deliberately correlation-sensitive: keep the zeta primitive and the reconstruction kernel coupled until after their oscillation has interacted.

There is an exact identity that makes this branch concrete. In the absolutely convergent half-plane, a smoothed von-Mangoldt shell is recovered from the `j`-fold zeta primitive by convolution with the reconstruction kernel, and the factors `(log n)^j` and `(log n)^(-j)` cancel **coefficient by coefficient inside the signed integral**. Moreover, because a genuine shell is supported away from logarithmic frequency `u=0`, the reconstruction kernel annihilates every polynomial jet of the primitive. Thus the primitive's absolute size, and even any finite Taylor drift across the vertical variable, is invisible to the exact shell extraction.

The `X^j` tariff from `NB-213`--`NB-217` is therefore not an algebraic obstruction to the exact bilinear pairing. It enters precisely when the pairing is decoupled into a reconstruction norm times a pointwise primitive norm. This does not yet beat the tariff analytically: any estimate that takes absolute values after the convolution inherits the same reciprocal-support lower bounds. What changes is the next target. The live source problem is now a **local Fourier-coefficient / oscillatory-convolution estimate for the zeta primitive**, not a better pointwise bound for that primitive and not another shell redesign.

## 1. Exact primitive convolution in the absolutely convergent half-plane

Fix

\[
\sigma=1+a>1,
\qquad
u_n:=\log n,
\]

and let

\[
h\in C_c^\infty((0,\infty);\mathbb C).
\]

For an integer `j>=1`, define the `j`-fold logarithmic primitive Dirichlet series

\[
P_{j,\sigma}(t)
:=
\sum_{n\ge2}
\frac{\Lambda(n)}{(\log n)^j}
\,n^{-\sigma-it}.
\tag{1}
\]

Absolute convergence is immediate for `sigma>1`. Define also the source shell correlation

\[
S_{h,\sigma}(t)
:=
\sum_{n\ge2}
\Lambda(n)h(\log n)n^{-\sigma-it},
\tag{2}
\]

and the reconstruction kernel

\[
K_{j,h}(v)
:=
\int_0^\infty
u^j h(\nu)e^{iv\nu}\,d\nu.
\tag{3}
\]

Since `h` is smooth and compactly supported, `K_(j,h)` is Schwartz. Fourier inversion gives

\[
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)e^{-iv\nu_n}\,dv
=
\nu_n^j h(\nu_n).
\tag{4}
\]

Insert (1) into the convolution and use absolute convergence together with the rapid decay of `K_(j,h)`:

\[
\begin{aligned}
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)
P_{j,\sigma}(t+v)\,dv
&=
\sum_{n\ge2}
\frac{\Lambda(n)n^{-\sigma-it}}{\nu_n^j}
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)e^{-iv\nu_n}\,dv\\
&=
\sum_{n\ge2}
\Lambda(n)h(\nu_n)n^{-\sigma-it}.
\end{aligned}
\]

Hence

\[
\boxed{
S_{h,\sigma}(t)
=
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)
P_{j,\sigma}(t+v)\,dv.
}
\tag{5}
\]

The reconstruction multiplier and primitive divisor cancel exactly **inside** the oscillatory integral. No factor comparable with the shell scale has yet been lost.

## 2. For `j=1` the primitive is exactly `log zeta`

For `Re(s)>1`, the Euler product gives the classical identity

\[
\log\zeta(s)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\log n}n^{-s}.
\tag{6}
\]

Therefore

\[
\boxed{
P_{1,\sigma}(t)
=
\log\zeta(\sigma+it),
}
\tag{7}
\]

with the analytic branch supplied by the nonvanishing Euler product in the half-plane `Re(s)>1`. More generally, if

\[
P_{0,\sigma}(t)
:=
\sum_{n\ge2}\Lambda(n)n^{-\sigma-it}
=
-\frac{\zeta'}{\zeta}(\sigma+it),
\tag{8}
\]

then

\[
\boxed{
\frac d{dt}P_{j,\sigma}(t)
=-iP_{j-1,\sigma}(t).
}
\tag{9}
\]

Thus (1) is literally the vertical primitive hierarchy relevant to `NB-213`--`NB-217`. Equation (5) is not an analogy between a generic Fourier model and the Euler source: for `j=1` it couples the shell directly to `log zeta`, and for higher `j` to its successive vertical primitives.

## 3. A true shell annihilates every finite polynomial jet of the primitive

Put

\[
g_{j,h}(\nu):=\nu^j h(\nu).
\]

Because `h` has compact support strictly inside `(0,infinity)`, the function `g_(j,h)` vanishes on a neighbourhood of `nu=0`. The Fourier transform in (3) therefore has vanishing moments of every order:

\[
\boxed{
\int_{\mathbb R}v^mK_{j,h}(v)\,dv=0
\qquad(m=0,1,2,\ldots).
}
\tag{10}
\]

Indeed, Fourier inversion identifies the left side, up to the harmless convention-dependent unit factor, with `2pi` times the `m`-th derivative of `g_(j,h)` at the origin, and every such derivative vanishes.

Consequently, for **every polynomial** `q(v)`, equation (5) may be rewritten as

\[
\boxed{
S_{h,\sigma}(t)
=
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)
\bigl(P_{j,\sigma}(t+v)-q(v)\bigr)\,dv.
}
\tag{11}
\]

In particular, the constant component can always be removed:

\[
S_{h,\sigma}(t)
=
\frac1{2\pi}
\int_{\mathbb R}
K_{j,h}(v)
\bigl(P_{j,\sigma}(t+v)-P_{j,\sigma}(t)\bigr)\,dv.
\tag{12}
\]

And for any fixed `m`, one may subtract the degree-`m` Taylor polynomial of the primitive at `t` without changing the source correlation. The shell does not see a large slowly varying background of `P_j`; it sees only the component whose vertical Fourier content reaches the logarithmic frequencies occupied by the source.

This sharpens the phrase “exploit oscillatory correlation” left by `NB-217`. The correlation is not merely a possible numerical cancellation. Shell localization forces an exact high-pass cancellation of every finite polynomial jet before any analytic estimate is applied.

## 4. On a moving shell the problem is an explicit local Fourier coefficient

Suppose for clarity that

\[
h(\nu)=\phi(\nu-X),
\qquad
\operatorname{supp}\phi\subset[0,\Delta],
\qquad
X>0.
\tag{13}
\]

Then

\[
K_{j,h}(v)
=
e^{iXv}B_{X,j,\phi}(v),
\tag{14}
\]

where

\[
B_{X,j,\phi}(v)
:=
\int_0^\Delta
(X+y)^j\phi(y)e^{ivy}\,dy.
\tag{15}
\]

Equation (5) becomes

\[
\boxed{
S_{h,\sigma}(t)
=
\frac1{2\pi}
\int_{\mathbb R}
B_{X,j,\phi}(v)
P_{j,\sigma}(t+v)
e^{iXv}\,dv.
}
\tag{16}
\]

So the shell source is exactly a Fourier coefficient at the carrier frequency `X` of a locally weighted translate of the zeta primitive. The coefficient divisor `(log n)^(-j)` in `P_j` and the factor `(X+y)^j` in `B` are matched on the same spectral atoms. This is the signed mechanism that disappears when one replaces the integrand by its modulus.

For `j=1`, the concrete target is therefore

\[
\frac1{2\pi}
\int_{\mathbb R}
B_{X,1,\phi}(v)
\log\zeta(\sigma+i(t+v))
e^{iXv}\,dv,
\tag{17}
\]

not `sup_v |log zeta(sigma+i(t+v))|` by itself.

## 5. This locates exactly where the `NB-217` tariff enters

If equation (5) is immediately bounded by absolute values, one gets

\[
|S_{h,\sigma}(t)|
\le
\frac1{2\pi}
\|K_{j,h}\|_1
\sup_v|P_{j,\sigma}(t+v)|.
\tag{18}
\]

This is precisely the decoupling architecture audited by `NB-213`--`NB-217`. For support `E=supp(h)`, `NB-217` gives, after normalization by any bounded nonzero source signal `M_psi(h)`,

\[
\frac{\|K_{j,h}\|_1}{|M_\psi(h)|}
\ge
\frac{2\pi}{\int_E\nu^{-j}\,d\nu}.
\tag{19}
\]

When `E` stays in `nu asymp X`, this reproduces the positive-power reconstruction tariff. Equation (5), however, shows that this lower bound is a statement about the **operator norm of the decoupled estimate**, not about an unavoidable scalar factor in the exact source identity.

The same point is visible from (11). Define the weighted polynomial-quotient error

\[
\mathcal E_{j,h,m}(t)
:=
\inf_{q\in\mathcal P_m}
\int_{\mathbb R}
|K_{j,h}(v)|
|P_{j,\sigma}(t+v)-q(v)|\,dv.
\tag{20}
\]

Then

\[
\boxed{
|S_{h,\sigma}(t)|
\le
\frac1{2\pi}\mathcal E_{j,h,m}(t)
}
\tag{21}
\]

for every `m`. This bound can discard an arbitrarily large polynomial component of the primitive for free. Yet if one controls the residual only by a uniform envelope, the `L^1` tariff returns. Thus merely replacing `||P_j||_infinity` by a better pointwise primitive bound is still insufficient; one needs either unusually accurate local polynomial approximation on the kernel-weighted region or, more strongly, a direct signed estimate of (16).

## 6. What this does and does not buy on the Vinogradov--Korobov route

The identity settles one representation question. **There is no intrinsic `X^j` multiplier loss before absolute-value decoupling.** The full source coefficient is reconstructed exactly from the primitive coefficients. The positive powers isolated in `NB-213`--`NB-217` arise when a proof forgets the phase relation between `K_(j,h)` and `P_j` and prices them independently.

That does not yet improve the Vinogradov--Korobov corridor. Three nontrivial analytic issues remain.

First, (5) is proved cleanly on `Re(sigma)>1`, where the Dirichlet series is absolutely convergent. The source gain in `NB-211`--`NB-213` comes from shifting toward a zero-free line to the left of `1`. Continuing the primitive convolution through that shift requires tracking the pole, branch choices for `log zeta`, zeros avoided by the contour, and the truncation tails. The exact half-plane identity does not make those terms disappear.

Second, (5) is a full-line convolution. The Vinogradov--Korobov input is effective on a controlled vertical window. Replacing the full integral by that window requires a tail theorem for the coupled kernel-primitive product. Bounding the tail by `||K||_1 sup|P_j|` simply recreates the tariff outside the window.

Third, a pointwise estimate for `P_j` cannot exploit (10). What is needed is information about the **vertical Fourier content or local oscillation** of the primitive at the moving carrier frequency `X`. That is a different analytic object from the pointwise envelopes audited in `NB-212`--`NB-217`.

Accordingly, this finding is a reduction of the live escape, not a new zeta bound and not a lower bound for the Nyman distance.

## 7. Representation and prior-art audit

**Generic mechanism.** Equations (5), (10) and (11) are Fourier inversion and moment cancellation. Any Dirichlet/Fourier series with spectral atoms `nu_n`, whose `j`-fold primitive divides coefficients by `nu_n^j`, has the same exact reconstruction identity after multiplication by `nu^j` in the shell kernel. The annihilation of polynomial jets follows generically from physical-frequency support separated from the origin.

**Arithmetic specialization.** For the Euler source the spectral atoms are `nu_n=log n`, the coefficients are `Lambda(n)n^(-sigma)`, the first primitive is exactly `log zeta`, and the zeroth member is `-zeta'/zeta`. Those identities make the generic convolution coincide with the actual full von-Mangoldt acquisition used in this research line rather than with a surrogate Fourier model.

A targeted prior-art search found the standard Dirichlet-series identities for `-zeta'/zeta` and `log zeta`, as well as the classical Fourier/explicit-formula viewpoint connecting logarithmic prime frequencies to the zeta function. No external theorem is load-bearing for (5) or (10): both are direct Fourier inversion once (6) is known, and no novelty is claimed for those generic identities. The project-local contribution is the method localization: after `NB-217`, the exact pairing proves that the remaining cost is not coefficient reconstruction itself but the analytic act of decoupling the zeta primitive from its carrier-frequency kernel. `SOURCES.md` therefore needs no new anchor.

## 8. Adversarial checks and research consequence

**The identity is not itself a saving.** A convolution formula can be exact while every available estimate for it is still expensive. If the proof returns to (18), all conclusions of `NB-213`--`NB-217` apply unchanged.

**Polynomial annihilation is not the same as small remainder.** Equation (11) removes any chosen finite jet exactly, but `zeta` may vary too rapidly on the relevant vertical scale for the residual to be small enough. No regularity estimate with the required strength is asserted here.

**The half-plane location matters.** The clean coefficientwise derivation uses `sigma>1`. Transporting it to the shifted Vinogradov--Korobov contour is a separate analytic step and may introduce boundary or branch contributions. Those contributions must be accounted for rather than hidden in the notation.

**Rough source masks require approximation.** Smooth compact support was chosen so `K_(j,h)` is Schwartz and all moment manipulations are classical. Bounded or discontinuous masks can be approximated, but their tails must be priced explicitly before importing the same conclusions.

**Destination coupling is still absent.** Nothing here proves that a near-optimal Nyman approximant forces a nontrivial value of `S_(h,sigma)(t)`. The destination theorem identified throughout this line remains load-bearing.

The durable next question is now precise. Instead of seeking another primitive, another sign pattern, or another support geometry, seek a **cancellation-sensitive estimate for the carrier Fourier coefficient (16)**, together with a localization theorem that survives the Vinogradov--Korobov contour shift. A positive result must retain the correlation between `P_j(t+v)` and `e^(iXv)B(v)`; a negative result would have to show that even this native bilinear pairing necessarily pays a positive-power cost. Either outcome would address the actual escape left by `NB-217` rather than another absolute-norm representation variant.
