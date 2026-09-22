# MI-059 — Positive residue energies do not determine the signed source coherence

**Evidence level:** exact finite-dimensional source-fidelity synthesis from [PL-419](../../findings/PL-419-positive-residue-pair-correlation-blindness.md), sharpening the block-fidelity obstruction of MI-058.

The repaired mod-5 source target is the signed character-channel quadratic form with metric `D=diag(15,-1,-1,-1)`. It is tempting to replace the full channel Gram matrix by the positive residue-class pair-correlation energies `F_5(a)=w_a^*G w_a`, but PL-419 shows that this diagonal positive data does not determine `tr(DG)` even when `G>=0`.

The loss is exact. The residue projectors `P_a=w_aw_a^*` have constant diagonal, so the source metric `D` is outside their span. In the residue basis the target decomposes into a diagonal positive-energy contribution plus an explicit sum of off-diagonal residue coherences. The missing information is therefore not an unspecified “phase”: it is the cross-residue matrix data discarded when one keeps only the positive energies `F_5(a)`.

This gives a sharper representation-fidelity gate than raw spectral positivity. A transform may be invertible at the vector level and each retained statistic may be positive, yet a diagonalization or marginalization can still erase the signed quadratic functional required by the arithmetic source. Positive pair-correlation channels are useful only if an additional theorem reconstructs the lost coherences from them.

The surviving analytic route should therefore keep the full cross-residue/cross-character covariance matrix through source/model subtraction, or prove a genuinely arithmetic relation that determines the off-diagonal coherences from the positive diagonal energies. Replacing the required signed block statistic by a collection of positive marginal energies is not a harmless repackaging.

**Boundary.** PL-419 is an exact linear-algebraic non-identifiability statement for the mod-5 block geometry and its odd-prime analogue. It does not prove that the actual prime covariance realizes arbitrary positive Gram matrices, nor does it rule out arithmetic identities that constrain the missing coherences. It supplies no signed supertrace estimate or RH theorem by itself.