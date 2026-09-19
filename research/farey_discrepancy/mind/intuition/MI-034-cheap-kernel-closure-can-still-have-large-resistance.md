# MI-034 — Cheap kernel closure can still have large resistance

**Evidence level:** exact synthesis from [FD-202](../../findings/FD-202-prime-path-cross-mode-differences-collapse-random-multiplicative-energy-to-the-critical-scale.md) and [FD-203](../../findings/FD-203-scalar-anchors-close-the-prime-path-kernel-at-critical-random-cost-but-retain-path-resistance-amplification.md).

FD-202 shows that an exact signed projection can change the scaling of a positive quadratic statistic without changing the underlying Farey observation family. Adjacent differences of normalized reciprocal-prime rows cancel their common long Mertens bulk before squaring, and the resulting prime-path energy has the critical squarefree-random scale `Theta(H)` instead of the diagonal `H^(3/2+o(1))` tariff. Algebraically the only missing direction is the constant shell mode.

FD-203 shows that the dimension of that kernel is not the right measure of the remaining inverse problem. Add any scalar anchor `ell` with `ell(1)=1` and define

`||S||_ell^2=sum_(i=1)^(m-1)|S_i-S_(i+1)|^2+|ell(S)|^2`.

The constant direction is now removed, but the endpoint-difference functional still has the exact dual norm

`||e_1-e_m||_(ell,*)^2=m-1`,

independently of the anchor. Consequently some point evaluation has squared dual cost at least `(m-1)/4`. For an endpoint anchor this order is exact coordinatewise: `||e_i||_*^2=m-i+1`.

The source-cost side behaves differently. The endpoint anchor itself has squarefree-random variance `Theta(K)` on the reciprocal-prime shell, so after the same shell normalization as FD-202 the complete anchored statistic still has expectation `Theta(H)`. **Kernel closure is therefore cheap while propagation through the path is expensive.** The two costs are independent resources.

This distinction is the reusable point. A low-dimensional nullspace can be eliminated by very little additional data while the resulting inverse remains badly conditioned because the observation graph has large effective-resistance diameter. Counting missing dimensions would call the problem solved; the dual geometry says it is not. Conversely, a large representation-space condition number does not prove that the physical source realizes its worst directions.

For the prime shell, `m~K/(2 log K)`. Thus an `H^(1+o(1))` anchored path budget gives the correct square-root scale at the anchored coordinate itself but does not force the same scale uniformly across all shell coordinates by abstract inversion alone. A successful continuation must therefore do at least one of two things: make the anchor itself the downstream witness, avoiding long propagation, or enrich the signed observation graph so that effective resistance falls without repaying the gain in random-multiplicative energy.

**Boundary.** The resistance lower bound is exact for unrestricted shell-coordinate space. FD-203 does not show that its extremizers are attainable by Möbius, by squarefree random multiplicativity, or by the Farey source class. Source-specific compatibility could eliminate high-resistance directions. Nor does the result say that every denser projection is useful: extra edges count only if their source-faithful quadratic cost remains at the critical scale and the resulting statistic still maps to the Farey/Franel destination.
