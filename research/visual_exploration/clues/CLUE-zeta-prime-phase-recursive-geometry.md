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
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
  - research/visual_exploration/findings/VIS-072-fixed-prime-window-discrepancy-sinc-spectrum.md
  - research/visual_exploration/findings/VIS-074-additive-log-euler-window-corridor.md
  - research/visual_exploration/findings/VIS-075-holomorphic-euler-product-positive-cone-window-law.md
  - research/visual_exploration/findings/VIS-076-squared-euler-product-signed-mode-fixed-support-bound.md
  - research/visual_exploration/findings/VIS-078-signed-euler-product-l2-energy-certificate-gap.md
  - research/visual_exploration/findings/VIS-079-signed-euler-product-triangular-autocorrelation.md
  - research/visual_exploration/findings/VIS-080-signed-euler-product-coprime-ratio-support-crowding-floor.md
  - research/visual_exploration/findings/VIS-081-signed-euler-product-dickman-scaling-law.md
  - research/visual_exploration/findings/VIS-082-signed-euler-product-sharp-log-cutoff-threshold.md
  - research/visual_exploration/findings/VIS-083-gram-point-prime-phase-haar-equidistribution.md
  - research/visual_exploration/findings/VIS-084-gram-short-block-prime-phase-freezing.md
  - research/visual_exploration/findings/VIS-085-gram-local-arc-growing-support-collapse.md
---

# Can a zeta visual statistic leave the prime-torus information class?

## Observation

The prime-phase program has closed several increasingly sophisticated apparent escape routes.

`VIS-064`--`VIS-066` show that once the explicit hybrid residual is retained, quotient compensation, prime/zero contrast, and deterministic recombination do not create a new information channel: the complete factor/residual field is related by an invertible shear. `VIS-071` identifies the long-height law of every fixed finite prime field with its shared-phase Haar control, while `VIS-072` gives the exact finite-window sinc filtering of the same torus frequencies.

The nonlinear Euler-product branch is also sharply classified. `VIS-074` removes additive cross-prime small divisors, `VIS-075` shows that the raw holomorphic finite Euler product stays in the positive exponent cone, and `VIS-076` closes fixed-support signed beats for `|P_X|^2`. `VIS-078`--`VIS-079` then replace misleading reciprocal-frequency certificates by the exact sinc-filtered energy and its one-variable triangular autocorrelation form. `VIS-080`--`VIS-082` close the growing-support signed route: the normalized triangular energy tends to zero exactly when `log X/L -> 0`, while persistence outside that corridor is already forced by ordinary coprime-ratio support crowding.

Gram sampling supplies complementary global and local controls. `VIS-083` proves Haar equidistribution for every fixed finite prime-phase vector over the Gram population. `VIS-084` shows that consecutive sublogarithmic Gram blocks freeze and logarithmic blocks first trace a deterministic torus arc.

`VIS-085` now removes the apparent longer-block loophole much more broadly than its original logarithmic formulation. For arbitrary block length `H_n` and prime cutoff `P_n`, after subtracting the first-order inverse-theta arc one has

`max_(h<=H_n,p<=P_n) |R_(n,h)(p)-1| << H_n^2 log P_n/[g_n(log g_n)^3]`.

Thus the Gram-clock residual collapses whenever

`H_n^2 log P_n=o(g_n(log g_n)^3)`.

For polynomial prime support this includes every `H_n=o(sqrt(g_n) log g_n)`, vastly beyond the first `Theta(log g_n)` phase-motion scale. Longer blocks alone therefore do not produce a new local information channel throughout this entire corridor.

## Research question

After these closures, does any **independently anchored** or **independently calibrated factor/residual** visual statistic expose information that is not already determined by the prime torus, its exact observation-window/sampling geometry, or an invertible coordinate change of the same underlying field?

Three possibilities remain materially distinct.

