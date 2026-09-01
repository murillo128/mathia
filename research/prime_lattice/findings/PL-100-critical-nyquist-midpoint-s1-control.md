# PL-100 — Exact Nyquist midpoint sampling attains the continuum in trace norm

## Claim

The exact endpoint left open by `PL-099` admits a fully deterministic non-arithmetic control. Fix

```text
A<B,
Delta=B-A,
```

and for each `N>=1` set the midpoint frequencies

```text
y_(j,N)=A+(j-1/2) Delta/N,
1<=j<=N,
```

at the **exact Nyquist observation time**

```text
T_N=2 pi N/Delta.
```

On

```text
H_N=L^2([0,T_N],dt/T_N),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

define

```text
A_N=(1/N) sum_(j=1)^N P_(y_(j,N)),

B_N=(1/Delta) integral_A^B P_y dy.
```

Then

```text
boxed:
||A_N-B_N||_(S_1)
 =O(sqrt(log N/N))
 ->0.
```

Consequently the ordered eigenvalue lists converge in `ell^1`, and for every fixed bounded `z>=0`,

```text
log det(I+z A_N)-log det(I+z B_N) ->0.
```

Thus the critical value

```text
T_N Delta/(2 pi N)=1
```

is not, by itself, an arithmetic discriminator. A completely non-arithmetic equally spaced midpoint cloud attains the same log-uniform PNT/prolate continuum in trace norm at exact Nyquist.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
exact-Nyquist shell covariance
+ S_1 convergence to the PNT/prolate continuum
    -> rational-prime-specific or RH-sensitive evidence by itself.
```

This finding does **not** prove trace-norm convergence for the actual prime-power shell at critical scale, nor does it classify every sequence with `T_N/N -> 2 pi/Delta`. It supplies a decisive matched control at the exact endpoint: if an arithmetic cloud also converges there, the bare convergence statement is already reproduced without primes, multiplication, Euler products, or zeta zeros.

## Exact Fourier orthogonality at Nyquist

At the chosen observation time,

```text
Delta/N = 2 pi/T_N.
```

Hence for `j!=k`,

```text
<nu_(y_(j,N)),nu_(y_(k,N))>
 =(1/T_N) integral_0^(T_N)
   exp(i t (y_(k,N)-y_(j,N))) dt
 =0.
```

The `N` midpoint exponentials are therefore orthonormal. If `P_N` denotes their orthogonal projection, then

```text
boxed:
A_N=(1/N)P_N.
```

In particular,

```text
Tr A_N=1,
Tr A_N^2=1/N.
```

The continuum comparator is also positive trace one. Plancherel gives, for every `f in H_N`,

```text
integral_R |<f,nu_y>|^2 dy
 =(2 pi/T_N)||f||^2,
```

so

```text
<B_N f,f>
 <=(1/Delta)(2 pi/T_N)||f||^2
 =(1/N)||f||^2.
```

Therefore

```text
boxed:
0<=B_N<=I/N,
Tr B_N=1,
Tr B_N^2<=1/N.
```

This is the critical time-bandwidth normalization of the same continuous prolate comparator used in `PL-095`--`PL-099`, but no prolate eigenvalue asymptotic is needed below.

## The selected Fourier block misses only `O(log N/N)` continuum mass

Parameterize the continuum band by

```text
y=A+(Delta/N)r,
0<=r<=N.
```

The complete family

```text
A+(k+1/2)Delta/N,
k in Z,
```

is a full orthonormal Fourier basis of `H_N`; `P_N` selects precisely the block `k=0,...,N-1`.

Write

```text
sinc_pi(x)=sin(pi x)/(pi x).
```

For `r_j=j-1/2`, direct integration gives

```text
|<nu_y,nu_(y_(j,N))>|^2
 =sinc_pi(r-r_j)^2.
```

By Parseval, the leakage outside the selected block is

```text
L_N(r)
 =1-sum_(j=1)^N sinc_pi(r-j+1/2)^2

 =sum_(k<0 or k>=N)
   sinc_pi(r-k-1/2)^2.
```

Because

```text
sin^2(pi(r-k-1/2))=cos^2(pi r),
```

this has the exact form

