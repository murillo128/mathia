# MI-011 — Sequential physical elimination turns source attenuation into a complementary angle defect

**Evidence level:** exact on every finite strictly positive canonical section through PF-315. Infinite-section convergence and the required singular-value/ideal estimates remain open.

PF-281 identifies the physical target as the energy-normalized angle between the full physical-low space `P=C+L` and the physical-high space `H`. PF-311 then shorts the retained nonconstant low modes `L` and exposes the conditional constant/high angle `T_H`. PF-315 determines exactly how that conditional channel sits inside the original physical angle.

After the sequential elimination, let

`Z_LH = J_LL^(-1/2) J_LH J_HH^(-1/2)`

be the direct retained-low/high angle and

`V_H = R_H^(1/2) J_HH^(-1/2)`

be the residual physical-high input map. Up to a unitary change of physical-low energy coordinates,

`T_(P/H) = (T_H V_H, Z_LH)^T`,

while

`V_H* V_H = I-Z_LH*Z_LH`

and therefore

`I-T_(P/H)*T_(P/H) = V_H*(I-T_H*T_H)V_H`.

The key point is that `V_H` is not an arbitrary source map. Any direction suppressed before entering `T_H` is suppressed precisely because the direct `L/H` angle is already close to isometric there. Conversely, if `Z_LH` has a uniform gap from one, then `V_H` is uniformly invertible and cannot hide bad singular-value behavior of `T_H`.

This gives an exact two-channel dichotomy for the full physical angle. Either `Z_LH` itself carries a heavy/noncompact source-reached range, or the remaining burden is the conditional factor `T_H V_H`. There is no third free operator-norm source-amplification or source-avoidance mechanism between them. In particular, estimating `T_H` alone can be stronger than necessary when `Z_LH` has no gap, while estimating a free-standing Green/source map can miss the complementary direct channel that pays for its attenuation.

**Boundary.** PF-315 is exact finite-section Schur geometry, not compactness or weak-trace control. The infinite physical problem still requires a common limiting realization plus singular-value counting for `Z_LH` and `T_HV_H`, followed by the symmetric reassembly and signed target composition gates.