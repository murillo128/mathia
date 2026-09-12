# MI-018 — Nonnegative transference does not create fixed-power sign balance

**Evidence level:** supported by the first-shell scale reduction MC-232--MC-235 and the exact/published-resolution audit in MC-236; this is a limitation of the audited dense-model/transference pipeline, not an impossibility theorem for the underlying method.

The hard first-shell coordinates require a **signed** progression estimate. For a fixed interior pair

\[
q=X^{2\alpha+o(1)},\qquad Z=X^{1-\beta+o(1)},\qquad d=\frac12-2\alpha-\beta>0,
\]

the required relative sign bias is `X^{-d+o(1)}`, equivalently a fixed negative power of `q`.

MC-235 shows that this is not a support problem: the 2026 Linnik machinery already supplies essentially full-exponent populations of both Möbius signs in the selected progression. MC-236 then isolates the missing information in the proof architecture. The sign-specific dense models satisfy exact principal-mode preservation,

\[
\mathbb E(g^+-g^-)=\mathbb E(f^+-f^-).
\]

So dense modeling transports whatever total sign bias was already present; it does not regularize that bias toward zero. The later threshold sets and product-set argument deliberately convert the models into one-sided coverage information.

The obvious repair—transfer the positive and negative convolutions separately and subtract—also misses the required scale. In the published Möbius specialization the explicit transference tolerance is only `q^{-o(1)}` relative to the one-sided main threshold, while the first-shell amplitude asks for `q^{-c}` with fixed `c>0`. Two accurate enough statements for positivity/support can therefore be far too coarse after subtraction.

The reusable lesson is: **signed cancellation must be coupled before an information-losing nonnegative quotient if the downstream target is a small difference of two large masses**. Separate abundance, exact preservation of each mean, and one-sided convolution coverage are compatible with a large signed discrepancy.

A viable continuation must expose a signed comparative quantity before thresholding or triangle inequality—such as a controlled difference of Fourier coefficients or a signed convolution with fixed-power resolution—or obtain cancellation only after recombining the smooth-dilation family so that separate component errors are never paid.

**Boundary.** MC-236 does not prove that Matomäki--Teräväinen dense modeling cannot participate in a stronger signed argument, nor that the true transference error is as large as the published bound. It rules out treating the current separate-sign, nonnegative, one-sided estimates as if they already implied the fixed-power near-balance required by the first-shell route.