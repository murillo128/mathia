---
id: CLUE-visual-exploration-zeta-montgomery-support-edge-arithmetic-residual
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-019-raw-adjacent-gap-geometry-finite-size-rmt-baseline.md
  - research/visual_exploration/findings/VIS-122-frozen-half-arc-four-triad-panel-fails-cue-upper-tail-gate.md
  - research/visual_exploration/findings/VIS-123-montgomery-cue-edge-ramp-null-logarithmic-ripple.md
  - research/visual_exploration/findings/VIS-124-montgomery-weight-laplace-smooths-cue-edge.md
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond finite CUE?

## Observation

`VIS-122` closes the frozen half-arc third-order confirmation route and requires any new zero-configuration thread to begin from an independent mathematical carrier. Montgomery's weighted pair-correlation transform supplies such a carrier, but the visually obvious support edge is shared by the CUE/GUE null and therefore cannot itself count as arithmetic structure.

Two calibration layers are now exact. `VIS-123` matches the Montgomery Fourier phase to full-circle CUE under the local unfolding `L_T=log(T/(2*pi))`: the finite-height edge is centered by

`v=(alpha-1)log(T)+log(2*pi)`,

with `k-N=(N/L_T)v`. It also shows from the exact all-real-time finite-`N` CUE form factor that a continuous ramp-centered edge contains a universal logarithmic finite-size ripple.

`VIS-124` fixes the pair-weight layer. In unfolded difference coordinates Montgomery's weight becomes

`W_L(x)=1/(1+(pi*x/L)^2)`,

whose Fourier transform is the unit-mass Laplace kernel

`P_L(r)=L exp(-2L|r|)`.

Thus the full-circle weight-matched CUE null is not the pointwise real-time form factor but its exact convolution `P_L*K_N`. Even the infinite-CUE ramp acquires the universal centered residual

`-(1/(4L_T)) exp(-2|v|)`

at leading edge scale. A ramp subtraction, or an unweighted finite-CUE subtraction, therefore leaves a deterministic non-arithmetic bump.

The remaining candidate is narrower: after the phase centering, finite-`N` real-time correction, and pair-weight convolution are all matched, does the actual finite-height zeta window leave any reproducible residual whose sign or scale is predicted independently by arithmetic lower-order terms?

## Research question

Can the actual finite-height Montgomery statistic be transferred to a finite-CUE control with the same source-window geometry, nonstationary unfolding, pair weight, diagonal convention, effective-size rule, and covariance structure, so that a predeclared low-dimensional support-edge residual can be tested without universal finite-size or smoothing contamination?

If such a matched null exists, is there an amplitude normalization for the post-null residual that follows from the arithmetic lower-order formula rather than from inspecting zero data, and does the resulting statistic survive on untouched high-zero material?

## Why it may matter

This route is source-motivated rather than a post-hoc repair of the failed third-order panel. Pair-correlation error terms are classically linked to prime-side fluctuation information, while the random-matrix support edge supplies a strong universal null. The exact controls in `VIS-123` and `VIS-124` make it possible to ask whether anything genuinely source-specific remains after those two effects are removed.

A positive result would still most likely organize known lower-order arithmetic rather than establish a new pair-correlation theorem. A negative result is equally useful: if the finite-height/window transfer absorbs the residual, the support edge should be treated as another closed visual control rather than an arithmetic carrier.

## Decisive test

Do not inspect fresh confirmation zeros yet. First freeze one exact finite-height statistic. Preserve the chosen zero-height window, local-density convention, Montgomery pair weight, diagonal treatment, edge coordinates, and low-dimensional decision statistic.

Use `VIS-123` for the exact phase dictionary and finite-`N` continuous-time CUE edge correction. Use `VIS-124` to apply Montgomery's pair weight as the exact Laplace convolution `P_L*K_N`, rather than evaluating the unweighted CUE curve pointwise. Then derive or simulate the remaining source-window transfer: hard/tapered height geometry, density variation across the window, effective `N(T)`, any compactification/branch convention, and the joint covariance of all predeclared edge coordinates. The finite-CUE control must reproduce those choices exactly enough that a null sample and the source statistic live in the same representation.

Only after that null is fixed should the arithmetic lower-order formula determine whether the post-null residual is expected at scale `1/log T`, `log log T/log T`, another scale, or no stable universal scale. The universal finite-`N` ripple from `VIS-123` and the weight-induced `1/log T` bump from `VIS-124` must be removed before choosing a residual amplitude normalization.

Then test on untouched high-zero material using the frozen statistic and combined decision rule. Kill the route if the residual is reproduced by the fully matched finite-CUE/window null, disappears under exact diagonal/window accounting, changes qualitatively under predeclared reasonable representations, or reduces entirely to established lower-order arithmetic with no residual question. Continue only if a predeclared residual survives and agrees with an arithmetic prediction made before confirmation data are inspected.

## Evidence boundary

Montgomery's pair-correlation statistic and support boundary, CUE/GUE pair statistics, exact all-real-time finite-`N` CUE form factors, and the pair-correlation/short-interval arithmetic bridge are prior art. `VIS-123` establishes only the phase/edge calibration and one universal finite-CUE correction. `VIS-124` establishes only the exact Fourier-convolution effect of Montgomery's pair weight and the resulting universal ramp rounding.

The actual finite-height zeta-to-CUE window transfer, the correct effective `N(T)`, the joint covariance after that transfer, the post-null amplitude scale, and the existence of any reproducible arithmetic support-edge residual remain unproved. No fresh zero confirmation data have been inspected for the resulting design.

Even a successful test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new zero-correlation theorem.

## Research disposition

Accepted for continued investigation. The phase-centering and pair-weight layers are now calibrated; the next unresolved step is **finite-window/effective-size transfer after exact weight convolution, not source inspection**. Acceptance records that this bounded residual question remains worth testing, not that a nonzero arithmetic residual exists.