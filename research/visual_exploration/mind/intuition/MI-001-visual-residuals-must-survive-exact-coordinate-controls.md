# MI-001 — Visual residuals must survive deterministic quotients, statistical closures, ordering controls, and arithmetic-bearing boundary layers

**Evidence level:** supported through VIS-030 by exact reconstruction identities, classical statistical geometry, finite-population discrepancy controls, and exact Farey endpoint/totient reductions

## Core intuition

Visual complexity is not an independent arithmetic resource when it can be reconstructed from ordinary coordinates, lower-order statistics, symmetry, ordering baselines, or deterministic boundary geometry. The meaningful object is the residual after the strongest control preserving the information already known to generate the picture.

Farey discrepancy now adds an important qualification: a nuisance control can itself become arithmetic when enlarged across scale. A fixed endpoint layer is a legitimate deterministic null; progressively subtracting the whole endpoint hierarchy is not automatically neutral, because that hierarchy is a smoothed totient/Möbius channel.

## Strongest justified principle

VIS-013--VIS-025 classify circular reconstruction, Gram occupancy, sampled `S`, parity, and the first three-gap Markov/Pearson/correspondence residuals. VIS-026 keeps the centered gap multiset fixed and randomizes only order, giving an exact Brownian-bridge baseline; VIS-027 conditions additionally on reflection symmetry, which annihilates every odd Dirichlet mode.

VIS-028 identifies the first deterministic Farey boundary control. The unit-fraction endpoint fan occupies `Theta(n)` ranks, contributes `Theta(1/n)` discrepancy energy, and forces the observed `r=Theta(n)` even-mode scale by an explicit continuum transform.

VIS-029 shows that this fan is only the first chart of a full fixed-`nx` hierarchy. For every pre-fixed `Y`, all bounded-numerator endpoint layers converge to an explicit totient profile `K(y)` and produce the same `r=Theta(n)` spectral scale. Removing only the `Y=2` fan therefore does not isolate an interior arithmetic residual.

VIS-030 identifies the information contained in that hierarchy. `K(y)` is exactly a first-order Riesz/Cesaro mean of `phi(a)/a`, equivalently an integral of the summatory-totient remainder, with an exact finite Möbius decomposition and Dirichlet series `zeta(s)/zeta(s+1)`. Thus a pre-fixed finite endpoint window is an admissible control, but letting the endpoint cutoff grow until a residual stabilizes can subtract the very arithmetic cancellation one hoped to detect.

## What remains possible

For Farey discrepancy, either pre-register a finite family of endpoint cutoffs and demand residual stability across them, or prove that the full fixed-`nx` endpoint contribution is negligible for a chosen bulk statistic without assuming the target cancellation. Only then should surviving even-mode/cross-band structure be attributed to denominator strata, mediant ancestry, long-range gap order, or another interior mechanism.

For other visual branches the same rule applies: strengthen controls only while keeping explicit what information they preserve or remove, and convert any surviving pattern into a rendering-independent support, rank, conditioning, correlation-order, boundary, or scale statement.

## Status / novelty

The underlying Farey ranks, totient identities, Riesz means, Möbius convolution, statistical closures, and harmonic transforms are classical or persisted reductions. The synthesis is the visual gate: **a residual is meaningful only after deterministic controls are matched, but a growing control must itself be audited so it does not absorb the arithmetic signal**.

## Falsification criterion

Show that the fixed-`nx` endpoint hierarchy does not produce the VIS-029 profile or modal scale, or exhibit a bulk residual stable under pre-fixed endpoint controls whose claimed signal can nevertheless be reconstructed from the same totient/Riesz channel.

## Lean-formalizable core

- Gram occupancy/S/parity quotient.
- Same-gap permutation and reflection controls.
- Fixed-`nx` Farey endpoint rank asymptotic.
- Endpoint Dirichlet scaling.
- Riesz/totient/Möbius identities for the growing endpoint profile.
