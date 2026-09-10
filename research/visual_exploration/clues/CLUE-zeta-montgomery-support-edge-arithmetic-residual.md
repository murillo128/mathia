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
  - research/visual_exploration/findings/VIS-139-disjoint-pair-stat-covariance-requires-four-level-information.md
  - research/visual_exploration/SOURCES.md
---

# Can a Montgomery support-edge arithmetic residual beat the finite-CUE noise and finite-height transfer floor?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before inspecting fresh confirmation zeros. `VIS-123`--`VIS-131` fix the phase dictionary, Montgomery smoothing, source-window convention, capacity/effective-size controls, and the bounded-tent finite-CUE mean profile. `VIS-132` isolates the realized diagonal `1/L` fluctuation as a common mode removable exactly by samplewise subtraction or a predeclared zero-sum contrast.

`VIS-133` shows that nearby normalized terminal edge amplitudes retain an explicit strictly positive-definite covariance kernel `R_(alpha,rho)`. `VIS-134` decomposes the corresponding intensity covariance into a positive Wick kernel plus a potentially cancelling connected fourth cumulant and proves that neither zero-sum projection nor fixed Laplace smoothing removes the Wick contribution. `VIS-135` closes the remaining single-window CUE loophole: higher normalized cumulants vanish, so the terminal packet is asymptotically proper complex Gaussian and its smoothed intensity field retains the positive order-one covariance floor.

`VIS-136` sharpens the averaging gate. For a stationary sequence of frozen per-window contrasts with covariance `gamma(h)`, the exact variance of the average is `m^(-1)[gamma(0)+2 sum_(h<m)(1-h/m)gamma(h)]`. Thus the covariance tail fixes the information exponent: short memory with positive long-run variance gives the familiar quadratic `Theta(L^2)` requirement for an `O(1/L)` mean shift, positive long memory is worse, a persistent common mode blocks averaging, and faster decay requires separately proved low-frequency cancellation.

`VIS-137` closes the within-circle translation loophole. Translating the same fixed-ratio tent around one CUE matrix gives a leading cross-window covariance equal to the Fourier transform of the actual overlap of the two source tents; pairwise-disjoint tents decorrelate at leading order. But each tent occupies a fixed angular fraction `alpha`, so at most `floor(1/alpha)` pairwise-disjoint supports fit on one circle. A single finite-CUE realization therefore cannot manufacture the required `m -> infinity` source-window pool merely by taking more translated windows.

`VIS-138` closes a stronger marginal-calibration loophole. A stationary refresh chain can have **exact CUE(N) marginal law in every source window** while its centered contrast has covariance `q^h sigma_N^2`. For fixed `q<1` it is reversible and geometrically mixing, yet the long-run variance is inflated by `(1+q)/(1-q)`; if `1-q_L` shrinks like `L^-alpha`, the window requirement for a `1/L` signal grows from `L^2` to `L^(2+alpha)`. At `q=1` averaging fails completely. Thus exact one-window CUE means, cumulants, and edge covariances do not identify the cross-height averaging law, and even pointwise-in-`L` mixing is insufficient without a uniform dependence bound.

`VIS-139` now identifies the correlation order that the disjoint-window version of this gate actually consumes. For quadratic pair statistics supported on disjoint source windows, the exact covariance is a four-level factorial-moment functional `alpha^(4)-alpha^(2) tensor alpha^(2)`; the shared-point second- and third-level contractions vanish. An explicit four-site even-parity process matches independent Bernoulli occupancy through every one-, two-, and three-site inclusion marginal yet changes the covariance of two disjoint pair indicators from `0` to `1/16`. Therefore Montgomery-style two-level pair correlation, even supplemented by arbitrary exact three-level marginals, cannot determine the needed disjoint-window covariance without additional structure.

## Research question

For a predeclared sequence of actual zeta height windows using the exact bounded-tent, effective-size, unfolding, diagonal-subtraction, edge-coordinate, and Montgomery conventions frozen by `VIS-123`--`VIS-139`, what covariance tail or low-frequency spectral law does the resulting per-window contrast obey?

For disjoint source windows, can the required four-level cross-height functional be controlled uniformly in `L` for the exact frozen pair kernel? Alternatively, is there a rigorous structural closure in the relevant regime that reduces the four-level term to lower-order data, or a direct covariance/mixing theorem that bypasses the factorial-moment expansion? For overlapping windows, can the additional second- and third-level contraction terms also be controlled at the shrinking `1/L` signal scale?

