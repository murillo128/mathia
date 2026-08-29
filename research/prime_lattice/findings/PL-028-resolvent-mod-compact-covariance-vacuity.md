# PL-028 — Prime-shift covariance modulo compact resolvents is vacuous for compact-resolvent Hilbert–Pólya operators

## Claim

A natural weakening of the additive covariance obstructions in `PL-025`–`PL-027` is to move the compact error from the unbounded Hamiltonian itself to its resolvent. For a compact-resolvent Hilbert–Pólya operator, that weakening goes too far: compact-resolvent covariance is automatic and therefore cannot carry prime-lattice information.

Let `H` be self-adjoint with compact resolvent on a Hilbert space. For any nonreal `z`, any real `a`, and any unitary `U`,

```text
U^* (H-z)^(-1) U - (H+a-z)^(-1)
```

is compact. Hence a proposed relation such as

```text
U_p^* (H-z)^(-1) U_p
  = (H+log p-z)^(-1) + C_p(z),
C_p(z) compact,
```

places **no restriction at all** on `H` or on the unitary `U_p`: both resolvents are compact separately, so their difference is compact. In the Calkin algebra every compact resolvent is simply zero.

For a hypothetical Riemann-zero Hamiltonian, the statement can be sharpened. The Riemann–von Mangoldt counting law implies

```text
(H-z)^(-1) in S_q  <=>  q>1,
```

up to the usual choice of positive ordinates versus a symmetric `+-gamma` spectrum. Therefore, for every `q>1`, every unitary `U`, and every real `a`,

```text
U^*(H-z)^(-1)U - (H+a-z)^(-1) in S_q
```

is again automatic. In particular, Hilbert–Schmidt-mod-resolvent covariance is also vacuous. `S_1` is the first ordinary Schatten level not forced merely by the zero density.

The scalar translation itself is even smaller: because the zero resolvent is Hilbert–Schmidt,

```text
(H+a-z)^(-1) - (H-z)^(-1)
 = -a (H+a-z)^(-1)(H-z)^(-1)
```

is trace class. Thus even at the resolvent level the `+log p` scalar shift contributes no nontrivial prime signature by itself; any `S_1`-level content would have to come from the specified unitary prime action or from additional observable/algebraic structure.

**Evidence/status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
compact-resolvent zero Hamiltonian
    + unitary prime actions
    + covariance only modulo compact (or S_q, q>1) resolvents
    -> RH-sensitive prime-lattice mechanism.
```

The compactness and Schatten conclusions are exact elementary consequences of compact resolvent and the unconditional Riemann–von Mangoldt counting law. Resolvent-level unitary equivalence modulo compacts is established operator-theory prior art; no novelty is claimed for that equivalence relation.

## Compact-resolvent covariance forgets the prime lattice completely

Fix `z` outside the real axis and write

```text
R_H(z) = (H-z)^(-1).
```

By definition of compact resolvent,

```text
R_H(z) in K.
```

A scalar translate `H+a` also has compact resolvent, and unitary conjugation preserves compactness. Hence

```text
U^* R_H(z) U in K,
R_(H+a)(z) in K,
```

so

```text
boxed:
U^* R_H(z) U - R_(H+a)(z) in K
```

for **every** unitary `U` and **every** real `a`.

No commutation law, representation of the exponent lattice, arithmetic input, or relation between `U` and `a` was used. Replacing `a` by `log p` therefore adds no information. The same statement would hold with `sqrt(2)`, `pi`, or any arbitrary real number in place of `log p`.

Equivalently, if `pi_Calkin:B(H)->B(H)/K` is the quotient map, then

```text
pi_Calkin(R_H(z)) = 0,
```

and consequently

```text
pi_Calkin(U^*R_H(z)U)
 = pi_Calkin(R_(H+a)(z))
 = 0.
