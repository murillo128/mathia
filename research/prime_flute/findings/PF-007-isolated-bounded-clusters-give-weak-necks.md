# PF-007 — isolated bounded clusters give arbitrarily weak necks

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `LITERATURE+DERIVED`.

## Claim

Pintz supplies arbitrarily large bounded clusters of consecutive primes preceded and followed by prime-free intervals whose lengths grow. For geometric exterior gaps `X,Z` and bounded internal span `Y`, PF-004 gives exactly

```text
sinh(L/4)^2 = Y(1/X + 1/Z + Y/(XZ)).
```

Therefore

```text
X,Z -> infinity, Y=O(1)  =>  L->0.
```

Using `u_q-u_p~(q-p)/pi`, an arithmetic block of internal diameter `D` and exterior gaps `G_L,G_R` has the pinching asymptotic

```text
L ~ 4 sqrt(D(1/G_L + 1/G_R)).
```

## Why it matters

This is a genuinely multi-gap geometric mechanism: an isolated bounded prime cluster becomes an almost-decoupled hyperbolic island.
