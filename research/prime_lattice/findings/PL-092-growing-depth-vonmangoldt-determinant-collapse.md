# PL-092 — Growing-depth von Mangoldt Gram determinants collapse before frequency geometry can help

## Claim

The determinant escape left outside `PL-091` is already closed at the ordinary per-site volume scale by the same natural von Mangoldt half-weight.

Fix

```text
0<a<b<infinity,
L=log X,
Q_(X,>=K)={n=p^k : k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)|,
```

and assume `N_X>0`. For `T>0` let

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt
```

and let `A_(X,T)` be the naturally normalized von-Mangoldt half-weighted Gram matrix from `PL-091`,

```text
A_(X,T)(m,n)
 = X/(log X)^2
   * Lambda(m)Lambda(n)/sqrt(mn)
   * G_(X,T)(m,n).
```

If `K=K(X)->infinity`, then uniformly in the observation horizon `T>0`,

```text
boxed:
(det A_(X,T))^(1/N_X)
 <= C_(a,b)/K^2,
```

and therefore

```text
boxed:
(1/N_X) log det A_(X,T)
 <= -2 log K + O_(a,b)(1)
 -> -infinity.
```

More generally, for every positive scalar amplification `c_X`,

```text
(det(c_X A_(X,T)))^(1/N_X)
 <= C_(a,b) c_X/K^2.
```

Hence every amplification

```text
c_X=o(K^2)
```

still has vanishing determinant root and per-site logarithmic determinant tending to `-infinity`. The first scalar normalization that can even avoid this elementary volume collapse is again `K^2`, exactly the same threshold forced by the trace in `PL-091`.

At that threshold the natural von-Mangoldt depth factor disappears from the determinant at leading per-site scale throughout the growing-depth regimes controlled in `PL-090`. Put

```text
E_X(n)=sqrt(X/n),
B_(X,T)=E_X G_(X,T) E_X,

R_X(p^k)
 =(K/k) * (log(p^k)/log X).
```

Then there is the exact factorization

```text
boxed:
K^2 A_(X,T)=R_X B_(X,T) R_X.
```

If either

```text
K=o(sqrt(log X))
```

or

```text
K/sqrt(log X)->alpha in (0,infinity),
```

then the depth-population estimates of `PL-090` imply

```text
boxed:
(1/N_X)
 log( det(K^2 A_(X,T)) / det B_(X,T) )
 ->0,
```

uniformly in `T>0`.

Thus the natural von-Mangoldt half-weight cannot create a nontrivial ordinary determinant phase on a growing-depth prime-power tail. Before the `K^2` repair the geometric mean eigenvalue is forced to zero by the diagonal amplitude alone; at the first possible repair, the specifically depth-sensitive factor is asymptotically removed and the per-site determinant problem reduces to the deterministic shell envelope `X/n` times the unweighted logarithmic Gram geometry.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
growing prime-power depth
+ natural Lambda(n)n^(-1/2) amplitude
+ arbitrary finite-time logarithmic Gram
+ ordinary determinant root / per-site log determinant
    -> nontrivial RH-sensitive invariant.
```

This does not classify the determinant of the `K^2`-rescaled envelope Gram `B`, a finer hard-edge normalization, extreme eigenvalues, inverse statistics, or regularized determinants such as `det(I+zA)`. Those remain different observables.

## Exact diagonal factorization

For `n=p^k`,

```text
Lambda(n)=log p=(1/k)log n.
```

Define

```text
d_n
 =sqrt(X)/log X * Lambda(n)/sqrt(n).
```

Then exactly

```text
A_(X,T)=D_X G_(X,T) D_X,
D_X=diag(d_n),
```

with

```text
d_n^2
 =X/n * (log n/log X)^2 * 1/k^2.
```

On the fixed multiplicative shell `aX<n<=bX`,

```text
X/n<=1/a,
log n/log X=1+O_(a,b)(1/log X),
```

so for all sufficiently large `X`,

```text
d_n^2<=C_(a,b)/k^2<=C_(a,b)/K^2.
```

The point is stronger than the trace estimate alone: the whole determinant separates exactly into a frequency-volume factor and a diagonal arithmetic-amplitude factor,

```text
boxed:
det A_(X,T)
 =det G_(X,T) * product_(n in Q_(X,>=K)) d_n^2.
```

No prime-number theorem or zero information enters this identity.

## The finite-time Gram is positive definite and has determinant at most one

For coefficients `c_n`,

```text
c^* G_(X,T)c
 =(1/T) integral_0^T
   |sum_n c_n exp(i t log n)|^2 dt.
```

The frequencies `log n` are distinct. If this quadratic form vanished, the finite exponential polynomial would vanish almost everywhere on an interval, hence identically there by continuity and then identically as an analytic exponential polynomial. Linear independence of distinct exponentials forces every `c_n=0`. Therefore

