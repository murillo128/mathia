# MI-022 — Pole-normalized curvature is the affine invariant of the Mangoldt carrier

**Evidence level:** exact transformation law and source-specific sign from [WP-305](../../findings/WP-305-reflected-mangoldt-hilbert-transform-has-wrong-gamma-curvature.md)--[WP-307](../../findings/WP-307-pole-normalized-mangoldt-curvature-stays-positive-under-every-affine-spectral-recentering.md). This is a local asymptotic obstruction, not a Weil-positivity theorem.

Write the canonical positive Mangoldt Laplace transform near the pole as

`F(s)=1/s+C_+ + A_0 s+O(s^2)`.

The quadratic coefficient of the pole-normalized logarithm,

`J=[s^2] log(sF(s))=A_0-C_+^2/2`,

is the correct coordinate-free quantity for affine recentering. Translation multiplies `F` by `exp(-ts)` and therefore changes only the linear logarithmic coefficient; `J` is unchanged. A positive dilation `E->aE` with the scalar normalization forced by unit asymptotic density sends `J` to `a^2J`.

For the actual Mangoldt source, WP-307 proves the unconditional coarse bound `J>7/300`. Consequently every density-normalized orientation-preserving affine transform satisfies

`A_(a,t)=a^2 J + (t-aC_+)^2/2 > 0`.

The reflected Riemann-Gamma curvature is negative. No choice of real origin or positive scale can therefore fix the mismatch. The obstruction is not support positivity—the formula still holds when a translation moves finitely many atoms below zero—but the positive affine orbit of one source invariant.

This is a useful design test for future positive models: normalize the leading pole first, pass to the logarithm, and identify coefficients invariant under the coordinate freedoms being proposed. If the target differs already on such an invariant, retuning coordinates is not new structure.

**Boundary.** Non-affine transformations, new boundary measures, finite--archimedean couplings, quotients and determinant/scattering constructions can change `J`; WP-307 does not rule them out. It only closes the affine recentering family of the already-forced carrier.
