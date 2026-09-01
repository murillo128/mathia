# PL-091 — Natural von-Mangoldt weighting collapses every growing-depth Gram bulk

## Claim

`PL-090` identifies the first population scale at which a prime-power tail with minimum depth `K=K(X)` is no longer rank-dominated by one exponent layer: when `K~alpha sqrt(log X)`, adjacent depths carry a geometric fraction of the matrix dimension. For the **naturally von-Mangoldt half-weighted finite-time Gram** used in `PL-086`--`PL-090`, that population transition nevertheless cannot produce a nontrivial ordinary empirical spectral law. A simpler positive-trace obstruction dominates it.

Fix

```text
0<a<b<infinity,
K=K(X)->infinity,
Q_(X,>=K)={n=p^k : p prime, k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)|,
```

and consider any sequence of `X` for which `N_X>0`. For arbitrary observation time `T=T(X)>0`, define

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt
```

and

```text
A_(X,T)(m,n)
 = X/(log X)^2
   * Lambda(m)Lambda(n)/sqrt(mn)
   * G_(X,T)(m,n),
       m,n in Q_(X,>=K).
```

Then `A_(X,T)` is positive semidefinite and, uniformly in the observation time,

```text
boxed:
(1/N_X) Tr A_(X,T)
 <= C_(a,b)/K(X)^2.
```

Consequently, if `mu_(X,T)` is its dimension-normalized empirical eigenvalue measure,

```text
boxed:
W_1(mu_(X,T),delta_0)
 =(1/N_X) Tr A_(X,T)
 =O_(a,b)(K^(-2))
 ->0,
```

again uniformly in `T`. In particular

```text
boxed:
mu_(X,T) => delta_0
```

for **every** growing minimum depth `K(X)->infinity`, including the critical population regime

```text
K~alpha sqrt(log X)
```

of `PL-090`.

The same proof shows that any scalar amplification `c_X A_(X,T)` with

```text
c_X=o(K^2)
```

still converges to `delta_0` in `W_1`. Thus an ordinary-bulk growing-depth construction using the inherited von-Mangoldt half-weight must amplify by at least the `K^2` scale before a nonzero first spectral moment is even possible.

At the `PL-090` critical depth scale that minimal amplification has a second consequence. If `k=K+r` with fixed offset `r`, then

```text
K^2/k^2 ->1.
```

Since `PL-090` proves that the depth offset has an asymptotically geometric, hence tight, distribution, the same convergence holds for all but an asymptotically negligible fraction of tail indices. Therefore the minimal `K^2` repair needed to prevent trace collapse simultaneously **erases the surviving `1/k^2` von-Mangoldt depth grading in ordinary population mass**. Any nontrivial rescaled critical-depth bulk would have to come from cross-depth frequency geometry, shell geometry, a different arithmetic coupling, or a more singular observable—not from the natural exponent-depth amplitude itself.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
growing minimum depth K(X)->infinity
+ natural Lambda(n)n^(-1/2) half-weight
+ arbitrary finite-time logarithmic Gram
+ ordinary dimension-normalized empirical spectrum
    -> a nontrivial growing-depth/cross-depth spectral phase.
```

This is not an RH-sensitive mechanism and uses no analytic continuation, prime number theorem, Hardy--Littlewood input, or zero information. It is a structural obstruction forced by positivity plus the elementary identity `Lambda(p^k)=log p`.

## Positivity is exact and independent of arithmetic distribution

For each `n` in the finite index set, put

```text
u_n(t)=exp(i t log n)
```

in `L^2([0,T],dt/T)`. Then

```text
G_(X,T)(m,n)=<u_n,u_m>
```

up to the harmless inner-product convention, so `G_(X,T)` is a Gram matrix and is positive semidefinite.

Let

```text
d_X(n)=sqrt(X)/log X * Lambda(n)/sqrt(n).
```

On prime powers `Lambda(n)>0`, and

```text
A_(X,T)=D_X G_(X,T) D_X,
```

where `D_X=diag(d_X(n))`. Hence

```text
A_(X,T)>=0
```

for every `X`, every nonempty tail, every choice of minimum depth, and every `T>0`.

No spacing estimate for the frequencies `log n` enters. In particular, close prime-power frequencies and arbitrarily large off-diagonal coherence can redistribute the eigenvalues but cannot evade the trace bound below, because all eigenvalues remain nonnegative and their total sum is fixed by the diagonal.

## The diagonal carries a uniform `1/k^2` bound

For `n=p^k`, the diagonal Gram entry is `G_(X,T)(n,n)=1`, and therefore

```text
A_(X,T)(n,n)
 = X/n * (Lambda(n)/log X)^2
 = X/n * (log p/log X)^2.
```

