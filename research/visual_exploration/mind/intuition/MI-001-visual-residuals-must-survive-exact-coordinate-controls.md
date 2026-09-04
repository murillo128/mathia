# MI-001 — Visual residuals must survive exact reconstruction, deterministic quotient, and matched statistical controls

**Evidence level:** supported through VIS-022 by exact reconstruction identities, deterministic Gram-coordinate quotients, and literature-backed statistical baselines; the currently open review on VIS-023 is not used here

## Core intuition

Visual complexity is not an independent arithmetic resource when it can be reconstructed from coordinates, divisor data, regular holomorphic continuation, phase gauge, or lower-order probability laws. The meaningful object is the residual after the strongest baseline that preserves the information already known to generate the picture.

The Gram-point evidence adds an exact quotient hierarchy. Interval occupancy, the sampled zero-count discrepancy `S(g_n)`, and the zero-count staircase increments are the same discrete information up to an initial integer. Hardy-`Z` sign changes at Gram points are only the parity projection of that occupancy. A visual atlas should therefore count these as one information family, not as independent channels whose agreement strengthens a claim.

## Strongest justified principle

VIS-013--VIS-018 classify complete circular modulus/phase data, connected overlap gluing, and winding as zero/divisor information plus harmonic boundary data and one global gauge.

VIS-019--VIS-020 establish the statistical control layer: finite-size CUE/arithmetic corrections are the baseline for adjacent gaps, and once two overlapping adjacent-pair marginals are fixed, the unique maximum-entropy three-gap completion is the first-order Markov closure with KL gap equal to conditional mutual information.

VIS-021 gives the deterministic Gram identity

`C_n = 1 + S(g_{n+1}) - S(g_n)`.

Thus interval occupancy and Gram-sampled `S` are invertible encodings once one initial count is supplied. VIS-022 then shows

`sgn Z(g_{n+1}) / sgn Z(g_n) = (-1)^{C_n}`,

without assuming RH: off-line reflected zeros contribute even multiplicity. Gram-sign data are therefore strictly coarser than occupancy, not a second zero statistic.

## What remains possible

Higher-order or long-range residuals, deliberately incomplete measurements with quantified recovery defect, separated-region bridge observables, and non-holomorphic/multi-object representations remain live. Any visual comparison should first collapse exact deterministic equivalence classes and then construct matched statistical closures separately on zeta and control data.

## Status / novelty

Complex-analysis reconstruction, Gram counting identities, Hardy `Z`, finite-size random-matrix spacing theory, maximum entropy, and conditional mutual information are prior art or exact persisted derivations. The synthesis is the strengthened visual gate: **independent-looking renderings are not independent evidence when exact maps recover one from another**.

## Falsification criterion

Exhibit a visual/statistical channel outside the covered deterministic/reconstruction quotients that separates zeta from matched controls preserving the same retained information, with a statement stable under rendering and binning choices.

## Lean-formalizable core

- Argument-principle winding as divisor count.
- Gram occupancy as discrete derivative of sampled `S`.
- Hardy-`Z` Gram-sign transition as occupancy parity.
- Maximum-entropy Markov completion from overlapping pair marginals.
