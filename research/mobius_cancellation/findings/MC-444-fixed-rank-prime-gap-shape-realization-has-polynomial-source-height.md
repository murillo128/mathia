# MC-444 — Fixed-rank prime-gap shape realization has polynomial source-height cost

**Evidence:** `LITERATURE+DERIVED · EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-443` proved that, for every fixed rank, selected-prime divisor gap shapes are dense in the whole positive projective gap cone, but left the source-height cost completely unpriced. That loophole is already much narrower than stated there: the classical Baker–Harman–Pintz theorem on primes in intervals of length `x^0.525` gives a **polynomial** realization cost in the requested projective accuracy.

Fix an integer `r>=2` and `0<kappa<1/(r-1)`. Let

\[
\Delta_{r-2}(\kappa)
=
\left\{u=(u_1,\ldots,u_{r-1}):u_i\ge\kappa,\ \sum_i u_i=1\right\}.
\tag{1}
\]

There are constants `C=C(r,kappa)>0` and `eta_0=eta_0(r,kappa)>0` such that for every

\[
u\in\Delta_{r-2}(\kappa),\qquad 0<\eta<\eta_0,
\]

one can choose primes

\[
p_1<\cdots<p_r
\]

whose normalized adjacent-gap shape `sigma(p_1,...,p_r)` from `MC-443` satisfies

\[
\|\sigma(p_1,\ldots,p_r)-u\|_\infty\le\eta,
\tag{2}
\]

and whose squarefree source

\[
n=p_1\cdots p_r
\]

obeys

\[
\boxed{
n\le C\,\eta^{-40r/19}.
}
\tag{3}
\]

Equivalently, if source height is measured logarithmically, then

\[
\log n\le \frac{40r}{19}\log\frac1\eta+O_{r,\kappa}(1).
\tag{4}
\]

Thus the fixed-rank density from `MC-443` is not hidden behind a superpolynomial or exponential-in-precision arithmetic cost. On every compact interior part of shape space, an `eta`-net of prime-derived shapes is reachable with source height polynomial in `1/eta`.

This does **not** give a useful Möbius bound. The exponent grows linearly with rank, the construction uses selected rather than globally consecutive primes, and it says nothing about how frequently a shape occurs among natural sources. It only closes one specific fixed-rank escape: source-height inefficiency cannot by itself rescue a continuous projective shape observable through a superpolynomial precision barrier.

## 1. Short-interval primes price the approximation

Use the established Baker–Harman–Pintz theorem: for all sufficiently large `x`, the interval

\[
[x,x+x^\theta]
\]

contains a prime with

\[
\theta=0.525=\frac{21}{40}.
\tag{5}
\]

Fix a target `u` in `(1)` and set

\[
c_1=1,
\qquad
c_j=1+\sum_{i=1}^{j-1}u_i\quad(2\le j\le r).
\tag{6}
\]

Then

\[
1\le c_j\le2,
\qquad
c_{j+1}-c_j=u_j\ge\kappa.
\tag{7}
\]

For a scale `X`, apply `(5)` at each `c_jX`. For sufficiently large `X`, choose

\[
p_j\in[c_jX,c_jX+(c_jX)^\theta].
\tag{8}
\]

Write

\[
p_j=(c_j+e_j)X.
\]

Since `c_j<=2`,

\[
0\le e_j\le E_X:=2^\theta X^{\theta-1}.
\tag{9}
\]

If `E_X<kappa/2`, the intervals in `(8)` are pairwise ordered and therefore

\[
p_1<\cdots<p_r.
\]

Let `g_i=p_{i+1}-p_i` and `S=p_r-p_1`. Equations `(6)` and `(9)` give

\[
\frac{g_i}{X}=u_i+e_{i+1}-e_i,
\qquad
\left|\frac{g_i}{X}-u_i\right|\le E_X,
\tag{10}
\]

and

\[
\frac{S}{X}=1+e_r-e_1,
\qquad
\left|\frac{S}{X}-1\right|\le E_X.
\tag{11}
\]

For `E_X<=1/2`, combining `(10)` and `(11)` yields

\[
\left|\frac{g_i}{S}-u_i\right|
=
\frac{|(e_{i+1}-e_i)-u_i(e_r-e_1)|}{|1+e_r-e_1|}
\le4E_X.
\tag{12}
\]

It is therefore enough to choose `X` so that

\[
4\,2^\theta X^{\theta-1}\le\eta.
\tag{13}
\]

Because `1-theta=19/40`, condition `(13)` is satisfied once

\[
X\ge C_0\,\eta^{-40/19}
\tag{14}
\]

for an absolute constant `C_0`, enlarged if necessary to pass the fixed Baker–Harman–Pintz threshold. Taking `eta_0<=kappa` makes the same choice ensure the ordering condition `E_X<kappa/2` uniformly for all `u` in `(1)`.

Finally, `(8)` and `c_j<=2` give `p_j<=3X` for large `X`, hence

\[
n=\prod_{j=1}^r p_j\le(3X)^r
\ll_{r,\kappa}\eta^{-40r/19},
\]

which proves `(3)`.

