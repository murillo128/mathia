# PL-095 — Growing-depth prime-power Grams are PNT-envelope universal below inverse PNT resolution

## Claim

The off-diagonal logarithmic-frequency geometry left open by `PL-094` is still universal through a large growing observation-time range. Before the finite-time Gram can resolve the actual prime-counting error inside the growing prime-power shell, its coherent spectrum is trace-norm equivalent to a deterministic Fourier/time-band limiting operator built from the continuum PNT envelope.

Fix

```text
0<a<b<infinity,
A=log a,
B=log b,
Delta=B-A,
L=log X,
K=K(X)->infinity,
K=O(sqrt(L)),
Q_(X,>=K)={n=p^k : k>=K, aX<n<=bX},
N_X=|Q_(X,>=K)|,
y_X(n)=log(n/X).
```

For the first depth block define the deterministic PNT shell density

```text
rho_X(y)
 =sum_(k=K)^(2K) exp((L+y)/k)/(L+y),
A<=y<=B,

Z_X=integral_A^B rho_X(y)dy,

d nu_X(y)=rho_X(y)dy/Z_X.
```

The density is the derivative of the logarithmic-integral main term after the map `p -> p^k`. Put

```text
Phi_(L,K)
 =(L/K)^(3/5)/(log(L/K))^(1/5).
```

Using the Vinogradov--Korobov PNT remainder already audited in `PL-062`, there is a constant `c=c(a,b)>0` such that

```text
delta_X
 =L exp(-c Phi_(L,K))
  +L^2 exp(-L/(2K))
 ->0
```

and the empirical shell measure

```text
mu_X=(1/N_X) sum_(n in Q_(X,>=K)) delta_(y_X(n))
```

satisfies

```text
boxed:
||F_(mu_X)-F_(nu_X)||_infinity
 <<_(a,b) delta_X,
```

while the smooth PNT envelope itself is uniformly log-flat,

```text
boxed:
||d nu_X/dy - 1/Delta||_(L^infinity[A,B])
 <<_(a,b) 1/K.
```

Now let

```text
G_(X,T)(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n))dt,

E_X(n)=sqrt(X/n)=exp(-y_X(n)/2),
B_(X,T)=E_X G_(X,T) E_X.
```

On

```text
H_T=L^2([0,T],dt/T)
```

put

```text
u_y(t)=exp(i t y),
P_y=|nu_y><nu_y|.
```

Define the two deterministic continuum operators

```text
C_T^(0)
 =(1/Delta) integral_A^B P_y dy,

C_T^(1)
 =(1/Delta) integral_A^B exp(-y) P_y dy.
```

If eigenvalue lists are arranged decreasingly and padded by zeros, then

```text
boxed:
sum_j |
 lambda_j(G_(X,T)/N_X)-lambda_j(C_T^(0))
|
 <<_(a,b) 1/K + T delta_X,
```

and

```text
boxed:
sum_j |
 lambda_j(B_(X,T)/N_X)-lambda_j(C_T^(1))
|
 <<_(a,b) 1/K +(1+T) delta_X.
```

The bounds are uniform in `T>0`. Consequently, for every horizon family satisfying

```text
boxed:
(1+T_X) delta_X ->0,
```

the entire `N_X`-scaled coherent spectrum, including every fixed extreme eigenvalue and every positive Fredholm determinant

```text
det(I+z B_(X,T_X)/N_X),
0<=z<=Z<infinity,
```

is asymptotically determined by the continuum operator `C_(T_X)^(1)`. Under either depth regime of `PL-093`, the same conclusion holds with `B_(X,T)` replaced by `K^2 A_(X,T)`, where `A_(X,T)` is the naturally von-Mangoldt half-weighted Gram.

A convenient unconditional sufficient range is

```text
boxed:
log T_X=o(Phi_(L,K)).
```

Indeed this implies `(1+T_X)delta_X->0`. At the first depth transition

```text
K/sqrt(L)->alpha in (0,infinity),
```

this includes every horizon with

```text
boxed:
log T_X
 =o(L^(3/10)/(log L)^(1/5)).
```

The comparator is classical. After removing the harmless center-frequency modulation, `C_T^(0)` is exactly the trace-one scalar multiple of the Slepian--Pollak continuous prolate time-band limiting operator for a frequency interval of width `Delta`. The weighted comparator `C_T^(1)` is the equally classical finite Wiener--Hopf/time-frequency limiting operator with fixed symbol

```text
exp(-y) 1_[A,B](y).
```

