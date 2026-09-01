# PL-104 — Bruhat–Tits radial geometry singles out `Re(s)=1/2` only as universal local temperedness

## Claim

The cheapest Bruhat–Tits enrichment proposed by `CLUE-bruhat-tits-local-prime-geometry` has a precise classical answer.

Let `F` be a non-archimedean local field with residue-field cardinality `q`, and let `T_q` be the Bruhat–Tits tree of `PGL_2(F)`. As an unrooted graph, `T_q` is the homogeneous `(q+1)`-regular tree. If `A_q` is its adjacency operator and `phi_k` is radial about a base vertex, then

```text
lambda phi_0 = (q+1) phi_1,

lambda phi_k = phi_(k-1) + q phi_(k+1),    k >= 1.
```

The radial characteristic equation is

```text
q r^2 - lambda r + 1 = 0.
```

Writing one root as `r=q^(-s)` gives the Weyl-symmetric parametrization

```text
lambda(s) = q^s + q^(1-s).
```

Since the self-adjoint adjacency spectrum is

```text
sigma(A_q) = [-2 sqrt(q), 2 sqrt(q)],
```

its spherical/tempered spectral axis is exactly

```text
s = 1/2 + i t,
lambda(s) = 2 sqrt(q) cos(t log q).
```

Thus **Bruhat–Tits radial geometry really does single out a half-axis**, but it is the classical local tempered/unitary axis of spherical harmonic analysis, not a new localization principle for the zeros of the Riemann zeta function.

The decisive obstruction is that the whole intrinsic radial package is universal for a homogeneous tree. Sphere cardinalities,

```text
|S_0|=1,
|S_k|=(q+1)q^(k-1),   k>=1,
```

the radial recurrence, the root Green function,

```text
G_q(z)
 = <delta_o,(z-A_q)^(-1)delta_o>
 = 2q / ((q-1)z + (q+1)sqrt(z^2-4q)),
```

and the Kesten--McKay/Plancherel spectral measure depend only on the free branching parameter `q`. The same formulas hold on an abstract `(q+1)`-regular tree even when `q` is not a prime power and therefore cannot be the residue cardinality of any non-archimedean local field. For example, the `7`-regular tree supplies the identical package with `q=6`.

When the local-field action is restored, the spherical Hecke algebra and Satake transform are exactly the classical mechanism that turns this radial recurrence into the parameter `x+x^(-1)` with `x=q^(s-1/2)`. On the ordinary unramified Riemann-zeta channel, however, the spherical state is one-dimensional. As established in `PL-039`, the zeta-sensitive part of the standard intertwiner is therefore a scalar local L-factor normalization; after spherical normalization no extra matrix/operator datum remains. `PL-040` then blocks the immediate repair by a fixed globally nonspherical vector, since nonspherical finite-place data are exceptional at only finitely many primes.

Hence the proposed route

```text
replace every prime exponent axis by its Bruhat--Tits tree
    -> intrinsic local spectral half-axis
    -> new operator-valued Euler-factor rigidity
    -> localization of global zeta zeros
```

fails at the rank-one decisive test. The first arrow is canonical and the second is real, but the resulting half-axis is universal local temperedness. The zeta-sensitive Euler response remains the already-known scalar Satake/Tate/intertwining datum, while the global analytic continuation and functional equation still require additional global structure.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
intrinsic rank-one Bruhat--Tits radial/adjacency/Green/boundary geometry
    -> residual zeta-sensitive operator beyond spherical Satake data
    -> new RH zero-localization mechanism.
```

No novelty is claimed for Bruhat--Tits trees, spherical functions, the Satake transform, the adjacency spectrum, local temperedness, or Kesten--McKay harmonic analysis. The durable contribution is the line-specific falsification: the apparent `1/2` spectral miracle survives the generic-tree control and therefore cannot by itself discriminate the rational-prime norm map or constrain the globally continued Riemann divisor.

## Exact rank-one calculation

Fix a root `o` of the `(q+1)`-regular tree and let a radial function have value `phi_k` on the sphere of radius `k`.

For `k>=1`, every vertex on that sphere has one neighbor toward `o` and `q` neighbors away from `o`. Therefore

```text
(A_q phi)_k = phi_(k-1) + q phi_(k+1),
```

while at the root

```text
(A_q phi)_0 = (q+1)phi_1.
```

Away from the root, an exponential ansatz `phi_k=r^k` gives

```text
lambda r^k = r^(k-1) + q r^(k+1),
```

hence

```text
q r^2 - lambda r + 1=0.
```

The two roots have product `q^(-1)`. If one is written

```text
r=q^(-s),
```

the other is `q^(-(1-s))`, and

```text
lambda(s)
  = r^(-1)+q r
  = q^s + q^(1-s).