```

Thus the quotient in which the proposed covariance is supposed to live has already annihilated the whole resolvent. It cannot distinguish the ordinary rational-prime energy increments from any other increments.

This is a stronger objection than merely saying that the relation is weak: under compact resolvent it is a tautology.

## Schatten refinement at Riemann-zero density

Suppose now that the eigenvalues of `H`, counted with multiplicity, have the Riemann-zero ordinate counting law. For a positive-ordinate model,

```text
N_H(T)
 = T/(2 pi) log(T/(2 pi))
   - T/(2 pi)
   + O(log T).
```

A symmetric `+-gamma` model changes only the leading constant. In either case,

```text
N_H(T) asymp T log T.
```

For fixed nonreal `z`, the singular values of the resolvent are

```text
s_j(R_H(z)) = |lambda_j-z|^(-1).
```

For large `|lambda_j|`, this is comparable to `|lambda_j|^(-1)`. Hence, using Stieltjes integration or summation by parts,

```text
sum_j s_j(R_H(z))^q
  converges
<=> integral_1^infinity t^(-q) dN_H(t) converges
<=> integral_1^infinity (log t) t^(-q) dt converges
<=> q>1.
```

Therefore

```text
boxed:
R_H(z) in S_q  iff  q>1.
```

The statement depends only on the known zero-counting asymptotic, not on RH: Riemann–von Mangoldt counts all nontrivial zeros irrespective of their real parts.

For every `q>1`, Schatten ideals are unitarily invariant and linear, so for arbitrary `U` and `a`,

```text
U^*R_H(z)U - R_(H+a)(z) in S_q.
```

Thus replacing “compact” by “Hilbert–Schmidt” or by any `S_q` with `q>1` still does not impose a prime-lattice constraint on a zero-density Hamiltonian. Such a condition follows before one has specified what the alleged prime shifts actually do.

The borderline `q=1` is different. The resolvent itself is not trace class for `N_H(T)~T log T`, so an arbitrary difference of two unitary-conjugate/translated resolvents need not be trace class. A trace-class **difference** can therefore remain nontrivial, but it must be proved from actual structure rather than inferred from compact resolvent.

## The scalar log-prime translation is trace-class at resolvent level

There is a useful further separation. The resolvent identity gives

```text
R_(H+a)(z)-R_H(z)
  = -a R_(H+a)(z) R_H(z).
```

For the zero-density spectrum both resolvents lie in `S_2`, and the product of two Hilbert–Schmidt operators lies in `S_1`. Hence

```text
boxed:
R_(H+a)(z)-R_H(z) in S_1.
```

In particular this holds for `a=log p`.

So a proposal of the form

```text
prime energy increment log p
    -> trace-class resolvent change
```

is still not enough: scalar translation alone already has that regularity. To get arithmetic information at the `S_1` level one would need, for example, a theorem controlling

```text
U_p^*R_H(z)U_p - R_H(z)
```

for a **specified** prime representation, a nontrivial trace/determinant extracted from it, or an algebraic relation that is not automatic from the Schatten class of the resolvent.

## Why this does not replace PL-026 or PL-027

`PL-026` and `PL-027` concern the much stronger unbounded-operator relation

```text
U^* H U = H + aI + K.
```

There the correction `K` is attached directly to `H`. Trace-class `K` forces at-most-linear counting even for two-sided compact-resolvent `H` (`PL-026`), and arbitrary compact `K` does so when `H` is semibounded (`PL-027`).

The present finding does **not** extend those conclusions to the remaining indefinite/two-sided additive compact case. Instead it rules out a tempting way of avoiding that hard case:

```text
additive compact covariance of H is restrictive
        |
        | weaken by applying the resolvent
        v
compact covariance of R_H
        |
        v
