# PL-082 — Bounded prime clusters force two-sided sharp-Gram spectral instability

## Claim

The bounded-gap obstruction in `PL-081` strengthens from a two-prime lower-edge effect to an **arbitrarily large coherent-cluster obstruction at both spectral edges**.

Fix a macroscopic prime band

```text
0<a<b<infinity,
P_X={p prime : aX<p<=bX},
```

and the sharp finite-time Gram matrix

```text
G_(X,T)(p,q)
 =(1/T) integral_0^T exp(i t(log p-log q)) dt,
p,q in P_X.
```

Assume only

```text
T(X)=o(X).
```

Then there is a sequence `X_r->infinity`, with the cluster size `r->infinity`, such that

```text
boxed:
lambda_min(G_(X_r,T(X_r))) -> 0,

lambda_max(G_(X_r,T(X_r))) -> infinity.
```

More precisely, the matrices contain `r x r` principal blocks whose eigenvalues are

```text
r+o(1), o(1), ..., o(1).
```

Thus every sublinear horizon admits arbitrarily large nearly rank-one prime clusters. In particular, no unweighted prime-basis sharp-Gram family at `T=o(X)` can have uniform operator-norm bounds, a uniform lower frame bound, a uniform Riesz condition number, or an extreme-eigenvalue phase that is protected from classical prime-cluster geometry.

Combined with `PL-081`, this gives a stronger separation in the regime

```text
X/log X << T(X) << X:
```

```text
empirical spectral measure -> delta_1,

but along a subsequence
lambda_min -> 0
and
lambda_max -> infinity.
```

So a vanishing spectral fraction can carry unbounded two-sided pathology while the bulk becomes asymptotically orthonormal.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT`, with a `DECISIVE-NEGATIVE` conclusion for the route

```text
unweighted prime basis directions
+ sharp finite-time Gram
+ any sublinear horizon T=o(X)
    -> uniform frame/Riesz stability
       or RH-sensitive extreme-eigenvalue rigidity.
```

The theorem concerns only the unweighted prime-support Gram. It does not determine the bulk law at `T~X/log X`, weighted von-Mangoldt observables, target-relative/Nyman quantities, or any object that includes analytic continuation.

## Maynard supplies arbitrarily large bounded-diameter prime clusters

Maynard proved that for every fixed integer `m>=1`,

```text
liminf_n (p_(n+m)-p_n) < infinity.
```

Equivalently, for every fixed cluster size `r=m+1`, there is a finite constant `B_r` and infinitely many blocks of `r` consecutive primes

```text
p_n < p_(n+1) < ... < p_(n+r-1)
```

with

```text
p_(n+r-1)-p_n <= B_r.
```

The constant may grow very rapidly with `r`; no uniform control in `r` is needed below. The key point is that, after fixing `r`, such a bounded-diameter cluster occurs infinitely often and hence arbitrarily far out.

Choose once and for all

```text
x_0 in (a,b).
```

For each `r`, because `T(X)/X ->0`, choose one of Maynard's `r`-prime clusters sufficiently far out that, with

```text
X_r=p_n/x_0,
```

we have

```text
epsilon_r
 := B_r T(X_r)/X_r
 <= r^(-2).
```

Since `B_r/X_r->0` for this choice, every prime in the cluster satisfies

```text
p_(n+j)/X_r = x_0 + o(1),
```

so the whole cluster lies in `P_(X_r)` for sufficiently large `r`.

This diagonal choice is legitimate despite the growth of `B_r`: for each fixed `r`, Maynard supplies infinitely many admissible occurrences, while the condition `T(X)/X->0` eventually beats the fixed number `B_r r^2`.

## The cluster block converges to the all-ones matrix

As in `PL-081`, centering the time interval changes the Gram only by diagonal unitary conjugacy. The centered kernel is

```text
A_(X,T)(p,q)
 = sinc((T/2) log(p/q)),

sinc(u)=sin(u)/u.
```

For two primes `p,q` in the selected cluster, both are asymptotic to `x_0 X_r` and

```text
|p-q| <= B_r.
```

Hence

```text
|(T(X_r)/2) log(p/q)|
 <<_(a,b) B_r T(X_r)/X_r
 = O(epsilon_r).
```

Using

```text
sinc(u)=1+O(u^2)
```

uniformly near zero, the `r x r` principal cluster block `A_r` satisfies

```text
A_r = J_r + E_r,
```

where `J_r` is the all-ones matrix and

```text
max_(i,j) |(E_r)_(i,j)|
 << epsilon_r^2.
```

Therefore

```text
||E_r||_op
 <= r max_(i,j)|(E_r)_(i,j)|
 << r epsilon_r^2
 <= r^(-3)
 ->0.
```

The spectrum of `J_r` is

```text
r, 0, ..., 0.
```

Weyl's inequality now gives

```text
lambda_max(A_r)=r+o(1),

lambda_j(A_r)=o(1)
for j=2,...,r.
```

Because `A_r` is itself a Gram matrix it is positive semidefinite, so in particular

```text
lambda_min(A_r)->0.
```

Finally, `A_r` is a principal submatrix of the full centered Gram. Cauchy interlacing yields

```text
lambda_max(G_(X_r,T(X_r)))
 >= lambda_max(A_r)
 = r+o(1),
