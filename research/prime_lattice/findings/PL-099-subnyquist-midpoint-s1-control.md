# PL-099 — Sub-Nyquist midpoint sampling attains the prolate continuum in trace norm

## Claim

The finite-ratio trace-class window left open by `PL-098` has a sharp non-arithmetic control on the sub-Nyquist side. The universal rank obstruction disappears there not merely because the lower bound becomes zero: an elementary deterministic `N`-point frequency cloud actually converges to the diffuse prolate comparator in `S_1`.

Fix

```text
A<B,
Delta=B-A,
m=(A+B)/2,
```

and, for each `N`, place the midpoint grid

```text
y_(j,N)=A+(j-1/2) Delta/N,
1<=j<=N.
```

On

```text
H_T=L^2([0,T],dt/T),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

define the empirical and continuum covariance operators

```text
A_(N,T)=(1/N) sum_(j=1)^N P_(y_(j,N)),

B_T=(1/Delta) integral_A^B P_y dy.
```

Both are positive trace-one operators and `rank A_(N,T)<=N`. If

```text
N->infinity,
T_N/N -> tau,
0<tau<2 pi/Delta,
```

then

```text
boxed:
||A_(N,T_N)-B_(T_N)||_(S_1) ->0.
```

Consequently the ordered eigenvalue lists converge in `ell^1`, and for every fixed bounded `z>=0`,

```text
log det(I+z A_(N,T_N))
 -log det(I+z B_(T_N))
 ->0.
```

The threshold is the same classical time-bandwidth value isolated in `PL-098`:

```text
W_T=T Delta/(2 pi).
```

Thus the finite-ratio phase has a genuinely two-sided non-arithmetic interpretation:

```text
T_N/N -> tau < 2 pi/Delta
    -> a deterministic midpoint grid attains the continuum in S_1;

T_N/N -> tau > 2 pi/Delta
    -> every positive trace-one rank-N state has a universal
       positive S_1 distance from the continuum (PL-098).
```

The exact endpoint `tau=2 pi/Delta` is not classified here.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
finite-ratio sub-Nyquist shell covariance
+ S_1 convergence to the PNT/prolate continuum
    -> rational-prime-specific or RH-sensitive evidence by itself.
```

This finding does **not** prove that the actual prime-power shell covariance converges in `S_1` when `T_N/N_X` tends to a sub-Nyquist constant. Its point is a discrimination control: if such convergence occurs, the convergence itself is already reproduced by a completely non-arithmetic cloud with the same macroscopic shell and sampling density. Any arithmetic content must therefore be in the excess error, microscopic spacing, coefficients, a distinguished target, or another coupling absent from this control.

## Exact midpoint kernel

Relative to the normalized measure `dt/T`, the rank-one projector `P_y` has integral kernel

```text
P_y(t,s)=exp(i y(t-s)).
```

Put

```text
u=t-s.
```

The midpoint average is an exact finite geometric sum:

```text
K_(N,T)(u)
 =(1/N) sum_(j=1)^N exp(i y_(j,N) u)

 =exp(i m u)
   sin(Delta u/2)
   /[N sin(Delta u/(2N))].
```

The continuum comparator has kernel

```text
K_T(u)
 =(1/Delta) integral_A^B exp(i y u)dy

 =exp(i m u)
   sin(Delta u/2)/(Delta u/2).
```

These formulas are understood by continuity at `u=0`.

Set

```text
x=Delta u/(2N).
```

Then `Delta u/2=Nx`, and the kernel difference is exactly

```text
K_(N,T)(u)-K_T(u)
 =exp(i m u)
  [sin(Nx)/N]
  [1/sin x-1/x].
```

Suppose

```text
T_N/N -> tau<2 pi/Delta.
```

Choose `c<pi` so that eventually

```text
|x|<=Delta T_N/(2N)<=c
```

for every `|u|<=T_N`. The function

```text
x -> 1/sin x-1/x
```

has a removable zero at `x=0` and is bounded on `[-c,c]`. Therefore

```text
boxed:
sup_(|u|<=T_N)
|K_(N,T_N)(u)-K_(T_N)(u)|
 <=C_c/N.
```

Since `H_T` uses normalized measure,

