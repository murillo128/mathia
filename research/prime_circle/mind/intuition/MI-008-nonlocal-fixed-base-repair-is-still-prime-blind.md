# MI-008 — Nonlocal harmonic elimination does not restore provenance after fixed-base puncture classicalization

**Evidence level:** proved for the one-hole fixed-base family in PC-161--PC-162

## Core intuition

Nonlocality is not itself a new arithmetic information channel. At fixed base conductor, the one-hole new-prime defect first localizes to a prime-blind trace-class star spectrum; integrating the deleted vertices out by the canonical Schur/Kron response makes the survivor interaction all-to-all, but the complete response still converges to the same coprime prime-blind limit.

The important ordering principle is therefore **couple provenance before classicalization**. Once the fixed-base puncture has collapsed to its universal star data, canonical harmonic elimination can redistribute that data nonlocally but cannot recreate whether the refining fiber was prime.

## Strongest justified principle

PC-161 proves `l1` convergence of the complete positive defect spectrum, along every coprime fiber size, to a direct sum of inverse-square weighted stars determined only by the base residue mask. Prime refinements are just one subsequence of a matched composite family.

PC-162 applies the canonical nonlocal repair. Schur/Kron elimination of the deleted old section yields a positive trace-class all-to-all star-mesh correction and converges in trace norm to a fixed-base limit along the same full coprime family. For each limiting block,

`det(I+z C_a)=F_a'(z)/F_a'(0)`,

where `F_a` is an explicit inverse-square edge product expressible through fixed-base cyclotomic/hyperbolic data. Its zeros are real negative. The nonlocal Fredholm object is therefore a classicalized response to the same prime-blind input, not a restored new-prime divisor.

## What remains possible

The result does not classify joint eigenvector geometry between the ambient prime shell and the defect, simultaneous growth of the base conductor, genuine multi-hole structure, cross-level noncommuting couplings, or operations applied before the fixed-base limit. Those are the places where provenance could still enter.

## Status / novelty

Schur complements, Kron reduction, trace ideals, weighted stars, and Fredholm determinant lemmas are classical. The project-specific theorem is the fixed-base matched coprime limit and its explicit determinant classicalization.

## Falsification criterion

Exhibit a canonical fixed-base one-hole invariant built from the PC-161 defect and its harmonic elimination that has different limiting value on prime and matched composite coprime refinements. A survivor must use information not contained in that complete limiting response.

## Lean-formalizable core

- Trace-norm star limit.
- Schur complement continuity with fixed eliminated dimension.
- Rank-one determinant derivative identity.
- Logical monotonicity of information under deterministic post-processing.
