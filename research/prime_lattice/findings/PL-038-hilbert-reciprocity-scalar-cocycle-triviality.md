# PL-038 — Hilbert reciprocity trivializes the canonical scalar local-global prime cocycle

## Claim

The most arithmetic scalar escape left open by `PL-036` and by the accepted trace-class prime-resolvent clue also collapses: replacing freely chosen projective prime phases by the **canonical quadratic Hilbert symbols of the rational primes** does introduce genuine local arithmetic, but their globally normalized scalar product is identically trivial by Hilbert reciprocity.

For a finite-support exponent vector

```text
alpha in N_0^(P),
n(alpha)=product_p p^(alpha_p) in Q_{>0},
```

and for every place `v` of `Q`, define

```text
omega_v(alpha,beta)
    = ( n(alpha), n(beta) )_v in {+1,-1},
```

where `(.,.)_v` is the quadratic Hilbert symbol on `Q_v^x`. The Hilbert symbol is bimultiplicative, so each `omega_v` is a scalar bilinear `2`-cocycle on the exponent semigroup. Unlike the arbitrary phases of `PL-036`, these local phases are canonically fixed by rational arithmetic and encode quadratic-residue information.

Nevertheless Hilbert's product formula gives, for all `a,b in Q^x`,

```text
product_v (a,b)_v = 1.
```

Since `n(alpha),n(beta)>0`, the real Hilbert symbol is also `1`. Hence on the positive prime-exponent lattice

```text
boxed:
product_(r finite prime) omega_r(alpha,beta) = 1
```

for every `alpha,beta`.

Thus the most direct scalar implementation of the surviving idea

```text
canonical local arithmetic phases
    + adelic / reciprocity / product-formula normalization
    -> nontrivial globally forced prime curvature
```

fails exactly: the local arithmetic defects cancel in the global scalar invariant. The construction is also independent of any spectral parameter `s`; it supplies no analytic continuation and no mechanism that can localize the Riemann zero divisor.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the route

```text
quadratic Hilbert-symbol phases on exponent vectors
+ scalar global product over places
    -> nontrivial RH-sensitive joint prime invariant.
```

The Hilbert symbol, its bimultiplicativity, the Hilbert product formula, and its relation to quadratic reciprocity are classical. The derived content here is only the consequence for the narrowed `prime_lattice` search: even a scalar joint structure that is genuinely arithmetic, canonical, local-global, and absent from generic Beurling prime systems can still become identically trivial after the very product-formula normalization that makes it global.

## Exact cocycle pullback to the exponent lattice

Let

```text
E = N_0^(P)
```

with addition, and let

```text
n : E -> Q_{>0}^x,
n(alpha+beta)=n(alpha)n(beta).
```

For a fixed place `v`, bimultiplicativity of the Hilbert symbol gives

```text
omega_v(alpha+beta,gamma)
 = omega_v(alpha,gamma) omega_v(beta,gamma),

omega_v(alpha,beta+gamma)
 = omega_v(alpha,beta) omega_v(alpha,gamma).
```

Therefore

```text
omega_v(alpha,beta) omega_v(alpha+beta,gamma)
 = omega_v(beta,gamma) omega_v(alpha,beta+gamma),
```

which is the normalized scalar `2`-cocycle identity.

For the quadratic symbol one also has

```text
(a,b)_v=(b,a)_v,
```

because the values are `+/-1` and the general norm-residue relation is `(b,a)_v=(a,b)_v^(-1)`. Consequently this particular arithmetic cocycle has **trivial projective commutator phase** already locally:

```text
omega_v(alpha,beta) / omega_v(beta,alpha) = 1.
```

This is an important distinction from `PL-036`. The Hilbert symbol carries nontrivial local residue information, but it does not evade the earlier projective-curvature obstruction merely by being canonical arithmetic data.

## Global product-formula cancellation

Hilbert reciprocity states that for rational `a,b`, all but finitely many local symbols equal `1` and

```text
product_v (a,b)_v = 1,
```

