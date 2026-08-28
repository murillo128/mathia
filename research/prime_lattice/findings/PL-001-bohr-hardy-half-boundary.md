# PL-001 — Bohr-Hardy evaluation boundary is `Re(s)=1/2`

## Claim

In the standard Hedenmalm–Lindqvist–Seip Hilbert space

```text
H = { f(s) = sum_{n>=1} a_n n^{-s} : sum_n |a_n|^2 < infinity },
```

point evaluation at `s = sigma + i t` is bounded exactly when

```text
sigma > 1/2.
```

Equivalently, along the Bohr curve

```text
z(s) = (p^{-s})_p,
```

the critical line `Re(s)=1/2` is the exact boundary at which the prime-coordinate point leaves the natural `ell^2` domain.

Cole–Gamelin's infinite-polydisk Hardy theory strengthens the interpretation: for every fixed `0 < p < infinity`, continuity of point evaluation in the standard `H^p`/`L^p` Hardy norm occurs exactly on `Delta^infinity intersect ell^2`. Hence the same prime curve has the same `Re(s)=1/2` evaluation boundary throughout the classical infinite-polydisk Hardy scale, not only at Hilbert exponent `p=2`.

**Evidence/status:** `LITERATURE+DERIVED`.

This is standard infinite-polydisk/Dirichlet-series Hardy theory plus an exact specialization to the prime-lattice curve. No novelty is claimed for the underlying theory.

## Derivation

For

```text
f(s) = sum_n a_n n^{-s}
```

with `(a_n) in ell^2`, Cauchy–Schwarz gives

```text
|f(s)| <= (sum_n |a_n|^2)^(1/2) (sum_n n^{-2 sigma})^(1/2).
```

Hence the evaluation functional has squared norm

```text
sum_n n^{-2 sigma} = zeta(2 sigma),
```

which is finite exactly for `2 sigma > 1`.

Hedenmalm–Lindqvist–Seip identify this Dirichlet-series Hilbert space with `H^2` on the infinite-dimensional polydisk/character space. Under the Bohr map,

```text
z_p(s) = p^{-s} = p^{-sigma} e^{-i t log p},
```

so

```text
sum_p |z_p(s)|^2 = sum_p p^{-2 sigma}.
```

The prime sum converges exactly for `sigma > 1/2`. Thus the same `1/2` threshold is visible directly in prime-coordinate geometry.

Cole and Gamelin independently characterize the analytic domain of the classical infinite-polydisk Hardy spaces: for each fixed `0 < p < infinity`, point evaluation at `zeta` is continuous in the `L^p` Hardy norm exactly when

```text
zeta in Delta^infinity intersect ell^2.
```

Specializing again to `z(s)=(p^{-s})_p` gives

```text
z(s) in ell^2
    <=> sum_p p^{-2 sigma} < infinity
    <=> sigma > 1/2.
```

Therefore the value `1/2` is not an artifact of having chosen the coefficient Hilbert norm `ell^2` and then applying Cauchy–Schwarz: it is also the common point-evaluation domain of the standard `H^p` theory on the infinite polydisk.

## Relevance to the Mathia construction

The prime-exponent representation makes `log n` the linear functional

```text
log n = sum_p v_p(n) log p,
```

and vertical translation `t` becomes simultaneous rotation of prime coordinates with frequencies `log p`. Within that standard geometry, `Re(s)=1/2` is not inserted by hand: it is the square-summability boundary of the Bohr curve and, by Cole–Gamelin, the Hardy evaluation boundary across the standard infinite-polydisk `H^p` scale.

This is a genuine structural coincidence with the Riemann critical line, but it is **not** evidence that zeta zeros are forced to lie there.

## Functional-equation coordinate coincidence

The investigation also noted the exact coordinate restatement

```text
J(z)_p = 1 / (p * conj(z_p)).
```

On the Bohr curve,

```text
J(z(s)) = z(1 - conj(s)).
```

Its fixed locus on that curve is exactly `Re(s)=1/2`. This is retained only as a boundary observation: it is the usual functional reflection written in prime coordinates, not an independent RH mechanism or novelty claim.

## Prior art and novelty assessment

The underlying Bohr lift and square-summable Dirichlet-series theory are classical; Hedenmalm–Lindqvist–Seip (1997) is the main Dirichlet-series anchor. Cole–Gamelin (1986) already establish the stronger `ell^2` point-evaluation domain for the infinite-polydisk Hardy scale `0<p<infinity`.

The Mathia-specific value is organizational: the same prime-coordinate model that linearizes multiplication also makes the RH value `1/2` appear as a canonical, `p`-robust Hardy-space boundary.

No claim is made that this coincidence is new in the literature.

## Boundary conditions and failure modes

- The bounded-evaluation statements concern standard Hardy spaces; they do not prove anything about the zero set of `zeta`.
- The argument does not continue point evaluation through the boundary; it explicitly identifies where the standard evaluation geometry stops.
- `H^p` robustness removes one easy objection — that `1/2` was chosen merely by the Hilbert exponent — but supplies no zero-localizing mechanism.
- The fixed-locus formula for `J` adds no independent content unless extra analytic or operator structure is supplied.
- Any proposed RH mechanism using this finding must still explain analytic continuation and why the Riemann zeta function is distinguished among multiplicative Dirichlet series.

## Audit criterion

For `H^2`, the exact claim is checked by

```text
||ev_s||^2 = zeta(2 Re(s)).
```

For the broader infinite-polydisk Hardy scale, the audit is Cole–Gamelin's criterion

```text
point evaluation at z is continuous <=> z in Delta^infinity intersect ell^2.
```

Any stronger RH interpretation must be rejected unless it supplies mathematically defined structure at or beyond the `Re(s)=1/2` boundary rather than merely reusing the same evaluation domain.

## Consequence for the research line

`Re(s)=1/2` is a legitimate intrinsic boundary of standard Bohr-Hardy geometry, and that boundary is stable across the classical `H^p` scale. This makes the value `1/2` structurally relevant, but by itself it does not turn the prime lattice into a spectral explanation of the Riemann zeros.
