# PL-101 — Near-critical Nyquist midpoint sampling remains trace-class universal

## Claim

The shrinking near-Nyquist window left open by `PL-100` is also non-arithmetic. Keep the midpoint cloud of `PL-099`--`PL-100`, but allow the observation time to approach the Nyquist value from **either side at an arbitrary rate**.

Fix

```text
A<B,
Delta=B-A,
m=(A+B)/2,
```

and, for each `N`, let

```text
y_(j,N)=A+(j-1/2)Delta/N,
1<=j<=N.
```

For any positive observation times `T_N`, define the dimensionless Nyquist ratio

```text
r_N=T_N Delta/(2 pi N).
```

On

```text
H_(T_N)=L^2([0,T_N],dt/T_N),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

put

```text
A_N=(1/N)sum_(j=1)^N P_(y_(j,N)),

B_N=(1/Delta)integral_A^B P_y dy.
```

Both are positive trace-one operators and `rank A_N<=N`. If

```text
boxed:
r_N -> 1,
```

with no assumption on the rate or on the side of approach, then

```text
boxed:
||A_N-B_N||_(S_1) ->0.
```

More precisely, after the unitary rescaling `t=T_N x` to `L^2([0,1],dx)`, there is an absolute constant `C` such that, whenever `1/2<=r<=3/2`,

```text
boxed:
||A_(N,r)-B_(N,r)||_(S_2)^2
 <=C[(r-1)_+/N + log(eN)/N^2].
```

Combining this with the finite-rank lifting lemma of `PL-099` gives

```text
||A_(N,r)-B_(N,r)||_(S_1)
 <=C sqrt((r-1)_+ + log(eN)/N)
   +2 epsilon_(N,r),
```

where

```text
epsilon_(N,r)
 =1-sum_(j=1)^N beta_j(B_(N,r))
```

is the continuum prolate trace lying below the top `N` eigenvalues. The Landau--Widom concentration already used in `PL-098` implies

```text
r_N->1  =>  epsilon_(N,r_N)->0,
```

so the trace-norm convergence follows.

Consequently, for `r_N->1`, the ordered eigenvalue lists converge in `ell^1`, and for every fixed bounded `z>=0`,

```text
log det(I+zA_N)-log det(I+zB_N)->0.
```

Thus **no shrinking critical window around the coarse Nyquist ratio is an arithmetic discriminator merely because it approaches from below, lands exactly at Nyquist, or approaches from slightly above**. A completely non-arithmetic midpoint cloud tracks the same PNT/prolate continuum in `S_1` throughout every sequence with `r_N->1`.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
near-critical finite-ratio shell covariance,
r_N=T_N Delta/(2 pi N)->1,
+ raw S_1 convergence / ordered-spectrum convergence /
  positive Fredholm-determinant convergence
    -> rational-prime-specific or RH-sensitive evidence by itself.
```

This does **not** prove the corresponding trace-norm convergence for the actual prime-power shell. It closes the matched-control question left explicitly open by `PL-100`: an arbitrary shrinking near-critical ratio does not create a new coarse spectral phase that is absent from non-arithmetic Fourier sampling.

## 1. Dimensionless midpoint and continuum kernels

Rescale `t=T_N x`, so all operators act on

```text
H=L^2([0,1],dx).
```

For a fixed dimensionless ratio

```text
r=T Delta/(2 pi N),
```

the midpoint and continuum kernels depend on `d=x-x'` and, after removing the common harmless phase `exp(iTm d)`, are

```text
K_(N,r)^(mid)(d)
 =sin(pi r N d)/[N sin(pi r d)],

K_(N,r)^(cont)(d)
 =sin(pi r N d)/(pi r N d).
```

Every apparent singularity is understood by continuous extension. Their difference is therefore

```text
D_(N,r)(d)
 =sin(pi r N d)/N
  [1/sin(pi r d)-1/(pi r d)].
```

The Hilbert--Schmidt norm is exactly

```text
||A_(N,r)-B_(N,r)||_2^2
 =2 integral_0^1 (1-d)|D_(N,r)(d)|^2 dd.
```

For fixed `r<1`, `PL-099` controlled this by staying uniformly away from the first pole of `1/sin(pi r d)`. At `r=1`, `PL-100` instead used exact Fourier orthogonality. The point here is that the numerator cancels the same apparent pole strongly enough to obtain one estimate uniform across a shrinking neighborhood of `r=1`.

## 2. The only near-critical alias singularity has vanishing weighted mass

Assume

```text
1/2<=r<=3/2
```

and set

```text
x=pi r d.
```

Then `0<=x<=pi r`, so the only nonzero singular point of `csc x` that can enter the integration range is `x=pi`. Away from fixed neighborhoods of `0` and `pi`,