automatic / no information.
```

Thus moving the compact error to the resolvent is not a successful interpolation between exact covariance and a genuinely global zero-sensitive correction. It erases too much.

## Prior art and novelty audit

Resolvent-level unitary equivalence modulo compact operators is a known distinct relation for unbounded self-adjoint operators. A direct anchor is:

- Hiroshi Ando and Yasumichi Matsuzawa, “The Weyl–von Neumann theorem and Borel complexity of unitary equivalence modulo compacts of self-adjoint operators,” *Proceedings of the Royal Society of Edinburgh, Section A: Mathematics* **145**(6) (2015), 1115–1144. DOI `10.1017/S0308210515000293`; arXiv `1402.6947`.

Their paper explicitly distinguishes additive unitary equivalence modulo compact perturbations from the apparently related unbounded relation

```text
A ~ B
iff exists unitary u such that
u(A-i)^(-1)u^* - (B-i)^(-1) is compact.
```

The present observation is the compact-resolvent specialization relevant to `prime_lattice`: once both resolvents are compact, that relation is automatically true for every pair related by arbitrary unitary conjugation and scalar translation. The specialization is elementary and is not claimed as a new operator-theory theorem.

The `S_q` threshold uses only the classical Riemann–von Mangoldt formula. No claim of novelty is made for the standard equivalence between eigenvalue-counting growth and resolvent Schatten summability.

## Boundary conditions and escape routes

### Trace-class resolvent covariance is not automatically vacuous

For a Riemann-zero spectrum, `R_H(z)` is not in `S_1`. Therefore an arbitrary unitary difference

```text
U^*R_H(z)U-R_(H+a)(z)
```

need not be trace class. A genuine `S_1` identity tied to a canonical prime action could carry information. The finding only says that its scalar-translation portion is already `S_1` and that the full relation must be justified rather than inherited from compactness.

### Additive compact covariance of the Hamiltonian remains a different problem

The two-sided/indefinite case of

```text
U^*HU=H+aI+K,
K compact but not S_1,
```

was left open by `PL-026`–`PL-027` and remains open here. Compactness after applying the resolvent is strictly weaker.

### Noncompact reference dynamics can remain informative

Scattering theory, relative resolvents against a noncompact reference operator, spectral-shift functions, resonances, and Connes-type absorption spectra are not covered. There the quotient or difference need not annihilate both sides separately, so compact/trace-class relative data may be genuinely meaningful.

### Other bounded transforms are not automatically covered

The argument uses the resolvent of a compact-resolvent operator. A bounded transform or commutator that retains a nonzero image in the Calkin algebra may still encode structure. One must inspect the exact transform rather than extrapolate this no-go to every bounded functional calculus.

## Audit / falsification tests

This finding would be falsified or materially narrowed by any of the following:

1. a self-adjoint compact-resolvent `H` for which `(H-z)^(-1)` is not compact at some nonreal `z`;
2. a unitary conjugate of a compact operator that is not compact, or a difference of compact operators that is not compact;
3. a Riemann-zero counting law for which `sum |lambda_j-z|^(-q)` has a Schatten threshold different from `q=1`;
4. failure of the resolvent identity used to prove the scalar-shift `S_1` statement;
5. a proposed prime-lattice model whose nontrivial condition lives at the unbounded-operator level, at the trace-class resolvent-difference level for a specified prime representation, or relative to a noncompact reference, in which case it lies outside this negative rather than contradicting it.

The first four tests are excluded by standard exact facts. The fifth marks the actual surviving design boundary.

## Consequence for the research line

The reversible-covariance branch now has a useful regularity ladder:

```text
exact unitary covariance on H
    -> full real spectrum                                  [PL-025]

additive S_1 cocycle on H
    -> N_H(T)=O(T), even two-sided                         [PL-026]

additive compact cocycle on semibounded H
    -> N_H(E)=O(E)                                         [PL-027]

compact / S_q (q>1) covariance only after resolvent
    -> automatic for a compact-resolvent zero Hamiltonian [PL-028]
```

So a viable prime-lattice spectral route cannot escape the `PL-025`–`PL-027` constraints merely by declaring covariance modulo compact resolvents. The quotient has already erased the spectrum it was meant to organize. Any surviving mechanism must retain a stricter nonautomatic coupling — for example an additive unbounded relation, a canonical trace-class relative invariant, a nonunitary/compressed action, or a genuinely global scattering/adelic/Weil construction.