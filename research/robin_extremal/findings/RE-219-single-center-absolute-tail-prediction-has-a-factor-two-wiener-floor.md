# RE-219 — Single-center absolute-tail prediction has a factor-two Wiener floor

**Status:** `EXACT-DERIVED + CONTINUUM-VERTICAL-EULER + OFF-CENTER-POLYNOMIAL-PREDICTION + WIENER-NORM-REPRESENTATION-LOWER-BOUND + PRIOR-ART-AUDIT`.

**Parent findings:** RE-216, RE-217, RE-218.

RE-217 isolates the global separated-prediction constant `C_sep` and RE-218 gives the current explicit interval

\[
1\le C_{\rm sep}\le 5.996390.
\]

The upper endpoint comes from the single-center negative-binomial expansion introduced in RE-216 and explicitly retuned in RE-218. That construction has three visible parameters: the observed arc half-width `alpha`, a positive real expansion center `a`, and a truncation ratio `lambda`. It was not known whether further parameter tuning inside the same proof architecture could in principle drive the Wiener exponent all the way to the unit lower floor.

It cannot. Consider the whole class obtained from

\[
z^{-m}
=a^{-m}\left(1-\frac{a-z}{a}\right)^{-m}
=\sum_{k\ge0}\binom{m+k-1}{k}a^{-m-k}(a-z)^k,
\tag{1}
\]

on an arc `|arg z|<=alpha`, with the discarded tail controlled by the **sum of absolute values** of its negative-binomial terms, exactly as in RE-216--RE-218. Allow any positive real center `a` for which the expansion contracts on the whole arc, and allow the parameters to vary asymptotically. Every such predictor with vanishing uniform tail error has leading Wiener exponent at least two:

\[
\boxed{
\liminf\frac{\log\|\mu_T\|_{TV}}{HT}\ge2.
}
\tag{2}
\]

If `C_(1c,abs)` denotes the optimal leading exponent in this single-center absolute-tail subclass, then

\[
\boxed{
2\le C_{1c,abs}\le5.996390.
}
\tag{3}
\]

The upper bound is RE-218. The lower bound is new and is **representation-local**: it does not improve the global RE-217 lower bound `C_sep>=1`. Its consequence is instead structural. No further scalar retuning of the RE-216/RE-218 center, arc width or truncation depth can close the factor-six-to-one prediction gap. Reaching a rate below two already requires leaving at least one part of this architecture: a different approximation geometry, several centers, or a tail argument that exploits complex cancellation rather than absolute domination.

## 1. Absolute-tail convergence forces truncation past a positive exponential mode

Put

\[
\delta=\frac{\alpha}{T},\qquad
m=\left\lceil\frac{H}{\delta}\right\rceil,
\qquad
z=e^{-i\delta t},
\qquad |t|\le T.
\tag{4}
\]

For a positive real center `a`, write

\[
r
:=\max_{|\theta|\le\alpha}
\frac{|a-e^{-i\theta}|}{a}
=
\frac{\sqrt{a^2+1-2a\cos\alpha}}{a}.
\tag{5}
\]

Uniform convergence of (1) on the full arc requires `r<1`. It is convenient to put

\[
u:=\frac1a.
\tag{6}
\]

Then

\[
r^2=1+u^2-2u\cos\alpha.
\tag{7}
\]

Thus `r<1` implies

\[
0<\alpha<\frac\pi2,
\qquad
0<u<2\cos\alpha.
\tag{8}
\]

Truncate (1) at

\[
N=\lambda m+O(1).
\tag{9}
\]

At `k=lambda m+O(1)`, Stirling gives the exponential rate of the corresponding absolute tail term as

\[
\tau(\lambda)
=-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log r.
\tag{10}
\]

The consecutive absolute-tail ratio tends to

\[
r\frac{1+\lambda}{\lambda}.
\tag{11}
\]

Hence the absolute terms attain their exponential mode at

\[
\lambda_p=\frac{r}{1-r}.
\tag{12}
\]

At this point (10) simplifies exactly to

\[
\tau(\lambda_p)=-\log\bigl(a(1-r)\bigr).
\tag{13}
\]

