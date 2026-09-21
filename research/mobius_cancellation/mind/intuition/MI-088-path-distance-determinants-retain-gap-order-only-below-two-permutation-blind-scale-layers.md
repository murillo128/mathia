# MI-088 — Path-distance determinant order first survives through one adjacency-endpoint scalar

**Evidence level:** exact/classical determinant synthesis from [MC-440](../../findings/MC-440-path-distance-determinant-buries-gap-order-two-degrees-down.md) and [MC-441](../../findings/MC-441-first-order-sensitive-path-coefficient-is-adjacency-endpoint-scalar.md), testing the growing-rank escape left by MC-439. The weighted-tree distance determinant formulas and principal-minor machinery are classical; the line-specific content is their placement after the Möbius full-interaction gate.

The path-distance kernel is a genuine escape from the fixed-feature-rank collapse of MC-439. For ordered points with adjacent gaps `g_1,...,g_(r-1)`, let `D(g)` be the matrix `D_ij=|x_i-x_j|`. Its rank grows with `r`, and `det(D-I_r)` can distinguish non-reversal permutations of the same gap multiset.

Common scaling nevertheless exposes two permutation-blind leading layers. With `g->Xg`, and

`S=sum_i g_i`, `P=prod_i g_i`, `Q=sum_i 1/g_i`,

MC-440 proves that the `X^r` and `X^(r-1)` coefficients depend only on the gap multiset. Different orders of one fixed gap shape first separate at degree `r-2`, hence at relative scale `O_g(X^(-2))` against the common `Theta_g(X^r)` determinant scale.

MC-441 identifies the full order dependence of that first surviving coefficient. Writing `h_i=1/g_i`, the permutation-sensitive part factors through the single scalar

`J(g)=h_1+h_(r-1)-S sum_i h_i h_(i+1)`.

All other terms in the `X^(r-2)` coefficient are symmetric in the gap multiset. Thus clearing the fixed-rank obstruction and reaching the first order-sensitive homogeneous layer still does not expose unrestricted global gap order: the initial ordinal carrier consists only of the two endpoint reciprocals and one nearest-neighbor reciprocal-product energy.

The locality is exact. For an interior adjacent transposition with neighboring reciprocal gaps `a,b,c,d`, MC-441 gives

`J_after-J_before=-S(c-b)(a-d)`.

So the first ordinal layer can be blind to a swap for a purely four-gap local reason even while the full permutation is different. This is a factorization statement, not a cardinality theorem: a single real scalar can still take many distinct values.

The surviving question is therefore quantitative and arithmetic. One must show that the actual prime-divisor gap family forces useful separation, rigidity or cancellation in `J(g)` at the `X^(-2)` relative layer, and that matched nonprime gap permutations do not reproduce the same behavior. Otherwise this first surviving determinant layer is only a local adjacency summary and the branch must descend to lower coefficients or change observable.

**Boundary.** These are finite exact identities and common-scale fixed-shape asymptotics, not a theorem about the distribution of consecutive prime gaps. Reflection remains invisible. Lower determinant coefficients can contain longer-range information, and other growing-rank kernels can have different scale hierarchies. No source-capacity or Mertens cancellation estimate follows from the existence or factorization of `J(g)` alone.