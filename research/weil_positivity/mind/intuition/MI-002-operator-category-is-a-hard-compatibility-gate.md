# MI-002 — Operator category is a hard compatibility gate for cross-branch positivity

**Evidence level:** proved for the audited Prime-Flute/Prime-Lattice comparison; supported as a broader gate

## Core intuition

Two constructions can carry closely related arithmetic-looking kernels and still be unable to represent the same positive operator because they live in incompatible operator ideals. The newer boundary-response evidence adds a second gate: even a category-changing passage is not enough if the operation reaches the critical spectral regime only by losing self-adjoint positivity. A viable bridge must change operator category **and** carry an independent sign theorem at the destination.

## Strongest justified principle

WP-014 compares the canonical exact Prime-Flute Schiffer compression from PF-085 with the exact positive finite-Weil operator isolated in WP-004. The Schiffer cell operator is trace class, so its absolute value, square, bounded congruences, and bounded compressions remain trace class or better. The finite-Weil operator with prime-power weights satisfies

\[
T\in S_q\iff q>2,
\]

and is not Hilbert--Schmidt. Bounded coordinate changes therefore cannot bridge the two.

WP-015 tests the most natural singular/boundary escape. Prime-Flute zero-energy DtN is genuinely positive, but its spectral continuation loses real positivity immediately; on the critical scattering line the outgoing response is non-Hermitian because of universal cusp flux. Feshbach reduction retains marked information through a resolvent, but the resolvent changes sign/poles across the positive spectrum rather than inheriting a Weil-type order theorem.

The combined gate is stronger than ideal mismatch alone:

\[
\boxed{
\text{soft trace-class geometry}
\to\text{category-changing operation}
\to\text{critical-scale arithmetic operator}
}
\]

is useful only if the middle arrow is geometrically forced **and** the final object has a sign theorem not borrowed from the positive source after that sign has already been lost.

## What remains possible

Unbounded weighting, singular boundary maps, relative/noncompact scattering, cohomological quotients, noncommuting insertions, or determinant-line constructions can cross Schatten boundaries. Boundary asymmetry and eta-type data can also retain information that a positive square forgets. None is ruled out categorically.

The requirement is that the category change itself be canonical, survive matched controls, and produce both the required slower arithmetic tail and an independent sign/order statement. Choosing a singular weight to reproduce Mangoldt coefficients, or invoking ordinary DtN positivity after continuation has destroyed it, does not meet that requirement.

## Status / novelty

Trace-ideal closure and boundary/Weyl theory are standard. The project-specific evidence is the exact placement of the Mathia operators on opposite sides of the Hilbert--Schmidt boundary together with the failure of the canonical Prime-Flute DtN/Feshbach bridge to preserve positivity at the critical spectral parameter.

## Falsification criterion

Construct a bounded transformation of the PF-085 trace-class compression yielding the finite-Weil operator, contradicting ideal invariance; or construct the ordinary continued Prime-Flute DtN/Feshbach object with a genuine positive quadratic form on the critical line despite the persisted cusp-flux obstruction. A different singular construction with its own sign theorem would evade rather than falsify the gate.

## Lean-formalizable core

- Ideal property under bounded sandwiches and compressions.
- Schatten criterion for the prime-power diagonal finite-Weil operator.
- Elementary variational loss of DtN positivity for `Delta-lambda` at `lambda>0`.
- Abstract distinction between information-preserving category change and sign preservation.
