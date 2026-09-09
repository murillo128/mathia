# MI-007 — Bow variance needs source-specific coherence at the distinguished twist

**Evidence level:** exact moving-window geometry plus literature-backed Dirichlet mean-value and source-specific norm-budget reductions through ANF-146

## Core intuition

The analytic bow is no longer a generic localization or moving-window problem. Generic logarithmic-twist averaging localizes any robust exceptional cancellation to an `O(X)` neighborhood, but that scale is sharp. Inside it, the moving-window operator leaves a full factor-`K` phase-coherence freedom even when support, coefficient magnitudes, and diagonal energy are fixed.

The decisive information must therefore come from the arithmetic phase/sign organization of the distinguished residual at the distinguished twist, or from cancellation retained across arithmetic decomposition pieces. Geometry that sees only support, magnitudes, diagonal mass, or componentwise mean square cannot supply the missing factor.

## Strongest justified principle

ANF-144 gives the uniform mean-value law with relative error `O(X/L)` and shows that every super-`X` twist interval has diagonal-scale average. Its adjacent-term matched control proves that `X` is the coefficient-general localization boundary rather than a proof artifact.

ANF-145 prices the source target: after normalization by the `x`-length the bow diagonal is `K log X`, while the available MRSTT componentwise type-II mean-square architecture remains at `K^2` times logarithmic savings. The gap is one full power of `K`, already before exceptional-set conversion.

ANF-146 identifies that same factor as intrinsic moving-window coherence. The length-`K` box operator has average squared singular scale `K` and top squared scale `K^2`, and equal-magnitude plane waves attain both zero and the sharp `K D` endpoint. No source-blind refinement of the box geometry can determine where the arithmetic residual lies in this coherence range.

## Program consequence

A positive bow theorem should expose a source-specific correlation, sign rule, decomposition-level cancellation, or another arithmetic invariant that controls the residual's projection onto the coherent moving-window modes at the distinguished twist. The theorem surface should quantify the required factor-`K` gain directly.

## Counterevidence / boundary

The findings do not prove that the distinguished bow twist exists or that the residual has coherent or incoherent phase. They only show that broad twist averaging and coefficient-general window geometry cannot decide the source-selected point.

## Epistemic status

**Supported source-specific coherence boundary; no bow contradiction or RH consequence is established.**

## Falsification criterion

Derive the required `o(K log X)` normalized bow variance from support, coefficient magnitudes, diagonal mass, or another coefficient-general moving-window estimate alone. A successful continuation should instead identify and verify the arithmetic information that removes the factor-`K` coherence freedom.