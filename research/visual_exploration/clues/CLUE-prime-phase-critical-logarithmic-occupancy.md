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
  - research/visual_exploration/findings/VIS-242-dirichlet-gap-tent-variance-overlap-classes.md
  - research/visual_exploration/findings/VIS-243-complement-symmetry-closes-cyclic-overlap-multiplicities.md
  - research/visual_exploration/findings/VIS-244-empirical-gap-concentration-identifies-dirichlet-alpha.md
  - research/visual_exploration/findings/VIS-245-gap-concentration-tent-covariance-beta-moments.md
  - research/visual_exploration/findings/VIS-246-concentration-conditioning-retains-dirichlet-alpha.md
  - research/visual_exploration/findings/VIS-247-log-product-conditioning-alpha-free-coarea-law.md
  - research/visual_exploration/findings/VIS-248-three-gap-log-product-discriminant-audit.md
---

# Is there prime-specific critical pair geometry after fixed-count dependent-spacing and endpoint-phase calibration?

## Observation

The critical coherence-cell branch has progressively quotiented the obvious representation and null-model confounds. `VIS-227`--`VIS-236` calibrate occupancy, heterogeneous/Markov effects, and the degeneracy of controls that ignore the actual monotone ordered-point support. `VIS-237` removes arbitrary grid origin by identifying the triangular short-range pair functional. `VIS-238` removes Poisson count noise, and `VIS-239` separates an independently specified one-point intensity from the dependence question.

`VIS-240` supplies a nontrivial representation-matched dependence family: symmetric cyclic Dirichlet gaps with fixed count, uniform one-point intensity after random rotation, monotone ordered support, and a predeclared parameter `alpha` controlling spacing dependence. `VIS-241` removes the arbitrary interval-cut phase when endpoints are nuisance. `VIS-242` reduces the exact tent variance to finite Dirichlet overlap classes, and `VIS-243` closes their deterministic cyclic multiplicities.

`VIS-244` gives a distinct same-configuration identification statistic,

`C=m sum_i X_i^2-1`,

with exact mean and variance under fixed `alpha`. `VIS-245` closes the remaining fixed-parameter second-moment cross term: `Cov(C,bar T)` is an explicit finite sum of one-dimensional truncated beta moments through degree four. Consequently the complete mean vector and covariance matrix of `(C,bar T)` are exact for every predeclared symmetric-Dirichlet `alpha`.

`VIS-246` separates nuisance identification from nuisance elimination. Conditioning on the observed concentration `C` does not remove `alpha` when `m>=3`, because a concentration sphere contains configurations with different products and hence different symmetric-Dirichlet likelihood ratios. The exact sufficient coordinate is instead

`Lambda=sum_i log X_i`.

`VIS-247` makes that route explicit rather than formal. On every regular `Lambda=lambda` level, the conditional gap law is the parameter-free coarea measure

`Z(lambda)^(-1) J(X)^(-1) d sigma_lambda`,

with `J^2=sum_i X_i^(-2)-(1/m)(sum_i X_i^(-1))^2`. It also gives an exact three-gap witness showing that `bar T` can vary on a fixed log-product level. Thus exact same-configuration nuisance removal is available and is not structurally forced to erase the tent statistic.

`VIS-248` now closes the low-dimensional deterministic audit target left implicit in that construction. For `m=3`, fixing `P=X_1X_2X_3=p` and quotienting by permutations leaves the single coordinate `Q=X_1X_2+X_2X_3+X_3X_1`. Its exact conditional density is proportional to

`Delta_p(Q)^(-1/2)`,

where `Delta_p(q)=q^2-4q^3-4p-27p^2+18pq` is the cubic discriminant, on the interval between its two positive roots. A cosine reparameterization removes the integrable endpoint singularities and gives stable deterministic one-dimensional quadrature. Any proposed conditional sampler can therefore be audited against an exact full distribution, not merely moment or constraint checks, before high-dimensional use.

The live question is no longer whether the nuisance can be removed in principle or whether a low-dimensional audit target exists. It is whether the frozen high-dimensional critical regime admits an accurate conditional sampler/calibration under that explicit measure, and whether the prime configuration retains a stable residual after the quotient.

## Research question

Fix the critical `lambda` family, midpoint-symmetric taper, phase/coherence tolerance, point-coordinate normalization, width rule, endpoint convention, statistic, and dependence model before confirmation.

For a same-configuration symmetric-Dirichlet calibration, condition on the observed log-product `Lambda` using the exact parameter-free surface law of `VIS-247`; do not estimate `alpha` from the same gaps and then substitute a fixed-parameter null. Under that frozen conditioning rule, does the prime-coordinate `bar T` exhibit a stable residual across increasing scales?

If theory or genuinely held-out information supplies `alpha`, the fixed-parameter route remains valid as a separate predeclared calibration. If endpoints are declared physical signal rather than nuisance, use the post-cut statistic and add the exact endpoint channel from `VIS-241` instead of switching conventions after observing the result.

