# PC-003 — exact harmonic interior/exterior duality of primitive-shell potentials

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `EXACT-DERIVED` + `CANDIDATE-NEW-STRUCTURE`.

## Claim

Define

```text
U_n(z) = log|Phi_n(z)|
       = sum_{zeta in P_n^*} log|z-zeta|.
```

Away from the unit-circle charges, `U_n` is harmonic. Cyclotomic reciprocity yields the exact inversion law

```text
U_n(z) = phi(n) log|z| + U_n(1/conj(z)).
```

At the common boundary vertex,

```text
U_n(1) = Lambda(n)
```

by PC-001.

The full-polygon and primitive-shell fields also satisfy the divisor/Möbius decomposition

```text
log|z^n-1| = sum_{d|n} U_d(z),
U_n(z) = sum_{d|n} mu(n/d) log|z^d-1|
```

away from singularities.

## Why it matters

This preserves the original circle's intrinsic inside/outside coupling while retaining the primitive/new-vertex shell as the charge distribution.

## Boundary

The inversion is spatial. It does not by itself imply the zeta functional-equation reflection in the scale variable.

## Research consequence

A substantive continuation must use information in the field, its interior/exterior coupling, modes, or nonlinear scale relations that is lost by evaluating only at `z=1` or immediately applying an ordinary Dirichlet transform.
