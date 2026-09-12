# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## First cross the first-prime positivity gate, then test the one-prime phase cone

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-257 show why scalar aperture firstness, the null equation and generic bounded-perturbation regularity do not supply the missing source control. WI-258 gives an exact source-explicit replacement: phase modulation and translated windows force

`S_v(r)+J_v(r,t) >= 0`,

with `J_v` a localized cosine transform of the von-Mangoldt/archimedean source-weighted autocorrelation. A source-forced negative `J_v` would create strict firstness slack.

WI-259 identifies the gate that must precede a prime-coupled use of this inequality. The first von-Mangoldt atom enters only above `r=(log 2)/2`; first crossing alone does not guarantee that radius is admissible. If strict positivity at `r=7/20` is established, monotonicity forces `a_*>7/20`, and because `log 2<7/10<log 3`, the fixed radius `7/20` contains exactly the single atom `n=2`.

The public `FP-0.35` certificate is currently only a candidate input: its post-fix computation has not been independently replayed by Mathia and the public theorem/status artifacts are inconsistent. Therefore the next gate is **independent finite-scale positivity beyond `(log 2)/2`**, not immediate optimization of the phase defect.

If that gate closes positively, freeze `r=7/20` and attack the exact one-prime identity using compact-support autocorrelation, positive-definiteness, first-crossing slack and the archimedean background. Prime activation alone is not enough: the first-prime shift can be absorbed locally by the endpoint potential, so the sign theorem must use the coupled source structure.

## Treat exact-profile information, firstness, null-equation redundancy, domain regularity, source activation, certificate trust, and phase-defect sign as separate gates

The phase cone survives the earlier abstraction losses, but WI-259 shows that its arithmetic usefulness also depends on proving that a prime threshold lies below every hypothetical first crossing. Do not smuggle a numerical/candidate positivity result into the source-sign argument. First certify the radius, then test the one-prime cone, and only then enlarge the source aperture if necessary.