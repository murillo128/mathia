# NB-187 — Poisson-scale prime codes carry vanishing Euler-Wiener mass

**Date:** 2026-09-17  
**Status:** `DERIVED + SOURCE-FIDELITY + EULER-WIENER + PRIME-NUMBER-THEOREM + CHANNEL-CARDINALITY-MISMATCH + NB-186-REFINEMENT`.

`NB-186` shows that `N asymp 1/a` prime phases can already have raw nuclear mass of order `N^(3/2)` on simultaneously acquisition-good heights. The unresolved step is amplitude-balanced extraction: those columns must be charged with the actual Euler amplitudes and the Wiener/capped-Poisson acquisition currency of `NB-182`.

There is a sharper mismatch than raw amplitude decay. The normalized Euler-Wiener budget of `NB-182` has a definite limiting distribution on the logarithmic frequency scale `u=a log n`. Its mass lives at `u=Theta(1)`, hence at arithmetic labels `n=exp(Theta(1/a))`. By contrast, the first `N asymp 1/a` primes used by `NB-186` satisfy `a log p_N -> 0`. They therefore occupy an asymptotically negligible corner of the actual source budget.

More precisely, if

\[
M_a(\lambda):=\max\{2,a\lambda\},
\qquad
b_a(n):=\frac{\Lambda(n)}{n^{1+a}}M_a(\log n),
\qquad
\mathcal W(a):=\sum_{n\ge2}b_a(n),
\]

then

\[
\boxed{
a\mathcal W(a)\longrightarrow 2+e^{-2}.
}
\tag{1}
\]

After normalization, the pushforward of the Euler-Wiener mass by `n -> a log n` converges to the probability density

\[
\boxed{
\frac{e^{-u}\max\{2,u\}}{2+e^{-2}}\,du,
\qquad u>0.
}
\tag{2}
\]

Prime powers of exponent at least two contribute only `O(1)` to `mathcal W(a)`, so the same limiting law is carried asymptotically by the prime channels themselves.

For the first `N` primes, whenever `a log p_N -> 0`, their normalized Wiener mass is

\[
\boxed{
\Theta_N(a)
:=
\frac{1}{\mathcal W(a)}
\sum_{j\le N}
\frac{\log p_j}{p_j^{1+a}}M_a(\log p_j)
=
\left(\frac{2}{2+e^{-2}}+o(1)\right)a\log p_N.
}
\tag{3}
\]

In particular, for the full Poisson packing scale `N asymp 1/a`, the prime number theorem gives

\[
\boxed{
\Theta_N(a)
=
\left(\frac{2}{2+e^{-2}}+o(1)\right)
a\log\frac1a
\longrightarrow0.
}
\tag{4}
\]

This is not special to choosing the first primes. Up to the irrelevant finite swap between `2` and `3`, the prime-channel weights `b_a(p)` decrease with `p`. Hence any set of `O(1/a)` individual prime channels has normalized Euler-Wiener mass `O(a log(1/a))`. Conversely, any set of prime channels carrying a fixed positive fraction of `mathcal W(a)` must contain exponentially many channels: for every fixed `delta>0` there is `c_delta>0` such that

\[
\boxed{
\sum_{p\in S_a} b_a(p)\ge\delta\mathcal W(a)
\quad\Longrightarrow\quad
|S_a|\ge \exp(c_\delta/a)
}
\tag{5}
\]

for all sufficiently small `a`.

Thus `NB-186` has established genuine growing **phase** rank, but that rank sits inside a block carrying vanishing source mass. A direct Wiener-faithful isolation and renormalization of that `N asymp 1/a` prime block costs the reciprocal factor

\[
\boxed{
\Theta_N(a)^{-1}
asymp
\frac{1}{a\log(1/a)},
}
\tag{6}
\]

