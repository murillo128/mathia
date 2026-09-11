# MI-024 — Periodic completeness turns Li cancellation into profinite leakage

**Evidence level:** proved

## Core intuition

Sparse root-rate fidelity depends on the admissible output sampler, not only on how well a phase can be approximated globally. For one conjugate Li mode, arbitrary unbounded sampling is governed by the strongest half-integer approximation events. Requiring the sampler to revisit every residue class modulo every integer changes the quantifiers: catastrophic approximation matters only if exponential cancellation leaks into **every** profinite cylinder strongly enough to survive that coverage obligation.

The correct constrained currency is therefore a congruence-uniform cancellation exponent, not the ambient irrationality exponent.

## Strongest justified claim

AF-257 proves for `F_{alpha,m}(n)=-2m cos(pi n alpha)` that the worst root-rate loss over all unbounded retained sets is exactly controlled by

`kappa_{1/2}(alpha)=2 limsup_{q_j even} log(q_{j+1})/q_j`,

where `q_j` are continued-fraction denominators. For an off-critical pair with radial factor `q_rho>1`, arbitrary sparse sampling preserves a strictly superunit pair rate exactly when this parity-filtered exponent is below `log q_rho`.

AF-258 imposes periodic completeness and obtains the exact replacement

`K_pc(alpha)=inf_M min_r K_{M,r}(alpha)`.

The worst periodically complete pair rate is `q_rho exp(-K_pc(alpha))`. In particular, one congruence cylinder with subexponential half-integer cancellation forces `K_pc=0` and hence full pair-rate fidelity for **every** periodically complete sampler. AF-258 constructs the sharp separation `kappa_{1/2}=+infinity` but `K_pc=0`.

AF-259 then classifies each `K_{M,r}` by even principal convergents and odd multipliers. A dangerous event at denominator `q_j` reaches sample index `g q_j/2`; the residue class is changed by `g`, while the cancellation exponent is diluted by essentially `1/g`. At any fixed positive margin only bounded odd multipliers can contribute.

## Synthesis of evidence

These findings show that output coverage acts like an information-preserving topology on sparse observation. Ambient super-Liouville behavior can be harmless when its strongest events are trapped in a proper profinite region, whereas much weaker ambient approximation can still be dangerous if it is distributed uniformly enough across congruence cylinders.

This is an exact two-mode theorem and therefore a reusable control for broader Li/root-rate proposals: a source theorem should be matched to the actual sampler class before demanding global Diophantine regularity.

## Counterevidence / boundary cases

The classification is for one conjugate two-mode signal. Several comparable off-critical modes can cancel on higher-dimensional affine resonance fibers, where one safe one-dimensional congruence cylinder need not control the full sum. Periodic completeness also does not cover arbitrary zero-density samplers with weaker or different combinatorial coverage constraints.

The formulas classify what must be proved for the actual Keiper phase; they do not establish the required continued-fraction distribution for zeta zeros.

## Epistemic status

**Exact two-mode classification:** arbitrary sparse fidelity is governed by the parity-filtered ambient exponent, while periodically complete fidelity is governed by profinite distribution of the dangerous convergents and their odd-multiplier leakage.

## Novelty/prior-art status

AF-257--AF-259 explicitly separate classical continued-fraction ingredients from the derived Mathia sampling formulas and make no broad novelty claim. This intuition inherits that boundary.

## Falsification criterion

Produce a periodically complete retained set whose two-mode root-rate is below `exp(-K_pc(alpha))`, or an admissible congruence-cylinder cancellation sequence not captured by the even-convergent/odd-multiplier formula of AF-259. Either would invalidate the profinite classification.

## Lean-formalizable core

The finite quantifier skeleton behind AF-258 is a natural formal target: given cylinderwise limsup bounds, construct a periodically complete diagonal set attaining the infimum up to an arbitrary epsilon, and prove the converse cylinder restriction bound. The continued-fraction asymptotic identification in AF-259 is a separate analytic formalization problem.
