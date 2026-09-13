# MI-015 — Intrinsic-angle packets must be normalized by completed diagonal energy

**Evidence level:** exact finite-section block algebra from [PF-329](../../findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md). No Hilbert--Schmidt endpoint estimate or packet-survival theorem is claimed.

Let the raw completed boundary form be `M_raw=Q+Lambda`, where the positive seam form `Q` respects the physical `L/H` split. After seam normalization, `M=Q^(-1/2) M_raw Q^(-1/2)` has diagonal blocks `A,C` and cross block `B`. PF-329 proves that the intrinsic angles formed before and after this block-diagonal congruence are unitarily equivalent.

The consequence is stronger than cancellation of a common scalar. Seam normalization is a coordinate change at the intrinsic-angle level: singular values and symmetric-ideal norms are unchanged after the corresponding unitary identification. The physical seam energy still matters inside the raw diagonal forms, but its inverse-square-root amplitude cannot by itself create a completed-angle gain.

For a unit packet `psi` in the normalized low angle coordinate, the raw low boundary trace actually entering canonical correlation is

`g = Q_L^(-1/2) A^(-1/2) psi`,

not the seam-only pullback `Q_L^(-1/2) psi`. The corrected trace satisfies the exact identity

`<g,A_0 g>=1`,

so it is normalized by the **completed total low energy**. Its angle response is equivalently the raw cross-correlation divided by the raw completed high energy. This is the representation in which the PF-318 endpoint must be tested.

This changes how packet witnesses should be interpreted. A large seam-only transverse energy may be accompanied by an equally large contribution to the low diagonal block, and the operator `A^(-1/2)` can reshape the packet rather than merely rescale it. Since `A^(-1/2)` need not commute with translations, a translated normalized packet family need not remain a translated family after pullback to raw pant coordinates.

The live positive route is therefore to prove that completed diagonal preconditioning preserves enough localization or critical cross-correlation for a positive-measure packet family. The live negative route is to show that this preconditioner suppresses or redistributes almost all critical packets strongly enough to satisfy the Hilbert--Schmidt budget. Estimating seam-only amplitudes cannot decide between these routes.

**Boundary.** The unitary-equivalence statement is finite-section linear algebra and does not make the seam geometry physically irrelevant. It supplies the correct normalization and packet variable; it neither proves nor refutes the completed direct-angle estimate.