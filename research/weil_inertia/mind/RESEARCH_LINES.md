# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Use the unrestricted first crossing only through source-specific arithmetic zero-mode information

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-254 show that the exact sliding-aperture profile determines the source-weighted real autocorrelation, while firstness provides only a lower envelope. WI-255 proves that the full `O(r)` correction is universal after imposing `Q_W(v)=0`; the apparent prime dependence cancels and the resulting comparison gives only the old constant-trial-function bound.

WI-256 identifies the exact next obstruction. After the universal leading and linear terms,

`F_v(r) = ... + E_v(r) + (7/2) r^2 + o(r^2)`,

where `E_v(r)` is a nonnegative weighted local translation defect. The available `H^log` regularity does not imply `E_v(r)=O(r^2)`.

WI-257 now proves that **generic zero-mode regularity cannot repair this**. After scaling, every localized Weil operator is `T_0+K_a` with one fixed logarithmic operator domain and bounded self-adjoint `K_a`. Every vector in that common domain can be made a zero mode of some bounded rank-at-most-two perturbation, while vectors in the domain realize incompatible quadratic `E(r)` behavior. Therefore the abstract equation `(T_0+K)v=0` supplies no generic translation-modulus upgrade.

The next small-aperture theorem must use the actual arithmetic form of `K_(a*)`: von-Mangoldt weighted translations, threshold changes at prime powers, the archimedean kernel, or a multi-aperture identity unavailable to arbitrary bounded perturbations. Otherwise prioritize medium-radius relations across prime-power thresholds or another source-specific operator identity.

## Treat exact-profile information, firstness, null-equation redundancy, domain regularity, and perturbation specificity as separate gates

The exact aperture profile is information-rich, but source information can be lost by envelope replacement, by algebraic cancellation against the null equation, by insufficient regularity for a desired asymptotic readout, and by replacing the arithmetic perturbation with an arbitrary bounded operator. WI-257 closes only the last generic route; it leaves source-specific arithmetic identities fully open.