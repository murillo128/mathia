# MI-026 — Zero-count fidelity is projective distance to the boundary-zero discriminant, and radial metric repair has an exact integrability price

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, for positive diagonal Hilbert reweightings by AF-292, for arbitrary positive-definite Hilbert metrics under a condition-number budget by AF-293, for uniformly quasisymmetric nonlinear representations with honest transport of the discriminant by AF-294, for the canonical complex-scalar quotient by AF-295, for reciprocal-distance condition geometry by AF-296, and for the full target-radial conformal class by AF-297; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the boundary-zero discriminant. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that this normalized radius can deteriorate as breadth grows even when eta truncations converge correctly on the boundary. AF-292--AF-294 progressively close diagonal Hilbert, bounded-condition dense Hilbert, and uniformly controlled quasisymmetric nonlinear repairs. An order-one represented margin requires the representation itself to become anisotropic/distorted at the shrinking discriminator scale, or the mathematical target/information category to change.

AF-295 identifies the normalization geometrically rather than merely operationally. If the failure set `D` is a complex cone, then

`dist_gap([b], P D) = dist(b,D)/||b||`,

with the corresponding Fubini--Study distance equal to `arcsin(dist(b,D)/||b||)`. The finite Dirichlet boundary-zero discriminant is such a cone because global complex rescaling changes neither the zero set nor the zero count. Therefore AF-290's normalized margin is **exactly the intrinsic projective separation from failure after quotienting global amplitude and phase**.

AF-296 identifies one singular metric response to that collapse: weighting projective path length by reciprocal discriminant distance `1/r` makes the bad set an infinite-distance ideal boundary and turns multiplicative margin loss into additive logarithmic distance.

AF-297 classifies the entire target-radial conformal family. In any proper geodesic metric space with closed bad set `D`, if a conformal path metric has density `phi(r)` depending only on ordinary distance `r=dist(.,D)`, then the exact distance from `r_0` to the level `r=epsilon` is

`int_epsilon^r0 phi(t) dt`,

and the boundary distance is `int_0^r0 phi(t) dt`. Hence for raw margins `r_N -> 0`, a fixed profile has only two outcomes: if `phi` is integrable at zero, the repaired margin still tends to zero; if it is not integrable, the bad set is at infinite distance. **No fixed target-radial conformal profile converts a vanishing raw margin into a finite positive asymptotic margin.**

A scale-dependent finite repair also has a sharp price. If `int_0^rN phi_N(t) dt >= c>0`, then

`ess sup_(0<t<r_N) phi_N(t) >= c/r_N`.

For the eta projective margin `r_N ~ 1/(sqrt(N) H_N(alpha))`, any finite order-one radial repair must therefore reach conformal density at least of order `sqrt(N) H_N(alpha)` somewhere in the collapsing layer, with scalar metric multiplier at least of order `N H_N(alpha)^2`. This is the same reciprocal raw-margin scale exposed by the linear conditioning bill, although the mechanisms are different.

The reusable distinction is therefore stronger: **source completeness, analytic convergence, acquisition conditioning, target robustness, representation distortion, target-null quotienting, and target-aware metric geometry are separate resources**. A target-radial reparameterization cannot provide a finite stable margin for free. A viable geometric repair must either be source-natural for a reason independent of the discriminant, carry nonradial/anisotropic information, add genuinely new source information, or change the target/category with a separately justified theorem.

**Boundary.** AF-297 does not rule out source-derived nonradial or anisotropic metrics, additional markings, a larger target-null quotient, enriched source data, or a different target category. It rules out a broad apparent escape: choosing a nicer fixed function of target distance merely reparameterizes the same collapsing margin, while an `N`-dependent finite repair must explicitly pay reciprocal-margin scale.