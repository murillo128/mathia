# MI-053 — Fixed bounded positive Whittaker scale preserves incidence only by exponentially suppressing arithmetic index

**Evidence level:** exact synthesis from [WP-368](../../findings/WP-368-bounded-source-fixed-whittaker-scale-forms-have-exponential-arithmetic-index-tails.md), interpreted together with the homogeneous-globalization obstructions WP-366--WP-367.

WP-366--WP-367 show one way positivity loses the finite--archimedean carrier: if a common radial geometry is globalized with exact dilation homogeneity, the `nY` coupling Mellin-separates at finite cutoff into a radial scalar times Rankin--Selberg data. At critical half-density the positive state is null or divergent.

WP-368 tests the opposite architecture. Keep the Whittaker scale source-fixed on `Y>=Y_*>0`, so the finite index `n` remains literally coupled to the archimedean coordinate through `nY`, and allow an arbitrary bounded positive operator on that radial Hilbert space. The Whittaker asymptotics then force

`q_A(F_(r,n)) <= C_(r,A,Y_*) n^(-1) exp(-4 pi (n-1)Y_*)`.

The induced norm therefore decays exponentially in the arithmetic index. Multiplying by polynomial- or logarithmic-size Hecke/Mangoldt factors cannot recover the critical Weil half-density, and cross-spectral pairings inherit the same exponential tail suppression.

This creates a two-sided positive trap. **Globalize a common scale exactly and incidence disappears; keep a bounded positive scale away from the cusp and incidence survives but its high-index mass disappears.** Positivity itself is not the full obstruction: the failure depends on how scale, boundedness and Fourier index are coupled.

The structural escape routes are correspondingly narrower. A viable positive construction must let the relevant scale move toward `Y=0` with the arithmetic index, employ an unbounded but canonically controlled form, introduce cross-Fourier coupling that is not componentwise radial, or obtain orientation from a cohomological/intersection/remainder mechanism outside the bounded fixed-scale class.

**Boundary.** WP-368 assumes a fixed lower scale `Y_*>0` and bounded positive operator. It does not rule out scale-mixing that reaches the cusp, unbounded canonical positive forms, cross-index kernels or indefinite geometries with an independent sign theorem. It supplies no RH implication; it excludes a broad source-localized positive mechanism for carrying the required arithmetic-index tail.