```text
L_N(r)
 =cos^2(pi r)/pi^2
  [
    sum_(m>=0) 1/(r+m+1/2)^2
    +
    sum_(m>=0) 1/(N-r+m+1/2)^2
  ].
```

Define the missed continuum mass

```text
delta_N
 =1-Tr(P_N B_N).
```

Since `dy=(Delta/N)dr`, the preceding identity yields

```text
delta_N
 =(1/N) integral_0^N L_N(r)dr.
```

For `x>=0`, monotonicity gives the elementary tail estimate

```text
sum_(m>=0) 1/(x+m+1/2)^2
 <=1/(x+1/2)^2+1/(x+1/2).
```

Using `cos^2(pi r)<=1` and symmetry of the two boundary tails,

```text
delta_N
 <=(2/(pi^2 N))
   integral_0^N
   [1/(r+1/2)^2+1/(r+1/2)]dr

 <=(2/(pi^2 N))[2+log(2N+1)].
```

Thus

```text
boxed:
delta_N=O(log N/N).
```

The logarithm is the ordinary accumulation of Fourier leakage from the two hard band edges. No arithmetic input occurs.

## Hilbert--Schmidt control is already strong enough

Using

```text
A_N=P_N/N,
Tr(P_N B_N)=1-delta_N,
```

we obtain

```text
||A_N-B_N||_2^2
 =Tr A_N^2+Tr B_N^2-2Tr(A_N B_N)

 <=1/N+1/N-(2/N)(1-delta_N)

 =2 delta_N/N.
```

Hence

```text
boxed:
||A_N-B_N||_2
 =O(sqrt(log N)/N).
```

At a growing rank this alone would not imply trace-norm convergence, so the `S_1` upgrade needs one more ingredient.

## Ky Fan plus the PL-099 lifting lemma gives trace-norm convergence

Let

```text
beta_1(B_N)>=beta_2(B_N)>=...
```

be the eigenvalues of `B_N`, and define

```text
epsilon_N
 =1-sum_(j=1)^N beta_j(B_N).
```

Ky Fan's variational principle says that the sum of the top `N` eigenvalues is the maximal `Tr(QB_N)` over rank-`N` projections `Q`. Taking the concrete Fourier projection `P_N`,

```text
sum_(j=1)^N beta_j(B_N)
 >=Tr(P_N B_N)
 =1-delta_N.
```

Therefore

```text
boxed:
epsilon_N<=delta_N=O(log N/N).
```

The finite-rank lifting lemma proved in `PL-099` states that for positive trace-one `A,B` with `rank A<=N`,

```text
||A-B||_1
 <=4 sqrt(N)||A-B||_2
   +2[1-sum_(j=1)^N beta_j(B)].
```

Applying it here gives

```text
||A_N-B_N||_1
 <=4 sqrt(2 delta_N)+2 delta_N

 =O(sqrt(log N/N)).
```

Thus

```text
boxed:
||A_N-B_N||_1 ->0.
```

Unlike the strict sub-Nyquist proof in `PL-099`, this endpoint proof does not estimate the midpoint kernel through `1/sin(Delta u/(2N))` near its first pole. It instead uses the exact Fourier orthogonality available only at Nyquist and controls the two omitted Fourier tails directly.

## Spectral and determinant consequences

For positive compact operators, the standard Lidskii--Mirsky eigenvalue inequality gives

```text
sum_j
|lambda_j(A_N)-lambda_j(B_N)|
 <=||A_N-B_N||_1
 ->0.
```

Since `lambda -> log(1+z lambda)` is `z`-Lipschitz on `[0,infinity)` for fixed `z>=0`,

```text
|log det(I+zA_N)-log det(I+zB_N)|
 <=z||A_N-B_N||_1
 ->0.
```

Thus even the full ordinary positive Fredholm determinant fails to distinguish this exact-Nyquist non-arithmetic control from the continuum comparator.

## Prior-art and novelty audit

The structural ingredients are classical Fourier/prolate sampling theory.

