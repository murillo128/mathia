# MI-002 — Localize and mark before global spectral compression

**Evidence level:** supported

## Core intuition

The infinite prime flute does not turn a finite prime-pattern pole into one more isolated global pole.  Recurrent isolated patterns can instead become **essential spectral data**.  The safe order of operations is therefore stronger than “localize first”: localize geometrically, retain the relevant mark or spectral mode, and only then compress by an operation known to be injective on that family.

## Strongest justified principle

Diverging collars can isolate a finite prime-derived tangent `Y_H` well enough that compactly supported spectral measures, wave observables and marked boundary/scattering data converge to finite-type tangent data.  When the same tangent occurs recurrently along the infinite flute, its low eigenvalues can be implanted into the global essential spectrum.

Consequently a residual eigenvalue

\[
\lambda=s(1-s),\qquad 0<\lambda<1/4,
\]

which is a genuine finite-rank resolvent/scattering pole on a finite tangent need not remain a discrete global resonance.  PF-092 makes the change of spectral category explicit: recurrent tangent values can be non-Fredholm points of the global `L^2` pencil.  Localization preserves the finite object; naive globalization changes what the singularity means.

At the same time, even after localization one must not overcompress.  PF-049/PF-050/PF-052 show that endpoint spectral measures/Weyl data can recover an ordered weighted path; PF-051/PF-053/PF-078/PF-079 retain comparable information in marked scattering.  PF-065 and PF-089 show the opposite behavior: Steklov eigenvalues can become universal after collar isolation, and a scalar low-energy determinant cancels the multiscale `w_j^2/w_{j-1}` memory visible in individual modes.

## Synthesis of evidence

PF-034 supplies the pointed geometric isolation mechanism.  PF-050 and PF-064 demonstrate recovery of tangent information from localized observables of the global Laplacian.  PF-066 gives an exact collar Schur complement that removes universal neck response without destroying the core boundary operator.  PF-043/PF-054 then show that repeated local spectral fingerprints enter the essential spectrum, while PF-092 proves that the corresponding near-one parameters obstruct the ordinary global Fredholm-resonance picture.

The synthesis is a local-to-global asymmetry:

\[
\text{finite tangent pole / marked response}
\quad\xrightarrow{\text{repetition}}\quad
\text{essential global spectral structure},
\]

not a countable union of ordinary global poles.

## Boundary cases and failure modes

This is not a complete localization-at-infinity theorem: PF-060 explains why bounded-geometry frameworks do not apply directly to the collapsing-neck tail.  Generalized finite-tangent inverse scattering is also not new inverse theory; PF-067 locates strong prior art.  Fixed patterns can be thermodynamically invisible because their area density is zero (PF-068).

The principle also does not forbid every global object.  Relative resolvents, rigged/weighted spaces, spectral-shift objects, or operator-valued direct integrals may remain viable if they explicitly account for the essential background instead of pretending it is a discrete resonance set.

## Status / novelty

The finite propagation, collar isolation, finite-tangent inverse theory, and Fredholm/essential-spectrum implications use classical machinery.  Their composition in this deterministic prime flute is supported by the established findings.  A complete two-scale operator theory for the infinite collapsing surface remains open.

## Falsification criterion

Refute the principle by showing that a recurrent isolated tangent eigenvalue below `1/4` remains an isolated finite-multiplicity pole of the ordinary global `L^2` resolvent rather than entering essential spectrum, or by producing a scalar compression known to be non-injective on the tangent family that nevertheless canonically recovers the lost marked data without adding information.

## Most informative next move

Build **relative or localized Weyl/scattering objects** around the isolated blocks and study how their residues or spectral measures sit inside the global essential spectrum.  Any subsequent determinant should be formed only after proving that the chosen compression preserves the multiscale data of interest.

## Lean-formalizable core

- Finite-propagation isolation behind a collar wider than the observation time.
- Matrix/Jacobi endpoint spectral measure determines the finite weighted path.
- Matrix-tree identity showing cancellation in the scalar pseudodeterminant.
- Abstract lemma: a Weyl sequence built from pairwise escaping copies puts the tangent eigenvalue in essential spectrum.
