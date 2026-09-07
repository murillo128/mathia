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
  - research/visual_exploration/findings/VIS-074-additive-log-euler-window-corridor.md
---

# Can prime-by-prime zeta approximants expose structure beyond the prime torus itself?

## Observation
The hybrid Euler--Hadamard representation gives a mathematically justified critical-strip scale decomposition into a finite von-Mangoldt prime factor, an independently defined smoothed zero factor, and an explicit residual. `VIS-010` and `VIS-064`--`VIS-066` show that quotient compensation, the raw prime/zero contrast, and arbitrary deterministic recombinations of the complete prime/zero increment fields do not create an additional information channel once the residual is retained.

`VIS-067`--`VIS-070` make the shared-prime-phase control exact: its covariance, all finite connected cumulants, and complete finite-dimensional characteristic law are deterministic consequences of the prime-power coefficient arrays. `VIS-071` then identifies that Haar control with the long-height law of the deterministic finite prime-phase orbit itself.

`VIS-072` closes the nearest finite-window escape at fixed finite support. A fixed window is a continuous function of the same torus initial phase, so the population of actual sliding-window statistics across starting heights converges to the frequency-preserving random-initial-phase control. For trigonometric-polynomial witnesses, the finite-window discrepancy is exactly a sinc-filtered spectrum of log-rational small divisors `lambda_m=sum_p m_p log p`.

`VIS-073` closes a first generic part of the growing-support escape by bounding a bounded-degree Fourier box through `exp(D_X vartheta(X))`. `VIS-074` then shows that this worst-case small-divisor cost is absent for additive one-prime-at-a-time harmonics. A coordinate-separable prime field has only frequencies `k log p`, and the logarithmic Euler field satisfies

`sup_h |(1/L) integral_h^(h+L) E_X(sigma,t) dt|`
` <= (2/L) sum_(p<=X) Li_2(p^(-sigma))/log p`.

On the critical line the right-hand side is `(4+o(1)) sqrt(X)/(L (log X)^2)`. Thus merely increasing the prime cutoff in the additive log-Euler representation remains inside an explicit weighted `1/L` averaging corridor whenever `L (log X)^2/sqrt(X) -> infinity`; cross-prime near resonances arise only after the witness itself mixes coordinates.

## Research question
After quotient/reconstruction controls, fixed-prime vertical equidistribution, the exact finite-window resonance null, the generic safe growing-support corridor, and the stronger additive log-Euler corridor are accounted for, is there a representation-stable visual statistic in the hybrid hierarchy that genuinely leaves the prime-torus information class?

The remaining admissible routes are now narrower: a growing-support witness whose **mixed-coordinate** Fourier complexity is essential and quantitatively controlled outside `VIS-073`; an externally anchored finite window whose anchor contributes independent information and whose selection is controlled; or a factor/residual dependence statistic whose residual component is independently defined and whose joint null is explicitly calibrated.

## Why it may matter
The prime-phase visual program has progressively removed increasingly sophisticated false positives: quotient algebra, residual-controlled compensation, coordinate recombination, covariance structure, all finite cumulants, the full fixed-finite phase law, finite-window population geometry driven by the same Kronecker frequencies, a generic bounded-degree growing-support corridor, and now the apparent growing-support escape of additive log-Euler fields themselves.

A surviving signal would therefore have to identify a real boundary of the prime-torus model rather than another rendering of its small-divisor or additive averaging geometry. In particular, “use more primes” is no longer a meaningful escape unless the proposed observable introduces mixed-coordinate structure or independent information and controls the resulting complexity explicitly.

## Decisive test
For a growing-support route, first classify the frozen witness by Fourier support. If it is coordinate-separable, apply `VIS-074` directly; for the critical-line logarithmic Euler field, kill the window-average route whenever `L (log X)^2/sqrt(X) -> infinity`. More generally use its exact weighted coefficient bound rather than the much looser full-box estimate.

If mixed-coordinate modes are genuinely present, write down the exact prime cutoff `X`, Fourier/coordinate degree envelope `D_X`, window length `L`, and nonconstant Fourier mass. If `A_X exp(D_X vartheta(X))/L -> 0`, kill the pointwise window-average route by `VIS-073`; for an RMS claim, apply its corresponding `R_X` condition. Leaving either sufficient corridor is not evidence of arithmetic structure: it only means those elementary bounds no longer decide the question.

Only after those gates, prove or import a quantitative equidistribution or small-divisor estimate uniform over the exact mixed-mode family needed by the witness. If the witness is nonlinear or a path functional, expand or approximate the actual Fourier support and account for the resulting approximation complexity, continuity modulus, or selection cost rather than attributing visually strong beat patterns to new arithmetic information.

For an externally anchored finite-window route, define the anchor independently of the prime-torus statistic, freeze the window rule and witness before confirmation, and compare against the exact frequency-preserving random-initial-phase law from `VIS-072`. Account for any search over anchors, windows, scales, or witnesses. Kill the route if the anchor is reconstructible from the same finite prime field or if the effect is reproduced by the matched resonance null.

For a factor/residual statistic, construct the hybrid prime factor, zero factor, and explicit residual independently, reduce deterministic prime/zero recombinations using `VIS-064`--`VIS-066`, and calibrate the joint `(factor,residual)` null at the actual claim strength. Apply `VIS-060`--`VIS-063` to separate exact null specification from finite-window/control uncertainty.

## Evidence boundary
`VIS-067`--`VIS-070` determine the fixed finite shared-phase null, `VIS-071` proves that the deterministic vertical prime field has that same long-height Haar law, and `VIS-072` gives the exact fixed-window sinc spectrum. `VIS-073` supplies a sufficient bounded-degree growing-support corridor for general trigonometric window averages. `VIS-074` supplies a substantially stronger corridor only for additive coordinate-separable prime harmonics, including the logarithmic Euler field.

None of these findings gives a sharp threshold for genuinely mixed growing-dimensional observables, proves that a witness outside the sufficient corridors separates from the torus null, handles arbitrary nonlinear growing-dimensional path functionals, proves that a particular externally anchored window is arithmetic-specific, gives a new prime/zero independence result, determines an unexpected factor/residual joint law, or implies RH.

## Research disposition
Accepted in further narrowed form. Treat fixed-finite population separation, fixed-finite sliding-window separation, the `VIS-073` generic safe corridor, and the `VIS-074` additive log-Euler growing-support corridor as closed. Continue only through quantitatively controlled mixed-coordinate growth, an independently anchored and selection-audited window, or an independently calibrated factor/residual coordinate.