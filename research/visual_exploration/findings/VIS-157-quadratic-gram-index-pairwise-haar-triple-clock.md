# VIS-157 — quadratic Gram-index subsampling is pairwise Haar but has a coherent triple clock relation

## Claim

Let `g_k` be the Gram points, let

`z_k=(p^(-i g_k))_p in Omega`,

and define the nonlinear sparse Gram-index subsequence

`w_n=z_(n^2)`

for sufficiently large `n`.

Then quadratic index subsampling creates a sharp fixed-offset distinction that is entirely deterministic sampling geometry.

First, for every fixed finite set of primes, the population `w_n` is Haar-equidistributed on the corresponding finite prime torus.

Second, for every fixed integer offset `h>=1`, the joint population

`(w_n,w_(n+h))`

is Haar-equidistributed on the product of two copies of every fixed finite prime torus.

Third, no analogous three-copy statement holds. For any three distinct fixed integer offsets

`b_0<b_1<b_2`,

there is a nontrivial fixed-prime product character whose value along

`(w_(n+b_0),w_(n+b_1),w_(n+b_2))`

tends to `1`. In particular, for equally spaced offsets,

`w_n(p) w_(n+2h)(p) / w_(n+h)(p)^2 -> 1`

for every fixed prime `p`.

Thus the quadratic selector is asymptotically **pairwise Haar but not three-wise Haar**. A sparse nonlinear Gram sample can therefore look fully mixed in every fixed one- and two-time prime-phase view while retaining an exact asymptotic second-difference clock constraint visible at three times.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-UNIFORM-DISTRIBUTION/GRAM-ASYMPTOTIC + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

No statement is made for growing prime support, growing offsets, polynomial selectors of degree other than two, arbitrary nonlinear or data-dependent selectors, zeta-value/zero-derived coordinates, stochastic mixing, or RH.

## 1. The quadratic sampled Gram clock has a slowly vanishing second derivative

Let `g(x)` be the smooth eventual inverse of

`theta(g(x))=pi x`

and define

`G(x)=g(x^2)`.

The inverse-Gram estimates used in `VIS-083`, `VIS-154`, and `VIS-156` give

`g'(x)~2 pi/log x`

and, for fixed `m>=2`,

`g^(m)(x) asymp_m x^(1-m)(log x)^(-2)`

with the expected eventual alternating signs. The chain rule therefore gives

`G'(x)=2x g'(x^2)~2 pi x/log x`,

while

`G''(x)=2 g'(x^2)+4x^2 g''(x^2)`
`       = 2 pi/log x + O((log x)^(-2))`.

Hence `G''(x)` is eventually positive, decreases to zero, and satisfies

`x G''(x)->infinity`.

Differentiating once more gives

`G'''(x)=O(1/[x(log x)^2])`,

with eventual negative leading sign. The important scale change is therefore exact at the level needed below: quadratic index acceleration converts the original Gram clock into a sampled clock whose **second** derivative has the Fejer scale.

## 2. The quadratic subsequence itself is still Haar on fixed prime support

Fix distinct primes `p_1,...,p_s` and a nonzero integer vector `m in Z^s`. Put

`A=sum_j m_j log p_j`.

Unique factorization gives `A!=0`. To apply Weyl's criterion to

`A G(n)/(2 pi)`,

use van der Corput's difference theorem. For every fixed integer `q>=1`, the difference

`D_q(x)=A[G(x+q)-G(x)]/(2 pi)`

has derivative

`D_q'(x)=A[G'(x+q)-G'(x)]/(2 pi)`
`       = A q G''(x)/(2 pi) (1+o(1))`.

By the preceding section, `D_q'(x)` has constant eventual sign, decreases to zero in magnitude, and satisfies

`x |D_q'(x)| -> infinity`.

The classical Fejer first-derivative criterion therefore makes every fixed difference sequence `D_q(n)` uniformly distributed modulo one. Van der Corput's difference theorem then makes `A G(n)/(2 pi)` uniformly distributed modulo one.

This holds for every nonzero prime character. Multidimensional Weyl therefore gives Haar equidistribution of `w_n` on every fixed finite prime torus.

Quadratic sparsity alone is not an independent prime-phase population source.

## 3. Every fixed two-time view is Haar

Fix `h>=1`. A character of the two-copy finite prime torus gives real coefficients

`A_0=sum_p m_(0,p) log p`,
`A_1=sum_p m_(1,p) log p`,

not both zero, and phase

`F(x)=A_0 G(x)+A_1 G(x+h)`.

There are two cases.

If `A_0+A_1!=0`, then for every fixed `q>=1`,

`F(x+q)-F(x)`

has derivative

`(A_0+A_1) q G''(x)+O(1/[x(log x)^2])`.

