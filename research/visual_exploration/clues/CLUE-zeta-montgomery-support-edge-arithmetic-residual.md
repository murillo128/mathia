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
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond a correctly windowed finite-CUE null?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before any fresh zero confirmation. `VIS-123` fixes the phase dictionary and identifies the full-circle finite-`N` CUE support-edge ripple. `VIS-124`--`VIS-130` then separate Montgomery weighting, source-window leakage, single-circle capacity, effective-size matching, and the distinction between replacing and compounding the full-circle coordinate window.

`VIS-131` derives the corrected bounded-tent **mean** edge profile. For `rho=N/L`, `kappa=M/L<rho`, and `q=1+v/L`,

`C_(N,L,M)(1+v/L) = 1 - Phi_(rho,kappa)(v)/L + O(L^-3)`

with a Poisson-sampled profile `Phi`. Its reflected identity makes the leading rounding symmetric, and an effective-size ratio perturbation `delta rho=O(1/log L)` moves this bounded-source mean only by `O(1/(L log L))`. The earlier full-circle same-order mean ambiguity is therefore not inherited by the correctly replaced smooth bounded source window.

`VIS-132` now resolves one piece of the stochastic covariance convention. The deterministic diagonal mean `1` in `C_(N,L,M)` corresponds in a single CUE realization to

`D_(N,M)=(3/M) sum_j h_M(y_j)^2`.

For fixed source ratio `M/N=alpha in (0,1)`, exact CUE trace covariance gives `Var(D_(N,M))=Theta(N^-2)`, and the CUE linear-statistic CLT makes `N(D_(N,M)-1)` asymptotically nondegenerate Gaussian. Thus in the support-edge scaling `N=Theta(L)` the **realized diagonal itself fluctuates at order `1/L`**. It is the same scalar at every edge coordinate, however: samplewise realized-diagonal subtraction or any zero-sum coordinate contrast removes it exactly. Subtracting only the ensemble mean `1` does not.

The remaining residual question is consequently narrower. The bounded-tent mean null, first-order effective-size sensitivity, and realized diagonal common mode are controlled. The unresolved stochastic object is the **off-diagonal joint covariance after that exact common-mode projection**, together with finite-height zeta-to-CUE transfer/unfolding errors and any independently predicted arithmetic lower-order amplitude.

## Research question

For one predeclared bounded physical tent width with nonvanishing single-circle capacity margin, one effective-size rule and integerization convention, and a small frozen set of nondegenerate edge coordinates `v`, what is the exact or asymptotically controlled joint covariance of the **samplewise diagonal-subtracted off-diagonal** finite-CUE statistics after the `VIS-131` mean profile is removed?

Does that covariance have a nonzero large-`L` floor, decay like a power of `L`, or contain a lower-rank nuisance geometry that can itself be projected out without fitting to zeta data? How do the remaining finite-height counting/unfolding and effective-size transfer uncertainties propagate through the same frozen contrast?

## Why it may matter

A candidate arithmetic edge residual naturally lives at `O(1/L)`. `VIS-131` shows that the bounded-tent **mean** can be calibrated at that scale without the earlier logarithmically amplified effective-size ambiguity. `VIS-132` shows that a careless diagonal convention can nevertheless inject a stochastic `O(1/L)` common mode of exactly the same size.

That nuisance is removable without source fitting, so it is not a reason to abandon the route. The decisive issue is now the off-diagonal stochastic floor. Ordinary full-circle random-matrix spectral form factors are known to be non-self-averaging, so it would be unsafe to assume that the bounded-taper covariance shrinks merely because its mean has a `1/L` expansion. If the projected covariance stays `O(1)`, resolving an `O(1/L)` mean signal requires an explicit averaging budget over effectively independent source windows; if it decays, the rate determines how much confirmation data are needed.

## Decisive test

Do not inspect fresh confirmation zeros. Freeze the bounded tent width, effective-size rule and integerization, local unfolding, Montgomery weight, edge coordinates, and one combined decision statistic. Fix the diagonal convention **at the realized-statistic level**: either subtract `D_(N,M)` samplewise or use a predeclared zero-sum coordinate contrast so that the common mode from `VIS-132` cancels identically.

Starting from the exact `VIS-130` finite-CUE source-window statistic and `VIS-131` mean profile, derive the covariance matrix of the remaining off-diagonal coordinates under the same finite-`N` CUE/tent/weight convention. Do not import full-circle SFF covariance. Determine its large-`L` scale, eigen-directions, and any exact symmetry-induced degeneracies. A bounded CUE simulation may be used as a falsification/control check, but the durable covariance claim must be derived or otherwise justified under the normal finding gate.

Then propagate the finite-height source-transfer uncertainties through that **same projected joint statistic**: residual admissible error in `N(T)`, smooth and stochastic unfolding/counting effects, and the exact connected/diagonal normalization. If the projected covariance has a nonzero limit, predeclare the number and independence structure of height windows needed to make the standard error smaller than the target `1/L` amplitude; do not infer independence from visual separation alone.

Only after the complete projected mean-plus-covariance null and nuisance directions are frozen should an arithmetic lower-order formula determine the predicted residual amplitude and direction. Then test the frozen statistic on untouched high-zero material with the predetermined combined decision rule. Kill the route if the residual is reproduced by the matched finite-CUE/taper null, absorbed by justified transfer uncertainty, disappears under exact normalization/unfolding accounting, or reduces entirely to established lower-order arithmetic with no residual question.

## Evidence boundary

The CUE determinantal kernel, Fejer expansion, Poisson summation, Montgomery's pair statistic and weight, finite-size CUE models for Riemann zeros, CUE trace covariance/linear-statistic CLTs, and ordinary window/autocorrelation Fourier identities are prior art. `VIS-123`--`VIS-132` establish calibration and compatibility controls plus the corrected bounded-tent mean null, its leading support-edge profile, and the exact scale/cancellation of the realized diagonal common mode. They do not establish an arithmetic residual.

`VIS-132` does **not** determine the total bounded-tent covariance. In particular, the off-diagonal quadratic statistic can fluctuate more strongly and can correlate with the diagonal component. The known non-self-averaging of the ordinary full-circle SFF is only a warning against assuming self-averaging here, not a theorem about the bounded-taper statistic.

No exact finite-height zeta-to-CUE transfer, stochastic counting-function covariance, arithmetic lower-order amplitude, or fresh zero confirmation has yet been supplied. Even a later positive test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new random-matrix theorem.

## Research disposition

Accepted for continued investigation. `VIS-131` resolves the bounded-tent mean support-edge asymptotic and first-order effective-size sensitivity; `VIS-132` resolves the realized diagonal common-mode piece of the covariance convention and shows how to remove it exactly. The remaining gate is the **off-diagonal projected finite-CUE covariance plus finite-height transfer/nuisance propagation**, followed — only if that survives — by an independently predicted arithmetic amplitude and untouched source confirmation.