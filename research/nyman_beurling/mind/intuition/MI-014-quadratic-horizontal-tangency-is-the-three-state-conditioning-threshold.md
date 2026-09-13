# MI-014 — Dimensionless Menger curvature is the three-state conditioning invariant

**Evidence level:** exact for sufficiently local triples by [NB-102](../../findings/NB-102-dimensionless-menger-curvature-controls-hierarchical-three-state-confluence.md), extending the regular common-scale circumradius law of [NB-101](../../findings/NB-101-local-circumradius-is-the-asymmetric-three-state-shear-scale.md) and the symmetric slice of NB-100. No source theorem for actual zeta-zero triples is claimed.

Canonical Blaschke deflation removes the raw pairwise Cauchy crowding, but a collective three-state shear remains. For any sufficiently local triple of distinct right-half-plane parameters, put

`a=Re lambda_1`,

and let `c(lambda_1,lambda_2,lambda_3)=1/R` be its Menger curvature, with `R` the Euclidean circumradius. The dimensionless curvature

`K = a/R = a c(lambda_1,lambda_2,lambda_3)`

is invariant under the common imaginary translation and positive dilation gauges of the canonical half-line construction. NB-102 proves, uniformly over all pairwise aspect ratios,

`kappa_2(C(lambda_1,lambda_2,lambda_3)) asy (1+K)^4`.

If `K->infinity`, the two collective third-column Cholesky shears are asymptotic to `2K` in magnitude. If `K=O(1)`, the full three-state conditioning stays bounded. A hierarchically tiny pair therefore creates no new singular scale by itself: only the curvature of the whole local triangle matters.

NB-101 recovers the regular common-scale form because for `lambda_j=lambda_*+epsilon w_j+O(epsilon^2)`, the actual circumradius is `epsilon R(w)+O(epsilon^2)`. The older NB-100 “quadratic horizontal tangency” criterion is the symmetric-coordinate expression of bounded Menger curvature. On that slice, first-order transverse bending gives `K~epsilon^-1` while quadratic bending keeps `K=O(1)`.

This makes the source obligation coordinate-free. A Nyman route based on this canonical state system needs a zeta-specific local theorem bounding `a/R` for every relevant near-confluent zero triple, including hierarchical gaps, or it must show that the destination does not require uniform three-state conditioning. Height, simplicity, quartet symmetry and global zero-density control are not substitutes for this local curvature bound.

**Boundary.** NB-102 is a local three-distinct-state theorem. It does not classify larger clusters, repeated zeros requiring derivative/Jordan states, or prove any constraint on actual zeta-zero Menger curvature. Bad canonical conditioning matters for RH only if the target conversion truly consumes this representation uniformly.