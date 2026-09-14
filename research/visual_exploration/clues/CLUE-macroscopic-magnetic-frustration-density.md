---
id: CLUE-visual_exploration-macroscopic-magnetic-frustration-density
type: research-clue
status: rejected
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md
  - research/visual_exploration/findings/VIS-219-cycle-packing-must-saturate-envelope-to-rms.md
  - research/visual_exploration/mind/intuition/MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization.md
---

# Can canonical prime-phase graphs sustain extensive magnetic frustration?

## Observation

The current magnetic branch has an exact edge-capacity cycle-packing lower-bound mechanism, while `VIS-218` closes the normalized magnetic spectral relaxation in the strictly subcritical regime. This clue originally proposed that the remaining cycle-packing route should be tested through an extensive raw packing/frustration density.

## Research question

For an increasing canonical prime-phase graph family, can one obtain a feasible fractional cycle packing with macroscopic aggregate frustration, and would such an extensive packing be special to the canonical arithmetic phases rather than generic in matched geometric or surrogate-phase controls?

## Why it may matter

Distributed cycle frustration remains a potentially stronger static mechanism than the normalized spectral relaxation. However, the original formulation treated a positive extensive density as though it were equivalent to the strength required for a Haar-RMS-scale worst-start certificate.

## Decisive test

The originally proposed test was to evaluate or bound the weighted fractional cycle-packing optimum `P_G` and ask whether `P_G/|E|` stays bounded below away from zero, with matched controls preserving graph geometry and replacing arithmetic phases.

`VIS-219` shows that this is not the correct normalization for the desired RMS conclusion. The packing objective is a weighted energy and rescales with the coefficients while `|E|` does not. More decisively, the `VIS-215` upper certificate has exact normalized residual

`[B-min(P_+,P_-)]/sqrt(R)`
` = sqrt(2N_eff) [1-min(P_+,P_-)/B]`.

Thus a fixed positive packing fraction is insufficient when `N_eff` diverges. The relevant test must instead ask whether the packing certificate nearly saturates `B` to within `O(sqrt(R))`.

## Evidence boundary

This rejected clue does not establish that extensive frustrated cycles fail to exist. It establishes only that **extensivity or positive raw packing density is not the quantitative criterion needed for the intended RMS-scale certificate**. The corrected saturation question is handed off separately.

## Research disposition

Rejected because the proposed normalization and claimed implication are incorrect for the target bound. `VIS-219` proves that `P_G/|E|` is not scale-invariant and that the `VIS-215` certificate can reach Haar-RMS scale only if

`B-min(P_+,P_-)=O(sqrt(R))`,

equivalently `1-min(P_+,P_-)/B=O(N_eff^(-1/2))`.

Successor question: `research/visual_exploration/clues/CLUE-magnetic-packing-envelope-saturation.md`.