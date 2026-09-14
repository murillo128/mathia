# MI-022 — Mangoldt curvature survives both affine spectral recentering and scalar Herglotz projective gauge

**Evidence level:** exact transformation laws and source-specific sign from [WP-305](../../findings/WP-305-reflected-mangoldt-hilbert-transform-has-wrong-gamma-curvature.md)--[WP-308](../../findings/WP-308-scalar-herglotz-projective-recodings-cannot-repair-mangoldt-gamma-curvature.md). This is a local asymptotic obstruction for the canonical scalar source response, not a Weil-positivity theorem.

Write the canonical positive Mangoldt Laplace transform near the pole as

`F(s)=1/s+C_+ + A_0 s+O(s^2)`.

The quadratic coefficient of the pole-normalized logarithm,

`J=[s^2] log(sF(s))=A_0-C_+^2/2`,

is the correct invariant for affine **input** recentering. Translation changes only the linear logarithmic coefficient; positive dilation with the normalization forced by unit asymptotic density sends `J` to `a^2J`. WP-307 proves `J>7/300` for the actual source, hence every orientation-preserving affine spectral recentering retains positive reflected curvature while the Riemann-Gamma curvature is negative.

WP-308 shows that changing the scalar Herglotz/Weyl **output** coordinate does not restore freedom. The constant positivity-preserving projective changes are exactly real Möbius automorphisms

`T(w)=(aw+b)/(cw+d)`, `ad-bc>0`.

Because the reflected source response has `m_-(iy)=log y+O(1)+i(pi/2+o(1))`, every map with `c!=0` sends it to the finite boundary point `a/c+O(1/log y)` and loses the logarithmic end. Preserving the required archimedean growth forces `c=0`, hence `T(w)=alpha w+beta` with `alpha>0`. Matching the unit `log y` coefficient then forces `alpha=1`, leaving the positive `y^-2` coefficient unchanged.

The design lesson is therefore gauge-invariant on both sides of the scalar model. Retuning the spectral origin/scale or choosing another scalar self-adjoint boundary coordinate is not new structure. To change the curvature sign while retaining positivity and the Gamma-scale end, the construction must leave this scalar constant-projective class before the response is formed.

**Boundary.** WP-308 does not classify matrix-valued boundary spaces, `z`-dependent Schur/transfer transformations, quotient/compression mechanisms, new boundary measures, determinant/scattering constructions or genuinely coupled finite--archimedean models. Those can change the relevant invariant, but they require an independent source-native meaning and positivity theorem rather than a scalar coordinate recoding.
