# MI-001 — Preserve structure before compressing

**Evidence level:** supported

## Core intuition

Across the prime-circle and prime-flute branches, information is repeatedly lost when geometry is compressed too early into a scalar spectrum, trace, determinant, path monodromy, or local jet. The surviving arithmetic signal tends to live one structural level earlier: in anchors, relative configurations, operator-valued boundary data, finite tangents, or multi-point moduli.

## Strongest current principle

A credible Mathia construction should pass an **information-preservation test before spectralization**. If a transformation identifies configurations known to be arithmetically distinct, telescopes interior refinements, or replaces an operator by a spectrum that is non-injective on the relevant family, no later zeta/spectral manipulation can recover the lost information without adding new data externally.

Prime-circle supplies three exact examples: unmarked primitive shells identify `n` with `2n`; one-dimensional projective/Euclidean transfers telescope; anchored local jets reduce to classical Jordan-totient data. Prime-flute supplies complementary examples: a single cuff is only a standard cylinder parameter; Steklov eigenvalues of an isolated block become universal although the full DtN operator retains the core; unmarked weighted-path eigenvalues are not inverse-unique, while endpoint spectral measures are.

The positive constructions obey the converse pattern. Relative multi-gap cross-ratios survive Möbius normalization, become finite-type hyperbolic moduli, and then influence genuine Laplace/resonance data. Spatial localization preserves those moduli long enough for spectral theory to see them.

## Boundary cases

Compression is not intrinsically bad. It is useful when injective on the restricted family: the four-punctured tangent systole recovers the unordered adjacent-gap contrast, and a Jacobi endpoint `m`-function recovers an ordered weighted path. The criterion is information loss, not dimensionality alone.

## Status / novelty

This is a program-level synthesis, not a standalone theorem.

## Falsification criterion

Find a repeatedly successful construction in this program where a demonstrably non-injective early quotient nevertheless yields a canonical later observable recovering the discarded arithmetic information without adding an external mark.

## Most informative next move

For every new proposed transform, explicitly compute its fibers on the prime-derived family before studying its spectrum or zeta.

## Lean-formalizable core

Formalize representative non-injectivity/telescoping lemmas and injectivity of the four-punctured systole map modulo reversal.
