---
id: PA-chebyshev-alternation
type: prior-art
canonical_name: Chebyshev alternation theorem
aliases:
  - polynomial equioscillation theorem
kind: uniform approximation theorem
topics:
  - polynomial-approximation
  - minimax-certificates
---

# Chebyshev alternation theorem

## What it is

For a continuous real function on a compact interval, approximation by polynomials of degree at most r has a unique uniform minimizer. A candidate is certified optimal if its residual stays within ±E throughout the interval and reaches alternating values ±E at r+2 ordered distinct nodes.

## Relation to RH / Mathia research

[[research/arithmetic_fidelity/findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic|AF-582]] uses three contacts for its affine approximant and four for its quadratic approximant. Its separate curvature argument controls the residual between contacts. This certifies the bounded-window quotient error, from which the source derives its binary noise radius and range cost.

## Known scope and limits

Alternating values alone do not certify a bound between nodes. The theorem supplies neither AF-582's moving-contact asymptotics nor its prime-edit transfer error. It concerns compact-interval approximation, with no arithmetic provenance or RH conclusion.

## Related prior art

[[research/prior_art/incremental/PA-weierstrass-polynomial-approximation|Weierstrass approximation]] allows degree to grow with tolerance; alternation certifies an optimum at fixed degree. [[research/prior_art/incremental/PA-hermite-polynomial-interpolation|Hermite interpolation]] matches prescribed finite data; it does not by itself minimize the uniform error.

## Evidence and provenance

- NIST Digital Library of Mathematical Functions, [§3.11(i), Minimax Polynomial Approximations](https://dlmf.nist.gov/3.11.i), existence/uniqueness and the sufficient alternation certificate.
- Persisted lookup trigger: `research/arithmetic_fidelity/findings/AF-582-quadratic-calibration-changes-sharp-window-cost-from-logarithmic-to-algebraic.md`, “Affine benchmark: an exact three-contact certificate” and “Quadratic certificate and its moving interior contact”, equations (6)–(13).
