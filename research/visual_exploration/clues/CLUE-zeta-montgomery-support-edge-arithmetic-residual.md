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
  - research/visual_exploration/findings/VIS-137-fixed-ratio-cue-translated-windows-do-not-provide-growing-independent-pool.md
  - research/visual_exploration/findings/VIS-138-exact-cue-marginals-do-not-determine-cross-window-averaging.md
  - research/visual_exploration/SOURCES.md
---

# Can a Montgomery support-edge arithmetic residual beat the finite-CUE noise and finite-height transfer floor?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before inspecting fresh confirmation zeros. `VIS-123`--`VIS-131` fix the phase dictionary, Montgomery smoothing, source-window convention, capacity/effective-size controls, and the bounded-tent finite-CUE mean profile. `VIS-132` isolates the realized diagonal `1/L` fluctuation as a common mode removable exactly by samplewise subtraction or a predeclared zero-sum contrast.

`VIS-133` shows that nearby normalized terminal edge amplitudes retain an explicit strictly positive-definite covariance kernel `R_(alpha,rho)`. `VIS-134` decomposes the corresponding intensity covariance into a positive Wick kernel plus a potentially cancelling connected fourth cumulant and proves that neither zero-sum projection nor fixed Laplace smoothing removes the Wick contribution. `VIS-135` closes the remaining single-window CUE loophole: higher normalized cumulants vanish, so the terminal packet is asymptotically proper complex Gaussian and its smoothed intensity field retains the positive order-one covariance floor.

`VIS-136` sharpens the averaging gate. For a stationary sequence of frozen per-window contrasts with covariance `gamma(h)`, the exact variance of the average is

`m^(-1)[gamma(0)+2 sum_(h<m)(1-h/m)gamma(h)]`.

Thus the covariance tail fixes the information exponent: short memory with positive long-run variance gives the familiar quadratic `Theta(L^2)` requirement for an `O(1/L)` mean shift, positive long memory is worse, a persistent common mode blocks averaging, and faster decay requires separately proved low-frequency cancellation.

`VIS-137` closes the within-circle translation loophole. Translating the same fixed-ratio tent around one CUE matrix gives a leading cross-window covariance equal to the Fourier transform of the actual overlap of the two source tents; pairwise-disjoint tents decorrelate at leading order. But each tent occupies a fixed angular fraction `alpha`, so at most `floor(1/alpha)` pairwise-disjoint supports fit on one circle. A single finite-CUE realization therefore cannot manufacture the required `m -> infinity` source-window pool merely by taking more translated windows.

`VIS-138` now closes a stronger marginal-calibration loophole. A stationary refresh chain can have **exact CUE(N) marginal law in every source window** while its centered contrast has covariance `q^h sigma_N^2`. For fixed `q<1` it is reversible and geometrically mixing, yet the long-run variance is inflated by `(1+q)/(1-q)`; if `1-q_L` shrinks like `L^-alpha`, the window requirement for a `1/L` signal grows from `L^2` to `L^(2+alpha)`. At `q=1` averaging fails completely. Thus exact one-window CUE means, cumulants, and edge covariances do not identify the cross-height averaging law, and even pointwise-in-`L` mixing is insufficient without a uniform dependence bound.

## Research question

For a predeclared sequence of actual zeta height windows using the exact bounded-tent, effective-size, unfolding, diagonal-subtraction, edge-coordinate, and Montgomery conventions frozen by `VIS-123`--`VIS-138`, what covariance tail or low-frequency spectral law does the resulting per-window contrast obey?

Can that law be justified directly for the zeta sequence, or through a multi-block/random-matrix surrogate with an explicit joint coupling/separation rule and a **uniform-in-`L`** dependence estimate accurate at the shrinking `1/L` signal scale? Does it place the statistic in the summable positive-long-run-variance regime, a power-law long-memory regime, a persistent-common-mode regime, or a genuinely degenerate zero-frequency regime with independently justified cancellation?

