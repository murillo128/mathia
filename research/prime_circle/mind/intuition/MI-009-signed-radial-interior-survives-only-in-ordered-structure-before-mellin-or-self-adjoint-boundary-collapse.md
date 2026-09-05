# MI-009 — Signed radial interior survives only in ordered structure before Mellin or self-adjoint boundary collapse

**Evidence level:** supported through PC-180 by exact cyclotomic flux identities, Mellin factorization, and the flux--potential integration-by-parts decomposition

## Core intuition

The signed cyclotomic radial flux is a real prime-power selector, but the obvious ways of turning it into a scalar or positive spectral object erase the new information before it can constrain zeros. Shellwise Mellinization inserts the same classical `zeta` factor for every shell, while the simplest symmetric cross-shell flux--potential pairing collapses its entire self-adjoint part to a rank-one von-Mangoldt endpoint form.

The only genuinely new datum surviving these first operations is **ordered radial interior information**: the antisymmetric part of the cross-shell pairing. It is non-coercive by itself, so a positive continuation must derive an additional source-forced operation before symmetrization or endpoint reduction.

## Strongest justified principle

PC-179 reconstructs the exact inward flux

`rho_n(x)=-d/dx log Phi_n(e^{-x})`.

It is pointwise positive exactly on prime powers and has total mass `Lambda(n)`. Yet its Mellin transform is

`-Gamma(s) zeta(s) n^(1-s) prod_{p|n}(1-p^(s-1))`.

Throughout the open critical strip the finite factor never vanishes, so every shell has exactly the same nontrivial zeta zeros. The `n=2` control is already the classical `Gamma(s) eta(s)` integral. Pointwise positivity and the Mellin half-density therefore do not provide a new zero-selection mechanism.

PC-180 couples shells before Mellinization via `A_mn=int rho_m F_n`. Integration by parts gives

`Sym A = (1/2) Lambda Lambda^T`.

Hence every radial-coordinate-independent real symmetric shell mixer produces only the classical quadratic form `Lambda^T C Lambda/2`. The radial interior survives solely in `Omega=(A-A^T)/2`, and `a^T Omega a=0` for every real amplitude vector.

## What remains possible

The no-go does not cover a source-forced radial-depth-dependent mixer, a genuinely nonlocal kernel coupling different depths, nonlinear use of the ordered matrix, a second intrinsic skew/noncommuting structure that can pair with `Omega`, or a growing/infinite-shell limit whose domain is part of the construction.

Any such continuation must preserve the cancellation on mixed-prime controls and obtain a self-adjoint/sign margin not inherited from the universal eta/zeta Mellin factor or the endpoint `Lambda` vector.

## Status / novelty

Cyclotomic logarithmic derivatives, Ramanujan Dirichlet series, Mellin eta/zeta integrals, and integration by parts are classical. The persisted synthesis is the Prime-Circle operation-order boundary: **scalar Mellinization classicalizes the zero set, constant symmetric first-order shell coupling endpoint-collapses, and only ordered interior data remain available for a genuinely new operation**.

## Falsification criterion

Find a shell whose Mellin flux has a nontrivial critical-strip zero not coming from zeta, a constant symmetric flux--potential coupling whose value depends on radial interior beyond `Lambda`, or a source-natural operation on the ordered sector producing a nonclassical self-adjoint margin while surviving matched shell controls.

## Lean-formalizable core

- Finite cyclotomic flux divisor formula and prime-power positivity criterion.
- Critical-strip nonvanishing of the finite Mellin factor.
- `A+A^T=Lambda Lambda^T` and vanishing real quadratic form of the antisymmetric sector.
