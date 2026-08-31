# PL-079 — The full macroscopic sharp Gram bulk spectrum is a classical locally Toeplitz mixture

## Claim

The global unweighted sharp-window escape left open by `PL-078` can be closed at the level of **empirical eigenvalue distribution**. Although the full macroscopic band `aT<n<=bT` is not one stationary prolate Toeplitz matrix, after an exact diagonal phase gauge its Gram matrix is asymptotically a Kac--Murdock--Szego / locally Toeplitz sequence whose symbol is the slowly varying family of prolate multipliers already identified locally in `PL-078`.

Fix

```text
0<a<b<infinity,
I_T={n in N : aT<n<=bT},
M_T=|I_T|,
```

and let `G_T` be the Gram matrix of the normalized characters

```text
nu_n^(T)(t)=T^(-1/2)n^(-it),
0<=t<=T,
n in I_T.
```

There is an exact diagonal unitary conjugacy from `G_T` to the real symmetric positive matrix

```text
A_T(m,n)=sinc((T/2) log(m/n)),
sinc(u)=sin(u)/u.
```

For `x in [a,b]` and `h in Z`, put

```text
a_h(x)=sinc(h/(2x)).
```

Its Fourier symbol is the periodized interval multiplier from `PL-078`,

```text
m_x(theta)
 =2 pi x sum_(ell in Z)
   1_[ -1/(2x), 1/(2x) ](theta+2 pi ell),
-pi<=theta<=pi.
```

Then for every continuous test function `phi` on a compact interval containing the spectra of `G_T`,

```text
lim_(T->infinity) (1/M_T) Tr phi(G_T)

 =1/(2 pi (b-a))
   integral_a^b integral_(-pi)^pi
      phi(m_x(theta)) dtheta dx.
```

Equivalently, the empirical spectral measure of the **entire macroscopic sharp band** is the `x`-average of the local prolate/aliasing spectral laws of `PL-078`. The curvature of `log n` only makes the local sampling ratio `x=n/T` vary slowly; it does not create a new arithmetic bulk spectrum.

In the clean no-alias regime

```text
a>1/(2 pi),
```

one has, for each `x`,

```text
m_x(theta) in {0,2 pi x}
```

with respective circle fractions

```text
1-1/(2 pi x),
1/(2 pi x).
```

Hence the limiting empirical measure is explicitly

```text
mu_(a,b)
 = [1-log(b/a)/(2 pi (b-a))] delta_0
   + 1_[2 pi a,2 pi b](y)
     dy/(2 pi (b-a)y).
```

The same limiting law is obtained from the matched non-arithmetic control frequencies `log(n+theta_0)`, `0<theta_0<1`. Thus the global **bulk** spectrum fails the line's rational-prime discrimination test just as the fixed local blocks do.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
unweighted positive-cone characters
+ sharp finite-time window
+ full macroscopic band n~T
+ empirical Gram spectrum
    -> new prime-lattice / RH-sensitive global spectral invariant.
```

The negative conclusion is deliberately limited to the empirical eigenvalue distribution. It does not classify extreme eigenvalues, determinant-scale corrections, arithmetic coefficient weightings, pointed target observables, or higher-order statistics whose normalization is sensitive to a vanishing fraction of the spectrum.

## Exact centered Gram matrix

For `m,n in I_T`, with the usual `L^2(0,T)` inner product,

```text
G_T(m,n)
 =(1/T) integral_0^T exp(-it log(n/m)) dt

 =exp(-i(T/2)log(n/m))
   sinc((T/2)log(n/m)).
```

The phase factors split as a diagonal gauge. If

```text
D_T(n,n)=exp(-i(T/2)log n),
```

then, up to the harmless convention of whether the inner product is linear in its first or second argument,

```text
G_T=D_T^* A_T D_T
```

or its conjugate equivalent. In either convention the matrices have exactly the same eigenvalues, and

```text
A_T(m,n)=sinc((T/2)log(m/n))
```

is real symmetric and positive semidefinite because it is the Gram matrix obtained by centering the observation interval to `[-T/2,T/2]`.

Thus no phase information is being discarded in the spectral statement.

## Uniform square-summable diagonal tails

The obstacle to applying the simplest KMS theorem verbatim is that the local Fourier coefficients decay only like `1/|h|`; they need not satisfy the classical absolute-summability hypothesis

```text
sum_h sup_x |a_h(x)| < infinity.
```

For the present Hermitian sequence the weaker square-summable control is enough.

If `m,n in I_T` and `h=m-n`, the mean-value theorem gives

```text
|log(m/n)| >= |h|/(bT+O(1)).
```

Consequently, uniformly in the macroscopic band,

```text
|A_T(m,n)|
 <= min(1,C_b/|h|)
```

for `h!=0` and a constant depending only on `b`. Therefore the diagonals are uniformly square summable:

```text
sup_T (1/M_T)
 sum_(m,n in I_T, |m-n|>H)
 |A_T(m,n)|^2
 =O_b(1/H).
