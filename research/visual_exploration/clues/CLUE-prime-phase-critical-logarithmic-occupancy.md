---
id: CLUE-visual-exploration-prime-phase-critical-logarithmic-occupancy
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/findings/VIS-225-coherent-prime-blocks-force-divergent-ising-scale.md
  - research/visual_exploration/findings/VIS-226-subcritical-symmetric-taper-worst-start-exact-scale.md
  - research/visual_exploration/findings/VIS-227-critical-phase-cell-collisions-have-balanced-occupancy-floor.md
  - research/visual_exploration/findings/VIS-228-multinomial-cell-collisions-have-extensive-excess-above-balanced-floor.md
  - research/visual_exploration/findings/VIS-229-nonuniform-categorical-cell-collisions-have-third-moment-variance.md
  - research/visual_exploration/findings/VIS-230-stationary-markov-cell-collisions-have-lag-return-center.md
  - research/visual_exploration/findings/VIS-231-stationary-markov-cell-collisions-have-exact-triple-quadruple-variance.md
  - research/visual_exploration/findings/VIS-232-transition-conditioned-collision-controls-are-occupancy-degenerate.md
  - research/visual_exploration/findings/VIS-233-lag-two-returns-escape-first-order-markov-type.md
  - research/visual_exploration/findings/VIS-234-markov-type-lag-two-pgf-recursion.md
  - research/visual_exploration/findings/VIS-235-lag-two-markov-type-mean-by-two-step-deletion.md
  - research/visual_exploration/findings/VIS-236-ordered-prime-coordinate-cells-make-first-order-type-degenerate.md
  - research/visual_exploration/findings/VIS-237-random-origin-cell-collisions-are-triangular-pair-functional.md
  - research/visual_exploration/findings/VIS-238-fixed-count-tent-calibration-removes-poissonization-variance.md
  - research/visual_exploration/findings/VIS-239-cumulative-intensity-gauge-uniformizes-specified-iid-intensity.md
  - research/visual_exploration/findings/VIS-240-rotation-randomized-dirichlet-gaps-give-fixed-count-uniform-intensity-dependence-null.md
  - research/visual_exploration/findings/VIS-241-random-cut-separates-endpoint-phase-variance.md
---

# Is there prime-specific critical pair geometry after fixed-count dependent-spacing and endpoint-phase calibration?

## Observation

The critical coherence-cell branch has progressively removed several large but non-arithmetic sources of structure. `VIS-227`--`VIS-231` calibrate deterministic occupancy, independent occupancy noise, one-point heterogeneity, and first-order Markov effects. `VIS-232`--`VIS-236` then show that conditioning on occupancies or on the exact first-order transition type is too strong for the actual ordered prime-coordinate representation: the cell labels are monotone runs, so the endpoint-matched transition table has no useful internal randomization.

`VIS-237` replaces arbitrary cell-origin scans by an exact quotient. Averaging an equal-width grid over its origin turns the same-cell count into the triangular short-range pair functional

`sum_(a<b) (1-|x_b-x_a|/ell)_+`.

`VIS-238` shows that the null must also respect the observed fixed point count: at critical occupancy, Poissonization adds a separate leading `Theta(m)` variance channel that disappears under the fixed-count uniform model. `VIS-239` removes any independently specified iid one-point intensity exactly by cumulative-intensity coordinates, while showing that same-sample empirical-CDF flattening is degenerate because it maps the data to a deterministic rank lattice.

`VIS-240` supplies the first nontrivial dependence family that respects all of those boundaries simultaneously. Symmetric cyclic gaps

`(G_1,...,G_m)/L ~ Dirichlet(alpha,...,alpha)`

followed by a uniform rotation and cut produce a fixed-count, monotone ordered-point process with exactly uniform one-point intensity. The parameter `alpha` changes short-gap dependence, and the finite-sample mean of the linear tent statistic is available exactly through beta/incomplete-beta integrals. Thus the iid-uniform model is only the `alpha=1` member of a wider representation-matched dependence calibration.

`VIS-241` separates the still-missing variance calibration into two exact channels. For a fixed circular configuration, averaging over the random cut gives the intrinsic pair functional

`bar T=sum_(i<j) (1-delta_ij/ell)_+(1-delta_ij/L)`,

where `delta_ij` is the shorter circular distance. If `G` denotes the random gap configuration, then

`Var_(G,Theta)(T)=Var_G(bar T)+E_G[V_cut]`,

with `V_cut` given exactly by weighted overlaps of the minor pair arcs. The first term is genuine circular gap-geometry variance; the second is variance introduced only by where the auxiliary circle is cut into a finite interval.

The live issue is therefore no longer a generic search for a stronger null. It is to calibrate the remaining **dependent circular pair geometry** without reintroducing arbitrary endpoint phase, count noise, intensity fitting, or support mismatch.

## Research question

Fix the critical `lambda` family, the inherited width rule, and a dependence model independently of confirmation data. After quotienting grid origin, total-count randomness, specified iid one-point intensity, and—when endpoints are nuisance—the random-cut phase, does the prime-coordinate configuration exhibit a stable residual relative to a fixed-count monotone dependence null?

