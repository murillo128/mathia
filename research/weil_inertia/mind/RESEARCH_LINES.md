# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Use the unrestricted first crossing only through information beyond the null-equation-determined small-aperture terms

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-254 show that the exact sliding-aperture profile is information-rich: distributional derivatives recover source-weighted real autocorrelation and prime-power slope jumps. Firstness, however, gives only the lower envelope `F_v(r)>=r lambda_r`, which cannot be differentiated, and the leading small-radius term is universally saturated.

WI-255 now closes the first obvious subleading escape. For a normalized first global zero mode,

\[
\mathcal F_v(r)
=
r\log(1/r)
+r\bigl(\psi(2)-\log(4\pi)\bigr)
+o(r).
\]

Before the zero-mode equation is imposed, the `O(r)` coefficient contains the prime autocorrelations and the regular archimedean remainder. Using `Q_W(v)=0` cancels them **exactly**, leaving a coefficient independent of the mode, the first-crossing aperture, and the arithmetic source. Comparing with Suzuki's ground-state expansion reduces firstness at this order to

\[
\mu_1\le1-\log2,
\]

which is already the elementary constant-trial-function variational bound. Thus the entire first subleading small-aperture comparison contains no new arithmetic rigidity.

The live unrestricted route must therefore use information not determined by the single scalar null equation: a genuinely higher-order term if the mode has sufficient regularity, a medium-radius relation across several prime thresholds, or an additional operator/eigen-equation identity beyond the quadratic-form value `Q_W(v)=0`. “Compute the first correction” is now closed.

## Treat exact-profile information, firstness envelopes, null-equation redundancy, radial flux, and cone positivity as separate gates

The aperture representation is information-complete for the real autocorrelation if the exact profile is known. The loss occurs first when exact profile information is replaced by a pointwise lower envelope, and again when the first asymptotic correction is collapsed by the same null equation that defines the mode.

This is distinct from the odd route's signed radial source problem and from generic semigroup positivity. A future contradiction must use a source-specific relation that survives these quotient/cancellation steps rather than repackage information already contained in `Q_W(v)=0`.
