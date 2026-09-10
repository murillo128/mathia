---
id: CLUE-visual-exploration-zeta-montgomery-support-edge-arithmetic-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-123-montgomery-cue-edge-ramp-null-logarithmic-ripple.md
  - research/visual_exploration/findings/VIS-124-montgomery-weight-laplace-smooths-cue-edge.md
  - research/visual_exploration/findings/VIS-125-hard-window-triangular-overlap-log-edge-leakage.md
  - research/visual_exploration/findings/VIS-126-rvm-density-drift-compatible-with-log-edge-resolution.md
  - research/visual_exploration/findings/VIS-127-single-cue-circle-growing-hard-window-obstruction.md
  - research/visual_exploration/findings/VIS-128-bounded-tent-taper-composed-edge-profile.md
  - research/visual_exploration/findings/VIS-129-pair-correlation-effective-size-fixes-tent-capacity-and-resolution.md
  - research/visual_exploration/findings/VIS-130-bounded-source-taper-replaces-full-circle-cue-coordinate-window.md
  - research/visual_exploration/findings/VIS-131-bounded-taper-cue-edge-profile-poisson-sampled.md
  - research/visual_exploration/findings/VIS-132-realized-tent-diagonal-one-over-l-common-mode.md
  - research/visual_exploration/findings/VIS-133-bounded-tent-edge-amplitudes-retain-order-one-covariance.md
  - research/visual_exploration/findings/VIS-134-edge-wick-term-forces-fourth-cumulant-cancellation.md
  - research/visual_exploration/findings/VIS-135-bounded-cue-cumulants-force-gaussian-terminal-tent-packet.md
  - research/visual_exploration/findings/VIS-136-source-window-covariance-fixes-averaging-exponent.md
  - research/visual_exploration/SOURCES.md
---

# Can a Montgomery support-edge arithmetic residual beat the finite-CUE noise and finite-height transfer floor?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before inspecting fresh confirmation zeros. `VIS-123`--`VIS-131` fix the phase dictionary, Montgomery smoothing, source-window convention, capacity/effective-size controls, and the bounded-tent finite-CUE mean profile. `VIS-132` isolates the realized diagonal `1/L` fluctuation as a common mode removable exactly by samplewise subtraction or a predeclared zero-sum contrast.

`VIS-133` shows that nearby normalized terminal edge amplitudes retain an explicit strictly positive-definite covariance kernel `R_(alpha,rho)`. `VIS-134` decomposes the corresponding intensity covariance into a positive Wick kernel plus a potentially cancelling connected fourth cumulant and proves that neither zero-sum projection nor fixed Laplace smoothing removes the Wick contribution. `VIS-135` closes the remaining single-window CUE loophole: higher normalized cumulants vanish, so the terminal packet is asymptotically proper complex Gaussian and its smoothed intensity field retains the positive order-one covariance floor.

`VIS-136` now sharpens the cross-window averaging gate without assuming a zeta covariance model. For a stationary sequence of frozen per-window contrasts with covariance `gamma(h)`, the exact variance of the average is

`m^(-1)[gamma(0)+2 sum_(h<m)(1-h/m)gamma(h)]`.

Thus the familiar `Theta(L^2)` window requirement for an `O(1/L)` mean shift is valid only in the short-memory regime with strictly positive long-run variance. A positive power-law tail `gamma(h)~c h^(-beta)`, `0<beta<1`, instead requires `Theta(L^(2/beta))` windows; a persistent positive common mode prevents averaging from resolving `1/L` at all. Faster-than-quadratic information accumulation is possible only through a separately proved low-frequency cancellation such as zero long-run variance.

The unresolved question has therefore narrowed from generic **effective averaging** to the actual **low-frequency covariance law of the predeclared zeta source-window statistic**, together with finite-height zeta-to-CUE transfer at the same `1/L` scale.

## Research question

