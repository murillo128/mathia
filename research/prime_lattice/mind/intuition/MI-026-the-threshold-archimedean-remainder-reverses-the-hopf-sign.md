# MI-026 — Completed-Weil order positivity fails before the first-prime wall even on the even sector

**Evidence level:** literature-backed exact synthesis from [PL-329](../../findings/PL-329-source-amplitude-controls-first-prime-reflection.md), [PL-332](../../findings/PL-332-uniform-endpoint-remainder-transports-the-first-prime-coefficient.md), [PL-333](../../findings/PL-333-first-prime-archimedean-antimarkov-hopf-obstruction.md), and [PL-334](../../findings/PL-334-even-sector-beurling-deny-plastic-threshold.md).

PL-329--PL-332 reduce the first-prime orientation problem to a uniform source-amplitude estimate and one fixed-threshold nonvanishing coefficient `C_0` at `a_0=(1/2)log2`. A natural attempt is to obtain that nonvanishing from positivity of the threshold state plus the Hopf boundary law for the Dirichlet logarithmic Laplacian.

PL-333 shows that the completed threshold operator has the wrong structure for that import. At `a_0`, the `p=2` translation has zero overlap, but Suzuki's archimedean remainder contributes a strictly positive off-diagonal kernel. It violates the first Beurling--Deny contraction inequality, so positivity improving for the principal logarithmic-Laplacian form is not inherited by the full completed-Weil form. Even if a nonnegative threshold eigenstate were granted, the full equation makes it a strict logarithmic-Laplacian **subsolution** near the boundary, whereas the standard Hopf theorem needs a nonnegative supersolution.

PL-334 closes the parity loophole. Restrict the localized Weil form to real even functions. Folding the continuous modulus defect pairs the archimedean coefficient as

`F(|x-y|)+F(x+y)`,

where `F` changes sign at `t_*=log rho_pl` and `rho_pl` is the plastic constant. Local concavity proves the even-sector modulus criterion exactly for `0<a<=log rho_pl`, while an even two-bump test defeats it for every larger aperture. Since

`log rho_pl < (1/2)log 2`,

the even semigroup has already ceased to be positivity preserving **before the first rational-prime translation enters**. Odd parity survives farther, exactly to the first-prime wall, but the relevant evenness of a candidate ground state does not restore the standard Perron--Frobenius/Hopf route.

The hierarchy is therefore structural rather than cosmetic:

`a_full=(1/2)log rho_pl < a_even=log rho_pl < a_odd=(1/2)log2`.

The completed archimedean term pairs differently under the two parities: addition in the even sector postpones but does not remove the continuous obstruction, while subtraction in the odd sector leaves the continuous defect favorable until the arithmetic translation itself appears. A parity restriction can move the order-positivity threshold without making it coincide with the source-selected first-prime threshold.

The reusable lesson is stronger than “the full form is not Markov.” A principal/limiting Dirichlet structure cannot supply state sign or boundary orientation for a completed operator merely because the target state lies in a symmetry sector. Before importing Perron--Frobenius or Hopf theory, the **restricted full operator** must itself retain the required order property at the aperture of interest.

**Boundary.** Failure of the even-sector modulus criterion does not prove that the actual even threshold eigenfunction changes sign and does not prove `C_0=0`. PL-333--PL-334 close generic order-semigroup proof routes, not the desired nonvanishing statement. The remaining gates are still the family-uniform source/remainder estimate and `C_0!=0`, but any proof of fixed sign or boundary nonvanishing must use state-specific information from the full completed-Weil operator or a genuinely non-Markov comparison principle.