```

This is the key fact allowing the exact sharp sinc tails to be retained while the limiting distribution is obtained from finite-band locally Toeplitz approximants.

## Fejer finite-band approximation

Let

```text
w_H(h)=(1-|h|/(H+1))_+,
```

and form the Fejer-weighted matrix

```text
A_T^(H)(m,n)=w_H(m-n)A_T(m,n).
```

For `|h|<=H`,

```text
1-w_H(h)=|h|/(H+1).
```

Combining this with the preceding `min(1,C_b/|h|)` estimate, and treating the tail `|h|>H` separately, gives the uniform normalized Hilbert--Schmidt estimate

```text
limsup_(T->infinity)
 (1/M_T)||A_T-A_T^(H)||_F^2
 =O_b(1/H).
```

Now keep `H` fixed. Write

```text
x_(m,n)=(m+n)/(2T).
```

For `h=m-n` with `|h|<=H`, uniformly for `m,n in I_T`,

```text
(T/2)log(m/n)
 =h/(2x_(m,n))+O_(a,H)(T^(-2)).
```

Hence `A_T^(H)` is normalized-Hilbert--Schmidt close, as `T->infinity`, to the finite-band KMS matrix

```text
B_T^(H)(m,n)
 =w_H(h)a_h(x_(m,n)).
```

After the affine rescaling of `x in [a,b]` to the unit interval, this is exactly a Hermitian Kac--Murdock--Szego sequence with continuous finite Fourier coefficients. Its symbol is

```text
m_(x,H)(theta)
 =sum_(|h|<=H) w_H(h)a_h(x)e^(ih theta).
```

The First KMS/Szego limit theorem therefore yields

```text
lim_(T->infinity) (1/M_T)Tr phi(B_T^(H))

 =1/(2 pi(b-a))
   integral_a^b integral_(-pi)^pi
     phi(m_(x,H)(theta)) dtheta dx
```

for continuous `phi` on the relevant spectral interval.

## Removing the finite-band cutoff

The coefficients `a_h(x)` are precisely the Fourier coefficients of

```text
m_x(theta)
 =2 pi x sum_ell
   1_[ -1/(2x),1/(2x) ](theta+2 pi ell).
```

Therefore `m_(x,H)` is the Fejer mean of `m_x`. For fixed `x`,

```text
m_(x,H)(theta)->m_x(theta)
```

at every continuity point and in `L^2(T)`. Moreover, for `x in [a,b]`, the covering multiplicity of the periodized interval is uniformly bounded, so both `m_x` and all its Fejer means have a common finite `L^infinity` bound. Dominated convergence then removes `H` on the symbol side.

On the matrix side, Hoffman--Wielandt gives, for bounded Lipschitz `phi`,

```text
| (1/M_T)Tr phi(A_T)
 -(1/M_T)Tr phi(A_T^(H)) |

 <= Lip(phi)
    [(1/M_T)||A_T-A_T^(H)||_F^2]^(1/2)
 =O_b(H^(-1/2))
```

uniformly after `T->infinity`. Since `A_T` is unitarily equivalent to `G_T`, it remains only to note that the spectra of `G_T` are uniformly bounded. Indeed, the Montgomery--Vaughan mean-value estimate already used in `PL-072`, applied to a coefficient vector supported inside `n<=bT+O(1)`, gives

```text
||G_T|| <= 1+C b+o(1).
```

The bounded-Lipschitz convergence therefore extends by uniform approximation to every continuous test function on a common compact spectral interval. This proves the displayed limiting spectral law.

## Explicit no-alias law and sanity checks

Assume `a>1/(2 pi)`. Then for every `x in [a,b]` the interval

```text
[-1/(2x),1/(2x)]
```

fits inside one period. Hence the local multiplier equals `2 pi x` on an arc of length `1/x` and zero elsewhere. Under normalized circle measure, the nonzero value has probability

```text
(1/x)/(2 pi)=1/(2 pi x).
```

Averaging uniformly over the integer band, for which `n/T` tends to Lebesgue measure on `[a,b]`, gives

```text
mu_(a,b)
 =1/(b-a) integral_a^b
   [(1-1/(2 pi x))delta_0
    +(1/(2 pi x))delta_(2 pi x)] dx.
```

Changing variables `y=2 pi x` gives the explicit formula in the claim.

Two checks are immediate. The limiting mean is

```text
integral y dmu_(a,b)(y)=1,
```

matching the exact diagonal identity `Tr G_T=M_T`. The limiting second moment is

```text
integral y^2 dmu_(a,b)(y)=pi(a+b),
```

which is also what the local projection law predicts after averaging `2 pi x` over `x`.

When the band crosses an alias threshold, no new arithmetic effect occurs. Write

```text
r_x=1/(2 pi x),
q_x=floor(r_x),
delta_x=r_x-q_x.
```

The periodized interval covering multiplicity is `q_x` or `q_x+1`, so the local spectral law is supported on

```text
2 pi x q_x,
2 pi x(q_x+1)
```

with circle fractions `1-delta_x` and `delta_x`. The global law is simply the `x`-mixture of these elementary two-point laws.

## Matched non-arithmetic control

Replace the integer frequencies by

```text
lambda_n=log(n+theta_0),
0<theta_0<1.
```

The centered sharp Gram matrix becomes

```text
A_(T,theta_0)(m,n)
 =sinc((T/2)log((m+theta_0)/(n+theta_0))).
