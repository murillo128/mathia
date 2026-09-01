# PL-093 — The first `K^2` repair is trace-norm equivalent to the unweighted envelope Gram

## Claim

The `K^2` normalization identified in `PL-091` and `PL-092` does more than remove the von-Mangoldt depth factor from the trace and ordinary determinant at leading scale. In the growing-depth regimes controlled by `PL-090`, it removes that factor from **every ordinary Lipschitz spectral statistic**.

Fix

```text
0<a<b<infinity,
L=log X,
Q_(X,>=K)={n=p^k : k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)|,
```

with `K=K(X)->infinity` and `N_X>0`. For `T>0`, let

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt
```

and let `A_(X,T)` be the naturally normalized von-Mangoldt half-weighted Gram from `PL-091`--`PL-092`,

```text
A_(X,T)(m,n)
 =X/(log X)^2
  *Lambda(m)Lambda(n)/sqrt(mn)
  *G_(X,T)(m,n).
```

Define, as in `PL-092`,

```text
E_X(n)=sqrt(X/n),
B_(X,T)=E_X G_(X,T) E_X,
R_X(p^k)=(K/k)(log(p^k)/log X).
```

Then exactly

```text
K^2 A_(X,T)=R_X B_(X,T) R_X.
```

Assume either

```text
K=o(sqrt(log X))
```

or

```text
K/sqrt(log X)->alpha in (0,infinity).
```

Then, uniformly in the observation horizon `T>0`,

```text
boxed:
(1/N_X)
||K^2 A_(X,T)-B_(X,T)||_(S_1)
->0.
```

Consequently, if `mu_C` denotes the dimension-normalized empirical spectral measure of a Hermitian matrix `C`, then

```text
boxed:
W_1(mu_(K^2 A_(X,T)),mu_(B_(X,T)))
->0
```

uniformly in `T`.

Thus for every fixed Lipschitz function `f:[0,infinity)->R`,

```text
(1/N_X)Tr f(K^2A_(X,T))
 -(1/N_X)Tr f(B_(X,T))
->0.
```

In particular, for every fixed `Z<infinity`,

```text
boxed:
sup_(0<=z<=Z)
| (1/N_X)log det(I+zK^2A_(X,T))
 -(1/N_X)log det(I+zB_(X,T)) |
->0.
```

Before the `K^2` threshold there is complete ordinary regularized-determinant collapse: for every `c_X=o(K^2)` and fixed `Z<infinity`,

```text
boxed:
sup_(0<=z<=Z)
(1/N_X)log det(I+z c_X A_(X,T))
->0
```

uniformly in `T`.

**Evidence/status:** `EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
growing prime-power depth
+ natural Lambda(n)n^(-1/2) half-weight
+ first nonvanishing K^2 scalar repair
+ ordinary Lipschitz spectral statistics / per-site log det(I+zA)
    -> a distinct depth-sensitive or RH-sensitive phase.
```

The result does not analyze the residual envelope Gram `B` itself. Hard-edge observables, inverse moments, condition numbers, operator-norm outliers, target-relative Schur complements, indefinite completed Weil forms, or scalings beyond ordinary dimension-normalized spectral statistics remain outside the claim.

## The depth multiplier converges to one in mean square

Write

```text
r_n=R_X(n),
delta_n=r_n-1.
```

On the fixed multiplicative shell,

```text
log n/log X=1+O_(a,b)(1/log X)
```

uniformly, while `K/k<=1`. Hence the entries `r_n` are uniformly bounded and it is enough to show

```text
(1/N_X) sum_n |1-K/k|^2 ->0.
```

If

```text
K=o(sqrt L),
```

`PL-090` proves that the depth-`K` layer occupies asymptotically all of `Q_(X,>=K)`. The displayed summand is zero on that layer and at most one on every deeper layer, so its empirical average tends to zero.

If instead

```text
K/sqrt L->alpha>0,
```

`PL-090` proves that the offset

```text
j=k-K
```

has an asymptotically geometric and therefore tight population profile. For every fixed `R`,

```text
sup_(0<=j<=R)
|1-K/(K+j)| <= R/K ->0,
```

while the population outside `0<=j<=R` can be made arbitrarily small uniformly in the limit by choosing `R` large. Since `0<=1-K/k<=1`, bounded convergence through this tightness gives

```text
(1/N_X) sum_n |1-K/k|^2 ->0.
```

Combining with the shell factor yields

```text
boxed:
(1/N_X) sum_n |delta_n|^2 ->0.
```

This is stronger than the logarithmic average used in the determinant comparison of `PL-092` and is the input that upgrades the reduction to trace norm.

## Schatten-Hölder gives normalized trace-norm equivalence

Put

```text
B=B_(X,T),
R=R_X,
D=R-I,
C=K^2A=RBR.
```

Then

```text
C-B=DBR+BD.
```

The envelope Gram is positive semidefinite and has diagonal

```text
B(n,n)=X/n,
```

so on `aX<n<=bX`,

```text
1/b <= B(n,n) <=1/a,
Tr B=Theta_(a,b)(N_X).
```

Classical Schatten Hölder gives

```text
||DBR||_1
 <=||D B^(1/2)||_2 ||B^(1/2)R||_2,

