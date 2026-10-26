---
id: PA-best-term-hilbert-approximation-weak-sequence
type: prior-art
canonical_name: Best-term Hilbert approximation and weak sequence spaces
aliases:
  - Nonlinear n-term approximation in a Hilbert space
  - Decreasing coefficient rearrangement
kind: approximation theorem
topics:
  - nonlinear approximation
  - Hilbert spaces
  - weak sequence spaces
---

# Best-term Hilbert approximation and weak sequence spaces

## What it is

For an orthonormal Hilbert expansion with decreasing absolute coefficients \(c_j^*\), the squared best \(M\)-term error is \(\sum_{j>M}(c_j^*)^2\). Error \(O(M^{-s})\) is equivalent to \(c_j^*=O(j^{-s-1/2})\), or membership in weak \(\ell^p\) with \(1/p=s+1/2\), for \(s>0\).

## Relation to RH / Mathia research

[[research/nyman_beurling/findings/NB-370-adaptive-lattice-selection-removes-the-three-orbit-cutoff-logarithm|NB-370]] invokes this classical mechanism for its rearranged squared sample weights. Its return counting and physical component comparison are separate source-specific arguments.

## Known scope and limits

The exact tail identity requires orthonormal coordinates. A bounded Hardy lift needs comparison inequalities; it does not inherit Parseval. This theorem alone gives neither a finite-generator Nyman rate nor an RH conclusion.

## Related prior art

Weak sequence spaces describe coefficient decay; they do not certify the arithmetic hypothesis producing it. No equivalence to the Nyman–Beurling closure criterion is asserted.

## Evidence and provenance

Ronald A. DeVore, *Nonlinear approximation*, Acta Numerica 7 (1998), 51–150, [DOI: 10.1017/S0962492900002816](https://doi.org/10.1017/S0962492900002816). The [author manuscript](https://people.math.sc.edu/devore/publications/nlacta.pdf), §2 equations (2.18)–(2.19), §4 equations (4.22)–(4.23), and §5, supplies the rearrangement and weak-sequence statements.

Persisted lookup trigger: `research/nyman_beurling/findings/NB-370-adaptive-lattice-selection-removes-the-three-orbit-cutoff-logarithm.md`, “Prior art, mathematical delta, and limits.”
