# MI-001 — Weil positivity needs a sign-producing global operation that preserves the source selector before positive scalarization

**Evidence level:** supported through WP-162 by exact selectors, sign obstructions, operator/category controls, algebraic-incidence exclusions, and the cyclotomic radial-flux classification

## Core intuition

The Weil-positivity search repeatedly finds mathematically natural objects that are positive, self-dual, Hodge-theoretic, information-geometric, or locally logarithmic. The strongest current finite-shell object is sharper: the primitive cyclotomic radial path itself has an intrinsic signed flux whose total mass is exactly `Lambda(n)`, and the flux is pointwise positive for all radial times exactly on prime powers.

That still does not give a positive Weil form. Mixed-prime shells achieve the required Mangoldt zero by cancellation of positive and negative flux. Any ordinary shellwise positive size removes that cancellation and becomes positive on every shell. The missing mechanism is therefore a **source-specific global sign operation that retains signed finite data until finite--archimedean assembly**, not merely a local positive density or the `log p` scale.

## Strongest justified principle

WP-140--WP-144 show that even an intrinsic, scale-invariant positive `log m`-scale Kron/SPD response is insufficient when matched composite controls reproduce it and no global Weil polarization appears. WP-145--WP-160 then show that positive completion, determinant formation, separated tensoring, and fixed finite-arity algebraic torsion incidence cannot manufacture missing mixed-prime provenance after the source has already split.

WP-161 provides a genuine escape from the fixed torsion category: a real radial deformation of the primitive cyclotomic shell has boundary value `Lambda(n)`. But every derivative-independent positive local jet is Jordan-totient data with full shell support.

WP-162 uses the whole radial half-line and recovers the selector exactly. For `rho_n(s)=-d/ds log Phi_n(e^{-s})`,

`int_0^infinity rho_n(s) ds = Lambda(n)`,

and `rho_n(s)>0` for all `s>0` exactly when `n` is a prime power. For non-prime-powers the zero total mass is a genuine sign cancellation. Consequently total variation, `L^q` size, squared flux, or any pointwise strictly positive energy is nonzero on every shell; even source-independent exponential damping destroys the exact mixed-prime zero in the first explicit control.

This identifies where positivity may still enter: after a signed nonlocal finite object has been coupled across shells and to the archimedean place, not by replacing that object with a positive shellwise norm.

## What remains possible

A viable construction may take the signed radial-flux family as input and assemble a global quadratic or operator object whose final polarization is positive for source-forced reasons. It may also use a genuinely nonlocal boundary response or cohomological coupling that preserves the net flux cancellation until the final finite--archimedean operation.

What is not enough is choosing a positive local density, absolute value, damping, or norm because it looks geometrically canonical. Those operations erase exactly the cancellation carrying Mangoldt support on mixed-prime shells.

## Status / novelty

Cyclotomic identities, logarithmic derivatives, Kron reduction, SPD geometry, positive energies, and radial integration are classical. The persisted synthesis is the stronger program gate: **even an exact prime-power positivity classifier does not become Weil positivity when the sparse selector is encoded in signed nonlocal cancellation; the final sign theorem must be produced only after that signed information has been assembled globally**.

## Falsification criterion

Construct a shellwise pointwise-positive scalarization of the WP-162 flux that still has exact Mangoldt support without importing the selector into the scalarization, or derive a source-specific finite--archimedean positive pairing from the signed flux family whose matched controls do not reproduce it.

## Lean-formalizable core

- Cyclotomic boundary-to-origin flux identity.
- Prime-power iff pointwise-positive flux classification.
- Mixed-prime sign-cancellation/total-variation obstruction.
- Logical separation of shell classifier from global Weil polarization.
