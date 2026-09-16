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
  - research/visual_exploration/findings/VIS-249-three-coordinate-log-product-gibbs-kernel.md
  - research/visual_exploration/findings/VIS-250-triple-gibbs-global-accessibility.md
  - research/visual_exploration/findings/VIS-251-uniform-triple-gibbs-escapes-dominant-labels.md
  - research/visual_exploration/findings/VIS-252-uniform-triple-gibbs-linear-eigenmode.md
---

# Is there prime-specific critical pair geometry after exact log-product nuisance calibration?

## Observation

The critical coherence-cell branch has progressively removed representation and null-model confounds. `VIS-237`--`VIS-243` remove arbitrary grid origin, Poisson count noise, specified one-point intensity, endpoint-cut phase, and cyclic-overlap bookkeeping while replacing support-mismatched controls by a symmetric fixed-count Dirichlet spacing family. `VIS-244`--`VIS-246` then separate nuisance identification from nuisance elimination: the concentration statistic identifies `alpha`, but conditioning on it does not remove `alpha`; the exact sufficient coordinate is instead

`Lambda=sum_i log X_i`.

`VIS-247` derives the exact same-configuration conditional law on every regular log-product level,

`P(dX | Lambda=lambda) proportional to J(X)^(-1) d sigma_lambda(X)`,

with `J^2=sum_i X_i^(-2)-(1/m)(sum_i X_i^(-1))^2`, and proves that the tent statistic need not collapse on such a level. `VIS-248` reduces the three-gap case to the exact discriminant-weighted law

`f(Q=q | P=p) proportional to Delta_p(q)^(-1/2)`

on a known interval, giving a deterministic full-distribution audit target for any numerical implementation.

`VIS-249` removes the abstract sampler-existence gap. Conditional on all but any three coordinates, the remaining block sum and product are fixed, so after scaling that block its exact full conditional is precisely the `VIS-248` three-gap law. Random-scan exact heat-bath updates over coordinate triples are reversible for the `VIS-247` target, and the infinitesimal directions supplied by the triple moves span the whole regular tangent space.

`VIS-250` closes the corresponding global communication question for the exact kernel. Every regular log-product level is connected, the admissible triple-fiber flows form a single global accessibility class, and the exact positive-weight random-scan heat-bath chain is `mu_lambda`-irreducible. Thus a disconnected exact support or hidden communication class cannot explain a failure of calibration.

`VIS-251` then removes a visually natural metastability story: inside a strongly dominant-coordinate cone, uniform triple Gibbs updates change the identity of the dominant label at exact rate `2/m`, independently of `lambda`. `VIS-252` supplies the first global quantitative calibration scale. Under uniform triple scanning every centered coordinate, and hence every coordinate contrast, is an exact eigenfunction with

`rho_m=(m-3)/(m-1)`,

so the chain has `gap(P)<=2/(m-1)` and every nondegenerate coordinate contrast has exact stationary autocorrelation `rho_m^t` and integrated autocorrelation time `m-2` in individual triple updates.

The live question is now purely quantitative and discriminating: whether a frozen implementation of that exact kernel realizes these exact low-order benchmarks and mixes the nonlinear `bar T`-relevant geometry adequately at the actual high-dimensional critical parameters, and whether the prime configuration retains a stable residual after that calibration.

## Research question

Fix the critical `lambda` family, midpoint-symmetric taper, phase/coherence tolerance, point-coordinate normalization, width rule, endpoint convention, statistic, triple-selection rule, and numerical block-sampling method before examining the confirmation residual.

Under the exact same-configuration log-product quotient, does the prime-coordinate `bar T` exhibit a stable residual across increasing scales after calibration with the `VIS-249` random-scan three-coordinate Gibbs kernel?

If a residual survives, can it also survive a stronger predeclared spacing control and then be translated into a lower bound, obstruction, or structural constraint for the signed prime-phase quadratic energy rather than remaining a generic point-process anomaly?

## Why it may matter

The log-product quotient is stronger than moment fitting: within the symmetric one-parameter Dirichlet family it removes `alpha` exactly. `VIS-247` gives the target measure, `VIS-248` gives an exact low-dimensional distributional benchmark, `VIS-249` gives an exact block-conditional Markov kernel with full local tangent rank, `VIS-250` removes the disconnected-support/global-communication ambiguity, `VIS-251` excludes a dominant-label barrier whose rate worsens with the conditioned level, and `VIS-252` gives an exact target-independent linear relaxation benchmark for the implemented chain.

