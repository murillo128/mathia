# PF-011 — the spine zeta is essentially prime zeta

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `NEGATIVE/OBSTRUCTION`.

## Claim

The zero-twist spine distance satisfies

```text
d_n = (h_n+h_{n+1})/2
    = (1/2) log(u_{n+1}/u_{n-1}),
```

so a canonical radial position is

```text
R_n = (1/2) log(u_{n-1}u_n) + constant.
```

The corresponding point zeta

```text
Z_spine(s)=sum_n (u_{n-1}u_n)^(-s/2)
```

reduces, using `cot(pi/p)=(p/pi)(1+O(p^-2))`, to

```text
Z_spine(s)=pi^s P(s)+H(s),
```

where `P(s)=sum_p p^(-s)` is the classical prime zeta and `H` is holomorphic for `Re(s)>0`.

## Research consequence

The one-dimensional spine reaches Riemann-zero information only by reconstructing a known prime Dirichlet series. It is not an independent geometric mechanism.
