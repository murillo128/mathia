# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Test intrinsic source-subspace localization beyond calibrated qutrit nuisance nulls

VIS-367--VIS-386 progressively remove source-free conditioning, similarity-orbit, generator-coordinate and tangent-amplitude artifacts. The intrinsic centered source subspace `S` carries a commutator Laplacian `Delta_S`; after removing the exact commutant component, the scale-free observable is the positive spectral probability measure seen by the normalized Gram tangent. Its first moment is the scalar defect rate, and super-mean cumulative mass has a universal Markov floor, so neither raw low-mode mass nor an order-one super-mean CDF window is source evidence by itself.

VIS-387 closes the normalized spectral-shape escape completely for qubits: on `Herm_0(2)`, the full positive spectral distribution is already determined by source rank and scalar defect rate. VIS-388 then identifies the minimal higher-dimensional capacity. For `d=3`, source rank one, the three positive root-sector eigenvalues are fixed by the cubic source invariant `t^2=tr(E^3)^2`; generic tangents with the same first moment can nevertheless have different spectral measures. This is algebraic capacity, not arithmetic specificity.

VIS-389 shows that the generic qutrit capacity is only one-dimensional after the obvious source and energy coordinates are fixed. If the positive support is `q_1<q_2<q_3` and `m_1` is the scalar defect rate, then the second moment `m_2` determines all three spectral weights by the Vandermonde/Lagrange formula. Equivalently, conditional on `(t^2,m_1)`, every normalized positive spectral profile is a function of one residual shape scalar. At the symmetry-enhanced qutrit boundaries the residual degree disappears entirely.

VIS-390 supplies an exact source-free null for that last scalar under Haar-isotropic tangent orientation. The three two-dimensional sector energies are `Dirichlet(1,1,1)`, so conditional on the observed `m_1`, the normalized residual coordinate

`u=(m_2-L(m_1))/(U(m_1)-L(m_1))`

is exactly `Uniform(0,1)` once `t^2` fixes the support.

VIS-391 strengthens the nuisance class substantially. If the three root-sector tangent blocks are independent centered isotropic Gaussians with arbitrary fixed sector variances `sigma_i^2`, the normalized sector weights have the scaled-Dirichlet density proportional to `A(w)^(-3)`, where `A(w)=sum_i lambda_i w_i` and `lambda_i=(2 sigma_i^2)^(-1)`. Restricting to a fixed first moment makes `A` affine in the residual coordinate `u`, so the exact conditional density is proportional to an inverse cube. Its closed-form conditional CDF `F_lambda(u|m_1)` uniformizes the residual exactly. The isotropic VIS-390 null is only the equal-variance special case.

The minimal qutrit test must therefore distinguish arithmetic structure from **sector anisotropy itself**, not merely from isotropy. The nuisance rate ratios must be independently specified, estimated from external/control information, or otherwise fixed before the candidate residual is scored; fitting them to the same candidate and then uniformizing would erase the very deviation being tested. Once the nuisance law is fixed, use the calibrated variable `v=F_lambda(u|m_1)` and ask whether the actual Wang-admissible family departs from uniformity under controls preserving source cubic geometry, admissibility, coarse Gram structure, block resources and other nonarithmetic causes of tangent anisotropy. Rejection of this stronger null is still only evidence against the calibrated Gaussian-sector control, not yet arithmetic specificity.

## Quotient universal compact geometry before crediting a Wang gain

For any proposed positive-Hilbert improvement, first reduce the source to the exact normalized statistic, price Vandermonde/capacity collapse, expose the full relative metric, restrict the differential to the true simultaneous-similarity orbit, replace arbitrary generator coordinates by the intrinsic centered source subspace, remove tangent-amplitude normalization, freeze the ambient Hilbert metric and numerical-rank rule, and calibrate both source-subspace and tangent-orientation nulls before interpreting nonlinear low modes.

The dimension-sensitive gate is now explicit. `d=2` has no independent normalized spectral shape. Generic `d=3,r=1` has exactly one residual shape coordinate after source conjugacy and scalar defect are conditioned out, and a whole three-parameter sectorwise Gaussian family can be exactly calibrated through a conditional probability transform. Higher dimension/rank may have larger spectral support and additional shape degrees, but nominal dimensionality is not itself evidence. The next genuine representation escape must show that the actual Wang/source family occupies one of these residual directions in a source-specific way that survives independently fixed anisotropic controls, and then prove that the destination still resolves and rewards that direction.