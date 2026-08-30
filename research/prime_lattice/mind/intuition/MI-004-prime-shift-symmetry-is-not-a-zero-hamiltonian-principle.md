# MI-004 — Prime-shift symmetry is scaffolding, not a zero-Hamiltonian principle

**Evidence level:** supported by exact operator obstructions and prior-art identifications

## Core intuition

The multiplicative prime action is canonical on the exponent lattice, but making that action look spectral is much easier than making it discriminate the Riemann zero set. Exact covariance is generally too rigid; weak covariance, scalar cocycles, projective phases, standard automorphic scattering, and generic model-space constructions are generally too flexible or already classical. The prime action becomes RH-relevant only when an additional target-sensitive invariant is forced by the exact rational-prime completion.

## Strongest justified principle

The negative evidence now covers several distinct repairs.

- PL-023--PL-028 squeeze ordinary prime-shift covariance from both sides: exact commutation is scalar, exact unitary logarithmic covariance gives full-line continuous spectrum, and the audited compact/trace-class Hamiltonian errors have the wrong eigenvalue-counting scale, while compact or `S_q`, `q>1`, resolvent covariance is essentially automatic at Riemann spectral density.
- PL-030--PL-031 show that canonical GCD/Poisson and weighted Hasse structures can produce the critical `1/2` boundary while leaving vertical phases gauge or the spectrum otherwise zero-blind.
- PL-034--PL-038 close straightforward relative/cocycle repairs. After subtracting the scalar logarithmic shift, the canonical Bost--Connes prime action has no residual cocycle; arbitrary scalar multiplicative/translated cocycles and projective phases can be manufactured without zero information; the canonical Hilbert-symbol reciprocity package collapses globally to the product formula rather than a new commutator invariant.
- PL-039--PL-040 show that unramified `GL_2` spherical scattering scalarizes to a classical zeta ratio, while fixed finite nonspherical ramification can introduce matrix structure at only finitely many places. Neither supplies an infinite prime-direction matrix selector.
- PL-041--PL-043 show that co-shift/model-space, Clark positivity, Sonine, de Branges, and related ambient Fourier machinery are real operator-theoretic frameworks, but their spectral reality/positivity is universal for arbitrary inner or Sonine data until a zeta-specific target theorem is added.

Thus “prime action + spectral formalism” is not yet a mechanism. The missing object must be an invariant that the action cannot realize for arbitrary Euler systems or arbitrary target inner functions.

## What remains possible

A target-relative nonnormal action, a boundary defect tied to the exact rational-prime norm, a genuinely infinite ramified/adelic construction, or a relative object against a noncompact reference can still evade the audited no-go results. Such a construction must survive Beurling controls and must not reduce to a scalar zeta factor whose zeros were already present by definition.

## Status / novelty

The commutant/covariance theorems, cocycle controls, automorphic scalarizations, and model-space universality results are persisted findings or audited prior art. The synthesis is a supported restriction on what can count as a prime-action Hamiltonian principle.

## Falsification criterion

Construct a canonical prime action with a nontrivial invariant forced by the exact rational-prime completion that cannot be reproduced by the matched Beurling, arbitrary-inner, scalar-cocycle, or standard spherical-scattering controls, and then prove that invariant constrains the zero divisor beyond functional-equation symmetry. A construction differing only by a chosen scalar cocycle or target function does not falsify the intuition.

## Lean-formalizable core

- Exact commutant and logarithmic covariance identities.
- Automatic compact/`S_q` resolvent covariance estimates.
- Triviality/flexibility tests for scalar and projective cocycles.
- Equality-of-framework implications for arbitrary-inner model-space controls.
