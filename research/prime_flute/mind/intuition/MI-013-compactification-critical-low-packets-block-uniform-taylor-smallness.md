# MI-013 — Seam-normalized critical packets retain both localization and compactified transverse energy

**Evidence level:** exact for the unprojected compactified cuff-cell form through [PF-322](../../findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md), the interior recentering through PF-323, the arithmetic terminal geometry through [PF-324](../../findings/PF-324-critical-packet-seam-distance-remembers-consecutive-prime-gap-ratio.md), the translation-frame/Hilbert–Schmidt identity through [PF-325](../../findings/PF-325-physical-translations-convert-the-local-hilbert-schmidt-gate-into-a-packet-position-integral.md), the seam-coordinate localization repair through [PF-326](../../findings/PF-326-seam-normalization-preserves-fixed-band-packet-localization.md), and the critical-energy preservation through [PF-327](../../findings/PF-327-seam-normalized-critical-packet-shapes-retain-compactified-transverse-energy.md). None is yet a lower bound for the completed shear-deleted intrinsic `L/H` angle.

PF-322--PF-324 show that the compactification-critical low packet cannot be dismissed by a uniform Taylor argument or as a seam artifact. For fixed `0<lambda<1`, the packet can be recentered at the interior point `s_n cosh tau_(n,lambda)=lambda`, where its scaled transverse energy stays nontrivial. The outgoing seam seen from this coordinate satisfies

`D_(n,lambda)=log((1+r_n)/lambda)+o(1)`,

with `r_n` asymptotic to a consecutive prime-gap ratio, so the same local witness occurs along both finite-boundary and escaping-boundary subsequences.

PF-325 supplies the exact accounting bridge to PF-318. In a fixed physical-low band of dimension `m~(kappa/pi)L`, the translated packets form a continuous tight frame. For every local low/high block `B`,

`||B||_(S_2)^2 = (m/L) integral_0^L ||B^* psi_t||^2 dt`.

Since `m/L` stays comparable to a constant, passing from Fourier rows to physical packet centers causes **no logarithmic dilution**. A fixed-width set of centers carrying order-one completed leakage would already violate the target budget.

PF-326 removes the seam-coordinate localization ambiguity. Pulling a unit equal-amplitude packet back through the exact seam-energy normalizer does not spread it over the growing cuff. On every fixed physical band, after removing the common parity scale and renormalizing in raw `L^2`, the Fourier weights converge uniformly to

`b_+(xi)=(1+xi^2)^(-1/2)` in the symmetric channel and `b_-(xi)=1` in the antisymmetric channel.

The seam normalizer commutes exactly with tangential translation, so the packet-position parameter survives. The resulting weighted packets converge to nonzero band-limited profiles of fixed physical width and retain a fixed positive fraction of their mass on a fixed window.

PF-327 closes the stronger possibility that this bounded frequency reweighting could preserve localization while destroying the **critical compactified energy**. At the PF-323 critical center, on every fixed interior window `|x|<=R<log(1/lambda)`, the coefficient satisfies

`s_n^2 cosh^2(tau_(n,lambda)+x) -> lambda^2 e^(2x)`

uniformly, while the exact seam-normalized packet converges locally in `L^2` to the nonzero profile `G_±`. Hence

`s_n^2 integral cosh^2(tau) |g_(n,lambda)^±(tau)|^2 d tau`

has a strictly positive limiting contribution on that fixed window. Positivity of the derivative part and the PF-233 comparison then give an order-one lower floor for the canonical variable-width diagonal transverse form. The coordinate-correct packet is therefore still compactification-critical at the unprojected transverse stage.

The remaining direct-angle theorem is now strictly downstream. Propagate these exact weighted packet families—with their common parity-dependent seam amplitudes retained—through the actual one-cusp-pant quotient, physical `L/H` projections and the common positive completion, then integrate the completed response using PF-325. The calculation must work in both PF-324 arithmetic terminal regimes.

This makes the critical packet a quantitative falsification family whose coordinate and pre-pant energy issues are already paid. If the completed response retains order-one leakage on a fixed-width set of centers, the Hilbert--Schmidt target fails at full physical density. If it is suppressed, the suppression must come from the pant/projection/completion/intrinsic-normalization geometry, not from seam normalization smoothing, delocalizing or energetically diluting the packet.

**Boundary.** PF-327 is still a shape-normalized, unprojected transverse-form statement. The common parity-dependent seam scales may affect the final intrinsic response magnitude; the pant crossing and `L/H` projection can still suppress correlation; bands reaching `|xi|~1/w_n` lie outside the fixed-band theorem. The conditional channel `T_H` and global ideal counts remain separate.
