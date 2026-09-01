# PL-097 — Super-N observation makes the S1 Gram defect universally maximal by rank

## Claim

The `S_1`-fine spectral-mass escape left open by `PL-096` has a universal obstruction at sufficiently long observation time. For the growing prime-power shell of `PL-094`--`PL-096`, once the observation horizon is much larger than the number of shell points, the empirical finite-rank covariance and its smooth PNT/continuum comparator become **maximally separated in trace norm and in `ell^1` eigenvalue distance**, independently of the arithmetic locations of those points.

Keep

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
y_X(n)=log(n/X),
```

along a sequence with `N_X->infinity`. On

```text
H_T=L^2([0,T],dt/T),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

let

```text
C_(mu_X,T)^(0)
 =(1/N_X) sum_(n in Q_(X,>=K)) P_(y_X(n)),

C_T^(0)
 =(1/Delta) integral_A^B P_y dy.
```

Then both are positive trace-class operators of trace one, while

```text
rank C_(mu_X,T)^(0)<=N_X
```

and the Fourier-multiplier representation already used in `PL-095` gives

```text
||C_T^(0)|| <= 2 pi/(T Delta).
```

Consequently

```text
boxed:
||C_(mu_X,T)^(0)-C_T^(0)||_(S_1)
 >=2[1-2 pi N_X/(T Delta)].
```

Since the opposite bound is always at most `2`, every horizon family with

```text
boxed:
T_X/N_X -> infinity
```

satisfies

```text
boxed:
||C_(mu_X,T_X)^(0)-C_(T_X)^(0)||_(S_1) ->2.
```

The same maximal separation occurs at the level of ordered eigenvalue lists. If `alpha_(X,T),r` are the eigenvalues of `G_(X,T)/N_X` and `beta_(T,r)` those of `C_T^(0)`, both decreasing and padded by zeros, then

```text
boxed:
sum_(r>=1)|alpha_(X,T_X),r-beta_(T_X,r)| ->2
```

whenever `T_X/N_X->infinity`.

For the shell-weighted covariance

```text
C_(mu_X,T)^(1)
 =(1/N_X) sum_n exp(-y_X(n)) P_(y_X(n)),

C_T^(1)
 =(1/Delta) integral_A^B exp(-y)P_y dy,
```

put

```text
m=(1/Delta)(1/a-1/b).
```

`PL-094` gives

```text
Tr C_(mu_X,T)^(1)->m,
Tr C_T^(1)=m,
```

and `PL-095` gives

```text
||C_T^(1)||
 <=2 pi/(T Delta a).
```

Hence for `T_X/N_X->infinity`,

```text
boxed:
||C_(mu_X,T_X)^(1)-C_(T_X)^(1)||_(S_1) ->2m,
```

and the `ell^1` distance between their ordered eigenvalue lists also tends to `2m`. Under either depth regime of `PL-093`, its uniform `S_1` equivalence transfers the same eigenvalue-list conclusion to the naturally half-weighted von-Mangoldt Gram `K^2 A_(X,T)/N_X`.

Thus the failure of all-horizon `S_1` convergence at super-`N_X` time is not hidden rational-prime information. It is the largest possible trace-class separation allowed by the common trace, forced solely by comparing an at-most-`N_X`-dimensional empirical state with a diffuse time-band limiting operator whose norm is `O(1/T)`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-OPERATOR-THEORY + DECISIVE-NEGATIVE` for the route

```text
growing prime-power shell
+ first K^2 von-Mangoldt repair / envelope Gram
+ T_X/N_X -> infinity
+ S_1 nonconvergence or ell^1 spectral mass
    -> rational-prime-specific or RH-sensitive information.
```

No novelty is claimed for trace-norm duality, Ky Fan rank bounds, or time-bandwidth/Nyquist geometry. The line-specific contribution is the application of those elementary facts to the exact `S_1` loophole left by `PL-096`: in the super-sampling regime that loophole is not merely uncontrolled; it is provably dominated by universal rank mismatch.

## A finite-rank state cannot approximate the diffuse comparator in S1 when `T >> N`

Write

```text
A=C_(mu_X,T)^(0),
B=C_T^(0),
N=N_X.
```

Let `P` be the orthogonal projection onto the range of `A`. Then

```text
rank P<=N,
PA=A,
Tr A=Tr B=1.
```

The self-adjoint unitary

```text
Q=2P-I
```

has operator norm one. Trace-norm duality therefore gives

```text
||A-B||_1
 >=|Tr Q(A-B)|.
