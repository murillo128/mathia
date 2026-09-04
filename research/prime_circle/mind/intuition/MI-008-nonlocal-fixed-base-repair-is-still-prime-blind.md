# MI-008 — Fixed-base one-hole harmonic and Feshbach repair remains prime-blind after provenance is lost

**Evidence level:** proved for the fixed-base one-hole family through PC-164

## Core intuition

Nonlocality and energy dependence are not new arithmetic information channels by themselves. At fixed base conductor, the one-hole new-prime defect classicalizes along the full coprime family before elimination. Schur/Kron reduction can make the survivor interaction all-to-all, and an energy-dependent Feshbach map can retain the entire finite spectral parameter, but both remain deterministic post-processings of the same prime-blind complete-fiber/Bloch data.

The ordering principle is therefore stronger than before: **couple provenance before fixed-base puncture classicalization or before eliminating the old section**. Once that stage has identified prime and matched composite refinements, neither zero-energy nor energy-dependent harmonic response recreates primality.

## Strongest justified principle

PC-161 proves `l1` convergence of the complete positive one-hole defect spectrum, along every coprime fiber size, to inverse-square star blocks determined only by the base residue mask. Prime refinements are one subsequence of this matched composite family.

PC-162 applies canonical Schur/Kron elimination. The positive all-to-all correction converges in trace norm to a fixed-base star-mesh limit whose Fredholm determinant is expressible through fixed-base cyclotomic/hyperbolic data.

PC-163 closes the most natural scalar joint escape that still retained the ambient shell. Matrix-tree plus Schur complementation gives the exact full Kron pseudodeterminant as the ambient complete-fiber determinant divided by the old-section determinant. The ambient factor is a cyclic sampling of one fixed Bloch polynomial, and its universal `+log m` term comes from the translational zero mode at the Bloch endpoints. The same formula holds for every coprime composite fiber size.

PC-164 extends the closure to spectral energy. The full Feshbach determinant is exactly

`det(M_{d,m}-E I) / det(G_{d,m}-E I)`,

hence a product of the same fixed-base Bloch characteristic polynomial over the cyclic grid divided by a fixed-size old-block polynomial. Its divisor is real and prime-blind, and the operator-valued self-energy has the corresponding fixed-base trace-class/cyclotomic limit. Energy-dependent elimination therefore does not reveal a hidden new-prime spectral divisor.

## What remains possible

The theorem does not cover simultaneous growth of the base conductor, genuine multi-hole geometry, cross-level transport, noncommuting provenance-sensitive couplings, or operations applied before the one-hole quotient forms. Those are the remaining places where new-prime information could still enter.

## Status / novelty

Schur complements, Feshbach maps, matrix-tree identities, Bloch decomposition, trace ideals, and determinant quotients are classical. The project-specific result is the exact fixed-base matched-coprime classicalization across defect spectrum, zero-energy nonlocal response, full Kron determinant, and energy-dependent Feshbach family.

## Falsification criterion

Exhibit a canonical fixed-base one-hole invariant built from the persisted defect/old-section data whose value or divisor distinguishes prime from matched coprime composite refinements. A survivor must use information not contained in the complete one-hole Bloch/Feshbach response.

## Lean-formalizable core

- Trace-norm star limit.
- Schur/Feshbach determinant quotient.
- Matrix-tree pseudodeterminant identity.
- Logical monotonicity of information under deterministic elimination.
