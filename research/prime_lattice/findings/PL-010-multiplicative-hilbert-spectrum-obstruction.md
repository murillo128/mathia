# PL-010 — The canonical multiplicative Hilbert operator is a zero-insensitive Carleman-type spectral model

## Claim

There is already a canonical **non-diagonal** operator attached to the multiplicative/Bohr geometry whose kernel is built directly from the Riemann zeta function and whose matrix is multiplicative Hankel in the integer basis. Its spectral theory is classical and rigorous, but it does **not** expose the nontrivial zeta zeros.

On the Hilbert space `mathcal H^2_0` of Dirichlet series

```text
f(s)=sum_{n>=2} a_n n^(-s),
||f||^2=sum_{n>=2}|a_n|^2,
```

Brevig--Perfekt--Seip--Siskakis--Vukotic define

```text
H f(s)=integral_{1/2}^infinity f(w) (zeta(s+w)-1) dw.
```

With respect to the orthonormal basis `(n^(-s))_{n>=2}`, its matrix is

```text
M_{m,n}=1/(sqrt(m n) log(m n)),   m,n>=2.
```

This is a Helson/multiplicative Hankel matrix and, under the Bohr lift, a bona fide small Hankel operator on the infinite torus `T^infinity`.

The established spectral theorem is:

```text
H is bounded and strictly positive,
||H||=pi,
H has no eigenvalues,
spec(H)=[0,pi] and is purely continuous.
```

Perfekt--Pushnitski subsequently proved that the spectrum is in fact purely absolutely continuous with multiplicity one and no singular continuous part.

For the prime-lattice program this gives a decisive negative for a natural spectral route: **the most canonical non-diagonal zeta-kernel operator arising from the Bohr/Helson structure has no point spectrum at all, and its ordinary spectrum is the classical Hilbert/Carleman continuum rather than a spectral encoding of the Riemann zeros.**

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE`.

No novelty is claimed for the operator or its spectral theorem. The Mathia-specific consequence is the audited obstruction and prior-art redirect: after `PL-009` ruled out the canonical diagonal Fredholm-regularization route, simply passing to the canonical non-diagonal multiplicative Hankel/zeta-kernel operator does not supply an RH zero mechanism either.

## Exact prime-lattice form

Write

```text
E(n)=log n=<v(n),(log p)_p>.
```

Then

```text
M_{m,n}
 = exp(-(E(m)+E(n))/2)/(E(m)+E(n)).
```

Equivalently,

```text
M_{m,n}=integral_{1/2}^infinity (m n)^(-w) dw.
```

Since

```text
E(mn)=E(m)+E(n),
```

this matrix depends on the sum of lattice energies, or equivalently on the product `mn`. It is therefore an intrinsic multiplicative Hankel kernel of the exponent lattice rather than an externally imposed additive matrix.

The identity also exhibits `M` as a positive Gram/embedding operator: if

```text
(J a)(w)=sum_{n>=2} a_n n^(-w),  w>1/2,
```

then formally and, by the cited bounded embedding theorem, rigorously,

```text
M=J* J.
```

Thus this operator is one of the most direct positive non-diagonal spectral constructions available from the Bohr-Hardy geometry.

## Why its zeta kernel does not sample the critical zeros

For `Re(s)>1/2` and real `w>1/2`,

```text
Re(s+w)>1.
```

Hence every value

```text
zeta(s+w)-1
```

appearing in the integral kernel is evaluated strictly inside the ordinary Euler-product half-plane, where zeta is zero-free. The operator reaches the singular boundary only as `s,w -> 1/2`, when `s+w -> 1`.

Set

```text
x=s-1/2,
y=w-1/2.
```

Near `x+y=0`,

```text
zeta(1+x+y)-1
 = 1/(x+y) + analytic remainder.
