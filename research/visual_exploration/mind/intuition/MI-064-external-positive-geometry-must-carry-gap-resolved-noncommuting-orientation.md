# MI-064 — External positive geometry must carry gap-resolved noncommuting orientation

**Evidence level:** exact finite-dimensional matrix-analysis synthesis from [VIS-372](../../findings/VIS-372-commuting-external-hermitian-structure-remains-joint-spectral.md) and [VIS-373](../../findings/VIS-373-small-commutator-is-gap-weighted-near-preconditioning.md), extending the one-Gram preconditioning audit of MI-063.

Adding independently supplied Hermitian structure does not leave the spectral-filter class merely because more than one matrix is present. VIS-372 shows that if the external Hermitian operators commute with the baseline Gram and with each other, then every simultaneous-unitary-equivariant positive metric constructor is scalar on their joint eigenspaces. The resulting metric still commutes with the Gram and is only joint spectral reweighting.

Genuine noncommutation is therefore a necessary first gate, but VIS-373 shows that it is not quantitatively sufficient. If `G=sum lambda_alpha P_alpha` and `C>0`, let `C_0=sum P_alpha C P_alpha` be the Gram-block pinching. Then

`||[G,C]||_F^2 = sum_(alpha!=beta) |lambda_alpha-lambda_beta|^2 ||P_alpha C P_beta||_F^2`.

Across resolved Gram gaps `delta_G`, the distance to a valid commuting positive metric satisfies `||C-C_0||_F <= ||[G,C]||_F/delta_G`. If also `C>=mI`, the entire Wang singular spectrum is perturbatively close to the commuting/preconditioning spectrum when `||[G,C]||_F/(sqrt(m) delta_G)` is small.

The meaningful resource is thus not the Boolean statement `[G,C]!=0`, but **orientation carried across Gram sectors after charging the spectral gaps and the metric scale**. Large rotations hidden inside nearly degenerate Gram clusters are a separate regime; there the burden is to show that the near-degeneracy is not itself the source-free mechanism producing the apparent gain.

A surviving positive-Hilbert candidate must therefore import external structure whose off-diagonal Gram-block mass remains non-negligible after gap normalization, or exploit a collapsing cluster with an independently justified destination effect. Merely naming a second operator, obtaining formal noncommutation, or using a tiny commutator does not establish new arithmetic leverage.

**Boundary.** VIS-372--VIS-373 are finite-dimensional positive-Hilbert statements. They do not classify genuinely indefinite forms, nonlinear source coupling, noncompact/global geometry or controlled infinite-dimensional limits. The inverse-gap estimate weakens when Gram gaps collapse; that is an identified live regime rather than a contradiction. No Chebyshev-theta, zeta-zero or RH estimate follows from these structural tests alone.