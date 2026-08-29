# MI-004 — Prime-shift symmetry is scaffolding, not a zero Hamiltonian principle

**Evidence level:** proved for the audited commutant/covariance classes; supported as a broader design gate

## Core intuition

The exponent lattice makes multiplication by a prime look like a canonical coordinate shift, but promoting that shift symmetry directly to a Hilbert--Pólya Hamiltonian is now heavily constrained. Exact invariance is too rigid, reversible additive covariance forces the wrong spectral geometry, weak covariance modulo compact/Schatten resolvents is often automatic, and the canonical positive translation-invariant metric/Laplacian models have featureless spectra or pure-gauge vertical phases.

## Strongest justified principle

PL-023--PL-031 separate the failures by operator category.

- PL-023: on the standard Hardy/Dirichlet representation, bounded operators commuting with all prime shifts are multipliers; normal multipliers are scalar. A self-adjoint operator whose nonreal resolvent commutes with all prime shifts is therefore scalar.
- PL-024: the natural one-sided logarithmic covariance is already the classical Bost--Connes/free-primon skeleton. It explains `log p` energies and the zeta partition function for `beta>1`, not critical-zero selection.
- PL-025: making the prime translations unitary with exact covariance `U_p^*HU_p=H+log p` forces the spectrum to be invariant under a dense additive subgroup and hence equal to all of `R`.
- PL-026--PL-027: adding trace-class, or in the semibounded case merely compact, errors at the Hamiltonian level forces at-most-linear eigenvalue counting, incompatible with Riemann--von Mangoldt `T log T` density.
- PL-028: moving the error to compact resolvents makes the relation vacuous for every compact-resolvent operator; even `S_q`, `q>1`, is automatic at Riemann-zero density. Any nontrivial `S_1` content must come from a specified prime action, not from the scalar `+log p` translation itself.
- PL-030--PL-031: canonical GCD/Poisson and weighted-Hasse constructions do produce real `1/2` measure/domain boundaries, but vertical log-prime phases are gauge and the resulting spectra do not see zeta zeros.

The surviving lesson is that **the arithmetic role of prime coordinates cannot be expressed solely as translation symmetry of the candidate spectrum**.

## What remains possible

A useful prime action can remain one-sided, target-relative, boundary-based, or attached to a noncompact reference where relative resolvents are not annihilated automatically. It may also act on observables or model spaces rather than translate the Hamiltonian itself. Such a mechanism must distinguish the exact rational-prime system from Beurling controls and must produce more than a known partition function, gauge phase, or automatic Schatten relation.

## Status / novelty

The individual no-go theorems and prior-art redirects are persisted findings. The synthesis is a supported operator-design constraint, not a classification of every possible prime action.

## Falsification criterion

Construct a nontrivial compact-resolvent zero Hamiltonian whose canonical prime-coordinate action lies inside one of the audited exact/compact covariance classes while retaining Riemann--von Mangoldt density, or show that one of the alleged vacuity/linear-counting conclusions fails under its stated hypotheses. A target-relative or noncompact-reference construction would instead evade, not falsify, the intuition.

## Lean-formalizable core

- Scalarity from a commuting normal multiplier/resolvent.
- Dense-translation invariance of a closed spectrum.
- Eigenvalue-counting obstruction under compact/trace-class additive covariance.
- Schatten membership of a resolvent from `N(T) asymp T log T`.