where `v` ranges over every finite prime and the real place.

For positive `a,b`, the real Hilbert symbol satisfies

```text
(a,b)_infinity=1,
```

because over `R` the quadratic Hilbert symbol is nontrivial only when both arguments are negative. Taking

```text
a=n(alpha),
b=n(beta)
```

therefore yields the exact finite-place identity

```text
product_r (n(alpha),n(beta))_r = 1.
```

So if a proposed global scalar curvature is obtained by multiplying the canonically normalized local prime phases, the result is not merely constrained: it is the constant function `1` on every pair of exponent vectors.

There is no limiting process, regularization, or use of an Euler product in this statement. It is an exact algebraic local-global identity.

## The prime-square calculation is quadratic reciprocity

The cancellation is visible already on two basis directions. Let `p != q` be odd rational primes and set

```text
alpha=e_p,
beta=e_q.
```

Then

```text
omega_p(e_p,e_q)=(p,q)_p=(q/p),
omega_q(e_p,e_q)=(p,q)_q=(p/q),
```

where the right-hand sides are Legendre symbols. At every odd finite place `r` different from `p,q` the local factor is `1`; the remaining finite correction is the `2`-adic Hilbert symbol. Since the real factor is `1`, Hilbert reciprocity becomes exactly the quadratic reciprocity relation, including its sign correction at `2`:

```text
(q/p)(p/q)(p,q)_2 = 1.
```

Thus the canonical arithmetic interaction between the prime directions is real and nontrivial **locally**, but the corresponding global scalar phase has been designed by reciprocity to cancel.

This gives a useful adversarial control for future prime-square constructions: observing Legendre/Hilbert-symbol structure between `e_p` and `e_q` is not yet a global spectral obstruction. The natural global scalar product of those local signs is identically flat.

## Why this is stronger than the Beurling control but still insufficient

`PL-015` and `PL-036` supplied a severe test: a candidate should fail when the rational-prime frequency list is replaced by a matched Beurling system. Arbitrary semigroup cocycles fail that test because the same phases can simply be assigned to generalized-prime generators.

Hilbert symbols pass that **particular** discrimination test. They require the local fields `Q_p`, square classes, norm-residue maps, and the diagonal embedding of `Q^x`; a generic Beurling prime system has no canonical analogue of this local-field package.

But the present calculation shows that

```text
"not reproducible by a generic Beurling system"
```

is only a necessary condition, not a sufficient one. The exact rational arithmetic can force a beautiful local-global law whose scalar global invariant is nevertheless constant and therefore incapable of selecting Riemann zeros.

This sharpens the accepted clue: arithmetic canonicality must produce **nontrivial global spectral/analytic content**, not merely a genuine reciprocity law.

## Relation to metaplectic/projective prior art

The connection between Hilbert symbols, scalar `2`-cocycles, metaplectic covers, and reciprocity is classical. In adelic metaplectic constructions the global cover is assembled from local cocycles and splits over the rational/principal subgroup; that splitting is another representation-theoretic expression of the same local-global cancellation principle.

Close prior art includes:

- J. S. Milne, *Class Field Theory*, version 4.03 (2020), Chapter VIII, section 5. Milne defines the Hilbert symbol through local Brauer/cup-product data, gives the symmetry relation, proves the Hilbert product formula, computes the real factor, and derives power/quadratic reciprocity from the local symbols. https://www.jmilne.org/math/CourseNotes/CFT.pdf
- Richard Hill, “Metaplectic covers of `GL_n` and the Gauss-Schering lemma,” *Journal de Theorie des Nombres de Bordeaux* **13**(1) (2001), 189–199, DOI `10.5802/jtnb.314`. It constructs metaplectic `2`-cocycles in direct connection with reciprocity laws.
- I. I. Piatetski-Shapiro, *Automorphic forms on the metaplectic group* (1978), which explicitly notes that the adelic metaplectic covering splits over the principal adeles.

