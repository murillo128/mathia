# PL-112 — Fixed-degree symmetric depth couplings scalarize to prime-zeta functions

## Claim

`PL-111` leaves genuinely nonmultiplicative mixed-coordinate depth couplings outside its scalar zeta-ratio no-go. The cheapest such coupling can be tested exactly, and it still scalarizes.

For a fixed depth `l>=1`, define

```text
omega_l(n) = #{p : v_p(n)>=l}
```

and, for fixed `k>=0`,

```text
C_(l,k)(n) = binom(omega_l(n),k).
```

For `k>=2`, this is a genuine mixed-coordinate statistic in the minimal precise sense: it counts unordered `k`-tuples of distinct prime coordinates that simultaneously cross depth `l`, and it is not multiplicative. Nevertheless, for `Re(s)>1`,

```text
D_(l,k)(s)
 := sum_(n>=1) C_(l,k)(n)n^(-s)
  = zeta(s) e_k((p^(-l s))_p),
```

where `e_k` is the `k`th elementary symmetric function of the prime weights. Newton's identities then give

```text
k e_k
 = sum_(j=1)^k (-1)^(j-1) e_(k-j) P(j l s),

P(z)=sum_p p^(-z),
```

so every fixed `D_(l,k)` is `zeta(s)` times a scalar polynomial in

```text
P(l s), P(2 l s), ..., P(k l s).
```

In particular, the first pair interaction is

```text
D_(l,2)(s)
 = zeta(s)/2 * (P(l s)^2-P(2 l s)).
```

More generally, every fixed polynomial observable `Q(omega_l(n))` has a Dirichlet series of this same finite prime-zeta form, because every polynomial in an integer variable is a finite linear combination of the binomial polynomials `binom(x,k)`.

Thus **breaking multiplicativity by a bounded-degree symmetric coupling of several exponent coordinates is not enough to escape one-variable scalarization**. The mixed interaction is real at coefficient level, but the Dirichlet transform sees only finitely many scalar prime-zeta functions.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PRIME-ZETA + NEGATIVE-BOUNDARY`.

No novelty is claimed for prime-zeta functions, the classical `omega(n)` generating products, elementary symmetric-function identities, or Newton's identities. The durable contribution is the line-specific falsification boundary: the most direct finite-degree symmetric version of the mixed-depth escape left open by `PL-111` still collapses before producing a non-scalar operator, positivity law, or critical-line geometry.

## 1. The pair statistic genuinely couples distinct exponent directions

The depth indicator of one coordinate is

```text
X_(p,l)(n)=1_(v_p(n)>=l)=1_(p^l | n).
```

Hence

```text
omega_l(n)=sum_p X_(p,l)(n)
```

and

```text
C_(l,k)(n)
 = sum_(p_1<...<p_k)
     product_(r=1)^k X_(p_r,l)(n).
```

For `k=2`, two coordinates must be occupied simultaneously. If `p!=q`, then

```text
C_(l,2)(p^l)=0,
C_(l,2)(q^l)=0,
C_(l,2)(p^l q^l)=1,
```

so `C_(l,2)` is not multiplicative. This is therefore not another instance of the multiplicative coordinate-by-coordinate observable in `PL-110`--`PL-111`.

The interaction is nevertheless highly symmetric: it depends only on **how many** coordinates reach the threshold, not on which primes they are or on any relation between their energies. That symmetry is exactly what permits the collapse below.

## 2. Exact Dirichlet scalarization

For `Re(s)>1`, absolute convergence permits the sums to be rearranged. Since

```text
product_(r=1)^k X_(p_r,l)(n)
 = 1_((p_1...p_k)^l | n),
```

we obtain

```text
D_(l,k)(s)
 = sum_(p_1<...<p_k)
     sum_((p_1...p_k)^l | n) n^(-s)

 = zeta(s)
   sum_(p_1<...<p_k)
     (p_1...p_k)^(-l s).
```

The final prime sum is precisely

```text
e_k((p^(-l s))_p).
```

Equivalently, all binomial moments are packaged by the exact generating deformation

```text
H_l(s,u)
 := sum_(n>=1) (1+u)^(omega_l(n)) n^(-s)
  = zeta(s) product_p (1+u p^(-l s)),
```

again for `Re(s)>1`. The local factor follows directly from

```text
sum_(a=0)^(l-1) p^(-a s)
 +(1+u) sum_(a=l)^infinity p^(-a s)
 = (1+u p^(-l s))/(1-p^(-s)).
```

Taking the coefficient of `u^k` recovers `D_(l,k)`.

Newton's identities express each elementary symmetric function using the power sums

```text
sum_p (p^(-l s))^j=P(j l s).
```

For example,

```text
e_1=P(l s),

e_2=(P(l s)^2-P(2 l s))/2,

e_3=(P(l s)^3-3P(l s)P(2 l s)+2P(3 l s))/6.
```

Therefore no matter how many distinct coordinates a **fixed** binomial moment couples, its Dirichlet transform remains a scalar function of one complex variable built from finitely many prime-zeta evaluations.

A useful consistency check is `u=1`:

```text
sum_(n>=1) 2^(omega_l(n)) n^(-s)
 = zeta(s) product_p(1+p^(-l s))
 = zeta(s) zeta(l s)/zeta(2 l s).
