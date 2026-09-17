# NB-184 — Quotient anchoring pushes typical Euler acquisition to the quadratic width scale

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + QUOTIENT-GEOMETRY + MEAN-SQUARE + GAGLIARDO-NIRENBERG + HEIGHT-SELECTIVE + NB-183-REFINEMENT`.

`NB-183` showed that the actual capped-Poisson seminorm of the local Euler kernel is typically much smaller than the uniform high-ordinate majorant, but it stated the convenient sufficient regime `T a^4 -> infinity`. That quartic condition is not the real acquisition threshold. In fact, the `NB-183` mean-square estimate alone already gives the desired `sqrt(a)`-normalized conclusion under the weaker cubic condition `T a^3 -> infinity`.

More importantly, `NB-183` estimated an absolute representative of the Euler kernel even though the signed samplers have zero mass and therefore see the kernel only modulo additive constants. Working in that quotient removes the irrelevant constant mode. A one-dimensional anchored Gagliardo--Nirenberg estimate then interpolates the cheap `L^2` energy of the anchored kernel with the derivative energy instead of paying the full derivative supremum directly.

The result reaches the quadratic scale: if `a=a_T -> 0` and

\[
T a_T^2\to\infty,
\]

then

\[
\boxed{
\sqrt{a_T}\,\mathcal H_{a_T,B}(t)\to0
\quad\text{in relative measure on }[T,2T].
}
\]

Consequently the charged scalar Euler acquisition ratio from `NB-182` beats the full generic `sqrt N` packing threshold on density-one heights for every power width `a=T^{-alpha}` with fixed `alpha<1/2`. The remaining finite-height boundary is the genuine quadratic endpoint `T a^2=O(1)`, not the quartic range left by the first Sobolev proof.

## Claim

Fix `B>0`, `T` sufficiently large and `0<a<=1`. Put

\[
K_{a,t}(u)
:=-\frac{\zeta'}{\zeta}(1+a+i(t+u)),
\qquad |u|\le B,
\]

\[
d_a(u,v):=
\min\left\{1,\frac{|u-v|}{a}\right\},
\]

and retain the actual capped-Poisson source seminorm from `NB-183`,

\[
\mathcal H_{a,B}(t)
:=
\sup_{\substack{u,v\in[-B,B]\\u\ne v}}
\frac{|K_{a,t}(u)-K_{a,t}(v)|}{d_a(u,v)}.
\]

Then

\[
\boxed{
\int_T^{2T}\mathcal H_{a,B}(t)^2\,dt
\ll_B
\sqrt{(T+a^{-2})(T+a^{-4})}
+
a^2\sqrt{(T+a^{-4})(T+a^{-6})}.
}
\tag{1}
\]

Hence, for every fixed `eta>0`,

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:
\mathcal H_{a,B}(t)>\eta a^{-1/2}
\right\}
\right|
\ll_{B,\eta}
 a
+
\frac1{\sqrt{T a^2}}
+
\frac1{T a^2}.
}
\tag{2}
\]

In particular, if `a_T -> 0` and `T a_T^2 -> infinity`, then

\[
\boxed{
\sqrt{a_T}\,\mathcal H_{a_T,B}(t)	o0
\quad\text{in relative measure on }[T,2T].
}
\tag{3}
\]

Since `NB-182` gives `W(a) asymp 1/a`, while the full generic capped-Poisson packing dimension satisfies `N(a) asymp 1/a`, the height-specific scalar acquisition gain obeys

\[
\frac{\kappa_{a,B}(t)}{\sqrt{N(a)}}
\asymp
\frac1{\sqrt a\,\mathcal H_{a,B}(t)}.
\]

Therefore (3) implies

\[
\boxed{
\frac{\kappa_{a_T,B}(t)}{\sqrt{N(a_T)}}
\to\infty
\quad\text{in relative measure}
}
\tag{4}
\]

throughout the quadratic-divergence regime `T a_T^2 -> infinity`.

## Derivation

### 1. The zero-mass transport lives in a quotient by constants

Every signed sampler in the `NB-167` transport setup has total mass zero. Thus

\[
\int (K_{a,t}+c)\,d\nu
=
\int K_{a,t}\,d\nu
\]

for every constant `c`. The intrinsic dual object is therefore the class of `K_{a,t}` in `C([-B,B])/constants`, not its absolute sup norm.

Choose the source-faithful representative

\[
F_t(u):=K_{a,t}(u)-K_{a,t}(0),
\qquad F_t(0)=0,
\]

and write

\[
G_t(u):=\partial_u K_{a,t}(u).
\]

For `|u-v|>=a`,

\[
|K_{a,t}(u)-K_{a,t}(v)|
=|F_t(u)-F_t(v)|
\le2\|F_t\|_\infty.
\]

For `|u-v|<a`, the mean-value theorem gives

\[
\frac{|K_{a,t}(u)-K_{a,t}(v)|}{|u-v|/a}
\le a\|G_t\|_\infty.
\]

Consequently

\[
\mathcal H_{a,B}(t)
\le
2\|F_t\|_\infty+a\|G_t\|_\infty.
\tag{5}
\]

The gain over `NB-183` starts here: the large-scale term is an oscillation norm with an anchored representative, rather than `2 sup|K|`.

### 2. Anchoring lowers the zeroth-order Montgomery--Vaughan endpoint cost

For `Re s=1+a>1`, absolute convergence gives

\[
K_{a,t}(u)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+a}}
 e^{-i(t+u)\log n}.
\]

For fixed `u`, the anchored difference `F_t(u)` is a Dirichlet series with coefficients

\[
\frac{\Lambda(n)}{n^{1+a}}
\left(e^{-iu\log n}-1\right).
\]

The squared coefficient sum is uniformly bounded, while the Montgomery--Vaughan endpoint term satisfies

\[
\sum_{n\ge2}
\frac{\Lambda(n)^2}{n^{1+2a}}
|e^{-iu\log n}-1|^2
\ll
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+2a}}
\ll a^{-2}.
\]

The last estimate is the pole-size bound obtained from one derivative of `-zeta'/zeta` at `1+2a`. Integrating first in height and then over the fixed `u` interval yields

