# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Separate the positive-order transport problem from the source-specific ground-sign problem

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-284 give the aperture ledger, terminating fixed-aperture positivity certificate, and a conditional endpoint at `a=0.8` with a simple isolated ground state. PL-285--PL-292 separate generic form/graph regularity from the much stronger all-log regularity of actual source-static eigenstates, but the optimized transport modulus remains sub-Hölder.

PL-293 shows that the universal Dirichlet logarithmic-Laplacian boundary channel blocks `H^(1/2)` and above when its natural `ell(t)^(1/2)` amplitude survives. PL-294 shows that ordinary Beurling--Deny positivity preservation ends at the archimedean aperture `a_BD`, before the first prime-power translation.

[PL-295](../findings/PL-295-hlog-hhalf-sign-cone-eventual-positivity-obstruction.md) now separates the two residuals more sharply. Even if the selected eigenbranch were upgraded to continuous `H^s` control for any `s<=1/2`, topology alone could not propagate fixed sign: arbitrarily small parity-preserving boundary perturbations can flip sign. And eventual/asymptotic semigroup positivity is circular for this purpose, because with a simple gapped ground state it forces positivity of the limiting ground projection and therefore already contains the missing sign theorem.

The **regularity** route remains useful only for transport: prove source-specific suppression of the universal boundary channel strongly enough to gain some `H^s`, `0<s<1/2`, or derive a non-absolute translation identity by another method. The **sign** route must use additional arithmetic eigen-equation structure—such as a boundary-weighted lower law, a source-specific maximum/oscillation principle, or an absolute-value defect—not merely continuity, parity, simplicity, a gap, or delayed positivity.

## Keep ambient topology, translation regularity and order structure separate

`H^log`/subcritical Sobolev control measures closeness, not membership in the positive cone. A spectral gap measures isolation, not order. Failure of Beurling--Deny positivity does not imply sign change, while eventual positivity strong enough to matter implies the desired ground sign. Future arguments should state explicitly whether they buy a translation modulus or a sign theorem; one no longer substitutes for the other.
