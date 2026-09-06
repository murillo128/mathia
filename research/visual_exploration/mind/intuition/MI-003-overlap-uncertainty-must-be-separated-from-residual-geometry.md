# MI-003 — Target uncertainty, control uncertainty, overlap geometry, and residual conditioning must stay separate

**Evidence level:** exact fixed-representation geometry and process-aware/control-only finite-sample interfaces through VIS-060

## Core intuition

A stable geometric residual is not yet a statistically stable observation of that residual, and comparing two residuals does not require assigning the same stochastic semantics to both objects. For overlapping gap blocks, raw-law estimation error, nonlinear closure sensitivity, normalization conditioning, deterministic short-range overlap, genuine long-range dependence, target-side generalization, and control-side Monte Carlo uncertainty are different channels.

For a frozen finite arithmetic table, the cleanest first question is conditional and finite-object: **hold the target fixed, randomize only the matched control, and ask whether the target residual lies outside a rigorously certified control-population ball or cone.** A process model for the target is needed only when the claim is generalized beyond that frozen table.

## Strongest justified principle

VIS-057 proves that adjacent-pair Markov completion is globally Lipschitz in finite-alphabet `L^1`, so any valid raw-law radius propagates deterministically to the Fisher residual and, away from zero residual energy, to normalized orientation.

VIS-058 derives the exact second moment of an empirical overlapping-block law. Dependence enters through collision covariances, with overlap lags explicit and only separated blocks delegated to a justified mixing or other process envelope. VIS-059 identifies the exceptional short lags as finite periodic-cylinder masses; for three gaps they are the constant-run and period-two return channels.

VIS-060 adds the asymmetric inference interface. If the zeta table `Z` is frozen and only a random control estimator `P_hat` approximates a control population `P`, the same deterministic residual map gives exact intervals for `||Delta(Z)-Delta(P)||_H`, residual-energy differences, and signed orientation using only the control-side confidence event. No sampling semantics for `Z` are introduced. The probability statement remains entirely about the independently simulated control.

## What remains possible

A fixed-window zeta/CUE experiment can therefore be tested with substantially fewer assumptions than a population statement about the zeta zeros. The representation and selected window must still be frozen before confirmation, or the confidence construction must cover the selection rule. If a finite-window separation survives fresh matched controls, replication across heights or a justified zeta-side dependence model can then ask whether it generalizes.

Sharper control concentration can replace the coarse second-moment radius without changing the residual geometry. Higher-order block laws can sharpen periodic-cylinder ceilings. Adaptive partition, support, unfolding, closure, and Fisher-reference changes still require their own simultaneous or fresh-sample controls.

## Status / novelty

Conditional-independence completion, empirical-measure covariance, mixing bounds, word periodicity, and Monte Carlo calibration are classical ingredients. The durable synthesis is the modular error architecture: **deterministic target geometry, control simulation uncertainty, target population uncertainty, overlap, long memory, and nonlinear residual conditioning have exact interfaces and should not be collapsed into one effective-sample-size story.**

## Falsification criterion

Invalidate the Markov-completion perturbation bound, the collision-covariance identity, the periodic-cylinder characterization, or VIS-060's fixed-target/control-only residual and orientation intervals under their stated hypotheses. Failure of one finite-window comparison to separate from its control does not falsify the architecture; it means the declared data/representation lack a certified residual difference at that scale.