\[
E_0
:=
\int_T^{2T}\|F_t\|_{L^2([-B,B])}^2dt
\ll_B T+a^{-2}.
\tag{6}
\]

The derivative budgets are exactly those already established in `NB-183`:

\[
E_1
:=
\int_T^{2T}\|G_t\|_2^2dt
\ll_B T+a^{-4},
\tag{7}
\]

and, with `G_t'=partial_u G_t`,

\[
E_2
:=
\int_T^{2T}\|G_t'\|_2^2dt
\ll_B T+a^{-6}.
\tag{8}
\]

No new arithmetic input is used here; the only change is that the zeroth-order object is estimated in the correct quotient representation.

### 3. One-dimensional interpolation converts energy into the required suprema

Because `F_t(0)=0`, the fundamental theorem of calculus gives, for every `u in [-B,B]`,

\[
|F_t(u)|^2
=
2\left|
\operatorname{Re}
\int_0^u F_t(x)\overline{G_t(x)}\,dx
\right|
\le
2\|F_t\|_2\|G_t\|_2.
\]

Thus

\[
\|F_t\|_\infty^2
\le2\|F_t\|_2\|G_t\|_2.
\]

After integration in `t` and Cauchy--Schwarz,

\[
\int_T^{2T}\|F_t\|_\infty^2dt
\ll_B
\sqrt{E_0E_1}
\ll_B
\sqrt{(T+a^{-2})(T+a^{-4})}.
\tag{9}
\]

For `G_t` no anchoring is available, because a constant derivative corresponds to a genuine linear mode of `K`. The standard one-dimensional Gagliardo--Nirenberg estimate on the fixed interval gives

\[
\|G_t\|_\infty^2
\ll_B
\|G_t\|_2^2
+
\|G_t\|_2\|G_t'\|_2.
\]

Hence

\[
\int_T^{2T}\|G_t\|_\infty^2dt
\ll_B
E_1+\sqrt{E_1E_2}
\ll_B
\sqrt{(T+a^{-4})(T+a^{-6})},
\tag{10}
\]

where `0<a<=1` makes the geometric-mean term dominate up to an absolute constant. Combining (5), (9) and (10) proves (1).

### 4. The density threshold is quadratic

Chebyshev at the acquisition-critical threshold `eta a^{-1/2}` gives

\[
\frac1T
\left|
\left\{t:\mathcal H_{a,B}(t)>\eta a^{-1/2}\right\}
\right|
\ll_{B,\eta}
\frac aT
\int_T^{2T}\mathcal H_{a,B}(t)^2dt.
\tag{11}
\]

Put `x=T a^2`. The first term from (1) becomes