Using `log n=k log p`, this is exactly

```text
boxed:
A_(X,T)(p^k,p^k)
 = X/p^k
   * (1/k^2)
   * (log(p^k)/log X)^2.
```

On the fixed multiplicative shell `aX<n<=bX`,

```text
X/n <=1/a,
```

and

```text
log n/log X
 =1+O_(a,b)(1/log X)
```

uniformly. Thus for all sufficiently large `X`,

```text
0<=A_(X,T)(p^k,p^k)
 <=C_(a,b)/k^2
 <=C_(a,b)/K^2.
```

Summing over the `N_X` tail indices gives

```text
Tr A_(X,T)
 <=C_(a,b) N_X/K^2.
```

This estimate does not use how many points lie at each depth. It therefore continues through precisely the `K~sqrt(log X)` population transition where the rank argument of `PL-089` stops working.

## Trace collapse forces empirical spectral collapse

Write the eigenvalues of `A_(X,T)` as

```text
lambda_1,...,lambda_(N_X)>=0
```

and its empirical measure as

```text
mu_(X,T)
 =(1/N_X) sum_j delta_(lambda_j).
```

Because the spectrum is nonnegative,

```text
W_1(mu_(X,T),delta_0)
 = integral lambda d mu_(X,T)(lambda)
 = (1/N_X) sum_j lambda_j
 = (1/N_X) Tr A_(X,T).
```

Therefore

```text
W_1(mu_(X,T),delta_0)
 <=C_(a,b)/K^2 ->0.
```

Equivalently, for each fixed `epsilon>0`,

```text
mu_(X,T)([epsilon,infinity))
 <= C_(a,b)/(epsilon K^2)
 ->0.
```

The conclusion is uniform in `T`, so retuning the finite-time observation horizon cannot rescue the ordinary bulk. It also allows a small set of very large eigenvalues: trace collapse only says that their total dimension-normalized positive mass tends to zero. Determinants, hard edges, extreme eigenvalues, or inverse-density observables remain outside the claim.

## The first possible scalar repair is at least `K^2`

For any deterministic scalar `c_X>=0`, positivity gives

```text
W_1(mu_(c_X A),delta_0)
 = c_X (1/N_X) Tr A
 <= C_(a,b) c_X/K^2.
```

Hence

```text
c_X=o(K^2)
```

is still too small to produce any nonzero ordinary empirical first moment.

This does **not** prove that `c_X~K^2` produces a nontrivial limit. It only identifies the first amplification scale not killed by the trace argument. That distinction matters because arbitrary rescaling can manufacture an order-one diagonal without creating arithmetic rigidity.

Moreover, the `K^2` scale is antagonistic to using the von-Mangoldt depth factor as the sought information carrier. On depth `k=K+r`, the rescaled diagonal factor contributed specifically by exponent depth is

```text
K^2/k^2
 =(K/(K+r))^2.
```

For each fixed `r`, this tends to `1`. In the critical regime of `PL-090`, with

```text
K/sqrt(log X)->alpha>0,
q_alpha=exp(-1/alpha^2),
```

that finding gives

```text
P_X(r=j) ->(1-q_alpha)q_alpha^j.
```

The limiting geometric law is tight. Given `eta>0`, choose fixed `R` so that `q_alpha^(R+1)<eta`; all but asymptotic mass at most `eta` lies in `0<=r<=R`, where

```text
sup_(0<=r<=R)
 |(K/(K+r))^2-1| ->0.
```

Thus, in empirical depth population,

```text
boxed:
K^2/k^2 ->1.
```

So the natural critical rescaling that merely compensates for amplitude decay does not preserve a nontrivial depth profile. The geometric **population** law of `PL-090` survives, but the inherited von-Mangoldt amplitude becomes asymptotically depth-blind across that population.

## Relation to `PL-087`--`PL-090`

The obstruction completes a clean hierarchy.

`PL-087` shows that on the full prime-power axis the higher powers occupy vanishing rank, so they cannot change the ordinary prime-dominated bulk even though `Lambda(p^k)/log(p^k)=1/k` survives pointwise.

`PL-088` conditions on one fixed depth and proves that it is exactly a time-dilated prime-support Gram with deterministic `1/k^2` grading. Retuning time can recover the same local Poisson-sinc process already present on primes, but not a new depth spectral phase.

`PL-089` keeps all depths `k>=K` for fixed `K` and shows by rank that the minimum depth still carries asymptotically all dimensions.

`PL-090` finds the sharp first failure of that rank argument: at `K~alpha sqrt(log X)` adjacent depths have geometric positive population, so a finite cross-depth stack can affect ordinary ESD in principle.

