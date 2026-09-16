# MI-002 — Canonical relational lifts can restore an intended gauge without restoring absolute coordinates

**Evidence level:** supported by exact finite harmonic, Euclidean and spectral models, with an exact classical target-fidelity separation from [AF-371](../../findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md).

## Core intuition

Information lost by a scalar or quadratic compression need not require restoring the original coordinates. A canonically available relation between surviving components can be enough to make the quotient faithful modulo the intended symmetry. The useful distinction is therefore not “scalar versus high-dimensional,” or even “few versus infinitely many inequalities,” but whether the retained relational data leave exactly the intended ambiguity group or target fibre.

## Strongest justified principle

AF-004 gives a harmonic example: for finite abelian signals with nonvanishing Fourier coefficients, the power spectrum loses phase while the bispectrum reconstructs the signal modulo translation. AF-005 makes the same mechanism algebraic: for a residual phase torus `K`, monomial observables with exponent lattice `L` leave ambiguity exactly `L^perp`; Smith normal form detects finite aliases invisible to rank.

AF-006 gives the operator version. A self-adjoint operator with ordered marks is classified, up to joint unitary equivalence, by the Gram data of the marked projections in each eigenspace. Diagonal spectral measures can lose relative orientation while the full matrix-valued marked spectral measure retains it.

AF-014 supplies an important adversarial correction to generic “Gram destroys sign” reasoning. For an ordered real configuration `X`, `X^T X` is complete modulo `O(d)`. At full row rank the entire Gram fiber splits into exactly two `SO(d)`-orbits, and compound minors recover every relative maximal-minor sign; only one global orientation torsor remains. One nonzero maximal-minor sign repairs that defect, while at rank deficiency even the orientation ambiguity disappears. A relational lift should therefore be measured against the exact fiber, not against a slogan about positivity or quadratic compression.

AF-371 gives the analytic target-fidelity analogue. If `1/Psi` is represented by its complete Taylor sequence, the analytic germ can still determine `Psi`; nevertheless compressing that rich data to the infinite Boolean signature “every Hankel moment matrix is positive” does not determine whether `Psi` lies in the Laguerre--Pólya class. Hamburger's theorem supplies target-mixed false positives. Schoenberg's translation total positivity instead tests all ordered cross-relations `det(Lambda(x_j-y_k))` and, for the stated reciprocal Laplace-transform class, is equivalent to Laguerre--Pólya membership. Thus **adding infinitely many positivity tests does not repair a quotient when the tests probe the wrong relational geometry**.

## What remains possible

These models do not say that bispectra, monomials, Gram data, matrix-valued measures or total positivity are universally sufficient. They show how to test a proposed lift: identify the ambiguity group or target fibre first, derive the relational observable canonically, and prove that the remaining ambiguity is precisely the intended gauge or that the target property factors through it. Arithmetic source specificity remains a separate gate.

AF-371 also makes the next positivity question sharper. Schoenberg gives an exact target-faithful lift, not a minimality theorem. Any proposal to use a smaller family of minors, finite order of total positivity, or a source-restricted positivity signature must prove that the corresponding fibre is already Laguerre--Pólya-pure; the number of inequalities is not evidence for that conclusion.

## Status / novelty

The bispectral, annihilator-lattice, Gram/compound-minor, marked-Hermitian and Hamburger/Schoenberg statements are persisted findings with classical ingredients. Their common interpretation as a constructive alternative to arbitrary target-carrying marks, and as a warning that positivity depth cannot substitute for the correct relational geometry, is a supported synthesis.

## Falsification criterion

Produce a claimed canonical relational lift whose exact retained data still admit two configurations outside the intended gauge orbit or on opposite sides of the target property. Conversely, a new lift that removes a documented ambiguity without importing the target would strengthen the principle.

## Lean-formalizable core

- Bispectral phase recursion modulo translation.
- Annihilator-lattice equality and Smith-normal-form aliases.
- Gram completeness modulo `O(d)` and the full-rank orientation torsor.
- Classification of marked Hermitian data by per-eigenspace Gram matrices.
