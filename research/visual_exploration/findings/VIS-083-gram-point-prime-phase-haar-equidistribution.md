# VIS-083 — Gram-point sampling is Haar-equidistributed on every fixed finite prime torus

## Claim

Let `t_n` be the Gram points, defined for all sufficiently large `n` by

`theta(t_n) = pi n`

(up to the harmless conventional integer shift in the Gram indexing), where `theta` is the Riemann–Siegel theta function. Fix distinct primes `p_1,...,p_r`. Then

`(t_n log p_1/(2 pi), ..., t_n log p_r/(2 pi)) mod 1`

is equidistributed on the torus `T^r` as `n -> infinity`.

Equivalently, for every continuous function `F:T^r -> C`,

`(1/N) sum_(n<=N) F(exp(-i t_n log p_1),...,exp(-i t_n log p_r))`

converges to the Haar average of `F` on `T^r`.

Therefore Gram-point sampling, although its anchor is defined independently through the gamma/theta factor, does **not** change the asymptotic population law of any observable depending continuously on a fixed finite set of prime phases. At this level it is reproduced exactly by the shared-phase Haar/random-initial-phase control already used in `VIS-071`.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL-UNIFORM-DISTRIBUTION + NEGATIVE/OBSTRUCTION + NO-NOVELTY-CLAIM`.

The prime-phase equidistribution itself is established prior art in the Gram-point discrete-universality literature; the derivation below records the elementary finite-dimensional specialization and its visual-control consequence. No quantitative discrepancy rate, short-block statement, growing-prime-support theorem, prime/zero independence theorem, or RH consequence is claimed.

## 1. The Gram inverse has the Fejér scale

Write `t(x)` for the continuous inverse determined by

`theta(t(x)) = pi x`

for sufficiently large `x`. Stirling's formula for the gamma factor gives the standard asymptotics

`theta'(t) = (1/2) log(t/(2 pi)) + O(t^(-2))`

and

`theta''(t) = 1/(2t) + O(t^(-3))`.

Thus `theta'` is eventually positive and increasing, and

`t'(x) = pi/theta'(t(x))`

is eventually positive, decreasing, and tends to zero.

The usual Gram-point asymptotic is

`t(x) ~ 2 pi x/log x`,

and hence

`t'(x) ~ 2 pi/log x`.

In particular,

`x t'(x) -> infinity`.

So for every fixed real `a != 0`, the derivative of

`g_a(x)=a t(x)/(2 pi)`

has constant eventual sign, tends monotonically to zero in magnitude, and satisfies

`x |g_a'(x)| -> infinity`.

The classical Fejér/van-der-Corput uniform-distribution criterion therefore implies that

`g_a(n) mod 1`

is uniformly distributed on `R/Z`.

## 2. Unique factorization supplies every nonzero Weyl frequency

Apply the multidimensional Weyl criterion to the prime-phase vector. For any nonzero integer vector

`m=(m_1,...,m_r) in Z^r`,

its scalar Fourier frequency is

`a_m = sum_j m_j log p_j`

`    = log(prod_j p_j^(m_j))`.

Unique factorization gives `a_m != 0` whenever `m != 0`. By the one-dimensional result above,

`t_n a_m/(2 pi) mod 1`

is uniformly distributed. Hence its nontrivial Weyl exponential sums vanish:

`(1/N) sum_(n<=N) exp(i t_n a_m) -> 0`.

This holds for every `m != 0`, which is exactly the Weyl criterion for Haar equidistribution of the full vector on `T^r`.

No Diophantine independence beyond the elementary multiplicative independence of distinct rational primes is needed.

## 3. What the result removes from the visual search space

A natural reading of the narrowed prime-phase clue was that Gram points might provide an independently defined anchor capable of exposing structure missed by ordinary vertical averaging. They are indeed independently defined: their locations come from the gamma/theta factor rather than from a chosen finite prime field.

But independence of the **definition of the sampling times** is not enough. For every fixed finite prime support, the resulting population of prime phases is asymptotically Haar. Thus a scatter plot, histogram, continuous phase statistic, or other fixed-dimensional observable evaluated over all Gram points cannot separate from the frequency-preserving random-initial-phase null merely because the samples were taken at Gram points.

This is an information boundary, not a statement that Gram points are useless. A finite-height discrepancy, a short moving block, a statistic whose prime support grows with height, or an observable coupling the prime field to genuinely additional Gram/zero data is a different question. Those regimes are not consequences of fixed-dimensional population equidistribution.

## Prior art and novelty assessment

Uniform-distribution criteria of Fejér/van der Corput and Weyl's criterion are classical; see, for example, L. Kuipers and H. Niederreiter, *Uniform Distribution of Sequences* (Wiley, 1974). The derivative criterion used above is the standard theorem that a differentiable `g` with eventually monotone `g'(x)->0` and `x|g'(x)|->infinity` produces a uniformly distributed sequence `g(n) mod 1`.

More decisively, A. Laurinčikas, **Joint Discrete Approximation of Analytic Functions by Shifts of the Riemann Zeta-Function Twisted by Gram Points**, *Mathematics* 11:3 (2023), 565, DOI `10.3390/math11030565`, directly introduces empirical measures of the prime-phase coordinates `p^(-i t_k^alpha)` on the infinite prime torus and proves the weak-convergence input needed for its Gram-point universality theorem. Its uniform-distribution section states the Weyl criterion and the same monotone-derivative sufficient condition; the case `alpha=1` contains the fixed-prime phase law used here. Earlier Gram-point discrete-universality work includes M. Korolev and A. Laurinčikas, **A new application of the Gram points**, *Aequationes Mathematicae* 93 (2019), 859–873, DOI `10.1007/s00010-019-00647-8`.

Thus the displayed torus-equidistribution claim is not a new theorem. The durable Mathia result is its **visual-control specialization**: Gram-point anchoring must not be counted as an independent fixed-finite-prime population channel against the shared-phase Haar null.

## Boundary and falsification

The proof fixes `r` and the primes before `n -> infinity`. It gives no rate uniform in a growing support and therefore does not justify replacing a growing-dimensional Gram sample by Haar. It also does not imply that finite consecutive blocks of Gram points are well distributed uniformly in their starting index.

The conclusion applies to continuous observables of those fixed prime phases. It does not erase information carried by `theta(t_n)` itself, Gram occupancy, `Z(t_n)` magnitude/derivatives, nearby zero geometry, or a jointly defined prime-plus-zero observable unless that additional coordinate is shown to be a deterministic function of the admitted torus data.

Falsify the argument by breaking one of its exact steps: the eventual inverse-derivative asymptotics for the Gram function, the uniform-distribution criterion, multiplicative independence of the selected primes, or the multidimensional Weyl reduction. A source-level falsification would require showing that the cited Gram-point prime-phase weak-convergence result has materially different hypotheses from the `alpha=1`, fixed-prime specialization used here.

## Visual consequence

No canonical PNG is retained. A finite-height torus scatter would only illustrate an asymptotic equidistribution theorem and could overemphasize finite discrepancy or plotting choices. The exact population-law obstruction is the durable result.

## Research consequence

The accepted `CLUE-zeta-prime-phase-recursive-geometry` should remain narrowed as published: **Gram points are closed as a positive external anchor for fixed-finite-prime population statistics**. A surviving externally anchored route must either use an anchor whose induced prime-phase population is not already asymptotically Haar, make a genuinely quantitative finite-window/short-block claim, allow support to grow under a separately justified control, or include an independently informative coordinate rather than only the same finite prime torus sampled at different times.