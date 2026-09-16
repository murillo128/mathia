# NB-163 — Finite-order moment balancing shares one target/Euler boundary currency

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + SOURCE-SPECIFIC + VANISHING-MOMENT + BOUNDARY-SCALE + DECISIVE-METHOD-BOUNDARY

`NB-162` leaves one-Poisson-width interlacing as the bounded-conditioning regime not controlled by either sign separation or sub-width transport collapse. A natural next escape is to interlace many positive and negative samples inside one width and impose several vanishing local moments, hoping that the prime-side Fourier phases then cancel to high order while the Poisson target remains visible.

For every fixed finite cancellation order, that hope has a precise generic limit. The same normalized absolute moment that bounds the target Poisson response also bounds the signed Euler response at its natural boundary scale. Thus finite-order local moment balancing does not create an independent prime-side currency: making its Taylor remainder small makes the target remainder small on the same scale.

## Claim

Fix an integer `r>=1` and `A>0`. Let `0<a<=A`, let `nu` be a finite real signed Borel measure on `R`, and choose a center `t_0 in R`. Assume

\[
\int (t-t_0)^k\,d\nu(t)=0,
\qquad 0\le k<r,
\]

and

\[
M_r(\nu;t_0)
:=
\int |t-t_0|^r\,d|\nu|(t)<\infty.
\]

Choose a positive reference mass `c>0` and define the dimensionless `r`-th moment currency

\[
\boxed{
\Xi_r
:=
\frac{M_r(\nu;t_0)}{c\,a^r}.
}
\]

Then the following hold.

### 1. Every target Poisson response is bounded by the same moment currency

For `x>0` and `gamma in R`, define

\[
Q_\nu(x,\gamma)
:=
\int
\frac{x}{x^2+(\gamma-t)^2}
\,d\nu(t).
\]

For every `x>=a`,

\[
\boxed{
|Q_\nu(x,\gamma)|
\le
\frac{M_r(\nu;t_0)}{x^{r+1}}
=
\frac{c}{x}\,\Xi_r\left(\frac{a}{x}\right)^r
\le
\frac{c}{x}\,\Xi_r.
}
\]

Consequently, if a target zero is required to carry a fixed fraction `q>0` of its natural Poisson peak scale,

\[
|Q_\nu(x_*,\gamma_*)|
\ge
q\frac{c}{x_*},
\]

then necessarily

\[
\boxed{
\Xi_r
\ge
q\left(\frac{x_*}{a}\right)^r
\ge q.
}
\]

Thus a family with `Xi_r -> 0` is target-invisible, independently of how many atoms or sign changes realize the moment cancellation.

### 2. The signed Euler response is bounded by the same `Xi_r`

Define

\[
\mathcal E_a(\nu)
:=
\int
\frac{\zeta'}{\zeta}(1+a+it)
\,d\nu(t).
\]

For `v>=0`, the moment conditions and the order-`r` Taylor remainder of `e^{-iv(t-t_0)}` give

\[
\left|
\int e^{-ivt}\,d\nu(t)
\right|
\le
\frac{v^r}{r!}M_r(\nu;t_0).
\]

Since the Dirichlet series for `zeta'/zeta` converges absolutely on `Re s>1`, termwise integration yields

\[
\boxed{
|\mathcal E_a(\nu)|
\le
\frac{M_r(\nu;t_0)}{r!}
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^r}{n^{1+a}}.
}
\]

Put

\[
F(a):=-\frac{\zeta'}{\zeta}(1+a)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^{1+a}}.
\]

Then

\[
(-1)^rF^{(r)}(a)
=
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^r}{n^{1+a}},
\]

and the simple pole of `zeta` at `1` gives, for every fixed `r`,

\[
(-1)^rF^{(r)}(a)
=
\frac{r!}{a^{r+1}}+O_{r,A}(1)
\qquad(a\to0^+).
\]

Hence

\[
\boxed{
|\mathcal E_a(\nu)|
\le
(1+o_r(1))\frac{c}{a}\,\Xi_r
\qquad(a\to0^+).
}
\]

More uniformly, for fixed `r` and `A` the finite constant

