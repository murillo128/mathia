# PF-001 — exact cuff coordinate

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `EXACT-DERIVED`, using the standard zero-twist tight-flute length formula.

## Claim

With

```text
u_n = cot(pi/p_n),
h_n = log(u_n/u_{n-1}),
```

the canonical cuff length satisfies

```text
ell_n = 2 log((sqrt(u_n)+sqrt(u_{n-1}))/(sqrt(u_n)-sqrt(u_{n-1})))
```

and exactly

```text
exp(-ell_n/2) = tanh(h_n/4).
```

Also

```text
sum_{n=m}^N h_n = log(u_N/u_{m-1}).
```

Using `u_p~p/pi` and the Baker–Harman–Pintz gap bound gives `sum_n h_n^2<infinity`.

## Why it matters

`h_n` is the natural logarithmic mesh coordinate. It separates telescoping first-order motion from higher-order gap fluctuations.

## Boundary / formal core

The finite algebra and telescoping identity are exact. Square summability imports analytic number theory and should remain a separate theorem bridge.