||BD||_1
 <=||B^(1/2)||_2 ||B^(1/2)D||_2.
```

The Hilbert-Schmidt factors are controlled entirely by the diagonal of `B`:

```text
||D B^(1/2)||_2^2
 =Tr(D^2B)
 =sum_n delta_n^2 B(n,n)
 =o(N_X),

||B^(1/2)D||_2^2
 =Tr(DBD)
 =sum_n delta_n^2 B(n,n)
 =o(N_X).
```

Moreover the uniform boundedness of `r_n` gives

```text
||B^(1/2)R||_2^2
 =Tr(RBR)
 =sum_n r_n^2 B(n,n)
 =O_(a,b)(N_X),
```

and

```text
||B^(1/2)||_2^2=Tr B=O_(a,b)(N_X).
```

Therefore

```text
||C-B||_1
 <=o(sqrt(N_X))*O(sqrt(N_X))
   +O(sqrt(N_X))*o(sqrt(N_X))
 =o(N_X).
```

Every bound uses only the diagonal `B(n,n)=X/n`; hence it is uniform in `T`, regardless of how coherent the logarithmic frequencies become off diagonal.

## Trace norm controls the whole ordinary empirical spectrum

For Hermitian matrices of the same size, the classical Lidskii--Mirsky--Wielandt perturbation inequality implies, after ordering eigenvalues compatibly,

```text
sum_j |lambda_j(C)-lambda_j(B)|
 <=||C-B||_1.
```

Coupling the two empirical measures by these ordered eigenvalues gives

```text
W_1(mu_C,mu_B)
 <=(1/N_X)||C-B||_1
 ->0.
```

Equivalently, for every Lipschitz `f`,

```text
| (1/N_X)Tr f(C)-(1/N_X)Tr f(B) |
 <=Lip(f) (1/N_X)||C-B||_1
 ->0.
```

Thus the first admissible scalar repair does not merely erase one moment or one determinant. At the ordinary dimension-normalized level, the entire spectral law is asymptotically insensitive to the natural `1/k` von-Mangoldt depth amplitude.

## The regularized determinant escape also collapses

For `z>=0`,

```text
f_z(lambda)=log(1+z lambda)
```

is `z`-Lipschitz on `[0,infinity)`. Therefore, uniformly for `0<=z<=Z`,

```text
| (1/N_X)log det(I+zC)
 -(1/N_X)log det(I+zB) |
 <= Z (1/N_X)||C-B||_1
 ->0.
```

This closes the ordinary per-site `det(I+zA)` escape explicitly left outside `PL-092` at the first nonvanishing amplitude scale.

Below that scale, positivity and `log(1+x)<=x` give an even simpler bound. For `c_X>=0`,

```text
0<= (1/N_X)log det(I+z c_XA)
   =(1/N_X)sum_j log(1+z c_X lambda_j(A))
 <=z c_X (1/N_X)Tr A.