```text
|1/sin x-1/x|<=C,
```

and the contribution to the squared Hilbert--Schmidt norm is `O(N^(-2))`. Near `x=0`,

```text
1/sin x-1/x=O(x),
```

so the same bound holds.

Near `x=pi`, write

```text
u=x-pi.
```

For sufficiently small fixed `|nu|`,

```text
|1/sin x-1/x|<=C/|nu|,
```

while the integer `N` gives the exact cancellation

```text
|sin(Nx)|=|sin(Nnu)|
 <=min(1,N|nu|).
```

Hence the continuously extended kernel difference satisfies

```text
|D_(N,r)|^2
 <=C min(1,1/(N^2 nu^2)).
```

The triangular Hilbert--Schmidt weight becomes

```text
1-d
 =1-x/(pi r)
 =[pi(r-1)-nu]/(pi r).
```

There are two cases.

### Subcritical side `r<=1`

Put `delta=pi(1-r)>=0`. The integration range stops at

```text
nu<=-delta,
```

and the triangular weight is bounded by `C|nu|`. Therefore the near-pole contribution is bounded by

```text
C integral_delta^c
  u min(1,1/(N^2u^2)) du
 <=C log(eN)/N^2,
```

uniformly in `delta`. This remains valid even when the endpoint approaches `pi` much faster than any prescribed function of `N`; there is no hidden rate condition on `1-r`.

### Supercritical side `r>=1`

Put

```text
delta=pi(r-1)>=0.
```

Now the integration passes through `x=pi`. In the near-pole region the triangular weight is at most `C(delta+|nu|)`, so

```text
integral
 (delta+|nu|)
 min(1,1/(N^2nu^2)) dnu

 <=C[delta/N + log(eN)/N^2].
```

The first term is the narrow first alias lobe: its height can be order one, but its width is `O(1/N)` and its triangular mass is proportional to the super-Nyquist excess `r-1`.

Combining the regular, zero, and first-alias regions gives

```text
boxed:
||A_(N,r)-B_(N,r)||_2^2
 <=C[(r-1)_+/N + log(eN)/N^2].
```

This estimate is the key distinction from a crude uniform kernel bound. Above Nyquist the midpoint kernel really does develop an order-one alias peak, so `sup|D|` does not tend to zero. What vanishes in a shrinking critical window is its **weighted Hilbert--Schmidt mass**.

## 3. Prolate concentration upgrades the estimate to trace norm

Let

```text
beta_1>=beta_2>=...
```

be the eigenvalues of the continuum comparator `B_(N,r)`, and define

```text
epsilon_(N,r)
 =1-sum_(j=1)^N beta_j.
```

The lifting lemma proved in `PL-099` applies to every positive trace-one `A,B` with `rank A<=N`:

```text
||A-B||_1
 <=4 sqrt(N)||A-B||_2
   +2[1-sum_(j=1)^N beta_j(B)].
```

Using the preceding Hilbert--Schmidt estimate gives

```text
boxed:
||A_(N,r)-B_(N,r)||_1
 <=C sqrt((r-1)_+ + log(eN)/N)
   +2 epsilon_(N,r).
```

The continuum operator is the normalized prolate time-band limiting operator with time-bandwidth dimension

```text
W=rN.
```

`PL-098`, via the classical Landau--Pollak/Landau--Widom concentration theorem, established for every finite limiting ratio that

```text
sum_(j=1)^N beta_j
 ->min(1,1/r_lim).
```

In particular, whenever

```text
r_N->1,
```

one has

```text
epsilon_(N,r_N)->0.
```

The first term in the trace-norm bound also tends to zero, because

```text
(r_N-1)_+->0
```

and `log N/N->0`. Therefore

```text
boxed:
||A_(N,r_N)-B_(N,r_N)||_1->0.
```

No scale such as

```text
|r_N-1| << 1/log N,
|r_N-1| << 1/sqrt(N),
or |r_N-1| << 1/N
```

is required.

## 4. Ordered spectrum and positive determinants remain universal

For positive compact operators, the Lidskii--Mirsky eigenvalue inequality gives

```text
sum_j
|lambda_j(A_N)-lambda_j(B_N)|
 <=||A_N-B_N||_1
 ->0.
```

For fixed `z>=0`, the function

```text
lambda ->log(1+z lambda)
```

is `z`-Lipschitz on the positive half-line, so

```text
|log det(I+zA_N)-log det(I+zB_N)|
 <=z||A_N-B_N||_1
 ->0.
```

Thus neither the entire ordered positive spectrum nor the ordinary positive Fredholm determinant creates an arithmetic invariant merely by tuning the observation horizon into an arbitrarily thin neighborhood of the Nyquist ratio.

## 5. Prior-art and novelty audit