```

The involution exchanging the two radial solutions is therefore exactly

```text
s <-> 1-s.
```

On the line `s=1/2+it`,

```text
lambda(s)
 = sqrt(q)(q^(it)+q^(-it))
 = 2 sqrt(q) cos(t log q),
```

so the spectral parameter is real and lies in `[-2sqrt(q),2sqrt(q)]`.

Conversely, every interior point of that spectral interval can be written in this form. This is the elementary tree form of the classical Satake/tempered parametrization: after normalizing adjacency by `sqrt(q)`, the spherical transform is the Weyl-invariant coordinate

```text
x + x^(-1),
x=q^(s-1/2),
```

and the self-adjoint/tempered locus is `|x|=1`, equivalently `Re(s)=1/2`.

The point is important but negative for RH. The local self-adjoint operator does not have the nontrivial zeros of global `zeta(s)` as its eigenvalues. It has a continuous interval of adjacency spectrum, and the same `1/2` parametrization occurs for every homogeneous tree of the same degree.

## The radial Green function contains no additional arithmetic datum

The root resolvent can be computed by the standard cavity recursion.

Let `h_q(z)` be the diagonal resolvent seen from a forward branch. Removing the edge to the parent leaves `q` identical descendants, so

```text
h_q(z) = 1 / (z - q h_q(z)).
```

Choosing the branch with `h_q(z)~1/z` at infinity gives

```text
h_q(z)
 = (z-sqrt(z^2-4q))/(2q).
```

At the root there are `q+1` identical branches, hence

```text
G_q(z)
 = 1/(z-(q+1)h_q(z))
 = 2q / ((q-1)z+(q+1)sqrt(z^2-4q)).
```

The branch cut is exactly `[-2sqrt(q),2sqrt(q)]`. Taking boundary values recovers the Kesten--McKay spectral measure

```text
dmu_q(x)
 = (q+1)/(2 pi)
   * sqrt(4q-x^2)/((q+1)^2-x^2)
   * 1_(|x|<=2sqrt(q)) dx.
```

Every coefficient here is determined by `q` alone. Return-walk counts are the moments of the same measure and are likewise polynomials/combinatorial functions of the branching number. There is no hidden rational-prime discriminator in the radial resolvent.

This addresses directly the clue's proposed adjacency/Laplacian/Green/return-path test.

## Prime-power depth is geometrized, but its Euler response is classical scalar data

For `F=Q_p`, one has `q=p`, so the tree genuinely geometrizes repeated `p`-adic depth:

```text
distance k
    -> q^k descendants up to the root factor
    -> p^k when q=p.
```

Likewise a boundary cylinder at depth `k` has canonical harmonic/Haar scale proportional to `q^(-k)`. Therefore powers such as `q^(-ks)` can arise naturally after applying a Mellin/spherical spectral parameter to depth; one need not regard every occurrence of `p^(-ks)` as an arbitrary hand-inserted weight.

But this does not produce a new mechanism. The corresponding geometric series

```text
sum_(k>=0) q^(-ks)
 = 1/(1-q^(-s))
```

is exactly the standard unramified local Euler/Tate factor. In Tate's local integral, recorded globally in `PL-014`, the same factor arises from the valuation shells of `O_F` under the multiplicative norm. In spherical `PGL_2` harmonic analysis, the depth variable is encoded by the Satake parameter and the spherical Hecke character.

Thus the tree does provide a geometric realization of prime-power depth, but the zeta response it produces on the trivial unramified channel is **the known scalar local factor**, not an additional operator invariant.

## Generic-tree falsification

The canonical graph underlying the Bruhat--Tits building does not remember that its branching number came from a rational prime.

For every integer `q>=2` there exists a unique homogeneous `(q+1)`-regular tree up to graph isomorphism. Its radial adjacency, Green function, Plancherel measure, boundary cylinders, and spherical recurrences are given by the formulas above.

A non-archimedean local field, by contrast, has residue-field cardinality equal to a prime power. Therefore `q=6` supplies a particularly clean control:

```text
abstract 7-regular tree:
    q=6,
    same radial formulas,
    same s <-> 1-s symmetry,
    same Re(s)=1/2 tempered parametrization;

local-field origin:
    impossible, because no finite field has 6 elements.