- D. Slepian, “Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty—V: The Discrete Case,” *Bell System Technical Journal* **57**(5) (1978), 1371–1430, DOI `10.1002/j.1538-7305.1978.tb02104.x`, develops the discrete prolate/time--frequency limiting theory at the natural sampling scale.
- Z. Zhu, S. Karnik, M. A. Davenport, J. Romberg, M. B. Wakin, “The Eigenvalue Distribution of Discrete Periodic Time-Frequency Limiting Operators,” *IEEE Signal Processing Letters* **25**(1) (2018), 95–99, DOI `10.1109/LSP.2017.2751578`, arXiv `1707.05344`, gives a close modern periodic/DFT prolate analogue and nonasymptotic eigenvalue concentration results.
- The continuous prolate time-bandwidth picture and its transition at dimension `T Delta/(2 pi)` were already audited in `PL-095`--`PL-099` through the classical Landau--Pollak and Landau--Widom theory.

A targeted search found mature discrete, periodic, and continuous prolate theory rather than a zeta- or prime-specific endpoint mechanism. The exact line-specific estimate above is rederived from the Fourier basis, Parseval, Plancherel, Ky Fan, and the already-persisted `PL-099` lifting lemma; no novelty is claimed for Nyquist sampling, discrete prolates, or prolate concentration. Failure to locate this exact normalization in prior wording would not establish novelty.

What is durable here is the **discrimination control** for the Prime-Lattice branch: the single coarse ratio left open by `PL-099` also admits trace-class continuum matching without arithmetic.

## Rational-prime discrimination

The construction depends only on

```text
[A,B], N,
and the exact Nyquist relation T_N Delta=2 pi N.
```

It contains no prime powers, von Mangoldt coefficients, Möbius signs, multiplicative semigroup, Euler product, functional equation, analytic continuation, or zero divisor. Nevertheless it matches the PNT/prolate continuum in `S_1`, ordered spectrum, and positive Fredholm determinant.

Therefore the statement

```text
critical shell covariance
 -> continuum covariance in S_1
```

cannot by itself be evidence of rational-prime structure. Any arithmetic content at this scale must lie in what this matched Fourier cloud erases: microscopic spacing, arithmetic weights/support, excess error or rate relative to an optimal control, a distinguished target, completion, or an indefinite/relative observable.

## Adversarial boundaries

1. **Only the exact Nyquist sequence is proved here.** The result assumes `T_N=2 pi N/Delta` for every `N`. It does not classify arbitrary sequences satisfying only `T_N/N ->2 pi/Delta`; a shrinking near-critical window may have its own behavior.
2. **No prime-power `S_1` convergence is proved.** The actual growing-depth shell can have microscopic spacing defects absent from the midpoint grid. The finding is a matched-control no-go, not a surrogate theorem for primes.
3. **No sharp optimal rate is claimed.** The bound `O(sqrt(log N/N))` is sufficient for trace-norm convergence. The leakage itself is of logarithmic edge type, but no asymptotic constant is needed here.
4. **The weighted/von-Mangoldt comparator is not covered.** A critical weighted Wiener--Hopf control would require its own construction and trace-class estimate.
5. **The super-Nyquist excess remains open.** `PL-098` gives the universal best rank floor above Nyquist, but an arithmetic empirical state may lie farther from the continuum. Subtracting that floor or resolving microscopic spacing is not addressed here.
6. **No analytic continuation or RH input occurs.** The proof is finite Fourier geometry plus elementary operator inequalities. It neither imports nor constrains the Riemann zero divisor.

## Consequence for the finite-ratio `S_1` branch

The non-arithmetic control picture is now sharper:

```text
matched midpoint shell,
T_N/N -> tau < 2 pi/Delta
    -> S_1 transport to the continuum (PL-099);

matched midpoint shell,
T_N = 2 pi N/Delta exactly
    -> S_1 transport to the continuum (PL-100);

any positive N-point trace-one state,
T_N/N -> tau > 2 pi/Delta
    -> universal positive S_1 rank floor (PL-098);

T_N/N -> infinity
    -> universal floor tends to maximal distance 2 (PL-097).
```

Thus the coarse subcritical/critical-versus-supercritical transition is ordinary Fourier rank/sampling geometry, not a rational-prime signature. The surviving arithmetic question is no longer whether the raw covariance can or cannot match the continuum on a given side of Nyquist. It is whether the **prime-specific excess, microscopic discrepancy, weighting, target coupling, or completed observable** carries information that survives the same matched non-arithmetic controls.