```

At `l=1` this is the classical identity

```text
sum_(n>=1) 2^(omega(n))n^(-s)=zeta(s)^2/zeta(2s).
```

So even the full fixed-parameter generating deformation can collapse further to an ordinary zeta ratio at special parameter values.

## 3. Analytic continuation does not restore multidimensional geometry

All Euler/product and rearrangement identities above are asserted only for `Re(s)>1`. Beyond that half-plane one must use analytic continuation of the scalar functions on the right, not termwise continuation of the prime product.

Fröberg's classical prime-zeta continuation starts from

```text
log zeta(z)=sum_(m>=1) P(m z)/m
```

in the absolute-convergence region and Möbius inversion gives

```text
P(z)=sum_(m>=1) mu(m)/m * log zeta(m z).
```

Branchwise continuation of `P` into `Re(z)>0` therefore inherits logarithmic singularities from the pole and zeros of `zeta`; `Re(z)=0` is the classical natural boundary. Consequently, whenever the finite prime-zeta expression for `D_(l,k)` is continued beyond `Re(s)>1`, all zero-sensitive information still enters through scalar terms of the form

```text
log zeta(m j l s).
```

A nontrivial zeta zero `rho` can therefore enter only through scaled locations

```text
s = rho/(m j l),
```

subject to the usual branch choices and possible coincidences among scalar terms. Under RH, the corresponding inherited real parts are

```text
Re(s)=1/(2 m j l),
```

not a new line selected by the mixed-coordinate interaction. The unique occurrence of `1/2` at `m=j=l=1` is simply the undilated original zeta scale.

The relevant point is not that every moment must have exactly the same branch singularities — special combinations can cancel logarithms, as the `u=1` zeta-ratio identity shows. It is that the entire continuation problem has already collapsed to the classical one-variable algebra generated by zeta and prime-zeta values. No residual operator, matrix geometry, or coordinate-coupling law remains that could independently constrain `Re(rho)`.

## 4. The scalarization is portable to a generic free multiplicative system

The negative control does not depend on rational-prime arithmetic.

Let `lambda_j>0` be arbitrary coordinate energies for a free commutative monoid `N_0^(J)` and define

```text
E(alpha)=sum_j alpha_j lambda_j,

Z_lambda(s)=product_j (1-exp(-s lambda_j))^(-1),

omega_l(alpha)=#{j:alpha_j>=l}.
```

Whenever the products converge absolutely, the identical incidence argument gives

```text
sum_alpha binom(omega_l(alpha),k) exp(-s E(alpha))
 = Z_lambda(s)
   e_k((exp(-l s lambda_j))_j).
```

Thus the mechanism survives unchanged after replacing

```text
lambda_p=log p
```

by an arbitrary admissible frequency list. The rational primes enter the Riemann case only through the scalar specialization of the coordinate weights. This fails the research line's matched-control requirement for a mechanism that is supposed to distinguish the exact rational-prime norm map from generic multiplicative frequency systems.

## 5. Prior art and novelty audit

The main continuation anchor is already present in `research/prime_lattice/SOURCES.md`:

- **Carl-Erik Fröberg**, “On the prime zeta function,” *BIT Numerical Mathematics* **8**(3) (1968), 187–202. DOI `10.1007/BF01933420`. Fröberg gives the classical prime-zeta continuation through Möbius inversion of `log zeta`, including the logarithmic singularity structure and natural boundary used above.

The `l=1` generating functions for `omega(n)` and their Euler products are classical analytic-number-theory material, and expressing symmetric prime sums through the power sums `P(j s)` is standard symmetric-function algebra. A targeted literature audit on 2 September 2026 also found the established almost-prime/prime-zeta literature in which reciprocal-power sums over fixed factor counts are expanded in products of ordinary prime-zeta values. None of this is treated as Mathia novelty.

The new durable statement is narrower and internal to this research program:

```text
PL-111 residual escape:
nonmultiplicative mixed exponent-depth coupling

cheapest symmetric fixed-degree test:
binom(#{p:v_p>=l},k)

exact outcome:
zeta(s) times a finite prime-zeta symmetric polynomial
```

That is a falsification result for a natural design family, not a new theorem about the prime zeta function.

## Adversarial boundaries

1. **This does not rule out arbitrary mixed-coordinate couplings.** A kernel depending on the identities or relative energies of `p` and `q`, incidence data not reducible to a symmetric count, or a target-relative operator may escape the argument.
2. **Fixed degree is essential.** If the interaction order `k` grows with the cutoff or spectral parameter, infinitely many prime-zeta scales may enter and the finite-polynomial reduction no longer describes the limiting problem uniformly.
3. **Polynomial dependence on `omega_l` is the exact class closed here.** Non-polynomial functions can be studied through `H_l(s,u)` or other transforms, but limits involving infinitely many binomial moments require a separate analysis.
4. **Scalarization does not mean triviality.** Prime-zeta functions have rich and delicate continuation. The negative conclusion is that their zero-sensitive structure is inherited from scalar zeta logarithms rather than generated by a new multidimensional lattice mechanism.
5. **No Euler product is used in the critical strip.** The identities are proved in `Re(s)>1`; any further statement uses the classical continuation of `zeta`/`P`.
6. **No RH equivalence is claimed.** The scaled zero singularities are a re-encoding of the zeta divisor, not a criterion forcing it onto the critical line.

## Consequence for the research line

`PL-110`--`PL-111` showed that a full-lattice depth observable can scalarize when it is multiplicative, and left nonmultiplicative depth coupling as a plausible escape. The present calculation shows that **nonmultiplicativity alone is not the missing ingredient**: even simultaneous interactions among arbitrarily many distinct prime coordinates collapse if their order is fixed and the observable only counts how many coordinates cross a common depth.

A viable mixed-depth continuation of the prime-lattice program must therefore carry information that this symmetric count forgets. Examples still outside the no-go include prime-label-dependent pair kernels, relations between coordinate energies, scale-growing interaction order, genuinely nonlocal incidence geometry, or an operator/positivity construction coupled to a distinguished arithmetic target. Such a candidate must also fail the generic free-monoid control above before its geometry can be credited with rational-prime-specific RH content.
