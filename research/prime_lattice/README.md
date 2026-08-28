# Prime-lattice research notes

This directory preserves high-signal findings from the **prime-exponent / Bohr-geometry** research line so they can be reused later by Mathia, independent review, and formalization.

The intrinsic arithmetic object is the unique-factorization exponent vector

```text
n = product_p p^{v_p(n)}
v(n) = (v_2(n), v_3(n), v_5(n), ...)
```

with finite support. Multiplication becomes vector addition, primes are coordinate basis directions, and square-free integers are the finite-support vertices of the infinite `{0,1}` hypercube. The logarithmic size is the linear functional

```text
log n = sum_p v_p(n) log p.
```

Under the classical Bohr correspondence, a Dirichlet series becomes a power series in prime coordinates. The one-complex-dimensional curve relevant to ordinary Dirichlet series is

```text
s = sigma + i t  ->  z(s) = (p^{-s})_p
                     = (p^{-sigma} e^{-i t log p})_p,
```

so vertical translation is a Kronecker-type flow with frequencies `log p`.

## Research stance

The exponent-vector representation, the square-free Boolean hypercube, the Euler-product factorization, and the classical Bohr lift are **baseline prior art**, not Mathia discoveries. A durable finding in this branch must add a precise consequence, obstruction, boundary condition, or prior-art redirect that materially changes what a geometric or spectral RH mechanism could be.

In particular, identities that hold only in `Re(s) > 1` must not be silently promoted into statements about the critical strip. Analytic continuation is a genuine boundary in the problem, not a coordinate change that can be ignored.

## Evidence labels

- **EXACT-DERIVED** — exact consequence derived from the explicit prime-lattice/Bohr setup.
- **LITERATURE+DERIVED** — a published theorem or standard construction plus a derived consequence for this research line.
- **CLASSICAL-IDENTITY** — exact structure already present in the literature; retained when its prior-art status materially redirects the investigation.
- **NEGATIVE/OBSTRUCTION** — rules out or sharply narrows a natural mechanism.
- **DECISIVE-NEGATIVE** — decisively kills a specifically stated route under its stated hypotheses.
- **CONJECTURAL** / **NEEDS-AUDIT** — reserved for claims that remain unproved or insufficiently sourced.

These labels describe provenance and certainty, not importance.

## Files

- [`FINDINGS.md`](FINDINGS.md) — compact index of durable positive and negative results.
- [`SOURCES.md`](SOURCES.md) — literature anchors used by the stored findings.
- [`findings/`](findings/) — detailed `PL-NNN-*` finding notes.

The separate Mathia mind process owns `mind/` synthesis; this evidence branch does not maintain intuitions, research lines, project status, or chronological logs.

## Durable high-level picture

The completed investigation established a useful separation:

```text
standard Bohr/Hardy geometry
    -> naturally singles out Re(s) = 1/2 as a Hilbert-space evaluation boundary

standard H^2 reproducing kernel
    -> remains entirely in the zero-free half-plane and cannot encode nontrivial zeros by kernel orthogonality

ambient prime torus + log-prime frequencies alone
    -> too flexible: Helson twists can have radically different zero/pole behavior
```

Thus the bare prime-exponent lattice and infinite torus are not, by themselves, a zero mechanism for the Riemann zeta function. Any viable continuation of this viewpoint must use additional structure that distinguishes the Riemann zeta function from generic multiplicative twists and genuinely survives passage to the critical strip.