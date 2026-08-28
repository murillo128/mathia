# PF-003 — canonical shears retain consecutive-gap irregularity

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `LITERATURE+DERIVED`.

## Claim

Let

```text
Delta_n = u_{n+1}-u_n,
sigma_n = log(Delta_{n+1}/Delta_n).
```

This is the standard fan shear. Since

```text
Delta_n = (g_n/pi)(1+O(p_n^-2)),
```

one has

```text
sigma_n = log(g_{n+1}/g_n) + o(1).
```

Pintz's consecutive-gap-ratio theorem therefore yields

```text
liminf sigma_n = -infinity,
limsup sigma_n = +infinity.
```

At the same time

```text
sigma_n = phi_{n+1}-phi_n,   phi_n=log Delta_n,
```

so a nearest-neighbour potential built only from the one-step shear is a coboundary and telescopes.

## Why it matters

The shear sequence retains relative gap irregularity, but its raw one-step scalarization does not automatically produce a nontrivial global invariant.
