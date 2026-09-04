# MI-001 — Visual residuals must survive deterministic quotients, statistical closures, ordering controls, and exact boundary layers

**Evidence level:** supported through VIS-028 by exact reconstruction identities, classical statistical geometry, finite-population discrepancy controls, and an exact Farey endpoint asymptotic

## Core intuition

Visual complexity is not an independent arithmetic resource when it can be reconstructed from ordinary coordinates, lower-order statistics, symmetry, ordering baselines, or a deterministic boundary layer. The meaningful object is the residual after the strongest control preserving the information already known to generate the picture.

For Farey discrepancy this now includes scale itself. The observed Dirichlet transition around mode index `r=Theta(n)` is not discriminating on its own: the exact unit-fraction endpoint fan already has width `Theta(n)` in rank space and forces precisely that spectral scale with an explicit continuum transform. A putative cross-scale arithmetic signal must therefore survive subtraction or matching of this boundary fan, not merely exhibit an `r/n` collapse.

## Strongest justified principle

VIS-013--VIS-025 classify circular reconstruction, Gram occupancy, sampled `S`, parity, and the first three-gap Markov/Pearson/correspondence residuals. These results show repeatedly that visually distinct representations can belong to the same deterministic or low-order statistical quotient.

VIS-026 holds the entire centered gap multiset fixed and randomizes only order, yielding an exact Brownian-bridge covariance and `L^2` baseline. VIS-027 additionally conditions on reflection symmetry; every odd Dirichlet sine mode then vanishes identically. The finite Farey suppression remaining after those nulls is genuine ordering information but is not yet mechanistically arithmetic.

VIS-028 adds a stronger deterministic control. The first `Theta(n)` Farey fractions are an exact unit-fraction fan, with a reflected copy at the right endpoint. After rank-grid centering, its discrepancy has the scaling `nD_k -> f(k/n)` and contributes a nonzero `Theta(1/n)` energy. In the Dirichlet basis its even coefficients satisfy a continuum law at `r=Theta(n)`, and the cumulative spectral energy converges under `r/n` scaling. Thus the existence of that scale and a substantial finite fraction of the observed energy can arise from classical endpoint geometry alone.

## What remains possible

For Farey-type discrepancy, remove the exact endpoint fan before interpreting modal collapse, or use a matched control that preserves the same boundary layer. Then test whether an even-mode or cross-band residual survives progressively stronger controls preserving the gap multiset, reflection, local adjacency, denominator strata, and mediant ancestry.

For three-gap data, retain orientation whenever scalar CMI or singular values would quotient it away. In every case the handoff should identify an exact residual statistic independent of rendering.

## Status / novelty

Likelihood-ratio geometry, correspondence analysis, permutation bridges, reflection parity, Farey endpoint structure, and sine transforms are classical or persisted exact reductions. The synthesis is the visual gate: **a scale, band, parity pattern, or residual becomes arithmetic evidence only after every deterministic structure capable of forcing it has been matched or removed**.

## Falsification criterion

Show that the VIS-028 endpoint fan does not produce the asserted `r=Theta(n)` spectral scale, or exhibit a residual that remains stable after endpoint subtraction and the existing ordering/symmetry controls while carrying source information absent from those controls.

## Lean-formalizable core

- Gram occupancy/S/parity quotient.
- Markov and Pearson interaction fibers.
- Same-gap permutation Brownian-bridge baseline.
- Reflection parity filter.
- Farey endpoint-fan spatial and Dirichlet scaling.
