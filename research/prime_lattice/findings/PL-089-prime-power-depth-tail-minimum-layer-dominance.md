# PL-089 — Every fixed prime-power depth tail has the ordinary bulk spectrum of its minimum depth

## Claim

`PL-087` shows that higher prime powers are a vanishing-rank perturbation of the prime block in the full prime-power shell, while `PL-088` shows that one isolated fixed depth `k` is exactly a time-dilated prime Gram. The remaining ordinary-bulk escape is to condition away the shallower layers and retain **all cross-depth couplings** among the surviving prime powers. For every fixed minimum depth `K>=2`, that escape also collapses.

Fix

```text
0<a<b<infinity,
K>=2 fixed,
Q_(X,>=K)={p^k : p prime, k>=K, aX<p^k<=bX},
Q_(X,K)={p^K : p prime, aX<p^K<=bX},
R_(X,K)=Q_(X,>=K)\Q_(X,K).
```

Write

```text
M_(X,K)=|Q_(X,K)|,
r_(X,K)=|R_(X,K)|,
N_(X,K)=M_(X,K)+r_(X,K).
```

Then the prime number theorem gives

```text
M_(X,K)
 ~ K (b^(1/K)-a^(1/K)) X^(1/K)/log X,
```

while the next depth is already lower order:

```text
r_(X,K)
 ~ (K+1)(b^(1/(K+1))-a^(1/(K+1)))
    X^(1/(K+1))/log X.
```

Consequently

```text
boxed:
r_(X,K)/N_(X,K)
 =O_(a,b,K)(X^(-1/(K(K+1)))) ->0.
```

Now let `A_X` be **any Hermitian matrix** indexed by `Q_(X,>=K)`, and let `H_(X,K)` be its principal block indexed by the minimum-depth layer `Q_(X,K)`. This includes, in particular, every finite-time logarithmic Gram matrix and the naturally normalized von-Mangoldt half-weighted Gram used in `PL-087`--`PL-088`, with all cross-depth entries retained.

If `F_A` and `F_H` denote their dimension-normalized empirical eigenvalue distribution functions, then

```text
boxed:
sup_y |F_(A_X)(y)-F_(H_(X,K))(y)|
 <= 3 r_(X,K)/N_(X,K)
 =O_(a,b,K)(X^(-1/(K(K+1)))) ->0.
```

The bound is independent of the observation time, the logarithmic kernel, and the sizes of the cross-depth matrix entries. It is a pure dimension/rank obstruction.

Therefore every weak ordinary-bulk spectral limit of the whole fixed tail `k>=K` is exactly the weak bulk limit of its minimum depth `K`. Combining this with the exact time-dilation identity of `PL-088`, the tail ordinary bulk is reduced to the ordinary prime-support Gram at base scale

```text
Y=X^(1/K)
```

with time changed by `T -> K T` and, for the natural von-Mangoldt half-weight, only the deterministic depth/macroscopic grading already identified in `PL-088`.

At the depth-`K` mean-gap horizon

```text
T_(X,K)=c X^(1/K)/log X
       =cY/(K log Y),
```

so that `K T_(X,K)=cY/log Y`, the full local Hardy--Littlewood hierarchy used in `PL-085` implies that the entire tail `k>=K` has the **same weak Poisson-sinc bulk law** as the depth-`K` prime block, up to the deterministic local factor

```text
1/(K^2 y^K),
```

with `p=yY`. Cross-depth couplings do not create an additional ordinary empirical spectral phase.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-CONTEXT + DECISIVE-NEGATIVE` for the route

```text
condition away all depths <K
+ retain every prime-power layer k>=K
+ retain all cross-depth Gram couplings
+ ordinary dimension-normalized empirical spectrum
    -> a new exponent-depth spectral phase.
