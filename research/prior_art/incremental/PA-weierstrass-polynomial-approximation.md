---
id: PA-weierstrass-polynomial-approximation
type: prior-art
canonical_name: Weierstrass polynomial approximation theorem
aliases:
  - uniform polynomial density on a compact interval
kind: approximation theorem
topics:
  - polynomial-approximation
  - uniform-topology
---

# Weierstrass polynomial approximation theorem

## What it is

For each continuous real function on a compact real interval and each positive tolerance, a real polynomial approximates the function uniformly within that tolerance. The degree is allowed to depend on the function and tolerance.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-580-positive-noise-destroys-finite-stopping-under-unknown-polynomial-calibration|AF-580]], equations (5)–(7a), uses this theorem to approximate source gaps, or source gaps plus a continuous reference error, on each compact window. Its separate cutoff and transcript-exhaustion argument turns the residual into an admissible bounded error. [[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]], equation (10), uses compact-interval density for full-curve aliases on a bounded window.

## Known scope and limits

This gives neither a supplied degree/coefficient bound nor uniform approximation on an unbounded ray. AF-580's window-by-window matching does not contradict AF-579's positive full-ray separation margin. The approximation theorem alone is not a randomized stopping theorem or an arithmetic discriminator.

## Related prior art

[[research/prior_art/incremental/PA-polynomial-interpolation-early-termination|Randomized interpolation early termination]] concerns finite interpolation and validation, a different use of polynomials from uniform approximation of a whole interval.

## Evidence and provenance

- Lloyd N. Trefethen, *Approximation Theory and Approximation Practice*, extended edition (2019), Chapter 6, pp. 43–48: [SIAM chapter and theorem summary](https://epubs.siam.org/doi/10.1137/1.9781611975949.ch6), DOI `10.1137/1.9781611975949.ch6`.
- Live lookup trigger: `research/arithmetic_fidelity/findings/AF-580-positive-noise-destroys-finite-stopping-under-unknown-polynomial-calibration.md`, “Exact compact-window matching” and “Prior art, mathematical delta, and limits”.
