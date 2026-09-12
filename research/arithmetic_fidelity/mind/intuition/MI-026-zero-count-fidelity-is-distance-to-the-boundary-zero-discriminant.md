# MI-026 — Zero-count fidelity is distance to the boundary-zero discriminant, and Hilbert mixing pays the missing conditioning

**Evidence level:** proved for finite Dirichlet polynomials by AF-290, for raw eta breadth growth by AF-291, for all positive diagonal Hilbert reweightings by AF-292, and for arbitrary positive-definite Hilbert metrics under a condition-number budget by AF-293; transfer from acquisition remains conditional on the actual coefficient-orbit error.

For a finite Dirichlet polynomial `P_b`, AF-290 identifies the exact robustness radius for the zero count inside a fixed zero-free Jordan contour: it is the coefficient-space distance from `b` to the boundary-zero discriminant. This is a target-conditioned quantity, not a consequence of frame conditioning or coefficient recovery alone.

AF-291 shows that this normalized radius can deteriorate as breadth grows even when eta truncations converge correctly on the boundary. For a contour with left edge `alpha>0`, the raw margin is comparable to `1/(sqrt(N) H_N(alpha))`; in the RH-relevant regime `alpha<1/2` its power is `N^(alpha-1)`.

AF-292 proves that diagonal rescaling cannot repair that exponent. For weights `d_n`, the margin is comparable to

`1 / sqrt[(sum d_n^2)(sum d_n^-2 n^-2alpha)]`,

whose optimum is attained at `d_n^2 proportional to n^-alpha`. The best diagonal margin is therefore comparable to `1/sum n^-alpha` and has the same critical-strip power as the raw coordinates.

AF-293 closes the next linear-Hilbert escape. If `G>0` is an arbitrary dense coefficient metric with `kappa(G)<=K`, then the best achievable normalized margin satisfies

`D_(Gamma,N)(K) asymp_Gamma min(1, sqrt(K)/(sqrt(N) H_N(alpha)))`.

Hence bounded-condition non-diagonal mixing cannot improve the raw breadth exponent. An order-one margin requires, up to contour constants,

`kappa(G_N) asymp N H_N(alpha)^2`.

If `G=A* A`, this is `kappa_2(A_N) asymp sqrt(N) H_N(alpha)`, exactly the reciprocal scale of the raw normalized margin. Dense mixing can therefore stabilize the target, but only by relocating the same conditioning bill into the representation map.

The reusable distinction is now sharper: **source completeness, analytic convergence, acquisition conditioning, representation distortion, and target robustness are separate resources**. A linear Hilbert change of coordinates is not a free repair when its anisotropy grows at the reciprocal target-margin scale.

**Boundary.** AF-293 does not rule out a nonlinear representation, a target-relevant quotient, a non-Hilbert topology, or an anisotropic geometry justified independently by the source rather than designed to encode the eta coefficient ray. A diverging condition number is a price to explain, not by itself a proof that a representation is useless.