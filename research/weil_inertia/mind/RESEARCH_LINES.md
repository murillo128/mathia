# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Exactly recertify first-prime positivity, then test the one-prime phase cone

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-258 isolate the phase-coupled source cone `S_v(r)+J_v(r,t)>=0`. WI-259 shows that a prime atom is not available at every hypothetical first crossing until finite-scale positivity has first been proved beyond `(log 2)/2`; positivity at `r=7/20` would reduce the next phase problem to exactly the single atom `n=2`.

WI-260 audits the latest public post-fix `FP-0.35` generator and sharpens the gate. A replay of the current script is **not** yet a mathematical certificate of `lambda_(7/20)>0`: load-bearing transcendental/rational quantities are inserted as nearby point approximations rather than rigorous enclosures of the exact operator, and the advertised Arb inverse-residual test neither aggregates interval magnitudes safely under Arb's partial comparisons nor bounds a submultiplicative induced matrix norm.

The numerical margin remains encouraging, so WI-260 is an evidence/certification barrier rather than a negative result about FP-0.35. The next gate is independent **exact recertification**: enclose the exact `log 2`, `sqrt 2`, `tau=20 log 2/7`, harmonic values and `Q[tau]` entries, then use certified row-sum residual bounds or interval `LDL^T`/Cholesky to prove positivity of the exact finite matrix.

Only after that gate closes should the line freeze `r=7/20` and attack the exact one-prime phase identity. Prime activation alone is still insufficient: the first-prime shift can be absorbed locally by the endpoint potential, so the sign theorem must use first-crossing structure plus the coupled source cone.

## Treat exact-profile information, firstness, source activation, certificate correctness and phase-defect sign as separate gates

The current public numerical output is not evidence that may be promoted through synthesis. Source activation requires an exact finite-scale positivity theorem; reproducing a checker with unresolved proof-boundary defects does not supply it. If exact recertification succeeds, the source-sign problem resumes at one prime. If it fails, the conditional WI-259 implication survives but the line returns to the prime-free regime or seeks another positivity theorem past the threshold.
