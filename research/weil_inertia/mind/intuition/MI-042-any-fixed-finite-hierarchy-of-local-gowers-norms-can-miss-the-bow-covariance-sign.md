# MI-042 — Any fixed finite hierarchy of local Gowers norms can miss the bow covariance sign

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-all-interval-u2-control-still-misses-the-bow-diagonal-variance-scale.md), [WI-333](../../findings/WI-333-square-root-phase-pseudorandomness-still-leaves-diagonal-bow-variance.md), and [WI-334](../../findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md). The obstruction is to black-box use of finitely many fixed-order local uniformity norms; it does not describe the actual signed covariance of `Lambda-Lambda_X^sharp`.

WI-333 already shows that strong one-point cancellation against every fixed-degree polynomial phase can coexist with full diagonal-scale sliding variance against an arbitrary prescribed unit carrier. WI-334 upgrades that separation from phase tests to the standard higher-order uniformity hierarchy.

For any fixed `S` and bow-scale interval length `K=N^kappa`, one can choose coefficients of size `sqrt(log N)` whose local `U^s` norms tend to zero by a power of `K` simultaneously for every `2<=s<=S` and **every** interval with length between `K` and `2K`, while

`sum_x |sum_(j<=K) b_(x+j) u_(x+j)|^2 = (1+o(1)) N K log N`

for any prescribed unit-modulus carrier `u`. The construction is a single Rademacher realization satisfying both properties.

Thus moving from `U^2` to arbitrarily high but fixed Gowers order does not repair the logical mismatch. Fixed-order Gowers smallness controls finite-complexity additive patterns; the bow square demands a signed two-point covariance whose off-diagonal part cancels a diagonal of macroscopic size. A finite PET or fixed-degree Taylor reduction that consumes only `U^2,...,U^S` cannot manufacture that missing sign.

The reusable lesson is stronger than “one-point pseudorandomness is insufficient.” **Any proof interface that records only a fixed finite hierarchy of local Gowers uniformity can forget exactly the covariance sign needed at the destination.** To cross the WI-195 gate one needs arithmetic two-point information, a source identity that subtracts the diagonal before generic inequalities lose the sign, or a quantitatively different norm/order regime whose theorem itself controls the required covariance rather than merely more finite-complexity patterns.

**Boundary.** The countermodel deliberately lacks prime arithmetic. It does not rule out a `K`-dependent Gowers order with sufficiently quantitative bounds, nor a theorem using the signed two-point structure of the von Mangoldt residual. Those possibilities remain live only if they are connected explicitly to the `o(XK log X)` bow variance scale.