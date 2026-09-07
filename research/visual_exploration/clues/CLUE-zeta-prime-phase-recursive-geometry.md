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
  - research/visual_exploration/findings/VIS-072-fixed-prime-window-discrepancy-sinc-spectrum.md
  - research/visual_exploration/findings/VIS-073-growing-prime-support-averaging-corridor.md
---

# Can prime-by-prime zeta approximants expose structure beyond the prime torus itself?

## Observation
The hybrid Euler--Hadamard representation gives a mathematically justified critical-strip scale decomposition into a finite von-Mangoldt prime factor, an independently defined smoothed zero factor, and an explicit residual. `VIS-010` and `VIS-064`--`VIS-066` show that quotient compensation, the raw prime/zero contrast, and arbitrary deterministic recombinations of the complete prime/zero increment fields do not create an additional information channel once the residual is retained.

`VIS-067`--`VIS-070` make the shared-prime-phase control exact: its covariance, all finite connected cumulants, and complete finite-dimensional characteristic law are deterministic consequences of the prime-power coefficient arrays. `VIS-071` then identifies that Haar control with the long-height law of the deterministic finite prime-phase orbit itself.

`VIS-072` closes the nearest finite-window escape at fixed finite support. A fixed window is a continuous function of the same torus initial phase, so the population of actual sliding-window statistics across starting heights converges to the frequency-preserving random-initial-phase control. For trigonometric-polynomial witnesses, the finite-window discrepancy is exactly a sinc-filtered spectrum of log-rational small divisors `lambda_m=sum_p m_p log p`.

`VIS-073` closes a first explicit part of the growing-support escape. For a prime cutoff `X`, coordinate degree bounded by `D_X`, window length `L`, and nonconstant Fourier `l1` mass `A_X`, the whole window-average discrepancy is uniformly bounded by

`A_X min(1, 2 exp(D_X vartheta(X))/L)`.

Hence merely letting the number of admitted primes grow does not create a new information class. Any bounded-degree trigonometric witness with `A_X exp(D_X vartheta(X))/L -> 0` is still uniformly absorbed by the same torus null. The growing-support question begins only outside that safe corridor, or for witness classes not controlled by this Fourier box estimate.

## Research question
After quotient/reconstruction controls, fixed-prime vertical equidistribution, the exact finite-window resonance null, and the explicit safe growing-support corridor are accounted for, is there a representation-stable visual statistic in the hybrid hierarchy that genuinely leaves the prime-torus information class?

The remaining admissible routes are now narrower: a growing-support or growing-complexity regime that deliberately leaves the `VIS-073` corridor and comes with a stronger witness-specific quantitative small-divisor/equidistribution theorem; an externally anchored finite window whose anchor contributes independent information and whose selection is controlled; or a factor/residual dependence statistic whose residual component is independently defined and whose joint null is explicitly calibrated.

## Why it may matter
The prime-phase visual program has progressively removed increasingly sophisticated false positives: quotient algebra, residual-controlled compensation, coordinate recombination, covariance structure, all finite cumulants, the full fixed-finite phase law, finite-window population geometry driven by the same Kronecker frequencies, and now a concrete family of growing-support trigonometric witnesses.

A surviving signal would therefore have to identify a real boundary of the prime-torus model rather than another rendering of its small-divisor structure. That sharply separates genuinely new information from visually strong but expected resonance geometry.

## Decisive test
For a growing-support route, first write down the exact prime cutoff `X`, Fourier/coordinate degree envelope `D_X`, window length `L`, and nonconstant Fourier mass of the frozen witness. If `A_X exp(D_X vartheta(X))/L -> 0`, kill the pointwise window-average route immediately by `VIS-073`; for an RMS claim, apply its corresponding `R_X` condition. Leaving that sufficient corridor is not evidence of arithmetic structure: it only means the elementary degree-box bound no longer decides the question.

Only after that gate, prove or import a quantitative equidistribution or small-divisor estimate uniform over the exact mode family needed by the witness. The estimate must beat the relevant Fourier-mass envelope strongly enough that the claimed residual cannot be explained by slow Kronecker filling or near-resonant `P`-smooth ratios. If the witness is not a trigonometric window average, state exactly which approximation complexity, continuity modulus, or nonlinear path feature prevents `VIS-073` from applying and control that new cost explicitly.

For an externally anchored finite-window route, define the anchor independently of the prime-torus statistic, freeze the window rule and witness before confirmation, and compare against the exact frequency-preserving random-initial-phase law from `VIS-072`. Account for any search over anchors, windows, scales, or witnesses. Kill the route if the anchor is reconstructible from the same finite prime field or if the effect is reproduced by the matched resonance null.

For a factor/residual statistic, construct the hybrid prime factor, zero factor, and explicit residual independently, reduce deterministic prime/zero recombinations using `VIS-064`--`VIS-066`, and calibrate the joint `(factor,residual)` null at the actual claim strength. Apply `VIS-060`--`VIS-063` to separate exact null specification from finite-window/control uncertainty.

## Evidence boundary
`VIS-067`--`VIS-070` determine the fixed finite shared-phase null, `VIS-071` proves that the deterministic vertical prime field has that same long-height Haar law, and `VIS-072` proves that fixed-length sliding-window populations converge to the corresponding frequency-preserving initial-phase null while giving an exact sinc-filtered Fourier formula for trigonometric witnesses. `VIS-073` adds only a sufficient growing-support corridor for bounded-degree trigonometric window averages with controlled Fourier mass.

None of these findings supplies a sharp growing-support threshold, proves that a witness outside the `VIS-073` corridor separates from the torus null, handles arbitrary growing-dimensional continuous path functionals, proves that a particular externally anchored window is arithmetic-specific, gives a new prime/zero independence result, determines an unexpected factor/residual joint law, or implies RH. The surviving routes remain hypotheses requiring new information beyond the controlled prime-torus regimes.

## Research disposition
Accepted in further narrowed form. Treat fixed-finite long-height population separation, fixed-finite sliding-window population separation, and the `VIS-073` safe corridor for bounded-degree growing-support window averages as closed. Continue only through a quantitatively justified regime outside that corridor, an independently anchored and selection-audited window, or an independently calibrated factor/residual coordinate.