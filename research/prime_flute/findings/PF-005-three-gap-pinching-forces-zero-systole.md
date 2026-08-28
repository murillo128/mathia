# PF-005 — a tiny gap between two much larger gaps forces zero systole

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `LITERATURE+DERIVED`; the topological identification remains an explicit audit boundary.

## Claim

Pintz supplies a three-gap subsequence on which the central gap is tiny relative to both neighbors. Applying PF-004 to four consecutive endpoint blocks gives asymptotically

```text
chi_n ~ g_n/g_{n-1} + g_n/g_{n+1}
        + g_n^2/(g_{n-1}g_{n+1}),
```

hence along that subsequence

```text
chi_n -> 0,
L_n = 4 asinh(sqrt(chi_n)) -> 0.
```

The quantitative estimate recorded in the legacy ledger is

```text
L_n = o((log n)^(-1/1264)).
```

If the corresponding words are the expected distinct simple primitive separating classes, then `sys(X_prime)=0` and there are infinitely many primitive geodesics below every positive length threshold.

## Audit boundary

PF-004 settles the matrix length. The simple/primitive/separating topological identification must be stated independently before using the final systolic conclusion as a theorem.
