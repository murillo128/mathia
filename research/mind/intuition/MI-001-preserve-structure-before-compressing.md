# MI-001 — Preserve structure before compressing

**Evidence level:** supported

## Core intuition

Across the prime-circle and prime-flute branches, the recurring failure mode is **premature quotienting**.  Geometry may contain arithmetic information and still lose it when pushed too early through a path monodromy, local jet, unmarked spectrum, trace, or scalar determinant.  The successful constructions keep enough structure alive until the relevant relational variable has entered an injective or marked observable.

## Strongest current principle

A credible Mathia mechanism should pass an information-preservation audit at every transformation.  If a map identifies prime-derived configurations already known to be distinct, telescopes interior refinements, or multiplies resolved modes in a way that cancels their interscale displacement, no later zeta or spectral manipulation can canonically reconstruct the discarded information without adding new data.

The audit now has several mathematically distinct examples:

- **quotient loss:** an unmarked primitive shell identifies `n` with `2n` (PC-019);
- **transport loss:** first-order projective/Euclidean path laws telescope interior refinements (PC-013/PC-014/PC-018);
- **local-jet loss:** the anchored one-shell jet reduces to classical Jordan-totient data (PC-020);
- **spectral-mark loss:** unmarked weighted-path spectra are not generally inverse-unique, while endpoint spectral measures are (PF-048/PF-049/PF-052);
- **determinant loss:** the `w_j^2/w_{j-1}` multiscale memory carried by individual low modes cancels in the path pseudodeterminant, which telescopes to endpoint scale data (PF-089);
- **globalization loss/change of category:** a finite-tangent pole can become an essential spectral point when the tangent recurs along the infinite flute (PF-092).

The positive side is equally important.  Multi-gap cross-ratios survive Möbius normalization, become genuine finite-type moduli, and enter resolved hyperbolic eigenvalues.  PF-090/PF-091 show that, in a quantitative multiscale window, even the first upstream Feshbach memory survives into the **actual** surface eigenvalues.  The information is present until scalar determinant compression removes it.

## Evidence against overgeneralization

Compression is not intrinsically destructive.  It is harmless or useful when it is injective on the restricted family: the four-punctured tangent systole determines the unordered adjacent-gap contrast, and an endpoint Jacobi `m`-function determines an ordered finite weighted path.  Likewise, PF-085 shows that a two-point conformal kernel can retain genuine exact-circle information while still being trace class; “preserved” does not mean “spectrally singular.”

The criterion is therefore not “avoid scalars” or “avoid spectra.”  It is: **compute the fibers of the proposed compression on the prime-derived family before interpreting its analytic features.**

## Status / novelty

This is a program-level synthesis, not a standalone theorem.  Each listed loss mechanism is supported by exact or rigorous local results; the principle that these form a general design rule is supported rather than proved universally.

## Falsification criterion

Find a canonical construction in which an early map is provably non-injective on the relevant prime-derived configurations, yet a later observable recovers the discarded distinction without receiving any additional mark, label, reference, or external arithmetic input.

## Lean-formalizable core

- Representative non-injectivity identities such as `Phi_(2n)(z)=Phi_n(-z)` for odd `n`.
- Telescoping/semigroup identities for first-order transfer.
- Matrix-tree identity and two-neck cancellation `mu_+mu_-=3ab`.
- Injectivity of selected marked spectral maps on finite weighted paths.
