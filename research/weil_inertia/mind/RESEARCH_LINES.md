# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Generalize Suzuki-null rigidity from endpoint bumps to arbitrary screened support geometry

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-258 isolate the phase-coupled source cone and the exact lower-envelope information available at a hypothetical first localized Weil crossing. WI-264 shows that every finite aperture admits an antisymmetric endpoint-bump autocorrelation which screens every active von-Mangoldt lag while the continuous source has favorable sign. WI-265 shows that the same geometry can satisfy every generic first-crossing operator condition in a flexible rank-one model.

WI-266 now proves that this explicit screening family is **not compatible with Suzuki's actual null equation**. The support gap contains an interval where all active prime translations vanish, while the regular kernel is strictly increasing with separation; the antisymmetric endpoint contributions therefore have a strict nonzero sign there. The actual localized Weil operator cannot annihilate the endpoint-bump vector.

The live theorem is to extend that source-specific contradiction beyond two separated endpoint components. Determine whether every genuine first-crossing null vector satisfies a support-spreading/no-long-gap condition forced by the prime translations plus the monotone continuous kernel, or construct a more complicated screened geometry whose translated components cancel the continuous convolution on every gap. The arithmetic null equation, not generic compression positivity, is now the controlling object.

## Treat source activation, autocorrelation screening, abstract firstness and arithmetic null-equation rigidity as separate gates

Finite source activation does not prevent screening, and abstract firstness does not prevent it either. WI-266 shows that the true arithmetic equation can still eliminate a geometry surviving both controls. This is a one-family exclusion, not a general no-screening theorem.

The next advance must preserve the exact source equation far enough to distinguish arbitrary support geometry. Reducing firstness back to generic Hilbert-space positivity before using the arithmetic kernel would discard precisely the information that produced WI-266.
