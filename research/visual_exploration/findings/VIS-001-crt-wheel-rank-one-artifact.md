# VIS-001 — CRT-aligned wheel masks are rank-one tensors

## Claim

Let `A,B > 1` be coprime and set `P = AB`. For each pair

```text
(a,b) in (Z/AZ) x (Z/BZ),
```

let `n(a,b)` be the unique residue modulo `P` given by the Chinese remainder theorem, and define the wheel-survivor mask

```text
M[b,a] = 1  if gcd(n(a,b), P) = 1,
         0  otherwise.
```

Then

```text
M[b,a]
  = 1[gcd(a,A)=1] * 1[gcd(b,B)=1].
```

Hence `M = v_B u_A^T` is an exact outer product and has real matrix rank exactly `1`. More generally, for any pairwise coprime factorization `P = A_1 ... A_k`, the CRT-coordinate unit mask is the rank-one tensor product of the one-dimensional unit indicators modulo the `A_i`.

**Evidence/status:** `CLASSICAL-IDENTITY + EXACT-DERIVED + NEGATIVE/OBSTRUCTION`.

The Chinese remainder theorem is classical and no novelty is claimed for the factorization. The research value here is as a falsification control for visual prime/sieve exploration: strong block, recursive, or self-similar-looking structure in a CRT-aligned wheel image can be imposed entirely by the coordinates.

## Derivation

The Chinese remainder theorem gives a ring isomorphism

```text
Z/(AB)Z  ~=  Z/AZ x Z/BZ
```

when `gcd(A,B)=1`. Under a ring product, an element is a unit exactly when each component is a unit. Therefore

```text
gcd(n(a,b),AB)=1
  <=> gcd(a,A)=1 and gcd(b,B)=1.
```

Writing

```text
u_A[a] = 1[gcd(a,A)=1],
v_B[b] = 1[gcd(b,B)=1]
```

gives `M[b,a] = v_B[b] u_A[a]`, so every row is either the zero row or the same vector `u_A`. Since the residue `1` is a unit modulo every positive modulus, both vectors are nonzero and `rank_R(M)=1`.

The same argument applied componentwise to a pairwise coprime factorization `P=A_1...A_k` gives

```text
1[gcd(n,P)=1] = product_i 1[gcd(a_i,A_i)=1],
```

which is exactly a separable rank-one tensor in CRT coordinates.

## Concrete primorial visualization

The retained visualization uses

```text
A = 210 = 2*3*5*7,
B = 143 = 11*13,
P = 30030 = 2*3*5*7*11*13.
```

It plots the `143 x 210` mask in CRT coordinates. The exact counts are

```text
phi(210) = 48,
phi(143) = 120,
phi(30030) = 5760 = 48*120.
```

Thus the image contains `5760` surviving cells, and the plotted matrix has exact rank `1`. The conspicuous repeated stripes and rectangular gaps are therefore not independent evidence of a fractal or global prime law; they are the visible outer-product decomposition.

Visualization: [[research/visual_exploration/visualizations/crt-primorial-rank-one-carpet.md]].

## Prior art and novelty assessment

The underlying mechanism is the standard Chinese remainder theorem. An authoritative algebra statement is Stacks Project, Lemma 10.15.4, which gives the ring-product isomorphism for pairwise comaximal ideals:

https://stacks.math.columbia.edu/tag/00DT

Passing from the product-ring isomorphism to its unit set and then to the indicator outer product is immediate. No novelty is claimed for this algebraic fact, for Euler's totient multiplicativity, or for wheel sieves.

The Mathia-specific contribution is the explicit use of the rank-one/tensor factorization as a visual-artifact baseline: a picture may look richly recursive while carrying no coupling at all between the CRT factors.

## Boundary conditions and failure modes

This result concerns the finite wheel-survivor mask `gcd(n,P)=1`, not the indicator of actual primes. For primes larger than the factors of `P`, coprimality with `P` is only a necessary local condition, so genuine residual structure may still exist inside the surviving cells.

Independent permutations of rows or columns preserve matrix rank while changing the visual texture. A different non-CRT embedding can hide the product appearance, and an arbitrary coordinate map mixing the two axes need not preserve rank-one matrix form. Thus the exact invariant is the separability induced by the CRT product coordinates, not any particular arrangement of black and white pixels.

The factorization also explains why adding more coprime CRT coordinates can produce increasingly elaborate recursive-looking pictures without adding cross-coordinate dependence. Such visual complexity must not be promoted as arithmetic structure unless a statistic survives conditioning on this product baseline.

## Audit criterion

For any proposed two-factor CRT wheel visualization, reconstruct its binary mask and verify either of the equivalent exact checks:

```text
M[b,a] = v_B[b] u_A[a]
```

or that every `2 x 2` minor vanishes. The survivor count must also satisfy

```text
sum(M) = phi(A) phi(B) = phi(AB).
```

For the retained `210 x 143` case, direct exact computation gives `sum(M)=5760` and matrix rank `1`.

## Consequence for the research line

CRT-aligned wheel pictures are useful as a deliberately strong null model for visual prime research. Future claims of multiscale, fractal-like, clustered, or anisotropic prime structure should first subtract, condition on, or otherwise beat this exact separable baseline. A residual signal that disappears after this control was wheel geometry, not new information about the primes.
