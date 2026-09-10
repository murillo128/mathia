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
  - research/visual_exploration/SOURCES.md
---

# Can a Montgomery support-edge arithmetic residual beat the finite-CUE noise and finite-height transfer floor?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before inspecting fresh confirmation zeros. `VIS-123`--`VIS-131` fix the phase dictionary, Montgomery smoothing, source-window convention, capacity/effective-size controls, and the bounded-tent finite-CUE mean profile. `VIS-132` isolates the realized diagonal `1/L` fluctuation as a common mode removable exactly by samplewise subtraction or a predeclared zero-sum contrast.

`VIS-133` shows that nearby normalized terminal edge amplitudes retain an explicit strictly positive-definite covariance kernel `R_(alpha,rho)`. `VIS-134` decomposes the corresponding intensity covariance into a positive Wick kernel plus a potentially cancelling connected fourth cumulant and proves that neither zero-sum projection nor fixed Laplace smoothing removes the Wick contribution.

`VIS-135` closes that remaining CUE-side loophole. The rank-`N` projection determinantal cumulant formula gives `O(N)` fixed-order cumulants for uniformly bounded CUE linear statistics. Since the terminal tent amplitudes are bounded test-function statistics normalized by `sqrt(H_2)=Theta(sqrt(N))`, every joint cumulant of order `p>=3` is `O(N^(1-p/2))`. The connected fourth cumulant is therefore `O(1/N)` and cannot cancel the order-one Wick term. The fixed-dimensional terminal packet is asymptotically proper complex Gaussian, and the smoothed intensity field retains the strictly positive-definite covariance kernel `G_(alpha,rho)`.

Thus a single matched finite-CUE source window has an order-one stochastic floor after all currently frozen mean, diagonal, coordinate, taper, and Montgomery controls. The unresolved question has moved from **single-window CUE covariance** to **effective averaging and finite-height transfer at the proposed arithmetic `1/L` scale**.

## Research question

Under a predeclared family of admissible zeta height/source windows using the exact bounded-tent, effective-size, unfolding, diagonal-subtraction, edge-coordinate, and Montgomery conventions already frozen by `VIS-123`--`VIS-135`, what is the effective covariance between windows and how accurately does the finite-CUE null transfer at order `1/L`?

Can one obtain enough effectively independent information that a predicted arithmetic mean displacement of order `1/L` is distinguishable from the positive single-window CUE variance floor, while keeping finite-height counting/unfolding and effective-size transfer errors smaller than the same target scale?

Only after those quantities are controlled should an arithmetic lower-order formula determine a frozen residual amplitude/direction and untouched zeta confirmation data be inspected.

## Why it may matter

`VIS-135` changes the feasibility calculation qualitatively. Under genuinely independent matched windows, a fixed nonzero contrast with order-one limiting variance needs `Theta(L^2)` effective windows for fixed signal-to-noise against an `O(1/L)` mean shift, and more than `L^2` for the stochastic error to be asymptotically smaller than the signal. Correlation between height windows can only make the effective-sample calculation more demanding unless it supplies some separately justified cancellation structure.

The route is therefore not blocked by an unknown CUE fourth cumulant anymore. Its next bottleneck is whether the Riemann-zero data admit a defensible source-window ensemble and a quantitative zeta-to-finite-CUE transfer precise enough to make the proposed arithmetic lower-order signal observable rather than absorbed by stochastic or finite-height uncertainty.

## Decisive test

Do not inspect untouched confirmation zeros. First freeze a source-window family and derive or justify its cross-window covariance under the matched null, including overlap, separation, local unfolding, effective-size estimation, and any common counting-function component. Convert that covariance into an effective sample size for the exact frozen support-edge contrast.

In parallel, bound the finite-height zeta-to-CUE mismatch and nuisance propagation through the same statistic at the `1/L` scale. The test passes this gate only if the effective averaging error and transfer uncertainty can both be made smaller than a predeclared arithmetic amplitude without fitting the window selection or statistic to confirmation data.

If the effective window count grows too slowly relative to `L^2`, if long-range dependence leaves an order-one averaged floor, or if transfer/unfolding uncertainty is already `Omega(1/L)` with no independent correction, treat that as a feasibility obstruction and do not proceed to confirmation. If the gate survives, freeze an independently derived arithmetic residual prediction and only then test it on untouched high-zero material.

## Evidence boundary

`VIS-135` is a matched finite-CUE result. It establishes the asymptotic Gaussianity of the bounded terminal amplitude packet at fixed scaled coordinates and the resulting positive covariance floor for fixed finite intensity contrasts, including after the frozen Laplace smoothing. It does **not** establish that zeta height windows are independent, that finite-height zeros follow this null to `o(1/L)`, or that an arithmetic residual exists.

The `Theta(L^2)` window count is an independence-model scaling consequence of an order-one per-window variance versus an `O(1/L)` mean target, not an empirical statement about available zeta data. No fresh confirmation-zero evidence has been used.

## Research disposition

Accepted for continued investigation. The single-window CUE fourth-cumulant gate is resolved by `VIS-135`; the next material gate is the **effective source-window covariance/sample size together with finite-height zeta-to-CUE transfer at order `1/L`**. Arithmetic-amplitude fitting and untouched confirmation remain downstream.