```

Because `PA=A`,

```text
Tr Q(A-B)
 =Tr A+Tr B-2Tr(PB)
 =2-2Tr(PB).
```

Positivity of `B` implies

```text
Tr(PB)<=rank(P)||B||<=N||B||.
```

The continuum operator is the fixed-band Fourier compression from `PL-095`, so

```text
||B||<=2 pi/(T Delta).
```

Combining the estimates yields

```text
||A-B||_1
 >=2[1-2 pi N/(T Delta)].
```

On the other hand positivity and the triangle inequality give

```text
||A-B||_1<=||A||_1+||B||_1=2.
```

Thus `T/N->infinity` squeezes the trace norm to its maximal possible value `2`.

Nothing in this argument uses that the points are prime powers. It works for **every** set of at most `N` frequencies in `[A,B]`, even with arbitrary spacing or multiplicity. In particular it also applies if the smooth comparator is the `PL-095` PNT envelope `nu_X` instead of the exactly log-uniform measure: its density is uniformly bounded, so the corresponding Fourier-compression norm is still `O(1/T)`.

## The same obstruction is visible in the eigenvalue list

Let

```text
alpha_1>=alpha_2>=...>=0
```

be the eigenvalues of `A`, padded by zeros, and

```text
beta_1>=beta_2>=...>=0
```

those of `B`. Since `rank A<=N`,

```text
alpha_r=0,
r>N.
```

Put

```text
B_N=sum_(r=1)^N beta_r.
```

Then

```text
B_N<=N beta_1<=N||B||
 <=2 pi N/(T Delta).
```

Using only the trace identities,

```text
sum_r |alpha_r-beta_r|

 >=|sum_(r=1)^N(alpha_r-beta_r)|
   +sum_(r>N) beta_r

 =|1-B_N|+(1-B_N).
```

For `T/N->infinity`, `B_N->0`, so the right side tends to `2`. The trivial upper bound

```text
sum_r |alpha_r-beta_r|
 <=sum_r alpha_r+sum_r beta_r=2
```

proves the claimed limit.

This is stronger than observing that the covariance operators live on different effective time-bandwidth scales: even after discarding eigenvectors and comparing only the ordered positive spectra, the `ell^1` discrepancy is asymptotically maximal.

## Weighted shell and the von-Mangoldt Gram

For

```text
A_1=C_(mu_X,T)^(1),
B_1=C_T^(1),
```

let `P_1` project onto the range of `A_1`. Again `rank P_1<=N`. Since `exp(-y)>0` on the shell, the empirical trace is

```text
t_X=Tr A_1
 =(1/N) sum_n exp(-y_X(n)),
```

and `PL-094` gives `t_X->m`, where

```text
m=(1/Delta) integral_A^B exp(-y)dy
  =(1/Delta)(1/a-1/b).
```

The continuum trace equals `m` exactly. Applying the same dual test `2P_1-I` gives

```text
||A_1-B_1||_1
 >=t_X+m-2N||B_1||.
```

The fixed weighted band symbol satisfies

```text
||B_1||<=2 pi/(T Delta a).
```

The triangle inequality gives the matching upper bound `t_X+m`. Hence

```text
T/N->infinity
 => ||A_1-B_1||_1->2m.
```

For ordered eigenvalues, the identical tail argument gives

```text
sum_r |alpha_r^(1)-beta_r^(1)|
 ->2m.
