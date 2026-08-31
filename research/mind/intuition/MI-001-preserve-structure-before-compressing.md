# MI-001 — Preserve the discriminating structure before compressing

**Evidence level:** supported, with exact transversal fidelity theorems in several categories

## Core intuition

Across Mathia, the recurring failure is not “spectralization,” “positivity,” or “taking a scalar” in the abstract. It is applying a transformation whose induced indistinguishability relation already identifies states that the later arithmetic claim needs to distinguish. The new Arithmetic Fidelity line turns this from a methodological slogan into exact model theorems: recoverability is fiberwise, admissible observables define a maximal quotient, and deterministic post-processing or stochastic garbling cannot recreate information absent from that quotient.

## Strongest current principle

Arithmetic Fidelity supplies the transversal formal core. AF-001 proves `d=r∘T` exactly when `d` is constant on `T`-fibers; AF-003 says the joint map of all admissible observables is the maximal quotient available to a constrained repair; AF-011 gives the zero-error support-confusability analogue. AF-002/AF-005 also show why “add more features” is not enough: the meaningful question is whether a canonically allowed family hits every discriminator conflict, including finite aliases invisible to rank. Unconstrained marks can simply leak the target and are mathematically vacuous.

The branch evidence then instantiates different failure modes. Prime Circle now has a genuinely nonlocal Hardy lift, yet every finite mixed essential algebra is only a wedge of universal Hilbert bands; arithmetic remains in trace-class relative data. Prime Flute has an even stronger matched control: PF-125 proves the exact prime flute and the all-composite `p_n+1` clone are compact-resolvent equivalent, so essential spectrum has already identified the prime/non-prime distinction. Prime Lattice repeatedly shows that generator/boundary compressions can be target-blind or topology-dependent. Weil Inertia separates optimization loss from a locally centered super-polylogarithmic alias obstruction. Weil Positivity shows that exact selectors can survive positive finite geometry while disappearing only when one passes to a radial reduction, principal class, or torsion-forgetting real pairing.

These are different theorems, not one universal category-free statement. Together they support a precise workflow:

\[
\boxed{\text{derive the admissible observable class} \to \text{compute its fibers} \to \text{only then optimize, spectralize, or prove positivity}.}
\]

## Positive examples

Compression can be repaired when the extra relation is canonical. AF-004's bispectrum restores finite-abelian signals modulo translation; AF-005 gives an exact annihilator-lattice criterion for monomial phase lifts; AF-006 shows that full marked eigenspace Gram data can classify what diagonal spectral measures lose. Prime-Flute marked Weyl/spectral data similarly retain ordered finite-neck memory that scalar determinants erase.

## Evidence against overgeneralization

Full input reconstruction is unnecessary if the desired predicate already factors through the quotient. Conversely, high rank, injective labels, a positive determinant, or an exact selector does not establish RH relevance. The relevant audit is always relative to the claimed discriminator and the admissibility constraints on information that may be added.

## Status / novelty

The fiberwise and category-specific fidelity results are persisted evidence; their use as a cross-branch order-of-operations principle is a supported synthesis.

## Falsification criterion

Find a canonical pipeline where the target discriminator varies inside the maximal admissible fiber at some stage, no later stage receives new admissible information, yet the final invariant recovers the discriminator. Within the audited deterministic/stochastic models this would contradict the persisted fidelity results.

## Lean-formalizable core

- Fiberwise factorization and post-processing monotonicity.
- Maximal admissible quotient and finite conflict hitting sets.
- Support-confusability monotonicity under garbling.
- Exact relational-lift examples via annihilator lattices and marked Gram data.
