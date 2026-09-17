# MI-037 — Fixed-complexity deflation cannot remove the canonical Green background

**Evidence level:** exact/literature-backed synthesis from [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md), [PC-328](../../findings/PC-328-canonical-green-band-normalization-has-pnt-driven-escaping-outliers.md), and [PC-329](../../findings/PC-329-no-fixed-packet-deflation-bounds-canonical-green-family.md).

PC-327 shows that growing-conductor Hilbert-band normalization already carries a universal shifted-Hilbert singularity. PC-328 identifies a much larger canonical effect: every fixed low Fourier mode of the prime-support source is of PNT/Li size `1/log q`, while the intrinsic band scale is only `sqrt(log q/q)`. The resulting normalized Green operator therefore has discrete outliers at least of scale

`sqrt(qr)/(log q log r)^(3/2)`,

or `Q/(log Q)^3` for comparable conductors. PC-325 simultaneously shows that the full separable Green spectrum is blind to independent source phases, so the raw divergence is not a zero selector.

A natural response was to freeze a finite low-mode PNT/Li packet and deflate it. PC-329 proves that this cannot work at any fixed complexity. If one removes any fixed collection of periodic Fourier residues, another fixed mode has the same `1/log q` source scale and reproduces the normalized escape.

The obstruction is stronger than failure of a particular Fourier subtraction. For every fixed rank `R`, even a conductor-dependent rank-`R` correction leaves a normalized `(R+1)x(R+1)` Cauchy/Hilbert block of full rank. Its smallest relevant singular scale remains bounded below by an `R`-dependent constant, so the residual Green family still has outliers of order

`kappa_R sqrt(qr)/(log q log r)^(3/2)`.

Thus **the smooth canonical background has growing effective rank**. The correct renormalization problem is not to choose a better finite packet; any potentially tight residual must allow subtraction complexity to grow with conductor or remove a whole source-derived smooth PNT/Li profile before spectral selectivity is assessed.

This makes the next test more precise. First define a source-canonical growing-rank or profile subtraction and prove a uniform residual bound in the intrinsic band normalization. Then compare that residual against both smooth non-arithmetic controls and the exact phase-gauge controls of PC-325. Only a survivor that those controls cannot reproduce is eligible for a separate theorem connecting its sign, divisor or spectrum to the Riemann zero restriction.

**Boundary.** PC-329 does not determine the minimal growth rate of the required subtraction rank, prove that a full Li/PNT profile subtraction is sufficient, or rule out a zero-sensitive residual after such a renormalization. It closes only the fixed-complexity repair. Failure of finite deflation is therefore a background-complexity theorem, not evidence that the escaping spectrum is RH-sensitive.