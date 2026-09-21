# MI-088 — Fixed-rank path-distance gap geometry is order-sensitive but not prime-separating

**Evidence level:** exact/classical determinant and source-geometry synthesis from [MC-440](../../findings/MC-440-path-distance-determinant-buries-gap-order-two-degrees-down.md), [MC-441](../../findings/MC-441-first-order-sensitive-path-coefficient-is-adjacency-endpoint-scalar.md), [MC-442](../../findings/MC-442-distance-polynomial-coefficients-have-universal-sign-rigidity.md), [MC-443](../../findings/MC-443-fixed-rank-prime-gap-shapes-are-projectively-dense.md), and [MC-444](../../findings/MC-444-fixed-rank-prime-gap-shape-realization-has-polynomial-source-height.md). The weighted-tree determinant and short-interval prime inputs are classical; the line-specific content is their placement after the Möbius full-interaction gate and the prime-gap projective/source-height audit.

The path-distance kernel is a genuine escape from the fixed-feature-rank collapse of MC-439. For ordered points with adjacent positive gaps `g_1,...,g_(r-1)`, its determinant can distinguish non-reversal permutations of the same gap multiset. Common scaling nevertheless exposes two permutation-blind leading layers, and MC-441 shows that all order dependence in the first surviving coefficient factors through

`J(g)=1/g_1+1/g_(r-1)-(sum_i g_i)(sum_i 1/(g_i g_(i+1)))`.

Thus the first ordinal signal is relative `O(X^(-2))` under common dilation and is compressed to endpoint plus nearest-neighbor reciprocal data. MC-442 strengthens the obstruction: every nonconstant coefficient of `det(XD-I)` has the same sign throughout the entire positive-gap domain, and `J(g)` itself is strictly negative. Lower determinant degrees may contain richer magnitudes, but no coefficient-sign layer can manufacture Möbius-like cancellation.

MC-443 then changes how even those magnitudes may be interpreted at fixed rank. After normalizing by total gap span, selected-prime gap shapes are dense in the full positive simplex. Any continuous scale-invariant statistic of a fixed number of gaps therefore has the same image closure on prime-derived and generic positive shapes. In particular, normalized path-distance coefficient vectors and `S(g)J(g)` cannot separate rational-prime chains from positive-gap controls by a forbidden range or a positive topological margin.

MC-444 prices the most immediate quantitative loophole in that density statement. Fix rank `r` and stay in a compact interior simplex `Delta_(r-2)(kappa)`. Every target shape can be approximated to projective accuracy `eta` by selected rational primes with squarefree source height

`n <= C(r,kappa) eta^(-40r/19)`.

Equivalently, `log n <= (40r/19) log(1/eta)+O_(r,kappa)(1)`. Thus the fixed-rank dense approximants are not hidden behind a superpolynomial precision barrier. A continuous normalized fixed-rank observable cannot recover robust prime specificity merely by claiming that generic-looking prime shapes occur only at astronomically inefficient source heights.

The surviving resources are narrower. Distribution or natural-source frequency can still distinguish how often shapes occur; growing rank can make the exponent itself grow; absolute scale can carry information erased by projectivization; discontinuous or exactly arithmetic observables can ignore topological approximation; and a lower-bound problem for minimal realization height remains distinct from the polynomial existence upper bound. Any such carrier must still survive the Möbius top-interaction gate and produce an analytic cancellation estimate.

The reusable lesson is that order sensitivity, sign variation, topological source separation and quantitative realization cost are different gates. A determinant can preserve gap order while its signs are universal; a continuous normalized magnitude can vary richly while prime-derived shapes are dense; and at fixed rank even the cost of reaching a generic interior shape is only polynomial in inverse precision.

**Boundary.** Projective density and the polynomial realization estimate are fixed-rank statements using selected primes, not necessarily consecutive ambient primes. The source-height theorem is an upper bound only, is uniform only away from the boundary of shape space, and gives no frequency/equidistribution statement. Growing-rank, natural-source, scale-sensitive, distributional and discontinuous regimes remain outside the no-go. No Möbius or zeta cancellation estimate follows from these representation facts alone.
