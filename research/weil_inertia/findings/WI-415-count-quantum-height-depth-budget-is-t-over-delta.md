# WI-415 — Translated Blaschke count coercivity has a sharp T/delta height-depth budget

**Status:** `CLASSICAL-IDENTITY + LITERATURE+DERIVED + EXACT-DERIVED + DECISIVE-NEGATIVE`.

**Parents:** [WI-411](./WI-411-vertical-translations-obey-height-area-budget.md), [WI-412](./WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md), [WI-414](./WI-414-one-sided-blaschke-coercivity-forces-haar-rate-scale-density.md).

## Claim

WI-414 left finite depth windows and coupling between horizontal scale and vertical center outside its Beurling-density theorem. For finite-total-variation **linear** translated Blaschke mixtures, those two freedoms can be priced together sharply when the desired observable is a fixed count quantum rather than a response proportional to the horizontal defect depth.

For

\[
q>0,\qquad T>0,\qquad 0<\delta\le d_0\le \frac12,
\]

let `M_*(T,delta,d_0;q)` be the infimum of `||nu||_TV` over finite signed or complex Borel measures `nu` on `(0,infinity) x R` such that the same mixture

\[
Q_\nu(\gamma,d)
:=
\int q_{a,b}(\gamma,d)\,d\nu(a,b),
\]

with

\[
q_{a,b}(\gamma,d)
=
\frac12\log
\frac{(\gamma-b)^2+(a+d)^2}
     {(\gamma-b)^2+(a-d)^2},
\tag{1}
\]

satisfies

\[
|Q_\nu(\gamma,d)|\ge q
\tag{2}
\]

for almost every `gamma in [T,2T]` and for every `d in [delta,d_0]` for which the mixture is defined. Then

\[
\boxed{
M_*(T,\delta,d_0;q)
\ge
\frac{qT}{2\pi\delta}.
}
\tag{3}
\]

Conversely, for every `A>1`,

\[
\boxed{
M_*(T,\delta,d_0;q)
\le
\frac{q(T+2Ad_0)}
     {2\delta(\pi-2/A)}.
}
\tag{4}
\]

In particular, choosing `A=sqrt(T/d_0)` when `T>d_0` gives

\[
M_*(T,\delta,d_0;q)
\le
\frac{q(T+2\sqrt{Td_0})}
     {2\delta\left(\pi-2\sqrt{d_0/T}\right)},
\tag{5}
\]

and therefore, uniformly in `0<delta<=d_0`,

\[
\boxed{
M_*(T,\delta,d_0;q)
\sim
\frac{qT}{2\pi\delta}
\qquad (T/d_0\to\infty).
}
\tag{6}
\]

Thus the optimal source-independent finite-TV price for a fixed Blaschke count quantum on a dyadic height window and a depth window whose shallow endpoint is `delta` is `Theta(T/delta)`, with sharp leading constant `1/(2 pi)`. Arbitrary coupling of scale `a` and vertical center `b` does not beat this order.

An immediate corollary is stronger than the finite-depth statement: on any target-height interval of positive length, a fixed count quantum that is required uniformly for **arbitrarily shallow** depths `d>0` cannot be produced by any finite-TV translated Blaschke mixture. The required TV diverges at least like `1/d`.

No improved simple-critical-zero proportion and no RH conclusion are claimed.

## 1. Lower budget from the exact vertical area law

WI-411 established the exact single-probe identity

\[
\int_{\mathbb R}q_{a,b}(\gamma,d)\,d\gamma
=2\pi\min(a,d)
\le 2\pi d,
\tag{7}
\]

and consequently, for every finite signed or complex probe measure,

\[
\int_{\mathbb R}|Q_\nu(\gamma,d)|\,d\gamma
\le 2\pi d\,\|\nu\|_{\rm TV}.
\tag{8}
\]

The new point is to apply this area budget to a **depth-independent** count quantum at the shallow endpoint. If (2) holds throughout the depth interval, then at `d=delta`,

\[
qT
\le
\int_T^{2T}|Q_\nu(\gamma,\delta)|\,d\gamma
\le
2\pi\delta\,\|\nu\|_{\rm TV}.
\]

This proves (3). Unlike the `Omega(T)` lower bound in WI-411 for a target of the form `c d`, the defect depth no longer cancels. A fixed count quantum therefore incurs a reciprocal shallow-depth tariff.