```text
||A_(N,T_N)-B_(T_N)||_(S_2)^2
 =(1/T_N^2)
   integral_0^(T_N) integral_0^(T_N)
   |K_(N,T_N)(t-s)-K_(T_N)(t-s)|^2 dt ds,
```

and hence

```text
boxed:
||A_(N,T_N)-B_(T_N)||_(S_2)=O(1/N).
```

This estimate uses only equally spaced midpoint quadrature and the strict sub-Nyquist inequality. No prime distribution, Euler product, or analytic continuation enters.

## A finite-rank lifting lemma upgrades `S_2` to `S_1`

Hilbert--Schmidt convergence is not enough for the `PL-098` trace-class question because the rank grows with `N`. The missing upgrade follows from the spectral concentration of the continuum comparator.

Let `A>=0` and `B>=0` be trace-one operators, with `rank A<=N`. Let `Q` be the spectral projection onto the top `N` eigenvectors of `B`, and write

```text
epsilon_N=Tr((I-Q)B)
          =1-sum_(j=1)^N beta_j(B).
```

For

```text
D=A-B,
```

block decomposition relative to `Q+(I-Q)` gives

```text
||Q D Q||_1
 <=sqrt(N)||D||_2,

||Q D(I-Q)||_1
 <=sqrt(N)||D||_2,

||(I-Q)D Q||_1
 <=sqrt(N)||D||_2.
```

For the tail block, positivity gives

```text
||(I-Q)D(I-Q)||_1
 <=Tr((I-Q)A)+Tr((I-Q)B).
```

Because `Tr A=Tr B=1`,

```text
Tr((I-Q)A)
 =epsilon_N-Tr(QD),
```

and

```text
|Tr(QD)|
 =|Tr(QDQ)|
 <=sqrt(N)||D||_2.
```

Therefore

```text
||(I-Q)D(I-Q)||_1
 <=2 epsilon_N+sqrt(N)||D||_2.
```

Summing the four blocks yields the useful general estimate

```text
boxed:
||A-B||_1
 <=4 sqrt(N)||A-B||_2
   +2[1-sum_(j=1)^N beta_j(B)].
```

No commutativity between `A` and `B` is assumed.

## Prolate concentration closes the sub-Nyquist side

For the present continuum operator, `PL-095` and `PL-098` identify

```text
B_T=(2 pi/(T Delta)) Q_c,
c=T Delta/4,
```

with the classical continuous prolate concentration operator. Its time-bandwidth dimension is

```text
W_T=T Delta/(2 pi).
```

`PL-098`, using the Landau--Pollak/Landau--Widom eigenvalue concentration theorem, proves that whenever

```text
T_N/N -> tau in (0,infinity),
```

one has

```text
sum_(j=1)^N beta_j(B_(T_N))
 ->min(1,2 pi/(tau Delta)).
```

For the strict sub-Nyquist range

```text
tau<2 pi/Delta,
```

this gives

```text
epsilon_N
 =1-sum_(j=1)^N beta_j(B_(T_N))
 ->0.
```

Insert the midpoint estimate

```text
||A_(N,T_N)-B_(T_N)||_2=O(1/N)
```

into the lifting lemma. Then

```text
||A_(N,T_N)-B_(T_N)||_1
 <=O(N^(-1/2))+2 epsilon_N
 ->0.
```

This is the claimed trace-norm convergence.

For positive compact operators, the standard Lidskii--Mirsky eigenvalue inequality gives

```text
sum_j
|lambda_j(A_(N,T_N))-lambda_j(B_(T_N))|
 <=||A_(N,T_N)-B_(T_N)||_1
 ->0.
```

Likewise, for fixed `z>=0`, the map `lambda ->log(1+z lambda)` is `z`-Lipschitz on `[0,infinity)`, so

```text
|log det(I+zA)-log det(I+zB)|
 <=z||A-B||_1.
```

Thus the entire ordinary positive Fredholm determinant also has the same sub-Nyquist continuum limit in this non-arithmetic control.

## The control is itself a discrete prolate system

The nonzero spectrum of `A_(N,T)` is the spectrum of its `N x N` Gram matrix. After a harmless diagonal phase gauge, that matrix has entries

```text
(1/N)
 sinc((T Delta/(2N))(j-k)).
```

This is the standard discrete time/band limiting Toeplitz geometry. In particular, the strict inequality

```text
T Delta/(2N)<pi
```

