---
id: PA-randomized-integration-unsolvability-on-unrestricted-smooth-functions
type: prior-art
canonical_name: Randomized integration unsolvability on unrestricted smooth functions
aliases:
  - Kunsch–Novak–Rudolf smooth integration obstruction
kind: information-based complexity theorem
topics:
  - adaptive-information
  - randomized-stopping
---

# Randomized integration unsolvability on unrestricted smooth functions

## What it is

Kunsch, Novak and Rudolf's Theorem 3.15 rules out guaranteed integration accuracy over all of C∞([0,1]) using randomized adaptive point values, even allowing an almost-surely finite, input-dependent number of observations. For any positive absolute tolerance and failure probability below one half, no such algorithm works uniformly on this unrestricted class.

Their proof compares the zero input with smooth bumps supported in increasingly small partition cells. Amplitudes are unrestricted. A fixed distribution over bumps hides a large integral from the finite observations with high probability; the realized algorithm seed does not select the input.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-580-positive-noise-destroys-finite-stopping-under-unknown-polynomial-calibration|AF-580]] explicitly cites this as prior art for the general sequential-impossibility mechanism. Its own theorem constructs exact compact-window matches inside finitely many source classes with polynomial calibration and small bounded errors. That source-specific construction and sharp label-error/return inequality are proved in AF-580, not supplied by the integration theorem.

## Known scope and limits

The theorem concerns unrestricted smooth integrands, without a common norm or derivative bound. It does not automatically apply to a fixed finite calibrated source family, imply its full-curve aliasing, or rule out finite stopping under quantitative promises. It provides no RH implication.

## Related prior art

[[research/prior_art/incremental/PA-weierstrass-polynomial-approximation|Compact-interval polynomial approximation]] is the distinct classical ingredient used to realize AF-580's local matches. The two results are not an asserted general equivalence.

## Evidence and provenance

- Robert J. Kunsch, Erich Novak and Daniel Rudolf, *Solvable Integration Problems and Optimal Sample Size Selection*, [author manuscript, arXiv:1805.08637v2](https://arxiv.org/pdf/1805.08637v2), introduction's solvability definition and §3.4, Theorem 3.15, printed p. 35.
- Live lookup trigger: `research/arithmetic_fidelity/findings/AF-580-positive-noise-destroys-finite-stopping-under-unknown-polynomial-calibration.md`, “Prior art, mathematical delta, and limits”.
