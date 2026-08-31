# PL-080 — The sharp logarithmic Gram determinant has a classical Nyquist phase

## Claim

The determinant/lower-edge escape left open by `PL-079` can be classified at its first natural scale. For the unweighted sharp-window Gram matrix on a macroscopic integer band

```text
I_T={n in N : aT<n<=bT},
M_T=|I_T|,

G_T(m,n)
 =(1/T) integral_0^T exp(i t(log m-log n)) dt,
```

put

```text
c_* = 1/(2 pi).
```

Then, away from the critical endpoint `b=c_*`, there is a sharp classical sampling transition.

### Subcritical density: `b<c_*`

There are constants

```text
0<A_(a,b)<=B_(a,b)<infinity
```

such that for all sufficiently large `T`,

```text
A_(a,b) I <= G_T <= B_(a,b) I.
```

Hence the full band has a uniform Riesz lower bound and bounded condition number. Moreover the first logarithmic determinant scale is completely determined by the locally Toeplitz symbol of `PL-079`:

```text
lim_(T->infinity) (1/M_T) log det G_T

 = L(a,b)

 = 1/(2 pi(b-a))
   integral_a^b integral_(-pi)^pi
      log m_x(theta) dtheta dx,
```

where

```text
m_x(theta)
 =2 pi x sum_(ell in Z)
   1_[ -1/(2x),1/(2x) ](theta+2 pi ell).
```

For every nondegenerate band `a<b<c_*`,

```text
-infinity < L(a,b) < 0.
```

### Supercritical density: `b>c_*`

A positive proportion of the empirical spectrum of `G_T` accumulates at zero. Consequently

```text
lambda_min(G_T) -> 0,
cond(G_T) -> infinity,
```

and, more strongly,

```text
boxed:
(1/M_T) log det G_T -> -infinity.
```

Equivalently,

```text
(det G_T)^(1/M_T) -> 0.
```

Thus the determinant decays faster than every fixed exponential `exp(-C M_T)` at this coarse per-site normalization.

The same dichotomy, with the same subcritical determinant limit and the same supercritical collapse, holds after replacing the arithmetic frequencies `log n` by the matched nonmultiplicative control

```text
lambda_n=log(n+theta_0),
0<theta_0<1.
```

Therefore the first lower-frame and logarithmic-determinant transition of the full critical sharp band is **Nyquist/Ingham density geometry**, not rational-prime factorization and not an RH-sensitive spectral effect.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route

```text
unweighted positive-cone characters
+ sharp finite-time window
+ full macroscopic band n~T
+ smallest-eigenvalue / condition-number / per-site determinant
    -> new prime-lattice or RH-sensitive spectral invariant.
```

The exact endpoint `b=c_*`, finer determinant normalizations after the supercritical collapse, arithmetic coefficient weights, and pointed target observables remain outside this no-go.

## Rescaling turns the band into a nonharmonic Fourier family

Scale the observation variable by

```text
u=t/T,
0<=nu<=1,
```

and define

```text
xi_(n,T)=T log n.
```

Then for every coefficient vector `c=(c_n)_(n in I_T)`,

```text
<c,G_T c>
 = integral_0^1
     |sum_(n in I_T) c_n exp(-i xi_(n,T) nu)|^2 dnu.
```

The consecutive rescaled frequency gaps are

```text
xi_(n+1,T)-xi_(n,T)
 =T log(1+1/n).
```

They decrease with `n`. Since the largest index in the band is `bT+O(1)`,

```text
min_(n,n+1 in I_T)
 [xi_(n+1,T)-xi_(n,T)]
 -> 1/b.
```

Thus the only parameter controlling the global separated-frequency lower-frame problem is the local density of the scalar energy levels `T log n` near the upper edge. The prime decompositions of the indices do not enter this gap calculation.

## Ingham gives a uniform lower frame bound when `b<1/(2 pi)`

Classical Ingham theory says that if a strictly increasing real frequency sequence has uniform gap at least `gamma>0`, then on an interval of length `L>2 pi/gamma` the corresponding exponentials satisfy two-sided `ell^2`/`L^2` inequalities, with constants depending only on the strict gap margin.

Assume

```text
b<c_*=1/(2 pi).
```

Then

```text
1/b>2 pi.
```

Choose a fixed number `gamma` with

```text
2 pi<gamma<1/b.
```

For all sufficiently large `T`, every consecutive gap of the finite family `{xi_(n,T):n in I_T}` is at least `gamma`. Applying Ingham on the unit interval gives constants `A,B>0`, independent of `T` and of the coefficient vector, such that

```text
A sum_(n in I_T)|c_n|^2
 <= <c,G_T c>
 <= B sum_(n in I_T)|c_n|^2.
```

Equivalently,

```text
A I<=G_T<=B I.
```

This sharpens the coarse `N/T` operator estimate in `PL-072`: that estimate already gave stability for sufficiently small ratios with an unspecified absolute constant, while the nonharmonic Fourier gap theorem identifies the classical transition value `1/(2 pi)` that also appeared independently in the local prolate symbol of `PL-078`.