A residual that disappears under this calibration is generic spacing heterogeneity within the admitted null, not prime-specific structure. A residual that survives is still far below an RH result, but it would have passed a materially stronger representation-matched nuisance quotient and would justify asking whether the surviving statistic couples to the signed arithmetic kernel rather than merely to local point geometry.

## Decisive test

Before using prime data as a confirmation target, implement the `VIS-249` block kernel with a uniform state-independent unordered-triple scan. For each selected block, preserve its exact sum and product, sample the normalized `Q` coordinate from the `VIS-248` discriminant law, reconstruct the cubic roots, assign labels symmetrically, and verify the constraints to tolerance materially below the final statistic error budget.

First require the one-block implementation to reproduce the exact `m=3` support and normalized CDF of `Q` at several predeclared product levels, together with selected deterministic-quadrature expectations, permutation symmetry, and endpoint mass. Then require the high-dimensional implementation to reproduce the exact `VIS-252` linear benchmark before interpreting any nonlinear statistic: empirical coordinate-contrast lag correlations must agree with `rho_m^t`, with `rho_m=(m-3)/(m-1)`, and the estimated integrated autocorrelation time must agree with `m-2` within the declared Monte Carlo tolerance when time is measured in individual triple updates.

After that mandatory check, at the actual high-dimensional `m` and `lambda`, test stationarity and mixing from deliberately separated admissible starting configurations using `bar T` and additional nonlinear within-level observables. `VIS-250` establishes exact irreducibility only, `VIS-251` excludes one label bottleneck only, and `VIS-252` supplies one exact eigenmode only; none of them gives the full spectral gap, conductance, practical burn-in, or protection against a slower nonlinear mode or a numerically distorted implementation.

Freeze burn-in, retained-sample count, thinning if any, convergence diagnostics, numerical CDF/root tolerances, and the final `bar T` comparison rule before examining the prime residual. Require Monte Carlo and numerical uncertainty to be materially below the residual scale. Kill the candidate if the exact low-dimensional or linear benchmarks fail, if different valid initializations do not converge to the same calibrated nonlinear law within the declared budget, if the residual disappears under the exact quotient, if the result depends on post-hoc tuning, or if a stronger representation-matched spacing control reproduces it.

If `alpha` is supplied by theory or genuinely held-out data, the exact fixed-parameter route from `VIS-240`--`VIS-245` remains a separate valid calibration. The concentration statistic `C` is useful for diagnostics but is not an exact same-sample nuisance quotient.

Only after a stable residual survives should a separate mathematical thread translate it back through the signed prime-phase kernel and audit equivalent formulations in logarithmic prime gaps, short-interval counts, prime-pair/higher-correlation statistics, and critical Dirichlet-polynomial theory.

## Evidence boundary

`VIS-246` identifies the log product as the exact sufficient statistic for the symmetric-Dirichlet nuisance. `VIS-247` derives the alpha-free coarea target and proves nondegeneracy of the tent statistic on at least one product level. `VIS-248` supplies the exact three-gap quotient distribution used as a deterministic implementation audit. `VIS-249` proves that these three-gap conditionals assemble into reversible random-scan block Gibbs kernels for the full conditioned law and that their local directions span the regular tangent space. `VIS-250` proves connectedness of the regular support, one global triple-flow accessibility class, and `mu_lambda`-irreducibility of the exact positive-weight triple heat-bath chain. `VIS-251` proves the exact `2/m` dominant-label switching law on its stated cone. `VIS-252` proves the exact uniform-scan coordinate eigenvalue, the resulting spectral-gap upper bound, and the coordinate-contrast autocorrelation benchmark.

None of these results proves the full spectral gap, a useful high-dimensional mixing time for `bar T`, floating-point implementation accuracy, fidelity of the one-parameter Dirichlet family as a final prime-gap model, a prime residual, or any RH consequence. The `m-2` integrated autocorrelation time is exact only for the displayed linear eigenfunctions; a slower nonlinear conditioned mode may still control the operational calibration budget.

## Research disposition

The clue remains `accepted`. The structural sampler problem is closed through exact conditionals, reversibility, tangent spanning, connected support, and global irreducibility, and the simplest linear relaxation channel now has an exact calibration target. The remaining gate is operational and high-dimensional: implement and validate the frozen kernel against both the exact `VIS-248` block law and the exact `VIS-252` autocorrelation law, establish adequate convergence/error control for nonlinear observables at the actual conditioned parameters, and only then test whether the prime statistic has a stable residual.
