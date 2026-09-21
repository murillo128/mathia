# MI-052 — Compact Wang tail maps have a uniform quotient floor even under source-adaptive selection

**Evidence level:** exact finite-dimensional synthesis from [VIS-354](../../findings/VIS-354-wang-tail-coefficient-block-vandermonde.md) and [VIS-355](../../findings/VIS-355-source-adaptive-compact-bank-floor.md), together with the stable phase-coordinate controls in VIS-351--VIS-353. Vandermonde rank, singular values and compact constant-rank conditioning are classical; the line-specific content is the closure of both hidden coefficient conditioning and bounded adaptive selection as Wang resources.

For one translation fiber with inverse scales `x_j=a_j^(-1)` and fixed tail depth `q`, the raw Wang polynomial coefficients satisfy

`d_b = D_beta V_b c_b`, with `(V_b)_(k,j)=x_j^k`, `1<=k<=q`.

Across translations the map is block diagonal. With source-independent bank parameters, the arithmetic source `G` does not enter this coefficient map at all.

VIS-355 strengthens the conclusion to source-adaptive choice. Fix a compact nondegenerate family in which inverse scales stay in a bounded positive interval, distinct scales have uniform separation, and the number of fibers/scales and `q` are fixed. The block map has constant rank, hence its smallest nonzero singular value has a uniform floor:

`||T_theta c||_2 >= sigma dist(c,ker T_theta)`.

This remains true pointwise when the source chooses `theta=theta(G)` and `c=c(G)`. Adaptivity does not change the worst-case quotient conditioning of the admissible family.

If a fiber has at most `q` scales, the kernel is zero. With more than `q`, the kernel is exactly the known moment-cancellation space `sum_j c_j a_j^(-k)=0`, `k=1,...,q`. Thus small tail coefficients inside the compact family mean motion toward an already-explicit filter-design kernel, not a hidden arithmetic localization effect.

Together with the divided-difference/Riesz controls for the downstream confluent exponential map, the bounded finite-bank chain has no remaining unnamed compact conditioning resource. A source-dependent selector earns new credit only by making something leave this ledger—growing dimension/depth/count, scale or phase degeneration, unbounded range, shrinking windows—or by supplying a genuinely new signed estimate of `G` outside passive parameter selection.

**Boundary.** Nonlinear source operations, infinite representations with controlled truncation, growing/degenerating geometries and direct arithmetic cancellation remain outside the theorem. “Source-adaptive” by itself is not such a resource.