The upper inequality itself does not require the strict Nyquist condition; uniform separation is enough. The strict condition is what supplies the positive lower bound.

## The first spectral law then controls the subcritical determinant

`PL-079` proves that the empirical spectral measure of `G_T` converges to the `x`-average of the symbols `m_x`. The only reason that theorem could not directly be tested with `phi(lambda)=log lambda` was the possible approach of eigenvalues to zero.

In the subcritical regime Ingham removes exactly that obstruction: all eigenvalues lie in a common compact interval

```text
[A,B] subset (0,infinity).
```

Hence `log` is a continuous test function on the spectral support, and the `PL-079` first limit law immediately yields

```text
(1/M_T) log det G_T
 =(1/M_T) Tr log G_T

 ->1/(2 pi(b-a))
   integral_a^b integral_(-pi)^pi
      log m_x(theta) dtheta dx.
```

The integral is finite because `m_x` is bounded away from zero for every `x<=b<c_*`.

There is also an elementary local form. Put

```text
r_x=1/(2 pi x),
q_x=floor(r_x),
delta_x=r_x-q_x.
```

Since `x<c_*`, one has `q_x>=1`. The multiplier takes the two values

```text
q_x/r_x,
(q_x+1)/r_x
```

with normalized circle fractions

```text
1-delta_x,
delta_x.
```

Therefore

```text
ell(x)
 =(1-delta_x) log(q_x/r_x)
   +delta_x log((q_x+1)/r_x),

L(a,b)=1/(b-a) integral_a^b ell(x) dx.
```

The local multiplier has mean one because its zeroth Fourier coefficient is `a_0(x)=1`. Concavity of `log` gives

```text
ell(x)<=0,
```

with equality only at the isolated alias points `r_x in N`, where the periodized interval covers the circle with constant multiplicity. Hence every band of positive length satisfies

```text
L(a,b)<0.
```

This is an ordinary nonharmonic/Toeplitz volume loss, not arithmetic cancellation.

## Above Nyquist, `PL-079` forces a macroscopic zero cluster

Assume now

```text
b>c_*.
```

For every

```text
x>c_*,
```

the local symbol is in the no-alias regime of `PL-078`:

```text
m_x(theta) in {0,2 pi x},
```

and its zero set has normalized circle measure

```text
1-1/(2 pi x)>0.
```

Consequently the limiting empirical measure in `PL-079` has an atom at zero of weight

```text
q_0(a,b)
 =1/(b-a)
   integral_(max(a,c_*))^b
     (1-1/(2 pi x)) dx
 >0.
```

Let the eigenvalues of `G_T` be

```text
0<lambda_1(T)<=...<=lambda_(M_T)(T).
```

For every fixed `epsilon>0`, Portmanteau applied to the open interval `(-epsilon,epsilon)` gives

```text
liminf_(T->infinity)
  1/M_T # {j:lambda_j(T)<epsilon}
 >=q_0(a,b).
```

In particular,

```text
lambda_1(T)->0.
```

Since the diagonal of `G_T` is identically one,

```text
Tr G_T=M_T,
```

so `lambda_max(G_T)>=1`. Thus

```text
cond(G_T)->infinity.
```

This is stronger than merely observing a local nearly-collinear pair: a **positive proportion** of the global spectrum approaches the lower edge once a macroscopic part of the band lies above the Nyquist density.

## The per-site determinant necessarily collapses super-exponentially

The same zero mass gives a determinant statement without invoking a strong Szego theorem at a singular symbol.

`PL-079` supplies a uniform spectral upper bound

```text
lambda_j(T)<=C_b
```

for all sufficiently large `T`. Fix `epsilon>0`. By the previous section, for large `T` at least `(q_0/2)M_T` eigenvalues are below `epsilon`. Therefore

```text
1/M_T log det G_T
 =1/M_T sum_j log lambda_j(T)

 <=(q_0/2) log epsilon
   +(1-q_0/2) log C_b.
```

Now first let `T->infinity` and then let `epsilon->0`. The right-hand side can be made arbitrarily negative, so

```text
lim_(T->infinity)
  1/M_T log det G_T
 =-infinity.
```

No interchange of `log` with a singular limiting measure is being assumed. The argument uses only the already-proved positive zero mass and a uniform upper spectral bound.

This does **not** determine the correct finer decay scale. Classical prolate/Toeplitz gap determinants often have much stronger `M^2`-scale behavior, and variable-coefficient Kac--Murdock--Szego determinant asymptotics can be sensitive to indexing even when the first spectral law is unchanged. The present result only closes the ordinary per-site logarithmic determinant scale.

## The shifted non-arithmetic control has the same phase

Replace the frequencies by

```text
xi_(n,T)^(theta)
 =T log(n+theta_0),
0<theta_0<1.
```

