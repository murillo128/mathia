# MI-015 — Completed normalization preserves packet mass; the live gate is DtN square-root locality

**Evidence level:** exact finite-section algebra from [PF-329](../../findings/PF-329-final-diagonal-normalization-turns-seam-pulled-packets-into-total-energy-unit-traces.md), [PF-330](../../findings/PF-330-completed-low-normalization-rotates-packet-frame-instead-of-damping-total-energy-mass.md) and [PF-331](../../findings/PF-331-completed-low-polar-factor-has-uniform-gap-and-cannot-amplify-locality-defects.md). No endpoint Hilbert--Schmidt estimate or uniform locality theorem is claimed.

Let `A_0=Q_L+Lambda_LL` be the raw completed low energy, `A=Q_L^(-1/2)A_0Q_L^(-1/2)`, and let `psi_t` be the PF-325 unit translation frame in the final normalized low angle coordinate. PF-329 identifies the raw trace entering canonical correlation as

`g_t=Q_L^(-1/2) A^(-1/2) psi_t`.

PF-330 factors the same map through the unitary

`U_L=A_0^(1/2) Q_L^(-1/2) A^(-1/2)`

and writes `g_t=A_0^(-1/2) U_L psi_t`. The family `U_L psi_t` remains a tight frame, every `g_t` has exactly unit `A_0`-energy, and the completed direct-angle Hilbert--Schmidt mass is exactly the raw total-energy packet average. Completed diagonal normalization therefore cannot solve the endpoint by damping total packet mass; it only rotates how that mass is located relative to the physical critical window.

PF-331 removes a second apparent instability. Put

`F=A_0^(1/2) Q_L^(-1/2)`.

Then `F^*F=A=I+K_LL>=I`, so the polar factor `U_L` has a uniform singular-value gap before extraction. For every bounded spatial localizer or translation,

`||[U_L,X]|| <= ||[F,X]||`.

Since the seam normalizer commutes with the physical translations, the remaining translation defect is controlled by the concrete completed-energy square-root map `A_0^(1/2)Q_L^(-1/2)`. Polar extraction cannot amplify that defect.

The endpoint has therefore become a **completed DtN square-root locality problem**. To transfer the PF-328 positive-measure packet obstruction, prove cutoff/translation commutators or quasilocal off-diagonal bounds for `F` strong enough on the critical center family. A failure of such locality would explain how total packet mass survives while its physical-window meaning is redistributed; a success transfers locality automatically to the polar unitary.

**Boundary.** The statements are finite-section and do not prove a uniform limit across the arithmetic terminal regimes. Tight-frame mass conservation is not spatial localization, and the gapped polar estimate does not itself bound `[F,X]`.