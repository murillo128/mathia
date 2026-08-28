# PC-001 — the common-vertex potential is exactly von Mangoldt

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE` (geometric organization).

## Claim

For the primitive/new-vertex shell

```text
P_n^* = {zeta : ord(zeta)=n}
```

define the logarithmic chord potential at the common vertex `1` by

```text
E_n = sum_{zeta in P_n^*} log|1-zeta|.
```

Since

```text
Phi_n(x) = prod_{zeta in P_n^*} (x-zeta),
```

one has exactly

```text
E_n = log|Phi_n(1)| = Lambda(n)    (n>1).
```

Thus `E_n=log p` on prime powers and `0` otherwise.

## Why it matters

The von Mangoldt source strength is already present as the exact interaction between the common vertex and the primitive shell; it is not inserted externally.

## Prior art / boundary

`Phi_n(1)=exp(Lambda(n))` is classical cyclotomic arithmetic. Consequently

```text
sum_{n>=2} E_n n^(-s) = -zeta'(s)/zeta(s)
```

is also classical and is not an independent RH mechanism.

## Research consequence

Any additional content must retain structure discarded by the scalar evaluation `U_n(1)`, for example the full two-dimensional potential field or genuinely nonlocal relations among shells.