```text
G_(X,T)>0
```

for every `T>0`, and so `A_(X,T)>0` as well.

Moreover

```text
G_(X,T)(n,n)=1.
```

Classical Hadamard determinant inequality for a positive-definite matrix therefore gives

```text
0<det G_(X,T)<=1.
```

Combining this with the diagonal factorization yields

```text
det A_(X,T)
 <= product_n C_(a,b)/K^2
 =(C_(a,b)/K^2)^(N_X),
```

which proves the determinant-root bound uniformly in `T`.

There is an independent consistency check from `PL-091`. If `lambda_j(A)>0` are the eigenvalues, arithmetic-geometric mean gives

```text
(det A)^(1/N_X)
 <=(1/N_X) sum_j lambda_j(A)
 =(1/N_X)Tr A
 <=C_(a,b)/K^2.
```

Thus the determinant conclusion is not relying on a delicate estimate of off-diagonal Gram entries: both the exact diagonal-volume factorization and the trace route force the same threshold.

## Every sub-`K^2` scalar repair still collapses

For `c_X>0`,

```text
det(c_X A)=c_X^(N_X) det A.
```

Hence

```text
(det(c_X A))^(1/N_X)
 =c_X(det A)^(1/N_X)
 <=C_(a,b)c_X/K^2.
```

If `c_X=o(K^2)`, the geometric mean eigenvalue tends to zero. Equivalently,

```text
(1/N_X)log det(c_X A)
 <=log C_(a,b)+log c_X-2log K
 ->-infinity.
```

This closes the most direct determinant repair below the amplitude scale identified in `PL-091`. It does not say that `c_X~K^2` is sufficient for a nondegenerate determinant; it says only that anything asymptotically smaller is impossible before the frequency geometry is even examined.

## At the first possible repair, the depth weight becomes determinant-negligible

Write `n=p^k` and define the deterministic shell envelope

```text
E_X(n)=sqrt(X/n).
```

Then

```text
B_(X,T)=E_X G_(X,T) E_X
```

is the unweighted logarithmic Gram with only the macroscopic shell grading retained. From the exact formula for `d_n`,

```text
K d_n
 =E_X(n)
   * (K/k)
   * (log n/log X).
```

Therefore, with

```text
R_X(n)
 =(K/k)(log n/log X),
```

one has exactly

```text
K^2 A_(X,T)=R_X B_(X,T)R_X.
```

Since all matrices are positive definite,

```text
boxed:
1/N_X log( det(K^2 A_(X,T))/det B_(X,T) )
 =2/N_X sum_(n=p^k in Q_(X,>=K))
   [log(K/k)+log(log n/log X)].
```

The second average tends to zero uniformly without any counting theorem, because on `aX<n<=bX`,

```text
log(log n/log X)=O_(a,b)(1/log X).
```

For the first average, the population analysis in `PL-090` is decisive. In the regime

```text
K=o(sqrt(log X)),
```

the minimum depth carries asymptotically all indices, while the proof of `PL-090` gives exponentially small bounds for the deeper tail. In the critical regime

```text
K/sqrt(log X)->alpha>0,
```

the depth offset `r=k-K` has a geometric limiting profile, with a uniform exponential majorant for `0<=r<=K`, while the sector `k>=2K` has mass bounded by

```text
O(L^2 exp(-L/(2K)))
```

relative to the minimum layer. Consequently

```text
1/N_X sum_n log(k/K)->0.
```

Indeed, on `k<=2K`, use `log(k/K)<= (k-K)/K` and the exponentially summable offset bound; on `k>=2K`, the logarithmic factor is at most `O(log L)` while the displayed far-tail bound is exponentially smaller. Hence

```text
1/N_X sum_n log(K/k)->0.
```

Substitution into the exact determinant ratio proves

```text
1/N_X
log( det(K^2A_(X,T))/det B_(X,T) )
 ->0.
```

The statement is uniform in `T` because the ratio contains no `T` at all.

This is the growing-depth analogue of the prime-only reduction in `PL-086`: once the natural amplitude is normalized at its first nonvanishing scale, the specifically von-Mangoldt factor no longer supplies an independent leading determinant channel.

## Relation to the earlier Gram determinant branch

`PL-080` already shows that the unweighted sharp integer-band determinant has a classical Nyquist/Ingham phase and is reproduced by a nonmultiplicative shifted control. The present result is different: it does not analyze frequency density or a determinant phase of the prime-power support. It proves that the **natural growing-depth arithmetic amplitude cannot rescue the determinant before such frequency geometry is studied**.

The logical reduction is

