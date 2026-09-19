# MI-048 — Outer parity and finite representation lifts expose only generic contragredient orientation

**Evidence level:** exact synthesis from [PC-353](../../findings/PC-353-outer-parity-sl3-produces-contragredient-control-spectrum.md) and [PC-354](../../findings/PC-354-representation-lift-spectra-are-reciprocal-functions-of-the-original-spectrum.md), sharpening the inner-parity obstruction of [PC-352](../../findings/PC-352-inner-parity-makes-nonsolvable-sl2-developments-control-conjugate.md).

PC-352 shows that a full semisimple target is still control-blind when the reciprocal source involution is implemented by one fixed **inner** automorphism. PC-353 tests the direct escape: choose a type-`A` target where the same parity is genuinely outer.

In `SL_d(C)`, `d>=3`, take `Theta(g)=g^(-T)`, with differential `theta(X)=-X^T`. Place the calibration direction in the skew-symmetric subspace and every centered shell direction in the symmetric traceless subspace. Naturality of the development gives, at every finite cutoff,

`tilde(D_R)=D_R^(-T)`.

Thus outer parity escapes the inner-conjugacy no-go, but only by producing reciprocal/contragredient spectrum. In `SL_3`, the two nontrivial characteristic-polynomial coefficients `tr D` and `tr D^-1` are exchanged, so a duality-odd coordinate can distinguish a path from its reciprocal twin. The escape is genuine at the Lie-algebra level, yet the same relation holds for every admissible non-arithmetic matched profile because it depends only on the parity law and target automorphism.

PC-354 closes the most obvious attempt to amplify that orientation. Let `rho` be any finite-dimensional algebraic representation of `SL_d`. If the eigenvalues of `D` are `lambda_i`, every eigenvalue of `rho(D)` is a fixed weight monomial `lambda^mu`; the unipotent part can change Jordan blocks but not spectral values. Moreover `D^-T` is conjugate to `D^-1`, so

`rho(tilde(D)) ~ rho(D)^(-1)`.

Hence every representation-lift spectrum is a deterministic algebraic function of the original spectrum and transforms by the same contragredient reciprocity. Fundamental exterior powers simply exchange `e_k` with `e_(d-k)`, reproducing the characteristic-coefficient reversal already visible in the standard representation. Higher symmetric/tensor/highest-weight representations do not open another channel.

The reusable lesson is a **three-stage quotient audit**. First ask whether the source/control involution is inner on the destination quotient; if yes, spectral class functions are blind. If it is outer, identify the exact duality action and test whether the surviving orientation is source-specific or shared by matched controls. Finally, if a richer finite representation is applied, ask whether its spectrum contains information beyond fixed weight functions of the already-formed conjugacy class. For algebraic representations of `SL_d`, it does not.

This means that source information lost at the ordinary finite-dimensional spectral quotient cannot be recovered by a representation wrapper applied afterward. A viable escape must inject source-forced structure **before** that quotient, keep a non-spectral covariant/canonical frame, or move to an infinite-dimensional operator whose domain and zero-sensitive destination theorem are independently justified from the roots geometry.

**Boundary.** PC-354 does not rule out source-dependent state spaces, representation laws that change intrinsically with refinement, non-spectral tensor/covariant data retained before quotienting, or source-forced infinite-dimensional operators. It rules out treating fixed finite-dimensional algebraic representation spectra, characters, traces of powers or their finite combinations as a new arithmetic selector after PC-353 has already reduced the control relation to contragredient reciprocity.