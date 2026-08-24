# PF-015 — local cusp transfer operators have a universal `1/2` threshold

**Status:** NEGATIVE/OBSTRUCTION.

## Claim

The appearance of `Re(s)=1/2` in a cusp-accelerated transfer operator is a universal rank-one parabolic phenomenon and therefore cannot, by itself, be interpreted as prime-specific evidence for the Riemann critical line.

For adjacent side-pairing generators of the zero-twist prime-flute, the word

```text
P_n = G_n G_{n+1}^{-1}
```

is parabolic (the adjacent cusp word; in the explicit normalization its trace is `-2`). Any nontrivial parabolic element of `PSL(2,R)` is conjugate to a translation

```text
T_w : z -> z + w,
```

for some cusp width `w>0` in the chosen cusp coordinate.

The standard acceleration of a parabolic branch sums its powers:

```text
N_s = sum_{k>=1} alpha_s(T_w^k).
```

For the scalar principal-series weight, the corresponding holomorphic kernel contains the standard series

```text
sum_{k>=1} (k w + z)^(-2s)
  = w^(-2s) zeta(2s, 1 + z/w),
```

or, with a unitary twist, the analogous Lerch-zeta series.

Hence the raw parabolic block has the universal convergence condition

```text
Re(s) > 1/2.
```

Its meromorphic continuation is governed by Hurwitz/Lerch zeta functions. In the standard transfer-operator theory for cusped geometrically finite surfaces, the possible cusp-generated pole lattice lies at half-integer shifts (with representation-dependent cancellations/order).

## Consequence for the prime-flute investigation

The following chain is therefore invalid as a prime-specific mechanism:

```text
prime-flute cusp
  -> accelerated transfer branch
  -> boundary Re(s)=1/2
  -> Riemann critical line.
```

The `1/2` is already forced by the derivative decay of powers of any rank-one parabolic branch (`k^{-2s}`), independently of prime gaps, cuff fluctuations, or the exact values `cot(pi/p)`.

The interior/exterior reflection can exchange the two orientations of the same cusp word (schematically `P_n <-> P_n^{-1}`), but the resulting positive/negative parabolic sums are still the same universal cusp mechanism. This symmetry therefore does not make the local `1/2` threshold arithmetically special.

Prime-specific information, if any survives in a transfer-operator description, must enter through **nonlocal coupling between distinct cusp channels or non-adjacent hyperbolic words**, not through the accelerated block attached to an individual cusp.

## Relation to earlier findings

This strengthens PF-006. PF-006 says that primitive hyperbolic lengths accumulating at zero obstruct the ordinary Selberg/Ruelle Euler product and any faithful eventually uniformly expanding Bowen-Series coding. PF-015 says that even before confronting that global obstruction, the most tempting local transfer-operator signature — the `1/2` convergence threshold of an accelerated cusp branch — is completely universal.

It does **not** prove that no transfer-operator formalism can ever be constructed for the infinitely generated prime-flute. Existing meromorphic/Fredholm results require hypotheses such as geometric finiteness, finitely many cusps, and a strict uniformly expanding transfer-operator approach that the prime-flute does not satisfy. No global determinant or meromorphic continuation for the prime-flute is asserted here.

## Literature anchors

- K. Fedosova and A. Pohl, *Meromorphic continuation of Selberg zeta functions with twists having non-expanding cusp monodromy*, Selecta Mathematica 26, 9 (2020), DOI `10.1007/s00029-019-0534-3`. Their continuation of cusp transfer blocks explicitly uses Hurwitz/Lerch transcendents; the strict-transfer framework also relies on a suitable uniformly expanding IFS and finitely many cusps.
- A. Adam and A. Pohl, *A transfer-operator-based relation between Laplace eigenfunctions and zeros of Selberg zeta functions*, Ergodic Theory and Dynamical Systems (2018), arXiv:`1606.09109`. For a parabolic element `h`, the fast/accelerated block is initially defined as `N_s = sum_{k>=1} alpha_s(h^k)` for `Re(s)>1/2` and is continued using Lerch zeta functions.
- The classical modular/Hecke transfer operator already has the prototype

```text
L_s f(x) = sum_{n>=1} (x+n)^(-2s) f(1/(x+n)),
```

with the same initial `Re(s)>1/2` threshold.

## Novelty assessment

The transfer-operator facts themselves are standard. The useful result here is a **negative application to the prime-flute research program**: it rules out interpreting the local cusp `1/2` threshold, its Hurwitz/Lerch factor, or the associated half-integer cusp poles as evidence specific to the primes or to RH.