```

`PL-093` proves, in its two growing-depth regimes, uniformly in `T`,

```text
||K^2 A_(X,T)/N_X-B_(X,T)/N_X||_(S_1)->0.
```

Trace-class eigenvalue perturbation therefore transfers the `ell^1` spectral separation from `B/N_X` to `K^2 A/N_X`. The von-Mangoldt half-weight changes neither the super-`N` obstruction nor its universal origin.

## Why this coexists with PL-096

There is no contradiction with

```text
sup_T
||C_(mu_X,T)^(j)-C_T^(j)||_(S_2)->0.
```

At super-`N` horizons the continuum trace is spread over roughly time-bandwidth-many very small modes, while the empirical covariance can occupy at most `N` modes. Trace norm counts the entire positive mass linearly, whereas Hilbert--Schmidt norm squares the mode sizes. A sequence can therefore have

```text
S_2 distance ->0
```

while its

```text
S_1 distance -> maximal value.
```

This is ordinary lack of uniform integrability across Schatten ideals, not evidence that an arithmetic zero signal has survived the `S_2` no-go.

It also explains why the fixed positive Fredholm determinant of `PL-096` remains universal. For fixed `z>=0`, the nonlinear correction to `z Tr C` is bounded by `z^2 Tr(C^2)/2`; the trace-class distance can be maximal while the Hilbert--Schmidt mass controlling that correction vanishes.

## Prior-art and novelty audit

The mechanism is classical at every ingredient level.

- The variational characterization of the trace norm and the bound on the mass a rank-`N` projection can capture from a positive operator are standard trace-class/Ky Fan facts.
- The continuum comparator is the Slepian--Pollak/Wiener--Hopf time-band limiting operator already identified in `PL-095`; its `O(1/T)` operator norm is the fixed-band Fourier-multiplier bound used there.
- `PL-078` and `PL-080` already establish that Nyquist/time-bandwidth transitions of sharp logarithmic Gram systems are classical sampling geometry rather than prime-factorization structure.

A targeted literature check for trace-distance/rank approximation of time-band limiting operators and finite-rank density operators finds precisely this classical operator-theoretic setting, not a prime-specific theorem. No new literature anchor is needed beyond the sources already stored for `PL-078`--`PL-080` and `PL-095`.

Accordingly, no novelty is claimed for the rank inequality itself. The durable new information for this line is negative: **the most obvious way `S_1` can fail after the uniform `S_2` closure of `PL-096` is guaranteed to fail for a completely universal reason.**

## Adversarial boundaries

1. **This does not prove all-horizon `S_1` universality.** It proves the opposite at `T/N->infinity`, and identifies the reason. The intermediate regime in which `T=O(N)` but the `PL-095` transport bound is no longer small remains open.
2. **The result does not classify the hard edge.** Smallest eigenvalues, inverse moments, condition numbers, and unscaled determinants can depend on spacing information even when the positive coherent spectrum is universal.
3. **Rank mismatch is not an arithmetic discriminator.** Any `N`-point frequency set in a fixed interval has the same obstruction against a bounded-density continuum comparator.
4. **No statement about RH follows from maximal `S_1` distance.** The argument uses only positivity, trace, rank, and the fixed-band norm estimate; it never crosses the `Re(s)=1` Euler-product boundary or invokes the zeta zero divisor.
5. **The transition window `T~N` is not classified here.** `PL-078`--`PL-080` warn that ordinary Nyquist geometry is already the default control, but the growing prime-power point set is not an equally spaced lattice, so a new proof would be needed before declaring that whole window universal.
6. **Target-relative and indefinite couplings remain outside the no-go.** A distinguished arithmetic vector, a Schur complement, or a completed Weil sign structure can evade the positive covariance/rank argument.
7. **The depth range remains that of `PL-094`--`PL-096` for the weighted transfer.** The bare rank statement is general, but the shell-trace asymptotic and the `K^2` von-Mangoldt equivalence used here are currently established only in the first growing-depth regimes.

## Consequence for the surviving branch

`PL-096` left `S_1`-fine mass as a formally possible carrier because uniform Hilbert--Schmidt convergence does not imply trace-norm convergence. This finding shows that the far end of that escape is misleading:

```text
T << inverse PNT discrepancy
    -> PL-095 gives S_1 continuum transport;

all T
    -> PL-096 gives S_2 spectral universality;

T >> N_X
    -> S_1 distance is universally maximal by rank.
```

Therefore a rational-prime-specific `S_1` mechanism, if one exists at all in this branch, must live in the **intermediate transition window** between the regime where smooth PNT transport still controls trace class and the regime where mere finite-rank sampling forces maximal trace-class separation. It cannot be inferred from the existence of `S_1` nonconvergence itself.
