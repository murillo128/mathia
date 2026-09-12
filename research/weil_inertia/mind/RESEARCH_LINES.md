# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Use the unrestricted first crossing only through information beyond the pointwise firstness envelope

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253 converts the first unrestricted localized crossing into a continuum of source-dependent sliding-window averages. WI-254 shows that the **exact** aperture profile is much richer than a single inequality: it is a `min`-transform whose distributional second derivative recovers the source-weighted real autocorrelation. Prime-power shifts appear as exact slope jumps and the continuous archimedean term recovers the remaining autocorrelation away from one removable zero of its weight.

But firstness supplies only the lower bound `F_v(r)>=r lambda_r`, not the exact profile, and that inequality cannot be differentiated to read the jump signs. Worse, the small-radius endpoint is saturated:

\[
\mathcal F_v(r)\sim r\log(1/r),
\qquad
r\lambda_r\sim r\log(1/r),
\qquad
\frac{\mathcal F_v(r)}{r\lambda_r}\to1.
\]

So neither derivative-sign inference nor a fixed relative small-radius reserve can close the first crossing. The live target is additional source-sensitive control of the **exact profile**: a subleading small-radius term, a medium-radius curvature/slope relation, or a zero-mode equation constraint that couples several prime-power thresholds.

The accepted local clue remains the right handoff, but its decisive test is now narrower: exploit information beyond the pointwise firstness envelope, not merely more radii.

## Treat exact-profile information, firstness envelopes, radial flux, and cone positivity as separate gates

The aperture representation itself is information-complete for the real autocorrelation if the exact profile were known. The loss occurs when exact profile information is replaced by a pointwise lower envelope. This is distinct from the odd route's signed radial source problem and from generic semigroup positivity.

A future contradiction must therefore use genuinely zeta-specific information that controls the profile more tightly than universal first-crossing asymptotics do. Failure of odd cone positivity, profile invertibility, or positivity of every sliding average is not by itself an RH consequence.