Every structural ingredient belongs to classical sampling and time--frequency limiting theory.

- Landau--Pollak identify the effective time-bandwidth dimension of the continuous concentration operator.
- Landau--Widom give the asymptotic prolate eigenvalue distribution and logarithmic transition width used in `PL-098` and again here only through the already-established top-`N` trace concentration.
- Slepian's discrete prolate theory is the classical setting for equally spaced finite Fourier samples and the Nyquist transition used in `PL-099`--`PL-100`.
- Kadec/nonharmonic-Fourier stability theory is nearby prior art for perturbations of exponential bases, but it is not load-bearing here: the present midpoint cloud changes the observation ratio rather than perturbing individual nodes, and the proof above comes directly from the exact geometric-sum kernel.

A targeted literature check around prolate transition width, near-Nyquist exponential sampling, discrete prolates, and trace/rank approximation found mature classical sampling/frame theory rather than a prime- or zeta-specific near-critical mechanism. No novelty is claimed for Nyquist aliasing, prolate concentration, the geometric-sum kernel, or Schatten interpolation estimates.

The durable line-specific information is the closure of the precise discrimination gap left by `PL-100`: **even an arbitrarily tuned shrinking window around the critical time-bandwidth ratio admits an explicit non-arithmetic `S_1` control.** Failure to find this exact normalization stated verbatim in the literature is not treated as a novelty claim.

No `SOURCES.md` update is needed: the load-bearing Landau--Pollak, Landau--Widom, and Slepian anchors are already recorded or cited in `PL-098`--`PL-100`; this finding uses no new external theorem beyond that audited corpus.

## 6. Rational-prime and Beurling discrimination

The midpoint cloud depends only on

```text
[A,B], N, T_N.
```

It has no prime powers, multiplication law, von Mangoldt or Möbius coefficients, Euler product, functional equation, analytic continuation, or zeta zero divisor. It can equally be viewed as a matched generalized-frequency control.

Nevertheless, whenever its macroscopic observation ratio satisfies

```text
T_N Delta/(2 pi N)->1,
```

it converges to the same PNT/prolate continuum comparator in trace norm, ordered spectrum, and positive Fredholm determinant.

Therefore a candidate arithmetic signal at near-critical Nyquist scale must use information this control omits: **microscopic prime-power spacing, arithmetic weights/support, excess over the matched control or universal rank floor, a distinguished target, completion, or an indefinite/relative coupling.** Merely tuning the coarse observation ratio ever more precisely to Nyquist cannot create rational-prime rigidity.

## 7. Adversarial boundaries

1. **This is a matched-control theorem, not a prime-power theorem.** No `S_1` convergence of the actual prime-power shell is asserted when `r_N->1`; that remains a question about its microscopic frequency discrepancy.
2. **A fixed super-Nyquist ratio is different.** If `r_N->r>1`, `PL-098` gives a strictly positive universal rank floor `2(1-1/r)`. The present convergence uses essentially that the supercritical excess itself tends to zero.
3. **Rates or renormalized excess can still carry information.** The result proves unscaled `S_1` convergence. A rescaling by `|r_N-1|`, by a microscopic spacing scale, or subtraction of a matched-control contribution is not classified here.
4. **The weighted/von-Mangoldt critical comparator is not covered.** The theorem is for the unweighted trace-one covariance. The weighted Wiener--Hopf analogue would need its own trace-tail and kernel analysis.
5. **Hard-edge observables remain outside the no-go.** Inverse eigenvalues, condition numbers, smallest singular values, target-relative Schur complements, or indefinite completed forms are not controlled by trace-norm convergence of the positive covariance.
6. **No analytic continuation or zero information enters.** The proof is finite Fourier geometry plus classical prolate concentration. It neither extends the Euler product nor constrains the Riemann zero divisor.
7. **No mathematical priority claim is made.** The estimate is stored because it materially closes a Prime-Lattice branch boundary, not because its sampling-theoretic ingredients are asserted to be new.

## 8. Consequence for the finite-ratio `S_1` branch

The coarse matched-control phase is now closed around Nyquist:

```text
midpoint control,
r_N->r<1
    -> S_1 continuum matching (PL-099);

midpoint control,
r_N=1 exactly
    -> S_1 continuum matching (PL-100);

midpoint control,
r_N->1 from either side at any rate
    -> S_1 continuum matching (PL-101);

any positive N-point state,
r_N->r>1
    -> universal positive S_1 rank floor (PL-098);

r_N->infinity
    -> universal floor tends to maximal distance 2 (PL-097).
```

Accordingly, the surviving arithmetic question is not a hidden coarse Nyquist edge. It is whether the **actual rational-prime excess over these matched Fourier/prolate controls**, or a weighted/target-relative/completed observable that they do not reproduce, carries structure relevant to zeta.