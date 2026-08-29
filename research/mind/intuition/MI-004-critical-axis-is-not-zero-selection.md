# MI-004 — A canonical critical axis is not a zero-selection mechanism

**Evidence level:** supported by exact/classical mechanisms in multiple branches

## Core intuition

Mathia now has several independent reasons why a distinguished real part such as `1/2` can emerge naturally: unitarity, self-duality, Hilbert-space membership, Schatten thresholds, cusp winding, or support/alias boundaries. These mechanisms explain **where a symmetry or analytic transition lives**, but not why the Riemann zero divisor should concentrate there. Axis generation and zero selection are separate mathematical problems.

## Strongest justified principle

Prime Lattice gives the cleanest separation. PL-014 shows that Tate's completed Fourier--Mellin involution has `Re(s)=1/2` as its Hermitian/unitary self-dual axis. This is exactly the right symmetry line, yet the functional equation alone permits zeros off that axis in reflected pairs. PL-021 gives a different `1/2`: the canonical Möbius Bohr vector belongs to `H^2` precisely for `sigma>1/2`, is cyclic unconditionally throughout that region, and leaves the Hilbert space at the boundary. Again, the boundary exists without an RH-sensitive transition.

Prime Flute supplies an adversarial analogue. PF-088/PF-102 show that the selected `1/4` scattering/Ruelle thresholds arise from universal one-dimensional propagation and even a single compact endpoint defect. PF-103 then shows that a full primitive-orbit completion restores the universal parabolic `1/2` threshold through cusp winding. These exponents describe the carrier dynamics, not primality.

Weil Positivity closes the most tempting implication. WP-008 keeps the standard finite adelic data fixed and shows that the global Fourier involution has both positive and negative even modes. Thus even the canonical self-duality responsible for the completed functional equation does not itself provide the sign theorem that could select the critical axis.

The programmatic requirement is therefore:

\[
\boxed{
\text{canonical axis/boundary}
+\text{independent selector}
\longrightarrow
\text{possible RH mechanism}.
}
\]

The selector might be a genuine positivity theorem, totality/cyclicity result with target-sensitive data, cohomological sign rule, inertia elimination, or another global rigidity statement. It cannot be inferred merely from the existence of the axis.

## Evidence against overgeneralization

This intuition does not demote the critical line to an arbitrary coordinate. Tate duality shows that it is canonically distinguished in the completed arithmetic harmonic analysis, and Nyman theory uses the same Hilbert boundary in a substantive way. The claim is only that **distinguished is weaker than attracting/containing the zero divisor**.

Nor must every useful threshold equal `1/2`; the flute's `1/4` examples are included precisely because they show how compelling exponents can arise from summability alone.

## Status / novelty

The component mechanisms are classical or exact persisted findings. Their separation into “axis generation” versus “zero selection” is a cross-branch synthesis, not a theorem about all RH approaches.

## Falsification criterion

Produce one of the audited canonical axis mechanisms and prove, from the same structural theorem with no additional positivity/totality/divisor assumption, that all nontrivial Riemann zeros lie on its fixed/boundary set.

## Lean-formalizable core

- Fixed-axis identity for Tate duality.
- Hilbert-membership boundary of the Möbius Bohr vector.
- `p`-series/cusp-winding threshold calculations.
- Abstract logical distinction between invariance of a divisor under reflection and support of the divisor on the reflection fixed set.
