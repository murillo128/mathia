# PC-002 — primitive-shell resultants detect prime-power scale jumps

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `CLASSICAL-IDENTITY` + `CANDIDATE-NEW-STRUCTURE`.

## Claim

For distinct primitive layers `m<n`, let

```text
I_{m,n} = sum_{zeta in P_m^*} sum_{eta in P_n^*} log|zeta-eta|.
```

Then

```text
I_{m,n} = log|Res(Phi_m,Phi_n)|.
```

Apostol's resultant theorem gives, for `n>m>1`,

```text
|Res(Phi_m,Phi_n)| = p^phi(m)   if n/m=p^k,
                     1          otherwise,
```

and therefore, when `m|n`,

```text
I_{m,n} = phi(m) Lambda(n/m),
I_{m,n}/phi(m) = Lambda(n/m),
```

with zero interaction otherwise.

## Why it matters

The circle carries a canonical interaction graph on primitive layers whose nonzero couplings occur exactly across prime-power multiplicative jumps.

## Prior art / boundary

The cyclotomic resultant formula is classical. Replacing the interaction graph immediately by a Dirichlet transform would only repackage known arithmetic.

## Research consequence

The potentially additional structure lies in the full interaction operator/geometry before diagonal or scalar compression.
