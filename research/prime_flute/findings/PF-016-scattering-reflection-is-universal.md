# PF-016 — scattering reflection is universal, not a prime-specific explanation of `s <-> 1-s`

**Status:** NEGATIVE/OBSTRUCTION; literature-backed.

## Claim

For any finite-area hyperbolic surface with finitely many cusps, the Eisenstein/scattering system already has the functional equation

```text
E(z,s) = Phi(s) E(z,1-s),
Phi(s) Phi(1-s) = I,
```

and therefore its scattering determinant satisfies

```text
phi(s) phi(1-s) = 1.
```

On the critical line `Re(s)=1/2`, the scattering matrix is unitary.

These identities are standard consequences of hyperbolic cusp scattering and do not depend on prime vertices, prime gaps, the exact `cot(pi/p)` embedding, or the interior/exterior reflection of the prime-circle construction.

## Consequence for the prime-flute program

The visually attractive chain

```text
interior/exterior sides of prime circles
        -> reflection
        -> s <-> 1-s
        -> Riemann functional equation
```

is not spectrally discriminating.

Even if the two sides of the exact orthogonal-circle geometry provide a natural geometric realization of a reflection, a scattering functional equation with exactly the same spectral involution exists for every finite-area cusped hyperbolic surface.

Thus the mere appearance of

```text
s <-> 1-s,
Re(s)=1/2,
unitarity on the critical line,
```

cannot be evidence that the prime-flute explains the Riemann functional equation or its zero set.

Combined with PF-015, even the *count* of many real residual poles in `(1/2,1)` for genus-zero many-cusp right limits is largely topological. The only potentially discriminating scattering information left at this level is the **divisor and channel structure**:

```text
exact pole/zero locations,
multiplicities,
scattering eigenvalues/eigenphases,
residues and channel couplings,
variation with the prime-derived moduli/cross-ratios.
```

This suggests a clean future control experiment: for a fixed cusp count, compare the scattering data of a prime-derived finite right limit `S_H` against non-prime punctured spheres with the same topology and matched coarse geometry. Any candidate prime signal must survive that control.

## Literature anchors

- Standard cusp-scattering theory: the scattering matrix `Phi(s)` is meromorphic and satisfies `Phi(s) Phi(1-s)=I`; on `Re(s)=1/2` it is unitary.
- M. Avdispahic and L. Smajlovic, *Explicit Formula for the Hyperbolic Scattering Determinant* (2005), records `phi(s)phi(1-s)=1` for finite-volume hyperbolic surfaces.
- Michael Levitin and Alexander Strohmaier, *Computations of eigenvalues and resonances on perturbed hyperbolic surfaces with cusps* (IMRN), demonstrates that scattering matrices/resonances can vary under conformal and Teichmüller deformation, so pole positions remain a genuinely moduli-sensitive quantity rather than a purely topological one.

## Novelty status

The scattering functional equation is classical. The project-specific result is a **decisive negative control**: the interior/exterior duality cannot, by itself, explain the special Riemann reflection symmetry, because hyperbolic cusp scattering supplies that symmetry universally.