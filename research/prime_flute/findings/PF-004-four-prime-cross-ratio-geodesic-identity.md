# PF-004 — exact four-prime cross-ratio/geodesic identity

> Retroactive persistence from the legacy `FINDINGS.md`; no new mathematical claim or evidence upgrade is introduced here.

**Status:** `EXACT-DERIVED`.

## Claim

For `a<b<c<d`, with the standard zero-twist generator `G(a,b)`, define

```text
chi(a,b,c,d) = ((c-b)(d-a))/((b-a)(d-c)).
```

Direct matrix algebra gives

```text
tr(G(a,b) G(c,d)^(-1)) = -2-4 chi.
```

If `L` is the corresponding hyperbolic translation length,

```text
cosh(L/2)=1+2 chi,
sinh(L/4)^2=chi,
L=4 asinh(sqrt(chi)).
```

Writing `X=b-a`, `Y=c-b`, `Z=d-c` gives

```text
sinh(L/4)^2 = Y(X+Y+Z)/(XZ).
```

For prime endpoints, this is an exact Möbius-invariant bridge from several prime gaps to a genuine separating geodesic.

## Formal/audit core

Determinant one, the trace identity, positivity of `chi`, and the elementary trace-to-length conversion can be checked independently.
