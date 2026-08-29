# MI-001 — Preserve the discriminating structure before compressing

**Evidence level:** supported

## Core intuition

Across Mathia, the recurring failure is not “spectralization,” “positivity,” or “taking a scalar” in the abstract. It is applying a transformation that is non-injective on the **particular distinction later claimed to be arithmetic**, or optimizing perfectly after that distinction has already been discarded. The order of operations matters: identify and preserve the selector first; only then compress, spectralize, or prove a sign.

## Strongest current principle

Several branches now exhibit mathematically different forms of the same information-loss mechanism.

- **Prime Circle:** even pointing a translation-invariant shell does not help when local spectral measures and Schur self-energies are derivative data (PC-038). Canonical divisor-level Kron refinement is path independent (PC-039), fixed primitive metric/chiral blocks classicalize to Dirichlet special values (PC-044--PC-045), and the joint same-level metric/chiral defect factors through old vertices with low rank (PC-046). The live information is old/new multilevel coupling before it is eliminated.
- **Prime Flute:** marked local spectral measures can retain ordered multi-neck data that scalar determinants erase, but the strong `p_n+1` composite clone shows that many tail cross-ratio/separator/collar quantities become asymptotically indistinguishable. The unresolved discriminator sits at the operator comparison, not in a chosen coordinate defect.
- **Prime Lattice:** a common off-line Blaschke factor is invisible to every generator Gram matrix while the Nyman statement remains target/model-space totality (PL-017, PL-019, PL-020). Prime-shift symmetry adds a second warning: exact covariance is too rigid whereas weak compact-resolvent covariance is automatic (PL-023--PL-028).
- **Weil Inertia:** WI-012 showed that block pinching loses feasible global Fenchel coordinates, but WI-015--WI-020 go further: after collapsing to the exact single-profile Gram defect, explicit countermodels remain. Perfect optimization of that defect cannot restore information discarded by the representation itself.
- **Weil Positivity:** the exact Mangoldt selector can be recovered by a signed Boolean supertrace or Poisson score (WP-018, WP-022), while canonical positive Hodge/information-geometric completions cancel, diverge, or universalize that data (WP-019--WP-023). Applying the positive symmetric quotient too early erases the selector one hoped positivity would control.

These are not one theorem, but they support one robust rule:

\[
\boxed{
\text{compute the fibers of every stage, and do not optimize or prove positivity after the target variable is already constant on them.}
}
\]

## Positive examples

Compression remains useful when its fibers are controlled. Prime-Flute endpoint spectral measures/Weyl data can determine an ordered finite weighted path even when unmarked eigenvalues cannot. The Weil-Inertia Fenchel dual is an exact compression that removes block-boundary optimization loss; its limitation appears only after one asks whether the underlying single-profile Gram defect itself distinguishes the adversarial configurations. WP-018 likewise shows that a finite difference/supertrace can be a useful selector even though it is not a positive functional.

## Evidence against overgeneralization

A map may be globally non-injective yet sufficient for one particular arithmetic predicate; full input reconstruction is unnecessary. Conversely, retaining a target variable does not prove RH relevance. The audit must be relative to the claimed distinction and must separate **optimization loss** from **information loss**.

Nor does the rule demand that the final object remain high-dimensional. A later scalar or determinant can be decisive if injectivity on the relevant family has already been proved or if a separate theorem shows that the target predicate factors through it.

## Status / novelty

This is a cross-branch synthesis, not a standalone theorem. Every listed loss mechanism is grounded in persisted findings; their organization as an order-of-operations principle is supported.

## Falsification criterion

Find a canonical pipeline in which a stage is provably invariant under changing the claimed RH-relevant variable, no later stage receives any new target/mark/reference/arithmetic information, yet a later observable recovers that variable. Alternatively, show that an exact countermodel for a compressed representation can be excluded solely by better optimization of that same representation.

## Lean-formalizable core

- Representative non-injectivity and telescoping identities.
- Inner-isometry invariance of Gram matrices.
- Schur/path-independence and low-rank old-vertex factorization.
- Exact Fenchel duality plus equality-of-representation/equality-of-optimized-value.
- Hodge/equivariant cancellation of selector data under symmetric positive compression.
