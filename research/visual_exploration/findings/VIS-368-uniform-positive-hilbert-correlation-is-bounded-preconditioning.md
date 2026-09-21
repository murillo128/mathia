# VIS-368 — uniformly comparable positive Hilbert coefficient metrics are only bounded preconditioning

## Claim

Let

`B=D_beta V`

be any Wang polynomial-coefficient map of the type isolated in `VIS-354`, with arbitrary finite scale count and arbitrary effective polynomial depth. Let `W` be a positive diagonal coefficient covariance and let `H` be any positive-definite Hermitian coefficient covariance, possibly non-diagonal. Measure physical coefficients `a` through the corresponding Hilbert norms by writing

`a=W^(1/2) z`

or, more generally,

`a=L z`, `H=L L^*`.

The Euclidean-coordinate Wang maps are therefore

`A_W=B W^(1/2)`

and

`A_H=B L`,

with

`A_W A_W^*=B W B^*`, `A_H A_H^*=B H B^*`.

Assume that the correlated metric is uniformly Loewner-comparable to the diagonal baseline:

`m W <= H <= M W`

for some `0<m<=M<infinity`. Then, for every singular-value index `k`,

`sqrt(m) s_k(A_W) <= s_k(A_H) <= sqrt(M) s_k(A_W)`.

Consequently:

- `A_H` and `A_W` have the same rank;
- every asymptotic singular exponent present in one map is the same in the other whenever `m,M` stay bounded away from `0,infinity`;
- no uniformly equivalent positive non-diagonal Hilbert metric can create a new polynomial-order or exponential-order Wang coefficient collapse;
- if the depth grows, the statement remains valid dimension by dimension, and remains asymptotically uniform whenever the same comparison constants work uniformly in the depth.

Thus **positive non-diagonal coefficient geometry is not a new Wang resource merely because it contains correlations**. A source-independent correlated Hilbert metric that stays uniformly equivalent to an already priced positive diagonal metric is only bounded preconditioning. Any claimed gain must come from degeneration of the metric-equivalence constants, source dependence, a genuinely indefinite/non-Hilbert topology, or another mechanism outside this positive Hilbert comparison class.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL LOEWNER/SINGULAR-VALUE MONOTONICITY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This proves no stronger estimate for the normalized Chebyshev-theta remainder, the prime number theorem remainder, zeta zeros, or RH.

## 1. The coefficient metric enters only through one positive covariance

The tail map from `VIS-354` sends physical bank coefficients to polynomial tail coefficients through `B=D_beta V`. A positive Hilbert coefficient norm can always be represented by a positive covariance matrix.

If

`||a||_(H^-1)^2=a^* H^(-1) a`,

choose any factor `L` with `H=L L^*` and set `a=Lz`. Unit Euclidean vectors `z` then represent unit vectors in the physical Hilbert norm, and the induced Wang operator is `A_H=BL`.

The choice of factor is irrelevant to the output singular values because

`A_H A_H^*=B H B^*`.

So the correct invariant is the positive covariance `H`, not a particular square root, Cholesky factor, coordinate basis, or correlation parametrization.

`VIS-361` treated the diagonal case `H=W`. The present question is whether off-diagonal positive correlations can supply a new asymptotic resource while remaining comparable to that already priced diagonal geometry.

## 2. Loewner comparison passes directly through the Wang map

Assume

`m W <= H <= M W`.

For every output vector `y`,

`y^* B H B^* y=(B^*y)^*H(B^*y)`.

Therefore

`m (B^*y)^*W(B^*y)`
` <= (B^*y)^*H(B^*y)`
` <= M (B^*y)^*W(B^*y)`.

Equivalently,

`m A_W A_W^* <= A_H A_H^* <= M A_W A_W^*`.

Eigenvalues of Hermitian matrices are monotone under Loewner order. Since the eigenvalues of `A A^*` are the squared singular values of `A`, ordered decreasingly,

`m s_k(A_W)^2 <= s_k(A_H)^2 <= M s_k(A_W)^2`

for every `k`. Taking square roots gives the claimed estimate.

The argument is exact and does not depend on the number of coefficient coordinates, node geometry, or polynomial depth. All such information remains inside the already existing map `B` and baseline covariance `W`.

## 3. Uniform correlations cannot change the asymptotic scale

Suppose an external parameter `X` changes the bank, support size, collision scale, or depth, and suppose

`m_0 W_X <= H_X <= M_0 W_X`

with constants `m_0,M_0` independent of `X`. Then for every singular sector,

`s_k(A_(H_X)) asymp s_k(A_(W_X))`

with constants depending only on `m_0,M_0`.

Hence any power-law, stretched-exponential, exponential, or zero/nonzero singular scale derived for the diagonal baseline survives unchanged. The off-diagonal correlations can change bounded constants and singular directions, but not the asymptotic size class.

This includes growing depth. If `q=q(X)` grows but the covariance comparison remains uniform in `q`, a correlated positive metric cannot erase or manufacture the universal compact high-degree baseline of `VIS-367` by more than a bounded factor. A better-conditioned coordinate presentation may still be useful numerically, but it is not an arithmetic gain unless the physical coefficient topology itself changes by an unbounded amount.