\[
B_{r,A}
:=
\sup_{0<a\le A}
\frac{a^{r+1}}{r!}
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^r}{n^{1+a}}
<\infty
\]

gives

\[
\boxed{
|\mathcal E_a(\nu)|
\le
B_{r,A}\frac{c}{a}\,\Xi_r.
}
\]

Thus `Xi_r=o(1)` buys strong generic signed Euler cancellation only by simultaneously making every Poisson target response `o(c/x)`.

### 3. Sub-width support converts moment cancellation into geometric suppression

Suppose in addition that

\[
\operatorname{supp}\nu
\subset
[t_0-L,t_0+L]
\]

and write

\[
V:=\|\nu\|_{\rm TV},
\qquad
C:=\frac{V}{c}.
\]

Then

\[
M_r(\nu;t_0)
\le
VL^r,
\]

so

\[
\boxed{
\Xi_r
\le
C\left(\frac{L}{a}\right)^r.
}
\]

For bounded conditioning, any fixed-order vanishing-moment sampler supported on `L=o(a)` is therefore invisible both to the target and to the Euler side. More quantitatively, if `L<=lambda a` with fixed `lambda<1`, each additional fixed vanishing moment improves the generic upper bound by another factor `lambda`.

But at the unresolved one-width scale `L asymp a`, the estimate only gives `Xi_r=O(C)`. Finite-order moment balancing by itself therefore supplies no new small parameter in the regime left open by `NB-162`.

## Derivation

### Target kernel

Write `u=t-t_0` and

\[
K(u)
:=
\frac{1}{x+i(t_0+u-\gamma)}.
\]

Then

\[
Q_\nu(x,\gamma)
=
\Re\int K(t-t_0)\,d\nu(t).
\]

For every integer `r>=0`,

\[
K^{(r)}(u)
=
\frac{(-i)^r r!}
{[x+i(t_0+u-\gamma)]^{r+1}},
\]

hence

\[
|K^{(r)}(u)|
\le
\frac{r!}{x^{r+1}}.
\]

Subtract the Taylor polynomial of degree `r-1` at `u=0`. Its integral against `nu` is zero by the moment hypotheses, while the integral remainder is at most `|u|^r/x^{r+1}`. Integrating against total variation proves the target bound.

### Euler kernel

For `Re s>1`,

