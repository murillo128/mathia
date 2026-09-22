# MI-060 — Finite Mellin packets cannot supply the missing divisor-depth exponent

**Evidence level:** exact source-demand synthesis from [FD-261](../../findings/FD-261-positive-capacity-phase-threshold-vs-first-row.md), [FD-263](../../findings/FD-263-block-location-controls-divisor-replication.md), [FD-266](../../findings/FD-266-deep-positive-mertens-blocks-need-negative-divisor-ancestry.md), and [FD-267](../../findings/FD-267-finite-mellin-zero-packets-have-only-linear-divisor-depth-amplification.md), refining MI-058--MI-059.

The canonical positive-capacity route needs more than arithmetic amplitude. FD-261 shows that, at the same source exponent as the first switched row, a deep-band obstruction can become decisive no later than that row only if its divisor-depth exponent exceeds

`2-beta`, with `beta=log_2(3/2)`.

FD-263 and FD-266 explain where such an exponent could in principle come from: source blocks are replicated according to their divisor incidence, and the destination sees the one-sided mass that survives negative proper-divisor ancestry. FD-267 now rules out the simplest spectral way of populating that geometry. For a fixed finite Mellin packet `F(t)=sum_j a_j t^(rho_j)` with `Re rho_j<=theta<1`, consecutive block differencing costs one power of the block index, while divisor replication restores at most that one power. The resulting dyadic field obeys

`sum_(x<d<=2x) |G_(F,N)(d)| <<_theta W(F) N^theta x`.

So every fixed packet has effective depth exponent at most `1`, even before one-sided sign losses are charged. Fixed logarithmic residue factors do not change the polynomial exponent. A finite collection of rightmost zero modes may carry the arithmetic exponent `theta`, but it cannot by itself manufacture the superlinear depth amplification required by the positive-capacity comparison.

The quantitative escape is now explicit. If the weighted packet complexity grows as `W_D=D^(omega+o(1))`, then the effective depth exponent is at most `1+omega`; crossing the first-row comparison requires

`omega > 1-beta = 0.4150374992...`.

Thus a spectral continuation must pay polynomially growing weighted complexity, or else place the missing growth in an explicit-formula remainder whose own divisor-range amplitude grows polynomially. In the simple-zero calibration the derivative weight is naturally `1/|zeta'(rho)|`, but FD-267 proves no zero-sum estimate of the required size.

This separates two previously conflated hopes. Divisor incidence can amplify arbitrary block data only according to the exact replication ledger, while a fixed Mellin packet is too smooth across consecutive blocks to feed that ledger at superlinear depth. The remaining source theorem must therefore create genuinely growing spectral complexity, a stronger remainder, or a different repair architecture; merely adding a bounded number of distinguished zeros is not a new depth resource.

**Boundary.** The conclusion is specific to the canonical full-grid divisor smoothing and to packets/remainders controlled in the norms stated in FD-267. It does not exclude a growing packet with sufficiently large weighted complexity, a signed prime-side cancellation theorem, switched-only repairs with different intermediate motion, or another source representation. It is a route-pruning result, not a Möbius-sign theorem or an RH implication.