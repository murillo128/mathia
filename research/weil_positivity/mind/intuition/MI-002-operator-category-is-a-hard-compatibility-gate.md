# MI-002 — Operator category, spectral type, and closable domain are hard compatibility gates for cross-branch positivity

**Evidence level:** proved for the audited Prime-Flute/Prime-Lattice and radial/solenoid comparisons; supported as a broader gate

## Core intuition

Two constructions can carry closely related arithmetic-looking kernels or even the same scalar dispersion law and still be unable to represent the same positive operator. The audited bridges now expose four independent compatibility gates: operator ideal/category, positivity under the category-changing operation, spectral type, and the **domain/closability** of any singular intertwiner. Matching eigenvalue formulas on a dense sample is not an operator bridge when one carrier is pure point and the other continuous, and distributional generalized eigenvectors do not repair that mismatch inside the natural Hilbert geometry.

A viable cross-branch identification must therefore transport not only a scalar symbol but the relevant spectral measure/type, a closable domain or alternative source-forced Hilbert structure, and the sign theorem needed at the destination.

## Strongest justified principle

WP-014 compares the canonical exact Prime-Flute Schiffer compression with the positive finite-Weil operator. The former is trace class; the latter lies in `S_q` exactly for `q>2` and is not Hilbert--Schmidt. Bounded coordinate changes, compressions, and congruences cannot cross that ideal boundary.

WP-015 tests the natural singular/boundary escape. Prime-Flute zero-energy DtN is positive, but spectral continuation loses self-adjoint positivity; on the critical scattering line the outgoing response is non-Hermitian because of universal cusp flux. A category-changing boundary operation therefore does not inherit a Weil-type sign theorem automatically.

WP-130--WP-131 add the spectral-type obstruction. The canonical solenoid Gamma generator samples the same scalar Gamma dispersion on the rational character spectrum, while the radial/log-scale Gamma generator realizes that dispersion as a continuous Fourier multiplier. After bounded heat functional calculus, the solenoid operator has a complete pure-point eigenbasis and the radial operator has no nonzero `L^2` eigenvectors. Consequently every bounded exact intertwiner in either direction is zero.

WP-132 closes the most immediate generalized-eigenfunction escape on the canonical Schwartz/character cores. Exact distributional intertwiners are forced coordinatewise onto Gamma level sets: away from zero they are weighted point evaluations at `±2π|q|`, and translation covariance reduces them to rational point samplers; the zero coordinate is at most a first jet. Every nonzero such sampler is nonclosable as an operator from natural radial `L^2`. Reverse exact intertwiners also vanish when they are closable and contain the finite-character core. At the critical Prime-Lattice amplitudes, reciprocal prime-power sampling fails even to be `ell^2`-valued at `sigma=1/2`, reproducing the independent WP-032 threshold.

## Evidence synthesis and boundaries

The escape is not “no singular geometry exists.” A zero-mode subtraction makes the critical sampling energy finite, but WP-132 shows that this subtraction changes the exact diagonal Gamma covariance and introduces a triangular coupling. Likewise an altered Hilbert norm, a boundary trace, a domain-changing quotient, or a non-exact intertwining response can evade the theorem. Such moves are **new operators**, not hidden equivalences between the existing carriers, and must derive their domain and positivity from the arithmetic geometry itself.

The four gates are logically distinct. Crossing a Schatten boundary does not preserve sign; changing spectral type distributionally does not give a closable Hilbert operator; and square summability above the critical sampling threshold does not repair point-evaluation nonclosability.

## Status / novelty

Trace-ideal closure, boundary/Weyl theory, the spectral theorem, point-supported distribution theory, and normal-operator intertwining theory are standard. The project-specific synthesis is the exact placement of Mathia candidates on incompatible sides of Schatten class, critical-line positivity, pure-point/continuous spectral type, and natural-domain closability.

## Falsification criterion

Construct a nonzero closable exact Gamma intertwiner on the canonical WP-132 cores, a bounded nonzero exact intertwiner from WP-131, or a bounded transformation of the PF-085 trace-class compression yielding the finite-Weil operator. A genuinely altered operator/Hilbert geometry with an independently proved sign theorem would evade rather than falsify the gate.

## Lean-formalizable core

- Ideal property under bounded sandwiches and compressions.
- Schatten criterion for the prime-power finite-Weil operator.
- Loss of ordinary DtN positivity after positive-energy continuation.
- Vanishing of bounded intertwiners across pure-point/continuous spectral type.
- Distributional support on multiplier level sets and collapse to point samples/jets.
- Nonclosability of nonzero point evaluation from `L^2`.
