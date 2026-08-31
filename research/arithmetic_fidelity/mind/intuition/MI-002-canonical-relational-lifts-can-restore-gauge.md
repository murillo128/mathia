# MI-002 — Canonical relational lifts can restore an intended gauge without restoring absolute coordinates

**Evidence level:** supported by exact finite harmonic and spectral models

## Core intuition

Information lost by a scalar or quadratic compression need not require restoring the original coordinates. A canonically available **relation between surviving components** can be enough to make the quotient faithful modulo the intended symmetry. The useful distinction is therefore not “scalar versus high-dimensional,” but whether the added relational observable kills exactly the unwanted ambiguity group.

## Strongest justified principle

AF-004 gives a clean harmonic example. For a finite abelian signal with nonvanishing Fourier coefficients, the power spectrum determines only autocorrelation and loses Fourier phase, while the bispectrum couples three frequencies and reconstructs the signal modulo translation. The higher-order observable restores the intended gauge rather than selecting an absolute origin.

AF-005 makes the same mechanism algebraic. For a residual phase torus `K` and intended invisible subgroup `H`, monomial observables with exponent lattice `L` leave ambiguity exactly `L^⊥`; completeness modulo the intended gauge is the exact condition `L=H^⊥`. Smith normal form detects finite aliasing that rank or connectivity alone can miss.

AF-006 gives the operator version. A self-adjoint operator together with ordered marks is classified, up to joint unitary equivalence, by the Gram data of the marked projections in each eigenspace. Diagonal spectral measures can lose the relative orientation even on cyclic data, whereas the full matrix-valued marked spectral measure retains it. Off-diagonal relation, not merely more scalar moments, is the missing variable.

## What remains possible

These models do not say that third-order statistics, monomials, or matrix-valued measures are universally sufficient. They show how to test a proposed lift: identify the ambiguity group or fiber first, derive the relational observable canonically, and prove that its annihilator is exactly the intended gauge. Arithmetic specificity remains a separate question.

## Status / novelty

The bispectral, annihilator-lattice, and marked-Hermitian classification statements are persisted exact findings with classical ingredients. Their common interpretation as a constructive alternative to arbitrary target-carrying marks is a supported synthesis.

## Falsification criterion

Produce a proposed canonical relational lift whose observable lattice/marked Gram/bispectral data satisfy the claimed completeness criterion but still admit two configurations outside the intended gauge orbit. Conversely, a new exact relational lift that removes a currently documented ambiguity without importing the target would strengthen this principle.

## Lean-formalizable core

- Bispectral phase recursion modulo translation in the nonvanishing Fourier regime.
- Annihilator-lattice equality and Smith-normal-form finite aliases.
- Classification of marked Hermitian data by per-eigenspace Gram matrices.
