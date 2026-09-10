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
  - research/visual_exploration/findings/VIS-140-rudnick-sarnak-support-budget-misses-edge-covariance.md
  - research/visual_exploration/findings/VIS-141-rudnick-sarnak-edge-companion-bandwidth-collapse.md
  - research/visual_exploration/SOURCES.md
---

# Can a Montgomery support-edge arithmetic residual beat the finite-CUE noise and finite-height transfer floor?

## Observation

The support-edge thread has progressively removed universal and representation-induced effects before inspecting fresh confirmation zeros. `VIS-123`--`VIS-131` fix the phase dictionary, Montgomery smoothing, source-window convention, capacity/effective-size controls, and the bounded-tent finite-CUE mean profile. `VIS-132` isolates the realized diagonal `1/L` fluctuation as a common mode removable exactly by samplewise subtraction or a predeclared zero-sum contrast.

`VIS-133` shows that nearby normalized terminal edge amplitudes retain an explicit strictly positive-definite covariance kernel `R_(alpha,rho)`. `VIS-134` decomposes the corresponding intensity covariance into a positive Wick kernel plus a potentially cancelling connected fourth cumulant and proves that neither zero-sum projection nor fixed Laplace smoothing removes the Wick contribution. `VIS-135` closes the remaining single-window CUE loophole: higher normalized cumulants vanish, so the terminal packet is asymptotically proper complex Gaussian and its smoothed intensity field retains the positive order-one covariance floor.

`VIS-136` sharpens the averaging gate. For a stationary sequence of frozen per-window contrasts with covariance `gamma(h)`, the exact variance of the average is `m^(-1)[gamma(0)+2 sum_(h<m)(1-h/m)gamma(h)]`. Thus the covariance tail fixes the information exponent: short memory with positive long-run variance gives the familiar quadratic `Theta(L^2)` requirement for an `O(1/L)` mean shift, positive long memory is worse, a persistent common mode blocks averaging, and faster decay requires separately proved low-frequency cancellation.

`VIS-137` closes the within-circle translation loophole. Translating the same fixed-ratio tent around one CUE matrix gives a leading cross-window covariance equal to the Fourier transform of the actual overlap of the two source tents; pairwise-disjoint tents decorrelate at leading order. But each tent occupies a fixed angular fraction `alpha`, so at most `floor(1/alpha)` pairwise-disjoint supports fit on one circle. A single finite-CUE realization therefore cannot manufacture the required `m -> infinity` source-window pool merely by taking more translated windows.

`VIS-138` closes a stronger marginal-calibration loophole. A stationary refresh chain can have **exact CUE(N) marginal law in every source window** while its centered contrast has covariance `q^h sigma_N^2`. For fixed `q<1` it is reversible and geometrically mixing, yet the long-run variance is inflated by `(1+q)/(1-q)`; if `1-q_L` shrinks like `L^-alpha`, the window requirement for a `1/L` signal grows from `L^2` to `L^(2+alpha)`. At `q=1` averaging fails completely. Thus exact one-window CUE means, cumulants, and edge covariances do not identify the cross-height averaging law, and even pointwise-in-`L` mixing is insufficient without a uniform dependence bound.

`VIS-139` identifies the correlation order consumed by the disjoint-window gate. For quadratic pair statistics supported on disjoint source windows, the exact covariance is a four-level factorial-moment functional `alpha^(4)-alpha^(2) tensor alpha^(2)`; shared-point second- and third-level contractions vanish. An explicit four-site even-parity process matches independent Bernoulli occupancy through every one-, two-, and three-site inclusion marginal yet changes the covariance of two disjoint pair indicators from `0` to `1/16`. Thus Montgomery-style two-level pair correlation, even supplemented by arbitrary exact three-level marginals, cannot determine the needed disjoint-window covariance without additional structure.

`VIS-140` then checks the most obvious unconditional four-level source. Rudnick–Sarnak's zeta `n`-level theorem requires `sum_j |xi_j|<2`; on the pair-pair plane `(q,-q,r,-r)` this is exactly `|q|+|r|<1`. Two Montgomery-edge factors near `(q,r)=(1,1)` therefore lie far outside the theorem's support budget, and the point `(1,0)` is already on the forbidden boundary.

