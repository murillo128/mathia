# MI-026 — Zero-count fidelity is distance to the boundary-zero discriminant, and diagonal reweighting cannot repair its critical-strip breadth law

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, and for all positive diagonal Hilbert reweightings of that eta model by AF-292; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the set of coefficients whose polynomial has a zero on the boundary. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that the normalized radius can deteriorate as breadth grows even when the analytic approximation behaves perfectly well. For raw eta truncations on a contour with left edge `alpha > 0`, the boundary modulus stays uniformly separated from zero while the normalized coefficient-space margin tends to zero. In the RH-relevant regime `alpha < 1/2`, its scale is `N^(alpha-1)`.

AF-292 proves that this critical-strip exponent is not a coordinate-scaling artifact. For an arbitrary positive diagonal metric with weights `d_n`, the normalized margin is comparable to

`1 / sqrt[(sum d_n^2)(sum d_n^-2 n^-2alpha)]`.

Cauchy--Schwarz makes the optimization exact: the best diagonal geometry has `d_n^2 proportional to n^-alpha` and margin comparable to `1 / sum n^-alpha`. Thus every diagonal metric still has vanishing margin for `alpha <= 1`, and when `alpha < 1/2` it cannot improve even the power of `N` over the raw eta coordinates.

The composition rule is therefore breadth-sensitive and representation-sensitive. If an upstream decoder has relative error `eta_N`, protecting the zero count requires `eta_N` to stay below the target margin in the metric actually used. A fixed relative guarantee fails for the raw eta geometry, and coordinatewise Hilbert preconditioning does not change that conclusion in the critical strip.

The reusable lesson is that **source completeness, analytic convergence, coordinate conditioning, and target robustness are separate resources**. A useful repair must alter relational geometry rather than merely rescale coordinates: for example non-diagonal mixing, a nonlinear representation, a target-relevant quotient, or another topology with its own recovery theorem.

**Boundary.** AF-292 classifies only diagonal Hilbert metrics for this fixed-contour eta zero-count target. It does not rule out general positive-definite mixing, nonlinear encodings, quotients, alternative carriers, growing contours, exact zero locations, or a different target topology. None of those alternatives is automatically well conditioned.