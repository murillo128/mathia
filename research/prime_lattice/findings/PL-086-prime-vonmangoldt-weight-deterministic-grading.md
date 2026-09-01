# PL-086 — Prime-only von Mangoldt half-weights collapse to deterministic macroscopic grading

## Claim

The most canonical arithmetic weighting left outside the support-only prime Gram analysis of `PL-081`--`PL-085` does **not** add an independent arithmetic degree of freedom when the index set has already been restricted to primes in a fixed macroscopic band.

Fix

```text
0<a<b<infinity,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
```

and, for any `T>0`, let

```text
G_(X,T)(p,q)
 =(1/T) integral_0^T exp(i t(log p-log q)) dt.
```

Consider the naturally rescaled Gram matrix of the critical half-weighted prime modes

```text
Lambda(p) p^(-1/2-it):

H_(X,T)
 = (X/(log X)^2)
   [ Lambda(p)Lambda(q)/(sqrt(pq))
     G_(X,T)(p,q) ]_(p,q in P_X).
```

Since `Lambda(p)=log p` on primes, define the deterministic macroscopic envelope

```text
B_X(p)=sqrt(X/p)
```

and the corresponding envelope-weighted support Gram

```text
K_(X,T)=B_X G_(X,T) B_X.
```

Then, with

```text
R_X(p)=log p/log X,
```

there is the **exact** factorization

```text
boxed:
H_(X,T)=R_X K_(X,T) R_X,
```

while uniformly on the whole band

```text
||R_X-I||_op=O_(a,b)(1/log X).
```

Consequently every ordered eigenvalue of `H_(X,T)` differs from the corresponding eigenvalue of `K_(X,T)` by a relative factor `1+O_(a,b)(1/log X)`, uniformly in the horizon `T` and uniformly across the hard edge and the upper edge. Their condition numbers therefore differ by a factor `1+O(1/log X)` whenever they are formed.

The determinant comparison is exact as well:

```text
boxed:
(1/M_X) log(det H_(X,T)/det K_(X,T))
 = (2/M_X) sum_(p in P_X)
     log(log p/log X)
 = O_(a,b)(1/log X).
```

At the mean-prime-gap horizon

```text
T_X=cX/log X,
```

the unconditional pair-sieve control already used in `PL-081`--`PL-083` gives

```text
(1/M_X)Tr(K_(X,T_X)^2)=O_(a,b,c)(1),
```

and hence the empirical spectral measures satisfy

```text
boxed:
W_2(mu_H,X,mu_K,X)=O_(a,b,c)(1/log X)->0.
```

Under the full local Hardy--Littlewood hierarchy assumed in `PL-085`, the proof of that finding extends verbatim through the bounded continuous envelope `X/p`. Thus the full bulk law of `H_(X,T_X)` is the same generic Poisson-sinc Euclidean-random-matrix law with local kernel multiplied by the deterministic factor `1/x` at `p~xX`. No additional bulk information is contributed by the factor `Lambda(p)` itself.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + DECISIVE-NEGATIVE` for the route

```text
prime basis support
+ Lambda(p)p^(-1/2) amplitude
+ finite-time spectral statistics
    -> an arithmetic escape from the support-only prime Gram branch.
```

The negative conclusion is deliberately restricted to **prime-only support in a fixed macroscopic band**. It does not apply to the full von Mangoldt sequence on the integer cone or to the prime-power axis skeleton of the completed explicit formula.

## Exact diagonal reduction

On a prime `p`,

```text
Lambda(p)=log p.
```

The natural rescaled amplitude in `H_(X,T)` is therefore

```text
sqrt(X)/log X * Lambda(p)/sqrt(p)

 =sqrt(X/p) * log p/log X

 =B_X(p) R_X(p).
```

Because `B_X` and `R_X` are diagonal, the Gram matrix factors exactly as

```text
H_(X,T)
 =(B_X R_X) G_(X,T) (B_X R_X)

 =R_X [B_X G_(X,T) B_X] R_X

 =R_X K_(X,T) R_X.
```

Now write `p=xX`, with `x in [a,b]`. Then

```text
R_X(p)
 =1+log(p/X)/log X,
```

so

```text
sup_(p in P_X) |R_X(p)-1|
 <= max(|log a|,|log b|)/log X.
```

Thus the only order-one half-weight remaining after prime support has already been selected is

```text
B_X(p)=sqrt(X/p),
```

a deterministic macroscopic grading. The specifically von-Mangoldt factor tends uniformly to the identity.

This sharpens the information split behind `PL-075`: the critical power `p^(-1/2)` is a universal scale choice, while on prime support the extra coefficient `Lambda(p)` is just the already-known logarithmic energy `log p` and becomes asymptotically scalar after the natural band normalization.

## Every eigenvalue is relatively unchanged by the von Mangoldt factor

Let

```text
r_-(X)=min_(p in P_X) R_X(p),
r_+(X)=max_(p in P_X) R_X(p).
```

For sufficiently large `X`, both are positive and

```text
r_-(X)=1+O(1/log X),
r_+(X)=1+O(1/log X).
```

For any nonzero vector, set `y=R_X x`. The Rayleigh quotient of `H=RKR` can be written as

```text
x* H x / ||x||^2
 = y* K y / (y* R_X^(-2) y).
