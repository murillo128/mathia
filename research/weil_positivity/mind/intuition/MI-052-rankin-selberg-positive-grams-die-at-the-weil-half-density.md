# MI-052 — Rankin--Selberg positive geometry fails at the Weil half-density even after canonical finite--archimedean completion and scale globalization

**Evidence level:** exact synthesis from [WP-363](../../findings/WP-363-eisenstein-rankin-selberg-gram-collapses-at-critical-exponent-and-first-jet-is-indefinite.md) through [WP-366](../../findings/WP-366-dilation-covariant-whittaker-boundary-averaging-collapses-to-rankin-selberg.md). The Rankin--Selberg factorization, Bessel Mellin product and Fubini--Study geometry are classical ingredients; the Mathia content is the critical-survival/sign and globalization audit.

For real spectral parameters `r,u` and `s>1`, the finite Hecke coefficients form a genuine positive Gram. WP-363 shows that its exact Rankin--Selberg factorization is killed at `s=1/2` by the common `1/zeta(2s)` denominator, and the first nonzero critical jet is indefinite. WP-364 removes the common scalar intrinsically by projectivization; the normalized overlap still becomes unbounded near critical-line zeros and its Fubini--Study metric becomes negative with double-pole divergence.

WP-365 adds an independent positive archimedean Hilbert space. The Bessel kernel

`H_s(r,u)=int_0^infinity K_(ir)(x)K_(iu)(x)x^(s-1)dx`

is positive for every `s>0` and genuinely nonseparable in `(r,u)`. Tensoring it with the finite Hecke Gram generates the completed zeta factors automatically. Yet the critical projective overlap still blows up near unconditional critical-line zeros and the Fubini--Study geometry again loses positivity. Canonical finite-times-archimedean tensor completion therefore does not repair a global divisor that remains multiplicatively packaged.

WP-366 tests a stronger-looking non-product feature before globalization. At a fixed physical height `Y`, the coordinates

`lambda_r(n) K_(ir)(2 pi nY)`

form a positive Gram in which finite and archimedean data are genuinely coupled through the product `nY`; this is not merely a tensor product with a separated scalar Gamma factor. But if the height variable is globalized by a positive scalar measure that is dilation-covariant, covariance forces that measure to be power-Haar, `c Y^q dY/Y`. Mellin integration then separates the `nY` incidence exactly back into the Rankin--Selberg/Bessel tensor geometry of WP-365. At the critical half-density the positive diagonal already diverges.

This adds a new failure mode. A representation may be genuinely non-product **locally in a scale parameter** yet become product-like again under the canonical symmetry used to eliminate that scale. The relevant question is therefore not only whether finite and archimedean variables interact before continuation, but whether the interaction survives the source-defined globalization/averaging operation.

A viable automorphic route must introduce a coupling that remains noncentral after the scale variable is treated canonically: a source-fixed scale with an independent theorem, an intrinsically non-Haar or operator-valued scale mixing forced by geometry, an interaction/remainder/cohomological sector whose sign is established before scalar separation, or another global degree of freedom that cannot be Mellin-diagonalized into the failed Rankin--Selberg product.

**Boundary.** WP-366 does not rule out fixed-scale source-defined observables, non-scalar scale measures, operator-valued averaging, Maaß--Selberg remainder structures, cohomological/intersection forms or enlarged automorphic spaces. It rules out the idea that retaining the literal `nY` coupling and then applying positive scalar dilation-covariant globalization preserves a new critical sign mechanism. No RH implication follows.