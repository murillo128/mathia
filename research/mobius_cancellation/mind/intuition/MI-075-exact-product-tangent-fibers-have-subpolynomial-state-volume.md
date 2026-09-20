# MI-075 — Exact fixed-product tangent fibers have only subpolynomial state volume

**Evidence level:** exact arithmetic synthesis from [MC-419](../../findings/MC-419-multiaxis-positive-kernels-can-multiply-bandwidth.md), [MC-420](../../findings/MC-420-support-lattice-rank-controls-stationary-positive-bandwidth.md), [MC-422](../../findings/MC-422-hyperbolic-shell-taxes-factor-axis-bandwidth.md), [MC-423](../../findings/MC-423-exact-product-fibers-have-subpolynomial-tangent-volume.md), and the whole-shell extension [MC-424](../../findings/MC-424-fixed-depth-factor-lifts-cannot-amplify-shell-state-exponent.md). The subpolynomial fiber conclusion assumes fixed factor depth and exact product preservation.

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

MC-424 shows that moving to neighboring product fibers does not restore a *state-count* gain at fixed depth: the union of all factorization fibers in a shell of width `X^(theta+o(1))` still has only `X^(theta+o(1))` states. The exact-fiber phase invariance above remains stronger and fiber-specific, but near-tangent shears can no longer be credited with an extra polynomial number of distinct factor states merely because they cross fibers. The remaining routes are analytic cancellation in the weights, extra arithmetic labels or transformed phases not determined by the factor tuple, boundary-crossing correlation families, or sufficiently growing factor depth; the whole-shell budget and growing-depth threshold are recorded in `MI-076`.

**Boundary.** The estimate `d_d(m)=m^(o(1))` is for fixed `d`; it is not uniform over arbitrary growing depth. The state-count conclusion in this note concerns one exact product fiber, while MC-424 handles the full short shell. Neither result says that factorization states are analytically useless, bounds coefficient cancellation, or yields a Möbius, Mertens or RH estimate.