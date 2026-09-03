---
id: CLUE-weil-inertia-higher-zero-correlations-horizontal-rigidity
type: research-clue
status: proposed
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/weil_inertia/findings/WI-001-two-moment-bandwidth-one-barrier.md
  - research/weil_inertia/findings/WI-002-density-one-moment-tower-needs-audit.md
  - research/weil_inertia/findings/WI-043-maximal-pair-discrepancy-does-not-control-locked-four-point-covariance.md
  - research/prior_art/montgomery-pair-correlation.md
---

# Can richer zero correlations turn horizontal information into a stronger critical-line inertia bound?

## Observation

`WI-001` isolates the present information barrier sharply: the first two trace moments with Fourier support one admit explicit extremizers and cannot push the simple-critical-line proportion anywhere near density one. The same finding records a qualitatively different escape route: sufficiently rich correlation information can distinguish on-line multiplicity from horizontal displacement, and the full pair-correlation conjecture in a formulation that does not assume RH would force asymptotically all zeros to be simple and on `Re s = 1/2`.

`WI-002` explores one way of supplying richer information, namely an all-order trace-moment tower, but its required arithmetic transport is not established. Independently, `WI-043` shows that even strong pair-discrepancy control need not determine a locked four-point covariance. Together these boundaries suggest looking on the zero side for observables richer than the current pairwise/second-moment compression, rather than only trying to manufacture higher trace moments from the prime side.

## Research question

Can the non-RH pair-correlation framework be lifted to a finite hierarchy of weighted pair statistics, mixed moments, or genuine `k`-point zero correlations that retain information about the real parts `Re rho`, and can that horizontal information be fed into the Weil-inertia certificate to force a strictly larger proportion of zeros onto `Re s = 1/2`?

The target is not a generic higher-moment inequality. Seek an explicit statistic whose value changes when a positive-density population of zeros is moved horizontally off the critical line while keeping essentially the same ordinate statistics and first-two-moment Weil data. Then derive a quantitative implication of the form: control of that statistic bounds the admissible off-line mass or horizontal-depth distribution, and the resulting bound improves the current simple-critical-line inertia certificate.

## Why it may matter

The present `weil_inertia` obstruction is partly an information-compression problem: shallow off-line pairs and multiple on-line zeros can be indistinguishable at first-two-moment resolution. A zero-correlation observable that is genuinely sensitive to horizontal displacement would attack exactly that degeneracy instead of postprocessing the same compressed matrix data.

This route is also distinct from the unverified density-one moment tower in `WI-002`. It could yield an intermediate unconditional gain from only a small amount of additional correlation information, or identify a precise correlation theorem whose proof would translate immediately into a stronger percentage on the critical line. Even a negative result would be useful if it proves that a broad class of higher zero statistics still collapses to the existing bandwidth-one information budget.

## Decisive test

Choose the lowest-complexity candidate beyond the present pairwise compression and carry out both directions of the audit.

First, construct two matched zero configurations with the same zero count, ordinate density, first two Weil trace moments, and all currently used pairwise data, but with different horizontal off-line mass. Test whether the proposed weighted pair or `k`-point statistic separates them at leading order. If it does not, kill that statistic as a horizontal discriminator.

If it does separate them, derive an explicit deterministic inequality converting its deviation into a bound on off-line mass or horizontal depth and insert that bound into the existing inertia/rank certificate. The clue survives only if the resulting certified simple-critical-line proportion is strictly stronger than the current first-two-moment bound and the needed correlation input is not merely RH, density-one criticality, or an unproved all-order prime-correlation statement in disguise.

A particularly valuable first success would be a finite-order statistic for which a known or realistically attackable unconditional correlation estimate already gives a numerical improvement.

## Evidence boundary

No such horizontal-sensitive statistic or stronger inertia inequality is established here. `WI-001` records that full correlation information can in principle force density one, while `WI-043` shows that pairwise information can fail to control a relevant four-point quantity; neither result proves that a useful finite-order intermediate statistic exists or that it is unconditionally evaluable.

The all-order trace-moment route of `WI-002` remains separately unverified and must not be treated as evidence for this clue. Any candidate whose evaluation silently requires RH, the desired critical-line conclusion, unsupported prime correlations beyond the available Fourier-support regime, or an equivalent restatement of the same missing theorem should be rejected rather than counted as progress.