Their consecutive gaps satisfy

```text
T log((n+1+theta_0)/(n+theta_0))
 ->1/b
```

uniformly at the upper macroscopic edge. Hence the same Ingham argument gives a uniform lower frame bound when `b<c_*`.

`PL-079` already proves that this shifted system has exactly the same limiting empirical spectral law as the rational-integer system. Therefore the same continuous-`log` argument gives the identical finite subcritical determinant limit `L(a,b)`, while the same positive zero atom gives

```text
lambda_min->0,
cond->infinity,
(1/M_T)log det->-infinity
```

when `b>c_*`.

This control is decisive for the line mandate. The transition survives after the multiplicative norm map `n=product p^(v_p(n))` has been replaced by a smooth nonmultiplicative sampling sequence. It is therefore a property of frequency density under a finite observation window, not of prime-coordinate arithmetic.

## Prior art and novelty audit

The two structural ingredients are classical.

- **A. E. Ingham**, “Some trigonometrical inequalities with applications to the theory of series,” *Mathematische Zeitschrift* **41** (1936), 367--379, is the classical nonharmonic Fourier gap theorem. In the normalization used here, a gap `gamma` gives a two-sided frame inequality on intervals of length strictly larger than `2 pi/gamma`.
- **H. J. Landau**, “Necessary density conditions for sampling and interpolation of certain entire functions,” *Acta Mathematica* **117** (1967), 37--52, DOI `10.1007/BF02395039`, is the classical density/Nyquist counterpart: stable interpolation of band-limited functions is constrained by Beurling density. For the rescaled logarithmic frequencies, the local frequency density near `n~xT` is exactly `x`, so `x=1/(2 pi)` is the ordinary unit-interval Nyquist density.
- The locally Toeplitz first spectral law and the shifted-control comparison are the canonical `PL-079` result; their Kac--Murdock--Szego prior-art audit need not be repeated here.

No novelty is claimed for Ingham inequalities, Beurling--Landau density, Nyquist sampling, or the inference `Tr log=(log det)`. The line-specific durable result is the collision between those classical theorems and the exact `PL-079` logarithmic Gram family: the lower-frame transition and the **entire first per-site determinant phase** on either side of `1/(2 pi)` are already sampling geometry and fail the rational-prime discrimination test.

## Adversarial boundaries

1. **The exact endpoint `b=1/(2 pi)` is not classified.** Ingham's strict gap margin disappears there, while the `PL-079` limiting measure has no positive zero atom because the critical point has zero macroscopic measure. A vanishing fraction of edge eigenvalues can therefore control the determinant without appearing in the first spectral law.
2. **No fine supercritical determinant asymptotic is claimed.** The result proves only `(1/M_T)log det G_T->-infinity`. It does not identify an `M_T^2`, `M_T log M_T`, or other renormalized scale, a Widom constant, or a strong KMS correction. Such finer quantities may be indexing-sensitive.
3. **Extreme-rate information remains open.** The supercritical result forces `lambda_min->0` but gives no sharp decay rate for the smallest eigenvalue, no complete extreme-eigenvalue law, and no pseudospectral statement.
4. **Arithmetic weights are outside the no-go.** Diagonal weights such as `mu(n)`, `Lambda(n)n^(-1/2)`, or a completion-dependent vector change the pointed/weighted operator. `PL-073`--`PL-077` explain why the first such escapes land in support, shifted-correlation, or prime/zero pair-correlation problems.
5. **Pointed observables remain outside.** A determinant or condition number discards a distinguished target and eigenvector geometry. Nyman/Bagchi-type approximation is not ruled out.
6. **There is no analytic continuation here.** Everything is a finite Fourier statement for the scalar energies `log n`; no Euler product, functional equation, zero divisor, or critical-strip continuation is used.

## Consequence for the sharp finite-horizon branch

Together, `PL-072`, `PL-078`, `PL-079`, and this finding now give a classical hierarchy for the unweighted sharp positive-cone Gram geometry:

```text
N=o(T)
    -> asymptotic orthogonality (Montgomery--Vaughan);

local n~xT
    -> prolate/Nyquist symbol (Slepian);

full macroscopic aT<n<=bT
    -> locally Toeplitz empirical law (KMS/GLT);

b<1/(2 pi)
    -> uniform Riesz stability
       + finite classical per-site log determinant;

b>1/(2 pi)
    -> macroscopic zero cluster
       + lower-frame collapse
       + per-site log determinant -> -infinity.
```

Every item in this unweighted hierarchy is reproduced by the shifted control `log(n+theta_0)`. The viable sharp-window search is therefore narrowed again: it must use the exact critical endpoint, a finer determinant/extreme normalization with a genuine arithmetic discriminator, arithmetic coefficient/target information, or a different construction that couples the prime-coordinate factorization to analytic continuation. Merely observing a condition-number blow-up or determinant collapse in the macroscopic critical band is not evidence of RH-sensitive prime-lattice structure.