Under a predeclared family of admissible zeta height/source windows using the exact bounded-tent, effective-size, unfolding, diagonal-subtraction, edge-coordinate, and Montgomery conventions already frozen by `VIS-123`--`VIS-136`, what covariance tail or low-frequency spectral law does the frozen per-window contrast obey under the matched null?

Does that law place the statistic in the summable positive-long-run-variance regime, a power-law long-memory regime, a persistent-common-mode regime, or a genuinely degenerate zero-frequency regime with independently justified cancellation? In the surviving regime, can the available effective information make a predicted arithmetic mean displacement of order `1/L` distinguishable while finite-height counting/unfolding and effective-size transfer errors remain smaller than the same target scale?

Only after those quantities are controlled should an arithmetic lower-order formula determine a frozen residual amplitude/direction and untouched zeta confirmation data be inspected.

## Why it may matter

`VIS-136` removes an ambiguity in the previous feasibility language. Correlated windows do not have one generic "effective sample size": the covariance tail fixes the averaging exponent itself. Ordinary short memory preserves the quadratic `L^2` requirement up to a long-run-variance constant, positive long memory can make the requirement polynomially worse, and a common mode can make it impossible. Conversely, any claimed improvement over the quadratic law requires a real cancellation theorem rather than an optimistic independence or anti-correlation assumption.

The route is therefore no longer blocked by an unknown finite-CUE fourth cumulant or by a vague sample-size heuristic. Its next bottleneck is a concrete source-window covariance/low-frequency calculation for the exact zeta statistic, followed independently by a quantitative zeta-to-finite-CUE transfer estimate precise enough to make a `1/L` lower-order signal observable rather than absorbed by stochastic or finite-height uncertainty.

## Decisive test

Do not inspect untouched confirmation zeros. First freeze the source-window spacing/overlap family and derive or justify the covariance sequence, or equivalently the low-frequency spectral mass, of the exact frozen support-edge contrast under the matched null. Include overlap, separation, local unfolding, effective-size estimation, and any common counting-function component.

Classify the resulting average using the `VIS-136` regimes rather than assuming independence. If covariance is summable, establish the long-run variance and whether it is strictly positive. If a positive power-law tail is present, determine its exponent and use the corresponding `L^(2/beta)` information requirement. If a common mode survives, treat that as an averaging obstruction. If the proposed route relies on faster-than-`1/m` variance decay, prove the low-frequency cancellation that makes the long-run variance degenerate instead of inferring it from finite data.

In parallel, bound the finite-height zeta-to-CUE mismatch and nuisance propagation through the same statistic at the `1/L` scale. The test passes this gate only if the covariance-implied averaging error and transfer uncertainty can both be made smaller than a predeclared arithmetic amplitude without fitting the window selection or statistic to confirmation data.

If the required effective window count is unavailable, if long-range dependence or a common mode leaves too much noise, or if transfer/unfolding uncertainty is already `Omega(1/L)` with no independent correction, treat that as a feasibility obstruction and do not proceed to confirmation. If the gate survives, freeze an independently derived arithmetic residual prediction and only then test it on untouched high-zero material.

## Evidence boundary

`VIS-135` is a matched finite-CUE single-window result. `VIS-136` is an exact stationary-covariance feasibility reduction. Neither establishes that zeta height windows are stationary, independent, short-memory, long-memory, or described by a specific covariance law, and neither establishes finite-height transfer to `o(1/L)` or the existence of an arithmetic residual.

The `Theta(L^2)` count is now justified only conditionally on summable covariance with positive long-run variance. The alternative long-memory and common-mode rates are control regimes, not empirical claims about Riemann zeros. No fresh confirmation-zero evidence has been used.

## Research disposition

Accepted for continued investigation. The single-window CUE covariance gate is resolved through `VIS-135`, and the generic averaging ambiguity is reduced by `VIS-136`. The next material gate is to **derive the covariance tail/zero-frequency mass of the exact frozen source-window statistic and independently control finite-height zeta-to-CUE transfer at order `1/L`**. Arithmetic-amplitude fitting and untouched confirmation remain downstream.