# MI-060 — Nested Vandermonde chains pay cumulative Newton separation costs

**Evidence level:** exact/classical clustered-Vandermonde synthesis from [VIS-364](../../findings/VIS-364-nested-vandermonde-chain-cumulative-scale-spectrum.md), sharpening the recursive-degeneration escape left by VIS-363. The underlying clustered-Vandermonde conditioning is classical; the line-specific content is its exact fixed-depth Wang specialization.

A second inner scale is not automatically a new compact cancellation resource. VIS-364 prices the maximally nested positive chain

`t_0=0`, `t_r=epsilon^(kappa_r)`, `0<kappa_1<...<kappa_(q-1)`,

by passing from monomials to the Newton basis. If `K_0=0` and `K_r=sum_(i=1)^r kappa_i`, the degree-`q-1` sampling matrix has singular spectrum

`s_(r+1) asymp epsilon^(K_r)`, `0<=r<=q-1`.

Each new direction therefore pays every coarser separation already crossed. The smallest singular value is not controlled only by the finest distance `epsilon^(kappa_(q-1))`; it pays the cumulative product scale `epsilon^(kappa_1+...+kappa_(q-1))`.

The mechanism is exact. Newton interpolation triangularizes the nested chain, and its diagonal pivots are the products of successive node separations. After column normalization the remaining triangular factors are uniformly conditioned, so the pivot valuations are the full singular-value valuations rather than only a determinant product identity.

For the fixed-depth Wang coefficient map this gives

`s_q(A) asymp rho^(q-1) epsilon^(K_(q-1))`

under fixed positive row weights and the usual compact positive anchor assumptions. Thus a finite one-branch hierarchy of polynomially nested positive scales remains source-free conditioning geometry: the entire loss is priced by a cumulative Newton ledger.

The compact escape left after VIS-363 must therefore be structurally deeper than “add another nested scale.” It needs branching cluster trees with competing local ranks or masses, recursively changing active subspaces, scale relations not reducible to one finite valuation chain, coefficient geometry outside the positive diagonal Hilbert setting, or genuinely source-dependent signed information.

**Boundary.** VIS-364 treats a fixed-depth one-dimensional nested chain with polynomial scale ordering and positive bounded weights. It does not classify arbitrary branching cluster trees, incomparable scale nets, growing depth, nonpositive coefficient geometry or source-dependent operators. The result is a conditioning benchmark, not a new estimate for the Chebyshev remainder or RH.