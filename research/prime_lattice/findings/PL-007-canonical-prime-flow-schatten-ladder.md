# PL-007 — The canonical prime-flow generator has a zeta Schatten ladder but no critical-strip trace

## Claim

On the Hardy–Hilbert space of square-summable Dirichlet series

```text
H^2_D = { f(s)=sum_{n>=1} a_n n^{-s} : sum_n |a_n|^2 < infinity },
```

the vertical translation/Kronecker flow has a canonical nonnegative self-adjoint generator

```text
A e_n = (log n) e_n,       e_n(s)=n^{-s}.
```

Thus

```text
U_t f(s) = f(s+i t) = exp(-i t A) f(s)
P_sigma f(s) = f(s+sigma) = exp(-sigma A) f(s).
```

Under the Bohr lift, `A` is the weighted prime occupation operator

```text
A = sum_p (log p) N_p,
```

on monomials `z^{v(n)}`. For every `q>0` and `sigma>0`, the horizontal translation satisfies the exact Schatten criterion

```text
P_sigma in S_q  <=>  q sigma > 1,
||P_sigma||_{S_q}^q = sum_n n^{-q sigma} = zeta(q sigma).
```

In particular, `Re(s)=1/2` is the Hilbert–Schmidt boundary, while `Re(s)=1` is the trace-class boundary. For complex `s=sigma+i t`, an ordinary operator trace exists only for `sigma>1`, and there

```text
Tr(exp(-s A)) = zeta(s).
```

Therefore the most canonical operator supplied by the prime-exponent lattice does produce zeta as a genuine heat/partition trace, but **only in the Euler-product half-plane**. Its ordinary trace cannot encode nontrivial zeta zeros in the critical strip. Reaching those zeros would require an additional regularized trace, enlarged operator, or other analytic structure not present in this canonical semigroup.

**Evidence/status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION`.

The diagonal calculation is exact. The ingredients — the Hardy space, translation/composition operators, Schatten ideals, and the `log n` Hamiltonian/partition-function interpretation — are classical; no novelty is claimed for them separately.

## Exact derivation

The Dirichlet monomials

```text
e_n(s)=n^{-s}
```

form an orthonormal basis of `H^2_D`. Vertical translation gives

```text
e_n(s+i t)=n^{-s} n^{-i t}=exp(-i t log n)e_n(s),
```

so the strongly continuous unitary group is diagonal with generator

```text
A e_n=(log n)e_n.
```

Its natural self-adjoint domain is

```text
D(A)={sum_n a_n e_n : sum_n (log n)^2 |a_n|^2 < infinity}.
```

Horizontal translation is the positive contraction

```text
P_sigma=exp(-sigma A),
P_sigma e_n=n^{-sigma}e_n.
```

Hence its singular values are exactly

```text
s_n(P_sigma)=n^{-sigma}.
```

For any Schatten exponent `q>0`,

```text
sum_n s_n(P_sigma)^q
    = sum_n n^{-q sigma}
    = zeta(q sigma),
```

which is finite exactly when `q sigma>1`.

For `s=sigma+i t`,

```text
exp(-sA)e_n=n^{-s}e_n,
```

and the singular values remain `n^{-sigma}`. Absolute trace convergence therefore requires `sigma>1`; in that domain

```text
Tr(exp(-sA))=sum_n n^{-s}=zeta(s).
```

At `sigma=1`, the operator is not trace class because `sum_n 1/n` diverges. At `sigma=1/2`, it is not Hilbert–Schmidt because `sum_n 1/n` again diverges in the squared singular-value sum.

## Prime-coordinate interpretation

Under the Bohr correspondence,

```text
n <-> v(n)=(v_p(n))_p
     <-> z^{v(n)}.
```

Define the prime number operators by

```text
N_p z^alpha = alpha_p z^alpha.
```

Then on every finite-support monomial,

```text
sum_p (log p) N_p z^{v(n)}
    = (sum_p v_p(n) log p) z^{v(n)}
    = (log n) z^{v(n)}.
```

Thus `A=sum_p(log p)N_p` is exactly the spectral realization of the linear functional

```text
log n = <v(n),(log p)_p>.
```

The vertical torus rotation

```text
z_p -> e^{-i t log p} z_p
```

is its Koopman/unitary flow. This is not merely an analogy: the exponent lattice diagonalizes the generator.

## Relation to PL-001 and PL-004

`PL-001` found that bounded point evaluation on the Bohr curve has

```text
||ev_{sigma+i t}||^2 = zeta(2 sigma)
```

and breaks at `sigma=1/2`. The present operator gives the exact parallel identity

```text
||P_sigma||_{S_2}^2 = zeta(2 sigma).
```

So the Bohr-Hardy evaluation boundary and the Hilbert–Schmidt boundary of the canonical translation semigroup are the same threshold.

`PL-004` records Julia's classical primon-gas Hamiltonian: prime modes have energies `log p`, total energy is `log n`, and the partition function is `zeta(beta)`. The operator `A` is precisely that Hamiltonian on the Dirichlet/Bohr Hilbert basis. The new value of this finding is not a new Hamiltonian, but the explicit operator-ideal ladder and the resulting obstruction on ordinary traces in the critical strip.

## Prior art and novelty assessment

- Hedenmalm–Lindqvist–Seip provide the Hardy–Hilbert/Bohr setting and orthonormal Dirichlet basis.
- Julia's Riemann/primon gas already identifies `log p`, `log n`, and zeta as the thermal partition function.
- Translation and composition operators on Hardy spaces of Dirichlet series, including their compactness and Schatten-class behavior, form an established operator-theoretic literature; Bayart–Kouroupis (2024) is a close modern Schatten anchor.

Accordingly, no novelty claim is made for the semigroup or the diagonal trace computation. The Mathia-specific contribution is the audited conclusion that the **canonical** spectral object suggested directly by the exponent lattice simultaneously explains the `1/2` Hilbert–Schmidt boundary and the `1` trace boundary, while showing why its unregularized trace does not reach the Riemann zeros.

## Boundary conditions and failure modes

- The negative conclusion applies only to the ordinary trace of this canonical diagonal semigroup. It does not rule out a mathematically justified regularized trace, determinant, scattering construction, quotient, or extension.
- Analytic continuation of the scalar function `zeta(s)` is not the same thing as continuation of `exp(-sA)` as a trace-class operator.
- Writing a formal `Tr(exp(-sA))=zeta(s)` inside `Re(s)<=1` without specifying a valid regularization is therefore invalid.
- The presence of the `1/2` Hilbert–Schmidt threshold does not localize zeros; it is an operator-ideal boundary.
- Arbitrary regularization would merely re-encode analytic continuation. A useful escape must be canonical and add independently testable structure.

## Audit / falsification criterion

The exact operator statement can be audited on the basis vectors. Any contradiction requires either

```text
sum_n n^{-q sigma}<infinity with q sigma<=1,
```

or a failure of the diagonal singular-value computation, neither of which occurs.

A proposed escape from the obstruction must explicitly define a trace-like object for `Re(s)<=1`, prove its existence and invariance/canonicity from additional structure, and show that it contains more information than simply declaring the analytically continued scalar `zeta(s)` to be a "regularized trace".

## Consequence for the research line

The exponent lattice does supply a natural self-adjoint generator and exact spectral scale. But its most direct heat-trace realization stops at `Re(s)=1`, before the critical strip, while the same semigroup becomes non-Hilbert–Schmidt exactly at `Re(s)=1/2`. This sharply separates a genuine spectral boundary from a zero mechanism: any RH-relevant operator construction must add nontrivial structure beyond the canonical prime occupation Hamiltonian.
