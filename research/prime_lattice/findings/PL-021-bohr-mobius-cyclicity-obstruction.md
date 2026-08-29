# PL-021 — The canonical Möbius Euler product is cyclic everywhere it belongs to Bohr `H^2`, so native prime-lattice cyclicity cannot encode RH

## Claim

For every real `sigma>1/2`, the canonical square-free/Möbius vector of the prime-exponent lattice

```text
M_sigma(z)
  = product_p (1-p^(-sigma) z_p)
  = sum_(n>=1) mu(n)n^(-sigma) z^(v(n))
```

is a cyclic vector of the standard Hardy space `H^2(D_2^infinity)` of the Hilbert multidisc under multiplication by the prime coordinates. Equivalently,

```text
closure span { z^alpha M_sigma : alpha in N_0^(P), finite support }
    = H^2(D_2^infinity).
```

This cyclicity is unconditional. At the endpoint `sigma=1/2`, however, `M_sigma` is no longer an `H^2` vector at all:

```text
||M_sigma||_2^2
 = sum_n mu(n)^2 n^(-2 sigma)
 = product_p (1+p^(-2 sigma))
 = zeta(2 sigma)/zeta(4 sigma),
```

which is finite exactly for `sigma>1/2` and diverges at `sigma=1/2`.

Thus the natural proposal

```text
square-free prime-lattice Möbius orientation
   -> Bohr H^2 cyclicity / completeness
   -> RH
```

is decisively blocked in the native Bohr-Hardy space: throughout the entire region where the Möbius Euler-product vector exists as an `H^2` element, it is already cyclic without RH, and at the critical boundary the vector exits the Hilbert space rather than undergoing an RH-sensitive cyclic/noncyclic transition.

**Evidence/status:** `LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the specifically stated native-Bohr-`H^2` cyclicity route. Nikolski's Hilbert-multidisc cyclicity theorem is literature; the specialization to the Möbius Euler product, the exact norm identities, and the comparison with the Nyman/Bagchi Hardy space are derived here. No novelty is claimed for Hilbert-multidisc cyclicity theory or the exponent-vector encoding.

## Exact prime-lattice realization

Let

```text
a_sigma = (p^(-sigma))_p.
```

For `sigma>1/2`,

```text
sum_p |a_sigma,p|^2 = sum_p p^(-2 sigma) < infinity,
```

so `a_sigma` is a point of the Hilbert multidisc `D_2^infinity`. The Euler product

```text
M_sigma(z)=product_p (1-a_sigma,p z_p)
```

is pointwise well defined and nonzero on `D_2^infinity`: for every `z in l^2`, Cauchy-Schwarz gives

```text
sum_p |a_sigma,p z_p|
 <= ||a_sigma||_2 ||z||_2
 < infinity,
```

and each factor is nonzero because `|a_sigma,p z_p|<1`. Hence the infinite product converges to a nonzero holomorphic function on the Hilbert multidisc.

Expanding the product uses each prime coordinate at most once:

```text
M_sigma(z)
 = sum_(S finite subset P)
      (-1)^|S| product_(p in S) p^(-sigma) product_(p in S) z_p
 = sum_(n square-free) mu(n)n^(-sigma) z^(v(n)).
```

This is exactly the oriented `{0,1}` sector of the exponent lattice, not an auxiliary encoding.

Its Hardy norm is therefore

```text
||M_sigma||_2^2
 = sum_n mu(n)^2 n^(-2 sigma)
 = product_p (1+p^(-2 sigma)).
```

For `sigma>1/2`, the standard Euler identity gives

```text
product_p (1+p^(-2 sigma))
 = zeta(2 sigma)/zeta(4 sigma).
```

The product converges precisely when `sum_p p^(-2 sigma)` does, hence precisely for `sigma>1/2`. At `sigma=1/2`, `sum_p 1/p` diverges and `M_(1/2)` is not in `H^2`.

## Cyclicity from Nikolski's theorem

Nikolski's 2012 Theorem 3.3 gives a sufficient condition for a nonvanishing `F in H^2(D_2^infinity)` to be cyclic under all coordinate shifts. In the corrected formulation/proof, it is enough that for some `epsilon>0` and integer `N>=1`,

```text
F^(1+epsilon) in H^2(D_2^infinity),
1/F^(1/N) in H^2(D_2^infinity).
```

The 2018 correction repairs the construction of powers and polynomial density used in the 2012 argument; it does not retract this sufficient cyclicity route.

For `F=M_sigma`, choose `epsilon=1` and `N=1`. The inverse is the reproducing-kernel Euler product at `a_sigma`:

```text
1/M_sigma(z)
 = product_p (1-p^(-sigma)z_p)^(-1)
 = sum_(n>=1) n^(-sigma) z^(v(n)).
