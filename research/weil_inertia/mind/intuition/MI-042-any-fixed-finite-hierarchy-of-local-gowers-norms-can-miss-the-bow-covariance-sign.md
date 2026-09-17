# MI-042 — Even near-log-log Gowers hierarchies can miss the bow covariance sign

**Evidence level:** exact synthesis from [WI-332](../../findings/WI-332-all-interval-u2-control-still-misses-the-bow-diagonal-variance-scale.md), [WI-333](../../findings/WI-333-square-root-phase-pseudorandomness-still-leaves-diagonal-bow-variance.md), [WI-334](../../findings/WI-334-fixed-order-gowers-uniformity-does-not-force-bow-variance-cancellation.md), and [WI-335](../../findings/WI-335-growing-gowers-hierarchy-still-does-not-force-bow-variance.md). The obstruction is to black-box use of local uniformity norms; it does not describe the actual signed covariance of `Lambda-Lambda_X^sharp`.

WI-333 shows that strong one-point cancellation against every fixed-degree polynomial phase can coexist with full diagonal-scale sliding variance against an arbitrary prescribed unit carrier. WI-334 upgrades that separation from phase tests to every fixed finite hierarchy of local Gowers norms. WI-335 shows that allowing the hierarchy depth to grow does not immediately repair the mismatch.

For bow-scale interval length `K=N^kappa`, one can choose coefficients of size `sqrt(log N)` such that, simultaneously on **every** interval with `K<=|I|<=2K`,

`||b||_(U^s(I))=o(1)` for every `2<=s<=S_N`

whenever

`2^(S_N) log log N=o(log K)`,

while

`sum_x |sum_(j<=K) b_(x+j)u_(x+j)|^2 = (1+o(1))NK log N`

for any prescribed unit-modulus carrier `u`. An explicit representative has

`S_N=log_2 log K-2 log_2 log log N+O(1)=(1-o(1))log_2 log K`.

Thus the fixed-order obstruction was not merely hiding in constants depending on `s`. A generic hierarchy can grow almost to `log_2 log K` and still forget the datum required by the destination. The bow square needs a signed off-diagonal covariance that cancels a macroscopic positive diagonal; small Gowers norms, even through many orders, are not themselves that covariance statement.

The complexity threshold is only a **necessary escape scale for this norm-only strategy**, not a sufficiency theorem. Nothing shows that `U^s` information at `s~log log K`, or at any larger order, forces the desired variance. A route at that scale would still need quantitative bounds strong enough to survive the normalization and an explicit theorem connecting the hierarchy to the signed two-point term.

The reusable lesson is that **increasing the descriptive complexity of a lossy pseudorandomness interface does not restore a destination sign unless the added information actually controls the relevant two-point observable**. A finite PET reduction fails; a slowly growing one also fails throughout the WI-335 range. The honest alternatives are arithmetic covariance information, a source identity that subtracts the diagonal before generic inequalities lose the sign, or a genuinely covariance-sensitive high-complexity theorem rather than another list of small norms.

**Boundary.** The countermodel deliberately lacks prime arithmetic. It does not rule out a signed shifted-prime theorem, a relative linear-forms estimate using the prime majorant, a source identity special to `Lambda-Lambda_X^sharp`, or a theorem at/above the near-`log log K` complexity threshold whose conclusion directly controls the bow variance. WI-335 also gives no sufficiency statement at the threshold. The accepted bow-cancellation clue remains unresolved and must be settled by the actual arithmetic source, not by the generic countermodel.