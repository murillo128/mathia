# PL-094 — Growing prime-power tails have a universal log-uniform shell envelope

## Claim

The residual shell envelope left after the `K^2` reduction of `PL-092`--`PL-093` is already universal at the one-point level throughout the first growing-depth range controlled by `PL-090`.

Fix

```text
0<a<b<infinity,
L=log X,
K=K(X)->infinity,
K=O(sqrt(L)),
Q_(X,>=K)={n=p^k : k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)|,
```

and put

```text
A=log a,
B=log b,
Delta=B-A=log(b/a),
y_X(n)=log(n/X).
```

Along every sequence for which `N_X>0`, the empirical shell coordinate is asymptotically uniform in logarithmic position:

```text
boxed:
(1/N_X) #{n in Q_(X,>=K) : y_X(n)<=u}
 -> (u-A)/Delta
```

uniformly for `u in [A,B]`.

Equivalently, for every continuous `f` on `[a,b]`,

```text
boxed:
(1/N_X) sum_(n in Q_(X,>=K)) f(n/X)
 -> (1/Delta) integral_a^b f(x) dx/x.
```

Thus the shell ratio `n/X` converges to the log-uniform law `dx/(Delta x)`, independently of whether the depth population is concentrated at `K` or has the geometric adjacent-depth profile of `PL-090`.

Now let

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt,

E_X(n)=sqrt(X/n),
B_(X,T)=E_X G_(X,T) E_X
```

be the unweighted envelope Gram from `PL-092`--`PL-093`. Then, uniformly in `T>0`,

```text
boxed:
(1/N_X) Tr B_(X,T)
 -> (1/Delta)(1/a-1/b).
```

Moreover, because `G_(X,T)` is positive definite for every finite nonempty index set and every `T>0`,

```text
det B_(X,T)
 =det G_(X,T) * product_(n in Q_(X,>=K)) X/n,
```

and therefore

```text
boxed:
(1/N_X)
[log det B_(X,T)-log det G_(X,T)]
 -> -1/2 log(ab),
```

again uniformly in `T`.

Under either of the two `PL-092`--`PL-093` depth hypotheses

```text
K=o(sqrt(log X))
```

or

```text
K/sqrt(log X)->alpha in (0,infinity),
```

the naturally von-Mangoldt half-weighted Gram `A_(X,T)` consequently satisfies

```text
boxed:
(1/N_X) Tr(K^2 A_(X,T))
 -> (1/Delta)(1/a-1/b),
```

and

```text
boxed:
(1/N_X)
[log det(K^2 A_(X,T))-log det G_(X,T)]
 -> -1/2 log(ab).
```

Hence the first `K^2` repair does not leave a hidden one-point arithmetic shell statistic. It removes the von-Mangoldt depth grading, while the remaining diagonal envelope converges to the elementary log-uniform law. Any residual non-universal information in this branch must therefore enter through the **off-diagonal logarithmic-frequency geometry of `G_(X,T)`**, a harder-edge/target-relative observable, or another coupling not determined by the one-point shell distribution.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-PNT + DECISIVE-NEGATIVE` for the route

```text
growing prime-power depth K=O(sqrt(log X))
+ natural K^2 repair
+ one-point shell/envelope statistics
+ ordinary trace or the shell contribution to per-site log determinant
    -> a rational-prime-specific or RH-sensitive invariant.
```

The log-uniform shell law itself is an elementary consequence of the quantitative prime number theorem already used in `PL-090`; no novelty is claimed for that distribution statement. The durable contribution here is the reduction it gives when combined with `PL-092`--`PL-093`: the depth transition and the diagonal shell envelope can both be removed from the list of possible information carriers at the first nonvanishing normalization.

## Uniform logarithmic shell law inside each relevant depth layer

For `u in [A,B]` and a fixed exponent `k`, define

```text
M_(k,u)(X)
 =#{p prime : aX<p^k<=exp(u)X}.
```

Equivalently,

```text
M_(k,u)(X)
 =pi(exp((L+u)/k))-pi(exp((L+A)/k)).
```

The quantitative PNT estimate used in `PL-090` is uniform for

```text
K<=k<=2K,
K=O(sqrt L).
```

Applying it at the two endpoints, or equivalently integrating the logarithmic integral, gives uniformly in both `k` and `u`,

```text
M_(k,u)(X)
 = integral_A^u exp((L+v)/k)/(L+v) dv
   +o(exp(L/k)/L).
```

Indeed the endpoint PNT error, divided by `exp(L/k)/L`, is bounded by

```text
O(L exp(-c sqrt(L/k)))=o(1),
```

because `L/k` is at least a constant multiple of `sqrt L` on this range. Since `A<=v<=B` is fixed while `k->infinity`,

```text
exp(v/k)=1+o(1),
L/(L+v)=1+o(1)
```

uniformly. Hence

```text
boxed:
M_(k,u)(X)
 =(u-A+o(1)) exp(L/k)/L
```

uniformly for `K<=k<=2K` and `u in [A,B]`.

Taking `u=B` recovers the layer count from `PL-090`,

```text
M_k(X)
 =(Delta+o(1)) exp(L/k)/L.
```

Therefore every relevant depth layer has the same limiting conditional shell law,

```text
M_(k,u)(X)/M_k(X)
 =(u-A)/Delta+o(1),
```

with an error uniform across the whole first depth block.

