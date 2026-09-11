---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
  - research/visual_exploration/findings/VIS-083-gram-point-prime-phase-haar-equidistribution.md
  - research/visual_exploration/findings/VIS-084-gram-short-block-prime-phase-freezing.md
  - research/visual_exploration/findings/VIS-085-gram-local-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-086-quadratic-gram-arc-growing-support-collapse.md
  - research/visual_exploration/findings/VIS-087-finite-order-gram-clock-null-hierarchy.md
  - research/visual_exploration/findings/VIS-088-polynomial-sensitivity-observables-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-089-inverse-polynomial-decision-margins-inherit-gram-clock-null.md
  - research/visual_exploration/findings/VIS-090-consecutive-gram-superlog-prime-torus-haar.md
  - research/visual_exploration/findings/VIS-091-gram-log-lag-increment-clock-collapse.md
  - research/visual_exploration/findings/VIS-150-gram-superlog-lag-second-clock-transition.md
  - research/visual_exploration/findings/VIS-151-gram-exact-lag-shear-haar.md
  - research/visual_exploration/findings/VIS-152-gram-joint-lag-finite-difference-threshold.md
  - research/visual_exploration/findings/VIS-153-gram-critical-lag-newton-product-law.md
  - research/visual_exploration/findings/VIS-154-gram-fixed-irregular-lag-vandermonde-threshold.md
  - research/visual_exploration/findings/VIS-155-gram-irregular-critical-haar-fiber-curve.md
  - research/visual_exploration/findings/VIS-156-gram-fixed-affine-subsampling-clock-null.md
  - research/visual_exploration/findings/VIS-157-quadratic-gram-index-pairwise-haar-triple-clock.md
  - research/visual_exploration/findings/VIS-158-polynomial-gram-index-d-wise-haar-threshold.md
  - research/visual_exploration/findings/VIS-159-power-law-gram-index-ceiling-haar-threshold.md
  - research/visual_exploration/findings/VIS-160-growing-degree-diagonal-gram-selector-complete-haar.md
  - research/visual_exploration/findings/VIS-161-two-prime-phase-height-injective-noncontinuous.md
  - research/visual_exploration/findings/VIS-162-prime-phase-lipschitz-decoder-collision-quotient.md
  - research/visual_exploration/findings/VIS-163-omitted-prime-phase-no-continuous-finite-support-decoder.md
  - research/visual_exploration/findings/VIS-164-anchored-heldout-prime-collision-haar-tail.md
  - research/visual_exploration/findings/VIS-165-prime-log-collision-polynomial-discrepancy.md
  - research/visual_exploration/findings/VIS-166-anchored-haar-collision-moment-threshold.md
  - research/visual_exploration/findings/VIS-167-prime-log-growing-cap-moment-transfer.md
  - research/visual_exploration/findings/VIS-168-growing-support-collision-null-mass-barrier.md
---

# Can a zeta visual statistic leave the regular prime-torus representation class after the full Gram-clock quotient?

## Observation

The prime-phase program has progressively removed representation and sampling effects that can look arithmetically structured without adding a new usable mechanism. `VIS-064`--`VIS-066` show that invertible hybrid factor/residual recombinations do not create information, while `VIS-083`--`VIS-091` and `VIS-150`--`VIS-156` show that the deterministic Gram clock can generate Haar populations, coherent lag fields, critical Haar fibers, irregular-delay geometry, and sparse affine samples from the same fixed-prime state.

`VIS-157`--`VIS-160` then show that increasingly complicated deterministic selectors do not solve this problem. Every fixed polynomial/power-law selector has a finite-order clock threshold, and a diagonal selector of growing degree can pass every fixed finite-order finite-prime Haar test. Fixed-test success, even at arbitrarily high finite order, is therefore not source evidence.

`VIS-161`--`VIS-163` move from sampling to representation. Two exact prime phases already identify height set-theoretically, but only through a nowhere-continuous inverse; finite-prime Lipschitz decoding is exactly a phase-collision quotient; and a completely ordinary held-out prime already has no continuous or globally Lipschitz decoder from fixed retained support. Absolute decoder failure is therefore not source-sensitive.