First, a Gram/prime-phase route may operate beyond the proved corridor `H_n^2 log P_n=o(g_n(log g_n)^3)`, where first-order arc subtraction no longer forces a vanishing coordinate residual. Such a route must establish an actual residual law rather than interpret failure of the current bound as positive evidence.

Second, an externally anchored observable may add a source coordinate not determined by the prime phases and the Gram clock — for example a genuinely informative zero/Gram analytic quantity — and then test a joint law that survives the matched prime-phase sampling null.

Third, a hybrid factor/residual statistic may be meaningful if it tests a joint law or dependence property that is not a deterministic consequence of the invertible factor/residual shear and is calibrated at the actual claim strength.

## Why it may matter

The current sequence of controls shows how easily visual structure can be generated by representation and sampling alone. The same prime field is globally Haar on fixed support, locally frozen on very short Gram blocks, organized into a deterministic arc at the first motion scale, and still arc-complete over much longer blocks after the Gram-clock curvature is bounded correctly.

A surviving statistic would therefore have a substantially stronger interpretation. It would need either a scale at which the prime-phase sampling null genuinely changes, an independently supplied coordinate/source law, or a joint-law statement that remains nontrivial after exact factor/residual information accounting.

## Decisive test

For an externally anchored route, define the anchor without using the prime-torus statistic being tested. Freeze the anchor rule, window, scale, normalization, witness, and comparison before confirmation. Determine the induced law and sampling geometry of the admitted prime-phase field under that anchor before interpreting a visual effect.

For consecutive Gram windows, first compare against `VIS-084` and `VIS-085`. Inside

`H_n^2 log P_n=o(g_n(log g_n)^3)`,

kill any claim whose signal can be reduced to raw phase clustering, the deterministic first-order torus arc, or the remaining nonlinear Gram-clock residual: `VIS-085` forces that coordinatewise residual to zero. A positive prime-phase route must either leave this corridor and derive a nontrivial residual law there, or use information not determined by the prime phases and their sampling clock.

Do not treat merely leaving the corridor as confirmation. Outside it, derive the correct higher-order or nonlocal sampling null and then show that the proposed statistic survives it. A natural next mathematical test is whether second- or higher-order inverse-theta subtraction extends the deterministic-null corridor further; that is a separate question, not evidence for a positive separator.

`VIS-083` still kills population-level fixed-prime claims when the induced law is merely Haar. Do not infer growing-dimensional Haar behavior from the local arc bounds.

For a factor/residual route, construct the hybrid prime factor, zero factor, and explicit residual independently. Reduce deterministic recombinations using `VIS-064`--`VIS-066`, then state the remaining claim as a property of the joint `(factor,residual)` law that would still be nontrivial after an invertible coordinate change. Calibrate that property with the finite-window and control uncertainty appropriate to its actual dimensionality. Kill the route if the claimed effect is forced by the shear, by marginal rescaling, by overlap/search selection, or by a null that preserves the same admitted joint information.

## Evidence boundary

The signed squared-Euler-product branch is resolved negatively as a separator by `VIS-080`--`VIS-082`. Gram-point anchoring is classified at several levels: `VIS-083` gives fixed-prime population Haar behavior, `VIS-084` gives raw short-block freezing and the first deterministic local arc, and `VIS-085` gives uniform first-order arc-removal collapse throughout the explicit `H_n^2 log P_n=o(g_n(log g_n)^3)` corridor.

None of these findings proves a nontrivial law beyond that corridor, growing-dimensional Haar equidistribution, a zeta approximation strong enough for the intended inference, independence of prime and zero data, or an RH consequence. In particular, failure of the `VIS-085` upper bound to vanish outside its corridor is not a lower bound and is not evidence that a visual residual survives.

## Research disposition

Accepted in further narrowed form. Continue only through a Gram/prime-phase statistic that survives the correct sampling null outside the proved first-order corridor, an independently informative added coordinate/source law, or an independently calibrated factor/residual joint-law question. Do not reopen shorter or polynomial-support Gram blocks merely by using more points, more primes, or a different rendering of the same prime-phase field.