```

So any proposed invariant using only the intrinsic homogeneous-tree radial geometry passes unchanged to a non-arithmetic control. It fails the `prime_lattice` mandate's requirement that a genuine mechanism discriminate the exact rational-prime norm map from generic multiplicative/regular-tree systems.

For `Q_p`, setting `q=p` of course recovers the numerical prime. What is absent is a mechanism forcing **primality or the global compatibility of the rational primes** from the local graph spectrum itself.

## What the full `PGL_2(Q_p)` action adds — and why it does not rescue the spherical zeta channel

The full Bruhat--Tits object is richer than an unlabeled regular graph. Its boundary is `P^1(Q_p)`, `PGL_2(Q_p)` acts on the tree and boundary, and nonradial/K-type/Iwahori structures can retain field-specific data.

This finding does not claim that all such structure is branching-universal.

The relevant projection for the ordinary unramified zeta channel is the spherical one. With

```text
K=PGL_2(Z_p),
```

the `K`-fixed line in an unramified principal series is one-dimensional. The spherical Hecke algebra is commutative and the Satake transform diagonalizes its action by scalar characters. `PL-039` already establishes the stronger intertwining statement: on the spherical line, the standard local intertwiner is

```text
scalar L-factor ratio
    x canonical Weyl transport,
```

and normalizing away the scalar removes the zeta-sensitive singularity.

Therefore field-specific angular/boundary information outside the radial line can matter only by leaving the ordinary spherical channel. For a standard fixed smooth adelic vector, `PL-040` shows that this happens at finitely many finite places. Such data do not create a new operator-valued coupling across the full infinite family of prime coordinates.

A future construction could still use a genuinely global family of boundary representations, an arithmetic quotient, or a target-relative object. It would then be a new global mechanism, not the intrinsic rank-one local-tree enrichment tested by this clue.

## Analytic-continuation boundary

All local formulas above are legitimate local spectral identities. As functions of the Satake parameter, local spherical quantities are rational/meromorphic and can be reparametrized by `q^(-s)`.

This does **not** imply that the Euler product

```text
product_p (1-p^(-s))^(-1)
```

continues term by term into the critical strip.

For Riemann zeta, the local product is initially valid only in `Re(s)>1`. The continuation and `s<->1-s` functional equation require a global theorem:

- Tate's additive Fourier/Poisson mechanism and the archimedean place, as in `PL-014`; or
- Eisenstein/intertwining meromorphic continuation, as in `PL-039`.

The local tree symmetry

```text
s <-> 1-s
```

is therefore not itself the analytic continuation bridge for `zeta(s)`. It is the local Weyl symmetry of the rank-one spherical recurrence. Once the global continuation is supplied by established automorphic machinery, the zeta-sensitive channel is again the scalar scattering factor already audited in `PL-039`.

This distinction prevents a false inference:

```text
local self-adjoint adjacency has tempered axis Re(s)=1/2
    !=>
