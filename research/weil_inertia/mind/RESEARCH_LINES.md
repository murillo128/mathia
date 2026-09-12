# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Independently recertify the exact first-prime matrix with a correct positivity judge, then test the one-prime phase cone

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-259 isolate the phase-coupled source cone `S_v(r)+J_v(r,t)>=0` and show that prime activation first requires finite-scale positivity beyond `(log 2)/2`. Positivity at `r=7/20` would reduce the next phase problem to exactly the single atom `n=2`.

WI-260--WI-261 show that the existing public FP-0.35 paths do not certify that premise. The reproduction script lacks rigorous enclosure/residual control, while the nominal exact-prime proofctl path assembles a midpoint surrogate and uses the wrong `c_L` for the theorem object.

WI-262 adds an independent judge-level failure. The interval LDL routine `_min_pivot_mpmath` updates every off-diagonal Schur entry twice. An exact rational indefinite `3x3` matrix with determinant `-3/50` is therefore reported with three positive pivots `1,1/4,21/100`. The defect survives arbitrary precision and zero-width intervals. Even after fixing it, the routine still needs genuine directed/outward interval arithmetic before its pivots can certify positivity.

The next gate is consequently an **independent two-stage certificate**: first assemble a dependency-safe enclosure of the intended exact operator with exact `tau`, prime terms and nonzero `c_L`; then prove positivity with a mathematically valid interval `LDL^T`/Cholesky or rigorous induced-norm residual theorem whose algebra and rounding are independently regression-tested. Only after both object identity and judge correctness are established should the line freeze `r=7/20` and attack the one-prime phase identity.

## Treat source activation, exact object identity, enclosure correctness, judge algebra and phase-defect sign as separate gates

Numerical margin, exact-looking metadata, and positive pivots do not compose into a proof unless they concern the same exact matrix and the positivity predicate itself is valid. WI-260--WI-262 are certification barriers, not evidence that the intended FP-0.35 operator is negative. If recertification succeeds, the source-sign program resumes at one prime; if it fails, WI-259 remains only a conditional reduction.