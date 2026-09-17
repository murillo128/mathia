# MI-037 — The canonical Green Hilbert background survives smooth Li-profile subtraction

**Evidence level:** exact/literature-backed synthesis from [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md), [PC-328](../../findings/PC-328-canonical-green-band-normalization-has-pnt-driven-escaping-outliers.md), [PC-329](../../findings/PC-329-no-fixed-packet-deflation-bounds-canonical-green-family.md), and [PC-330](../../findings/PC-330-smooth-li-profile-subtraction-preserves-canonical-green-hilbert-band.md).

PC-327--PC-329 show that the growing-conductor Green operator contains a canonical Hilbert-type background that no fixed set of Fourier modes or fixed-rank conductor-dependent correction can remove. That left open a natural possibility: subtract the entire smooth PNT/Li source profile rather than approximate it by finite complexity.

PC-330 shows that this also misses the load-bearing channel. The prime source and its smooth Li control have the same leading density but very different `L^2` geometry. At conductor `q`, the sparse prime source has RMS scale `log q/q`, while the diffuse Li-grid profile has RMS only `1/q`. Consequently

`||prime - Li||_2 / ||prime||_2 -> 1`.

Removing the smooth profile can eliminate fixed low-frequency mean structure, but it cannot cancel the sparse high-frequency energy that feeds the Green Hilbert channel. The residual simply moves the energy into growing Fourier modes.

The operator statement matches the source-space calculation. After intrinsic Green-band normalization, subtracting the Li Green operator leaves the dominant Hilbert-channel singular scale asymptotically unchanged. The canonical background is therefore not merely a low-rank or smooth-density artifact; it is tied to the sparse source geometry itself.

This sharpens the renormalization principle. A control subtraction must match the **norm and channel in which the obstruction lives**, not only the first-order density profile. In this setting a diffuse PNT approximation is accurate for weak/low-frequency observables while being asymptotically orthogonal to the sparse `L^2` resource that drives the spectral divergence.

The next meaningful Green construction must subtract or quotient the source-native Hilbert channel itself, or form a relative observable in which that channel cancels structurally. Only the residual after such a channel-matched operation is eligible for arithmetic selectivity tests against phase/autocorrelation and sparse non-arithmetic controls.

**Boundary.** PC-330 does not prove that no growing-complexity renormalization exists, determine a canonical Hilbert-channel subtraction, or connect any residual to RH. The durable conclusion is narrower: fixed-complexity subtraction and full smooth Li-profile subtraction both fail because neither matches the sparse Hilbert channel that carries the normalized background.