# PF-002 — local scalar cuff observables lose the fine gaps

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `NEGATIVE/OBSTRUCTION`.

## Claim

If a local observable has a uniform small-mesh expansion

```text
F(h,z) = A(z) h + O(h^2),
```

then PF-001 and `sum h_n^2<infinity` give

```text
sum_{n=m}^N F(h_n,z)
  = A(z) log(u_N/u_{m-1}) + C_F(z) + o(1).
```

The divergent term is endpoint-only; intermediate prime gaps survive only in a convergent correction.

A concrete exact example is

```text
prod_{n=m}^N coth(ell_n/4) = sqrt(u_N/u_{m-1}).
```

## Research consequence

A zeta or determinant that factorizes independently cuff-by-cuff is structurally prone to erase relational prime information.
