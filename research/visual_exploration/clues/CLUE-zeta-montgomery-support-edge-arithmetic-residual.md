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
  - research/visual_exploration/findings/VIS-125-hard-window-triangular-overlap-log-edge-leakage.md
  - research/visual_exploration/findings/VIS-126-rvm-density-drift-compatible-with-log-edge-resolution.md
  - research/visual_exploration/findings/VIS-127-single-cue-circle-growing-hard-window-obstruction.md
  - research/visual_exploration/findings/VIS-128-bounded-tent-taper-composed-edge-profile.md
  - research/visual_exploration/findings/VIS-129-pair-correlation-effective-size-fixes-tent-capacity-and-resolution.md
  - research/visual_exploration/clues/CLUE-zeta-critical-strip-multiscale-geometry.md
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond finite CUE?

## Observation

`VIS-122` closes the frozen half-arc third-order confirmation route and requires any new zero-configuration thread to begin from an independent mathematical carrier. Montgomery's weighted pair-correlation transform supplies such a carrier, but the visually obvious support edge is shared by the CUE/GUE null and cannot itself count as arithmetic structure.

The universal calibration is now considerably narrower. `VIS-123` fixes the phase dictionary and continuous finite-`N` CUE support-edge correction. `VIS-124` shows that Montgomery's pair weight is exactly the unit-mass Laplace convolution

`P_L(r)=L exp(-2L|r|)`,

so a ramp subtraction or an unweighted finite-CUE subtraction leaves a deterministic `1/L_T`-scale edge bump. `VIS-125` shows that a hard source window contributes an independent squared-sinc convolution and a larger `(log M)/M` ramp-edge leakage, while a taper with finite spectral first moment removes the logarithmic enhancement. `VIS-126` shows that smooth Riemann--von Mangoldt density drift is not by itself fatal: there is a broad asymptotic corridor in which center-density linearization is below `1/L_T`.

`VIS-127` closes one apparent escape. If `N/L_T -> rho` with finite positive `rho`, a growing hard physical source window cannot simultaneously fit as one connected non-wrapping `CUE_N` arc and remain in the fixed-`tau` support-edge regime used by the current finite-CUE calibration. `VIS-128` supplies a concrete bounded replacement: for the centered tent taper `h(t)=(1-2|t|)_+`,

`Q_M^tent(r)=(3M/4)sinc^4(Mr/2)`,

and the leading Montgomery+taper edge profile is the composed null `G_lambda=q_lambda*H`, not a sum of separate corrections. The tent fits a single finite-CUE arc when `H_src<2*pi*rho`, but its universal contribution remains at order `1/L_T`.

`VIS-129` now removes part of the remaining effective-size freedom. Classical finite-size Riemann-zero/CUE pair-correlation matching supplies the source-derived candidate

`N_e(T)=rho_* L_T`,

`rho_*=1/sqrt(12 Lambda)=0.230156986...`,

with `Lambda=1.573151071...`. Under this candidate the single-circle tent capacity becomes

`H_src < 2*pi*rho_* = 1.44611899...`.

The same finding exposes a calibration-resolution gate. At generic fixed support-edge coordinate `v`, the universal `VIS-123` ripple depends on `rho` with log-enhanced sensitivity `Theta(delta_rho log L_T/L_T)`. Thus an unresolved `delta_rho=Theta(1/log L_T)` transfer ambiguity can itself produce a `Theta(1/L_T)` displacement. Leading proportionality alone is therefore insufficient for identifying a same-scale arithmetic residual; the effective-size transfer must be sharper or its uncertainty must enter the null/covariance.

The remaining candidate is consequently precise: after phase centering, exact finite-`N` correction, Montgomery-weight convolution, a predeclared capacity-compatible bounded taper, smooth-density drift, effective-size transfer/sensitivity, diagonal/arc conventions, counting fluctuations, and covariance are all matched, does the finite-height zeta statistic leave a reproducible residual whose sign and scale are predicted independently by arithmetic lower-order terms?

## Research question

Can the actual finite-height Montgomery statistic be transferred to a finite-CUE control with the same predeclared bounded source taper, smooth unfolding convention, pair weight, diagonal convention, effective-size rule, arc/compactification convention, and covariance structure, so that a low-dimensional support-edge residual can be tested without universal finite-size, smoothing, boundary-leakage, density, or effective-size-calibration contamination?

Using the classical pair-correlation candidate `rho_*`, can one freeze a physical support `H_src<1.44611899...` with nonvanishing margin, apply a predeclared integerization convention, evaluate the exact finite-`N` composed null

`P_L*Q_M^tent*K_N`,

and derive its joint covariance before any fresh zero confirmation material is inspected?

What source-side argument or uncertainty analysis controls the transfer from the pair-correlation effective size to this weighted+tapered continuous support-edge observable strongly enough that the remaining `rho` nuisance cannot imitate a `1/L_T` residual? If such a matched null exists, is there then an amplitude normalization for the post-null residual that follows from an arithmetic lower-order formula rather than from the observed zero residual itself?

## Why it may matter