Only after that dependence law and the finite-height transfer error are controlled should an arithmetic lower-order formula determine a frozen residual amplitude/direction and untouched zeta confirmation data be inspected.

## Why it may matter

The current CUE null is now well constrained at the single-window level: its mean, common diagonal mode, terminal amplitude covariance, fourth-cumulant behavior, and fixed smoothing are all explicit. `VIS-136` shows that source-window dependence can change the asymptotic sample requirement itself, `VIS-137` shows that a finite CUE circle cannot supply a growing independent sample merely by translation, and `VIS-138` shows that **no amount of single-window marginal calibration can repair the missing cross-window coupling law**.

This removes two easy but invalid routes to optimistic effective sample size: translating one fixed-ratio CUE realization, and sampling independent CUE matrices then treating their imposed independence as evidence about separated zeta heights. The next progress must therefore come from a genuine cross-height covariance/mixing theorem or model with uniform quantitative control, or from a decisive obstruction showing that the available information cannot resolve the `1/L` scale.

## Decisive test

Do not inspect untouched confirmation zeros. First freeze a sequence of zeta source-window centers, widths, overlaps/separations, local unfolding rule, and effective-size rule. Derive or justify the covariance sequence, or equivalently the low-frequency spectral mass, of the exact frozen support-edge contrast across those windows. Account explicitly for shared zeros from overlap, counting-function components, local unfolding/effective-size estimation, and any dependence introduced by the centering procedure.

Do not use translated windows from a single fixed-ratio CUE matrix as an asymptotically growing independent calibration pool: `VIS-137` proves that only `O(1)` pairwise-disjoint fixed-ratio tents fit. If a multi-CUE surrogate is used, specify its **joint** law across blocks. Independent CUE blocks are only one admissible coupling; `VIS-138` gives equally exact CUE-marginal geometrically mixing couplings with arbitrarily degrading long-run variance. Any claimed zeta approximation must therefore control the cross-block/cross-height dependence uniformly in the same `L`-asymptotic regime, not only reproduce each block marginal.

Classify the resulting average using the `VIS-136` regimes. If covariance is summable, establish the long-run variance and whether it is strictly positive. If a Markov/spectral-gap surrogate is invoked, quantify the gap uniformly in `L`; a gap of order `L^-alpha` already permits an `L^(2+alpha)` source-window requirement by `VIS-138`. If a positive power-law tail is present, determine its exponent. If a common mode survives, treat that as an averaging obstruction. If faster-than-`1/m` variance decay is claimed, prove the low-frequency cancellation that makes the long-run variance degenerate instead of inferring it from finite data.

Independently bound the finite-height zeta-to-null mismatch and nuisance propagation through the same statistic at order `1/L`. The gate passes only if covariance-implied averaging error and transfer uncertainty can both be made smaller than a predeclared arithmetic amplitude without fitting window selection, effective size, or statistic to confirmation data.

## Evidence boundary

`VIS-135` is a matched finite-CUE single-window result. `VIS-136` is an exact stationary-covariance feasibility reduction. `VIS-137` gives translated-window covariance geometry and a fixed-ratio packing obstruction within one CUE realization. `VIS-138` gives an exact matched-marginal family proving that one-window CUE laws, and even nonuniform geometric mixing at each fixed `L`, do not determine the source-window averaging exponent.

None of these results establishes the covariance law of actual zeta height windows, stationarity or mixing of that sequence, a cross-height finite-CUE transfer theorem, a uniform spectral gap, or the existence of an arithmetic residual. The `Theta(L^2)` count remains conditional on summable covariance with uniformly controlled positive long-run variance. No fresh confirmation-zero evidence has been used.

## Research disposition

Accepted for continued investigation. Single-window finite-CUE calibration, within-circle translation, and marginally exact multi-window CUE surrogates are now insufficient by explicit controls. The next material gate is to **derive or justify the joint cross-height covariance/zero-frequency law of the exact frozen zeta source-window statistic with uniform-in-`L` dependence control, and independently control finite-height transfer at order `1/L`**. Arithmetic-amplitude fitting and untouched confirmation remain downstream.