---
id: CLUE-visual-exploration-prime-phase-critical-logarithmic-occupancy
type: research-clue
status: proposed
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
  - research/visual_exploration/findings/VIS-226-subcritical-prime-phase-box-grid-cannot-beat-net-scan.md
---

# Does the prime-phase coherence transition at `H ~ y/log y` reduce to logarithmic-scale prime occupancy?

## Observation

`VIS-225` obtains a subcritical worst-start lower bound by partitioning primes in `[y/2,y]` into phase-coherent frequency cells on which the sinc kernel stays uniformly positive. The corresponding prime-coordinate width is `Delta p = Theta(y/H)`. When `H=o(y/log y)`, these cells are much wider than `log y`; prime-number-theorem scale information then gives many primes per cell, and a Cauchy occupancy bound forces a macroscopic same-cell pair contribution.

At the critical scale `H=lambda y/log y`, the same construction changes character: `Delta p=Theta(log y)`, the number of cells and the number of primes are both `Theta(y/log y)`, and the mean occupancy is only `Theta(1)`. The coarse PNT+Cauchy certificate therefore stops forcing a positive linear surplus automatically. For this particular lower-bound mechanism, the representation factors through the cell-occupancy vector `(n_j)`: it retains the same-cell pair mass `sum_j binom(n_j,2)` needed for the positive sinc block, while discarding within-cell positions and all cross-cell kernel structure. This factorization applies only to the coherent-block certificate, not to the full prime-phase optimizer.

`VIS-226` independently shows that a naive fixed box-grid search does not provide a subcritical computational shortcut, so the critical occupancy boundary is not merely a restatement of that access-time obstruction.

## Research question

For fixed `lambda>0` and a pre-registered phase tolerance, what happens to the logarithmic-width occupancy statistic

`S_lambda(y)=sum_j binom(n_j,2)`

when `H=lambda y/log y`? In particular, is there a range of `lambda` for which `S_lambda(y)` has a positive linear-scale lower envelope relative to the number of primes in `[y/2,y]`, or does the coherent-block contribution fall to the scale predicted by generic logarithmic-gap occupancy?

If a non-generic occupancy effect survives, does it yield a genuine critical-scale worst-start lower bound that remains separated from the Haar-average `L2` scale, rather than merely extending the already-settled subcritical argument?

## Why it may matter

This is the first scale at which the visual/phase geometry appears to require genuinely local prime-spacing information. Below it, coarse prime density already forces coherent blocks; at `H ~ y/log y`, the cell width reaches the natural logarithmic prime-gap scale and local occupancy becomes load-bearing. Resolving this boundary could therefore identify whether the prime-phase transition contains arithmetic structure beyond the generic density mechanism, or whether the subcritical divergence simply dies when PNT-scale occupancy ceases to be deterministic.

## Decisive test

Fix the phase tolerance before inspecting outcomes, so that same-cell prime pairs have a uniform positive sinc-kernel lower bound. For `H=lambda y/log y`, partition `[y/2,y]` into the corresponding cells of width `c(lambda) log y` and obtain rigorous upper/lower information for `S_lambda(y)` from available short-interval or small-gap prime results. Compare the resulting occupancy scale with a matched random or Cramer-type logarithmic-gap baseline that preserves the same one-point prime density.

Then translate only the rigorously surviving same-cell mass back through the `VIS-225` kernel certificate. A useful positive result must show a stable excess or lower envelope not already forced by the matched generic occupancy model. Kill the route if the critical statistic is asymptotically generic, if existing prime-gap theory already makes the answer immediate with no residual mechanism, or if any apparent excess depends on tuning the cell phase after inspection. Before promotion to a finding, audit equivalent formulations in short-interval prime counts, prime-pair statistics, and logarithmic-scale gap literature.

## Evidence boundary

`VIS-225` establishes the coherent-block mechanism only in the subcritical regime where its occupancy forcing is coarse and robust. It does not establish critical-scale occupancy, a threshold in `lambda`, a critical worst-start divergence, or any RH consequence. The observation here is a representation-level boundary for that certificate: at `H ~ y/log y`, PNT-scale density alone no longer settles the same-cell pair mass. No novelty claim is made for logarithmic-width prime occupancy or the required short-interval/gap estimates.