```

Since

```text
r_+^(-2)||y||^2
 <= y*R_X^(-2)y
 <= r_-^(-2)||y||^2,
```

Courant--Fischer gives, for every eigenvalue index `j`,

```text
boxed:
r_-^2 lambda_j(K)
 <= lambda_j(H)
 <= r_+^2 lambda_j(K).
```

Therefore

```text
lambda_j(H)/lambda_j(K)
 =1+O_(a,b)(1/log X)
```

uniformly in `j` and `T`. In particular, the conclusion applies not only to normalized bulk observables but also to the smallest and largest eigenvalues.

The Gram matrices are positive definite for every `T>0`: for coefficients `c_p`,

```text
c*G c
 =(1/T) integral_0^T
   |sum_(p in P_X)c_p exp(i t log p)|^2 dt,
```

and a finite exponential polynomial with distinct frequencies `log p` cannot vanish identically on an interval unless every coefficient vanishes. Since the diagonal weights are positive, `H` and `K` are positive definite as well.

Hence

```text
(r_-^2/r_+^2) kappa(K)
 <= kappa(H)
 <= (r_+^2/r_-^2) kappa(K),
```

so any hard-edge ill-conditioning or upper-edge growth survives the insertion of `Lambda(p)` unchanged at relative leading order.

## The normalized determinant correction is explicit and macroscopic

Because all three matrices are positive definite,

```text
det H
 =det(R_X)^2 det K.
```

Therefore

```text
(1/M_X) log(det H/det K)
 = (2/M_X) sum_(p in P_X)
     log(log p/log X).
```

Uniformly on the band,

```text
log(log p/log X)=O_(a,b)(1/log X),
```

which proves the displayed `O(1/log X)` bound without any prime-distribution theorem beyond the existence of the band.

The prime number theorem makes even the first subleading term deterministic:

```text
(1/M_X) log(det H/det K)

 = (2/log X)
   [ (1/(b-a)) integral_a^b log x dx + o(1) ]
   +O_(a,b)(1/(log X)^2).
```

Thus a normalized `log det` cannot obtain a new leading arithmetic signal merely from multiplying an already prime-supported family by `Lambda(p)`. This does **not** settle the hard-edge integrability or determinant asymptotics of the envelope matrix `K` itself.

## Critical-scale empirical spectra are also unchanged

At

```text
T_X=cX/log X,
```

the centered support Gram satisfies

```text
|G_X(p,q)|^2
 <<_(a,b,c)
 min(1,(log X/|p-q|)^2).
```

The dimension-two prime-pair sieve used in `PL-081`--`PL-083` gives

```text
N_h(X)
 <<_(a,b) X/(log X)^2 S_+(h),

sum_(h<=Y) S_+(h) << Y.
```

Hence

```text
sum_(h<=log X) N_h(X)
 =O(X/log X),
```

and partial summation gives

```text
sum_(h>log X)
 N_h(X)(log X/h)^2
 =O(X/log X).
```

After adding the diagonal and dividing by `M_X~X/log X`,

```text
(1/M_X)Tr(G_X^2)=O_(a,b,c)(1)
```

unconditionally. Since `B_X(p)^2=X/p<=1/a`,

```text
(1/M_X)Tr(K_X^2)=O_(a,b,c)(1).
```

The relative eigenvalue estimate above now gives, with the ordered-eigenvalue coupling,

```text
W_2(mu_H,X,mu_K,X)^2
 <= (1/M_X) sum_j
      |lambda_j(H_X)-lambda_j(K_X)|^2

 << 1/(log X)^2
    * (1/M_X)Tr(K_X^2),
```

and therefore

```text
W_2(mu_H,X,mu_K,X)=O(1/log X).
```

This conclusion requires no Hardy--Littlewood asymptotic.

## Under local Hardy--Littlewood, the remaining envelope has a generic Poisson bulk

The `PL-085` compact-range argument survives the deterministic grading `B_X` with no new arithmetic input. In a closed walk of length `m`, every matrix edge contributes one factor from each endpoint, so the product of envelope weights is

```text
product_(j=0)^(m-1) X/p_j.
```

For every connected compact-range pattern at the critical scale,

```text
p_j=xX+O(log X),
```

and hence this product tends to `x^(-m)`. Thus the limiting fixed moments are

```text
(1/(b-a)) integral_a^b
 x^(-m) mu_m(x;c) dx,
```

where `mu_m(x;c)` is the Poisson-sinc Palm moment of `PL-084`--`PL-085`.

The rest of the proof is unchanged:

- the compact-range Carleman estimate only acquires the bounded factor `a^(-m)`;
- the local Hardy--Littlewood/Gallagher averaging is unchanged;
- the long-range Frobenius tail is multiplied by at most `a^(-2)`;
- Hoffman--Wielandt again removes the compact-range truncation.

Therefore, under the same **full local Hardy--Littlewood hierarchy** as `PL-085`, `K_X` converges in `W_2` to the macroscopic mixture of the unit-intensity Poisson sinc law whose local kernel at height `x` is

```text
k_env,x(u,v)
 = x^(-1) sinc(c(u-v)/(2x)).
