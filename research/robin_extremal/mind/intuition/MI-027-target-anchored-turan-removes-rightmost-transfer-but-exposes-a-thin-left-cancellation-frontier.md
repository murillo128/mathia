# MI-027 — Target-anchored Turán removes rightmost transfer but exposes a thin left-cancellation frontier

**Evidence level:** literature-derived/exact splice from [RE-143](../../findings/RE-143-turan-first-main-theorem-removes-rightmost-transfer-on-the-strong-atoms-rightward-packet.md), refining the Second-Main-Theorem packet/tail budget [RE-139](../../findings/RE-139-turan-second-main-theorem-removes-horizontal-spread-tax.md)--[RE-142](../../findings/RE-142-upper-zero-density-cannot-improve-the-rightmost-transfer-exponent.md).

RE-140--RE-142 normalize finite packets at the rightmost horizontal atom. This removes horizontal spread but introduces an amplitude-transfer factor `G(U,T)`, and RE-142 shows the current upper source envelopes permit the generic loss `G=T^-2+o(1)` even when the Turán mode count is negligible.

RE-143 shows that this transfer loss is not intrinsic to classical power-sum observability. Anchor instead at the algebraically strong target atom `rho_0` and keep only the retained zeros with `beta>=beta_0`. After multiplying by the target damping, the sampled power-sum roots all satisfy `|z_j|>=1`, so Turán's First Main Theorem applies directly. The coherent zeroth sum has one sign because the Robin coefficients lie in a fixed sector. Therefore some point of the physical observation window satisfies

`|S_0^+(u)| >= 2 c_Theta exp(-Lambda_kappa^(1) N_+) M_0(U)`

with no rightmost-amplitude factor and with complexity charged only to the rightward subpacket.

The price is relocated rather than removed. Zeros to the **left** of the target atom are not controlled by this witness and may cancel it. For an algebraically strong target `M_0(U)>=c U^-A`, however, absolute summability of the Robin coefficients and horizontal damping make every zero farther than `H log U/U` to the left negligible to arbitrary algebraic order once `H` is fixed large enough. Up to algebraic accuracy, only a shrinking one-sided slab immediately left of `beta_0` can defeat the target-anchored witness.

This replaces the old rightmost-transfer frontier by a more local relational one: **how much signed Robin mass can actual zeros place in the `O(log U/U)` left neighborhood of a strong atom, and can that thin packet coherently cancel the rightward Turán witness?** Another upper zero-density estimate far from the target is not the right currency unless it controls this one-sided near-left configuration.

The same result clarifies the role of the two Turán theorems. Rightmost anchoring plus the Second Main Theorem prices the whole core through a transfer to the extremal horizontal atom. Target anchoring plus the First Main Theorem keeps the original strong coefficient but only sees roots whose real parts do not decrease relative to it. They are complementary certificates with different remainder problems, not competing constants in one argument.

**Boundary.** RE-143 does not bound the near-left remainder and therefore does not close the full Robin packet. It assumes a finite rightward core before the already-controlled high-height tail is restored. The `O(log U/U)` left width is a sufficient algebraic localization, not claimed optimal. The remaining theorem is source-relational: it must control occupancy, signs or cancellation in that shrinking left slab, or give another target-aware infinite-packet certificate.