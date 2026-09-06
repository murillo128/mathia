# MI-009 — Finite, regular, or fixed-domain passive limits cannot realize the exact Gamma response

**Evidence level:** exact/literature-backed no-go chain through accepted WP-171, WP-173, and WP-174

## Core intuition

The obstruction to treating the archimedean Gamma phase as a passive response is not merely scalarity or finite dimensionality. Finite channel mixing, finite Pontryagin defect, ordinary indefinite external ports followed by regular passive Hilbert termination, and even singular parameter limits whose visible responses stay Schur on a common analytic domain all preserve too much of the passive analytic category. The exact Gamma factor carries an infinite non-Blaschke divisor and a boundary phase reversal that this closed class cannot absorb.

A genuine escape must change the analytic/sign category itself, not merely drive a regular passive parameter to a singular value.

## Strongest justified principle

WP-171 shows that at a regular lossless boundary point a matrix Schur transfer has a positive-semidefinite delay matrix, so every positive channel readout has one sign. A global matrix-inner realization therefore cannot reproduce the globally sign-changing Gamma velocity by positive scalarization.

WP-172 uses Krein--Langer factorization to show that finite negative index supplies only a finite Blaschke/Blaschke--Potapov denominator. The analytic Gamma orientation has infinitely many upper-half-plane zeros violating Blaschke, while the inverse has infinitely many poles. No finite defect or finite matrix coefficient/determinant repairs that divisor.

WP-173 shows that a regular `J`-contractive block terminated by an ordinary Hilbert-Schur load maps back into the Schur class even with infinitely many channels. WP-174 then closes the simplest singular-limit escape: Schur functions on one common domain, or on domains exhausting it with a uniform contractive bound, form a normal family. Convergence on any interior uniqueness set to the analytic Gamma target would force a Schur limit equal to Gamma, contradicting WP-170. For continuous lossless passive boundary responses, uniform convergence across the Gamma phase-velocity reversal is independently impossible because monotone phase order is closed under uniform limits.

## What remains possible

A domain may genuinely degenerate so that no common analytic neighborhood survives; convergence may be weak or boundary-only in a topology that does not preserve the Schur class; an unbounded renormalization may leave the passive unit ball; or the limit may be an unbounded operator/linear relation with changing domain rather than a scalar holomorphic transfer. Infinite negative index or a nonseparable finite--archimedean construction also remains outside the chain.

Each escape loses the inherited passive sign mechanism at exactly the point where it leaves the closed class. It must therefore state the limiting object and prove a new source-forced coercivity/positivity theorem rather than cite passivity of the approximants.

## Status / novelty

Matrix Schur kernels, Krein--Langer factorization, Pontryagin-space realization, `J`-contractive LFT theory, Vitali/Montel normal families, and monotone-limit arguments are classical. The durable synthesis is the category boundary: **the exact Gamma phase cannot be reached by finite/regular passive enlargements or by a fixed-domain singular limit that remains passive at every finite stage.**

## Falsification criterion

Construct a regular matrix-Schur positive readout reproducing the forbidden Gamma sign region, realize either Gamma orientation in a finite-index generalized-Schur class despite its divisor, give a regular `J`-contractive/passive-Hilbert LFT whose closed response is not Schur under WP-173's hypotheses, or produce a common-domain Schur sequence converging to the non-Schur Gamma response on an interior uniqueness set under WP-174's hypotheses.
