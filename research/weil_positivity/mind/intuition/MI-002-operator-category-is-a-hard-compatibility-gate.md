# MI-002 — Operator category is a hard compatibility gate for cross-branch positivity

**Evidence level:** proved for the audited Prime-Flute/Prime-Lattice comparison; supported as a broader gate

## Core intuition

Two constructions can carry closely related arithmetic-looking kernels and still be unable to represent the same positive operator because they live in incompatible operator ideals. This is stronger than a mismatch of coefficients: bounded coordinate changes, compressions, or standard positive repairs cannot cross a Schatten-class boundary.

## Strongest justified principle

WP-014 compares the canonical exact Prime-Flute Schiffer compression from PF-085 with the exact positive finite-Weil operator isolated in WP-004.

The Schiffer cell operator is trace class. Therefore its absolute value, square, bounded congruences, and bounded compressions remain trace class or better. By contrast, the finite-Weil operator with prime-power weights

\[
T e_{p^k}=(\log p)p^{-k/2}e_{p^k}
\]

satisfies

\[
T\in S_q\iff q>2,
\]

so it is not even Hilbert--Schmidt. No bounded change of Hilbert coordinates or standard positive repair of the Schiffer operator can therefore produce this finite-Weil operator.

This gives a useful cross-branch discriminator. If a proposed bridge starts from an analytically soft, trace-class geometric defect but the target arithmetic form has a critical non-Hilbert--Schmidt tail, the missing operation must be genuinely category-changing: unbounded weighting, singular limit, quotient/boundary construction, dynamical propagation, or another mechanism whose slower tail is derived rather than inserted.

## Evidence against overgeneralization

Operator ideals are not preserved by every mathematically natural construction. An unbounded transform or singular boundary map can change them, and this finding does not forbid such a route. The constraint is that the category change itself must be canonical and geometrically justified; choosing a singular weight solely to reproduce the desired Mangoldt tail would merely encode the target.

The mismatch also does not say that the exact Prime-Flute coupling is irrelevant. It says that its direct bounded positive functional calculus cannot be the finite Weil form. The coupling may still be an input to a larger dynamical or relative construction.

## Status / novelty

Trace-ideal closure properties are standard operator theory. The project-specific evidence is the exact placement of the two Mathia operators on opposite sides of the Hilbert--Schmidt boundary. The synthesis is a supported compatibility gate for future cross-branch proposals.

## Falsification criterion

Refute the narrow claim by constructing a bounded operator-theoretic transformation of the PF-085 trace-class compression that yields an operator unitarily equivalent to the WP-004 finite-Weil operator, contradicting ideal invariance. A singular/unbounded construction does not falsify the claim; it instead supplies the extra mechanism the intuition says is required.

## Lean-formalizable core

- Ideal property `A in S_1` and bounded `B,C` imply `BAC in S_1`.
- `A in S_1` implies `|A|` and `A^*A` lie in trace/Hilbert--Schmidt classes as appropriate.
- Series criterion giving `T in S_q iff q>2` for the prime-power diagonal weights.
