---
id: CLUE-visual-exploration-zeta-montgomery-support-edge-arithmetic-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-122-frozen-half-arc-four-triad-panel-fails-cue-upper-tail-gate.md
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
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond a correctly windowed finite-CUE null?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before any fresh zero confirmation. `VIS-123` fixes the phase dictionary and identifies the full-circle finite-`N` CUE support-edge ripple. `VIS-124`--`VIS-130` then separate Montgomery weighting, source-window leakage, single-circle capacity, effective-size matching, and the distinction between replacing and compounding the full-circle coordinate window.

`VIS-131` derives the corrected bounded-tent **mean** edge profile. For `rho=N/L`, `kappa=M/L<rho`, and `q=1+v/L`,

`C_(N,L,M)(1+v/L) = 1 - Phi_(rho,kappa)(v)/L + O(L^-3)`,

with a Poisson-sampled profile `Phi`. Its reflected identity makes the leading rounding symmetric, and an effective-size ratio perturbation `delta rho=O(1/log L)` moves this bounded-source mean only by `O(1/(L log L))`. The earlier full-circle same-order mean ambiguity is therefore not inherited by the correctly replaced smooth bounded source window.

`VIS-132` isolates the realized diagonal fluctuation

`D_(N,M)=(3/M) sum_j h_M(y_j)^2`.

It fluctuates at order `1/L` but is a common scalar across support-edge coordinates, so samplewise diagonal subtraction or a predeclared zero-sum coordinate contrast removes it exactly.

`VIS-133` then shows that the normalized terminal edge amplitudes themselves remain strongly correlated: their covariance converges to an explicit strictly positive-definite kernel `R_(alpha,rho)(v-w)`. The Montgomery weight averages a **fixed** correlated band in the scaled edge coordinate rather than an increasing collection of decorrelated amplitudes.

`VIS-134` identifies the exact remaining fourth-order obstruction. For the centered intensity field, the covariance decomposes into the positive Wick kernel `|R(v-w)|^2`, a vanishing pseudocovariance term, and one connected fourth cumulant. The Wick kernel remains strictly positive definite after both zero-sum common-mode projection and the fixed Laplace smoothing. Therefore any self-averaging of the projected quadratic statistic must come from a specific order-one connected fourth-cumulant cancellation; it cannot be attributed merely to diagonal subtraction, coordinate contrast, or Montgomery smoothing.

The remaining CUE-side question is consequently no longer “what is the covariance?” in general. It is whether the **connected fourth cumulant of the terminal-frequency bounded-tent packet cancels the explicit Wick kernel**, partially cancels it, or leaves a positive residual quadratic form. Finite-height zeta-to-CUE transfer/unfolding uncertainty remains separate and downstream.

## Research question

For one predeclared bounded physical tent width with nonvanishing single-circle capacity margin, one effective-size rule and integerization convention, and a small frozen set of nondegenerate edge coordinates, what is the asymptotic connected fourth-cumulant kernel of the terminal-frequency bounded-tent CUE amplitudes after the exact `VIS-132` diagonal convention and `VIS-133` Montgomery/Laplace smoothing?

Does the resulting fourth-order term cancel the strictly positive Wick kernel from `VIS-134`, merely deform it, or leave a nonzero large-`L` covariance floor for every nontrivial frozen contrast? If a cancellation occurs, what exact CUE mechanism produces it and at what residual scale?

Only after that CUE-side covariance is fixed should the remaining finite-height counting/unfolding and effective-size transfer uncertainties be propagated through the same frozen contrast, followed by an independently predicted arithmetic lower-order amplitude.

## Why it may matter

A candidate arithmetic support-edge residual naturally lives at `O(1/L)`. The mean-level nuisances that once lived at that scale have been progressively removed or quantified, but a single CUE realization can still have order-one quadratic fluctuations. `VIS-134` now shows exactly what would have to happen for those fluctuations to self-average: the connected fourth cumulant must cancel an explicitly known positive Wick term.

That turns an ambiguous numerical covariance problem into a sharply falsifiable random-matrix question. If the connected cumulant fails to cancel the Wick kernel, the route requires an explicit number and independence structure of source windows large enough to resolve an `O(1/L)` mean against an order-one per-window stochastic floor. If it does cancel, the residual rate and nuisance eigendirections determine the actual confirmation budget.

Either outcome materially changes whether an arithmetic support-edge residual is measurable before any zeta data are inspected.

## Decisive test

Do not inspect fresh confirmation zeros. Keep frozen the bounded tent, effective-size rule and integerization, local unfolding convention, Montgomery weight, edge coordinates, and realized diagonal/common-mode projection.

Starting from the exact finite-`N` CUE trace/determinantal representation behind `VIS-133`, compute or asymptotically control

`cum(X(v), overline{X(v)}, X(w), overline{X(w)})`

for the nearby terminal-frequency packet `k=N+O(1)`, and then propagate that connected kernel through the fixed Laplace average. Use exact CUE cumulant, determinantal, or Weingarten machinery. Do not delete the connected term by assuming a Gaussian field: the simple high-trace cumulant-vanishing condition of Soshnikov--Wu does not apply to nearby terminal modes because their differences are `O(1)<N`.

Compare the resulting connected kernel directly against the explicit Wick kernel `|R(v-w)|^2` from `VIS-134`. Determine the limiting covariance quadratic form and its eigen-directions on the predeclared coordinate set. A bounded CUE simulation may falsify an algebraic derivation, but the durable covariance result must satisfy the normal finding gate.

If the full projected covariance has a nonzero limit, derive the averaging requirement under an explicit independence/correlation model for source windows; do not infer independence from visual or height separation. If it decays, derive the rate. Only then propagate finite-height zeta-to-CUE transfer and unfolding/counting uncertainty through the same statistic, freeze an arithmetic lower-order prediction, and use untouched zeta confirmation data.

Kill the route if the fully matched finite-CUE/taper fourth-order null absorbs the proposed residual, transfer uncertainty dominates it, or the purported arithmetic term reduces entirely to already-accounted lower-order structure with no residual question.

## Evidence boundary

The CUE determinantal kernel, trace covariance, moment-cumulant identities, high-trace cumulant methods, Montgomery's pair statistic and weight, finite-size CUE models for Riemann zeros, and ordinary Fourier/window identities are prior art.

`VIS-123`--`VIS-132` establish calibration, source-window, effective-size, mean-profile, and realized-diagonal controls. `VIS-133` establishes the explicit nonvanishing second-order terminal edge-amplitude covariance and fixed-width Laplace representation. `VIS-134` establishes only the exact decomposition of intensity covariance into a strictly positive Wick contribution plus the still-unknown connected fourth cumulant, together with the fact that zero-sum projection and fixed Laplace smoothing do not erase that Wick contribution.

Neither `VIS-133` nor `VIS-134` proves a positive variance floor for the complete quadratic statistic, because an order-one connected fourth-cumulant cancellation remains possible. No exact finite-height zeta-to-CUE transfer, stochastic counting-function covariance, arithmetic lower-order amplitude, or fresh zero confirmation has yet been supplied. Even a later positive test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new general random-matrix theorem.

## Research disposition

Accepted for continued investigation. The CUE-side covariance gate is narrowed to the **connected fourth-cumulant kernel of the terminal bounded-tent packet after the fixed Laplace average**. The next material result should decide whether that term cancels the explicit Wick kernel from `VIS-134`; only after that should source-window averaging requirements, finite-height transfer, and untouched zeta confirmation be addressed.