which is asymptotically larger than the generic `sqrt N asymp a^{-1/2}` dense-code tariff from `NB-182`. Therefore shell flattening or selection of only Poisson-many individual prime frequencies cannot by itself bridge `NB-186` to a source-faithful `NB-178` certificate. A positive construction must compress and reuse coherently an exponentially larger Euler frequency population before paying the Wiener normalization, rather than merely choosing `O(1/a)` favorable channels.

## Derivation

### 1. PNT gives a scaled logarithmic-frequency law

Let

\[
\mu_a
:=
a\sum_{n\ge2}
\frac{\Lambda(n)}{n^{1+a}}
\delta_{a\log n}.
\tag{7}
\]

The prime number theorem in the Chebyshev form `psi(x)=sum_(n<=x) Lambda(n) ~ x` implies, by Stieltjes partial summation, that for every compactly supported continuous `f` on `(0,infinity)`,

\[
\int f(u)\,d\mu_a(u)
\longrightarrow
\int_0^\infty f(u)e^{-u}\,du.
\tag{8}
\]

Indeed, after the substitution `x=e^(u/a)`, the model measure `d psi(x)=dx` gives exactly `e^{-u}du`; the PNT error is `o(1)` after localization to a compact `u` interval. Chebyshev's bound `psi(x) << x` supplies uniform exponential tails, so (8) extends to functions of at most polynomial growth.

Taking `f(u)=max{2,u}` gives

\[
a\mathcal W(a)
\longrightarrow
\int_0^\infty e^{-u}\max\{2,u\}\,du.
\tag{9}
\]

The integral is elementary:

\[
2\int_0^2e^{-u}du+
\int_2^\infty ue^{-u}du
=2(1-e^{-2})+3e^{-2}
=2+e^{-2},
\]

which proves (1). Applying (8) with `f(u)=max{2,u}g(u)` for bounded continuous `g` proves the weak convergence (2).

### 2. Higher prime powers are lower order

For `k>=2`, use `max{2,ak log p} <= 2+ak log p`. Uniformly for `0<a<=1`,

\[
\sum_p\sum_{k\ge2}
\frac{\log p}{p^{k(1+a)}}
\max\{2,ak\log p\}
\]

is bounded by a constant multiple of

\[
\sum_p\frac{\log p}{p^2(1-p^{-1})}
+
a\sum_p\frac{(\log p)^2}{p^2}(1-p^{-1})^{-2},
\]

which is `O(1)`. Since `mathcal W(a) asymp 1/a`, higher prime powers carry `o(1)` of the normalized budget. This is the arithmetic step that lets the scaled law be read as a prime-channel statement rather than merely a von-Mangoldt statement.

### 3. Poisson-many primes lie at scaled frequency zero

Assume `a log p_N ->0`. Then eventually `M_a(log p_j)=2` for every `j<=N`, and uniformly on this range `p_j^(-a)=1+o(1)`. The classical PNT consequence

\[
\sum_{p\le x}\frac{\log p}{p}
=\log x+O(1)
\tag{10}
\]

therefore yields

\[
\sum_{j\le N} b_a(p_j)
=(2+o(1))\log p_N.
\tag{11}
\]

Combining (11) with (1) proves (3). If `N asymp 1/a`, then `p_N asymp N log N`, so

\[
\log p_N=(1+o(1))\log(1/a),
\]

and (4) follows.

For the maximal-mass statement, note that `2 log x x^(-1-a)` is decreasing for `x>=3` while `a(log x)^2x^(-1-a)` is decreasing throughout the region `a log x>=2`; the two formulas agree at the transition. Thus, apart from a finite initial reorder, the `K` largest prime-channel weights are the first `K` prime weights. Hence any `K=O(1/a)` prime channels obey the same `O(a log(1/a))` normalized-mass bound.

Finally, if `K` prime channels carry a fixed fraction `delta`, the preceding maximal-mass bound forces `a log p_K` to be bounded below by a positive constant depending on `delta`. Thus `p_K>=exp(c_delta/a)`. The PNT relation `p_K asymp K log K` then gives (5), after decreasing `c_delta` if necessary.

## Consequence for NB-186