```

By `PL-091`,

```text
(1/N_X)Tr A=O_(a,b)(K^(-2)),
```

so if `c_X=o(K^2)`, then uniformly for `0<=z<=Z`,

```text
(1/N_X)log det(I+z c_XA)->0.
```

Thus ordinary regularized determinants have exactly the same first possible scalar threshold as the trace and determinant root, and at that threshold the specifically depth-sensitive weight has already become spectrally negligible in normalized trace norm.

## Prior-art and novelty audit

The operator inequalities used here are classical:

- Schatten Hölder, especially `||UV||_1<=||U||_2||V||_2`;
- the Hermitian eigenvalue perturbation/majorization inequality associated with Lidskii, Mirsky, and Wielandt;
- `log(1+x)<=x` and the elementary Lipschitz bound for `log(1+zx)` on the nonnegative half-line.

A targeted literature search over von-Mangoldt-weighted Gram matrices, prime-power/logarithmic-frequency Grams, Dirichlet-polynomial Gram spectra, trace-norm perturbations, and regularized determinants did not locate a specialized result asserting the growing-depth reduction above. The search returned generic Dirichlet-polynomial and matrix-ideal theory rather than a prime-power theorem. Absence from search is not treated as evidence of novelty.

Accordingly, no novelty is claimed for any matrix inequality or for the abstract statement that a small trace-norm perturbation has close empirical spectrum. The durable line-specific content is the combination of those classical facts with the exact prime-power identity

```text
Lambda(p^k)/log(p^k)=1/k
```

and the `PL-090` depth-population law, yielding a uniform trace-norm collapse of the natural arithmetic depth multiplier at precisely the first scalar scale that survives `PL-091` and `PL-092`.

The README's strongest falsification control again fires in the negative direction: the proof uses no rational-prime property beyond the already PNT-level depth population. A generalized-prime or arbitrary-frequency model with the same shell population and `1/k` half-weight has the same trace-norm reduction. The phenomenon is therefore universal background geometry, not arithmetic rigidity.

## Adversarial boundaries

1. **Only the `PL-090` growing-depth population regimes are used for the `S_1/N` equivalence.** The sub-`K^2` regularized-determinant collapse from `PL-091` remains valid for every nonempty tail with `K->infinity`, but the reduction of `K^2A` to `B` is asserted only where the required depth tightness is proved.
2. **Normalized trace norm is an ordinary-bulk metric.** `||C-B||_1/N->0` does not force `||C-B||->0`. A vanishing fraction of extreme or hard-edge eigenvalues may still behave differently.
3. **The envelope Gram is not classified.** The result transfers ordinary spectral questions to `B`; it does not prove that `B` has a limit, is universal, or is insensitive to cross-depth logarithmic-frequency geometry.
4. **Positive regularized determinants only.** The displayed `log det(I+zC)` statement uses fixed `z>=0`. Complex `z`, zeros of a determinant as a function of `z`, perturbation determinants, and target-relative determinants require separate control.
5. **No analytic continuation occurs.** All matrices are finite dimensional and every identity is established directly before any passage to zeta continuation.
6. **The `K^2` threshold remains noncritical for RH.** It is the elementary square of the depth loss `Lambda(p^k)/log(p^k)=1/k`, not a mechanism selecting `Re(s)=1/2`.
7. **Indefinite completed forms are outside the proof.** Positivity is used both in the Gram setup and in the sub-threshold log-determinant bound; Weil-type signed cancellation can evade this argument.

## Consequence for the growing-depth branch

The ordinary natural-weight spectral branch is now closed more broadly than `PL-091`--`PL-092` recorded:

```text
c_X=o(K^2)
    -> empirical mass collapses (`PL-091`)
    -> determinant root collapses (`PL-092`)
    -> per-site log det(I+z c_XA) collapses (this finding);

c_X=K^2
    -> ordinary determinant depth factor disappears (`PL-092`)
    -> the full ordinary empirical spectrum is S_1/N-equivalent
       to the unweighted envelope Gram B (this finding)
    -> every fixed Lipschitz spectral statistic and
       per-site log det(I+z .) inherits the B problem.
```

Accordingly, continuing to vary ordinary polynomial, bounded-Lipschitz, or fixed-positive regularized-determinant statistics of the naturally weighted critical-depth stack would be churn. A surviving route must use information that normalized trace norm can miss — hard-edge/inverse or extreme statistics, determinant zeros in an additional spectral parameter, a distinguished target coupling, an indefinite completed form — or prove genuinely arithmetic structure in the residual envelope Gram `B` itself.