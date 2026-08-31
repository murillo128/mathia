# MI-002 — Canonical relational lifts can restore an intended gauge without restoring absolute coordinates

**Evidence level:** supported by exact finite harmonic, Euclidean, and spectral models

## Core intuition

Information lost by a scalar or quadratic compression need not require restoring the original coordinates. A canonically available relation between surviving components can be enough to make the quotient faithful modulo the intended symmetry. The useful distinction is therefore not “scalar versus high-dimensional,” but whether the retained relational data leave exactly the intended ambiguity group.

## Strongest justified principle

AF-004 gives a harmonic example: for finite abelian signals with nonvanishing Fourier coefficients, the power spectrum loses phase while the bispectrum reconstructs the signal modulo translation. AF-005 makes the same mechanism algebraic: for a residual phase torus `K`, monomial observables with exponent lattice `L` leave ambiguity exactly `L^perp`; Smith normal form detects finite aliases invisible to rank.

AF-006 gives the operator version. A self-adjoint operator with ordered marks is classified, up to joint unitary equivalence, by the Gram data of the marked projections in each eigenspace. Diagonal spectral measures can lose relative orientation while the full matrix-valued marked spectral measure retains it.

AF-014 supplies an important adversarial correction to generic “Gram destroys sign” reasoning. For an ordered real configuration `X`, `X^T X` is complete modulo `O(d)`. At full row rank the entire Gram fiber splits into exactly two `SO(d)`-orbits, and compound minors recover every relative maximal-minor sign; only one global orientation torsor remains. One nonzero maximal-minor sign repairs that defect, while at rank deficiency even the orientation ambiguity disappears. A relational lift should therefore be measured against the exact fiber, not against a slogan about positivity or quadratic compression.

## What remains possible

These models do not say that bispectra, monomials, Gram data, or matrix-valued measures are universally sufficient. They show how to test a proposed lift: identify the ambiguity group/fiber first, derive the relational observable canonically, and prove that the remaining ambiguity is precisely the intended gauge. Arithmetic source specificity remains a separate gate.

## Status / novelty

The bispectral, annihilator-lattice, Gram/compound-minor, and marked-Hermitian classification statements are persisted exact findings with classical ingredients. Their common interpretation as a constructive alternative to arbitrary target-carrying marks is a supported synthesis.

## Falsification criterion

Produce a claimed canonical relational lift whose exact retained data still admit two configurations outside the intended gauge orbit. Conversely, a new lift that removes a documented ambiguity without importing the target would strengthen the principle.

## Lean-formalizable core

- Bispectral phase recursion modulo translation.
- Annihilator-lattice equality and Smith-normal-form aliases.
- Gram completeness modulo `O(d)` and the full-rank orientation torsor.
- Classification of marked Hermitian data by per-eigenspace Gram matrices.