# PL-002 — Standard `H^2` kernel cannot see nontrivial zeta zeros

## Claim

For the standard Hilbert space of Dirichlet series with square-summable coefficients, the reproducing kernel is

```text
K(s,w) = zeta(s + conj(w)),
```

with

```text
Re(s) > 1/2,
Re(w) > 1/2.
```

Therefore

```text
Re(s + conj(w)) > 1,
```

so the kernel is evaluated only in the Euler-product zero-free half-plane. In particular, **kernel zeros or orthogonality of the standard Bohr-Hardy evaluation states cannot encode the nontrivial zeros of the Riemann zeta function**.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

The kernel formula is standard/elementary in the Hedenmalm–Lindqvist–Seip Hilbert space; the obstruction is the exact consequence derived in the completed investigation.

## Derivation already established in the investigation

For a bounded evaluation point `w`, the kernel vector has Dirichlet coefficients

```text
n^{-conj(w)}.
```

Hence

```text
K(s,w)
  = sum_{n>=1} n^{-s} n^{-conj(w)}
  = sum_{n>=1} n^{-(s+conj(w))}
  = zeta(s+conj(w)).
```

The standard point-evaluation domain requires `Re(s), Re(w)>1/2`. It follows immediately that

```text
Re(s+conj(w)) > 1.
```

The Euler product converges there and `zeta` has no zeros there. Thus

```text
K(s,w) != 0
```

throughout the standard reproducing-kernel domain.

Equivalently, if `k_s` and `k_w` are the evaluation kernel states, then

```text
<k_w, k_s> = K(s,w)
```

never vanishes in their natural domain. The tempting interpretation

```text
Riemann zero <-> orthogonality of two ordinary Bohr-Hardy evaluation states
```

is therefore impossible in this setting.

## Relevance to the Mathia construction

`PL-001` shows that the standard Bohr-Hardy geometry naturally singles out the critical-line value `1/2`. This finding shows the limitation of that fact: the canonical kernel built from the same geometry never reaches the nontrivial zero set.

The result cleanly separates

```text
having a natural 1/2 boundary
```

from

```text
having a spectral mechanism for zeta zeros.
```

## Prior art and novelty assessment

The Hilbert space and its reproducing-kernel structure are standard Dirichlet-series theory. No novelty is claimed for the formula `K(s,w)=zeta(s+conj(w))`.

The durable Mathia-specific conclusion is negative: **the most direct kernel-orthogonality route from the prime-lattice/Bohr picture to RH is structurally blocked before the critical strip is reached**.

## Boundary conditions and scope of the negative result

This obstruction is deliberately narrow and exact. It rules out only mechanisms that stay inside the standard square-summable Dirichlet-series reproducing-kernel space and try to identify nontrivial zeros with zeros/orthogonality of its ordinary evaluation kernels.

It does **not** rule out:

- a different Hilbert or Krein space;
- a renormalized boundary object;
- a different operator acting on prime-coordinate data;
- an adelic/noncommutative enlargement;
- analytic-continuation machinery not represented by ordinary bounded point evaluations.

None of those alternatives was established as a positive finding in the completed investigation.

## Audit criterion

The obstruction is falsified only if one can exhibit `s,w` inside the standard bounded-evaluation domain such that

```text
zeta(s+conj(w)) = 0.
```

That would require a zeta zero with real part strictly greater than `1`, contradicting the classical Euler-product zero-free region. Thus the stated kernel route is decisively excluded under its own hypotheses.

## Consequence for the research line

The standard Bohr `H^2` geometry can explain why `1/2` is a natural boundary, but **its canonical reproducing kernel cannot be the missing zero detector**. Any viable spectral interpretation must introduce genuinely additional structure rather than merely reinterpret the same kernel.
