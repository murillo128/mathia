# MI-002 — Operator category, spectral type, closable domain, and sign inheritance are hard compatibility gates

**Evidence level:** proved for the audited Prime-Flute/Prime-Lattice and radial/solenoid comparisons; supported as a broader gate

## Core intuition

Matching scalar kernels or dispersions does not identify positive operators. The audited bridges now expose distinct gates for operator ideal, positivity under category change, spectral type, closable domain, and **inheritance of a sign/contractivity theorem after renormalization**. A singular subtraction can make a previously divergent statistic finite while simultaneously destroying the dynamics from which its positivity was supposed to descend.

A viable bridge must therefore transport the entire analytic category needed by the final theorem, or else admit that a new operator has been created and prove its sign from scratch.

## Strongest justified principle

WP-014 places the Prime-Flute Schiffer compression and the finite-Weil operator on opposite sides of a Schatten boundary. Bounded sandwiches and compressions cannot bridge trace class to the slower Weil tail.

WP-015 shows that a natural boundary category change does not preserve sign automatically: zero-energy DtN is positive, while critical scattering continuation is non-Hermitian because of cusp flux.

WP-130--WP-131 add spectral type. The solenoid Gamma generator is pure point on rational characters while the radial Gamma generator has continuous multiplier spectrum. Even after bounded heat functional calculus, every bounded exact intertwiner in either direction is zero.

WP-132 closes the canonical exact distributional escape. Such intertwiners collapse to rational point samples/jets on Gamma level sets, are nonclosable from natural radial `L^2`, and at the critical prime-power amplitudes fail even the required `ell^2` summability.

WP-133 closes the tempting claim that anchored zero-mode subtraction can regularize the critical sampler while retaining the old Gamma Markov sign. On every finite set of distinct positive Gamma frequencies, a positive quadratic form that kills constants and is contractive under one nontrivial Gamma heat step must vanish identically. The Vandermonde orbit of the constant vector fills the whole value space. Therefore any nontrivial anchored positive form necessarily abandons contractivity under the old semigroup.

## Evidence synthesis and boundaries

A new triangular generator, boundary response, altered Hilbert geometry, quotient, cohomological complex, or non-exact coupling can evade these theorems. But such a construction is not a hidden equivalence of the old carriers. Its domain, closability, critical scale, and sign theorem must be derived independently.

The gates are independent. Crossing an ideal boundary does not preserve sign; matching point spectra distributionally does not give a closable operator; square summability does not repair point evaluation; and making a form finite by anchoring does not preserve semigroup contractivity.

## Status / novelty

Trace ideals, boundary/Weyl theory, spectral-type decomposition, distribution-supported intertwiners, and Lyapunov/contractivity arguments are classical. The project-specific synthesis is the exact placement of the Mathia candidates across these incompatible categories.

## Falsification criterion

Construct a nonzero bounded/closable exact Gamma intertwiner in the covered categories, or a nonzero positive constant-killing finite Gamma form satisfying the WP-133 heat contractivity inequality. A genuinely altered operator with its own sign theorem would evade rather than falsify the gate.

## Lean-formalizable core

- Schatten ideal invariance under bounded transformations.
- Loss of DtN positivity under positive-energy continuation.
- Vanishing bounded intertwiners across pure-point/continuous spectral type.
- Nonclosability of point-evaluation intertwiners.
- Vandermonde kernel propagation for anchored contractive forms.