The present result says that **for the specific natural von-Mangoldt weighted Gram motivating that branch, the newly available population is too weakly weighted to survive ordinary normalization at all once `K->infinity`**. The rank obstruction ends, but positivity plus trace immediately replaces it.

Thus the `sqrt(log X)` transition remains a genuine statement about exponent-layer population, but it is not a natural-weight spectral transition.

## Prior-art and novelty audit

Every ingredient of the proof is classical or elementary:

- `Lambda(p^k)=log p` is the defining prime-power value of the von-Mangoldt function;
- a finite-time exponential correlation matrix is a Gram matrix and hence positive semidefinite;
- the trace of a positive semidefinite matrix is the sum of its nonnegative eigenvalues;
- a vanishing normalized first moment forces its empirical measure to converge to `delta_0` on the nonnegative half-line.

The closest internal antecedents are `PL-086`--`PL-090`: they already isolate the von-Mangoldt `1/k` amplitude, its `1/k^2` diagonal grading, fixed-depth time dilation, rank collapse of fixed tails, and the `sqrt(log X)` population transition. The new point is the exact combination of these already-audited facts with positivity, which closes the **growing-depth natural-weight ordinary-bulk** escape left explicitly open by `PL-090`.

A targeted external search across combinations of prime powers, von-Mangoldt weights, finite-time/logarithmic Gram matrices, and empirical spectral distributions did not locate a source asserting this matrix-level growing-depth trace collapse. The search did recover only the standard prime-power definition of `Lambda`, generic Dirichlet-polynomial literature, and unrelated Gram/spectral uses. That absence is not treated as evidence of novelty, and no novelty is claimed for the ingredients or for the generic positive-trace lemma. The finding is stored as a line-specific obstruction/routing result.

The strongest falsification control is immediate: the argument does not distinguish the rational primes. Any generalized-prime or arbitrary-frequency model carrying points with the same depth label and the same `1/k` half-weight obeys the same PSD trace bound. Therefore the collapse is universal background geometry, not arithmetic rigidity.

## Adversarial boundaries

1. **Positivity is essential.** A signed or completed Weil form can have large positive and negative spectral contributions with small trace. The present argument does not apply to indefinite operators.
2. **The natural half-weight is essential.** An explicit depth-dependent amplification of order `K` at vector level, hence `K^2` at matrix level, can evade the first-moment collapse. Such an amplification must then justify its own canonicity and arithmetic discrimination.
3. **Only ordinary dimension-normalized bulk is closed.** A vanishing fraction of eigenvalues can remain large or small enough to affect operator norm, hard edges, determinants, spectral shifts, or other singular statistics.
4. **No claim is made about an unweighted Gram.** `PL-090` still leaves cross-depth ordinary bulk structurally open for matrices whose diagonal does not decay like `1/k^2`.
5. **No PNT or local-prime model is needed.** The theorem remains true before deciding whether adjacent depth blocks have Poisson, arithmetic, or other correlations. It cannot therefore be interpreted as evidence about those correlations.
6. **The `K^2` threshold is an amplitude threshold, not the Riemann critical line.** It comes from squaring the elementary `1/k` von-Mangoldt depth factor.
7. **Analytic continuation is absent.** No identity from `Re(s)>1` is transported into the critical strip, and no zeta zero enters the proof.

## Consequence for the research line

The natural finite-time prime-power Gram branch at ordinary-bulk level is now closed for **all** minimum-depth regimes:

```text
K fixed
    -> minimum-depth rank dominance (`PL-089`);

K->infinity, K=o(sqrt(log X))
    -> minimum-depth rank dominance (`PL-090`)
       and, more strongly for the natural weight,
       trace collapse to delta_0 (this finding);

K~alpha sqrt(log X)
    -> several depths have positive population (`PL-090`),
       but the natural weighted ESD still collapses to delta_0
       at rate O(K^(-2)) in W_1 (this finding);

arbitrary K(X)->infinity with a nonempty tail
    -> the same natural-weight trace collapse,
       without any prime-counting hypothesis.
```

Accordingly, continuing this branch by merely computing the finite cross-depth stack singled out by `PL-090` would be churn **unless the observable is changed**. A surviving direction must deliberately leave at least one hypothesis of the no-go: use a canonically justified `K^2`-scale or stronger renormalization and then prove genuinely arithmetic cross-depth structure; target hard-edge/determinant/extreme-eigenvalue information that ordinary trace does not control; or return to an indefinite completed/target-relative form where cancellation rather than positive mass is the relevant invariant.

Any such escape still has to pass the README controls against generalized-prime systems and generic frequency geometry before it can count as RH-relevant structure.