```

Therefore

```text
||1/M_sigma||_2^2
 = sum_n n^(-2 sigma)
 = zeta(2 sigma)
 < infinity
```

for every `sigma>1/2`.

Likewise,

```text
M_sigma(z)^2
 = product_p (1-2p^(-sigma)z_p+p^(-2sigma)z_p^2),
```

and orthogonality of monomials gives the exact finite-product norm factors

```text
||M_sigma^2||_2^2
 = product_p (1+4p^(-2 sigma)+p^(-4 sigma)).
```

Since

```text
log(1+4x+x^2) = O(x)  as x -> 0,
```

this infinite product is finite when `sum_p p^(-2 sigma)<infinity`. Hence both hypotheses of Nikolski's theorem hold, and

```text
M_sigma is cyclic in H^2(D_2^infinity) for every sigma>1/2.
```

This is very close to explicit prior art rather than a new cyclicity phenomenon. Nikolski proves that every reproducing kernel

```text
K_a(z)=product_p (1-a_p z_p)^(-1)
```

is cyclic, and recovers Wintner's cyclicity of the Dirichlet vector with coefficients `n^(-sigma)` for `sigma>1/2`. The present Möbius statement is the reciprocal-kernel specialization of the same theorem: `M_sigma=1/K_(a_sigma)` and the two elementary norm checks above put the reciprocal into Theorem 3.3.

## Dirichlet-series interpretation and the analytic-continuation boundary

Under the standard Bohr transform, `M_sigma` corresponds to the square-summable-coefficient Dirichlet series

```text
D_sigma(w)
 = sum_(n>=1) mu(n)n^(-sigma)n^(-w).
```

Point evaluation for the standard Dirichlet-Hardy space is continuous only for

```text
Re(w)>1/2.
```

When `sigma>1/2`, every such point automatically satisfies

```text
Re(w+sigma)>1.
```

Therefore, throughout the point-evaluation region actually used by this Hilbert space, the ordinary absolutely convergent Dirichlet-series identity is valid:

```text
D_sigma(w)=1/zeta(w+sigma).
```

No analytic continuation through `Re(w+sigma)=1` is involved in the cyclicity proof. In particular, this construction does **not** provide an `H^2` avatar of `1/zeta` inside the critical strip. Its function-theoretic access to `1/zeta` stays entirely in the classical Euler-product half-plane.

This is the exact boundary distinction that must not be blurred:

```text
sigma>1/2:
    M_sigma in Bohr H^2,
    M_sigma cyclic unconditionally,
    point evaluations only see Re(w+sigma)>1;

sigma=1/2:
    ||M_sigma||_2=infinity,
    so the native Bohr-H^2 cyclicity question ceases to exist.
```

Trying instead to remove the coefficient damping and use `sum mu(n)n^(-w)` directly does not help: the coefficient sequence `(mu(n))` is not in `l^2`, so that function is outside this standard Bohr `H^2` from the outset.

## Why this does not contradict Nyman–Beurling / Bagchi

`PL-017` through `PL-020` concern a different Hilbert geometry. Bagchi's reformulation places

```text
G_n(s)=(n^(-s)-n^(-1)) zeta(s)/s
```

in the classical half-plane Hardy space `H^2(Re(s)>1/2)` obtained from a Mellin transform, and RH is equivalent to totality of the distinguished Nyman span there.

The present space is instead the coefficient/Bohr Hardy space

```text
mathcal H^2
 <-> H^2(D_2^infinity),