global zeros of continued zeta lie on Re(s)=1/2.
```

## Adversarial checks

### The half-axis coincidence is real, not dismissed as notation

The parametrization `lambda=q^s+q^(1-s)` is not an arbitrary re-labeling chosen solely to manufacture `1/2`. It is forced by the two characteristic roots of the radial tree recurrence, whose product is `q^(-1)`, and it is exactly the classical Satake/Weyl normalization.

The negative conclusion is stronger: **even a genuinely canonical local half-axis is insufficient**, because it expresses local temperedness rather than global zero localization.

### The tree can generate local zeta factors

The finding does not claim that Bruhat--Tits geometry is incapable of producing expressions involving `zeta_p(s)`. Valuation depth, Poisson kernels, spherical functions, and p-adic boundary constructions routinely generate local zeta factors.

The claim is that, on the ordinary trivial spherical channel, these factors are classical scalar Satake/Tate data. Producing them again from tree paths or boundary measure does not leave a residual operator after the standard spherical normalization.

### Arithmetic quotients are a different mechanism

A quotient `Gamma\T_q` may have closed geodesics and an Ihara/Selberg-type trace formula; its spectrum can encode substantial arithmetic information. The infinite tree itself has no cycles, while the quotient introduces the global/discrete group `Gamma`.

Such a quotient is not evidence that the **local prime axis alone** contains the missing RH rigidity. It is precisely an added global arithmetic coupling and must be audited on its own terms.

### Nonradial boundary data are not ruled out absolutely

Boundary cross-ratios, Iwahori-fixed spaces, harmonic cochains, and other nonspherical objects can retain data absent from the radial graph. This finding does not assert their triviality.

It establishes the clue's specified first gate: no zeta-sensitive residual survives on the canonical rank-one spherical channel. Under the clue's own decision rule, there is therefore no basis to escalate to higher-rank buildings merely in the hope that more local matrix structure will constrain ordinary Riemann zeta.

### Higher rank is classical Satake territory, not a free escape

Higher-rank Bruhat--Tits buildings have genuinely richer apartments, Hecke algebras, and local representations. But their unramified spherical harmonic analysis is again governed by Satake, with scalar characters of the commutative spherical Hecke algebra and local L-factors attached to representation data.

A higher-rank proposal would need to specify a canonical nonspherical/global datum that acts back on the **ordinary degree-one Riemann zeta scalar** and proves a new positivity/localization theorem. Richer local geometry by itself does not supply that bridge.

## Prior art and novelty audit

The relevant structure is classical and explicit.

- **Jean-Pierre Serre**, *Trees*, Springer-Verlag, 1980, DOI `10.1007/978-3-642-61856-7`. Chapter II treats the tree of `SL_2` over a local field and the lattice/group-action geometry underlying the rank-one Bruhat--Tits model.
- **Pierre Cartier**, “Fonctions harmoniques sur un arbre,” *Symposia Mathematica* **9** (1972), 203–270. Classical harmonic analysis, Poisson boundary, and spherical/radial analysis on homogeneous trees.
- **Ichiro Satake**, “Theory of spherical functions on reductive algebraic groups over p-adic fields,” *Publications Mathématiques de l'IHÉS* **18** (1963), 5–69, DOI `10.1007/BF02684781`. Classical spherical Hecke/Satake transform and unramified harmonic-analysis framework.
- **Ian G. Macdonald**, *Spherical Functions on a Group of p-adic Type*, Ramanujan Institute Publications No. 2, University of Madras, 1971; updated annotated edition with Anne-Marie Aubert, Springer Lecture Notes in Mathematics **2392** (2026), DOI `10.1007/978-3-032-15671-6`. Explicit spherical functions and Plancherel theory.
- **Allan J. Silberger**, *PGL2 over the p-adics: Its Representations, Spherical Functions, and Fourier Analysis*, Lecture Notes in Mathematics **166**, Springer, 1970. Rank-one representation/spherical Fourier theory specific to `PGL_2`.
- `PL-039` and `PL-040` already contain the line's detailed audit of spherical intertwining scalarization and restricted-tensor nonspherical support.

Modern homogeneous-tree literature continues to use exactly the same universal `q`-dependent radial structure. For example, the adjacency operator of the `(q+1)`-regular tree has pure absolutely continuous spectrum `[-2sqrt(q),2sqrt(q)]`, and the spherical recurrence depends only on `q`; this is graph harmonic analysis rather than a rational-prime-specific phenomenon.

The literature audit therefore classicalizes both positive-looking ingredients:

```text
Bruhat--Tits tree gives a canonical 1/2 axis
    -> classical local temperedness/Satake;

Bruhat--Tits depth gives p^k / p^(-ks)
    -> classical valuation/Tate/Satake local factor.
```

No source found a residual rank-one spherical operator, after standard normalization, that couples the rational primes globally or forces the Riemann zero divisor onto the local tempered axis. That absence is consistent with the exact one-dimensional scalarization theorem already persisted in `PL-039`.

## Falsification / escape tests

This obstruction would be materially escaped only by an explicit construction that proves all of the following.

1. It uses field-specific Bruhat--Tits data not determined solely by the homogeneous branching parameter `q`.
2. It is nontrivial after projection/normalization of the standard spherical Satake/L-factor scalar.
3. It canonically couples **infinitely many** rational-prime places, rather than adding finitely supported K-type/ramified corrections excluded by `PL-040`.
4. Its global object has a mathematically justified continuation into the critical strip that is not a termwise Euler-product continuation.
5. It yields a positivity, self-adjointness, determinant, trace, resonance, or other falsifiable condition whose spectral consequence concerns the **global zeta zero divisor**, not merely local tempered Satake parameters.
6. The construction fails or changes materially for the generic `(q+1)`-regular-tree control and for suitable generalized-prime systems.

Without these steps, “each prime carries a Bruhat--Tits tree” is a geometrically rich restatement of classical local harmonic analysis, not a new RH mechanism.

## Consequence for `prime_lattice`

The proposed Bruhat--Tits clue has passed its cheap rank-one falsification test with a negative result.

The useful lesson is sharper than “the trees are classical”:

```text
local recursive prime geometry
    -> canonical Weyl symmetry s <-> 1-s
    -> canonical self-adjoint/tempered axis Re(s)=1/2
    -> BUT this survives arbitrary regular-tree branching
    -> and the ordinary zeta channel scalarizes under Satake/intertwining.
```

So a local geometric explanation of the number `1/2` is **not** the missing ingredient. `PL-014` already supplies a global adelic self-dual `1/2` axis, and this finding supplies an independent local-tree one; neither local/global symmetry alone localizes the Riemann divisor.

Future work should not escalate to higher-rank buildings merely because they have richer geometry. A surviving building-based proposal must first exhibit a field-specific, nonspherical or global invariant that remains nontrivial after spherical normalization and then prove how it constrains the ordinary Riemann-zeta scalar across infinitely many prime places.
