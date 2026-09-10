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
  - research/visual_exploration/SOURCES.md
---

# Does the Montgomery support edge carry a reproducible arithmetic residual beyond a correctly windowed finite-CUE null?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before any fresh zero confirmation. `VIS-123` fixes the phase dictionary and shows that the all-real-time full-circle finite-`N` CUE statistic has a logarithmic support-edge ripple. `VIS-124` identifies Montgomery's pair weight as an exact Laplace multiplier/convolution. `VIS-125`--`VIS-128` isolate source-window leakage, rule out a growing hard window inside one logarithmic-size CUE circle, and replace it by an explicit bounded tent taper whose pair-overlap kernel is known exactly. `VIS-129` supplies the classical pair-correlation effective-size candidate `N_e(T)=rho_* L_T`, with `rho_*=1/sqrt(12 Lambda)=0.230156986...`, so a single non-wrapping tent arc must satisfy `H_src<2*pi*rho_*=1.44611899...`.

`VIS-130` corrects the finite-`N` transfer by showing that a bounded source taper must replace, rather than compound, the rectangular coordinate-overlap factor already built into the full-circle continuous-time spectral form factor. The exact connected bounded-tent CUE mean is

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 exp(2*pi*i*q*x) dx`.

`VIS-131` now derives the support-edge mean asymptotic of this corrected object. For `rho=N/L`, `kappa=M/L<rho`, and `q=1+v/L`,

`C_(N,L,M)(1+v/L)`
` = 1 - Phi_(rho,kappa)(v)/L + O(L^-3)`,

with an explicit Poisson-sampled profile

`Phi_(rho,kappa)(v)=rho^-2 sum_(j>=1) j hat g_kappa(v+j/rho)`.

The single-arc capacity condition makes the leading rounding alias-free and forces

`Phi(-v)-Phi(v)=v`,

so after subtracting the ideal ramp/plateau the leading finite-CUE rounding is symmetric across the edge. More importantly, the profile depends regularly on the effective-size ratio: a ratio perturbation `delta rho` changes the bounded-source mean only by `O(delta rho/L)`. Therefore the `delta rho=O(1/log L)` ambiguity that was dangerous for the full-circle real-time statistic is only `O(1/(L log L))` here and is no longer a same-order `1/L` mean obstruction.

The remaining residual question has consequently moved again. The bounded-tent **mean** null and its first-order effective-size sensitivity are now controlled analytically, but the joint covariance of the frozen edge coordinates, stochastic finite-height transfer/unfolding effects, and any independently predicted arithmetic lower-order amplitude are still missing.

## Research question

For one predeclared bounded physical tent width `H_src<1.44611899...` with nonvanishing capacity margin, one effective-size rule and integerization convention, and a small frozen set of nondegenerate edge coordinates `v`, what is the exact or asymptotically controlled **joint covariance** of the corresponding finite-CUE statistics after the `VIS-131` mean profile is subtracted?

Can the remaining finite-height zeta-to-CUE transfer uncertainties — including counting/unfolding fluctuations, diagonal convention, and any admissible error in `N(T)` beyond its now-subleading mean effect — be propagated through that covariance strongly enough that a later arithmetic residual has a genuinely predeclared amplitude, direction, and significance?

## Why it may matter

`VIS-131` removes a previously plausible identifiability obstruction rather than producing a positive arithmetic signal. A smooth bounded source taper does more than fit inside one effective CUE circle: it also removes the slow full-circle window tail responsible for the logarithmically amplified effective-size sensitivity. This makes an `O(1/L)` residual *in principle* distinguishable at the mean level even when the effective-size ratio is known only up to `O(1/log L)`.

That is useful only if covariance and source-side transfer do not reintroduce an equally large nuisance direction. A positive result after those controls would still most likely organize known arithmetic lower-order structure rather than establish a new pair-correlation theorem. A negative result would close the support-edge route cleanly by showing that the fully matched stochastic null absorbs it.

## Decisive test

Do not inspect fresh confirmation zeros. Freeze the bounded tent width, the effective-size rule and integerization, local unfolding, Montgomery weight, diagonal/connected normalization, edge coordinates `v`, and one combined residual statistic.

Use the exact `VIS-130` finite-CUE source-window statistic and the `VIS-131` Poisson-sampled mean profile as the null mean. Derive the covariance matrix of the frozen coordinates under the same finite-`N` CUE/tent/weight convention rather than importing full-circle covariance. Check that the covariance construction respects the same non-wrapping source geometry and determine its large-`L` scale.

Propagate finite-height transfer uncertainty through the **joint** null. In particular, include the residual effect of theoretically admissible perturbations of `N(T)`, smooth and stochastic unfolding/counting errors, and the exact diagonal convention. The mean-level `delta rho=O(1/log L)` direction established in `VIS-131` should enter only at `O(1/(L log L))`; if a covariance or transfer term lifts it back to `O(1/L)`, that mechanism must be derived explicitly rather than inferred from the obsolete full-circle logarithmic ripple.

Only after the complete mean-plus-covariance null and nuisance directions are frozen should an arithmetic lower-order formula determine the predicted residual amplitude/direction. Then test the frozen statistic on untouched high-zero material with the predetermined combined decision rule. Kill the route if the residual is reproduced by the fully matched finite-CUE/taper null, absorbed by justified source-transfer uncertainty, disappears under exact diagonal/window/unfolding accounting, or reduces entirely to established lower-order arithmetic with no residual question.

## Evidence boundary

The CUE determinantal kernel, Fejer expansion, Poisson summation, Montgomery's pair statistic and weight, finite-size CUE models for Riemann zeros, and ordinary window/autocorrelation Fourier identities are prior art. `VIS-123`--`VIS-131` establish a sequence of calibration and compatibility controls plus the corrected bounded-tent mean null and its leading support-edge profile; they do not establish any arithmetic residual.

`VIS-131` is specifically a mean-null result. It does not derive the joint covariance, the exact finite-height zeta-to-CUE transfer, stochastic counting-function effects, or an arithmetic lower-order amplitude. Its regular effective-size sensitivity is conditional on a fixed positive single-arc capacity margin and the smooth bounded tent; harder windows or a taper approaching the circle capacity can have different edge behavior.

No fresh zero confirmation has been inspected for this narrowed design. Even a positive later test would not prove RH, Montgomery's full pair-correlation conjecture, Hardy--Littlewood prime-pair asymptotics, or a new random-matrix theorem.

## Research disposition

Accepted for continued investigation. `VIS-131` resolves the bounded-tent **mean support-edge asymptotic and first-order effective-size sensitivity** portion of the previous decisive test. The remaining gate is the joint finite-CUE covariance plus finite-height transfer/nuisance propagation for the frozen edge coordinates, followed — only if that survives — by an independently predicted arithmetic amplitude and untouched source confirmation.
