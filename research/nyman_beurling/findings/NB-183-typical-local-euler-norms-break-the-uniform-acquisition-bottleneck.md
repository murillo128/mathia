# NB-183 — Typical local Euler norms break the uniform acquisition bottleneck

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-SPECIFIC + MEAN-SQUARE + CAPPED-POISSON + HEIGHT-SELECTIVE + NB-182-FREQUENCY-RESOLUTION`.

`NB-182` prices the genuine non-Hilbert Euler scalar family by its charged Wiener exposure. Its remaining source-side question is whether the actual height-specific capped-Poisson norm of

\[
K_{a,t}(u):=-\frac{\zeta'}{\zeta}(1+a+i(t+u)),
\qquad |u|\le B,
\]

is commonly much smaller than the uniform high-ordinate majorant

\[
H_T=\min\left\{\frac1a,\frac{\log T}{\log\log T}\right\}.
\]

It is. In the broad regime `T a^4 -> infinity`, the local capped-Poisson seminorm has bounded mean square on a dyadic height block. Consequently, when `a -> 0`, it is `o(a^{-1/2})` on density one. Since the Euler Wiener exposure is `W(a) asymp 1/a`, the resulting charged acquisition gain beats the `sqrt N` threshold for the full generic packing dimension `N asymp 1/a` on density-one heights.

Thus the square crossover from `NB-182` is a limitation of the **uniform** source bound, not a typical-height acquisition barrier. What remains is no longer to find enough scalar Euler exposure at most heights, but to turn that exposure into coherent high-rank phase reuse and then connect it back to the Nyman target. The ultra-thin range `T a^4 = O(1)` remains outside this argument.

## Claim

Fix `A,B>0`. For `T` sufficiently large and `0<a<=A`, put

\[
d_a(u,v):=\min\left\{1,\frac{|u-v|}{a}\right\}
\]

and define the actual local capped-Poisson source seminorm

\[
\mathcal H_{a,B}(t)
:=
\sup_{\substack{u,v\in[-B,B]\\u\ne v}}
\frac{|K_{a,t}(u)-K_{a,t}(v)|}{d_a(u,v)}.
\]

This is the relevant dual seminorm for the zero-mass signed Jordan transport of `NB-167`; additive constants in `K_{a,t}` are invisible.

Then

\[
\boxed{
\int_T^{2T}\mathcal H_{a,B}(t)^2\,dt
\ll_{A,B}
T+a^{-4}.
}
\]

Equivalently,

\[
\boxed{
\frac1T\int_T^{2T}\mathcal H_{a,B}(t)^2\,dt
\ll_{A,B}
1+\frac1{Ta^4}.
}
\]

Hence for every `R>0`,

\[
\boxed{
\frac1T
\left|
\left\{t\in[T,2T]:\mathcal H_{a,B}(t)>R\right\}
\right|
\ll_{A,B}
\frac1{R^2}
\left(1+\frac1{Ta^4}\right).
}
\]

In particular, if `a=a_T -> 0` and

\[
Ta_T^4\to\infty,
\]

then

\[
\boxed{
\sqrt{a_T}\,\mathcal H_{a_T,B}(t)\to0
\quad\text{in relative measure on }[T,2T].
}
\]

More quantitatively, for every fixed `eta>0`,

\[
\frac1T
\left|
\left\{t:\mathcal H_{a_T,B}(t)>\eta a_T^{-1/2}\right\}
\right|
\ll_{A,B,\eta}
a_T\left(1+\frac1{Ta_T^4}\right)
=o(1).
\]

A convenient explicit density-one threshold is

\[
R_T=a_T^{-1/4}.
\]

Then

\[
\frac1T
\left|
\left\{t:\mathcal H_{a_T,B}(t)>a_T^{-1/4}\right\}
\right|
\ll_{A,B}
a_T^{1/2}\left(1+\frac1{Ta_T^4}\right)
=o(1).
\]

## Consequence for the NB-182 acquisition threshold

`NB-182` shows that the charged absolute Euler exposure satisfies

\[
W(a)\asymp \frac1a.
\]

At a height `t`, replacing the uniform majorant `H_T` by the actual local dual cost gives the available scalar acquisition ratio

\[
\kappa_{a,B}(t)
\asymp
\frac{W(a)}{\mathcal H_{a,B}(t)}
\asymp
\frac1{a\,\mathcal H_{a,B}(t)}.
\]

The full generic Poisson packing dimension from `NB-179`--`NB-182` is

\[
N(a)\asymp\frac1a,
\qquad
\sqrt{N(a)}\asymp a^{-1/2}.
\]

Therefore

\[
\frac{\kappa_{a,B}(t)}{\sqrt{N(a)}}
\asymp
\frac1{\sqrt a\,\mathcal H_{a,B}(t)}.
\]

Under `a_T -> 0` and `T a_T^4 -> infinity`, the previous density statement yields

\[
\boxed{
\frac{\kappa_{a_T,B}(t)}{\sqrt{N(a_T)}}\to\infty
\quad\text{in relative measure on }[T,2T].
}
\]

For the explicit choice `R_T=a_T^{-1/4}`, a density-`1-o(1)` set of heights satisfies

\[
\mathcal H_{a_T,B}(t)\le a_T^{-1/4},
\]

and hence

\[
\boxed{
\kappa_{a_T,B}(t)
\gg
a_T^{-3/4}
=
a_T^{-1/4}\sqrt{N(a_T)}.
}
\]

Thus the source-side acquisition budget is not merely at threshold: on most heights it is supercritical by a power of the Poisson packing scale.

This includes all logarithmic and Vinogradov--Korobov widths considered in the preceding high-ordinate analysis. For example, `a_T` of order `log log T/log T` or any fixed negative power of `log T` satisfies `T a_T^4 -> infinity` overwhelmingly.

## Derivation

### 1. The local transport seminorm reduces to two short-interval suprema

For `|u-v|>=a`, the denominator in `d_a` is one, so

\[
|K_{a,t}(u)-K_{a,t}(v)|
\le
2\sup_{|w|\le B}|K_{a,t}(w)|.
\]

For `|u-v|<a`, the mean-value theorem gives

\[
\frac{|K_{a,t}(u)-K_{a,t}(v)|}{|u-v|/a}
\le
a\sup_{|w|\le B}|K'_{a,t}(w)|.
\]

Consequently

\[
\mathcal H_{a,B}(t)
\le
2\sup_{|w|\le B}|K_{a,t}(w)|
+
a\sup_{|w|\le B}|K'_{a,t}(w)|.
\]

This deterministic reduction is deliberately crude but source-faithful: it keeps exactly the capped metric used by the Jordan transport in `NB-167`.

### 2. Montgomery--Vaughan gives the derivative budgets

For `Re s=1+a>1`, absolute convergence gives

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
\]

The `j`-th vertical derivative has Dirichlet coefficients, up to unit complex factors,

\[
b_{j,n}
=
\frac{\Lambda(n)(\log n)^j}{n^{1+a}}.
\]

For each fixed `j=0,1,2`,

\[
\sum_{n\ge2}|b_{j,n}|^2
=
\sum_{n\ge2}
\frac{\Lambda(n)^2(\log n)^{2j}}{n^{2+2a}}
\ll_{A,j}1.
\]

For the Montgomery--Vaughan endpoint term, use

\[
\Lambda(n)^2\le\Lambda(n)\log n.
\]

Then

\[
\sum_{n\ge2}n|b_{j,n}|^2
\le
\sum_{n\ge2}
\frac{\Lambda(n)(\log n)^{2j+1}}{n^{1+2a}}
\ll_{A,j}
a^{-(2j+2)}.
\]

The last estimate is the standard pole-size bound obtained by differentiating `-zeta'/zeta` a fixed number of times at `1+2a`; for `a` bounded away from zero it is absorbed into the `A`-dependent constant.