```

The conclusion is deliberately restricted to **fixed `K` and ordinary weak empirical spectral laws**. It does not control hard-edge statistics, extreme eigenvalues, raw or regularized determinants, high moments, inverse-density amplification of deeper layers, depth-dependent reweightings, Schur-complement observables considered outside normalized ESD, or growing minimum depth `K=K(X)`.

## The minimum surviving depth dominates the tail cardinality

Every prime power has a unique representation `p^k` with prime base `p`. For fixed depth `k`, the shell condition is

```text
(aX)^(1/k)<p<=(bX)^(1/k).
```

Hence, by the prime number theorem,

```text
|Q_(X,k)|
 =pi((bX)^(1/k))-pi((aX)^(1/k))

 ~ k(b^(1/k)-a^(1/k))
    X^(1/k)/log X.
```

In particular the `k=K` layer has size of order `X^(1/K)/log X`, whereas the first omitted layer `k=K+1` has size of order `X^(1/(K+1))/log X`.

For all deeper exponents `k>=K+2`, there are only `O(log X)` possible values of `k`, and each layer contains at most `O_(b,K)(X^(1/(K+2)))` points. Therefore

```text
sum_(k>=K+2)|Q_(X,k)|
 =O_(a,b,K)(X^(1/(K+2)) log X)
 =o(X^(1/(K+1))/log X).
```

Thus the `K+1` layer dominates the whole remainder:

```text
r_(X,K)
 ~ (K+1)(b^(1/(K+1))-a^(1/(K+1)))
    X^(1/(K+1))/log X.
```

Dividing by the depth-`K` asymptotic gives

```text
r_(X,K)/M_(X,K)
 =O_(a,b,K)(
    X^(1/(K+1)-1/K)
   )

 =O_(a,b,K)(X^(-1/(K(K+1)))).
```

Since `N=M+r`, the same estimate holds with `N` in the denominator.

This is a recursive version of the density obstruction used in `PL-087`: after deleting any finite collection of shallower exponent layers, the **new minimum depth still asymptotically contains all matrix dimensions**.

## Cross-depth couplings are only a vanishing-rank perturbation for ESD

Order the tail indices with `Q_(X,K)` first. Every Hermitian matrix on the tail has block form

```text
A_X = [ H_(X,K)   C_X ]
      [ C_X^*      D_X ],
```

where the lower block has dimension `r=r_(X,K)`. Compare it with

```text
A_X^0=diag(H_(X,K),0_r).
```

Then

```text
A_X-A_X^0
 = [ 0       C_X ]
   [ C_X^*   D_X ].
```

The top component of its image lies in the column space of `C_X`, of dimension at most `r`, and the bottom component lies in the `r`-dimensional deeper-layer coordinate space. Hence

```text
rank(A_X-A_X^0)<=2r.
```

The standard rank/interlacing inequality for Hermitian matrices of equal size gives

```text
sup_y |F_(A_X)(y)-F_(A_X^0)(y)|
 <=2r/N.
```

On the other hand,

```text
F_(A_X^0)(y)
 =(M/N)F_(H_(X,K))(y)
  +(r/N) 1_(y>=0),
```

so

```text
sup_y |F_(A_X^0)(y)-F_(H_(X,K))(y)|
 <=r/N.
```

The triangle inequality yields the claimed

```text
sup_y |F_(A_X)(y)-F_(H_(X,K))(y)|
 <=3r/N.
```

No bound on `||C_X||`, `||D_X||`, or the Gram weights is needed. This is why even potentially large cross-depth interactions cannot change the ordinary weak empirical law: they act through only `o(N)` rows and columns.

The same strength is also the main limitation. A rank-`o(N)` perturbation can still move a small set of eigenvalues by arbitrarily large amounts, create or remove tiny eigenvalues, and change determinants drastically. The argument says nothing about those observables.

## Reduction to the depth-`K` prime process

For the logarithmic finite-time Gram,

```text
G_(X,T)(p^K,q^K)
 =(1/T) integral_0^T
   exp(i t K(log p-log q)) dt.
```

With `Y=X^(1/K)`, `PL-088` gives the exact identity

```text
G_(X,T)^(K)=G_(Y,KT)^prime.
```

For the naturally normalized von-Mangoldt half-weighted block,

```text
A_(X,T)^(K)
 =(1/K^2)
  R_Y B_(K,Y)
  G_(Y,KT)^prime
  B_(K,Y) R_Y,
