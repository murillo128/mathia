# MI-052 — Rankin--Selberg positive geometry fails at the Weil half-density even after canonical finite--archimedean completion and homogeneous radial globalization

**Evidence level:** exact synthesis from [WP-363](../../findings/WP-363-eisenstein-rankin-selberg-gram-collapses-at-critical-exponent-and-first-jet-is-indefinite.md) through [WP-367](../../findings/WP-367-dilation-homogeneous-radial-positive-forms-still-separate-whittaker-incidence.md). The Rankin--Selberg factorization, Bessel Mellin product and dilation-homogeneity ingredients are classical; the Mathia content is the critical-survival/sign and globalization audit.

For real spectral parameters `r,u` and `s>1`, the finite Hecke coefficients form a genuine positive Gram. WP-363 shows that its exact Rankin--Selberg factorization is killed at `s=1/2` by the common `1/zeta(2s)` denominator, and the first nonzero critical jet is indefinite. WP-364 removes the common scalar intrinsically by projectivization; the normalized overlap still becomes unbounded near critical-line zeros and its Fubini--Study metric becomes negative with double-pole divergence.

WP-365 adds an independent positive archimedean Hilbert space. The Bessel kernel is positive and genuinely nonseparable in the spectral parameters, and tensoring it with the finite Hecke Gram generates the completed zeta factors automatically. Yet the critical projective overlap still blows up near unconditional critical-line zeros and the Fubini--Study geometry again loses positivity. Canonical finite-times-archimedean tensor completion therefore does not repair a global divisor that remains multiplicatively packaged.

WP-366 tests a stronger non-product feature before globalization. At fixed physical height `Y`, the coordinates `lambda_r(n)K_(ir)(2 pi nY)` couple finite and archimedean data through `nY`. If the height variable is globalized by a positive scalar dilation-covariant measure, covariance forces power-Haar averaging, and Mellin integration separates the incidence exactly back into Rankin--Selberg/Bessel tensor geometry. At the critical half-density the positive diagonal diverges.

WP-367 shows that replacing that scalar measure by a much richer positive radial geometry still does not help if the geometry is common to all Fourier indices and exactly dilation-homogeneous. For any positive-semidefinite radial form `b` satisfying

`b(D_a f,D_a g)=a^(-delta)b(f,g)`,

the finite-cutoff Whittaker form factors exactly as

`E_(delta,X)(r,u)=b(F_r,F_u) sum_(n<=X) conj(lambda_r(n))lambda_u(n)n^(-delta)`.

This is an algebraic finite-cutoff statement, so no interchange of infinite sums, regularization or continuation is responsible for the loss of incidence. At `delta=1/2`, if `b(F_r,F_r)>0` the nonnegative Rankin--Selberg diagonal diverges; if `b(F_r,F_r)=0`, positivity makes `F_r` a null vector and the entire row/column vanish. The critical positive state is therefore either infinite or trivial throughout this class.

The matched fixed-height point-evaluation form clarifies the culprit. Point evaluation is positive and keeps the nonseparable `nY` incidence, but it is not dilation-homogeneous. Thus positivity alone does not force separation. What kills the coupling is the combination of **one common componentwise radial geometry and exact scale homogeneity** used to remove the auxiliary height.

A viable automorphic route must therefore introduce coupling that remains noncentral after the scale variable is treated: cross-Fourier terms, a source-fixed/nonhomogeneous scale with an independent theorem, an operator-valued mixing not reducible to a common homogeneous radial form, a boundary/counterterm/cohomological sector whose sign is fixed before scalar separation, or another global degree of freedom that cannot be Mellin-diagonalized into the failed Rankin--Selberg product.

**Boundary.** WP-367 does not rule out fixed-scale source-defined observables, cross-index positive forms, nonhomogeneous radial geometry, independently forced counterterms, Maaß--Selberg remainder structures, cohomological/intersection forms or enlarged automorphic spaces. It rules out the broader class of common componentwise positive radial forms with exact dilation homogeneity. No RH implication follows.