If a residual survives, can it also survive a stronger predeclared spacing control and then be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The branch has removed forced occupancy, count fluctuation, specified one-point intensity, arbitrary grid origin, support-mismatched label randomization, a nontrivial spacing-dependence axis, arbitrary endpoint cut phase, cyclic-overlap bookkeeping, and the same-sample Dirichlet nuisance parameter itself.

The log-product quotient is stronger than a moment correction: within the symmetric one-parameter Dirichlet family it removes `alpha` exactly from the conditional law. `VIS-247` shows that this quotient need not collapse `bar T`, while `VIS-248` supplies an exact three-gap distributional benchmark for detecting incorrect weighting or sampling of the conditioned measure.

A residual that disappears under the exact conditional law is generic spacing heterogeneity, not prime-specific structure. A residual that survives is still far below an RH result, but it would have passed a materially stronger representation-matched null and would justify asking whether the surviving statistic couples to the signed arithmetic kernel rather than merely to local point geometry.

## Decisive test

Before examining the confirmation residual, freeze all representation choices and the nuisance rule. For the same-configuration route, compute or independently validate the conditional distribution of the predeclared `bar T` under

`P(dX | Lambda=lambda) proportional to J(X)^(-1) d sigma_lambda(X)`

at the observed `m`, `u`, and `lambda`, with numerical/integration/sampling error materially below the proposed residual scale. Do not replace the `J^-1` weight by uniform surface sampling.

Before trusting any production sampler, require it to pass the exact `m=3` audit from `VIS-248` at several predeclared product levels `p`: reproduce the support and normalized CDF of `Q` under the `Delta_p(q)^(-1/2)` law, selected deterministic-quadrature moments/expectations, permutation symmetry, and the correct endpoint mass, while satisfying the simplex and product constraints to tighter tolerance than the eventual error budget. This is a necessary implementation/calibration audit, not evidence that the same algorithm is accurate at large `m`.

Use the differential criterion from `VIS-247` to verify that the actual conditioned regime is not locally degenerate for `bar T`; the three-gap witness proves only that degeneracy is not automatic. Freeze all integration/sampling choices before looking at the prime residual.

If `alpha` is instead supplied by theory or genuinely held-out data, use the exact fixed-parameter center/variance calibration from `VIS-240`--`VIS-243` and propagate whatever uncertainty remains. The concentration statistic `C` from `VIS-244`--`VIS-245` remains useful for model diagnostics but is not an exact same-sample nuisance quotient.

Compare the predeclared prime statistic against the chosen calibration across increasing scales without retuning `alpha`, `ell`, `Lambda` conditioning rules, endpoint convention, or the statistic. Kill the candidate if the anomaly disappears under the frozen dependence calibration; if it depends on Poisson count noise, same-sample intensity flattening, random-cut phase declared to be nuisance, incorrect uniform sampling on a `Lambda` level, same-sample plug-in fitting, or post-hoc tuning; if significance is unstable across the predeclared scale family; or if a stronger representation-matched spacing control reproduces the effect.

Only after a stable residual survives should a new mathematical thread translate it back through the signed prime-phase kernel and audit equivalent formulations in logarithmic prime gaps, short-interval counts, prime-pair/higher-correlation statistics, and critical Dirichlet-polynomial theory.

## Evidence boundary

`VIS-237`--`VIS-241` establish the representation quotients and the symmetric-Dirichlet dependence family. `VIS-242`--`VIS-243` establish the exact fixed-parameter tent variance reduction and deterministic overlap coefficients. `VIS-244` establishes the concentration-based `alpha` identification channel and its variance. `VIS-245` establishes the exact fixed-parameter cross-covariance between that concentration and `bar T`.

`VIS-246` proves that concentration conditioning retains `alpha` for `m>=3` and identifies the log-product as an exact sufficient statistic. `VIS-247` derives the explicit alpha-free coarea law on log-product levels, gives a local gradient criterion for conditioned variation, and proves by an exact three-gap example that `bar T` is not intrinsically collapsed by this quotient. `VIS-248` reduces the `m=3` quotient to the exact discriminant-weighted `Q` interval and gives a nonsingular deterministic quadrature representation for validation.

None of these findings supplies a production high-dimensional conditional sampler, validates that sampler at the actual prime parameters, proves that the one-parameter Dirichlet family is a faithful final model of prime gaps, or reports a prime residual. `VIS-248` is an audit law only; matching it in three dimensions is necessary but not sufficient for high-dimensional correctness. No cited result establishes prime-specific critical separation or any RH consequence.

## Research disposition

The clue remains `accepted`. Same-configuration nuisance elimination is structurally resolved by `VIS-247`, and `VIS-248` now gives an exact low-dimensional distributional benchmark for auditing its implementation. The remaining gate is operational and high-dimensional: obtain or implement an accurate sampler/evaluator for the frozen conditional law, demonstrate that it passes the exact three-gap benchmark before scaling, then test whether the prime statistic has a stable residual. Held-out/theoretical `alpha` remains the independent alternative.