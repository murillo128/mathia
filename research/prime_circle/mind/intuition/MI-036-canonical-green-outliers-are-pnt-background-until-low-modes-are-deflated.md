# MI-036 — Canonical Green outliers are PNT background until low modes are deflated

**Evidence level:** exact/literature-backed synthesis from [PC-325](../../findings/PC-325-green-relative-spectrum-is-phase-gauge-and-autocorrelation-only.md), [PC-327](../../findings/PC-327-band-normalized-green-defect-has-universal-schatten-divergence.md), and [PC-328](../../findings/PC-328-canonical-green-band-normalization-has-pnt-driven-escaping-outliers.md).

PC-327 shows that growing-conductor Hilbert-band normalization already carries a universal shifted-Hilbert singularity: every nonzero centered periodic source pair loses uniform Schatten control. PC-328 identifies a second and much larger effect for the canonical prime-support source. Fixed Fourier modes decay only as `1/log q` by the ordinary prime number theorem, while the intrinsic Hilbert-band scale decays as `sqrt(log q/q)`.

That mismatch is enough to force actual discrete spectrum to escape. A single `(1,1)` Green coefficient gives, for two growing prime conductors,

`||G_(q,r)||/c_(q,r) >= const * sqrt(qr)/(log q log r)^(3/2)`,

so the normalized self-adjoint Green operator has an off-band eigenvalue pair whose magnitude diverges; for comparable conductors the lower scale is `Q/(log Q)^3`. The trace-class defect itself consequently diverges in normalized operator norm, far more strongly than the universal logarithmic Schatten floor.

The key interpretation is negative. The fixed-mode amplitude is produced by the smooth PNT/Li source profile before any explicit-formula zero information enters. Moreover PC-325 supplies non-arithmetic phase controls that are exactly isospectral for the complete separable Green operator. **Large canonical Green outliers are therefore background source geometry, not evidence of a zero-sensitive arithmetic spectrum.**

A growing-conductor Green program must now renormalize two distinct effects rather than celebrate either divergence: the universal generalized-Hilbert offset singularity and the canonical low-frequency PNT/Li packet. Only the residual after those backgrounds are removed can be tested for tightness, source selectivity and a possible zero-sensitive destination theorem.

This suggests a precise next architecture rather than another raw normalization. Freeze the finite low-mode packet predicted by the PNT/Li expansion, subtract or deflate it together with the universal Hilbert background, and compare the residual against both smooth Li-type controls and the exact phase-gauge controls of PC-325. A surviving residual matters only if it cannot be reproduced by those controls and if an independent theorem connects its sign, divisor or spectrum to the Riemann zero restriction.

**Boundary.** PC-328 does not prove that finitely many low modes suffice to make the residual tight, identify the asymptotic top eigenvalue, or exclude a zero-sensitive residual after source-derived deflation. It proves that the raw band-normalized canonical spectrum is dominated by a classical PNT-scale outlier mechanism and therefore cannot itself be interpreted as RH-sensitive.