## 4. Metric degeneration is the actual resource when comparison is not uniform

If no uniform constants exist, define the relative positive operator

`C=W^(-1/2) H W^(-1/2)`.

Then the best comparison constants are

`m=lambda_min(C)`, `M=lambda_max(C)`.

The singular-value comparison becomes

`sqrt(lambda_min(C)) s_k(A_W)`
` <= s_k(A_H)`
` <= sqrt(lambda_max(C)) s_k(A_W)`.

So any asymptotically new effect available solely through a positive correlated metric must be accompanied by degeneration of the relative spectrum of `C`. That degeneration is not free: it is exactly the amount by which the new coefficient topology ceases to be uniformly equivalent to the baseline one.

For the Wang audit this provides a direct accounting rule. If a proposal attributes gain to a non-diagonal positive metric, first compute or bound the relative eigenvalues of `C`. If they remain bounded, kill the metric as bounded preconditioning. If they diverge or vanish, treat that growth as an explicit resource and show why the physical destination norm permits it rather than hiding it inside a convenient coefficient coordinate system.

## 5. Static signs and phases are an exact gauge special case

A fixed sign or phase attached to each coefficient coordinate does not create an indefinite geometry. If `U` is diagonal unitary and one replaces a factor `W^(1/2)` by

`W^(1/2) U`,

then

`(W^(1/2)U)(W^(1/2)U)^*=W`.

Thus all singular values are exactly unchanged. Signed cancellation in a chosen coefficient vector remains real and may be mathematically useful, but the mere availability of fixed source-independent signs/phases does not alter the positive Hilbert conditioning capacity of the bank.

This sharpens the phrase “signed coefficient geometry” in the current clue. What remains outside the positive closure is not ordinary signed coefficients under a positive Hilbert budget; those were already allowed by the Vandermonde moment map. A genuinely different route must use source-dependent signed selection, an indefinite quadratic form, a non-Hilbert topology, or a positive metric whose relative conditioning itself degenerates and is justified by the physical Wang destination.

## 6. Wang consequence

`VIS-361` priced arbitrary positive diagonal weights by a weighted moment Gram. `VIS-366` then removed support-cardinality and power-valuation restrictions at fixed depth, and `VIS-367` identified the universal source-free Chebyshev/capacity collapse that appears when polynomial depth grows.

The present result closes a remaining wording-level loophole: **bounded positive off-diagonal correlation does not leave that source-free Hilbert category**. Uniformly equivalent positive metrics have singular spectra comparable term by term, so they cannot generate a new asymptotic localization scale.

A surviving coefficient-topology route must therefore exhibit at least one of:

- relative metric eigenvalues that degenerate with the asymptotic parameter or depth, with that degeneration paid for in the physical coefficient/destination norm;
- a metric or selector depending on signed arithmetic source information, whose gain is proved as a source estimate rather than attributed to passive conditioning;
- a genuinely indefinite, Krein/Pontryagin-type, non-Hilbert, or nonlinear coefficient geometry for which the positive Loewner comparison no longer applies;
- or a separate noncompact/global mechanism outside the compact polynomial coefficient audit.

## Prior-art audit

The matrix inequalities are classical. Roger A. Horn and Charles R. Johnson, *Matrix Analysis*, 2nd ed., Cambridge University Press (2013), Chapter 7, develops positive-definite matrices and Loewner order. Horn and Johnson, *Topics in Matrix Analysis*, Cambridge University Press (1991), Chapter 3, treats singular-value inequalities. The implication used here is the elementary combination of Loewner monotonicity with the fact that the squared singular values of `A` are the eigenvalues of `AA^*`.

No novelty is claimed for positive-definite covariance factorizations, Loewner order, generalized coefficient metrics, preconditioning, or singular-value comparison. The Mathia-specific contribution is only the audit consequence for the current Wang frontier: a non-diagonal positive Hilbert metric must become asymptotically inequivalent to the already priced diagonal metric before its correlations can count as a new resource.

## Dependencies

- `VIS-354`: Wang tail coefficients form a source-free truncated Vandermonde moment map.
- `VIS-361`: arbitrary positive diagonal coefficient weights are priced by a weighted moment Gram.
- `VIS-366`: fixed-depth positive compact polynomial sampling is priced by Vandermonde partition sums.
- `VIS-367`: growing compact depth has a universal Chebyshev/capacity conditioning baseline.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The Wang coefficient-topology frontier is narrower. **Uniformly comparable positive non-diagonal Hilbert metrics are only bounded preconditioners of the already priced positive diagonal geometry.** They preserve rank and every singular-value asymptotic scale up to fixed multiplicative constants, including at growing depth when the comparison is uniform in depth.

Future work should therefore not cite off-diagonal positive correlations by themselves as an escape from the moment/Vandermonde audit. A genuine coefficient-topology mechanism must pay for metric degeneration, use source-dependent arithmetic information, or leave positive Hilbert geometry altogether.