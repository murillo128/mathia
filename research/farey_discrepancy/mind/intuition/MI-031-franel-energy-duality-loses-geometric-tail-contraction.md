# MI-031 — Franel energy duality loses geometric tail contraction

**Evidence level:** exact synthesis from [FD-193](../../findings/FD-193-geometric-square-root-band-has-explicit-cumulative-inverse.md) through [FD-195](../../findings/FD-195-franel-duality-has-a-nonvanishing-cost-on-geometric-quotient-witnesses.md). The GCD-matrix/Franel identity and Hilbert-space duality are classical; the Mathia content is the exact comparison with the geometric signed-Fourier inverse.

At and above the geometric square-root coverage threshold, the retained signed-Fourier data recover the cumulative source with a uniformly stable explicit inverse. On the geometric witness corresponding to source index `k~n`, the relevant raw inverse row contracts like `2^omega(k)/k=n^(-1+o(1))`. It is therefore tempting to expect the classical scalar Franel energy to inherit the same shrinking cost.

FD-195 shows that it does not. If `K_H` is the Franel/GCD quadratic form, the sharp Hilbert dual cost of the same coordinate is

`(K_H^(-1))_(k,k)=k^2 sum_(m<=H/k) mu(m)^2/J_2(km)`.

Along the geometric witnesses this converges to a positive constant, with limiting value `zeta(2) prod_(p|k)(1+p^(-2))`. The source direction that is cheap in the raw `l_infinity` inverse is therefore order one in the scalar Franel-energy dual geometry.

This is a destination-topology effect, not a contradiction. Exact source information can survive the observation map while a subsequent quadratic compression destroys the inverse contraction needed for a sharper pointwise consequence. At `H~n^2`, the RH-equivalent Franel scale combined with generic one-horizon Hilbert duality yields only `M(n)=O(n^(1+epsilon))`; obtaining square-root Mertens by that route would require a substantially smaller Franel energy than RH itself supplies.

The reusable lesson is that **stable inversion is norm-specific**. Before transporting a source-recovery theorem into a scalar discrepancy criterion, compute the dual norm of the actual destination witness. A contractive inverse in the raw coordinate topology can become noncontractive after quadratic aggregation even when no algebraic information has been lost.

**Boundary.** This rules out only the generic one-horizon Franel/GCD energy duality route for these geometric quotient witnesses. It does not show that Franel discrepancy is useless, exclude cross-horizon cancellation, source-dependent relations, nonlinear statistics or other destination norms, and it does not weaken the classical Franel--Landau equivalence with RH.
