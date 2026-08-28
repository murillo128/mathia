# PF-013 — Poisson/logistic shear background is zero-free

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `CONJECTURAL` as a prime model; exact as the stated probability calculation.

## Claim

If normalized consecutive gaps are modeled by independent exponential variables `X_n` and

```text
sigma_n=log X_{n+1}-log X_n,
```

then `sigma_n` has logistic density

```text
f(x)=1/(4 cosh(x/2)^2).
```

With `nu=2s-1`, its moment transform is

```text
K(s)=E exp((2s-1)sigma)
    =Gamma(2s) Gamma(2-2s),
```

which converges for `0<Re(s)<1`, satisfies `K(s)=K(1-s)`, and is zero-free because Gamma has no zeros.

On the critical line,

```text
K(1/2+it)=2 pi t/sinh(2 pi t).
```

## Research consequence

A Poisson/logistic background can reproduce the strip and reflection symmetry but not the Riemann zeros. If shear dynamics matter, zero structure must come from non-Poisson arithmetic correlations rather than this background model alone.
