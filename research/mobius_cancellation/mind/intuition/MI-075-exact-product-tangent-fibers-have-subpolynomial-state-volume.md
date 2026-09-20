# MI-075 — Exact fixed-product tangent fibers have only subpolynomial state volume

**Evidence level:** exact arithmetic synthesis from [MC-419](../../findings/MC-419-multiaxis-positive-kernels-can-multiply-bandwidth.md), [MC-420](../../findings/MC-420-support-lattice-rank-controls-stationary-positive-bandwidth.md), [MC-422](../../findings/MC-422-hyperbolic-shell-taxes-factor-axis-bandwidth.md), and [MC-423](../../findings/MC-423-exact-product-fibers-have-subpolynomial-tangent-volume.md). The subpolynomial conclusion assumes fixed factor depth and exact product preservation; it does not classify near-tangent motion across neighboring fibers.

For fixed `d>=2` and product `m`, the exact integer tangent states are the ordered factorization fiber

`F_d(m)={(u_1,...,u_d) in N^d: u_1...u_d=m}`.

If `m=prod_p p^(a_p)`, then

`|F_d(m)|=d_d(m)=prod_p binom(a_p+d-1,d-1) <= tau(m)^(d-1)=m^(o(1))`.

Thus the continuous logarithmic tangent dimension `d-1` does not translate into a polynomial number of arithmetic states. If a rank-`r` rectangular translation family with side lengths `H_1,...,H_r` is supposed to give genuinely distinct cells inside one exact product fiber, injectivity forces

`prod_j H_j <= d_d(m)=m^(o(1))`.

At `m asymp X`, exact product redistribution at fixed depth therefore cannot supply `X^delta` effective translation volume for any fixed `delta>0`. This closes the literal exact-tangent interpretation of the multiaxis bandwidth escape left open by MC-422.

There is a second, independent restriction on source phase. For every completely multiplicative `chi`,

`prod_j chi(u_j)=chi(m)`

throughout `F_d(m)`. Exact redistribution may alter individual factor phases or sieve coefficients, but the total multiplicative source phase is invariant along the fiber. Tangency removes shell-normal motion precisely where the raw product character also loses variation.

The surviving geometry must therefore change something more than the allocation of a fixed product. A near-tangent sheared family may move through many neighboring product fibers while staying inside the short shell; growing factor depth can change the ordered-factorization count; or a transformed nonseparable phase/coefficient structure can carry information not determined by the total product. Each route must be credited only after collisions, shell boundary loss, source stationarity and positive-closure costs are computed on the actual family.

**Boundary.** The estimate `d_d(m)=m^(o(1))` is for fixed `d`; it is not uniform over arbitrary growing depth. The state-count conclusion concerns exact product preservation and injective effective cells. It does not say that factorization fibers are analytically useless, does not exclude coefficient variation inside a fiber, and does not constrain near-tangent motion across products. No Möbius estimate, Mertens bound or RH consequence is inferred.