Thus neither the coherent outliers nor the `1/N_X`-scaled Fredholm determinant can carry rational-prime-specific information throughout this whole sub-inverse-PNT-error range.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
growing prime-power depth K=O(sqrt(log X))
+ sharp finite-time logarithmic Gram
+ first K^2 von-Mangoldt repair / shell envelope
+ observation horizon below inverse PNT-error resolution
+ N_X-scaled extreme spectrum or det(I+z A/N_X)
    -> a rational-prime-specific or RH-sensitive invariant.
```

The result does not classify horizons at or beyond inverse PNT-error resolution, the unscaled hard edge, inverse moments/condition numbers, target-relative Schur complements, or indefinite completed-Weil couplings.

## Quantitative PNT envelope for the shell points

For `K<=k<=2K` and `u in [A,B]`, write

```text
M_(k,u)(X)
 =#{p : aX<p^k<=exp(u)X}
 =pi(exp((L+u)/k))-pi(exp((L+A)/k)).
```

The logarithmic-integral main term is

```text
integral_A^u exp((L+y)/k)/(L+y) dy.
```

The Vinogradov--Korobov estimate for `pi(t)-li(t)` gives, uniformly over the whole block,

```text
M_(k,u)(X)
 =integral_A^u exp((L+y)/k)/(L+y)dy
  +O(exp(L/k) exp(-c Phi_(L,K))).
```

The full layer has size `asymp exp(L/k)/L`, so the endpoint error relative to that shell scale is

```text
O(L exp(-c Phi_(L,K))).
```

uniformly in `k` and `u`. Summing the layer errors does not introduce an additional factor `K`, because each error is bounded by the same relative factor times its own PNT main mass. After normalization by the total first-block mass this gives

```text
sup_u
|F_(actual, K<=k<=2K)(u)-F_(nu_X)(u)|
 <<L exp(-c Phi_(L,K)).
```

The far-depth estimate from `PL-090` gives

```text
sum_(k>2K) M_k(X)/M_K(X)
 <<L^2 exp(-L/(2K)).
```

and the first block contains the depth-`K` layer, so adding the omitted tail changes the normalized CDF by at most the second term in `delta_X`. This proves the first boxed discrepancy estimate.

The smooth envelope has no hidden depth transition. Uniformly for `K<=k<=2K` and `A<=y<=B`,

```text
exp((L+y)/k)/(L+y)
 =exp(L/k)/L
  *[1+O_(a,b)(1/K)].
```

Every layer density is therefore a constant in `y` times the same `1+O(1/K)` relative perturbation. Positive mixing over depth preserves that estimate, and normalization over `[A,B]` yields

```text
d nu_X/dy
 =1/Delta+O_(a,b)(1/K).
```

This strengthens the weak log-uniform law of `PL-094` in exactly the way needed for moving finite-time spectral testing: the deterministic nonuniformity can be separated in total variation, while only the genuinely discrete PNT error must be paid for through frequency resolution.

## Covariance realization of the Gram matrices

Let

```text
S_X:C^(N_X)->H_T,
S_X e_n=N_X^(-1/2) nu_(y_X(n)).
```

Then

```text
S_X^* S_X=G_(X,T)/N_X
```

up to the common phase `exp(i t log X)`, which cancels from every inner product, while

```text
S_X S_X^*
 =integral P_y d mu_X(y).
```

Hence the nonzero eigenvalues of `G_(X,T)/N_X` are exactly those of the empirical covariance operator

```text
C_(mu_X,T)=integral P_y d mu_X(y).
```

For the shell-weighted matrix use

```text
S_X^(1)e_n
 =N_X^(-1/2) exp(-y_X(n)/2) nu_(y_X(n)).
```

Then

```text
(S_X^(1))^* S_X^(1)=B_(X,T)/N_X,
```

and its covariance operator is

```text
C_(mu_X,T)^(1)
 =integral exp(-y) P_y d mu_X(y).
```

Thus the matrix problem can be compared directly with continuum frequency measures without an entrywise-to-operator dimension loss.

## Wasserstein control resolves the discrete PNT error

For unit vectors `nu_y,nu_z`, the difference of rank-one projectors obeys

```text
||P_y-P_z||_(S_1)
 =2 sqrt(1-|<nu_y,nu_z>|^2)
 <=2 ||nu_y-nu_z||.
```

Moreover

```text
||nu_y-nu_z||^2
 =(1/T) integral_0^T
    |exp(ity)-exp(itz)|^2 dt
 <=T^2 |y-z|^2/3.
```

Therefore

```text
boxed:
||P_y-P_z||_(S_1)
 <=(2/sqrt(3))T |y-z|.
```

For probability measures on the fixed interval `[A,B]`, one-dimensional transport gives

```text
W_1(mu,nu)
 =integral_A^B |F_mu(u)-F_nu(u)|du
 <=Delta ||F_mu-F_nu||_infinity.