This quantity is strictly positive for every nondegenerate arc satisfying (8). If `a<=1`, then `a(1-r)<1` immediately. If `a>1`, positive `alpha` gives

\[
r>1-\frac1a,
\]

so again `a(1-r)<1`. Moreover

\[
\tau''(\lambda)=-\frac1{\lambda(1+\lambda)}<0,
\tag{14}
\]

while `tau(lambda)->-infinity` as `lambda->infinity`. Consequently there is a unique larger zero

\[
\lambda_0>\lambda_p
\tag{15}
\]

of `tau`. Any proof that bounds the discarded tail by summing its absolute values and obtains a vanishing uniform remainder must truncate asymptotically beyond this zero. Truncating before the mode leaves an exponentially positive absolute term later in the discarded tail; truncating between the mode and `lambda_0` leaves the first omitted scale exponentially positive.

This is the first source of the representation floor: the polynomial must be carried beyond the natural negative-binomial mode before absolute-tail control starts to decay.

## 2. At the tail boundary the Wiener exponent has an exact one-parameter form

Expanding `(a-z)^k` into nonnegative powers of `z`, all contributions to a fixed output degree have the same sign, as in RE-216--RE-218. Therefore there is no hidden cancellation in the coefficient `ell^1` norm. Its exponential rate at `N=lambda m+O(1)` is

\[
\nu(\lambda)
=-\log a
+(1+\lambda)\log(1+\lambda)
-\lambda\log\lambda
+\lambda\log\frac{a+1}{a}.
\tag{16}
\]

Since

\[
\nu'(\lambda)
=
\log\left(
\frac{a+1}{a}\frac{1+\lambda}{\lambda}
\right)>0,
\tag{17}
\]

using a deeper truncation can only increase the leading Wiener exponent. The cheapest absolutely convergent truncation is therefore approached from above at `lambda=lambda_0`.

At the boundary `tau(lambda_0)=0`, subtracting (10) from (16) gives

\[
\nu(\lambda_0)
=
\lambda_0
\log\frac{(a+1)/a}{r}.
\tag{18}
\]

Because `lambda_0>r/(1-r)`,

\[
\nu(\lambda_0)
>
\frac{r}{1-r}
\log\frac{1+u}{r}.
\tag{19}
\]

The logarithm is positive: `(1+u)^2-r^2=2u(1+cos alpha)>0`. Applying the elementary strict inequality

\[
\log x>\frac{2(x-1)}{x+1},
\qquad x>1,
\tag{20}
\]

to `x=(1+u)/r` yields

\[
\nu(\lambda_0)
>
2J(\alpha,u),
\tag{21}
\]

where

\[
J(\alpha,u)
:=
\frac{r}{1-r}
\frac{1+u-r}{1+u+r}.
\tag{22}
\]

Thus it remains only to compare this elementary geometric quantity with the observed arc width.

## 3. The arc geometry supplies the factor two

We prove

\[
\boxed{
J(\alpha,u)\ge2\tan\frac\alpha2>\alpha
}
\tag{23}
\]

throughout the contraction domain (8).

Fix `alpha` and let `u` vary in `(0,2 cos alpha)`, with `r` defined by (7). The function `J` is continuous. At the right endpoint `u->2 cos alpha`, one has `r->1` and therefore

\[
J(\alpha,u)\longrightarrow+\infty.
\tag{24}
\]

At the left endpoint `u->0`, direct expansion gives

\[
J(\alpha,u)
\longrightarrow
\frac{1+\cos\alpha}{2\cos\alpha}.
\tag{25}
\]

This is at least `2 tan(alpha/2)`, because

\[
(1+\cos\alpha)^2
\ge4\cos\alpha
\ge4\cos\alpha\sin\alpha.
\tag{26}
\]

It remains to inspect an interior stationary point. Differentiating `log J` with respect to `u` and eliminating `cos alpha` through (7) reduces the stationary equation to

\[
u^2+2r(r-1)u-(1-r)^2=0.
\tag{27}
\]

The positive solution is

\[
u=(1-r)\left(r+\sqrt{1+r^2}\right).
\tag{28}
\]

Writing

