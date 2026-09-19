# MI-048 — Outer parity exposes only contragredient orientation without a source-specific destination

**Evidence level:** exact synthesis from [PC-353](../../findings/PC-353-outer-parity-sl3-produces-contragredient-control-spectrum.md), sharpening the inner-parity obstruction of [PC-352](../../findings/PC-352-inner-parity-makes-nonsolvable-sl2-developments-control-conjugate.md).

PC-352 shows that a full semisimple target is still control-blind when the reciprocal source involution is implemented by one fixed **inner** automorphism. PC-353 tests the direct escape: choose a type-`A` target where the same parity is genuinely outer.

In `SL_d(C)`, `d>=3`, take

`Theta(g)=g^(-T)`, with differential `theta(X)=-X^T`.

Place the calibration direction `A` in the skew-symmetric subspace and every centered shell direction `B_j` in the symmetric traceless subspace. Then `theta(A)=A` and `theta(B_j)=-B_j`, exactly matching the reciprocal control. Naturality of the development gives, at every finite cutoff,

`tilde(D_R)=D_R^(-T)`.

Thus outer parity does escape the inner-conjugacy no-go, but it does not create arbitrary new spectral content. The matched control spectrum is the reciprocal spectrum. In `SL_3`, the two nontrivial characteristic-polynomial coefficients are `tr D` and `tr D^-1`, and the control swaps them. The simplest odd coordinate is

`Delta(D)=tr D-tr D^-1`,

which changes sign under reciprocity.

The escape is genuine rather than triangular: PC-353 gives explicit skew/symmetric generators that produce all of `sl_3`, so no fixed inner conjugator can implement the parity on the generated algebra. A numerical cyclotomic example also shows that `Delta` need not vanish for the actual source.

But the same theorem applies to every admissible non-arithmetic reciprocal profile. The contragredient relation is forced entirely by the target automorphism and the generic sign flip. Therefore **outer parity creates control-sensitive orientation, not arithmetic selectivity**. Reciprocal-symmetric class functions remain blind; reciprocal-odd functions can distinguish a path from its twin but still require an independent reason that the odd coordinate is tied to primes or zeta zeros.

The reusable lesson is a two-stage automorphism audit. First ask whether the source/control involution is inner on the destination quotient; if yes, spectral class functions are blind. If it is outer, identify the exact quotient action it induces and ask whether the surviving orientation is generic for matched controls. Escaping inner conjugacy is necessary for some spectral discriminators, but it is not sufficient for a source-specific one.

**Boundary.** PC-353 does not rule out outer-parity constructions with additional source-forced tensors, pairings, functional equations or destination theorems that distinguish the arithmetic source from generic reciprocal controls. It rules out treating contragredient spectral asymmetry itself as the missing RH mechanism.
