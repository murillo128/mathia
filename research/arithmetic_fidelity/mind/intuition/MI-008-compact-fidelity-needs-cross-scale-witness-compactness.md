# MI-008 — Compact-target fidelity requires witnesses that do not escape across scale

**Evidence level:** proved for the compact-target cone families and bounded witness pools covered by AF-069--AF-075

## Core intuition

At finite resolution, every requested consequence can have an excellent finite witness while the infinite-resolution claim still fails. What matters for compact targets is not merely approximation accuracy at each scale but **cross-scale non-escape of the witnessing directions**.

The exact invariant can be expressed equivalently as a compact-transversal margin, a coherent finite approximant tower, a precompact pooled witness set, or decay of Kolmogorov widths. This converts an apparently qualitative infinite-presentation issue into a quantitative compactness/fidelity gate.

## Strongest justified principle

AF-069--AF-070 show that for compact targets, downward-directed closed cone families can acquire consequences that are absent at every finite stage. In finite dimension this is measured by zero normalized excess from the retained cone family to the candidate consequence.

AF-071 identifies the precise limitation of that scalar excess: in infinite dimension the implication can hold even when normalized excess is maximal because witness directions escape every compact set. The finite-dimensional converse is recovered exactly when the collective unit-direction family is precompact.

AF-072 replaces normalized excess by the intrinsic compact-transversal margin. A cone is a compact-target consequence exactly when every compact unit-direction transversal meets it, equivalently when this margin vanishes.

AF-073--AF-074 turn the criterion into finite data. The same condition is equivalent to the existence of coherent finite approximants with summable cross-scale motion, and also to arbitrarily accurate finite witness pools whose **entire union is precompact**. Arbitrarily good but unrelated approximants at successive scales do not suffice.

AF-075 gives the quantitative Hilbert/Banach diagnostic: bounded pooled witness sets are precompact exactly when their Kolmogorov widths tend to zero. In Hilbert language, this is uniform finite-rank tail control. The standard orthonormal sequence is the sharp control: every stage has a one-point finite witness, but the pooled widths stay equal to one.

## What remains possible

For an arithmetic limit construction, a finite-rank or finite-complexity explanation at every cutoff is not evidence of a stable limiting discriminator unless the witness family has a source-natural compactness mechanism. A positive route should derive uniform width decay, a compact transversal, or an equivalent coherent approximation theorem from the arithmetic representation itself.

This criterion is especially relevant when a proposed invariant is recovered from growing windows, increasing interaction degree, or increasingly fine refinements. The question is not only whether every finite target can be approximated, but whether the required information can be carried by one non-escaping family as the scale grows.

## Status / novelty

Compactness, Kolmogorov widths, and finite-dimensional approximation theory are classical. The persisted synthesis is their role as an exact fidelity test for infinite-resolution witness systems: **per-scale success is weaker than compact-target fidelity; cross-scale compactness is the missing resource**.

## Falsification criterion

Produce a compact-target consequence in the covered cone setting with positive compact-transversal margin, or a bounded pooled witness family with vanishing Kolmogorov widths that is not precompact. For an arithmetic application, show that a proposed per-scale witness scheme remains faithful despite a pooled family that escapes every compact set.

## Lean-formalizable core

- Compact-transversal margin equivalence.
- Coherent finite approximant tower criterion.
- Pooled precompact witness criterion.
- Kolmogorov-width characterization of precompactness.