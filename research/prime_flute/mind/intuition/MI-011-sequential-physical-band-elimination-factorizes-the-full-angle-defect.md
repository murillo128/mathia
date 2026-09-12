# MI-011 — Sequential physical elimination reduces the weak-trace endpoint to two visible angle channels

**Evidence level:** exact on every finite strictly positive canonical section through PF-316. Compatible infinite-section realization and the required channel singular-value estimates remain open.

PF-281 identifies the physical target as the energy-normalized angle between the full physical-low space `P=C+L` and the physical-high space `H`. PF-311 shorts the retained nonconstant low modes `L` and exposes the conditional constant/high angle `T_H`. PF-315 determines exactly how that conditional channel sits inside the original physical angle:

`T_(P/H) ~= (T_H V_H, Z_LH)^T`,

`V_H*V_H=I-Z_LH*Z_LH`.

PF-315 already shows that attenuation into `T_H` is complementary to saturation of the direct `L/H` angle `Z_LH`. PF-316 makes that complementarity quantitative without assuming a uniform gap. Writing the polar decomposition `V_H=W_H D_H`, the defect `C_H=I-D_H` satisfies

`s_j(C_H)=1-sqrt(1-s_j(Z_LH)^2) <= s_j(Z_LH)^2`.

Since `T_H W_H=T_HV_H+T_HW_HC_H`, Fan's inequality yields

`s_(2j-1)(T_H) <= s_j(T_HV_H)+s_j(Z_LH)^2 <= s_j(T_(P/H))+s_j(T_(P/H))^2`.

Thus a conditional singular direction cannot be hidden by a small residual input: making `V_H` small forces the direct channel `Z_LH` to become correspondingly visible. At the compactness and weak-trace endpoints this closes the previous gap completely:

`T_(P/H) in S_(1,infinity)  <=>  T_H in S_(1,infinity) and Z_LH in S_(1,infinity)`,

with the analogous compactness statement and finite-section Schatten consequences.

The residual map `V_H` remains essential for exact representation but is not a third endpoint regularizer. The physical endpoint burden is exactly the pair `(T_H,Z_LH)`. A proof may estimate the two channels by different mechanisms, but failure of either one is already a full-angle obstruction.

**Boundary.** PF-316 is singular-value calculus on the canonical finite-section factorization and compatible limiting realizations; it does not prove either channel is compact or weak trace, construct the infinite operator by itself, close symmetric reassembly, or supply the final signed target composition.