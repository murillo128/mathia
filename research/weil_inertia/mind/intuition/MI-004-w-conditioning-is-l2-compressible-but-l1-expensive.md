# MI-004 — Hierarchical conditioning saves norm structure only by exposing a genuine four-prime rectangle

**Evidence level:** supported by exact Fourier-conductor identities, redundancy lower bounds, and the exact residue-summed rectangle expansion

## Core intuition

The `W`-local conditioning spectrum has real projective `L^2` structure, but exploiting it is not a purely functional-analytic compression problem. The current per-modulus interface cannot be made cheap by sparse selection, soft attenuation, one common refinement, or redundant overlapping refinements. Opening the natural residue-summed square function reveals exactly why: the vector norm itself is a four-prime rectangle correlation. A successful hierarchical estimate therefore requires new source information, not just a better norm inequality.

## Strongest justified principle

WI-058--WI-064 establish the first separation. The squared Fourier mass lives on subpolynomial conductors, but no fixed polylog cutoff captures asymptotically all of it; every asymptotically lossless diagonal retention has super-polylogarithmic conductor-weighted cost. Pair errors across divisor refinements nevertheless satisfy exact conditional-expectation/martingale identities, and reduced additive frequencies are consistent across multiples. A single common refinement can exploit orthogonality by Parseval, but the available residue-maximum input then pays the full refinement modulus.

WI-065 closes the obvious redundant-refinement repair. Even if every conductor is split arbitrarily across many refinement moduli and residue handling is treated optimistically inside the same Mikawa-type budget, the best weighted-frame lower bound saves at most a logarithm. An asymptotically lossless family still has super-polylogarithmic cost. The obstruction is therefore not an unlucky choice of partition.

WI-066 identifies the arithmetic content of the desired vector estimate. For the shifted pair sequence, summing the squared residue-conditioned errors over classes opens to a rectangle correlation of the form

`Lambda(n) Lambda(n+h) Lambda(n+r) Lambda(n+r+h)`

with the modulus encoded in the rectangle separation. Centering removes local main terms but does not kill the off-diagonal rectangle. Thus a residue-averaged `L^2` theorem is already a fourth-moment prime theorem in disguise.

WI-068--WI-070 then show that this rectangle cannot be discharged for free by existing finite-complexity representations: freeing shifts creates a thin slope selector, while aggregating bases produces a multivariate anisotropic polynomial-prime system. The hierarchy is useful because it identifies the right square-function geometry, but the missing estimate must carry this genuine higher-correlation source structure.

## What remains possible

A blockwise martingale theorem, vector-valued pair-in-AP dispersion estimate, or direct rectangle covariance theorem could still exploit the projective structure without paying a giant refinement modulus. It must, however, prove the required four-prime control rather than assume that `L^2` orthogonality alone supplies it. A Yang-specific cancellation identity that removes the rectangle would be equally decisive.

## Status / novelty

The conductor law, lossless-retention obstruction, redundant-refinement lower bound, divisor-martingale identities, and rectangle expansion are persisted exact findings. The Mikawa/Shao--Teräväinen interfaces remain literature-backed with the evidence boundaries recorded in the findings.

## Falsification criterion

Find an asymptotically lossless redundant refinement with polylogarithmic cost inside the WI-065 interface, or show that the residue-summed square function factors into only two-prime data despite WI-066's exact rectangle identity. A positive advance must control the rectangle in a source-faithful hierarchical norm.

## Lean-formalizable core

- Lossless retention versus conductor-weighted cost.
- Redundant weighted-frame lower bound.
- Divisor-lattice conditional-expectation identities.
- Exact residue-sum-to-rectangle expansion.
