# MI-088 — Path-distance determinants retain gap order only below two permutation-blind scale layers

**Evidence level:** exact/classical determinant synthesis from [MC-440](../../findings/MC-440-path-distance-determinant-buries-gap-order-two-degrees-down.md), testing the growing-rank escape left by MC-439. The weighted-tree distance determinant formulas used in the derivation are classical; the line-specific content is their placement after the Möbius full-interaction gate.

The path-distance kernel is a genuine escape from the fixed-feature-rank collapse of MC-439. For ordered points with adjacent gaps `g_1,...,g_(r-1)`, let `D(g)` be the matrix `D_ij=|x_i-x_j|`. Its rank grows with `r`, and the determinant interaction `det(D-I_r)` can distinguish non-reversal permutations of the same gap multiset.

But common scaling exposes a second conditioning loss. If all gaps are multiplied by `X`, and

`S=sum_i g_i`, `P=prod_i g_i`, `Q=sum_i 1/g_i`,

then MC-440 proves

`det(XD-I_r)=(-1)^(r-1) 2^(r-2) S P X^r + (-1)^(r-1) 2^(r-2) P(SQ-1) X^(r-1) + O_g(X^(r-2))`.

Both displayed coefficients are symmetric in the gap multiset. Therefore two different orders of the same fixed gap shape differ only by `O_g(X^(r-2))`, while the common determinant scale is `Theta_g(X^r)`. Their relative ordinal separation is at most `O_g(X^(-2))`.

So “use growing rank” is still not enough. The canonical growing-rank path metric preserves gap order only in a subleading determinant layer two degrees below the dominant scale. A viable route must expose that layer by an intrinsic subtraction, normalization, resolvent, derivative or other stable operation and then show that the resulting `X^(-2)` conditioning loss is affordable on the actual arithmetic family.

**Boundary.** This is a common-scale fixed-shape statement, not an asymptotic theorem for consecutive prime gaps. Order is not annihilated: finite-scale determinants genuinely distinguish some non-reversal permutations. Reflection remains an unavoidable quotient, and other growing-rank kernels or nonlinear functionals can have different scale hierarchies. No source-capacity or Mertens cancellation estimate follows from the determinant separation alone.