# MI-002 — Operator category and spectral type are hard compatibility gates for cross-branch positivity

**Evidence level:** proved for the audited Prime-Flute/Prime-Lattice and radial/solenoid comparisons; supported as a broader gate

## Core intuition

Two constructions can carry closely related arithmetic-looking kernels or even the same scalar dispersion law and still be unable to represent the same positive operator. There are at least three independent compatibility gates: operator ideal/category, positivity under the category-changing operation, and **spectral type**. Matching eigenvalue formulas on a dense sample is not an operator bridge when one carrier is pure point and the other continuous.

A viable cross-branch identification must therefore transport not only a scalar symbol but the relevant spectral measure/type and sign structure.

## Strongest justified principle

WP-014 compares the canonical exact Prime-Flute Schiffer compression with the positive finite-Weil operator. The former is trace class; the latter lies in `S_q` exactly for `q>2` and is not Hilbert--Schmidt. Bounded coordinate changes, compressions, and congruences cannot cross that ideal boundary.

WP-015 tests the natural singular/boundary escape. Prime-Flute zero-energy DtN is positive, but spectral continuation loses self-adjoint positivity; on the critical scattering line the outgoing response is non-Hermitian because of universal cusp flux. A category-changing boundary operation therefore does not inherit a Weil-type sign theorem automatically.

WP-130--WP-131 add a different obstruction. The canonical solenoid Gamma generator samples the same scalar Gamma dispersion on the rational character spectrum, while the radial/log-scale Gamma generator realizes that dispersion as a continuous Fourier multiplier. After bounded heat functional calculus, the solenoid operator has a complete pure-point eigenbasis and the radial operator has no nonzero `L^2` eigenvectors because its multiplier has null level sets. Consequently **every bounded exact intertwiner in either direction is zero**. The mismatch is stronger than failure of unitary equivalence; changing to a bounded nonunitary representation does not help.

## Evidence synthesis and boundaries

The three gates are logically distinct. An unbounded or distributional transform can change spectral type; a boundary map or Schur complement can change operator ideal; a non-self-adjoint continuation can carry response data. None is ruled out merely because bounded intertwiners fail. But each such escape adds new structure and must prove its own domain, topology, and positivity theorem rather than borrowing positivity from the source operator.

Dense agreement of scalar dispersion values is therefore weak evidence. What matters is whether the spectral measures and the operation that transports them are canonically forced by the arithmetic geometry.

## Status / novelty

Trace-ideal closure, boundary/Weyl theory, the spectral theorem, and normal-operator intertwining theory are standard. The project-specific synthesis is the exact placement of Mathia candidates on incompatible sides of three boundaries: Schatten class, critical-line positivity, and pure-point versus continuous spectral type.

## Falsification criterion

Construct a bounded nonzero exact intertwiner between the WP-131 canonical heat semigroups, or a bounded transformation of the PF-085 trace-class compression yielding the finite-Weil operator. A genuinely unbounded/distributional or category-changing construction with an independently proved sign theorem would evade rather than falsify the gate.

## Lean-formalizable core

- Ideal property under bounded sandwiches and compressions.
- Schatten criterion for the prime-power finite-Weil operator.
- Loss of ordinary DtN positivity after positive-energy continuation.
- Vanishing of bounded intertwiners from complete point spectrum to a multiplication operator with null level sets, and conversely by adjoints.
