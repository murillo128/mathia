---
id: CLUE-visual_exploration-macroscopic-magnetic-frustration-density
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-218-subcritical-effective-edge-density-closes-magnetic-rms.md
  - research/visual_exploration/mind/intuition/MI-015-prime-phase-worst-starts-are-frustrated-torus-optimization.md
---

# Can canonical prime-phase graphs sustain extensive magnetic frustration?

## Observation

The current magnetic branch has an exact edge-capacity cycle-packing lower-bound mechanism, while `VIS-218` closes the sparse route: when the effective packed-cycle edge density is subcritical, the resulting certificate is too small to force a non-vanishing normalized RMS obstruction. The unresolved regime is therefore not merely whether frustrated cycles exist, but whether frustration can occupy a macroscopic fraction of the graph under the same edge-capacity constraints.

## Research question

For an increasing canonical prime-phase graph family, does there exist a sequence of feasible fractional cycle packings whose total certified frustration is `Omega(|E|)`, equivalently strong enough to keep the normalized magnetic RMS bounded away from zero under the established normalization? If so, is that extensive packing/frustration density special to the canonical arithmetic phases rather than generic in matched geometric or surrogate-phase controls?

## Why it may matter

This is the remaining scale at which the present magnetic obstruction could become globally consequential after `VIS-218`. A positive answer would convert local nonzero holonomy into an extensive obstruction that survives normalization; a negative answer would close the current cycle-packing route to a global RMS separation and force the visual branch toward a different invariant or normalization.

## Decisive test

Formulate the finite edge-capacity fractional cycle-packing optimization using the exact cycle-frustration weights already justified by the magnetic findings, and evaluate or bound its optimum `P_G` along increasing graph sizes. The route survives only if `P_G/|E|` is bounded below away from zero on the canonical prime-phase family, with that normalization translated explicitly into the magnetic RMS lower bound.

Run matched controls preserving graph geometry, degree profile, admissible cycle lengths, and other already-identified structural confounds while replacing the arithmetic phase data by the strongest reasonable surrogate ensemble. A canonical/control separation must persist under those controls. Kill the route if `P_G=o(|E|)`, if extensive packing is recreated at comparable scale by the controls, or if the apparent lower bound is carried only by a small exceptional subgraph whose edge mass vanishes globally.

## Evidence boundary

`VIS-218` establishes only that subcritical effective edge density is insufficient and records the existing cycle-packing mechanism; `MI-015` supplies the current torus-frustration interpretation. Neither establishes existence of an extensive feasible packing, a positive asymptotic packing density, canonical/control separation, or a non-vanishing global magnetic RMS obstruction. This clue isolates that missing macroscopic-scale test; it is not evidence that canonical prime phases are extensively frustrated.
