# MI-008 — Gaussian-reference localization is relatively exact but intrinsically local

**Evidence level:** exact Xi/Appell and theta-seam analysis through XF-074

## Core intuition

The source-to-periodic interface does have a Xi-specific solution, but it is not a global periodic zero carrier. XF-073 changes the object being periodized: apply the exact Gaussian/Appell symmetry to the Xi heat solution, periodize both the transformed field and a known Gaussian reference, and divide. On a safe interior high-line segment, the Gaussian image penalty overwhelms Xi growth and the quotient recovers the true Xi solution with super-polynomial relative accuracy.

XF-074 shows why this success must remain local. The periodized Gaussian reference has an exact theta seam-zero lattice. For generic heat data those reference zeros do not cancel; even a zero-free Fourier-mode solution produces genuine poles in the quotient. The reference therefore removes the huge Gaussian amplitude locally without manufacturing a globally holomorphic periodic object.

## Strongest justified principle

For the Xi scaling used in XF-073, the Gaussian/Appell transform preserves backward heat exactly. Periodization is normally convergent, and on the interior contour `|Re z|<=L/4` every noncentral image pays a quadratic Gaussian cost. Dividing by the equally periodized Gaussian cancels the reference scale, leaving a relative error `exp(-c (log T)^(9/2))` with fixed derivative control over bounded positive heat time.

This is stronger than generic period dilation because it uses Xi-specific high-line growth against a known reference rather than suppressing a selected-zero seam by geometric dilution. It closes the relative source-localization gate that XF-072 left open.

But the reference itself has seam zeros at half-period horizontal position and vertical spacing `2 pi v/L`. XF-074 gives an exact zero-free heat-mode control whose transformed periodization is a vertical translate of the reference, so the quotient has poles at every reference seam zero. At the Xi scaling that vertical spacing shrinks like `(log T)^(-3/2)`. No macroscopic full-period holomorphic strip survives.

Thus **reference division is a center-local normalization mechanism, not an entire periodic Vieta carrier**. It can feed the destination only through a localization theorem that never silently crosses the reference divisor, or through an explicit meromorphic/divisor-aware reformulation.

## What remains possible

Three routes remain structurally honest: keep the construction on interior center-local windows and prove the destination-weighted estimate there; work meromorphically while controlling seam residues/divisors so that they are provably destination-null; or replace the infinite periodization by a finite entire trigonometric surrogate with a separately neutralized reference divisor and conditioning bound.

None is supplied by XF-073--XF-074. The other missing half is destination nontriviality: a hypothetical positive-transition state must carry order-one mass in the weighted quotient after the same localization.

## Status / novelty

Caloric Appell transforms, Gaussian periodization, Jacobi-theta seam geometry, and Fourier heat modes are classical. The Mathia-specific synthesis is the interface boundary: **Xi admits super-polynomial relative Gaussian-reference periodization on safe interior high lines, but the same reference necessarily introduces a global seam divisor, so the bridge is intrinsically local unless that divisor is handled explicitly.**

## Falsification criterion

Find a global positive-width full-period strip on which the periodized Gaussian reference is zero-free at the XF-073 scaling, or show that the generic heat-mode control in XF-074 fails to produce quotient poles at the seam zeros. Otherwise any Xi-to-Vieta bridge must remain local or become explicitly divisor-aware.
