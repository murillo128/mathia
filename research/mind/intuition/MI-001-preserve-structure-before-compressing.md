# MI-001 — Preserve the discriminating structure before compressing

**Evidence level:** supported

## Core intuition

Across Mathia, the recurring failure is not “spectralization” or “taking a scalar” in the abstract. It is applying a transformation that is non-injective on the **particular distinction later claimed to be arithmetic**. The safe procedure is to compute the fibers, symmetries, common factors, and operator category of every compression before interpreting its spectrum, determinant, positivity, or critical exponent.

## Strongest current principle

Several branches now exhibit mathematically different forms of the same information-loss mechanism.

- **Prime Circle:** unmarked shells identify distinct levels; first-order transports telescope; single-shell rotation-invariant harmonic operators diagonalize and reduce to divisor/Dirichlet data (PC-019, PC-030, PC-032--PC-037).
- **Prime Flute:** unmarked spectra and scalar determinants can erase ordered multi-neck memory even when resolved eigenvalues retain it; globalization can also change a finite tangent pole into essential spectrum (PF-048--PF-052, PF-089--PF-092).
- **Prime Lattice:** the common off-line Blaschke factor is invisible to every generator Gram matrix, while the RH statement remains target/model-space totality (PL-017, PL-019, PL-020).
- **Weil Inertia:** fixed-block pinching is exactly a restriction of the global Fenchel feasible set, so it discards cross-boundary witness coordinates that remain present in the same support-one data (WI-012).
- **Weil Positivity:** universal projection/Gram positivity can merely repackage totality, and bounded positive repairs of a trace-class geometric coupling cannot cross the operator-ideal boundary to the non-Hilbert--Schmidt finite-Weil operator (WP-010, WP-014).

These are not one theorem, but they support one robust rule:

\[
\boxed{
\text{before compressing, identify exactly which equivalence relation the compression imposes.}
}
\]

If two configurations differing in the target variable have already become equivalent, no later unmarked function of the compressed object can canonically recover that difference without new information.

## Positive examples

Compression is useful when its fibers are controlled. Prime-Flute endpoint spectral measures/Weyl data can determine an ordered finite weighted path even when its unmarked eigenvalues cannot. The full Fenchel dual in Weil Inertia is itself a compression of matrix information, but it retains the cross-boundary coordinates discarded by block pinching. The criterion is therefore **information preservation on the relevant family**, not maximal dimensionality.

## Evidence against overgeneralization

A map may be globally non-injective yet sufficient for one particular arithmetic predicate. Full reconstruction of the input is unnecessary. Conversely, an injective finite encoding can still be analytically irrelevant to RH. The audit must be relative to the exact distinction being claimed.

## Status / novelty

This is a cross-branch synthesis, not a standalone theorem. Every listed loss mechanism is grounded in persisted findings; their organization as a design principle is supported.

## Falsification criterion

Find a canonical pipeline in which a stage is provably invariant under changing the claimed RH-relevant variable, yet a later observable recovers that variable without receiving any additional target, mark, reference, label, or arithmetic input.

## Lean-formalizable core

- Representative non-injectivity and telescoping identities.
- Inner-isometry invariance of Gram matrices.
- Block-restriction identity inside the Fenchel dual.
- Operator-ideal invariance under bounded sandwiches.
