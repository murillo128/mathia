# MI-026 — Zero-count fidelity is distance to the boundary-zero discriminant, and controlled representations preserve vanishing margin

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, for all positive diagonal Hilbert reweightings by AF-292, for arbitrary positive-definite Hilbert metrics under a condition-number budget by AF-293, and for uniformly quasisymmetric nonlinear representations with honest transport of the discriminant by AF-294; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the boundary-zero discriminant. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that this normalized radius can deteriorate as breadth grows even when eta truncations converge correctly on the boundary. For a contour with left edge `alpha>0`, the raw margin is comparable to `1/(sqrt(N) H_N(alpha))`; in the RH-relevant regime `alpha<1/2` its power is `N^(alpha-1)`.

AF-292 proves that diagonal rescaling cannot repair that exponent. AF-293 closes the full linear-Hilbert escape: if `G>0` has `kappa(G)<=K`, then the best normalized margin is comparable to

`min(1, sqrt(K)/(sqrt(N) H_N(alpha)))`.

An order-one repair therefore requires `kappa(G_N) asymp N H_N(alpha)^2`, or transform condition number `kappa_2(A_N) asymp sqrt(N) H_N(alpha)` for `G=A* A`. Dense mixing can stabilize the target only by relocating the missing scale into representation anisotropy.

AF-294 shows that this is not an artifact of quadratic norms. Let `rho_X=dist_X(x,D)/d_X(x,a)` and let an injective representation `F` transport `x`, the anchor, and the bad set honestly. If `F` is `eta`-quasisymmetric on the relevant points, then

`1/eta(1/rho_X) <= rho_Y <= eta(rho_X)`.

Thus any family controlled by one distortion function satisfies `rho_X,N -> 0 => rho_Y,N -> 0`. Fixed nonlinear relative geometry may alter the numerical rate of collapse, but cannot turn collapse into a positive asymptotic margin. If `rho_Y,N>=c>0`, the distortion itself must degenerate at the source margin scale: `eta_N(rho_X,N)>=c`.

The reusable distinction is now stronger: **source completeness, analytic convergence, acquisition conditioning, target robustness, and representation distortion are separate resources, and controlled changes of representation preserve the qualitative collapse of a relative discriminator margin**. A claimed repair must explain why its growing anisotropy or nonlinear relative distortion is source-natural, or else change the mathematical problem by altering the target/bad set, quotienting, enriching the data, or leaving the controlled metric category.

**Boundary.** AF-294 requires honest transport of the same discriminant and uniform quasisymmetric control. It does not rule out a family whose distortion degenerates with `N`, a target-relevant quotient, a noninjective compression, an enriched lift carrying genuinely additional information, a different bad set, or a non-quasisymmetric/nonmetric topology. Those are category changes requiring their own fidelity and conditioning theorem; degeneration of distortion is a price to explain, not automatically a disqualification.