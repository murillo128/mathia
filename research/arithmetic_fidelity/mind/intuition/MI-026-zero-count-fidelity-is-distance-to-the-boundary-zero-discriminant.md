# MI-026 — Zero-count fidelity is projective distance to the boundary-zero discriminant, and controlled representations preserve vanishing margin

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, for positive diagonal Hilbert reweightings by AF-292, for arbitrary positive-definite Hilbert metrics under a condition-number budget by AF-293, for uniformly quasisymmetric nonlinear representations with honest transport of the discriminant by AF-294, and for the canonical complex-scalar quotient by AF-295; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the boundary-zero discriminant. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that this normalized radius can deteriorate as breadth grows even when eta truncations converge correctly on the boundary. AF-292--AF-294 progressively close diagonal Hilbert, bounded-condition dense Hilbert, and uniformly controlled quasisymmetric nonlinear repairs. An order-one represented margin requires the representation itself to become anisotropic/distorted at the shrinking discriminator scale, or the mathematical target/information category to change.

AF-295 identifies the normalization geometrically rather than merely operationally. If the failure set `D` is a complex cone, then

`dist_gap([b], P D) = dist(b,D)/||b||`,

with the corresponding Fubini--Study distance equal to `arcsin(dist(b,D)/||b||)`. The finite Dirichlet boundary-zero discriminant is such a cone because global complex rescaling changes neither the zero set nor the zero count. Therefore AF-290's normalized margin is **exactly the intrinsic projective separation from failure after quotienting global amplitude and phase**.

For eta truncations, projectivization preserves the AF-291 decay law. Likewise, changing the underlying projective Hilbert metric inherits AF-293's condition-number threshold. The collapse is therefore angular/projective rather than a radial artifact caused by carrying an irrelevant scalar coordinate.

The reusable distinction is now stronger: **source completeness, analytic convergence, acquisition conditioning, target robustness, representation distortion, and target-null quotienting are separate resources, but the canonical scalar quotient is already paid for by the normalized discriminant margin itself**. A claimed quotient repair must exhibit additional target-null directions beyond global `C*` scaling and prove that the resulting quotient geometry is source-natural and still faithful to the final zero-count target.

**Boundary.** AF-295 closes only the complex-scalar gauge for homogeneous failure sets. It does not rule out a larger target-null quotient, noninjective target-relevant compression, enriched source data, a different bad set, or a non-Hilbert/non-quasisymmetric geometry. Those are genuine category changes requiring their own fidelity and conditioning theorem; they cannot be credited merely because projectivization sounds like a new representation.