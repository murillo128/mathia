# MI-033 — Macroscopic Gamma cost is a rank-one signed height moment, not an unavoidable vertical-range tariff

**Evidence level:** proved for the exterior signed-Poisson sampler regime of NB-148--NB-157, with the sharpened conservation law in [NB-157](../../findings/NB-157-three-height-balancing-annihilates-the-macroscopic-gamma-tariff.md).

NB-156 bounded the completed-Gamma contribution of a vertically macroscopic zero-mass sampler by the absolute envelope

`C_G log(G/H_G)`.

NB-157 identifies the exact leading quantity before taking absolute values. With target charge scale `q_G`, total variation `V_G`, boundary-normalized conditioning `D_G=V_G/(a_G q_G)`, define

`J_G = q_G^(-1) | int log((G+Im w)/G) d mu_G(w) |`.

Then the signed zero conservation law has only the leading Gamma defect

`(1/2) int log((G+Im w)/G) d mu_G(w)`

plus an Euler/boundary error `O(V_G/a_G)`. Consequently a logarithmic target packet still exports logarithmic adverse zero mass whenever

`D_G + J_G = o(log G)`.

The old `C_G log(G/H_G)` term is therefore an envelope, not an intrinsic price for vertical extent. On the mass-zero sampler space the leading Gamma background is one additional linear functional. Two distinct sampled heights cannot cancel both mass and this log-height moment nontrivially, but three heights can, with bounded coefficients, even when the lowest sampled height is only a fixed power of `G`.

This changes the frontier sharply. **Macroscopic vertical range is not itself an escape resource.** A sampler may descend polynomially far while paying zero leading Gamma tariff. To evade the adverse-charge obstruction it must instead make the signed log-height defect genuinely logarithmic, already pay logarithmic boundary conditioning, or exploit arithmetic signed cancellation that changes the conservation argument while retaining useful target charge.

The remaining resource is a coupled one: target charge `q_G`, total variation and boundary gap through `D_G`, the signed log-height moment `J_G`, and the prime/Nyman-side cancellation must be simultaneously compatible. A construction that merely widens the vertical support has not purchased anything unless it changes one of those quantities.

**Boundary.** Gamma balancing does not prove that a three-height sampler has useful target charge or good conditioning. It removes one universal background term; it does not solve the target-selection or prime-side problem.