```

whose norm is the `l^2` norm of Dirichlet coefficients. These spaces have different norms, different evaluation geometry, and different ways of crossing—or failing to cross—the line of absolute convergence.

Nikolski explicitly distinguishes the periodic dilation/Hilbert-multidisc cyclicity problem from Nyman's non-periodic RH completeness problem. Therefore one cannot transfer the unconditional cyclicity of `M_sigma` into the Nyman setting, nor can one infer that Nyman cyclicity is easy. The negative result is the converse: **moving the Möbius/RH completeness question into the native Bohr coefficient space throws away precisely the difficult analytic-continuation content.**

## Prior art and novelty audit

The candidate was searched structurally through Hilbert-multidisc cyclic vectors, periodic dilation systems, Hardy spaces of Dirichlet series, weak invertibility, reproducing kernels, reciprocal kernels, Möbius coefficients, and Euler-product cyclicity.

- Hedenmalm–Lindqvist–Seip (1997) are the foundational source identifying square-summable Dirichlet coefficients with Hardy space on the infinite polydisc/character space and translating periodic dilation completeness into cyclicity.
- Nikolski (2012) makes the exponent-vector semigroup explicit, proves the relevant Hilbert-multidisc sufficient cyclicity theorem, proves all reproducing kernels are cyclic, and states the Wintner specialization `sum n^(-sigma)z^n` for `Re(sigma)>1/2`.
- Nikolski's 2018 correction repairs technical points in the 2012 construction of powers and polynomial density and corrects an unrelated invariant-subspace formula. The correction was checked before using Theorem 3.3.
- No reliable source was found that promotes the reciprocal Möbius specialization above as an RH mechanism. In any case, the specialization is an immediate theorem application and is classified here only as `LITERATURE+DERIVED`, not as new mathematics.

The value of the finding is therefore not novelty but a clean route-killing distinction between two superficially similar uses of multiplicative cyclicity.

## Boundary conditions and adversarial checks

### Cyclicity is only claimed for `sigma>1/2`

At `sigma=1/2`, the defining coefficient vector is not in `H^2`. Nothing here defines a renormalized boundary cyclic vector. A different function space or renormalization could in principle produce a meaningful critical object, but that would be additional structure and is not covered by this negative result.

### The theorem requires nonvanishing on the Hilbert multidisc

This holds for `M_sigma` because `a_sigma,z in l^2` imply `sum_p |a_sigma,p z_p|<infinity`, and every factor has modulus-separated-from-zero pointwise (`|a_sigma,p z_p|<1`). Thus the convergent product cannot acquire a zero from an infinite accumulation of factors.

### The inverse being in `H^2` does not mean it is bounded

`1/M_sigma` is generally not an `H^infinity` multiplier. The argument deliberately uses Nikolski's weaker Theorem 3.3(3), not the simpler bounded-inverse criterion.

### `1/zeta(w+sigma)` is used only where the Dirichlet series converges absolutely

The identity is invoked only when `Re(w)>1/2` and `sigma>1/2`, hence `Re(w+sigma)>1`. No claim about the analytic continuation of `1/zeta` in the critical strip is smuggled into the Bohr product.

### This does not rule out other enriched Bohr constructions

The decisive negative applies to the canonical Möbius Euler-product vector and cyclicity/completeness in the **standard** coefficient `H^2`. A mechanism using an adelic completion, a different weighted Hilbert norm, a singular/renormalized critical boundary, the Nyman target geometry, or an operator that genuinely incorporates analytic continuation lies outside the claim.

## Falsification / audit test

The finding should be withdrawn if any of the following exact steps fails:

1. `M_sigma` is an `H^2(D_2^infinity)` nonvanishing function for every `sigma>1/2` with coefficients `mu(n)n^(-sigma)`;
2. `1/M_sigma` belongs to `H^2` with squared norm `zeta(2 sigma)`;
3. `M_sigma^2` belongs to `H^2` because `product_p(1+4p^(-2sigma)+p^(-4sigma))<infinity`;
4. Nikolski's corrected sufficient criterion implies cyclicity from these two memberships;
5. at `sigma=1/2`, `sum_n mu(n)^2/n` diverges, so the canonical Möbius vector is outside standard Bohr `H^2`;
6. the Dirichlet identity with `1/zeta(w+sigma)` is used only in `Re(w+sigma)>1`.

All six points are independently checkable without RH.

## Consequence for the research line

The square-free hypercube and Möbius orientation remain arithmetically important, but **their most direct cyclicity in the native prime-lattice Hardy space is too easy**. The critical value `1/2` marks loss of square-summable membership, not an RH-sensitive defect of the cyclic span.

Future cyclicity/completeness work should therefore remain on structures that retain information beyond coefficient-space Bohr geometry—for example the Nyman/Bagchi Mellin target and its model-space obstruction (`PL-017`–`PL-020`), or a genuinely new critical-boundary/renormalized space whose definition survives `sigma=1/2` and whose cyclicity is not already automatic by Hilbert-multidisc weak-invertibility theory.

## Sources

- Nikolai Nikolski, “In a shadow of the RH: Cyclic vectors of Hardy spaces on the Hilbert multidisc,” *Annales de l'Institut Fourier* **62**(5) (2012), 1601–1626. DOI: `10.5802/aif.2731`. In particular Theorem 3.3, Corollaries 3.7–3.8, and the Bohr/exponent-semigroup intertwining in Section 2.
- Nikolai Nikolski, “A correction to ‘In a shadow of the RH: Cyclic vectors of Hardy spaces on the Hilbert multidisc’,” *Annales de l'Institut Fourier* **68**(2) (2018), 563–567. DOI: `10.5802/aif.3170`.
- Håkan Hedenmalm, Peter Lindqvist, Kristian Seip, “A Hilbert space of Dirichlet series and systems of dilated functions in `L^2(0,1)`,” *Duke Mathematical Journal* **86** (1997), 1–37. DOI: `10.1215/S0012-7094-97-08601-4`.
