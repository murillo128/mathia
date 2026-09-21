# MI-052 — Fixed Wang tail coefficients are a source-free block Vandermonde map

**Evidence level:** exact finite-dimensional synthesis from [VIS-354](../../findings/VIS-354-wang-tail-coefficient-block-vandermonde.md), extending the moment/fiber decomposition in VIS-343--VIS-344 and the collision conditioning ledger in VIS-351--VIS-353. Vandermonde rank and compact singular-value bounds are classical; the line-specific content is the elimination of a hidden source-to-coefficient channel in the fixed-bank Wang model.

For one translation fiber with inverse scales `x_j=a_j^(-1)` and fixed tail depth `q`, the raw Wang polynomial coefficients satisfy

`d_b = D_beta V_b c_b`,  `(V_b)_(k,j)=x_j^k`, `1<=k<=q`,

with invertible diagonal `D_beta`. Across translations this map is block diagonal. The arithmetic source `G` does not enter it at all when bank weights, scales and translations are source-independent.

If a fiber has at most `q` distinct scales and the inverse scales remain in a compact interval with fixed separation, `D_beta V_b` has a uniform positive smallest singular value. Its coefficient vector therefore cannot become asymptotically small relative to the bank weights. If the fiber has more than `q` scales, the only exact nullspace is the already-known moment cancellation `sum_j c_j a_j^(-k)=0` for `k=1,...,q`; near-nullness is approximate filter-design cancellation of the same source-free equations.

Thus the bounded finite-bank chain separates into two explicit maps: bank weights to tail coefficients via block Vandermonde moments, then those coefficients to the confluent exponential function via phase/Hermite geometry. VIS-351--VIS-353 already price the second map in stable coordinates; VIS-354 shows that the first contains no latent arithmetic localization either.

**Boundary.** A genuinely source-specific collapse is still possible only if some bank parameter or selection rule depends on `G` or equivalent arithmetic information, or if another explicit resource escapes the compact finite model: growing scale count/depth, scale collisions or unbounded scale range, growing/global phase geometry, shrinking windows, frequency-dependent coefficients or infinite representations. Source dependence must then be counted as mathematical input and traced through the downstream map rather than credited to passive Wang smoothing.