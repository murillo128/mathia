---
id: PA-gaussian-conditioning-adaptive-linear-information
type: prior-art
canonical_name: Gaussian conditioning under adaptive linear information
aliases:
  - conditional Gaussian measure for adaptive information
kind: information-based complexity method
topics:
  - adaptive-information
  - gaussian-measures
---

# Gaussian conditioning under adaptive linear information

## What it is

For a finite-dimensional Gaussian input, independent linear observations selected from previous answers leave an affine Gaussian conditional law on the remaining directions. Kunsch's Lemma 2.2 gives its projection representation and an inductive proof for adaptive information. Section 2.2 uses truncated Gaussian input measures for randomized lower bounds.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-578-continuous-randomness-retains-fixed-budget-polynomial-calibration-obstruction|AF-578]], equations (6)–(9), uses Gaussian polynomial coefficients and innovation energy. [[research/xi_flow/findings/XF-206-noiseless-analytic-calibration-retains-sharp-stopping-tails|XF-206]], equations (13)–(20), uses conditional Gaussian continuity, then conditions the input prior onto an admissible coefficient region. Both draw one calibration before the policy's seed.

## Known scope and limits

Conditioning on an admissibility region does not generally preserve a Gaussian law. XF-206 applies Gaussian formulas before that truncation and separately bounds its total-variation cost. The cited linear-approximation lower bounds do not by themselves prove these discrete-label theorems. Source-gap interpolation, endpoint-flat coefficient room and stopping certificates require the findings' own arguments. No RH implication follows.

## Related prior art

[[research/prior_art/incremental/PA-le-cam-two-point-testing|Le Cam testing]] converts sufficiently close admitted transcript mixtures into error lower bounds; it is distinct from the conditional-measure calculation.

## Evidence and provenance

- Robert J. Kunsch, *High-Dimensional Function Approximation: Breaking the Curse with Monte Carlo Methods* (2017), §2.2 and §2.2.1, Lemma 2.2, printed pp. 18–22: [author dissertation](https://arxiv.org/pdf/1704.08213).
- Persisted lookup triggers: `research/arithmetic_fidelity/findings/AF-578-continuous-randomness-retains-fixed-budget-polynomial-calibration-obstruction.md`, “Adaptive Gaussian transcript bound” and “Prior art, delta, and limits”; `research/xi_flow/findings/XF-206-noiseless-analytic-calibration-retains-sharp-stopping-tails.md`, “Finite adaptive Gaussian transcripts are continuous in the mean shift” and “Controls, prior art, and consequence”.
