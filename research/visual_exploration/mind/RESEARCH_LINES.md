# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Test intrinsic source-subspace localization beyond exact qutrit nulls

VIS-367--VIS-386 progressively remove source-free conditioning, similarity-orbit, generator-coordinate and tangent-amplitude artifacts. The intrinsic centered source subspace `S` carries a commutator Laplacian `Delta_S`; after removing the exact commutant component, the scale-free observable is the positive spectral probability measure seen by the normalized Gram tangent. Its first moment is the scalar defect rate, and super-mean cumulative mass has a universal Markov floor, so neither raw low-mode mass nor an order-one super-mean CDF window is source evidence by itself.

VIS-387 closes the normalized spectral-shape escape completely for qubits: on `Herm_0(2)`, the full positive spectral distribution is already determined by source rank and scalar defect rate. VIS-388 then identifies the minimal higher-dimensional capacity. For `d=3`, source rank one, the three positive root-sector eigenvalues are fixed by the cubic source invariant `t^2=tr(E^3)^2`; generic tangents with the same first moment can nevertheless have different spectral measures. This is algebraic capacity, not arithmetic specificity.

VIS-389 shows that the generic qutrit capacity is only one-dimensional after the obvious source and energy coordinates are fixed. If the positive support is `q_1<q_2<q_3` and `m_1` is the scalar defect rate, then the second moment `m_2` determines all three spectral weights by the Vandermonde/Lagrange formula. Equivalently, conditional on `(t^2,m_1)`, every normalized positive spectral profile is a function of one residual shape scalar. At the symmetry-enhanced qutrit boundaries the residual degree disappears entirely.

VIS-390 supplies an exact source-free null for that last scalar. Under Haar-isotropic tangent orientation in the six-dimensional positive spectral subspace, the three two-dimensional sector energies are `Dirichlet(1,1,1)`. Hence `(m_1,m_2)` is uniform on the moment triangle, and conditional on the observed `m_1`, the normalized residual coordinate

`u=(m_2-L(m_1))/(U(m_1)-L(m_1))`

is exactly `Uniform(0,1)` once `t^2` fixes the support. Thus an extreme qutrit residual is evidence only against isotropic tangent orientation at fixed source spectrum and defect energy; it is not yet arithmetic/source evidence.

The live minimal test is therefore sharply calibrated. For an admissible Wang qutrit Gram tangent, measure the position of `m_1` under its exact source-free first-moment null and the conditional residual `u`, then ask whether any deviation survives controls preserving source cubic geometry, admissibility, coarse Gram structure, block resources and other nonarithmetic causes of tangent anisotropy. Only a residual that survives those stronger controls and remains stable under the permitted scale/truncation budget should be propagated to the Wang destination. There is no reason at `d=3,r=1` to search an arbitrary family of CDF windows or higher moments independently: after `(t^2,m_1)`, they carry no more information than `u`.

## Quotient universal compact geometry before crediting a Wang gain

For any proposed positive-Hilbert improvement, first reduce the source to the exact normalized statistic, price Vandermonde/capacity collapse, expose the full relative metric, restrict the differential to the true simultaneous-similarity orbit, replace arbitrary generator coordinates by the intrinsic centered source subspace, remove tangent-amplitude normalization, freeze the ambient Hilbert metric and numerical-rank rule, and calibrate both source-subspace and tangent-orientation nulls before interpreting nonlinear low modes.

The dimension-sensitive gate is now explicit. `d=2` has no independent normalized spectral shape. Generic `d=3,r=1` has exactly one residual shape coordinate after source conjugacy and scalar defect are conditioned out, and that coordinate has an exact isotropic conditional null. Higher dimension/rank may have larger spectral support and additional shape degrees, but nominal dimensionality is not itself evidence. The next genuine representation escape must show that the actual Wang/source family occupies one of these residual directions in a source-specific way that matched controls cannot reproduce, and then prove that the destination still resolves and rewards that direction.