```

Since `W_2(mu_H,X,mu_K,X)->0`, the half-weighted von-Mangoldt prime Gram has exactly this same limit. The bulk is still a generic local point-process law; `Lambda(p)` does not restore analytic-continuation data after the support has already been restricted to primes.

## Relation to the prime-power axis skeleton

This obstruction is specific to the **basis directions** `e_p`. It explains why the explicit-formula route of `PL-013` fundamentally uses the whole prime-power axis skeleton rather than only primes.

For an axis point

```text
n=p^k~X,
```

one has

```text
Lambda(p^k)=log p=(1/k)log(p^k),
```

so after normalization by `log X`,

```text
Lambda(p^k)/log X -> 1/k.
```

The depth `k` therefore survives as genuine order-one axis information. Restricting to primes fixes `k=1` and collapses this depth variable completely.

In exponent-lattice language:

```text
basis only {e_p}
    -> Lambda is just the energy log p
       and is asymptotically scalar on a macroscopic shell;

axis rays {k e_p : k>=1}
    -> Lambda/log n =1/k
       retains exponent-depth information.
```

This does not make the prime-power route novel: `PL-013` already identifies it with the classical completed Weil explicit formula. It does show precisely which lattice information the prime-support truncation discarded.

## Prior-art and novelty audit

No novelty is claimed for `Lambda(p)=log p`, for the `p^(-1/2)` critical weight, for finite Gram matrices, or for diagonal congruence estimates. Classical mean-value theory for Dirichlet polynomials already treats weighted coefficients, while `PL-075`--`PL-077` route genuinely long/full von-Mangoldt aggregates into Hardy--Littlewood, Selberg-variance, and zero-pair-correlation theory. `PL-013` already identifies the prime-power support of the completed explicit formula.

A targeted search around von-Mangoldt-weighted prime Dirichlet polynomials, prime-supported logarithmic Gram matrices, diagonal weighted Gram spectra, and weighted Euclidean random matrices did not locate a source asserting this exact bandwise reduction. The durable content here is therefore not a novelty claim but an exact **line-specific obstruction**: once prime support is selected first, the canonical `Lambda(p)` amplitude becomes a near-identity grading and cannot supply the missing RH information carrier at leading spectral order.

This closes a boundary explicitly left open by `PL-081`, `PL-083`, and `PL-085`, which excluded distinguished arithmetic weights from their support-only conclusions.

## Adversarial boundaries

1. **Prime support is essential.** For the full integer index set, `Lambda(n)` is sparse and supported on all prime powers; it is not a near-constant diagonal grading.
2. **The band is macroscopic and fixed.** Uniformity of `log p/log X->1` uses `aX<p<=bX` with fixed positive `a,b`. A scale whose multiplicative width grows with `X` needs a separate audit.
3. **Only the von-Mangoldt amplitude is removed.** The deterministic envelope `sqrt(X/p)` remains nonconstant across `[a,b]`, and the prime support itself remains arithmetic.
4. **The determinant statement is normalized by dimension.** The raw determinant ratio can be exponentially large or small on subleading scales even though its logarithm per prime is `O(1/log X)`.
5. **The hard edge of `K` is not classified.** The result proves that `Lambda(p)` cannot repair or fundamentally change it; it does not prove that every determinant/extreme statistic of `K` is generic.
6. **The Poisson full-bulk conclusion is conditional.** It inherits exactly the full local Hardy--Littlewood hierarchy of `PL-085`. Only the `H` versus `K` comparison and the critical-scale `W_2` closeness are unconditional.
7. **No analytic continuation occurs.** Every exact identity is finite-dimensional. The conditional bulk law uses local prime tuples, not a continuation of the Euler product.
8. **Fine amplified corrections are not advertised as an RH mechanism.** One may magnify the `O(1/log X)` difference, but its coefficient is the explicit deterministic function `log(p/X)` of the already-known prime frequency. Any claim that such an amplification creates new arithmetic information would need a separate falsifiable mechanism and matched controls.

## Consequence for the prime-lattice search

The weighted escape from the support-only critical Gram now splits cleanly:

```text
prime support + Lambda(p)p^(-1/2)
    -> deterministic p^(-1/2) macroscopic grading
       + a von-Mangoldt factor that tends uniformly to 1;

full Lambda(n)n^(-1/2) on the positive cone
    -> sparse prime-power support / Hardy--Littlewood and
       global zero-correlation channels (`PL-013`, `PL-075`--`PL-077`).
```

Thus merely attaching the canonical von-Mangoldt half-weight to the **prime basis directions** does not escape the support-only universality and cluster obstructions of `PL-081`--`PL-085`. A surviving weighted mechanism must retain information that prime preselection erased: prime-power depth, a target/completion coupling, a genuinely global aggregate, or another arithmetic amplitude not determined by the same prime frequency itself.