`VIS-141` sharpens that support failure into a design law. If pair-frequency supports are `A,B`, with `a=sup_A|q|` and `b=sup_B|r|`, a tensor-product covariance test can fit wholly inside Rudnick–Sarnak only when `a+b<1`. Identical factors require `a<1/2`, so simply narrowing two copies of an edge statistic cannot preserve the Montgomery edge. If one factor approaches the edge with `a=1-epsilon`, the companion is forced into `b<epsilon`; as the edge probe approaches `|q|=1`, the companion collapses toward DC. The restricted-support escape is therefore not an edge-edge variance estimate but a different asymmetric edge–low-frequency observable whose arithmetic relevance must be proved separately.

## Research question

For a predeclared sequence of actual zeta height windows using the exact bounded-tent, effective-size, unfolding, diagonal-subtraction, edge-coordinate, and Montgomery conventions frozen by `VIS-123`--`VIS-141`, what covariance tail or low-frequency spectral law does the resulting per-window contrast obey?

For the original disjoint-window **edge-edge** statistic, can the required four-level cross-height functional be controlled uniformly in `L` by a genuinely wider-support theorem, a structural closure valid for the exact statistic, or a direct covariance/mixing theorem that bypasses the factorial-moment expansion?

A separate redesign question remains: can one construct an asymmetric near-edge × low-frequency observable that stays inside a rigorously available support domain **and** independently prove that its collapsing low-frequency companion carries a source-specific arithmetic signal at the required scale rather than only coarse density/window information? Such a redesign is not evidence for the variance of the original edge statistic and must earn its own arithmetic interpretation.

For overlapping windows, can the additional second- and third-level contraction terms also be controlled at the shrinking `1/L` signal scale?

Only after the dependence law and finite-height transfer error are controlled should an arithmetic lower-order formula determine a frozen residual amplitude/direction and untouched zeta confirmation data be inspected.

## Why it may matter

The current CUE null is well constrained at the single-window level: its mean, common diagonal mode, terminal amplitude covariance, fourth-cumulant behavior, and fixed smoothing are all explicit. `VIS-136` shows that source-window dependence can change the asymptotic sample requirement itself, `VIS-137` shows that a finite CUE circle cannot supply a growing independent sample merely by translation, and `VIS-138` shows that **no amount of single-window marginal calibration can repair the missing cross-window coupling law**.

`VIS-139` makes the missing information concrete at the four-level layer. `VIS-140` shows that the classical unconditional Rudnick–Sarnak support theorem does not reach the edge-edge packet, while `VIS-141` rules out a vague “just redesign it inside the support diamond” shortcut for two identical edge factors: doing so pushes each factor below `|q|<1/2`. Keeping one factor near the edge instead forces the other toward DC and changes the statistic.

The live fork is therefore sharper. Either obtain genuinely wider-support/direct four-level control for the original frozen edge covariance, or deliberately study a different edge–low-frequency observable and prove from scratch that it retains the desired arithmetic channel. This prevents restricted-support compatibility from being mistaken for preservation of the original question.

## Decisive test

Do not inspect untouched confirmation zeros. First freeze a sequence of zeta source-window centers, widths, overlaps/separations, local unfolding rule, effective-size rule, and the exact pair-frequency support/decay convention of the statistic. For disjoint windows, write the exact order-two pair kernel of the frozen support-edge contrast and reduce its cross-window covariance to the corresponding four-level factorial-moment integral from `VIS-139`. Then obtain a bound or asymptotic for that integral that is uniform in the same `L`-dependent family needed by the experiment.

Any attempt to invoke Rudnick–Sarnak restricted support must expose the actual pair supports. For tensor-product factors `A_L,B_L`, verify `sup_(q in A_L)|q| + sup_(r in B_L)|r| < 1` with the strict support margin required by the theorem. If the first factor approaches the Montgomery edge so that `a_L=1-epsilon_L -> 1`, the second must satisfy `b_L<epsilon_L -> 0`; additionally justify any use of an `L`-dependent family whose support margin itself tends to the theorem boundary. For identical factors the gate `a_L<1/2` shows immediately that the original edge statistic has been abandoned.

