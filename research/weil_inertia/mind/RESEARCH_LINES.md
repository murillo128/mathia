# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Use the unrestricted first crossing through the phase-coupled source cone, not generic zero-mode regularity

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-254 show that the exact sliding-aperture profile determines the source-weighted real autocorrelation, while firstness provides only a lower envelope. WI-255 proves that the full `O(r)` correction is universal after imposing `Q_W(v)=0`; the apparent prime dependence cancels and the resulting comparison gives only the old constant-trial-function bound.

WI-256 identifies the next obstruction. After the universal leading and linear terms,

`F_v(r) = ... + E_v(r) + (7/2) r^2 + o(r^2)`,

where `E_v(r)` is a nonnegative weighted local translation defect. The available `H^log` regularity does not imply `E_v(r)=O(r^2)`.

WI-257 proves that **generic zero-mode regularity cannot repair this**. After scaling, every localized Weil operator is `T_0+K_a` with one fixed logarithmic operator domain and bounded self-adjoint `K_a`. Every vector in that common domain can be made a zero mode of some bounded rank-at-most-two perturbation, while vectors in the domain realize incompatible quadratic `E(r)` behavior.

WI-258 supplies the first exact source-specific replacement rather than another regularity upgrade. Phase modulation preserves support and forces the global cosine cone

`M_v(t)=int (1-cos(th)) dmu_v(h) >= 0`,

while combining modulation with translated windows gives

`S_v(r)+J_v(r,t) >= 0`,

where `S_v(r)=F_v(r)-r lambda_r` and `J_v(r,t)=int_0^(2r) (2r-h)(1-cos(th)) dmu_v(h)`. Therefore any source-forced negative localized cosine defect `J_v(r,t)<=-epsilon` yields at least `epsilon` of strict firstness slack. Prime-power atoms enter only after their aperture thresholds and carry explicit phase weights.

The next theorem is now a concrete medium-radius source-sign problem: use the actual von-Mangoldt atoms, archimedean density, compact-support autocorrelation, and positive-definiteness to force `inf_t J_v(r,t)<0` for some `r<a_*`, or construct a source-compatible compact-support autocorrelation satisfying the full scalar aperture and phase-modulated cones. Generic modulation positivity alone is not enough.

## Treat exact-profile information, firstness, null-equation redundancy, domain regularity, perturbation specificity, and phase-defect sign as separate gates

The exact aperture profile is information-rich, but source information can be lost by envelope replacement, by algebraic cancellation against the null equation, by insufficient regularity for a desired asymptotic readout, and by replacing the arithmetic perturbation with an arbitrary bounded operator. WI-258 adds a genuinely source-explicit inequality family after those losses, but still leaves one decisive sign theorem open: the zeta factorization must force a negative localized phase defect rather than merely satisfy an abstract cosine-positivity cone.