The same Montgomery--Vaughan mean-value theorem already used in `NB-168` therefore gives, after harmlessly enlarging the height interval by `B`,

\[
I_j(T,a)
:=
\int_{T-B}^{2T+B}
\left|
\frac{d^j}{dt^j}
\left(-\frac{\zeta'}{\zeta}(1+a+it)\right)
\right|^2dt
\ll_{A,B,j}
T+a^{-(2j+2)}.
\]

Thus

\[
I_0\ll T+a^{-2},
\qquad
I_1\ll T+a^{-4},
\qquad
I_2\ll T+a^{-6}.
\]

### 3. One-dimensional Sobolev converts average derivative energy into local suprema

On the fixed interval `[-B,B]`, the elementary `H^1 -> L^infinity` inequality gives

\[
\sup_{|u|\le B}|F(u)|^2
\ll_B
\int_{-B}^B\bigl(|F(u)|^2+|F'(u)|^2\bigr)\,du.
\]

Apply this first to `F(u)=K_{a,t}(u)` and then to `F(u)=K'_{a,t}(u)`, and integrate over `t in [T,2T]`. Fubini merely shifts the vertical variable by `u`, so

\[
\int_T^{2T}
\sup_{|u|\le B}|K_{a,t}(u)|^2dt
\ll_{A,B}
I_0+I_1
\ll
T+a^{-4},
\]

while

\[
a^2
\int_T^{2T}
\sup_{|u|\le B}|K'_{a,t}(u)|^2dt
\ll_{A,B}
a^2(I_1+I_2)
\ll
T+a^{-4}.
\]

Combining these estimates with the deterministic reduction proves

\[
\int_T^{2T}\mathcal H_{a,B}(t)^2dt
\ll_{A,B}T+a^{-4}.
\]

Chebyshev gives all stated density consequences.

## What this resolves from NB-182

`NB-182` left two possibilities above its uniform square crossover:

1. the actual Euler source norm could remain generically as expensive as the worst-case high-ordinate bound, making source acquisition itself the obstruction; or
2. vertical arithmetic phases could cancel at typical heights, leaving coherent rank/phase reuse as the real obstruction.

The mean-square estimate chooses the second alternative throughout `T a^4 -> infinity`. The actual local capped-Poisson norm is tight in `L^2` once the quartic finite-height error is negligible, whereas the uniform majorant `H_T` can grow like `log T/log log T`. In particular, the uniform condition

\[
aH_T^2=O(1)
\]

is not a typical-height necessity for crossing the non-Hilbert acquisition threshold.

This is a source-specific gain, not a change of dual geometry. The metric remains the same capped Poisson metric, and the Wiener exposure remains charged with the true Euler amplitudes. The improvement comes only from vertical phase cancellation in the actual zeta logarithmic derivative.

## Self-adversarial review and limits

### This does not construct a phase code

A large scalar acquisition ratio says that the source budget is sufficient to pay for a hypothetical dense code. It does **not** show that a common family of source-natural probes has `Theta(N)` effective rank, that its singular values stay at Hadamard scale, or that the good heights can be selected coherently for the Nyman approximation problem.

So the surviving obstruction is now sharper: one must prove coherent phase reuse/rank on the same height set, rather than merely exhibit many individually affordable Euler coordinates.

### Density one is not pointwise control

The conclusion is a dyadic relative-measure statement. It does not exclude a sparse exceptional sequence of heights at which `mathcal H_{a,B}` is as large as the uniform bound. Any argument that selects its height adversarially can still live entirely inside that exceptional set.

### The quartic width is a method boundary, not a claimed arithmetic phase transition

The term `a^{-4}` comes from applying fixed-interval Sobolev to `K` and then Montgomery--Vaughan to its first derivative; controlling the derivative supremum introduces `K''` and, after the prefactor `a^2`, again leaves `a^{-4}`. Nothing here proves that `a ~ T^{-1/4}` is intrinsic.

A sharper maximal Dirichlet-series estimate could plausibly push the finite-height threshold below `T^{-1/4}`. The regime

\[
Ta^4=O(1)
\]

must therefore remain open rather than being advertised as a source obstruction.

### The mean-square argument is generic; its acquisition interpretation is source-specific

The analytic engine is classical: one-dimensional Sobolev plus the Montgomery--Vaughan mean-value theorem for Dirichlet series. The source-specific content is that the Euler coefficients of `-zeta'/zeta` have the exact derivative budgets above, that `NB-167` identifies their local oscillation with capped Jordan transport, and that `NB-182` converts the resulting local seminorm into charged Wiener acquisition gain.

A prior-art search around mean-square bounds for zeta logarithmic derivatives and short-interval maxima found the classical neighboring literature, including mean-square log-derivative work and pointwise bounds for `zeta'/zeta`, but no statement matching this capped-Poisson local seminorm or its Nyman acquisition consequence. No new external theorem is load-bearing here, so `SOURCES.md` does not need a new dependency.

## Updated frontier

For `a_T -> 0` with `T a_T^4 -> infinity`, the first branch of the post-`NB-182` target is settled positively: **height-selective source cancellation is abundant enough to beat the full generic `sqrt N` acquisition threshold on density-one heights**.

The next source-side question is therefore not whether enough charged Euler exposure exists, but whether that exposure can be organized into a source-natural response matrix with enough coherent rank on a common good-height set. A negative theorem here would have to bound nuclear growth or effective rank using arithmetic phase relations that survive the true Euler amplitude budget; a positive theorem would have to construct those relations without falling back to independently normalized weak frequency channels.

Separately, the ultra-thin finite-height regime `T a_T^4=O(1)` remains unresolved and may admit a sharper maximal estimate.