```

For fixed `h=m-n` and `x=(m+n)/(2T)`, the same expansion gives

```text
(T/2)log((m+theta_0)/(n+theta_0))
 =h/(2x)+o(1)
```

uniformly on finite diagonals, while the same `O(1/|h|)` tail estimate holds. The entire Fejer/KMS argument therefore produces the identical limiting measure.

This control is stronger than observing that one local block is universal: the **full empirical spectrum across the varying macroscopic ratio `n/T`** is preserved after replacing the rational-integer norm map by a shifted nonmultiplicative sampling sequence. The bulk law consequently cannot detect the prime-coordinate factorization of `n`.

## Prior-art and novelty audit

The spectral-distribution mechanism is classical variable-coefficient Toeplitz theory, not a new zeta operator.

- **Alain Bourget, Allen Alvarez Loya, Tyler McMillen**, “Spectral asymptotics for Kac--Murdock--Szego matrices,” *Japanese Journal of Mathematics* **13** (2018), 67--107, DOI `10.1007/s11537-018-1640-2`, arXiv:1610.00084. Their survey records the original Kac--Murdock--Szego generalized Toeplitz matrices, the First Szego limit law for the empirical eigenvalue distribution, Trotter's Riemann-integrable extension, and the later locally Toeplitz/GLT framework. It also emphasizes that alternative diagonal sampling with mesh tending to zero preserves the first-order eigenvalue distribution while determinant asymptotics can be highly indexing-sensitive.
- **David Slepian**, “Prolate Spheroidal Wave Functions, Fourier Analysis, and Uncertainty--V: The Discrete Case,” *Bell System Technical Journal* **57**(5) (1978), 1371--1430, DOI `10.1002/j.1538-7305.1978.tb02104.x`, is the classical prolate/DPSS anchor already used in `PL-078` for each frozen local symbol.

The simple classical KMS theorem is normally stated under absolute summability of Fourier diagonals. The exact sinc symbol here has only `1/|h|` decay. The line-specific derivation above therefore does not silently invoke that theorem outside its hypotheses: Fejer truncation reduces to finite-band KMS matrices, the exact sharp tails are uniformly negligible only in **normalized Hilbert--Schmidt norm**, and Hoffman--Wielandt transfers the resulting first-order empirical spectral law.

No claim of novelty is made for KMS/locally Toeplitz spectral asymptotics, Fejer approximation, Hoffman--Wielandt, or the prolate multiplier. The durable line-specific result is the collision audit with the exact logarithmic Gram family: the macroscopic curvature escape explicitly left open in `PL-078` still classicalizes at the bulk spectral-distribution level.

## Adversarial boundaries

The conclusion must not be extended beyond what the first spectral law controls.

1. **Bulk distribution is weaker than extreme spectrum.** A perturbation affecting `o(M_T)` eigenvalues is invisible to the empirical measure but may change the smallest/largest eigenvalues, condition number, pseudospectral features, or a distinguished low-dimensional sector.
2. **Determinants are explicitly outside the argument.** KMS theory itself warns that determinant asymptotics can be sensitive to diagonal indexing even when the first eigenvalue distribution is unchanged. Here the limiting symbol also has zero regions in the no-alias regime, so a naive `integral log m_x` argument is singular. No determinant or Fredholm invariant is claimed.
3. **Arithmetic weights are outside the no-go.** Replacing the bare characters by coefficients such as `mu(n)`, `Lambda(n)n^(-1/2)`, or a completion-dependent vector changes the pointed/weighted operator. `PL-074`--`PL-077` show that these routes feed into additive correlations, short-interval variance, or zero pair-correlation theory; the present result does not identify all such weighted global spectra.
4. **A target-relative observable may survive.** The empirical spectrum discards eigenvectors and any fixed target. Nyman/Bagchi-type approximation is therefore not ruled out by this bulk law.
5. **No analytic continuation occurs.** The theorem is a finite-time Fourier statement. Its limit contains no functional equation, zero divisor, Euler-product continuation, or critical-line input.
6. **No hidden rational-prime discrimination is present at first order.** The shifted control `log(n+theta_0)` has the same law. Any proposed RH mechanism based only on this empirical spectrum therefore fails before Helson or Beurling controls are even needed.

## Consequence for the finite-horizon branch

The unweighted sharp positive-cone Gram geometry is now classified at both local and global first-order spectral scales:

```text
fixed window around n~xT
    -> prolate / periodized-interval Toeplitz spectrum (`PL-078`);

full macroscopic band aT<n<=bT
    -> x-mixture of the same local symbols (this finding).
```

Thus the slow curvature of `log n` does not rescue a Riemann-specific **bulk** spectral phase at the critical `N~T` resolution. A useful continuation of the sharp finite-horizon branch must use information discarded by the limiting empirical measure: extreme spectral scales, determinant-scale corrections with a genuine arithmetic discriminator, a distinguished arithmetic target/weight, or another higher-order observable that survives the line's existing correlation, Helson, and Beurling controls.