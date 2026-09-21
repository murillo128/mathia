# MI-077 — Target pairings change projection mismatch, not source-Gram strength

**Evidence level:** exact finite-dimensional destination identity from [NB-272](../../findings/NB-272-target-cross-terms-cannot-supply-the-missing-k-scale-gram-repair.md), interpreted together with the resolved-channel scale law of [NB-269](../../findings/NB-269-resolved-multi-shell-hardy-projection-compresses-a-shallow-matched-ford-residue-into-a-1-over-k-center-spike.md) and [NB-271](../../findings/NB-271-inverse-gram-anchor-criterion-forces-k-scale-operator-growth-for-any-off-diagonal-ford-channel-repair.md). No asymptotic estimate for the canonical Nyman target is supplied by this identity.

For a resolved synthesis map `S_K`, source Gram `R_K=S_K^*S_K`, target pairing `b_K=S_K^*g`, and Euler anchor `e_K^*c=1`, completing the square gives the exact constrained residual

`inf ||g-S_K c||^2 = delta_K^2 + |mu_K|^2/(e_K^*R_K^(-1)e_K)`,

where

`delta_K=dist(g,ran S_K)`

and

`mu_K=1-e_K^*R_K^(-1)b_K`.

The target therefore changes the unconstrained projection and the scalar compatibility with the Euler anchor, but it does **not** add a positive coefficient-space Hessian: the quadratic form in `c` is still exactly `R_K`. A target cross term cannot be reinterpreted as the missing positive Gram repair required by NB-271.

In the resolved NB-269 regime `R_K asymp I`, the denominator is `Theta(K)`. Hence the target mismatch contributes only `Theta(|mu_K|^2/K)`. A bounded, or more generally `o(sqrt(K))`, mismatch cannot create an order-one floor; an order-one obstruction can instead come from a nonvanishing section defect `delta_K`, from `|mu_K|=Omega(sqrt(K))`, or from a genuinely new source-source quadratic component outside the resolved channel.

This sharpens the destination audit. “Target-sensitive structure” is not one resource. Projection defect, affine-anchor mismatch and source-source Gram strength are three different currencies. Only the last can supply the `Omega(K)` operator growth tested by NB-271; the first two must be estimated directly on the actual Nyman target.

**Boundary.** The identity does not show that `delta_K` or `mu_K` vanish, grow, or remain bounded for the canonical target. Uniform control of `R_K` and `||g||` alone still permits `|mu_K|=O(sqrt(K))`. Nor does the identity rule out an additional exact source map whose Gram has rank-growing anchor-aligned strength. It removes only the idea that the ordinary target cross term itself is such a Gram correction.