The leading derivative again has the Fejer scale: constant eventual sign, tending to zero, with `x` times its magnitude diverging. Thus every fixed difference of `F(n)/(2 pi)` is uniformly distributed, and van der Corput gives uniform distribution of `F(n)/(2 pi)` itself.

If `A_0+A_1=0`, then `A_1!=0` and

`F(x)=A_1[G(x+h)-G(x)]`.

Now

`F'(x)=A_1[G'(x+h)-G'(x)]`
`     = A_1 h G''(x)(1+o(1))`,

so the first-derivative Fejer criterion applies directly.

Every nontrivial two-copy character therefore has vanishing empirical average. Weyl's criterion proves Haar equidistribution of `(w_n,w_(n+h))` on the two-copy fixed prime torus.

This is stronger than the one-time population null: a conventional pair scatter, pair correlation of fixed prime phases, or any continuous fixed-support two-time view can look asymptotically fully mixed under the completely deterministic selector `n -> n^2`.

## 4. Three fixed times expose the hidden deterministic clock

Now fix distinct integers `b_0<b_1<b_2`. Choose a nonzero integer vector `c=(c_0,c_1,c_2)` satisfying

`sum_j c_j=0`,
`sum_j c_j b_j=0`.

For example one may take

`c_0=b_2-b_1`,
`c_1=-(b_2-b_0)`,
`c_2=b_1-b_0`.

Its quadratic moment

`S_2=sum_j c_j b_j^2`

is nonzero because the nodes are distinct. Taylor expansion with fixed offsets gives

`sum_j c_j G(x+b_j)`
` = (S_2/2) G''(x) + O(G'''(x))`.

Since `G''(x)->0` and `G'''(x)->0`, this combination tends to zero.

Choose any fixed prime `p` and the product character

`Chi(omega_0,omega_1,omega_2)=product_j omega_j(p)^(c_j)`.

Then

`Chi(w_(n+b_0),w_(n+b_1),w_(n+b_2))`
` = exp(-i log(p) sum_j c_j G(n+b_j)) -> 1`.

A nontrivial Haar character must have expectation zero, so the three-copy empirical law cannot converge to Haar.

For `b=(0,h,2h)`, the primitive relation is `(1,-2,1)` and the obstruction becomes

`w_n(p) w_(n+2h)(p) / w_(n+h)(p)^2 -> 1`.

The apparent pairwise mixing is therefore not stochastic independence. It is the lower-dimensional face of a deterministic smooth clock whose curvature reappears as soon as three fixed samples are compared.

## 5. Prior art and novelty audit

The proof uses only classical uniform-distribution machinery: Weyl's criterion, the Fejer monotone-derivative criterion, and van der Corput's difference theorem; see L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974). The Gram inverse asymptotics are the same classical Riemann-Siegel-theta consequences already used throughout `VIS-083`, `VIS-154`, and `VIS-156`.

Antanas Laurincikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, supplies the established Gram-point prime-phase/uniform-distribution context used in `VIS-083`; its sampled shifts involve powers of Gram values rather than the polynomial **index selector** `g_(n^2)` considered here. Related Gram-point universality literature likewise provides the surrounding discrete-shift context rather than a novelty basis for the fixed pair/triple classification above.

A targeted literature check did not identify a reason to present this quadratic-index pairwise-Haar/triple-clock statement as a new general uniform-distribution theorem. **No novelty is claimed.** Its durable Mathia value is as a sampling null: nonlinear sparsity and pairwise Haar appearance still need not supply information beyond the deterministic Gram clock.

## Boundary and falsification

The selector is exactly `n^2` and the offsets and prime support are fixed before `n->infinity`. The result gives no uniformity in growing offsets, growing support, changing character complexity, or another selector.

The pairwise Haar statement concerns only prime phases. It does not imply pairwise independence after adjoining `Z(g_(n^2))`, derivatives, zero occupancy, or another independently anchored analytic coordinate.

The triple obstruction is asymptotic and deterministic; it does not claim that every finite-height three-time plot is visually close to a one-dimensional surface before normalization.

Falsify the result by breaking the sampled-clock derivative asymptotic, the Fejer/van-der-Corput reductions, the Weyl character argument, or the two moment cancellations in the three-node product character.

## Visual consequence

No canonical PNG is retained. A pair scatter of quadratic-index Gram samples would emphasize the Haar-looking projection while hiding the three-time constraint. The exact two-versus-three character calculation is the stronger and safer visual control.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should narrow its nonlinear-subsampling escape. The canonical test case `k=n^2` is not an independent source: one- and two-time fixed-prime views are Haar, while every fixed three-time view carries a coherent second-difference clock character.

The natural next question is whether this extends to a degree-`d` polynomial hierarchy — Haar through `d` fixed samples with a deterministic `(d+1)`-point finite-difference obstruction — or whether some genuinely non-polynomial/data-dependent selector escapes that clock classification. That is a separate investigation, not part of the present finding.