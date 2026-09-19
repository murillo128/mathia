# MI-047 — Inner parity can make semisimple spectralization control-blind

**Evidence level:** exact synthesis from [PC-351](../../findings/PC-351-faithful-upper-triangular-signature-decoding-is-spectrally-trivial-and-control-conjugate.md) and [PC-352](../../findings/PC-352-inner-parity-makes-nonsolvable-sl2-developments-control-conjugate.md).

PC-351 shows that faithful noncommutative source recovery can become useless after passing to a basis-free spectral quotient: the canonical triangular decoder stores the centered radial source in an oriented off-diagonal coordinate, while the reciprocal control `W -> -W` is related to it by a fixed unitary conjugation.

A natural repair is to leave the solvable/triangular sector and use a genuinely semisimple development. PC-352 shows why that criterion is too weak. Write a centered radial connection as

`Omega=A dX_2+sum_j B_j dW_j`,

where `A` is the calibration/residue direction and the matched reciprocal control flips every centered coordinate:

`tilde(Omega)=A dX_2-sum_j B_j dW_j`.

If there is one fixed target element `J` with

`Ad_J(A)=A`, `Ad_J(B_j)=-B_j`,

then the parity involution is inner and

`tilde(Omega)=Ad_J(Omega)`.

Uniqueness of the development ODE transports this identity to every finite cutoff. Since the reciprocity closing factor depends only on `A` and is also fixed by `J`, the regularized defects satisfy

`tilde(D_R)=J D_R J^(-1)`

before any limiting argument. Every conjugacy-invariant spectral readout is therefore exactly identical for arithmetic and matched control.

The obstruction survives a target whose generated Lie algebra is all of `sl_2(C)`. Taking `A=alpha H_0` and `B=beta E+gamma F` with all coefficients nonzero generates `H_0,E,F`, while `J=diag(i,-i)` fixes the Cartan direction and negates both root spaces. Passing to any finite-dimensional `SL_2` representation merely transports the same group-level conjugacy. More representation dimension does not recover a discriminator already killed by an inner symmetry.

The reusable lesson is that **non-solvability and spectral richness are not control selectivity**. Before crediting a representation-based spectral mechanism, identify the source/control involution on the target and ask whether it is inner on the proposed observable quotient. If it is, all class-function spectral data are blind by construction, however complicated the generated Lie algebra is.

This tightens the quotient audit from PC-351. A surviving route must either use a target in which the reciprocal involution is genuinely outer/non-equivalent on the relevant quotient, or retain a source-forced observable that does not descend to the conjugacy class. The latter must still avoid becoming a gauge-oriented copy of the source and must feed an independently zero-sensitive destination theorem.

**Boundary.** PC-352 does not prove that every semisimple or `SL_2` development is control-conjugate. Targets whose arithmetic/control involution is not implemented by one fixed inner automorphism remain outside the no-go. The result also does not show that an outer-parity construction is useful; it only identifies a necessary control-separation condition that must be passed before spectral invariants can carry prime-specific content.