`VIS-164` makes that omitted-source control quantitative on exact returns of one retained prime. With `d=|P|-1`, the held-out-prime collision score has a fixed-threshold Haar law with tail `c_d L^(-d)`. `VIS-165` crosses the first order-of-limits boundary: Matveev-type finite Diophantine control plus Erdős--Turán--Koksma discrepancy gives a polynomial finite-`Q` discrepancy rate for the prime-log rotation, and the collision exceedance law continues to track its shrinking Haar tail for thresholds `L(Q)=Q^gamma` with sufficiently small positive `gamma`. Thus even **positive-power growth of anchored collision scores is already present in the matched omitted-prime null at fixed support**.

`VIS-166` shows that the same support dimension is the exact Haar moment threshold: collision moments are finite precisely for orders `s<d`, critical order `s=d` diverges logarithmically, and `s>d` diverges polynomially. `VIS-167` combines that moment law with the quantitative discrepancy bound from `VIS-165`: a nontrivial positive-power family of growing caps already transfers from Haar to the deterministic held-out-prime orbit. Subcritical capped moments can converge to their finite Haar population values, while critical and supercritical capped moments exhibit the generic dimension-forced logarithmic or polynomial growth. Raw or capped moment growth is therefore not a source-sensitive escape route either.

`VIS-168` closes a different part of the growing-support boundary before discrepancy is even considered. Uniform small-ball bounds give

`log mu_d(L)=-(d/2)log d-d log L+O(d)`

for `L>=1`. Hence any fixed positive-power threshold `L=Q^gamma` has vanishing matched Haar mass `Q mu_d(L)` as soon as `d(Q)->infinity`; a relative empirical tail law is then impossible by integer granularity. Even at fixed threshold there is a population-mass wall near `d=2 log Q/log log Q`. Growing support therefore requires dimension-rescaled thresholds and a null-mass check before one asks for uniform prime-log discrepancy.

## Research question

After quotienting the prime-torus population law, the full finite-test Gram-clock hierarchy, pathological exact-height encoding, the Lipschitz collision criterion, the dimension-coded held-out-prime tail, its quantitative shrinking-target regime, the support-dimension moment null, and the growing-support null-mass barrier, does any zeta-facing statistic exhibit a **predeclared relative regularity/decoder separation from matched omitted-prime controls**?

The target is no longer absolute instability, raw collision growth, moment growth, successful fixed-dimensional visualization, or a collision threshold whose matched Haar population is already asymptotically empty. A surviving route must distinguish the zeta-facing observable after matching support, anchor/recurrence geometry, normalization, decoder class, finite-window complexity, heavy-tail/moment normalization, and growing-support event mass.

## Why it may matter

The control surface now reaches beyond qualitative equidistribution. `VIS-165` proves that the held-out-prime null itself has a nontrivial quantitative shrinking-target regime, `VIS-166`--`VIS-167` show that the same generic recurrence controls which collision moments exist and how polynomially capped moments behave along the deterministic orbit, and `VIS-168` shows that growing support changes the population scale before any arithmetic discrepancy question arises. A numerical or visual candidate can therefore display increasing extremes, diverging high moments, apparently stable low moments, or an apparent disappearance of collisions while remaining completely source-blind.

This sharpens the useful question to a relative one. A positive result would need an exponent, normalized tail, approximation error, moment ratio, or other complexity functional that differs from the matched omitted-prime baseline under a frozen representation budget and a nondegenerate null-mass regime. Such a separation would be materially stronger than the representation, clock, tail, moment, and support-volume effects already closed; failure would close another attractive visual route without confusing generic omitted-frequency geometry with zeta-specific structure.

## Decisive test

Freeze before inspection:

- a retained finite prime support `P`, or an explicit support-growth law;
- the anchor/recurrence family and torus metric;
- the zeta-facing observable `A` and normalization;
- the base-height/window rule;
- one or more held-out-prime controls chosen by a predeclared matching rule;
- the decoder/approximation class and complexity budget;
- the collision, tail, capped-moment, or approximation statistic, threshold/cap family, comparison functional, and decision rule.

For fixed support, use `VIS-164`--`VIS-167` as the mandatory anchored-recurrence baseline. The held-out-prime control already has fixed-threshold law `mu_d(L)`, tail `c_d L^(-d)`, polynomial star-discrepancy convergence, a rigorous positive-power shrinking-threshold regime, a sharp moment threshold at order `d`, and explicit positive-power cap ranges on which deterministic capped moments inherit the Haar law.

For growing support, apply `VIS-168` **before** attempting a uniform discrepancy theorem. Require the predeclared support/threshold law to keep the matched Haar mass `Q mu_d(L)` nonvanishing, and preferably growing, if the intended statistic is a relative exceedance frequency. A fixed `L=Q^gamma` with `gamma>0` is already ruled out when `d(Q)->infinity`. A meaningful joint scale should instead be expressed through `Q mu_d(L)` or a dimension-rescaled exponent such as `kappa=d log L/log Q`; when `d~c log Q/log log Q`, the first-order Haar-mass boundary is `kappa+c/2=1`.

Only after this population gate should the deterministic problem attack uniformity in the changing dimension, prime-log Diophantine constants, boundary complexity, and next omitted frequency. A candidate is interesting only if it proves a predeclared separation from the resulting matched law: for example a different asymptotic exponent, a normalized tail ratio bounded away from the control, a capped-moment ratio with a source-dependent limit after the `VIS-167` normalization, a strictly different approximation-error law at matched decoder budget, or a stable distributional functional not forced by the same prime-log recurrence geometry.

Kill the route if the apparent zeta separation is reproduced by held-out-prime phases under the same frozen budget, disappears after normalization by the `VIS-164`--`VIS-168` control, uses a threshold whose matched Haar mass is already asymptotically empty, or depends on choosing support, thresholds, caps, windows, moment order, or controls after inspecting favorable residuals.

## Evidence boundary

`VIS-150`--`VIS-160` are deterministic clock/sampling controls. `VIS-161`--`VIS-163` establish the representation and decoder boundaries. `VIS-164` gives the fixed-threshold anchored Haar law and support-dimension tail. `VIS-165` supplies a fixed-support polynomial discrepancy rate and a conservative but rigorous jointly growing threshold regime. `VIS-166` identifies the support dimension as the exact Haar collision-moment threshold. `VIS-167` transfers those capped moments to the deterministic prime-log orbit over explicit positive-power cap ranges. `VIS-168` gives uniform-in-dimension Haar small-ball bounds and the resulting growing-support population-mass barrier.

None of these results compares a zeta-facing observable with the held-out-prime baseline and proves a source-sensitive separation. The deterministic quantitative results remain fixed-support; `VIS-168` is a population theorem and does not supply growing-dimensional prime-log discrepancy. The exponents in `VIS-165`--`VIS-167` may be extremely poor, and no result here identifies the true deterministic extreme-value scale or controls uncapped empirical moments. They give no zeta or RH consequence. The current clue therefore remains an accepted research question rather than evidence for a new mechanism.

## Research disposition

Accepted in further narrowed form. Fixed finite phase mixing, increasingly rich deterministic Gram selectors, raw-information arguments, absolute continuous/Lipschitz decoder failure, fixed-threshold omitted-prime collision tails, fixed-support positive-power anchored collision growth, support-dimension moment divergence, the corresponding polynomially capped moment laws, and **fixed positive-power collision thresholds under unbounded support growth** are all closed as standalone positive discriminators.

Continue only through a predeclared relative zeta-versus-held-out-prime separation after the `VIS-164`--`VIS-168` baseline is accounted for. A growing-support route must first remain inside a nonempty Haar-mass regime and then prove uniform deterministic control of its changing dimension and arithmetic constants rather than assuming those difficulties away.