```

Coupling `mu_X` to the PNT envelope `nu_X` and integrating the projector bound yields

```text
||C_(mu_X,T)-C_(nu_X,T)||_1
 <<_(a,b) T delta_X.
```

For the weighted covariance, on the fixed shell

```text
y -> exp(-y)P_y
```

is trace-norm Lipschitz with constant `O_(a,b)(1+T)`, giving

```text
||C_(mu_X,T)^(1)-C_(nu_X,T)^(1)||_1
 <<_(a,b) (1+T)delta_X.
```

This is the only place where increasing observation time amplifies the arithmetic discrepancy.

## The smooth PNT tilt costs only total variation, not frequency

The previous estimate should not be combined naively with the `O(1/K)` difference between `nu_X` and uniform measure through the same `T`-Lipschitz bound. The PNT envelope is already absolutely continuous, and its density differs from `1/Delta` by `O(1/K)` uniformly. Therefore its total-variation distance from uniform measure is `O(1/K)`.

Since

```text
||P_y||_1=1
```

and `exp(-y)` is bounded on `[A,B]`, direct integration gives

```text
||C_(nu_X,T)-C_T^(0)||_1
 <<_(a,b)1/K,

||C_(nu_X,T)^(1)-C_T^(1)||_1
 <<_(a,b)1/K,
```

with **no factor `T`**. Combining the two comparisons gives the trace-norm operator bounds in the claim.

For compact positive self-adjoint operators, the Lidskii--Mirsky eigenvalue inequality then yields

```text
sum_j |lambda_j(C)-lambda_j(D)|
 <=||C-D||_1.
```

Since the covariance operators and the scaled Gram matrices have the same nonzero spectra, the displayed eigenvalue-list estimates follow immediately.

## Fredholm determinants and coherent outliers also classicalize

For `z>=0`, `lambda -> log(1+z lambda)` is `z`-Lipschitz on `[0,infinity)`. Hence for every fixed `Z<infinity`,

```text
sup_(0<=z<=Z)
|log det(I+z B_(X,T)/N_X)
 -log det(I+z C_T^(1))|

 <<_(a,b,Z) 1/K +(1+T)delta_X.
```

The right-hand determinant is the ordinary Fredholm determinant of a positive trace-class Fourier-limiting operator. The same trace-norm bound controls each fixed ordered eigenvalue, so passing from ordinary empirical spectral statistics in `PL-093` to the `N_X`-scaled coherent outlier sector does not rescue arithmetic information in this range.

Under the hypotheses of `PL-093`,

```text
(1/N_X)||K^2 A_(X,T)-B_(X,T)||_1 ->0
```

uniformly in `T`. Equivalently,

```text
||K^2 A_(X,T)/N_X-B_(X,T)/N_X||_1->0.
```

Thus the same continuum reduction applies to the first nonvanishing von-Mangoldt normalization.

There is also a useful large-`T` sanity check. The uniform weighted comparator is, up to Fourier convention,

```text
C_T^(1)
 =(2 pi/(T Delta))
   P_[0,T] F^(-1)
   M_(exp(-y)1_[A,B](y))
   F P_[0,T].
```

Therefore

```text
||C_T^(1)||
 <=2 pi/(T Delta) *max_(A<=y<=B) exp(-y),
```

while

```text
Tr C_T^(1)
 =(1/Delta) integral_A^B exp(-y)dy
 =(1/Delta)(1/a-1/b).
```

If `T_X->infinity` but still `(1+T_X)delta_X->0`, every `N_X`-scaled extreme eigenvalue tends to zero and

```text
log det(I+z B_(X,T_X)/N_X)
 ->z/Delta*(1/a-1/b)