```

where

```text
B_(K,Y)(p)=(Y/p)^(K/2),
R_Y(p)=log p/log Y=1+O_(a,b,K)(1/log Y)
```

uniformly on the fixed base-prime band.

The tail theorem therefore contains no hidden analytic-continuation step. The cross-depth reduction is finite-dimensional rank geometry, and the remaining minimum-depth block is an exact reparameterization of the prime process. Any zero-sensitive conclusion would still require extra global arithmetic/analytic input beyond this Gram geometry.

At the depth-critical horizon

```text
T_(X,K)=cY/(K log Y),
```

we have `KT=cY/log Y`. Under the same full local Hardy--Littlewood hierarchy as `PL-085`, the depth-`K` block consequently has the Poisson-sinc weak bulk law described in `PL-088`; the rank estimate transfers that law unchanged to the entire tail.

At horizons where the depth-`K` block is over-resolved and becomes asymptotically diagonal, the tail has the same deterministic weak limit. At arbitrary horizons, the conclusion is still exact at the level of subsequential weak ESD limits: whatever the minimum-depth block does, the entire fixed tail does the same in ordinary bulk.

## Prior-art and novelty audit

The mathematical ingredients are classical and no novelty is claimed for them individually:

- the prime number theorem gives the cardinality hierarchy of fixed prime-power layers;
- finite-rank/rank-`o(N)` perturbations preserve empirical spectral distributions in the standard random-matrix sense;
- `PL-087` already uses this rank mechanism for the split between primes and all higher powers;
- `PL-088` already identifies one fixed depth with a time-dilated prime Gram.

A targeted literature search across prime-power spectral matrices, logarithmic/Dirichlet Gram matrices, empirical spectral distributions, and rank perturbations did not expose a separate theorem whose mathematical content is this exact fixed-depth-tail reduction. That absence is not treated as evidence of novelty. The durable line-specific contribution is the **recursive closure of the cross-depth ordinary-bulk escape left open by `PL-087`--`PL-088`**: after conditioning away any fixed number of low depths, the same vanishing-rank obstruction reappears, and the surviving minimum depth is already a regraded prime process.

The result also has a strong generic-control interpretation. The rank conclusion does not use rational-prime logarithmic relations at all after the layer cardinalities are known. Any generalized-prime model with the same fixed-depth counting hierarchy has the same ordinary-bulk dominance. Thus the mechanism is structurally incapable of supplying rational-prime/RH rigidity by itself.

## Boundary conditions and falsification

The fixed-`K` hypothesis is essential. The exponent gap

```text
1/K-1/(K+1)=1/(K(K+1))
```

shrinks as `K` grows. The present proof gives no uniform conclusion when `K=K(X)` tends to infinity; that regime requires a separate count of how the number and sizes of adjacent depth layers compete.

Likewise, the normalization by total matrix dimension is essential. If deeper layers are amplified by inverse density, isolated before normalization, or used through a determinant/hard-edge observable, their vanishing population does not make them negligible. A counterexample to the present claim would therefore have to violate one of its explicit hypotheses: fixed minimum depth, ordinary dimension-normalized ESD, or Hermitian finite matrices on the stated prime-power tail. Within those hypotheses the rank bound is exact.

## Consequence for the research line

The finite-time prime-power Gram branch now has a recursive classification at ordinary bulk level:

```text
all depths k>=1
    -> depth 1 bulk (`PL-087`);

one fixed depth K
    -> time-dilated prime bulk (`PL-088`);

all depths k>=K, fixed K
    -> depth K bulk (this finding).
```

So merely retaining cross-depth couplings, or conditioning away the prime layer and repeating the same empirical-spectrum construction, cannot produce a new exponent-lattice phase. A surviving prime-power direction must intentionally target information that rank-`o(N)` perturbations can affect: hard edges, determinants, extreme eigenvalues, inverse-density renormalizations, growing-depth filtrations, or a completed/target-relative observable. Those possibilities remain open and require their own arithmetic and prior-art audits.