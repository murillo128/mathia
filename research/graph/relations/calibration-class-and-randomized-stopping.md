---
id: RG-calibration-class-and-randomized-stopping
type: research-graph-relation
scope: arithmetic_fidelity-xi_flow
derived: true
---

# Calibration class and randomized stopping

This projects the explicit AF-to-Jacobi transfer in XF-204 and the function-class boundary in [[research/mind/intuition/MI-039-calibration-gluing-transfers-randomized-stopping-bounds-only-in-the-admitted-function-class|global MI-039]]. The common mechanism has different admissibility proofs and noise assumptions in the two lines.

## A fixed pair before the seed

[[research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth|AF-575]] supplies finite exact stopping on each noiseless input with unknown strictly subcritical derivative calibration. [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]], equations (6)–(15), upgrades its finite-prefix obstruction to a randomized theorem: two fixed admissible inputs agree with the midpoint outside a shrinking interval near the excluded endpoint. For any capped adaptive policy, the probability of entering that interval tends to zero. The pair is selected after the policy and cap, before its seed.

[[research/xi_flow/findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail|XF-204]], equations (7)–(17), explicitly transfers that coupling question but must preserve the queryable endpoint of a complex response. Its convex-velocity join matches both the endpoint value and the tail's value and derivative while retaining strict derivative slack. [[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]], equations (6)–(11), supplies the strict speed decrease for the complete response, including the reciprocal term. [[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]], equations (8)–(12), supplies the pointwise finite certificate under one known total squared-noise budget.

In each binary experiment the capped minimax error is \(1/2\). Truncation and fair guessing give the sharp worst-case stopping tail \(1-2\alpha\) for error allowance \(\alpha<1/2\), despite finite cost at every input for an attaining policy. The worst-case input may change with the cap. These are explicit applications of [[research/prior_art/incremental/PA-le-cam-two-point-testing|classical two-point testing]], not a new general testing principle.

## Polynomial calibration changes the experiment

[[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]], equations (2)–(6), assumes a known finite family of real-analytic sources with nonpolynomial pairwise gaps and one polynomial nuisance of unknown finite, unbounded degree. Every finite deterministic transcript has another-label extension. Yet one continuously random exact validation coordinate, independent of all fitted interpolants, rejects every false analytic residual almost surely for each fixed input; degree \(d\) needs at most \(d+2\) observations, taking \(d=0\) for zero calibration. The interpolation-and-validation idea has [[research/prior_art/incremental/PA-polynomial-interpolation-early-termination|classical early-termination prior art]].

AF-577 separately proves that finite-bit zero-error stopping is impossible and that every positive uniform noise margin vanishes. It does not give a sharp capped minimax law for the polynomial class. Its result is a distinction from AF-576, not a refutation: smooth interval-gluing witnesses need not be polynomial or analytic. Conversely, analyticity of the sources does not grant continuous-real randomness or exact comparisons. The local syntheses [[research/arithmetic_fidelity/mind/intuition/MI-079-unknown-polynomial-calibration-separates-random-identification-from-certification|AF MI-079]] and [[research/xi_flow/mind/intuition/MI-014-endpoint-preserving-calibration-joins-force-sharp-randomized-stopping-tails|Xi MI-014]] retain these separate interfaces.

## Limits of the bridge

The AF derivative slack convention is twice the Xi convention after identifying the critical derivative magnitude. AF-575's positive supremum-noise obstruction does not transfer to Xi's total squared-noise model. Neither source supplies physical Xi access, ordinary-prime identification, or an RH implication. There is no proved classification of all analytic or quasianalytic calibration classes. The direct AF-576-to-XF-204 relation is supported by XF-204's explicit transfer passage, independently of their shared prior-art citation.
