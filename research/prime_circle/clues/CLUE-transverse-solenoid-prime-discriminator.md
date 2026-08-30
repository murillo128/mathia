---
id: CLUE-prime-circle-transverse-solenoid-prime-discriminator
type: research-clue
status: proposed
origin: master
target_line: prime_circle
based_on:
  - research/prime_circle/findings/PC-058-exact-radial-birth-gram-has-fixed-divisor-haar-basis.md
  - research/prime_circle/findings/PC-059-infinite-divisor-haar-limit-is-profinite-valuation-measure.md
  - research/prime_circle/findings/PC-060-exact-radial-symbol-vanishes-ae-and-mass-is-log-series-atoms.md
  - research/prime_circle/findings/PC-061-normalized-radial-spectral-mass-returns-profinite-haar.md
  - research/prime_circle/findings/PC-064-compatible-refinement-is-the-adelic-solenoid.md
  - research/prime_circle/findings/PC-065-solenoid-leafwise-laplacian-has-dense-rational-square-spectrum.md
---

# Can transverse solenoid structure retain a prime discriminator?

## Observation

The canonical Prime-Circle completion has now been pushed through several increasingly global compressions. PC-058--PC-061 show that the exact radial birth Gram diagonalizes in a divisor-Haar basis and that its normalized infinite radial mass returns profinite Haar behavior rather than a zero-selective spectral law. PC-064 identifies the compatible refinement limit with the arithmetic solenoid, while PC-065 shows that its bare leafwise Laplacian has the classical dense rational-square spectrum, noncompact resolvent, infinite heat trace, and no intrinsic RH-sensitive selector.

These findings close the route in which the radial/refinement data are first collapsed to the canonical leaf metric and only afterward interpreted spectrally. PC-065 explicitly leaves a narrower escape: transverse finite-adic structure or a genuinely nonlocal archimedean--finite-adic coupling introduced before diagonalization.

## Research question

Does the Prime-Circle refinement system canonically force a **transverse or nonlocal operator/form on the arithmetic solenoid** whose matrix elements or spectral data retain the prime-power/valuation discriminator lost by the radial Haar and bare leafwise-Laplacian reductions, without adding an external denominator/height weighting by hand?

The test is deliberately owner-local: any candidate must be derived from already-persisted Prime-Circle refinement, shell, root, or valuation data. Importing an arbitrary adelic weight or a generic pseudodifferential symbol does not answer the question.

## Decisive test

A positive resolution must exhibit one specified operator/form forced by the Prime-Circle construction and prove all of the following:

1. its definition uses transverse/refinement data before the PC-058--PC-061 radial/Haar collapse;
2. a concrete invariant of the operator distinguishes rational-prime structure from a matched composite or relabeled control preserving the same ambient solenoid/refinement layer;
3. the invariant is not reducible to the universal rational-square leaf spectrum of PC-065 or to an externally prescribed denominator/height weight;
4. the operator lies in an analytically usable category for the claimed next step (for example compact relative resolvent, a justified Schatten class, or a separately proved sign/coercivity property), rather than inferring arithmetic significance from spectrum alone.

A negative resolution may instead prove that every canonical refinement-compatible transverse construction in a precisely stated natural class factors through the same profinite-Haar/rational-frequency data, or that any prime-selective version necessarily introduces extra arithmetic structure not forced by Prime Circle. Either result would materially narrow the line.

## Evidence boundary

This clue is not evidence that such an operator exists, that the arithmetic solenoid is an RH model, or that transverse finite-adic structure is automatically prime-selective. PC-065 establishes the opposite warning for the bare leaf geometry: its canonical spectrum is classical and too large, and regularizations based on denominator or height inject structure absent from that metric.

The clue therefore keeps the remaining question upstream of spectral interpretation: **is there any canonical Prime-Circle transverse discriminator left before the final scalar/leafwise compression?**
