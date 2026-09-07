---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
  - research/visual_exploration/findings/VIS-067-independent-prime-phase-scale-covariance-gram-kernel.md
  - research/visual_exploration/findings/VIS-068-shared-prime-phase-third-order-harmonic-resonances.md
  - research/visual_exploration/findings/VIS-069-shared-prime-phase-all-order-connected-resonance-cumulants.md
  - research/visual_exploration/findings/VIS-070-shared-prime-phase-full-characteristic-law.md
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
---

# Can prime-by-prime zeta approximants expose structure beyond the prime torus itself?

## Observation
The hybrid Euler--Hadamard representation gives a mathematically justified critical-strip scale decomposition into a finite von-Mangoldt prime factor, an independently defined smoothed zero factor, and an explicit residual. `VIS-010` and `VIS-064`--`VIS-066` show that quotient compensation, the raw prime/zero contrast, and arbitrary deterministic recombinations of the complete prime/zero increment fields do not create an additional information channel once the residual is retained.

`VIS-067`--`VIS-070` then make the shared-prime-phase control exact: its covariance, all finite connected cumulants, and complete finite-dimensional characteristic law are deterministic consequences of the prime-power coefficient arrays. Prime-phase randomization therefore has structured resonance geometry rather than a featureless-noise baseline.

`VIS-071` closes the most direct arithmetic-versus-null population comparison at fixed finite support. Because distinct prime logarithms have no nontrivial integer relation, the deterministic vertical prime-phase orbit is equidistributed on the same finite torus. Hence every bounded continuous statistic of a fixed finite coordinate field has the **same long-height Cesaro law** as the shared-phase Haar null from `VIS-070`.

The shared-phase null is therefore the asymptotic invariant law of the deterministic finite prime field itself, not merely an external randomized comparator.

## Research question
After quotient/reconstruction controls and finite-prime vertical equidistribution are accounted for, is there still a representation-stable visual statistic in the hybrid hierarchy that probes information **outside the fixed finite prime-torus law**?

The remaining admissible targets are narrower: a quantitatively controlled finite-window discrepancy relative to a null that preserves the same `log p` Kronecker dynamics, a regime where prime/harmonic support grows with height and uniform equidistribution is proved strong enough for the intended statistic, or a factor/residual dependence statistic whose residual component is independently defined and whose joint null is explicitly calibrated.

A fixed-finite long-height prime-factor statistic is no longer an admissible positive target: `VIS-071` proves that its population law converges to the shared-phase null.

## Why it may matter
This removes a large class of visually plausible false positives. A finite prime-factor field can display multiscale bands, anisotropy, nonlinear geometry, higher-order resonances, and complicated finite-grid topology while still being nothing more than one orbit of the same torus law used as its randomized control.

A surviving signal must therefore identify a genuine boundary of that equivalence rather than another statistic on the same fixed phase coordinates. That makes finite-window dynamics, growing-support limits, and prime/residual interaction substantially cleaner research questions.

## Decisive test
For a finite-window within-prime experiment, freeze the finite prime/harmonic support, scale pair, height offsets, window length, statistic, normalization, and claim strength before confirmation. Do **not** compare the observed vertical field with phases independently resampled at every height. Instead randomize the initial torus phase and evolve every control with the same deterministic frequency vector `(log p)` and the same phase-sharing convention. A candidate finite-window effect must separate the arithmetic starting orbit from this frequency-preserving ensemble and survive modest window/scale perturbations without post-hoc selection.

For a growing-support experiment, state an explicit relation such as `X=X(T)` and prove or import a quantitative equidistribution bound uniform enough over the resulting prime/harmonic/coordinate family to distinguish a genuine residual from slow Kronecker filling or near-resonance effects.

For a factor/residual statistic, construct the hybrid prime factor, zero factor, and explicit residual independently, reduce any prime/zero deterministic recombination using `VIS-064`--`VIS-066`, and calibrate the joint `(factor,residual)` null at the actual claim strength. Apply `VIS-060`--`VIS-063` to separate exact null specification from finite-window/control uncertainty.

Kill the route if the apparent signal is reproduced by the frequency-preserving Kronecker control, disappears under predeclared representation perturbations, is forced by known hybrid approximation error, or reduces to another deterministic function of already admitted coordinates.

## Evidence boundary
The hybrid decomposition is established prior art. `VIS-067`--`VIS-070` determine the finite shared-phase null from second order through its complete finite-dimensional law. `VIS-071` proves that at fixed finite support the deterministic vertical prime field has that same Haar law under long-height averaging by classical Kronecker/Bohr equidistribution.

None of these findings provides a finite-window discrepancy rate, a uniform theorem when support grows with height, a new prime/zero independence theorem, an unexpected factor/residual joint law, or an RH implication. A finite-window deviation from Haar is not automatically arithmetic evidence; it may only measure slow deterministic filling of the prime torus.

## Research disposition
Accepted in further narrowed form. Treat fixed-finite long-height prime-factor population separation from shared phases as closed. Continue only through a boundary not covered by `VIS-071`: frequency-preserving finite-window discrepancy, quantitatively justified growing support, or an independently calibrated factor/residual joint statistic.