## 2. The conclusion is uniform on compact interior shape classes

The point of the `kappa`-truncation in `(1)` is not cosmetic. Without a positive lower bound on the target gaps, the selected-prime intervals may cease to be ordered at a scale controlled solely by `eta`; the constant must then depend on the particular target shape through `min_i u_i`.

On `Delta_(r-2)(kappa)`, however, the construction is uniform. The short-interval theorem has one eventual threshold, all centers `c_jX` lie between `X` and `2X`, and `(9)` is independent of the target apart from this bounded range. Thus `(3)` is a genuine uniform `eta`-net source-height bound for every fixed `(r,kappa)`.

This sharpens the topology-only statement of `MC-443` in exactly the direction left open there. Fixed-rank continuous projective observables cannot hide a robust arithmetic discriminator behind the claim that prime-derived points only approach generic shapes at astronomically inefficient source heights: polynomial height already suffices.

## 3. What the polynomial cost does and does not kill

Suppose `Phi` is a continuous scale-invariant fixed-rank observable and has a quantitative modulus of continuity. `MC-443` says its prime-derived image is dense in its generic positive-gap image. The present result additionally says that, away from the boundary of shape space, the prime source needed to approximate a target to accuracy `eta` can be chosen with

\[
\log n=O_r(\log(1/\eta)).
\tag{15}
\]

Therefore a proposed separation whose only defense is that the approximating prime source has superpolynomial height cannot survive at fixed rank.

Several stronger escapes remain intact:

- a statistic can use **absolute scale** rather than projective shape;
- a statistic can be discontinuous or exactly arithmetic, so topological approximation is irrelevant;
- a distributional mechanism can distinguish how often different shapes arise even though both supports have the same closure;
- rank can grow with source size, in which case the exponent `40r/19` itself grows and the fixed-rank estimate need not remain useful;
- a natural-source restriction can forbid choosing arbitrary selected primes even though such primes occur as the divisor set of some squarefree integer.

These are now the honest surviving directions. Merely invoking an unspecified source-height bottleneck is no longer one of them at fixed rank.

## 4. Prior art and novelty boundary

The analytic input is classical: R. C. Baker, G. Harman and J. Pintz, *The Difference Between Consecutive Primes, II*, Proceedings of the London Mathematical Society 83 (2001), 532–562, DOI `10.1112/plms/83.3.532`, proves that `[x,x+x^0.525]` contains primes for sufficiently large `x`. No novelty is claimed for that theorem or for converting a short-interval existence exponent into a simultaneous finite collection of prime approximations.

A current preprint by Runbo Li, *The number of primes in short intervals and numerical calculations for Harman's sieve*, arXiv:`2308.04458`, claims the stronger exponent `0.52`. If that preprint's theorem is ultimately accepted at the required level, the identical derivation would replace the exponent `40r/19` in `(3)` by `25r/12`. The present finding deliberately uses the established Baker–Harman–Pintz exponent instead, so its claim does not depend on that recent computationally assisted preprint.

Adjacent prime-divisor-gap literature such as Sofos's 2023 moment/Poisson analysis concerns typical gap statistics rather than the source-height cost of realizing a prescribed finite projective shape. The source-height estimate here is retained as a Mathia frontier consequence of classical short-interval prime theory, with `NO-NOVELTY-CLAIM` for the standalone number-theoretic corollary.

## Boundaries and falsification tests

- **Fixed rank only.** The exponent in `(3)` is proportional to `r`; no useful uniform growing-rank theorem follows.
- **Interior compactness is essential for uniformity.** As `min_i u_i -> 0`, the ordering threshold can diverge relative to a fixed requested `eta`.
- **Selected primes, not ambient consecutive primes.** Other primes may lie between `p_i` and `p_(i+1)`; the claim concerns adjacent prime divisors of the chosen squarefree source.
- **Upper bound only.** No matching lower bound on the minimal source height is proved. Polynomial realizability does not identify the true optimal exponent.
- **No distribution statement.** The construction proves existence, not frequency or equidistribution among integers of bounded height.
- **No scale-sensitive obstruction is touched.** Absolute-scale or scale-shape couplings can still contain information erased by projectivization.
- **No Möbius estimate follows.** The theorem closes one representation loophole and supplies no direct cancellation, zero-free region, or RH consequence.
- **Recent `0.52` input is not used.** The quantitative claim `(3)` remains anchored to the established `0.525` theorem.

## Consequence for the research line

`MC-443` moved the fixed-rank gap branch from support/range separation toward distribution, source-height, growing-rank, absolute-scale, or discontinuous arithmetic structure. The present result removes the strongest naive version of the source-height escape: on compact interior shape classes, fixed-rank approximation by genuine rational-prime divisor sets already costs only a power of the requested precision.

The live source question is therefore narrower. Any source-height mechanism worth pursuing must exploit **growing rank, natural-source frequency, an optimal lower bound, or absolute arithmetic scale**, rather than mere existence of a very large prime source realizing a fixed-rank shape. In particular, a fixed-rank continuous projective statistic cannot recover prime-specific Möbius cancellation simply by assigning an unspecified high cost to the dense approximants from `MC-443`.