# MI-026 — Zero-count fidelity is projective distance to the boundary-zero discriminant, and metric repairs must pay distortion or target-awareness

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, for positive diagonal Hilbert reweightings by AF-292, for arbitrary positive-definite Hilbert metrics under a condition-number budget by AF-293, for uniformly quasisymmetric nonlinear representations with honest transport of the discriminant by AF-294, for the canonical complex-scalar quotient by AF-295, and for reciprocal-distance condition geometry by AF-296; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the boundary-zero discriminant. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that this normalized radius can deteriorate as breadth grows even when eta truncations converge correctly on the boundary. AF-292--AF-294 progressively close diagonal Hilbert, bounded-condition dense Hilbert, and uniformly controlled quasisymmetric nonlinear repairs. An order-one represented margin requires the representation itself to become anisotropic/distorted at the shrinking discriminator scale, or the mathematical target/information category to change.

AF-295 identifies the normalization geometrically rather than merely operationally. If the failure set `D` is a complex cone, then

`dist_gap([b], P D) = dist(b,D)/||b||`,

with the corresponding Fubini--Study distance equal to `arcsin(dist(b,D)/||b||)`. The finite Dirichlet boundary-zero discriminant is such a cone because global complex rescaling changes neither the zero set nor the zero count. Therefore AF-290's normalized margin is **exactly the intrinsic projective separation from failure after quotienting global amplitude and phase**.

AF-296 then identifies the canonical singular metric response to that collapse. On the projective complement of the discriminant, let `r(x)` be Fubini--Study distance to the discriminant and weight infinitesimal path length by `1/r`. The induced condition metric satisfies

`d_cond(x,y) >= |log(r(y)/r(x))|`,

and the distance from a point with margin `r_0` to the level set `r=epsilon<r_0` is exactly `log(r_0/epsilon)`. For eta truncations this turns the projective margin law into recession from every fixed stable core by

`log(sqrt(N) H_N(alpha)) + O(1)`.

This is not a contradiction to AF-294 and not recovered arithmetic information. Condition geometry deliberately leaves the uniformly controlled metric category: the discriminant becomes an ideal boundary at infinite distance, and the conformal factor is built from the target failure set itself. At the eta ray its length scale `r_N^{-1}` matches the transform-conditioning scale `sqrt(N) H_N(alpha)` from AF-293, while the metric-tensor factor matches `N H_N(alpha)^2`; the mechanisms differ, but both expose the reciprocal raw margin as the scale at which canonical projective geometry must cease to be uniformly comparable.

The reusable distinction is therefore stronger: **source completeness, analytic convergence, acquisition conditioning, target robustness, representation distortion, target-null quotienting, and target-aware condition geometry are separate resources**. A claimed repair must either exhibit additional target-null directions, add genuinely new source information, or derive a source-natural geometry independently of the discriminant and prove that it supplies the required scale-dependent distortion.

**Boundary.** AF-296 does not rule out a source-defined geometry that is independently comparable to condition geometry, a larger target-null quotient, noninjective target-relevant compression, enriched source data, a different bad set, or another metric/topological category. It rules out treating reciprocal-distance conditioning itself as evidence that arithmetic instability has disappeared: the construction encodes the target failure locus by definition and merely logarithmizes approach to it.