# MI-002 — Localize in space before compressing spectrally

**Evidence level:** supported

## Core intuition

The infinite prime flute is too singular for most global spectral compressions, yet finite prime-derived regions can become asymptotically isolated by collars whose widths diverge. This creates a robust asymmetry: **globalize first and the arithmetic signal is swamped; localize geometrically first and ordinary finite-type spectral theory becomes informative again.**

## Strongest justified principle

Recurring isolated prime patterns produce genuine pointed tangents `Y_H`, and compactly supported spectral measures/wave observables in the corresponding blocks converge to those of `Y_H`. Thus finite-pattern moduli can enter the essential spectrum and local spectral response of the global Laplacian even when no useful global trace or determinant exists.

PF-034 gives the geometric isolation mechanism. PF-050 and PF-064 show that local spectral measures and localized wave traces can recover tangent data from the global Laplacian. PF-066 shows that an exact maximal-collar Schur complement can canonically strip the universal neck from full DtN data. PF-065 supplies the warning: spectral compression of that boundary operator to Steklov eigenvalues alone becomes universal and loses the interior exponentially.

## Boundary cases

This is not a complete characterization of the essential spectrum: PF-060 blocks direct use of standard bounded-geometry localization-at-infinity theorems. Nor does full generalized scattering reconstruction count as new inverse theory; PF-067 identifies strong prior art. Fixed-pattern signals also have zero area density (PF-068), so uniform thermodynamic averaging erases them.

## Status / novelty

The localization and inverse tools are classical; their exact fit to the prime-derived collar isolation is supported. A general two-scale essential-spectrum theorem for this collapsing flute remains open.

## Falsification criterion

Find a canonical normalized global trace/IDS that preserves a fixed tangent fingerprint with nonzero weight, or show that localized global resolvents fail to converge to the finite tangent despite diverging separating collars.

## Most informative next move

Develop a two-scale localization theorem separating noncollapsed finite tangents from universal collapsing-collar channels, rather than searching for another absolute trace.

## Lean-formalizable core

- Collar width tends to infinity as separating length tends to zero.
- Finite-propagation isolation lemma for compact supports behind a collar of width `W>T`.
- Exact Schur-complement identity for collar DtN stripping.
