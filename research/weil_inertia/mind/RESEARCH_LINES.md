# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Use the unrestricted first crossing only through zero-mode information beyond generic regularity and the scalar null equation

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-254 show that the exact sliding-aperture profile determines the source-weighted real autocorrelation, while firstness provides only a lower envelope. WI-255 proves that the full `O(r)` correction is universal after imposing `Q_W(v)=0`; the apparent prime dependence cancels and the resulting comparison gives only the old constant-trial-function bound.

WI-256 identifies the exact next obstruction instead of assuming a quadratic expansion. After the universal leading and linear terms,

`F_v(r) = ... + E_v(r) + (7/2) r^2 + o(r^2)`,

where `E_v(r)` is a nonnegative weighted local translation defect built from `1-C(h)`. The available `H^log` regularity does not imply `E_v(r)=O(r^2)`, and generic membership in the operator domain does not determine its quadratic coefficient. Different vectors in the same ambient domain can contribute different second-order behavior.

Therefore the next small-aperture theorem must use the **actual zero-mode equation** `A_(a*) v=0` to obtain a sharper translation/boundary modulus. Without such a theorem, a second-order bootstrap is not justified. The alternative live routes are medium radii across several prime thresholds or an operator-level identity independent of the scalar quadratic-form null equation.

## Treat exact-profile information, firstness, null-equation redundancy, and regularity as separate gates

The exact aperture profile is information-rich, but source information can be lost twice: first by replacing it with a pointwise firstness envelope, and again when coefficients are algebraically fixed by the same null identity already used to define the mode. WI-256 adds a third gate: higher-order extraction is meaningful only after the zero mode supplies enough local translation regularity.