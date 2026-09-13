# MI-015 — Completed packet locality should be priced in the Hilbert--Schmidt currency before operator norm

**Evidence level:** exact finite-section algebra from [PF-329](../../findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md)--[PF-332](../../findings/PF-332-completed-square-root-defect-is-a-resolvent-dressed-pant-insertion.md), the generic operator-norm obstruction [PF-333](../../findings/PF-333-relative-square-root-sensitivity-remains-logarithmic-even-for-positive-insertions.md), and the dimension-free Hilbert--Schmidt refinement [PF-334](../../findings/PF-334-hilbert-schmidt-relative-square-root-control-escapes-logarithmic-dimension-loss.md). No Prime-Flute locality estimate or endpoint weak-trace-class theorem is claimed.

Let `A_0=Q+Lambda_LL`, `K=Q^(-1/2)Lambda_LLQ^(-1/2)>=0`, and `F=A_0^(1/2)Q^(-1/2)`. PF-329--PF-331 show that completed normalization preserves the critical packet family and that polar extraction cannot amplify a defect already controlled at the appropriate stage. PF-332 gives the exact relative representation

`F-I=(1/pi) int mu^(1/2)(A_0+mu)^(-1) Lambda_LL (Q+mu)^(-1)Q^(-1/2) dmu`,

so the baseline seam square-root defect cancels and every nonidentity term contains the actual pant/core insertion.

PF-333 shows that forgetting this structure and asking for a generic **operator-norm** relative square-root theorem is too expensive: the worst first-order constant grows like `log r` even for positive normalized perturbations in dimension `r`.

PF-334 identifies the norm mismatch. The first relative derivative is an entrywise Schur multiplier and satisfies, for Hermitian `E`,

`||R_Q(E)||_(S2) <= 2^(-1/2) ||E||_(S2)`

with no dependence on dimension or the condition number of `Q`. For the full positive insertion,

`||F-I||_(S2) <= C_2(||K||) ||K||_(S2)`.

Thus, under a uniform operator-norm envelope for `K`, the nonlinear relative square-root step itself does **not** add a logarithmic-rank loss in the Hilbert--Schmidt currency already sufficient in PF-318.

The live endpoint is consequently sharper than “prove relative locality.” First establish the localized reciprocal-prime `S_2` mass of the actual pant/core insertion or the exact PF-318 low/high block, and preserve enough spatial structure to pass through the PF-332 resolvent dressing. The remaining logarithmic-rank cost, if any, must come from the insertion, localization or block geometry, not merely from taking the relative square root.

Operator norm and Hilbert--Schmidt norm should therefore not be interchanged in the obstruction analysis. PF-333 remains a valid warning against an `S_infinity` shortcut; PF-334 shows that warning does not transfer automatically to the averaged `S_2` endpoint the proof actually needs.

**Boundary.** PF-334 does not identify the PF-318 cross block with the whole `K`, does not prove off-diagonal decay, and needs a uniform `||K||` bound for its nonlinear constant. A global Hilbert--Schmidt estimate is not locality and may hide exceptional packet directions; the PF-328 positive-measure obstruction remains live.