```text
natural weighted prime-power determinant

    c_X=o(K^2)
        -> forced volume collapse from amplitudes;

    c_X=K^2
        -> depth-sensitive von-Mangoldt factor disappears
           at per-site determinant scale in the PL-090 regimes;
        -> residual problem is the envelope-weighted
           unweighted cross-depth Gram determinant.
```

Accordingly, any surviving determinant mechanism must come from the frequency/support geometry of the rescaled cross-depth Gram, from a finer normalization than the ordinary determinant root, or from an observable that retains distinguished target/zero information. It cannot be attributed to the raw `Lambda(p^k)=log p` depth weight itself.

## Prior art and novelty audit

The determinant ingredients are classical.

- Hadamard's determinant inequality gives `det G<=product G_(nn)=1` for a positive-definite Gram matrix with unit diagonal.
- Arithmetic-geometric mean of the positive eigenvalues gives `(det A)^(1/N)<=Tr(A)/N`.
- Determinants under diagonal congruence satisfy `det(DGD)=det(D)^2det(G)`.

No novelty is claimed for any of those matrix facts. A targeted literature search around von-Mangoldt-weighted finite-time Gram determinants, prime-power Gram determinants, and Dirichlet-polynomial Gram determinants did not identify a specialized theorem whose content is the growing-depth reduction above. That absence is not used as a novelty claim.

The durable line-specific content is the collision of these classical determinant facts with the exact prime-power depth identity

```text
Lambda(p^k)/log(p^k)=1/k
```

and the `PL-090` growing-depth population law. It closes an observable explicitly left outside `PL-091` and shows that the same `K^2` amplitude threshold governs both arithmetic mean spectral mass and geometric mean spectral volume.

The result also fails the line's strongest arithmetic-discrimination test in the expected direction. The determinant-root upper bound uses only unit-diagonal Gram geometry and the depth-amplitude bound; any matched generalized-prime model with the same depth weighting obeys it. The `K^2` determinant reduction uses only the depth-population estimates already identified in `PL-090` as PNT-level rather than RH-level structure.

## Adversarial boundaries

1. **This is an upper-volume no-go, not a determinant asymptotic.** It gives no lower bound on `det A` and does not identify the decay rate beyond the forced `K^-2` geometric-mean factor.
2. **`K^2` is necessary, not sufficient.** The envelope Gram `B_(X,T)` may itself have a vanishing determinant root because of frequency crowding, hard-edge behavior, or cross-depth near-dependence. No nondegenerate limit for `det(K^2A)` is claimed.
3. **The determinant-equivalence after `K^2` uses the `PL-090` population regimes.** The raw upper bound is valid for every nonempty growing-depth tail, but the per-site reduction to `B` is asserted only for `K=o(sqrt(log X))` or `K/sqrt(log X)->alpha in (0,infinity)`, where the required depth-tail control is already proved.
4. **Ordinary determinant root is the observable being closed.** Finer scales such as `N^-2 log det`, hard-edge large deviations, individual extreme eigenvalues, inverse moments, condition numbers, or pseudospectral quantities can behave differently.
5. **Regularized and pointed determinants are outside the claim.** Objects such as `det(I+zA)`, perturbation determinants, target-relative Schur complements, or Fredholm determinants after an additional completion are not bounded by this statement in the same way.
6. **The low-depth/full von-Mangoldt sequence is not covered.** The mechanism requires the minimum prime-power exponent `K` to tend to infinity. Fixed depths remain governed by `PL-086`--`PL-089` and can carry order-one amplitude.
7. **No analytic continuation or zero divisor occurs.** Every identity is finite-dimensional and valid directly from the prime-power coefficients. The result neither transports the Euler product into the critical strip nor singles out `Re(s)=1/2`.
8. **The square-root depth transition remains noncritical for RH.** At `K~alpha sqrt(log X)`, the geometric population law of `PL-090` is still PNT-level. The present determinant reduction removes rather than enhances the natural von-Mangoldt depth grading at the first scalar normalization capable of surviving.

## Consequence for the growing-depth branch

`PL-090` and `PL-091` left open the possibility that the critical adjacent-depth stack might be invisible to ordinary empirical spectral mass yet survive in a multiplicative spectral observable. At the ordinary determinant-root scale, that possibility is now eliminated for the canonical von-Mangoldt half-weight.

The remaining growing-depth finite-time Gram targets are therefore narrower:

```text
unweighted/envelope cross-depth Gram geometry at K~sqrt(log X),
    especially hard-edge or extreme statistics;

finer determinant normalizations after the forced K^2 repair;

target-relative observables that do not average away
    a vanishing spectral sector;

or a genuinely global/completed construction that imports
    analytic-continuation information without merely rewriting
    the explicit formula.
```

The natural arithmetic half-weight by itself supplies no ordinary determinant-volume escape from the collapse already seen at trace level.