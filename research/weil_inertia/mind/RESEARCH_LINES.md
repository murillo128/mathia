# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Turn Suzuki support-spreading into quantitative non-screenable arithmetic overlap

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-258 isolate the phase-coupled source cone and exact lower-envelope information at a hypothetical first localized Weil crossing. WI-264 constructs endpoint-bump modes that screen every active von-Mangoldt autocorrelation lag, and WI-265 shows that generic nested positivity/first-crossing structure cannot rule that geometry out.

WI-266 uses Suzuki's actual null equation to exclude that explicit two-endpoint family. WI-267 now removes the dependence on that geometry: for **every nonzero localized Weil null vector**, every point outside its essential support must be reached from the support by at least one active prime-power translation. Equivalently, a null mode has no open support gap on which the mode and all active translations simultaneously vanish.

This is an exact source-specific support-propagation theorem, but it is not yet the desired arithmetic non-screening statement. Pointwise translated activity can still cancel the regular convolution while every global prime-lag autocorrelation vanishes. The live theorem is therefore to combine the support cover with the distributional null equation and/or sliding lower-envelope inequalities to force a quantitative overlap or symbol that cannot be screened.

## Treat translated activity, autocorrelation overlap and first-crossing positivity as separate gates

WI-267 proves that the arithmetic source must be active across every support gap; it does **not** prove `C_v(log n) != 0` for some active prime power. A multi-component vector may have translated mass everywhere while signs/phases cancel its global autocorrelations.

The next advance must retain enough of Suzuki's exact source equation to turn translation domination into a quantitative non-screenable overlap. Returning to generic Hilbert-space positivity would discard precisely the structure that strengthened WI-266 into WI-267.