If an asymmetric edge–low-frequency redesign is pursued, define the companion observable explicitly and derive a source-specific arithmetic contribution at the target scale before treating it as useful. Kill that redesign if the low-frequency factor reduces to density/window/diagonal information, if the arithmetic term disappears as its bandwidth collapses, or if the finite-height transfer error is not below the claimed signal. A non-factorized four-level test is admissible only after proving a quantitative bridge back to the desired arithmetic residual; support placement alone is not enough.

A lower-order shortcut for the original statistic is admissible only with a proved structural closure, such as an appropriate determinantal/Gaussian/Wick-type joint law that genuinely determines the needed four-level term in the relevant finite-height regime. Pair correlation by itself is not such a closure. If a direct mixing/covariance theorem is used instead, it must bound the same frozen statistic rather than a neighboring observable.

For overlapping source windows, retain and control the explicit second- and third-order shared-point contractions rather than importing the disjoint-window formula. If a multi-CUE surrogate is used, specify its **joint** law across blocks. Independent CUE blocks are only one admissible coupling; `VIS-138` gives equally exact CUE-marginal geometrically mixing couplings with arbitrarily degrading long-run variance.

Classify the resulting average using the `VIS-136` regimes. If covariance is summable, establish the long-run variance and whether it is strictly positive. If a Markov/spectral-gap surrogate is invoked, quantify the gap uniformly in `L`; a gap of order `L^-alpha` already permits an `L^(2+alpha)` source-window requirement by `VIS-138`. If a positive power-law tail is present, determine its exponent. If a common mode survives, treat that as an averaging obstruction. If faster-than-`1/m` variance decay is claimed, prove the low-frequency cancellation that makes the long-run variance degenerate instead of inferring it from finite data.

Independently bound the finite-height zeta-to-null mismatch and nuisance propagation through the same statistic at order `1/L`. The gate passes only if covariance-implied averaging error and transfer uncertainty can both be made smaller than a predeclared arithmetic amplitude without fitting window selection, effective size, or statistic to confirmation data.

## Evidence boundary

`VIS-135` is a matched finite-CUE single-window result. `VIS-136` is an exact stationary-covariance feasibility reduction. `VIS-137` gives translated-window covariance geometry and a fixed-ratio packing obstruction within one CUE realization. `VIS-138` gives an exact matched-marginal family proving that one-window CUE laws, and even nonuniform geometric mixing at each fixed `L`, do not determine the source-window averaging exponent. `VIS-139` is an exact generic point-process identifiability result showing that disjoint quadratic pair-statistic covariance requires four-level information absent from lower-order marginals.

`VIS-140` is a literature-bounded support audit: the classical Rudnick–Sarnak theorem does not include the Montgomery edge-edge four-level packet. `VIS-141` is an elementary support-budget corollary showing that an identical-factor restricted-support redesign is confined below `|q|<1/2`, while a near-edge factor forces an independent companion band toward zero frequency. Neither finding proves that no wider-support theorem, direct covariance theorem, non-factorized bridge, or useful edge–low-frequency arithmetic observable exists.

None of these results establishes the four-level correlation law of actual zeta height windows, stationarity or mixing of that sequence, a cross-height finite-CUE transfer theorem, a uniform spectral gap, or the existence of an arithmetic residual. The `Theta(L^2)` count remains conditional on summable covariance with uniformly controlled positive long-run variance. No fresh confirmation-zero evidence has been used.

## Research disposition

Accepted for continued investigation. The main gate remains the original **edge-edge** dependence problem: control the four-level cross-height functional of the exact frozen disjoint-window zeta pair statistic uniformly in `L`, prove a structural closure that supplies that control, or bypass it with a direct covariance/mixing theorem; then independently control finite-height transfer at order `1/L`.

The Rudnick–Sarnak restricted-support route is now narrowed rather than left generic. It cannot control two identical Montgomery-edge factors; any support-safe near-edge construction must use a collapsing low-frequency companion and must separately prove that this changed observable still carries a nontrivial arithmetic signal. Two-level Montgomery calibration alone remains insufficient, and arithmetic-amplitude fitting plus untouched confirmation remain downstream.