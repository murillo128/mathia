# MI-068 — Qutrit residual shape has an exact sector-anisotropic Gaussian null

**Evidence level:** exact finite-dimensional synthesis from [VIS-389](../../findings/VIS-389-qutrit-rank-one-spectral-profile-is-one-dimensional-after-source-and-energy-conditioning.md), [VIS-390](../../findings/VIS-390-qutrit-isotropic-tangent-residual-has-exact-uniform-conditional-null.md), and [VIS-391](../../findings/VIS-391-sector-anisotropic-qutrit-residual-null.md).

VIS-389 reduces the generic rank-one qutrit positive spectral profile to one residual coordinate after the source cubic invariant and scalar defect rate are fixed. VIS-390 then shows that under isotropic Gaussian/Haar tangent orientation the three two-dimensional sector energies are `Dirichlet(1,1,1)`, making the normalized residual coordinate `u` conditionally uniform.

VIS-391 shows that uniformity of `u` is not the robust null; exact **calibratability** is. Let the three root-sector tangent blocks be independent centered Gaussians with fixed variances `sigma_i^2 I`, and write `lambda_i=(2 sigma_i^2)^(-1)`. After normalizing by total positive energy, the sector weights have density

`2 lambda_1 lambda_2 lambda_3 / A(w)^3`,

where `A(w)=sum_i lambda_i w_i`. On a fixed first-moment slice the admissible weight vector is affine in the single residual coordinate `u`, so `A(w)` becomes `A_L+u(A_U-A_L)`. The conditional density is therefore an explicit inverse cube, and its conditional CDF `F_lambda(u|m_1)` maps the residual exactly to `Uniform(0,1)`. Equal sector variances recover VIS-390 as the constant-density special case.

This changes what an extreme residual can mean. Raw `u` measures position in the one-dimensional qutrit shape fibre, but sector-dependent nuisance scales can tilt its law strongly without introducing arithmetic structure. A candidate anomaly must therefore be assessed in the calibrated coordinate `v=F_lambda(u|m_1)` under nuisance parameters fixed independently of the candidate being tested. Estimating the sector scales from the same residual realization and then applying the probability transform would turn the control into an adaptive fit and could erase genuine source dependence.

The reusable distinction is between a **source-free coordinate** and a **source-free law family**. Quotienting symmetry leaves one genuine geometric degree of freedom, but nuisance anisotropy can still move probability mass along that degree. Exact knowledge of the nuisance family does not eliminate the coordinate; it supplies the correct conditional baseline against which source-specific occupation must be measured.

**Boundary.** The null assumes independent centered Gaussian sector blocks with fixed sectorwise isotropy and independently specified variance ratios. Rejection of this family does not by itself identify arithmetic structure, because non-Gaussian dependence, within-sector anisotropy, admissibility constraints or other source-free mechanisms may also alter the residual law. VIS-391 supplies a stronger exact control, not a Wang destination gain or an RH implication.