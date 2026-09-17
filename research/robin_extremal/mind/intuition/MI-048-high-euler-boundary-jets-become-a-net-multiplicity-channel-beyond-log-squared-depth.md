# MI-048 — High Euler boundary jets become a net-multiplicity channel beyond log-squared depth

**Evidence level:** exact synthesis from [RE-188](../../findings/RE-188-logarithmic-chebyshev-growth-cuts-the-euler-jet-spatial-tariff-to-linear.md) and [RE-189](../../findings/RE-189-high-euler-boundary-jets-collapse-to-net-multiplicity-past-log-squared-depth.md). The log-squared saturation statement is exact for factorial-normalized derivatives of finite prime packets in a fixed multiplicative selector window; it is not a full rigidity theorem for arbitrary Euler observables.

The matched-control program previously showed that growing scalar Euler-jet depth remains repairable throughout a large sub-log-squared range. RE-189 adds a different obstruction at the opposite end: sufficiently high scalar boundary derivatives cease to become more prime-resolving even before any repair construction is considered.

For one Euler factor with `L=log q`, the normalized `j`th boundary derivative has the exact partial-fraction expansion

`U_j(q)/(j-1)! = 1 + 2 Re sum_(k>=1) (L/(L+2pi i k))^j`.

Once `j` is at least a constant multiple of `L^2`, the nonzero singularity terms are exponentially attenuated:

`|U_j(q)/(j-1)! - 1| <= C exp(-c j/L^2)`.

Thus every prime on the same logarithmic scale approaches the same normalized coordinate. For a finite signed packet in a fixed multiplicative window, the high jet approaches its **net multiplicity**; a zero-net-multiplicity packet becomes exponentially small. The prime-location information survives only in exponentially weak corrections.

This changes the scalar-depth picture qualitatively. Below the currently constructed repair range, increasing depth may add genuinely distinct scalar constraints. But after the `j~(log p)^2` crossover, factorial-normalized depth is no longer a monotone proxy for source information: the coordinates collapse toward a common mode. More derivatives can mean less robust location discrimination.

The reusable lesson is that **scalar depth has both a repair-cost regime and an intrinsic saturation regime**. Apparent rigidity cannot be inferred merely from making the jet family arbitrarily deep. A source selector must either exploit the intermediate window before log-squared saturation, renormalize and recover the exponentially small nonzero modes with justified conditioning, or introduce a joint/nonlocal invariant that does not collapse to net multiplicity.

**Boundary.** RE-189 does not close the intermediate gap between the current constructive non-rigidity range and the log-squared saturation scale, and it does not prove that all possible derivative renormalizations are useless. Extracting the exponentially small prime-dependent corrections is an inverse-conditioning problem whose cost has not been identified here.