No novelty is claimed for Hilbert symbols, reciprocity, quadratic reciprocity, metaplectic cocycles, or adelic splitting. The only durable purpose here is to eliminate a specific residual mechanism suggested by the preceding Mathia obstruction chain.

## Analytic-continuation boundary

Nothing in the Hilbert-symbol calculation crosses the Euler-product boundary.

The variables are rational numbers and local square classes; there is no complex parameter `s`, no Dirichlet series, no meromorphic continuation, and no completed functional equation. One could attach a separate analytic family to the local phases, but the reciprocity identity itself would not provide that continuation.

This is structurally different from Tate's mechanism in `PL-014`: Tate uses additive Fourier transform, self-dual measures, the archimedean place, and Poisson summation to continue the global zeta integral and to produce the involution `s -> 1-s`. Hilbert reciprocity supplies global arithmetic compatibility, but **not** that analytic bridge.

## Boundary conditions and surviving escapes

### Operator-valued local-global scattering is not ruled out

The decisive cancellation concerns the **scalar product of local Hilbert-symbol phases**. A family of local operators or scattering matrices can obey a product formula or reciprocity constraint without its global composition reducing to the number `1`. Noncommutative ordering, domains, kernels, determinants, or an automorphic representation may retain global spectral information.

That is the most relevant surviving branch of the accepted clue.

### A completed automorphic object can be nontrivial even when its central extension splits rationally

Metaplectic splitting over rational points does not make metaplectic automorphic theory trivial. The negative is narrower: the scalar cocycle value on the rational exponent-lattice inputs cannot itself be the missing zero-localizing invariant merely because it is locally arithmetic and globally normalized.

### Higher reciprocity symbols require separate analysis

The quadratic case already falsifies the proposed **generic principle** that replacing arbitrary phases by a canonical scalar reciprocity cocycle automatically creates useful RH rigidity. Higher norm-residue symbols and higher `K`-theoretic reciprocity laws may carry richer local data, but their relevance to zeta zeros would require an explicit global invariant that does not collapse under their own reciprocity law.

### The finding does not weaken the adelic completion route

On the contrary, it distinguishes two uses of local-global structure:

```text
scalar Hilbert reciprocity
    -> exact product cancellation;

Tate additive Fourier/Poisson completion
    -> nontrivial meromorphic continuation and functional equation.
```

The second contains analytic information absent from the first.

## Falsification / escape test

A future reciprocity-based prime-lattice proposal escapes this negative only if it proves at least one of the following:

1. its global invariant is not the scalar product of local norm-residue/Hilbert-symbol phases and remains nontrivial on rational principal data;
2. an operator-valued or scattering composition retains information after the scalar reciprocity cancellation and that retained information is canonically forced;
3. the construction couples reciprocity to a genuine analytic continuation theorem or explicit formula rather than only to algebraic exponent-vector data;
4. the retained global invariant distinguishes the rational-prime system from matched Beurling controls **and** is not identically fixed by the relevant product formula.

Conversely, if the proposed arithmetic projective phase reduces on exponent vectors to local Hilbert symbols whose only global operation is multiplication over all places, Hilbert reciprocity forces the candidate to be trivial.

## Consequence for the research line

The obstruction chain now separates three progressively stronger notions of joint prime structure:

```text
free scalar 1-cocycle
    -> arbitrary transfer function                         [PL-035]

free scalar projective 2-cocycle
    -> arbitrary pairwise phases                           [PL-036]

canonical arithmetic Hilbert-symbol local cocycle
    + scalar product-formula completion
    -> globally trivial by reciprocity                     [PL-038]
```

The surviving target is therefore narrower than “find a canonical arithmetic cocycle.” It is:

```text
find a global, preferably operator-valued or scattering invariant
whose local prime pieces are arithmetically forced,
whose completion survives reciprocity rather than cancelling to a scalar,
and whose analytic structure reaches the zeta zero divisor.
```

That target is consistent with the positive structural lessons of `PL-014` and with the automorphic scattering prior art of `PL-033`, but it is no longer supplied by scalar prime-lattice cohomology or reciprocity alone.