```

for fixed `z>=0`. The coherent Fredholm determinant then degenerates to the elementary exponential of the trace rather than developing a new arithmetic phase.

## Classical time-band limiting collision

For the unweighted comparator, the frequency midpoint `(A+B)/2` is a diagonal/unitary modulation and does not affect the spectrum. After rescaling `[A,B]` to `[-1,1]`, the integral kernel is

```text
(1/2) sinc(c(x-x')),

c=T Delta/4.
```

Equivalently,

```text
C_T^(0)
 =(2 pi/(T Delta)) Q_c,
```

where `Q_c` is the standard continuous Slepian--Pollak prolate concentration operator with kernel

```text
sin(c(x-x'))/[pi(x-x')].
```

So the continuum off-diagonal spectrum is not merely analogous to a familiar signal-processing object; it is exactly a trace-one rescaling of the classical time-band limiting operator. `PL-078` already found the discrete prolate operator in a different local sharp-Gram scaling. The present collision is its continuous growing-depth shell counterpart.

The shell factor `exp(-y)` converts the flat band symbol into a fixed positive frequency weight but does not restore arithmetic: `C_T^(1)` is simply a finite Wiener--Hopf/Fourier multiplier compression whose symbol is determined by the macroscopic shell endpoints.

## Prior-art and novelty audit

The ingredients are classical and are not claimed as new:

- the Vinogradov--Korobov PNT remainder and its modern sharp form are already anchored in `SOURCES.md` 59--60 and used in `PL-062`;
- continuous sinc-kernel time-band limiting is the classical Slepian--Pollak/prolate problem, while `PL-078` already stores the corresponding discrete prolate collision for a local sharp logarithmic Gram;
- nonzero spectra of `S^*S` and `SS^*`, one-dimensional Wasserstein transport, trace-norm bounds for rank-one projectors, and Lidskii--Mirsky eigenvalue perturbation are standard functional analysis.

A targeted literature search over prime-power logarithmic-frequency Gram matrices, von-Mangoldt Gram matrices, prolate operators on prime-power shells, and finite-time Dirichlet-polynomial Grams did not locate a specialized theorem asserting this growing-depth PNT-envelope reduction. The search instead returned ordinary Dirichlet-polynomial mean-value theory and classical time-band limiting. Absence from search is not treated as novelty evidence.

The durable line-specific content is the combination of four already-audited pieces that had not yet been closed together:

```text
growing prime-power shell
 -> quantitative layerwise PNT envelope;

shell log positions
 -> a frequency measure;

finite-time Gram / N_X
 -> covariance operator of that measure;

trace-norm transport
 -> a deterministic prolate/Wiener--Hopf spectral comparator
    until the observation horizon resolves the PNT error.
```

The matched-control audit is negative in the intended direction. A generalized-prime system whose base-prime counting function has the same quantitative PNT remainder on these shells produces the same continuum envelope and the same argument. The `3/5` barrier is therefore a zero-free-region/PNT resolution scale, not a mechanism selecting `Re(s)=1/2`.

## Adversarial boundaries

1. **The inverse-PNT range is sufficient, not sharp.** The estimate proves universality when `(1+T)delta_X->0`; failure of this condition does not imply arithmetic spectral structure appears.
2. **Only the first growing-depth range is controlled.** The proof uses `K=O(sqrt(log X))`, where `PL-090` supplies a negligible tail beyond `2K` and the layer shells remain inside uniform quantitative PNT control.
3. **The comparator is continuum PNT geometry, not exact prime geometry.** At horizons capable of resolving errors smaller than the available PNT remainder, the proof deliberately stops.
4. **Hard-edge observables remain open.** Trace-norm convergence of `B/N_X` controls its macroscopic coherent eigenvalues and positive Fredholm determinants but not the smallest eigenvalues of the unscaled matrix, inverse moments, or condition numbers.
5. **No target or completion is present.** Nyman-type pointed approximation, indefinite Weil forms, functional-equation coupling, and zero-divisor information can evade a positive covariance comparison.
6. **The result uses only `Re(s)=1`-side information.** The PNT remainder comes from the classical zero-free region near `1`; no Euler product is analytically continued by the matrix argument and no critical-line zero is inserted.
7. **The shell-weighted comparator is not claimed to have a new spectral law.** It is a standard finite Fourier-multiplier compression. Its exact finite-`T` eigenvalues need not be elementary for the negative conclusion.
8. **Beurling discrimination fails.** Any matched generalized-prime model with the same shellwise PNT accuracy obeys the same transport bound, so survival below this scale cannot be a rational-prime-specific mechanism.

## Consequence for the growing-depth branch

`PL-091`--`PL-094` removed the vanishing amplitude, determinant volume, ordinary empirical spectrum, depth population, and one-point shell envelope from the list of possible information carriers. This finding removes the next natural escape over a broad moving-time range:

```text
residual off-diagonal frequency Gram
+ coherent 1/N_X scaling
+ observation time below inverse PNT-error resolution
    -> deterministic PNT envelope
    -> classical prolate/Wiener--Hopf operator.
```

Accordingly, a rational-prime-specific mechanism in the growing prime-power Gram branch must now do at least one of the following:

```text
resolve shell discrepancies at or beyond inverse-PNT accuracy;
use a hard-edge/inverse statistic invisible to trace-norm coherent scaling;
retain a distinguished arithmetic target;
introduce an indefinite completed/explicit-formula coupling;
or leave the K=O(sqrt(log X)) depth regime.
```

Merely increasing the sharp observation horizon through any range with

```text
log T=o((L/K)^(3/5)/(log(L/K))^(1/5))
```

cannot expose an RH-sensitive prime-lattice spectrum: the full coherent spectral data is still asymptotically classical continuum Fourier geometry.