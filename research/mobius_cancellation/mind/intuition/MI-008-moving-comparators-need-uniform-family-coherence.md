# MI-008 — Moving comparators need coherent turnover and a transfer budget stronger than constant-defect imitation

**Evidence level:** supported by MC-053--MC-064; the fixed-class transfers, conductor repulsion, and Burgess/square-divisor transfer bounds are theorem-level in their stated hypotheses

## Core intuition

Allowing a comparator to depend on observation scale is a real escape from fixed-comparator transfer theorems, but finite-prefix agreement plus a good exponent for each frozen object is too weak. The missing resource is a **uniform, scale-coherent cancellation certificate whose fidelity actually decays at the power rate required by the target transfer**.

Quadratic characters make this boundary rigid in two independent ways. Good subquadratic fits cannot turn over freely from one nearby scale to the next, and the direct Burgess/square-divisor transfer itself has a method-specific exponent floor. Constant-defect imitation may force conductor geometry without yet transporting a power saving for Mertens.

## Strongest justified principle

MC-053--MC-061 establish the earlier family gate: fixed comparator classes transfer exponents; exact and weighted character imitation forces conductor growth; competing quadratic fits have product-conductor repulsion; and even one good quadratic fit forces a large twisted-Möbius uniformity cost.

MC-062 converts pair repulsion into scale sparsity. For any fixed defect below one half and subquadratic conductor window `X<q<=X^kappa`, `kappa<2`, two good certificates at nearby bounded-ratio scales must use the same conductor. Thus a fresh good character cannot exist at every multiplicative scale.

MC-063 strengthens this to power separation: distinct good certificates at scales `X<=Y` satisfy a lower bound of the form `Y >> X^(4/kappa-1-o(1))`. For `kappa<2` the turnover exponent is superlinear, so only very sparse fresh identities can occur along a long scale range.

MC-064 adds the transfer audit. A weighted quadratic defect `A_X(chi)` gives

`|M(X)| <= X A_X(chi) + X^(1/2) q^(3/16)`

up to logarithmic factors in the stated squarefree setting. Because exact fidelity already forces `q>X`, this direct route cannot beat the method-specific exponent `11/16`; obtaining a target exponent `theta` additionally requires `A_X(chi)` to decay like `X^(theta-1)` and constrains the conductor accordingly. In the subquadratic regime needed below `7/8`, the MC-062--MC-063 turnover rigidity is therefore unavoidable.

## What remains possible

A moving-comparator proof must derive a source-forced family whose defects decay at the required polynomial rate, whose conductors lie in the transfer-compatible window, and whose identities can remain coherent across the scales needed for the final Mertens estimate. A different comparator category may evade the character-specific exponents, but it must expose an independently bounded replacement/complexity resource rather than hide cancellation in the moving certificate.

## Status / novelty

The transfer mechanisms, character interpolation, Burgess bounds, reciprocity, and square-divisor identities are classical or literature-backed. The synthesis is the two-resource gate: **moving fidelity must be strong enough for the transfer and coherent enough across scale; constant-defect per-scale approximation supplies neither conclusion by itself**.

## Falsification criterion

Construct a scale-dependent comparator family with power-decaying Möbius defect, transfer-compatible complexity, and uniform inter-scale coverage whose total hypotheses are provably weaker than the Mertens exponent obtained, or invalidate one of the stated conductor/turnover/transfer bounds under its hypotheses.

## Lean-formalizable core

- Character-prefix conductor lower bounds.
- Product-conductor and scale-turnover repulsion.
- Quadratic defect to twisted/Mertens transfer inequality.
- Separation between constant-defect sparsity and power-decaying transfer fidelity.