\[
a
\sqrt{
\left(1+\frac1x\right)
\left(1+\frac1{x a^2}\right)
},
\]

and the second becomes

\[
a^3
\sqrt{
\left(1+\frac1{x a^2}\right)
\left(1+\frac1{x a^4}\right)
}.
\]

Using `sqrt(1+y)<=1+sqrt(y)` and `0<a<=1`, their sum is

\[
\ll
 a+x^{-1/2}+x^{-1}.
\]

This proves (2)--(3). For a power width `a=T^{-alpha}`, the condition is simply `alpha<1/2`.

There is also a bookkeeping correction worth making explicit. `NB-183` proved

\[
T^{-1}\int_T^{2T}\mathcal H_{a,B}(t)^2dt
\ll1+(Ta^4)^{-1}.
\]

At the same threshold `a^{-1/2}`, that estimate by itself gives exceptional density

\[
\ll a+(Ta^3)^{-1}.
\]

So even before the quotient refinement, `T a^3 -> infinity` was enough for the acquisition conclusion. The quartic condition in `NB-183` was a convenient regime making the unnormalized mean square `O(1)`; it should not be read as an acquisition barrier.

## Representation audit

This refinement is representation-sensitive in a favorable and source-faithful way. The zero-mass Jordan transport pairs against functions modulo constants. Anchoring `K_{a,t}` at `u=0` does not change a single physical response, and any other choice of representative in the same quotient gives the same transport functional.

The previous `sup|K|` estimate retained a constant mode that the sampler cannot observe. Estimating that representative before quotienting paid regularity for invisible information. The durable representation lesson is therefore: **quotient out exactly invisible modes before applying maximal or regularity estimates**.

The argument would not transfer unchanged to samplers with nonzero total mass, because additive constants would then become observable. Thus the gain is not an arbitrary normalization trick; it depends essentially on the zero-mass conservation law built into the `NB-167` setup.

## Prior-art boundary

The analytic ingredients are classical: Montgomery--Vaughan mean-value control for Dirichlet series and a one-dimensional Gagliardo--Nirenberg/Sobolev interpolation inequality. A prior-art search also finds the classical and modern literature on mean values of `zeta'/zeta`, including Goldston--Gonek--Montgomery and later work near the critical line, but not a statement for this capped-Poisson quotient seminorm or its Nyman acquisition interpretation.

No new external theorem is load-bearing beyond inputs already anchored in `SOURCES.md`; the elementary anchored inequality above is proved directly. Therefore `SOURCES.md` does not need a new durable dependency.

## Self-adversarial review and limits

### This still does not construct coherent rank

Equation (4) only says that, on most heights, the scalar Euler source has enough charged acquisition gain to pay the `sqrt N` tariff identified in `NB-182`. It does not produce an `N x N` source-natural response matrix with many singular values of order `sqrt N`, nor does it show that the same good-height set supports the phase relations required for such a matrix.

The main post-`NB-183` obstruction therefore survives unchanged: affordable scalar exposure is abundant, but coherent phase reuse remains unproved.

### The conclusion is still density-one, not pointwise

Nothing here excludes a sparse adversarially selected sequence of heights where `mathcal H_{a,B}` is large. The result cannot replace the uniform bound in an argument whose height is chosen after seeing the exceptional set.

### The exact quadratic endpoint remains open

The proof needs `T a^2 -> infinity`. At `T a^2=O(1)`, the Montgomery--Vaughan finite-height endpoint in the anchored zeroth-order energy is already comparable with the acquisition threshold, and (2) no longer tends to zero.

This does not prove that `a ~ T^{-1/2}` is an arithmetic phase transition. It identifies the boundary of this quotient-energy argument. Reaching or crossing the endpoint would require a sharper finite-height/maximal Dirichlet-series input, extra cancellation in the anchored coefficients, or additional source structure.

## Updated frontier

The finite-height side question left by `NB-183` is now compressed from a quartic sufficient regime to the quadratic scale. For `a_T -> 0` with `T a_T^2 -> infinity`, typical local Euler acquisition is already supercritical for the full generic Poisson packing dimension.

The principal source-side question is therefore still coherent rank: can the density-one affordable scalar exposure be organized into a common source-natural phase code without independently renormalizing weak Euler channels? Separately, the only unresolved width regime for this mean-square acquisition mechanism is now the quadratic endpoint and below, `T a_T^2=O(1)`.