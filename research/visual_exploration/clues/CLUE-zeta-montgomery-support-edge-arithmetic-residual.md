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
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond a correctly windowed finite-CUE null?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before any fresh zero confirmation. `VIS-123` fixes the phase dictionary and shows that the all-real-time full-circle finite-`N` CUE statistic has a logarithmic support-edge ripple. `VIS-124` identifies Montgomery's pair weight as an exact Laplace multiplier/convolution. `VIS-125`--`VIS-128` isolate source-window leakage, rule out a growing hard window inside one logarithmic-size CUE circle, and replace it by an explicit bounded tent taper whose pair-overlap kernel is known exactly. `VIS-129` supplies the classical pair-correlation effective-size candidate `N_e(T)=rho_* L_T`, with `rho_*=1/sqrt(12 Lambda)=0.230156986...`, so a single non-wrapping tent arc must satisfy `H_src<2*pi*rho_*=1.44611899...`.

`VIS-130` corrects the remaining finite-`N` transfer. The continuous full-circle quantity `S_N(Nq)/N` is already the Fourier transform of a connected CUE pair kernel multiplied by the rectangular coordinate-overlap factor `R_N(x)=(1-|x|/N)_+`. Convolving that already-windowed object with the tent kernel would multiply the pair measure by both `R_N` and the tent overlap, thereby compounding two source-coordinate windows. For a bounded tent that is meant to replace the full-circle source window, the exact connected finite-CUE expectation is instead

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 exp(2*pi*i*q*x) dx`,

with `D_N(x)=sin(pi x)/(N sin(pi x/N))`, `W_L(x)=1/(1+(pi*x/L)^2)`, and `A_M` the exact compact cubic tent-overlap profile from `VIS-130`.

The residual question is therefore narrower and cleaner. Before source confirmation, the exact bounded-arc null itself must be analyzed near the Montgomery support edge, including its finite-`N` asymptotic, effective-size sensitivity, diagonal convention, and joint covariance. The full-circle `VIS-123` logarithmic ripple and the `VIS-129` `delta_rho=Theta(1/log L_T)` calibration threshold remain valid for that full-circle statistic, but they cannot simply be transplanted to the bounded-tent null without re-deriving the dependence from `C_(N,L,M)`.

## Research question

For the predeclared effective-size rule `N=N_e(T)` and a bounded physical tent width `H_src<1.44611899...` with nonvanishing capacity margin, what is the exact and asymptotic support-edge behavior of `C_(N,L_T,M)` when `M=H_src L_T/(2*pi)` and `q=1+v/L_T` at several fixed nondegenerate coordinates `v`?

Can its joint covariance and sensitivity to theoretically admissible perturbations of `N(T)` be derived strongly enough that a later `1/L_T`, `log log T/log T`, or other proposed arithmetic residual cannot be mimicked by universal finite-CUE geometry, the source taper, Montgomery weighting, or effective-size uncertainty?

## Why it may matter

The previous convolutional formulation risked manufacturing a false finite-size correction by applying a bounded source window on top of the rectangular coordinate window already implicit in the noninteger-time full-circle CUE transform. `VIS-130` removes that ambiguity at the measure level and gives a direct exact finite-`N` object whose source geometry matches the intended bounded taper.

This is useful even if the route ultimately fails. If the exact bounded-arc null absorbs the apparent edge structure, the support edge becomes a closed visual control rather than an arithmetic carrier. If a residual survives only after all source/null choices are fixed independently of the zero data, its interpretation is substantially cleaner, although it would still need an independently derived arithmetic amplitude and fresh confirmation before carrying mathematical weight.

## Decisive test

Do not inspect fresh confirmation zeros. Freeze one bounded physical tent width strictly below the `VIS-129` capacity ceiling, the effective-size rule and integerization convention, the local unfolding, Montgomery weight, diagonal/connected normalization, a small set of nondegenerate edge coordinates `v`, and the combined decision statistic.

Use the exact `VIS-130` integral as the null, not `P_L*Q_M^tent*[S_N(N·)/N]`. First verify internal consistency by recovering the full-circle all-real-time `S_N(Nq)/N` when `A_M` is replaced by the exact full-circle overlap `R_N` and `W_L=1`. Then derive or tightly control the large-`L_T` fixed-ratio support-edge expansion of the bounded-tent integral and the joint covariance at the frozen coordinates.

Recompute the effective-size sensitivity for this actual source-window representation. Propagate any unresolved transfer uncertainty in `N(T)` into the null/covariance rather than fitting `rho` to a residual. Kill a same-scale arithmetic interpretation if admissible effective-size variation, exact arc/window geometry, diagonal treatment, or the complete finite-CUE covariance can reproduce the candidate effect. Only after this null is frozen and its nuisance directions are controlled should an arithmetic lower-order formula set the expected residual scale and untouched zero material be examined.

## Evidence boundary

The CUE determinantal kernel, the all-real-time full-circle spectral form factor, Montgomery's pair statistic and weight, finite-size CUE models for Riemann zeros, and ordinary window/autocorrelation Fourier identities are prior art. `VIS-123`--`VIS-130` establish a sequence of calibration and compatibility controls plus the exact bounded-tent finite-CUE expectation under one coordinate convention; they do not establish any arithmetic residual.

In particular, `VIS-130` does not prove the bounded-arc support-edge asymptotic, its covariance, or the precision with which the pair-correlation effective size transfers to this observable. It also does not prove that the full-circle logarithmic ripple disappears; it proves only that the bounded-source null must be derived from the correctly replaced source window rather than by automatically multiplying the already-windowed full-circle statistic by another window factor.

No fresh zero confirmation has been inspected for this narrowed design. Even a positive later test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new random-matrix theorem.

## Research disposition

Accepted for continued investigation in corrected form. The next unresolved step is the **exact bounded-tent finite-CUE support-edge asymptotic, covariance, and effective-size sensitivity derived from `C_(N,L,M)`**, all frozen before fresh source inspection. The earlier full-circle convolution `P_L*Q_M^tent*K_N` is no longer treated as the exact bounded-source null unless an additional argument proves that its built-in rectangular overlap is intended or asymptotically negligible.