is exactly the no-alias/Nyquist side of the same prolate sampling theory that appeared locally in `PL-078` and in the continuum rank count of `PL-098`.

The classical prior art is mature rather than zeta-specific. David Slepian's discrete prolate theory studies precisely finite equally spaced samples under time/frequency concentration:

- D. Slepian, “Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case,” *Bell System Technical Journal* **57**(5) (1978), 1371–1430, DOI `10.1002/j.1538-7305.1978.tb02104.x`.

The continuous concentration/rank asymptotics used through `PL-098` are the classical Landau--Pollak and Landau--Widom results already audited there. No novelty is claimed for discrete prolate sequences, midpoint quadrature, Nyquist sampling, or prolate eigenvalue concentration. The line-specific contribution is the exact control conclusion: the side of the `PL-098` phase where the universal rank floor vanishes is actually attainable in `S_1` by a deterministic non-arithmetic shell with the same macroscopic geometry.

## Rational-prime discrimination

The midpoint cloud uses only

```text
[A,B], N, T.
```

It has no multiplication, prime powers, von Mangoldt weights, Möbius signs, Euler product, functional equation, or zeta zero divisor. Nevertheless, below the same finite Nyquist threshold as `PL-098`, it reproduces the continuum comparator in trace norm and hence in the full ordered eigenvalue list and positive Fredholm determinant.

Therefore the statement

```text
empirical shell covariance
 -> continuum PNT/prolate covariance in S_1
```

cannot by itself distinguish rational primes from a matched deterministic sampling system. Conversely, `PL-098` shows that a positive `S_1` defect above Nyquist also cannot distinguish them, because a universal rank floor is forced there for every `N`-point positive state.

The only potentially discriminating quantity in this finite-ratio trace-class branch is therefore something beyond the raw side of the phase: for example the **excess over the best non-arithmetic control/rank floor**, a rate tied to microscopic prime-power spacing, an arithmetic coefficient/target, or an indefinite completed coupling.

## Adversarial boundaries

1. **No prime-power `S_1` convergence at `T~tau N_X` is proved.** `PL-095` controls the actual shell only while the observation horizon is below the inverse PNT-discrepancy scale. The present midpoint cloud is a matched control, not a surrogate theorem for prime gaps.
2. **The critical endpoint is deliberately excluded.** At `tau=2 pi/Delta`, the factor `1/sin x` reaches its first pole at the edge of the difference interval, so the uniform `O(1/N)` kernel estimate used here is unavailable. The prolate transition also has its classical logarithmic edge width. A separate endpoint analysis would be needed.
3. **The super-Nyquist excess remains open.** `PL-098` identifies the exact minimum trace distance imposed by rank, but an arithmetic empirical covariance may lie strictly farther from the continuum than that optimum.
4. **The weighted/von-Mangoldt comparator is not classified sharply here.** The argument is for the unweighted trace-one covariance. A weighted Wiener--Hopf analogue would require its own spectral-tail estimate and control.
5. **Microscopic spacing is intentionally erased by the control.** Failure of the actual prime-power cloud to behave like the midpoint grid at the same ratio could be mathematically meaningful. This finding says only that success is not, by itself, arithmetic evidence.
6. **No analytic continuation or RH input occurs.** The proof is finite Fourier/operator theory plus classical prolate spectral concentration. It neither imports nor constrains the zeta zero divisor.

## Consequence for the growing-depth `S_1` branch

The current hierarchy can now be stated with a sharper discrimination boundary:

```text
actual prime-power shell,
(1+T_X) delta_X ->0
    -> S_1 transport to the PNT/prolate continuum (PL-095);

matched midpoint shell,
T_N/N -> tau < 2 pi/Delta
    -> S_1 transport to the same continuum (PL-099);

any positive N-point shell state,
T_N/N -> tau > 2 pi/Delta
    -> universal positive S_1 rank floor (PL-098);

T_N/N -> infinity
    -> universal floor tends to maximal distance 2 (PL-097).
```

Thus neither side of the coarse finite-ratio trace-class phase is intrinsically arithmetic. A viable continuation must resolve what the raw Nyquist/rank geometry has quotiented out: exact frequency-spacing discrepancies, arithmetic weights/support, a distinguished target, completion, or another observable whose value changes under the line's non-arithmetic/Beurling controls.