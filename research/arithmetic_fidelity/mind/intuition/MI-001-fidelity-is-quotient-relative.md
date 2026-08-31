# MI-001 — Fidelity is quotient-relative, and admissible information loss is irreversible

**Evidence level:** supported by exact deterministic, invariant, smooth, and stochastic models

## Core intuition

A compression should be audited through the indistinguishability relation it imposes on the discriminator that matters. In the exact models developed in this line, recoverability is not a vague function of rank or dimension: the discriminator must be constant on the relevant fibers. Once two conflicting states have been identified and no new admissible information is introduced, downstream processing cannot separate them again.

## Strongest justified principle

AF-001 gives the deterministic core: for `T:X→Y`, exact recovery of `d` through `T` is equivalent to `d` being constant on every `T`-fiber, and any further deterministic map only coarsens that partition. AF-003 upgrades this to a constrained observable library: the joint map of all admissible observables is the maximal admissible quotient, so the right question is whether `d` factors through that quotient rather than whether one can invent some arbitrary faithful mark.

The same principle appears in different categories without becoming one category-free theorem. AF-007 gives a first-order smooth obstruction through the vertical rank of `dD|ker dT`; AF-009 identifies conditional variance as the exact `L²` prediction defect and proves monotonicity under garbling; AF-011 gives the zero-error analogue through support-confusability. Each version formalizes an information boundary appropriate to its own category.

The important qualification is AF-001's target-leakage warning. On a finite set, an unconstrained auxiliary mark can always encode the missing discriminator. A mathematically meaningful repair must therefore specify admissibility — naturality, equivariance, locality, a fixed observable family, or another independently forced restriction — before asking for minimal additional information.

## What remains possible

A lossy quotient can still be sufficient for one arithmetic predicate even when it does not reconstruct the full input. Conversely, a large or injective representation is not automatically useful if its extra coordinates are target-leaking or classically determined. The live problem is to characterize the smallest **admissible** quotient on which the intended discriminator becomes well defined.

## Status / novelty

The fiberwise, maximal-observable, smooth-rank, conditional-variance, and support-confusability statements are persisted exact findings or standard-category consequences specialized here. Their organization as a reusable Mathia fidelity gate is a supported synthesis.

## Falsification criterion

Exhibit a pipeline in one of the audited categories where two states remain indistinguishable under every admissible observable entering the downstream construction, the discriminator differs on those states, yet a later deterministic or admissible stochastic stage recovers it without receiving new information. That would contradict the corresponding persisted fidelity theorem.

## Lean-formalizable core

- Fiberwise factorization criterion and monotonicity under post-composition.
- Maximal admissible observable quotient.
- Conflict-hypergraph formulation for finite observable libraries.
- Support-confusability zero-error criterion.
