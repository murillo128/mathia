# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## If using Bombieri truncations, control coefficient cost and height tightness rather than raw span separation

**Linked intuitions:** `MI-008-inertia-counts-offline-pairs-but-not-their-distance`, `MI-014-source-coercivity-must-survive-confluence-and-drifting-bows`.

WI-231--WI-237 show that finite negative inertia detects off-line packets exactly but can lose coercivity as height grows. The unconditional simple critical-line exponentials are complete on bounded windows and are not a Bessel family, so ordinary separation/Riesz arguments cannot exclude spectral collapse. The surviving currency is coefficient price together with height tightness.

## Close the first odd crossing through the signed radial source flux, not generic ground-state positivity

**Linked intuition:** `MI-016-finite-radius-source-localization-can-replace-zero-side-tightness`.

WI-238--WI-252 isolate the finite-radius first-odd-crossing witness. Layer-cake localization produces a signed radial von-Mangoldt flux, while prime reflection violates the first Beurling--Deny positivity criterion. The live odd-sector theorem remains source-specific: control that signed flux, derive a phase/nodal restriction from the eigen-equation plus arithmetic source, or find another order structure not contradicted by prime reflections.

## Independently recertify the exact first-prime matrix, then test the one-prime phase cone

**Linked intuition:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols`.

WI-253--WI-259 isolate the phase-coupled source cone `S_v(r)+J_v(r,t)>=0`. WI-259 shows that a prime atom is not available at every hypothetical first crossing until finite-scale positivity has first been proved beyond `(log 2)/2`; positivity at `r=7/20` would reduce the next phase problem to exactly the single atom `n=2`.

WI-260 shows that the public `FP-0.35` reproduction script does not yet certify the exact matrix: load-bearing transcendental/rational quantities are point approximations rather than rigorous enclosures, and the Arb inverse-residual path does not establish the required induced-norm bound.

WI-261 closes the obvious fallback that the repository's separate `proofctl` exact-prime checker might already supply the missing theorem. Its recomputed exact-prime object is dead with respect to the judged matrix; matrix assembly instead evaluates the prime layer at a rational midpoint `TAU_MID`. Exact rational arithmetic proves that the advertised interval for `S2[0,0]` actually excludes the true entry. The same checker also substitutes `c_L=0` for the nonzero Weil constant used by the thin FP-0.35 Schur gate. Thus the nominal `J-E-matrices-exact`/positive-pivot attestations certify a surrogate, not the required exact first-prime operator.

The numerical margin remains potentially real, so WI-260--WI-261 are certification barriers rather than negative spectral results. The next gate must be **independent exact recertification of the intended operator**: interval-enclose the exact `log 2`, `sqrt 2`, `tau=20 log 2/7`, harmonic values and all `Q[tau]` entries, use the correct nonzero `c_L`, assemble the exact finite matrix with dependency-safe enclosures, and prove positivity by interval `LDL^T`/Cholesky or a valid induced-norm residual theorem.

Only after that gate closes should the line freeze `r=7/20` and attack the exact one-prime phase identity. Prime activation alone is still insufficient: the first-prime shift can be absorbed locally by the endpoint potential, so the sign theorem must use first-crossing structure plus the coupled source cone.

## Treat exact-profile information, firstness, source activation, object identity, certificate correctness and phase-defect sign as separate gates

A successful checker must prove positivity of the **same exact matrix** required by the theorem; reproducing a nearby midpoint matrix or a modified `c_L` problem is not conservative without a proved order relation. Source activation requires exact finite-scale positivity, and exact finite-scale positivity still does not prove the one-prime phase defect sign. If recertification succeeds, the source-sign program resumes at one prime; if it fails, WI-259 remains only a conditional reduction.