\[
s:=\sqrt{1+r^2},
\tag{29}
\]

substitution into (7) gives

\[
\cos\alpha=s-r^2,
\qquad
J=\frac{r(s+2)}{3-r^2}.
\tag{30}
\]

A direct algebraic comparison with `tan(alpha/2)^2=(1-cos alpha)/(1+cos alpha)` now gives

\[
J^2-4\tan^2\frac\alpha2
=
\frac{(s-1)^3(s+2)^2(5s-1)}
{r^2(3-r^2)^2}
>0.
\tag{31}
\]

So every possible interior minimum is strictly above `2 tan(alpha/2)`, while the two boundary limits satisfy the same lower bound. This proves the first inequality in (23). The second is the standard strict inequality `tan x>x` for `x>0`.

Combining (19), (21), and (23),

\[
\nu(\lambda_0)>2\alpha.
\tag{32}
\]

Finally, from (4),

\[
m=\frac{HT}{\alpha}+O(1).
\tag{33}
\]

Hence every absolutely convergent truncation in this family satisfies

\[
\frac{\log\|\mu_T\|_{TV}}{HT}
\ge
\frac{\nu(\lambda_0)}{\alpha}+o(1)
>2+o(1).
\tag{34}
\]

Taking the infimum over admissible parameter choices proves the lower half of (3). The pointwise argument also covers asymptotically varying real centers or arc widths: degeneration can approach the constant two, but cannot cross it within this absolute-tail certificate.

## 4. Stress tests and representation boundary

The first possible objection is cancellation in the discarded analytic tail. The theorem deliberately does **not** exclude it. RE-216 and RE-218 certify their remainder by absolute negative-binomial terms and a consecutive-term ratio; (2) prices exactly that architecture. A cancellation-sensitive contour, minimax or complex approximation may have a smaller remainder for the same polynomial coefficients and lies outside the present lower bound.

The second possible escape is moving the expansion center through `a=1`. The proof already allows every positive real `a` satisfying the full-arc contraction `r<1`, including admissible centers below one. Thus the factor two is not an artifact of the `a>1` choices used in RE-216--RE-218. Complex centers, several centers and non-binomial bases are not covered.

The third possible escape is to let the parameters depend on `T`. Equations (19)--(34) are pointwise in every admissible triple `(alpha,a,lambda)` before taking the asymptotic limit. Parameter drift can at most approach the factor-two boundary. Rounding `m` and `N` changes logarithmic rates by `o(HT)`, and the exact DC renormalization used in RE-216--RE-218 is `1+o(1)` once the tail error vanishes.

The fourth check is source dependence. None enters the proof. The bound concerns the pure exponential predictor before ordinary-prime realization, and therefore leaves RE-208's `{0,1,2}` carrier construction, KV fidelity and half-mass source capacity unchanged. This is a representation obstruction, not evidence that prime sources themselves require exponent two.

Causal prediction of band-limited data, Chebyshev/Newton prediction, finite-memory polynomial prediction and incomplete-polynomial approximation are classical neighboring approximation theories. The prior-art audit found no need for an external theorem in the argument above: (1)--(34) are elementary consequences of the exact RE-216 expansion, Stirling asymptotics and one-variable algebra. No novelty is claimed for one-sided polynomial prediction itself, and no new load-bearing source is added to `SOURCES.md`.

## Research consequence

The global live interval remains

\[
1\le C_{\rm sep}\le5.996390.
\tag{35}
\]

RE-219 does not raise its lower endpoint. It instead removes an entire class of prospective incremental improvements: **single-positive-real-center negative-binomial prediction with absolute-tail control cannot achieve Wiener rate below two**, regardless of how its three scalar parameters are retuned.

This makes the next constructive obligation sharper than after RE-218. Improving `5.996390` numerically within the same family is possible in principle but cannot solve even half of the remaining leading-order gap. A serious route toward `C_sep=1` must introduce genuinely different prediction geometry or exploit analytic cancellation that the absolute-tail proof discards. Conversely, a future global lower bound above one must use information beyond this representation-local obstruction; the factor-two theorem cannot be promoted into a statement about arbitrary separated measures.