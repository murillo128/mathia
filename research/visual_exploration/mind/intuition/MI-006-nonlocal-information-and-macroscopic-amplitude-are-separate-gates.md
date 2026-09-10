# MI-006 — Source specificity begins only after the finite-size, window, and calibration null is resolved at the same scale

**Evidence level:** exact information/amplitude separation, failed fresh confirmation, and composed support-edge controls through VIS-129

## Core intuition

Nonlocal information and visible amplitude are not enough to identify arithmetic structure. At the support edge, universal weighting, source-window geometry, finite-circle capacity and effective-size calibration all create deterministic effects at precisely the scale where an arithmetic residual would be tempting to interpret.

The current null is now narrow enough to be constructive: use a bounded smooth-enough source taper and an explicit finite-CUE model, but demand calibration precision commensurate with the residual scale.

## Strongest justified principle

VIS-121--VIS-123 separate a failed predeclared source panel from the next support-edge opportunity. VIS-124 shows Montgomery's pair weight is a Laplace convolution; VIS-125 adds the window convolution; VIS-126 controls smooth density drift in a compatible regime.

VIS-127 proves that the growing-hard-window fix is geometrically inconsistent with a single `N=Theta(L_T)` CUE circle and the fixed-edge scaling. VIS-128 gives a concrete bounded tent alternative and its exact kernel, showing that pair-weight and taper corrections interact at leading `1/L_T` order. VIS-129 imports the classical pair-correlation effective-size candidate `N_e=rho_*L_T`, fixing a capacity scale, but proves that a generic `Theta(1/log L_T)` uncertainty in `rho` already shifts the null by `Theta(1/L_T)`.

## Program consequence

Before looking for a fresh source residual, compute the exact finite-`N` composed null for a predeclared bounded taper, effective-size transfer, diagonal/arc convention and covariance. Either justify the transfer of `rho` to `o(1/log L_T)` at the chosen coordinates or propagate the remaining uncertainty as a nuisance direction. Fresh data should only decide a residual after that model is frozen.

## Counterevidence / boundary

The pair-correlation effective size is a principled candidate, not a theorem that it transfers unchanged to the weighted tapered support-edge statistic. The exact finite-`N` covariance and any arithmetic lower-order term remain unknown. Special coordinates with vanishing first calibration derivative are not a safe post-hoc escape.

## Epistemic status

**An increasingly exact deterministic null and calibration-resolution gate; no source-specific support-edge residual has been established.**

## Falsification criterion

Derive an exact matched null in which the stated window/capacity/effective-size effects disappear at the claimed scale, or show that admissible calibration uncertainty is provably smaller than the current bound. A positive continuation should freeze the complete null and then survive untouched confirmation.