This route is source-motivated rather than a post-hoc repair of the failed third-order panel. Pair-correlation error terms are classically linked to prime-side fluctuation information, while the random-matrix support edge supplies a strong universal null. The current findings have progressively removed attractive false positives and implementation ambiguities: continuous finite-CUE edge structure, Montgomery-weight smoothing, hard-window leakage, smooth deterministic density drift, the incompatible growing-hard-window/single-circle construction, the assumption that a smooth bounded taper is negligible, and now the freedom to choose an effective-size ratio from the observed residual.

The tent family plus the classical pair-correlation effective size gives one concrete path on which the remaining finite-CUE transfer can be made auditable. A positive result after all controls would still most likely organize known lower-order arithmetic rather than establish a new pair-correlation theorem. A negative result is equally useful: if the complete finite-height/CUE null or its justified effective-size uncertainty absorbs the residual, the support edge should be treated as another closed visual control rather than an arithmetic carrier.

## Decisive test

Do not inspect fresh confirmation zeros yet. First freeze one exact finite-height statistic and its source taper family. Preserve the zero-height regime, smooth-density convention, Montgomery pair weight, diagonal treatment, edge coordinates, and low-dimensional decision statistic.

Use `VIS-123` for the phase dictionary and exact finite-`N` continuous-time CUE edge correction, `VIS-124` for Montgomery's Laplace kernel, and `VIS-126` for the smooth-density linearization gate. Treat `VIS-127` as excluding the literal “grow one hard window inside one logarithmic-size CUE circle” construction. Use `VIS-128` as the explicit bounded-tent family. Use `VIS-129` to adopt the pair-correlation-derived `rho_*` as the first non-fitted effective-size candidate, freeze `H_src<1.44611899...` with margin, and specify the integerization/interpolation convention before source inspection.

Then derive the genuinely remaining null rather than adding asymptotic correction coefficients by hand. Evaluate the finite-`N` convolution `P_L*Q_M^tent*K_N` under one exact full-circle/arc convention and the same diagonal normalization as the source statistic. Determine how the pair-correlation effective-size matching transfers to this observable, how the bounded source taper is represented on the circle, the contribution of counting-function fluctuations beyond the smooth Riemann--von Mangoldt main term, and the joint covariance of every predeclared support-edge coordinate. The null and source statistic must live in the same representation.

Alongside the nominal `rho_*` null, propagate any theoretically unresolved effective-size uncertainty. At generic predeclared coordinates, kill a claimed `1/L_T` arithmetic residual if admissible variation of `rho` can move the universal null by the same order and that nuisance direction has not been independently constrained. Do not select a special zero-sensitivity/integer-mode coordinate post hoc; use multiple predeclared nondegenerate coordinates or otherwise establish the sensitivity before confirmation.

The `VIS-128` infinite-ramp profile `G_lambda` is a consistency check, not a substitute for the finite-`N` calculation. Kill any implementation whose finite-`N` null does not converge to that composed profile in the corresponding fixed-ratio regime, or whose capacity/arc convention silently periodizes the source window.

Only after the complete null and its nuisance structure are frozen should an arithmetic lower-order formula determine whether the post-null residual is expected at scale `1/log T`, `log log T/log T`, another scale, or no stable universal scale. Then test the frozen statistic on untouched high-zero material with the predetermined combined decision rule. Kill the route if the residual is reproduced by the fully matched finite-CUE/taper null, absorbed by justified effective-size uncertainty, disappears under exact diagonal/window/unfolding accounting, changes qualitatively under predeclared reasonable representations, or reduces entirely to established lower-order arithmetic with no residual question.

## Evidence boundary

Montgomery's pair-correlation statistic and support boundary, CUE/GUE pair statistics, the classical pair-correlation-derived effective matrix size, exact finite-`N` CUE form factors, Fourier windowing, triangular/tent tapers, the Riemann--von Mangoldt smooth zero density, and the pair-correlation/short-interval arithmetic bridge are prior art. `VIS-123`--`VIS-129` establish only the current control stack, compatibility boundaries, one source-derived effective-size candidate, and the precision with which an effective-size mismatch can contaminate the explicit log-enhanced null term.

In particular, `VIS-129` does not prove that `N_e(T)=rho_* L_T` is the exact effective size for the weighted+tapered support-edge statistic or that its transfer error is as large as `1/log L_T`. It shows that if an ambiguity of that order remains theoretically admissible, then a generic `1/L_T` residual is not identified against the universal finite-CUE ripple.

The exact finite-height zeta-to-CUE transfer, exact arc representation, counting-function fluctuations beyond the smooth main term, finite-`N` composed covariance, support-edge effective-size transfer precision, post-null arithmetic amplitude scale, and existence of any reproducible arithmetic support-edge residual remain unproved. No fresh zero confirmation material has been inspected for the resulting design.

Even a successful test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new zero-correlation theorem.

## Research disposition

Accepted for continued investigation. The generic source-window and effective-size choices are now narrowed to an explicit bounded-tent family and a classical pair-correlation-derived first candidate `rho_*`, with a quantified calibration-sensitivity gate. The next unresolved step is **the exact finite-`N` composed tent+Montgomery CUE null, transfer precision of the effective-size rule, counting-fluctuation accounting, arc/diagonal conventions, and covariance**, all frozen before fresh source inspection. Acceptance records that this residual question remains worth testing, not that a nonzero arithmetic residual exists.
