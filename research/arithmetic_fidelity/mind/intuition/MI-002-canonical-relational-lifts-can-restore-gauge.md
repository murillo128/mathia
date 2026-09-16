# MI-002 — Canonical relational lifts can restore an intended gauge without restoring absolute coordinates

**Evidence level:** supported by exact finite harmonic, Euclidean and spectral models, with exact classical target-fidelity separations from [AF-371](../../findings/AF-371-hankel-positivity-vs-total-positivity-target-fidelity.md), the finite-arity obstruction [AF-372](../../findings/AF-372-every-finite-toeplitz-minor-order-has-polya-frequency-false-positives.md), and the determining-sampling separation [AF-373](../../findings/AF-373-sampling-geometry-can-preserve-all-order-polya-frequency-fidelity.md).

## Core intuition

Information lost by a scalar or quadratic compression need not require restoring the original coordinates. A canonically available relation between surviving components can be enough to make the quotient faithful modulo the intended symmetry. The useful distinction is therefore not “scalar versus high-dimensional,” or even “few versus infinitely many inequalities,” but whether the retained relational data leave exactly the intended ambiguity group or target fibre.

## Strongest justified principle

AF-004 gives a harmonic example: for finite abelian signals with nonvanishing Fourier coefficients, the power spectrum loses phase while the bispectrum reconstructs the signal modulo translation. AF-005 makes the same mechanism algebraic: for a residual phase torus `K`, monomial observables with exponent lattice `L` leave ambiguity exactly `L^perp`; Smith normal form detects finite aliases invisible to rank.

AF-006 gives the operator version. A self-adjoint operator with ordered marks is classified, up to joint unitary equivalence, by the Gram data of the marked projections in each eigenspace. Diagonal spectral measures can lose relative orientation while the full matrix-valued marked spectral measure retains it.

AF-014 supplies an important adversarial correction to generic “Gram destroys sign” reasoning. For an ordered real configuration `X`, `X^T X` is complete modulo `O(d)`. At full row rank the entire Gram fiber splits into exactly two `SO(d)`-orbits, and compound minors recover every relative maximal-minor sign; only one global orientation torsor remains. One nonzero maximal-minor sign repairs that defect, while at rank deficiency even the orientation ambiguity disappears. A relational lift should therefore be measured against the exact fiber, not against a slogan about positivity or quadratic compression.

AF-371 gives the analytic target-fidelity analogue. If `1/Psi` is represented by its complete Taylor sequence, the analytic germ can still determine `Psi`; nevertheless compressing that rich data to the infinite Boolean signature “every Hankel moment matrix is positive” does not determine whether `Psi` lies in the Laguerre--Pólya class. Hamburger's theorem supplies target-mixed false positives. Schoenberg's translation total positivity instead tests all ordered cross-relations `det(Lambda(x_j-y_k))` and, for the stated reciprocal Laplace-transform class, is equivalent to Laguerre--Pólya membership. Thus **adding infinitely many positivity tests does not repair a quotient when the tests probe the wrong relational geometry**.

AF-372 adds a second resource axis inside the *correct* geometry. For every fixed `r`, there are nonnegative translation profiles in `TN_r\TN_(r+1)`. Therefore even exhaustive location sampling at a fixed determinant size does not recover the all-order Pólya-frequency target on the unrestricted class. The exact certificate needs **unbounded relational arity**, not merely many instances of one bounded-arity relation.

AF-373 separates a third resource that AF-372 did not settle: **where** the all-order relations are sampled. On the exponentially decaying source class `L`, Ganzburg's determining-set theorems allow one row-coordinate to be restricted to a much thinner infinite skeleton `E` without losing the full Pólya-frequency discriminator. An accumulation point is sufficient, and so is a symmetric unbounded sequence `u_s=o(sqrt(s))`. Yet the integer lattice `E=Z` admits explicit compactly supported `E`-PF false positives. Thus unbounded arity can survive while location geometry is compressed exactly, but only when the source class and sampling set supply a uniqueness theorem. Relational arity and sampling geometry are independent fidelity resources.

## What remains possible

These models do not say that bispectra, monomials, Gram data, matrix-valued measures or total positivity are universally sufficient. They show how to test a proposed lift: identify the ambiguity group or target fibre first, derive the relational observable canonically, and prove that the remaining ambiguity is precisely the intended gauge or that the target property factors through it. Arithmetic source specificity remains a separate gate.

For positivity routes the audit now has three independent questions: **is this the right relation, is the retained relational arity sufficient, and is the retained sampling geometry determining for the declared source class?** Ordinary Hankel PSD can fail the first question; fixed-order translation total positivity can fail the second; a fixed lattice can fail the third even when every determinant order is kept. Conversely AF-373 proves that spatial compression is not intrinsically fatal: it becomes exact when a source-class-specific determining theorem supplies the missing locations.

## Status / novelty

The bispectral, annihilator-lattice, Gram/compound-minor, marked-Hermitian, Hamburger/Schoenberg, Karlin--Khare and Ganzburg statements are persisted findings with classical ingredients. Their common interpretation as a constructive alternative to arbitrary target-carrying marks—and as a warning that relation type, relational arity and sampling geometry are distinct fidelity currencies—is a supported synthesis.

## Falsification criterion

Produce a claimed canonical relational lift whose exact retained data still admit two configurations outside the intended gauge orbit or on opposite sides of the target property. For a positivity lift, a matched control agreeing on every retained order and sampled location but differing at the target is decisive. Conversely, a source-class theorem proving that a thinner relational skeleton is determining strengthens the principle only for the hypotheses under which that uniqueness result holds.

## Lean-formalizable core

- Bispectral phase recursion modulo translation.
- Annihilator-lattice equality and Smith-normal-form aliases.
- Gram completeness modulo `O(d)` and the full-rank orientation torsor.
- Classification of marked Hermitian data by per-eigenspace Gram matrices.