The argument does not assume that `a` and `b` are independent, that the coefficient measure is positive, or that the horizontal scale is fixed. It prices the full two-parameter finite-TV mixture class directly through total variation.

More generally, if `I` is any interval of length `L` and the same mixture obeys `|Q_nu(gamma,delta)|>=q` almost everywhere on `I`, then

\[
\|\nu\|_{\rm TV}
\ge \frac{qL}{2\pi\delta}.
\tag{9}
\]

Letting `delta downarrow 0` proves the all-shallow-depth impossibility on every fixed positive-length height interval.

## 2. A matching construction up to an asymptotically sharp boundary collar

The lower bound is not an artifact of the total-variation estimate. A positive mixture with one horizontal scale and a continuum of vertical centers attains the same leading constant.

Fix

\[
a=d_0.
\]

For `0<d<=a`, put `x=gamma-b`. Away from the removable/singular endpoint convention at `x=0,d=a`, differentiation of (1) gives

\[
\frac{\partial}{\partial d}q_{a,b}(\gamma,d)
=
\frac{a+d}{x^2+(a+d)^2}
+
\frac{a-d}{x^2+(a-d)^2}
\ge0.
\tag{10}
\]

Hence a lower bound proved at `d=delta` persists for every `d in [delta,d_0]`.

At the shallow endpoint, (7) gives full mass `2 pi delta` because `a=d_0>=delta`. We only need to quantify how much of this mass is captured by a finite vertical collar. From `log(1+u)<=u` for `u>=0`,

\[
q_{a,0}(x,\delta)
=
\frac12\log\left(
1+
\frac{4a\delta}{x^2+(a-\delta)^2}
\right)
\le
\frac{2a\delta}{x^2}
\qquad (x\ne0).
\tag{11}
\]

Let

\[
R=Aa,
\qquad A>1.
\]

Then

\[
\int_{|x|>R}q_{a,0}(x,\delta)\,dx
\le
4a\delta\int_R^\infty\frac{dx}{x^2}
=
\frac{4\delta}{A},
\]

so

\[
\int_{-R}^{R}q_{a,0}(x,\delta)\,dx
\ge
2\delta\left(\pi-\frac2A\right).
\tag{12}
\]

Now take the positive measure

