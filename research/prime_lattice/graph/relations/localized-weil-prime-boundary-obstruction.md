---
id: RGR-PL-WEIL-BOUNDARY-001
type: research-graph-relation
scope: prime_lattice
relation: localized-weil-prime-boundary-obstruction
derived: true
---

# Localized Weil prime operator: topology-sensitive boundary obstruction

[[research/prime_lattice/findings/PL-049-weil-prime-shift-norm-exponential-obstruction|PL-049]] proves that the localized non-archimedean Weil prime operator retains exponential operator-norm scale. [[research/prime_lattice/findings/PL-050-rescaled-weil-prime-boundary-escape|PL-050]] then shows that natural fixed-window rescaling has zero bulk strong limit while order-one spectral edges escape into shrinking endpoint layers.

The boundary blow-up sequence makes the topology split explicit:

- [[research/prime_lattice/findings/PL-051-weil-boundary-rank-one-pnt-model|PL-051]] gives a universal rank-one PNT Hankel model as the fixed-depth strong boundary limit.
- [[research/prime_lattice/findings/PL-052-weil-boundary-kronecker-norm-gap|PL-052]] shows that prime-log recurrence prevents operator-norm convergence to that universal model.
- [[research/prime_lattice/findings/PL-053-weil-boundary-essential-norm-obstruction|PL-053]] strengthens the obstruction to the Calkin quotient: compact counterterms cannot remove the residual.
- [[research/prime_lattice/findings/PL-054-weil-threshold-delta-hankel-essential-channel|PL-054]] shows that individual prime-power thresholds enter as infinite-multiplicity essential delta-Hankel channels rather than discrete eigenvalue births.
- [[research/prime_lattice/findings/PL-055-fixed-sobolev-weil-boundary-smoothing|PL-055]] closes the simplest smoothing escape: every fixed compact Sobolev smoothing removes the high-frequency recurrence and upgrades the same universal PNT boundary model to norm, and in the stated range Schatten, convergence.

The source-backed boundary is therefore:

```text
bulk strong topology       -> arithmetic escapes / limit is zero
fixed-depth strong blow-up -> universal PNT rank-one model
norm and Calkin topology   -> prime-log recurrence survives essentially
fixed compact smoothing    -> recurrence is erased and the universal model returns
```

This closes neither the full localized Weil operator nor an `L`-dependent mesoscopic/relative topology derived independently of the zeros. The current synthesis identifies precisely that intermediate topology as the surviving route.