```

and

```text
lambda_min(G_(X_r,T(X_r)))
 <= lambda_min(A_r)
 ->0.
```

This proves the two-sided instability.

## Why the effect is stronger than the bounded-pair obstruction

A single bounded prime gap only gives a nearly singular `2 x 2` principal block, hence a collapsing lower edge. Maynard's full theorem gives bounded-diameter clusters of **every fixed cardinality**. Diagonalizing the cluster size against its occurrence height turns those fixed-cardinality theorems into a growing coherent block.

The upper edge therefore also escapes:

```text
||G_(X_r,T(X_r))||_op
 = lambda_max(G_(X_r,T(X_r)))
 -> infinity.
```

Consequently

```text
||G_(X_r,T(X_r))-I||_op -> infinity
```

along the same subsequence. This is substantially stronger than the statement in `PL-081` that operator-norm convergence to the identity can fail.

At horizons satisfying

```text
X/log X << T(X) << X,
```

`PL-081` independently proves

```text
(1/|P_X|)||G_(X,T)-I||_F^2 ->0.
```

There is no contradiction: the coherent cluster occupies only `r=o(|P_(X_r)|)` directions after choosing each occurrence sufficiently far out. Normalized Hilbert--Schmidt mass and empirical spectral measure may therefore ignore the same rare cluster that destroys both extreme spectral bounds.

This also warns against determinant or condition-number experiments. Rare clusters are spectrally negligible in proportion but can dominate the smallest eigenvalue, the largest eigenvalue, and products of eigenvalues.

## Prior art and novelty audit

The arithmetic input is classical and is not claimed as new:

- **James Maynard**, “Small gaps between primes,” *Annals of Mathematics* **181**(1) (2015), 383--413, DOI `10.4007/annals.2015.181.1.7`, proves in particular `liminf_n(p_(n+m)-p_n)<infinity` for every integer `m`. `PL-081` already cites this paper, but only used the `m=1` consequence.
- Classical nonharmonic Fourier/frame theory already treats frequency separation and local density as fundamental obstructions to uniform Riesz/frame bounds. `PL-072`--`PL-080` audit the relevant Ingham/Landau/prolate sampling background for the surrounding sharp-Gram program.

A targeted search for prime-supported sinc/finite-time Gram formulations did not locate a source stating the exact growing-cluster consequence above. The line-specific contribution is therefore an **exact derived synthesis**: Maynard's all-`m` bounded-cluster theorem plus the sharp logarithmic sinc kernel and principal-submatrix interlacing.

That synthesis is not evidence for a new RH mechanism. Its role is negative: the extreme spectrum is even less rigid than the pair-gap argument suggested, and its pathology already follows from unconditional local prime geometry without using zeta zeros, Euler-product continuation, or the functional equation.

## Adversarial boundaries

1. **The cluster diameter is not uniform in `r`.** The proof never assumes it is. It first fixes `r`, takes the corresponding finite `B_r`, and then chooses the cluster occurrence far enough out that `B_r T(X)/X` is tiny.
2. **No rate in `X` is claimed.** The construction is subsequential and may require extremely large occurrence heights as `r` grows.
3. **The result is about spectral extremes, not the empirical law.** It does not settle the exact `T~X/log X` bulk distribution.
4. **The result is support-only.** Arithmetic weights can suppress or amplify cluster directions and require a separate analysis.
5. **No analytic continuation enters.** The theorem cannot by itself distinguish `Re(s)=1/2`; it is a local-frequency obstruction generated by prime clustering.
6. **The statement does not distinguish rational primes from every sparse control.** Any frequency set containing arbitrarily large bounded-diameter clusters at sufficiently high energies would create the same Gram pathology. Rational-prime specificity here is exactly Maynard's theorem, not the ambient exponent lattice.
7. **A rescaled or regularized operator is a different object.** Dividing by local cluster size, imposing weights, deleting dense clusters, or replacing extreme eigenvalues by a robust bulk statistic can evade this theorem, but then the added normalization must itself be justified arithmetically and tested against the line's generic sparse controls.

## Consequence for the prime-lattice search

The unweighted sharp-Gram branch now has three sharply separated behaviors:

```text
full integer positive cone, T~X
    -> classical prolate/Nyquist bulk (PL-078--PL-080);

prime basis directions,
X/log X << T <= X
    -> bulk delta_1 when X/T=o(log X) (PL-081);

prime basis directions,
any T=o(X)
    -> arbitrarily large coherent prime clusters
       force lambda_min ->0 and lambda_max ->infinity
       along subsequences (this finding).
```

Hence neither the bulk nor the raw extremes of the unweighted prime-support Gram supply the missing RH rigidity: the bulk is sparse-sampling controlled above the mean-gap scale, while the extremes are dominated by unconditional bounded-cluster geometry throughout every sublinear horizon.

A surviving finite-horizon route must add a distinguished arithmetic weight or target, an explicit-formula coupling, or another zero-sensitive structure whose effect cannot be reproduced by local prime clustering or generic sparse controls.