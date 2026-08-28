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

**Evidence/status:** `LITERATURE+DERIVED`.

This is a standard Hilbert-space/Bohr construction plus an exact specialization to the prime-lattice curve. No novelty is claimed for the underlying theory.

## Derivation already established in the investigation

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

## Relevance to the Mathia construction

The prime-exponent representation makes `log n` the linear functional

```text
log n = sum_p v_p(n) log p,
```

and vertical translation `t` becomes simultaneous rotation of prime coordinates with frequencies `log p`. Within that standard geometry, `Re(s)=1/2` is not inserted by hand: it is the natural square-summability boundary for the Bohr curve.

This is a genuine structural coincidence with the Riemann critical line, but it is **not** evidence that zeta zeros are forced to lie there.

## Functional-equation coordinate coincidence

The completed investigation also noted the exact coordinate restatement

```text
J(z)_p = 1 / (p * conj(z_p)).
```

On the Bohr curve,

```text
J(z(s)) = z(1 - conj(s)).
```

Its fixed locus on that curve is exactly `Re(s)=1/2`. This is retained only as a boundary observation: it is the usual functional reflection written in prime coordinates, not an independent RH mechanism or novelty claim.

## Prior art and novelty assessment

The underlying Bohr lift and `H^2` Dirichlet-series theory are classical; the main source is Hedenmalm–Lindqvist–Seip (1997). The Mathia-specific value of the observation is organizational: the same prime-coordinate model that linearizes multiplication also makes the RH value `1/2` appear as a canonical Hilbert-space boundary.

No claim is made that this coincidence is new in the literature.

## Boundary conditions and failure modes

- The bounded-evaluation statement is about the standard square-summable-coefficient Hilbert space, not a proof about the zero set of `zeta`.
- The argument does not continue point evaluation through the boundary; it explicitly identifies where the standard bounded-evaluation geometry stops.
- The fixed-locus formula for `J` adds no independent content unless extra analytic or operator structure is supplied.
- Any proposed RH mechanism that uses this finding must still explain analytic continuation and why the Riemann zeta function is distinguished among multiplicative Dirichlet series.

## Audit criterion

The exact claim is checked by the evaluation norm

```text
||ev_s||^2 = zeta(2 Re(s)).
```

Any stronger interpretation must be rejected unless it supplies a mathematically defined structure at or beyond the `Re(s)=1/2` boundary rather than merely reusing the same bounded point evaluations.

## Consequence for the research line

`Re(s)=1/2` is a legitimate intrinsic boundary of standard Bohr-Hardy geometry. This makes the value `1/2` structurally relevant, but by itself it does not turn the prime lattice into a spectral explanation of the Riemann zeros.