\[
\frac{\zeta'}{\zeta}(s)
=-\sum_{n\ge2}\frac{\Lambda(n)}{n^s}
\]

absolutely. The order-`r` Taylor formula gives

\[
e^{-ivu}
=
\sum_{k=0}^{r-1}\frac{(-ivu)^k}{k!}
+R_r(u,v),
\qquad
|R_r(u,v)|\le\frac{|uv|^r}{r!}.
\]

The polynomial terms vanish after integration against `nu`, so

\[
\left|
\widehat\nu(v)
\right|
\le
\frac{v^r}{r!}M_r.
\]

Substituting `v=log n` in the absolutely convergent Euler series proves the displayed estimate. The Laurent expansion

\[
F(a)=\frac1a+H(a),
\]

with `H` analytic near `a=0`, gives

\[
(-1)^rF^{(r)}(a)
=
\frac{r!}{a^{r+1}}+O_r(1)
\]

for fixed `r`, which identifies the boundary normalization.

## Sharpness of the order-`r` scaling

The power `r` is not an artefact of the proof. For fixed `r`, take the signed finite-difference measure

\[
\nu_{r,h}
=
\alpha
\sum_{j=0}^r
(-1)^{r-j}\binom rj
\delta_{t_0+jh}.
\]

It annihilates every polynomial of degree below `r`. For any sufficiently smooth test function `f`,

\[
\int f(t)\,d\nu_{r,h}(t)
=
\alpha\,\Delta_h^r f(t_0)
=
\alpha h^r f^{(r)}(t_0)+O_r(|\alpha|h^{r+1}\|f^{(r+1)}\|).
\]

For the Poisson kernel, choose a bounded normalized target offset at which its `r`-th derivative is nonzero. With `x=a` and `h/a->0`, this gives a response of order

\[
\frac{|\alpha|}{a}
\left(\frac{h}{a}\right)^r.
\]

Likewise its Fourier transform is exactly

\[
\widehat\nu_{r,h}(v)
=
\alpha e^{-it_0v}
(e^{-ihv}-1)^r,
\]

which is of order `|alpha|(hv)^r` when `hv` is small. Thus the exponent `r` in the generic Fourier/Taylor control cannot be improved from the vanishing-moment hypotheses alone.

This sharpness statement does **not** lower-bound the complete zeta Euler sum: the arithmetic phases `n^{-it_0}` can still cancel across `n`. Such source-specific cancellation is precisely outside the absolute-value argument here.

## Relation to NB-162

For `r=1`, the present centered first absolute moment is a convenient but generally nonoptimal transport quantity. `NB-162` is sharper because it uses the optimal Jordan coupling `W_1`, not transport through a prescribed center. The new content starts with higher vanishing moments: even after forcing exact cancellation of several local polynomial modes, the first uncontrolled moment enters the target and the prime-side Fourier response with the same boundary normalization.

This narrows the one-width frontier. A construction cannot claim a new escape merely because its signed height profile has many zero moments. To beat the generic obstruction it must do at least one of the following: exploit arithmetic phase cancellation in the actual von Mangoldt sum beyond the moment majorant; use a nonlocal geometry not captured by a finite local Taylor jet; or produce source-faithful target information that is not represented by the same exterior Poisson kernel.

## Prior-art and novelty audit

Vanishing moments, Taylor suppression of smooth test functions, and finite-difference measures are classical tools from approximation and wavelet analysis. A fresh search around vanishing-moment Fourier bounds, finite-difference annihilators, and zeta logarithmic-derivative sampling found those standard mechanisms and nearby kernel constructions, but no source giving the line-specific coupled statement above: the same normalized `r`-th local moment simultaneously upper-controls an exterior zeta-zero Poisson target and the signed Euler-product response at the `c/a` boundary scale.

No novelty is claimed for the Taylor remainder, the Fourier vanishing-moment estimate, finite differences, or the Laurent expansion separately. All load-bearing zeta identities are already part of this line's analytic toolkit, so `SOURCES.md` requires no new anchor.

## Boundaries and failure modes

The theorem is a **generic absolute-value obstruction**, not a lower bound on actual Euler leakage and not a proof that one-width interlacing fails. A zeta-specific correlation among the phases `n^{-it_0}` may make `mathcal E_a(nu)` much smaller than the displayed majorant while leaving target response visible; establishing such cancellation would be genuinely new arithmetic input.

The order `r` is fixed while `a->0`. No uniform statement is claimed for `r=r(a)->infinity`; that regime requires uniform control of `B_{r,A}`, the conditioning cost of imposing many moments, and the geometry of the resulting signed measure. The support estimate also uses an actual local radius `L`; moment cancellation without localization need not make `M_r` small.

Finally, the result concerns the exterior Poisson/Euler architecture developed in `NB-154` through `NB-162`. It does not by itself control the finite-section target leakage in the older Hardy/Nyman projection problem, nor does it convert a local sampler estimate into an RH consequence.

## Source map

- `NB-154`: unsigned boundary Euler cost at horizontal gap `a`.
- `NB-160`: routine adverse-zero reservoir for sufficiently sign-separated Jordan supports.
- `NB-161`: Jordan transport length as the conditioning price of sign collapse.
- `NB-162`: the first-order scale-invariant transport currency `Theta=C ell/a` controlling both target gain and signed Euler leakage.

## Consequence for the line

Finite-order local moment cancellation does not open a free channel inside the signed exterior-sampling architecture. **For each fixed order `r`, the dimensionless quantity `Xi_r=M_r/(c a^r)` upper-controls both every normalized Poisson target response and the signed Euler response relative to its natural `c/a` boundary scale.** Sub-width localization can make both small as `(L/a)^r`; at one Poisson width, however, finite moment balancing alone supplies no small parameter. The surviving question is therefore genuinely arithmetic or nonlocal: can an interlaced one-width sampler use zeta-specific prime phases, rather than generic smooth-kernel cancellation, to suppress the Euler side without suppressing its target?