```

The cited 2016 analysis explicitly uses the fact that

```text
zeta(z)-1/(z-1)
```

is entire to relate `H` to the classical Carleman operator with kernel

```text
1/(x+y).
```

This is the key structural audit: the singularity that drives the boundary spectral behavior is the **pole at `s=1`**, not the nontrivial zero divisor in the critical strip.

## Prior-art spectral theorem

Brevig et al. proved that `H` has norm `pi`, is strictly positive, has no eigenvalues, and has purely continuous spectrum `[0,pi]`. Their proof explicitly compares the boundary singularity with the classical Carleman/Hilbert operator and uses Mellin-transform methods.

Perfekt and Pushnitski then applied spectral perturbation and scattering theory to prove that the spectrum has no singular continuous component and that the absolutely continuous spectrum has multiplicity one.

Thus even after introducing:

```text
non-diagonality
+ multiplicative Hankel structure
+ a zeta-valued kernel
+ operator-theoretic scattering methods,
```

the ordinary spectrum remains a featureless interval rather than a discrete set related to zero ordinates.

## Relevance to the earlier findings

`PL-002` showed that the standard `H^2` reproducing kernel `zeta(s+conj(w))` stays in `Re>1` and cannot encode nontrivial zeros through kernel orthogonality.

`PL-009` showed that the canonical diagonal one-particle determinant regularization available for `Re>1/2` is zero-free and removes the prime-zeta term that can carry zero singularities.

The multiplicative Hilbert operator is a substantially different test: it is non-diagonal and genuinely Hankel, with matrix entries coupling all pairs `(m,n)` through the lattice energy `E(m)+E(n)`. Nevertheless its zeta kernel again remains in `Re>1`, and its spectrum is governed by the boundary pole/Carleman singularity.

So **non-diagonality by itself is not the missing structure**. A successful spectral route must do more than replace the diagonal prime Hamiltonian by the most natural positive multiplicative Hankel coupling.

## Prior art and novelty assessment

- Ole Fredrik Brevig, Karl-Mikael Perfekt, Kristian Seip, Aristomenis G. Siskakis, and Dragan Vukotic introduced and analyzed the multiplicative Hilbert matrix in 2016. The Bohr-lift interpretation as a small Hankel operator on `T^infinity`, the zeta-kernel representation, positivity, norm `pi`, and spectrum `[0,pi]` are their results.
- Karl-Mikael Perfekt and Alexander Pushnitski proved in 2018 that its spectrum is purely absolutely continuous of multiplicity one, using spectral perturbation and scattering theory.
- The analogy with the classical Hilbert/Carleman operator is explicit in the original paper; it is not a Mathia discovery.

The only new content retained here is the branch-level consequence: this literature already realizes one of the most obvious proposed escapes from the diagonal prime-lattice obstruction, and shows that it remains spectrally insensitive to the Riemann zero set.

## Boundary conditions and counterarguments

- This finding rules out **reading the Riemann zeros from the ordinary spectrum or eigenvalues of this specific canonical multiplicative Hilbert operator**. It does not rule out all Helson matrices or all non-diagonal operators.
- The later use of scattering theory to establish spectral type does not imply that every conceivable scattering invariant of every related operator is zero-insensitive. No claim is made here about an independently constructed scattering determinant or phase that samples analytically continued zeta data.
- The operator kernel uses `zeta(s+w)-1` only for `Re(s+w)>1`. A different operator that canonically samples the analytically continued completed zeta function in the critical strip would not be covered by this obstruction.
- The fact that the spectrum is `[0,pi]` does not prove that every matrix element or generalized eigenfunction is arithmetically trivial. The negative claim is specifically about a direct RH mechanism based on its ordinary spectrum/point spectrum.

## Audit / falsification criterion

The finding can be audited in four independent steps:

1. Verify directly that

   ```text
   integral_{1/2}^infinity (m n)^(-w) dw
   =1/(sqrt(m n) log(m n)).
   ```

2. Verify from the primary 2016 paper that this is the matrix of the zeta-kernel operator on `mathcal H^2_0` and a small Hankel operator under the Bohr lift.
3. Verify the spectral theorem `spec(H)=[0,pi]` with no eigenvalues, and the 2018 refinement to purely absolutely continuous spectrum of multiplicity one.
4. Check the domain inequality `Re(s+w)>1` and the decomposition of the boundary singularity into the Carleman pole `1/(s+w-1)` plus an analytic remainder.

A counterexample to the stored negative conclusion would need to show that the ordinary spectrum or point spectrum of this exact operator carries nontrivial zero locations despite the cited complete spectral theorem. A different operator or a new scattering invariant would be an escape from the finding, not a falsification of it.

## Consequence for the research line

The canonical spectral ladder now contains two complementary obstructions:

```text
diagonal prime operator
    -> natural Schatten threshold at 1/2
    -> standard regularized determinant is zero-free                 [PL-009]

canonical non-diagonal multiplicative Hankel operator
    -> natural zeta kernel / Bohr small-Hankel structure
    -> spectrum is purely a.c. [0,pi], with no eigenvalues           [PL-010]
    -> kernel probes only Re(z)>1 and boundary pole/Carleman behavior
```

Therefore a credible RH spectral mechanism in the prime-lattice picture must introduce structure that is not exhausted by the bare `log p` energy, standard Schatten renormalization, or the canonical positive multiplicative Hankel coupling. In particular, it must explain how analytically continued, zero-sensitive information enters without merely being inserted as external zeta data.