The immediate tractable target is the symmetric-Dirichlet family of `VIS-240`. For a predeclared `alpha`, derive or independently validate the finite-sample variance/covariance of

`bar T=sum_(i<j) (1-delta_ij/ell)_+(1-delta_ij/L)`

under the circular Dirichlet gaps. If the physical interval endpoints are instead mathematically meaningful, retain the linear post-cut statistic and add the exact endpoint-phase contribution `E_G[V_cut]` from `VIS-241` rather than conflating it with gap dependence.

If a residual survives this calibration across increasing scales, can it be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has now isolated almost every obvious scalar nuisance at the critical cell scale: forced finite occupancy, independent and heterogeneous occupancy noise, serial-label dependence, conditioning degeneracy, monotone-support constraints, grid phase, count randomization, specified one-point intensity, a nontrivial fixed-count spacing-dependence axis, and finally the endpoint phase introduced by opening a stationary circular model into an interval.

This makes the next comparison materially harder to dismiss. A signal that vanishes after calibrating `Var_G(bar T)` was generic short-gap dependence, not prime-specific structure. A signal that survives still does not prove anything about RH, but it would have passed a substantially stronger representation-matched null than the earlier occupancy, Poisson, iid-uniform, or arbitrary-grid controls.

The separation in `VIS-241` is also operationally important: it prevents a hard Dirichlet covariance calculation from spending effort on a variance component caused only by an arbitrary cut. The gap-geometry term can now be attacked directly when endpoint phase is not part of the mathematical signal.

## Decisive test

Before confirmation, freeze the midpoint-symmetric taper, phase/coherence tolerance, critical `lambda` family, point-coordinate normalization, width rule, statistic, endpoint convention, and null family. Do not tune `alpha` on the same statistic being tested; choose it from theory, independent data, or a fitting procedure whose uncertainty is carried through the null.

If endpoints are treated as nuisance, use the cut-averaged statistic `bar T` and calibrate `Var_G(bar T)` under the frozen symmetric-Dirichlet family. An exact calculation is preferred; an independently validated numerical calibration is admissible only if it preserves the fixed count, circular gap law, and predeclared parameter without retuning on confirmation outcomes. Check the result at `alpha=1` against the corresponding iid-uniform circular-spacing specialization and against direct finite-sample integration or high-precision simulation.

If endpoints are treated as signal, use the linear post-cut statistic and calibrate

`Var_G(bar T)+E_G[V_cut]`

with `V_cut` computed from the exact pair-arc overlap formula of `VIS-241`. Do not switch between endpoint-sensitive and endpoint-quotiented statistics after seeing which gives the stronger residual.

A stronger null beyond symmetric Dirichlet is useful only if it preserves increasing point support, fixed count, the predeclared one-point intensity treatment, and a nondegenerate value of the chosen statistic. Hard-core, renewal, or Markov-gap alternatives may be compared after the Dirichlet calibration, but opening a second null family is not necessary to decide the present variance question.

Kill the candidate if the apparent anomaly disappears under the frozen dependent-spacing calibration; if significance depends on the Poisson count channel isolated by `VIS-238`; if it depends on same-sample empirical-CDF flattening ruled out by `VIS-239`; if it is driven by random-cut phase after endpoints were declared nuisance; if `alpha` or another null parameter must be retuned on confirmation data; or if the control gains apparent flexibility only by leaving the monotone ordered-point support.

Only after a residual survives these gates should it be translated back through the signed phase kernel. Before promotion to a prime-specific finding, audit equivalent formulations in logarithmic prime gaps, short-interval counts, renewal and repulsive point-process controls, prime-pair/higher-correlation statistics, and the relevant critical Dirichlet-polynomial literature.

## Evidence boundary

`VIS-227`--`VIS-236` establish occupancy/Markov baselines and the support/conditioning obstructions that make label-randomization controls unsuitable for the actual monotone cell representation. `VIS-237` establishes the exact grid-origin quotient. `VIS-238` establishes fixed-count versus Poisson mean/variance calibration. `VIS-239` establishes exact removal of a specified iid one-point intensity and the degeneracy of same-sample empirical-CDF flattening.

`VIS-240` establishes a fixed-count, uniform-intensity, monotone-support symmetric-Dirichlet spacing family and its exact finite-sample tent-statistic mean. It does not supply the dependent variance or assert that any `alpha` models prime gaps faithfully.

`VIS-241` establishes an exact decomposition of the random-cut variance into circular gap-geometry variance and endpoint-phase variance. It does not compute `Var_G(bar T)`, estimate the size of the cut term asymptotically, identify the correct endpoint convention for the prime problem, or establish a surviving prime residual.

None of the cited findings establishes prime-specific critical separation, a faithful final stochastic model of the prime coordinates, or any RH consequence.

## Research disposition

The clue remains `accepted`. Its current frontier is a single bounded calibration problem: with the endpoint convention fixed in advance and `alpha` frozen independently of confirmation data, compute or independently validate the finite-sample variance of the cut-averaged circular tent functional under the symmetric-Dirichlet gap family. Only after that variance is available should the prime configuration be tested for a residual.