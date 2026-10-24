---
id: PA-polynomial-interpolation-early-termination
type: prior-art
canonical_name: Randomized early termination in polynomial interpolation
aliases:
  - interpolation post-testing
kind: randomized algebraic algorithm
topics:
  - polynomial-interpolation
  - identity-testing
---

# Randomized early termination in polynomial interpolation

## What it is

Randomized early termination allows black-box interpolation without a supplied degree or sparsity bound. Kaltofen and Lee analyze Monte Carlo stopping and describe fitting at nonrandom interpolation nodes followed by testing agreement at a random coordinate. Their §6 also describes random post-tests of a computed interpolant.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]] explicitly identifies this as prior art for its interpolation-and-validation mechanism. Its source quotient, nonpolynomial prime-edit gaps and exact continuous-real observation model are separately stated there.

## Known scope and limits

The cited finite-sampling Monte Carlo guarantees are not a zero-error theorem for arbitrary analytic residuals. AF-577 instead proves almost-sure identification for each fixed input using null analytic zero sets, one independent continuous validation coordinate, and exact equality tests. It does not implement that coordinate with finitely many random bits or supply a positive uniform noise margin.

## Related prior art

Classical polynomial interpolation and identity testing provide the background. The source's analytic-zero-set argument is an additional ingredient, not a consequence of the finite-sampling error estimate.

## Evidence and provenance

- Erich Kaltofen and Wen-shin Lee, *Early Termination in Sparse Interpolation Algorithms*, *Journal of Symbolic Computation* 36 (2003), 365–400, §1.2 and §6: [author manuscript](https://kaltofen.math.ncsu.edu/bibliography/03/KL03.pdf).
- Live lookup trigger: `research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification.md`, “Prior art, mathematical delta, and limits”.
