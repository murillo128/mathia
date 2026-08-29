# MI-003 — The arithmetic selector and the positive bulk repeatedly live on opposite sides of a symmetry-breaking operation

**Evidence level:** supported by several exact constructions and matched controls

## Core intuition

The strongest recent Weil-positivity candidates reveal the same structural fork in different languages. A positive bulk geometry is easy to obtain, but its canonical symmetric functional often pairs away the arithmetic information. The exact arithmetic selector survives only after taking a signed derivative, supertrace, noncommuting insertion, boundary flux, or spectral asymmetry — operations for which positivity is no longer inherited automatically.

## Strongest justified principle

Three exact examples isolate the pattern.

1. **Boolean/Hodge selector.** WP-018 recovers `Lambda(n)` from the supertrace of a positive residual-energy operator on the backward Boolean cube. WP-019--WP-020 show that a supersymmetric completion which keeps the insertion `Q`-invariant cancels all positive nonzero spectrum to an index. The successful Mangoldt insertion evades cancellation precisely because `[R_alpha,Q_alpha] != 0`.
2. **Boundary asymmetry.** WP-021 shows that eta data survive positive-square compression because they remember the sign of the boundary operator, but `B` and `-B` have the same positive square and opposite eta. Escaping the positive square restores information and simultaneously removes inherited sign.
3. **Information geometry.** WP-022 derives the exact critical finite Weil cosine comb as the radial score of a canonical positive product-Poisson family. The Fisher norm of that score diverges at `sigma=1/2`. WP-023 shows that standard positive divergences either reduce infinitesimally to the same Fisher geometry or have a boundary limit controlled only by the universal zeta pole, while unit-speed normalization sends every fixed prime-power coefficient to zero.

These examples support a precise design rule: **do not apply the positive/symmetric quotient before the arithmetic first variation or asymmetry has been coupled to the global completion**.

## What remains possible

A successful construction may be noncommutative, relative, boundary-based, graded, or cohomological. It need not make each local term positive. What it must supply is an independently forced theorem saying that the final coupled signed object is nonnegative on the Weil test class.

This intuition does not claim that every useful positivity proof must preserve a literal supertrace or score. A new geometric operation could reorganize the selector into a positive form. The requirement is only that the reorganization be derived before the selector is erased and that its sign not be equivalent to the desired RH conclusion by construction.

## Status / novelty

The individual selector identities, index cancellations, eta sign control, and Fisher/divergence obstructions are persisted findings. Their common “symmetry-breaking selector versus positive bulk” interpretation is a supported synthesis, not a universal theorem about positivity methods.

## Falsification criterion

Exhibit one of the audited positive bulk constructions and a canonical symmetry-preserving positive functional on it that retains the exact finite Mangoldt/Weil coefficients at the critical scale and supplies the missing completion without a signed/noncommuting/boundary input. Conversely, a new coupled sign theorem acting after a symmetry-breaking selector would support rather than falsify the intuition.

## Lean-formalizable core

- `Str R_alpha = Lambda(n)` and `[R_alpha,Q_alpha] != 0`.
- Equivariant McKean--Singer cancellation for `Q`-invariant insertions.
- Same-square/opposite-eta matched control.
- Finite-product score coefficient identity and Fisher divergence criterion.