`NB-186` supplies `N asymp 1/a` heights for which the raw first-prime matrix

\[
P_{ij}=e^{-it_i\log p_j}
\]

has `||P||_* >> N^(3/2)` at the cubic simultaneous-selection scale. Equations (3)--(4) show that exactly those columns carry only `Theta_N(a)=o(1)` of the normalized Euler-Wiener source.

In the Wiener representation of `NB-182`, projecting the normalized scalar Euler source to this prime block produces a convex combination of total coefficient mass `Theta_N(a)`. Renormalizing that projected block to coefficient mass one therefore costs exactly `Theta_N(a)^(-1)` in this coefficient/total-variation currency. Equation (6) is a tariff for this **direct block-isolation strategy**, not a universal lower bound on every possible non-coordinatewise acquisition.

This distinction matters. A successful source-faithful map could in principle aggregate exponentially many weak Euler characters into only `O(1/a)` effective observables and reuse their mass coherently. The present finding does not rule that out. It proves that choosing, flattening, or separately exposing only Poisson-many favorable prime channels cannot carry a positive fraction of the actual Euler-Wiener source.

## Generality audit

**Generality audited.** The weak law (8) is a generic Abelian consequence of a positive coefficient-counting measure with PNT-type asymptotic density; the limiting factor `e^{-u}` comes from the near-pole Laplace scale and `max{2,u}` comes from the capped-Lipschitz acquisition cost. The monotone-cardinality argument is likewise generic once positive channel weights are ordered.

The arithmetic-specific content is that the coefficients are `Lambda(n)`, higher prime powers are negligible in the `1/a` budget, prime channels therefore carry the limiting law, and the raw code of `NB-186` uses only `N asymp 1/a` distinct prime logarithms. The missing bridge remains genuinely source-specific: either construct an overlapping/non-coordinatewise acquisition that coherently compresses exponentially many true-amplitude Euler channels into Poisson-many effective probes, or prove that such compression necessarily loses the nuclear mass needed by `NB-178`; then connect any surviving certificate back to a matched-control Nyman approximation statement.

## Prior-art audit

Content searches were made for Wiener-algebra treatments of the zeta logarithmic derivative, scaled von-Mangoldt Laplace laws, weighted Dirichlet/Vandermonde phase matrices, and Nyman--Beurling uses of such acquisition budgets. The ingredients found are classical separately: `-zeta'/zeta=sum Lambda(n)n^(-s)` in `Re s>1`, the PNT/`psi(x)~x`, and generic sampling/Vandermonde theory. No source located in this pass states the line-specific conclusion that the `NB-186` Poisson-scale prime code carries vanishing normalized Euler-Wiener acquisition mass or the resulting exponential channel-cardinality mismatch. No new external theorem is load-bearing beyond the PNT consequences already anchored in `SOURCES.md`, so `SOURCES.md` is unchanged.

## Self-review

The strongest claim is deliberately limited to **individual prime-channel mass and direct Wiener block isolation**. Equation (5) does not say that every source-faithful observable must explicitly contain exponentially many separately exposed coordinates, nor does (6) lower-bound an arbitrary overlapping acquisition map. Those stronger statements would require a new factorization or entropy theorem and are not asserted here.

The asymptotic constant in (1) depends on the exact `NB-182` capped-character cost `M_a(lambda)=max{2,a lambda}`. Changing that normalization changes the limiting density and constant but not the structural conclusion that the natural mass lives at `a log n=Theta(1)` while polynomially many primes lie at `a log p=o(1)`.

## Research consequence

The post-`NB-186` positive route should no longer search for a better set of only `N asymp 1/a` individual prime columns. Even the best such set captures vanishing Wiener mass. The relevant question is whether one can build **mass-reusing aggregate probes**: each effective coordinate must combine a large population of true Euler channels while preserving enough independent height-phase response to retain `N^(3/2)`-scale nuclear mass after the actual acquisition charge. A negative result should target that overlap/compression mechanism directly.