\[
d\nu(a',b)
=
c\,\delta_a(da')\,
\mathbf 1_{[T-R,\,2T+R]}(b)\,db,
\tag{13}
\]

where

\[
c
=
\frac{q}{2\delta(\pi-2/A)}.
\tag{14}
\]

For every `gamma in [T,2T]`, the `b`-support in (13) contains `[gamma-R,gamma+R]`. Translation invariance of (1) and (12) therefore give

\[
Q_\nu(\gamma,\delta)
\ge
c\int_{-R}^{R}q_{a,0}(x,\delta)\,dx
\ge q.
\tag{15}
\]

By (10), (15) holds for every `d in [delta,d_0]`. The measure is positive, so its total variation is simply its mass:

\[
\|\nu\|_{\rm TV}
=c(T+2R)
=
\frac{q(T+2Ad_0)}
     {2\delta(\pi-2/A)}.
\tag{16}
\]

This proves (4).

For `T>d_0`, choosing `A=sqrt(T/d_0)` makes the collar width `R=sqrt(Td_0)=o(T)` as `T/d_0` grows while `A` tends to infinity. Substitution gives (5). Dividing (5) by the lower bound (3) shows that the ratio tends to one, proving (6).

The construction also shows why the reciprocal-depth price is real rather than a weakness of the lower proof. At depth `delta`, every probe has at most `2 pi delta` vertical response area, and a near-optimal family simply tiles the target-height window with almost all of that available area while paying only a sublinear boundary collar.

## 3. Relation to the previous Blaschke barriers

WI-411 priced vertical coverage for a response proportional to depth and obtained a sharp `Theta(T)` TV budget. The present count-coercive target replaces `c d` by a fixed `q`; the exact area law therefore upgrades the tariff from `Theta(T)` to `Theta(T/delta)`.

WI-412--WI-414 addressed a different axis: centered scale mixing. WI-412 showed that Haar measure in logarithmic scale gives a depth-independent count quantum but has infinite total scale mass; WI-413 proved exact-Haar uniqueness for constant centered response in the tempered class; WI-414 showed that even one-sided global centered coercivity forces Haar-rate lower Beurling density for translation-bounded scale measures.

The present theorem couples the two probe parameters instead of treating height and scale separately. It shows that restricting attention to a **finite** depth interval does not make continuum-uniform height coercivity cheap. Even though the log-depth interval is finite, the shallow endpoint imposes a stronger `1/delta` area bottleneck once the same source-independent detector must cover a height interval of length `T`.

There is no contradiction with the logarithmic-scale Haar picture. Scale averaging can redistribute the response among horizontal scales, but at the shallow depth `delta` the total response area in the vertical target variable remains bounded by `2 pi delta` per unit coefficient TV, independently of the scale. The vertical area law therefore survives arbitrary scale mixing.

## 4. Scope: what this closes and what remains open

The barrier is exact for the stated architecture: finite-TV **linear** mixtures of the translated half-plane Blaschke charges (1), with one source-independent coefficient measure required to work throughout the continuum target rectangle

\[
[T,2T]\times[\delta,d_0].
\]

Within that class, neither vertical translation, scale mixing, nor arbitrary coupling between the two can lower the asymptotic `T/delta` budget. In particular, no finite-TV mixture can deliver a fixed count quantum on a positive-length height interval all the way down to arbitrarily shallow off-line displacement.

Several escapes remain genuinely outside the theorem. The `L^1(d gamma)` argument still does not control an oracle-like measure singularly adapted to the discrete ordinates of the actual exceptional zeros; a measure-zero target set can evade a continuum area bound. Such targeting would need a non-circular zeta-side construction. The result also does not rule out nonlinear observables, generalized source distributions that are not finite measures, renormalized infinite-budget identities, or new arithmetic/spectral input that independently supplies a positive lower depth cutoff.

Most importantly, this is a source-budget obstruction, not yet a defect-to-zero theorem. To convert it into exclusion of off-critical zeros one would still need an independently justified upper bound showing that the admissible zeta-side source budget grows strictly slower than the `T/delta` tariff in the relevant regime, or another invariant that prevents the shallow-depth escape directly.

## 5. Prior-art and novelty audit

The load-bearing identity (7) and its finite-TV consequence (8) are already established in WI-411. They are elementary half-plane Blaschke/Poisson-kernel calculus, not a new harmonic-analysis theorem. Classical literature on logarithmic integral means of half-plane Blaschke products includes G. V. Mikayelyan and F. V. Hayrapetyan, *On integral logarithmic means of Blaschke products for a half-plane*, Proceedings of Yerevan State University A 52:3 (2018), DOI `10.46991/PYSU:A/2018.52.3.166`. Classical work on translates of Poisson kernels includes J. Bruna and M. Melnikov, *On translates of the Poisson kernel and zeros of harmonic functions*, Bulletin of the London Mathematical Society 39 (2007), 317--326, DOI `10.1112/blms/bdl039`.

WI-414 already records Gabardo's convolution/Beurling-density theorem as direct prior art for global one-sided centered coercivity. The present proof does not need that theorem: its lower bound is the exact vertical area law, and its upper bound is an explicit positive translated-probe construction plus the elementary tail estimate (11).

A targeted prior-art search around half-plane Blaschke logarithmic means, Poisson-kernel translates, Beurling density, and scale/translation mixtures located the classical sources above but did not locate this exact two-parameter finite-window `T/delta` minimization law. That negative search is not evidence of priority, and no priority claim is made. The line-specific contribution recorded here is the exact asymptotic budget consequence for the Mathia defect-to-zero architecture and the observation that the finite-depth/height-scale-coupling escape left after WI-414 still pays the reciprocal shallow-depth tariff.

## Consequence

For source-independent linear translated-Blaschke detectors, the continuum count-coercivity budget is now quantitatively rigid in both height and depth:

\[
\boxed{
\text{height length }T
\quad+\quad
\text{shallow depth }\delta
\quad\Longrightarrow\quad
\text{TV cost }\sim\frac{qT}{2\pi\delta}.
}
\]

This closes the finite-depth-window plus arbitrary `(a,b)` coupling escape **within the finite-TV continuum-coverage model**. A viable zero-defect bootstrap must therefore leave that model, target the discrete exceptional set through independently available zeta information, tolerate a source budget of order `T/delta`, or obtain new arithmetic/spectral information that prevents `delta` from becoming arbitrarily small.