Only after that dependence law and the finite-height transfer error are controlled should an arithmetic lower-order formula determine a frozen residual amplitude/direction and untouched zeta confirmation data be inspected.

## Why it may matter

The current CUE null is well constrained at the single-window level: its mean, common diagonal mode, terminal amplitude covariance, fourth-cumulant behavior, and fixed smoothing are all explicit. `VIS-136` shows that source-window dependence can change the asymptotic sample requirement itself, `VIS-137` shows that a finite CUE circle cannot supply a growing independent sample merely by translation, and `VIS-138` shows that **no amount of single-window marginal calibration can repair the missing cross-window coupling law**.

`VIS-139` makes the missing information more concrete. Because the frozen support-edge observable is quadratic in the local point configuration, the covariance between disjoint source windows lives at the four-level correlation layer. This rules out an otherwise tempting shortcut: calibrating only against Montgomery pair correlation and then assuming that the source-window averaging law follows. The next progress must either reach the relevant four-level information with uniform quantitative control, prove a valid closure mechanism, or establish the covariance directly.

## Decisive test

Do not inspect untouched confirmation zeros. First freeze a sequence of zeta source-window centers, widths, overlaps/separations, local unfolding rule, and effective-size rule. For disjoint windows, write the exact order-two pair kernel of the frozen support-edge contrast and reduce its cross-window covariance to the corresponding four-level factorial-moment integral from `VIS-139`. Then obtain a bound or asymptotic for that integral that is uniform in the same `L`-dependent family needed by the experiment.

A lower-order shortcut is admissible only with a proved structural closure: for example, an appropriate determinantal/Gaussian/Wick-type joint law that genuinely determines the needed four-level term in the relevant finite-height regime. Pair correlation by itself is not such a closure. If a direct mixing/covariance theorem is used instead, it must bound the same frozen statistic rather than a neighboring observable.

For overlapping source windows, retain and control the explicit second- and third-order shared-point contractions rather than importing the disjoint-window formula. If a multi-CUE surrogate is used, specify its **joint** law across blocks. Independent CUE blocks are only one admissible coupling; `VIS-138` gives equally exact CUE-marginal geometrically mixing couplings with arbitrarily degrading long-run variance.

Classify the resulting average using the `VIS-136` regimes. If covariance is summable, establish the long-run variance and whether it is strictly positive. If a Markov/spectral-gap surrogate is invoked, quantify the gap uniformly in `L`; a gap of order `L^-alpha` already permits an `L^(2+alpha)` source-window requirement by `VIS-138`. If a positive power-law tail is present, determine its exponent. If a common mode survives, treat that as an averaging obstruction. If faster-than-`1/m` variance decay is claimed, prove the low-frequency cancellation that makes the long-run variance degenerate instead of inferring it from finite data.

Independently bound the finite-height zeta-to-null mismatch and nuisance propagation through the same statistic at order `1/L`. The gate passes only if covariance-implied averaging error and transfer uncertainty can both be made smaller than a predeclared arithmetic amplitude without fitting window selection, effective size, or statistic to confirmation data.

## Evidence boundary

`VIS-135` is a matched finite-CUE single-window result. `VIS-136` is an exact stationary-covariance feasibility reduction. `VIS-137` gives translated-window covariance geometry and a fixed-ratio packing obstruction within one CUE realization. `VIS-138` gives an exact matched-marginal family proving that one-window CUE laws, and even nonuniform geometric mixing at each fixed `L`, do not determine the source-window averaging exponent. `VIS-139` is an exact generic point-process identifiability result showing that disjoint quadratic pair-statistic covariance requires four-level information absent from lower-order marginals.

None of these results establishes the four-level correlation law of actual zeta height windows, stationarity or mixing of that sequence, a cross-height finite-CUE transfer theorem, a uniform spectral gap, or the existence of an arithmetic residual. `VIS-139` also does not show that four-level data must be supplied independently when a valid structural closure theorem is available. The `Theta(L^2)` count remains conditional on summable covariance with uniformly controlled positive long-run variance. No fresh confirmation-zero evidence has been used.

## Research disposition

Accepted for continued investigation. The next material gate is now sharper: **control the four-level cross-height functional of the exact frozen disjoint-window zeta pair statistic uniformly in `L`, prove a structural closure that supplies that control from lower-order data, or bypass it with a direct covariance/mixing theorem; then independently control finite-height transfer at order `1/L`**. Two-level Montgomery calibration alone is insufficient by `VIS-139`, and arithmetic-amplitude fitting plus untouched confirmation remain downstream.