## Summing over depth does not change the law

Summing the preceding uniform asymptotic over `K<=k<=2K` gives

```text
sum_(k=K)^(2K) M_(k,u)(X)
 =[(u-A)/Delta+o(1)]
   sum_(k=K)^(2K) M_k(X).
```

The tail estimate proved in `PL-090` gives

```text
sum_(k>=2K) M_k(X)/M_K(X)
 <<L^2 exp(-L/(2K))
 ->0
```

whenever `K=O(sqrt L)`. Since the block `K<=k<=2K` contains the depth-`K` layer, the same tail is negligible relative to the whole population. Thus

```text
(1/N_X) #{n in Q_(X,>=K): y_X(n)<=u}
 =(u-A)/Delta+o(1)
```

uniformly in `u`.

This argument is deliberately stronger than choosing one of the two population regimes of `PL-090`. Below `sqrt L`, the minimum layer dominates; at `K~alpha sqrt L`, adjacent layers have a geometric population profile. But because **every** layer in the relevant block has the same conditional log-shell law, mixing the layers cannot change the one-point shell distribution.

The equivalent weak-limit formula follows by the change of variables `x=exp(y)`:

```text
(1/Delta) integral_A^B f(exp(y)) dy
 =(1/Delta) integral_a^b f(x) dx/x.
```

## The envelope diagonal is therefore universal

The diagonal of the envelope Gram is independent of the observation horizon:

```text
B_(X,T)(n,n)
 =E_X(n)^2 G_(X,T)(n,n)
 =X/n.
```

Apply the shell law to `f(x)=1/x`. This gives

```text
(1/N_X) Tr B_(X,T)
 =(1/N_X) sum_n X/n

 ->(1/Delta) integral_a^b dx/x^2
 =(1/Delta)(1/a-1/b).
```

More generally, every bounded continuous statistic of the diagonal envelope `X/n` converges to the pushforward of log-uniform measure. If `r=X/n`, its limiting density on `[1/b,1/a]` is

```text
dr/(Delta r).
```

Thus the diagonal shell factor carries no memory of the geometric depth population from `PL-090`.

## The shell contribution to the determinant is an elementary constant

For every `T>0`, `PL-092` proves that the distinct frequencies `log n` make the finite Gram matrix `G_(X,T)` positive definite. Hence both determinants below are positive and

```text
B_(X,T)=E_X G_(X,T) E_X
```

gives the exact identity

```text
det B_(X,T)
 =det G_(X,T) det(E_X)^2
 =det G_(X,T) product_n X/n.
```

Taking logarithms and dividing by dimension,

```text
(1/N_X)
[log det B_(X,T)-log det G_(X,T)]
 =(1/N_X) sum_n log(X/n).
```

The shell law with `f(x)=log x` yields

```text
(1/N_X) sum_n log(n/X)
 ->(1/Delta) integral_A^B y dy
 =(A+B)/2.
```

Therefore

```text
(1/N_X)
[log det B_(X,T)-log det G_(X,T)]
 ->-(A+B)/2
 =-1/2 log(ab).
```

The difference is exactly independent of `T`, so the convergence is uniform in the observation horizon even if `G_(X,T)` becomes highly coherent.

Finally, `PL-092` gives

```text
(1/N_X)
log(det(K^2 A_(X,T))/det B_(X,T))
 ->0
```

in its two growing-depth regimes, while `PL-093` gives normalized `S_1` equivalence between `K^2A` and `B`. The determinant and trace conclusions in the claim follow immediately.

## Prior-art and novelty audit

The prime-distribution input is classical. This finding uses no new zero-free region, short-interval theorem, or weighted prime theorem beyond the quantitative PNT already audited for `PL-090`. The log-uniform density `dx/x` is simply what the PNT becomes after the map

```text
p -> p^k/X
```

when `k->infinity`: the Jacobian and the `1/log p` prime density cancel the exponent scale to first order.

The nontrivial point for the current corpus is not that change of variables in isolation. It is that `PL-092`--`PL-093` had reduced the first nonvanishing natural von-Mangoldt normalization to an unweighted envelope Gram but deliberately left the envelope `B` unanalyzed. The calculation above shows that **all one-point information in that envelope is universal** and that its full multiplicative contribution to the ordinary per-site determinant is only the constant `-log(ab)/2`.

The same conclusion would hold for a Beurling/generalized-prime control possessing the corresponding uniform local PNT on the base-prime shells. It therefore fails the Prime-Lattice mandate's rational-prime discrimination test and cannot by itself be the sought global zeta mechanism.

## Boundaries and surviving question

This is not a classification of the residual Gram `G_(X,T)`. It does not control:

- off-diagonal correlations between `log(p^k)` and `log(q^ell)`;
- smallest eigenvalues, inverse moments, or condition numbers beyond what follows from the exact diagonal factorization;
- operator-norm outliers carried by a vanishing fraction of the spectrum;
- target-relative Schur complements or indefinite completed-Weil couplings;
- depths larger than the `K=O(sqrt(log X))` range where the uniform layer PNT used here has been established in the corpus.

Accordingly the surviving question after `PL-091`--`PL-094` is narrower: if the growing prime-power branch contains any rational-prime-specific information at its first natural normalization, it must be encoded in **cross-point frequency relations or a non-one-point arithmetic coupling**, not in depth population, von-Mangoldt amplitude, or the macroscopic shell envelope.
