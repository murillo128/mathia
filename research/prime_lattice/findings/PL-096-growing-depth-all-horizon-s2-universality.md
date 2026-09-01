# PL-096 — Growing-depth coherent Grams are Hilbert--Schmidt universal at every observation horizon

## Claim

The inverse-PNT-error horizon left open by `PL-095` is a barrier for its **trace-norm transport estimate**, but it is not a genuine transition for the `1/N_X`-scaled coherent spectrum. In the whole first growing-depth range, the empirical prime-power covariance remains uniformly Hilbert--Schmidt close to the deterministic continuum PNT geometry for **every** observation horizon `T>0`.

Keep the notation of `PL-095`:

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

and, along sequences with `N_X>0`, let

```text
mu_X=(1/N_X) sum_(n in Q_(X,>=K)) delta_(y_X(n)).
```

Let `nu_X` be the normalized smooth PNT envelope from `PL-095`, and write

```text
delta_X
 =L exp(-c Phi_(L,K))
  +L^2 exp(-L/(2K)),

Phi_(L,K)
 =(L/K)^(3/5)/(log(L/K))^(1/5).
```

Thus `delta_X->0` and `PL-095` gives

```text
||F_(mu_X)-F_(nu_X)||_infinity << delta_X,

||d nu_X/dy-1/Delta||_infinity << 1/K.
```

On

```text
H_T=L^2([0,T],dt/T),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

define, for `j=0,1`,

```text
w_0(y)=1,
w_1(y)=exp(-y),

C_(mu_X,T)^(j)=integral w_j(y) P_y d mu_X(y),

C_T^(j)
 =(1/Delta) integral_A^B w_j(y) P_y dy.
```

The nonzero spectra of `C_(mu_X,T)^(0)` and `C_(mu_X,T)^(1)` are exactly those of

```text
G_(X,T)/N_X
```

and

```text
B_(X,T)/N_X,
```

respectively, with `G` and `B` as in `PL-094`--`PL-095`.

Then

```text
boxed:
sup_(T>0)
||C_(mu_X,T)^(j)-C_T^(j)||_(S_2)
 <<_(a,b)
  1/K + delta_X^(1/3)
 ->0,

j=0,1.
```

Consequently, after arranging eigenvalues decreasingly and padding by zeros,

```text
boxed:
sup_(T>0)
[
 sum_r |
   lambda_r(G_(X,T)/N_X)-lambda_r(C_T^(0))
 |^2
]^(1/2)
 ->0,
```

and

```text
boxed:
sup_(T>0)
[
 sum_r |
   lambda_r(B_(X,T)/N_X)-lambda_r(C_T^(1))
 |^2
]^(1/2)
 ->0.
```

The same all-horizon closure holds for the fixed positive Fredholm determinants. For every fixed `Z<infinity`,

```text
boxed:
sup_(T>0)
sup_(0<=z<=Z)
|
 log det(I+z B_(X,T)/N_X)
 -log det(I+z C_T^(1))
|
 ->0.
```

There is an analogous statement with `B,C^(1)` replaced by `G,C^(0)`.

In particular, for **every** horizon family `T_X->infinity`, with no relation between `T_X` and the PNT remainder,

```text
boxed:
||B_(X,T_X)/N_X|| ->0,
```

and, for fixed `z>=0`,

```text
boxed:
log det(I+z B_(X,T_X)/N_X)
 -> z/Delta*(1/a-1/b).
```

For the unweighted Gram,

```text
||G_(X,T_X)/N_X|| ->0,

log det(I+z G_(X,T_X)/N_X)->z.
```

Under either depth hypothesis of `PL-093`,

```text
K=o(sqrt(log X))
```

or

```text
K/sqrt(log X)->alpha in (0,infinity),
```

the uniform trace-norm equivalence

```text
||K^2 A_(X,T)/N_X-B_(X,T)/N_X||_(S_1)->0
```

transfers all of these coherent-scale conclusions to the naturally von-Mangoldt half-weighted Gram `K^2 A_(X,T)/N_X`.

Thus merely pushing the observation time through or beyond inverse PNT accuracy does **not** rescue a rational-prime-specific coherent outlier or positive fixed-`z` Fredholm determinant. The surviving information carriers are narrower: `S_1`-fine spectral mass not controlled by `S_2`, the unscaled hard edge/inverse statistics, a distinguished arithmetic target, an indefinite completed coupling, or a different depth regime.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-HARMONIC-ANALYSIS + DECISIVE-NEGATIVE` for the route

```text
growing prime-power depth K=O(sqrt(log X))
+ first K^2 von-Mangoldt repair / envelope Gram
+ arbitrary observation horizon T>0
+ 1/N_X coherent eigenvalue scale
+ fixed positive Fredholm determinant det(I+z A/N_X)
    -> a rational-prime-specific or RH-sensitive phase.
```

No novelty is claimed for the sinc/Fejer kernel identities, Hilbert--Schmidt covariance calculus, or elementary determinant estimates used below. The line-specific contribution is that the PNT discrepancy estimate already stored in `PL-095` closes the coherent spectral branch at **all** horizons once the correct Schatten topology is used.

## Local mass control survives beyond inverse PNT resolution

The key point is that the CDF estimate in `PL-095` gives more than low-frequency Wasserstein transport. Since `nu_X` has uniformly bounded density on the fixed interval `[A,B]`, every interval `I subset [A,B]` satisfies

```text
nu_X(I) <<_(a,b) |I|.
```

The Kolmogorov discrepancy then gives

```text
boxed:
mu_X(I)
 <<_(a,b) |I|+delta_X.
```

Indeed, for `I=(u,v]`,

```text
mu_X(I)
 =F_(mu_X)(v)-F_(mu_X)(u)

 <=F_(nu_X)(v)-F_(nu_X)(u)
   +2||F_(mu_X)-F_(nu_X)||_infinity.
```

This estimate does **not** say that the atomic prime-power measure becomes absolutely continuous below scale `delta_X`. It only says that no interval can carry more than its continuum mass plus `O(delta_X)`. That weak local statement is nevertheless enough for Hilbert--Schmidt control because the squared finite-time character kernel is integrable.

## The squared character kernel is an integrable approximate identity

For `r=y-z`,

```text
<nu_y,nu_z>
 =(1/T) integral_0^T exp(i t r)dt
 =exp(iTr/2) sinc(Tr/2),
```

so

```text
K_T(r)
 =|<nu_y,nu_z>|^2
 =sinc^2(Tr/2)
 <=min(1,4/(T^2 r^2)).
```

For `T>=1`, fix `y` and split the `z`-integral into

```text
|y-z|<=1/T
```

and dyadic annuli

```text
2^j/T<|y-z|<=2^(j+1)/T.
```

The local-mass estimate gives

```text
mu_X(|y-z|<=R)
 <<R+delta_X.
```

On the `j`-th annulus the kernel is `O(4^(-j))`. Hence

```text
integral K_T(y-z) d mu_X(z)

 << 1/T+delta_X
    +sum_(j>=0)
       4^(-j)(2^j/T+delta_X)

 << 1/T+delta_X.
```

Integrating once more in `y`, and using that `w_1(y)=exp(-y)` is bounded above and below on the fixed shell, yields

```text
boxed:
Tr[(C_(mu_X,T)^(j))^2]
 =||C_(mu_X,T)^(j)||_(S_2)^2
 <<_(a,b) 1/T+delta_X,

T>=1,
quad j=0,1.
```

For the absolutely continuous uniform comparator the same calculation, now without the discrepancy term, gives

```text
boxed:
||C_T^(j)||_(S_2)^2
 <<_(a,b)1/T,

T>=1.
```

This is the mechanism that removes the apparent inverse-PNT barrier. At very long times one does not need to transport individual shell points to the continuum accurately: both positive covariance operators have already dispersed their trace over enough almost-orthogonal time-frequency modes that their Hilbert--Schmidt mass is small.

## Stitching short and long horizons gives a uniform `S_2` bound

`PL-095` already proves, uniformly in `T`,

```text
||C_(mu_X,T)^(0)-C_T^(0)||_(S_1)
 <<1/K+T delta_X,
```

and

```text
||C_(mu_X,T)^(1)-C_T^(1)||_(S_1)
 <<1/K+(1+T)delta_X.
```

Use this estimate when

```text
T<=delta_X^(-2/3).
```

Since `||.||_2<=||.||_1`, it gives

```text
||C_(mu_X,T)^(j)-C_T^(j)||_2
 <<1/K+delta_X^(1/3).
```

For

```text
T>delta_X^(-2/3),
```

the long-time estimates above and the triangle inequality give

```text
||C_(mu_X,T)^(j)-C_T^(j)||_2

 <=||C_(mu_X,T)^(j)||_2+||C_T^(j)||_2

 <<sqrt(delta_X+1/T)+T^(-1/2)
 <<delta_X^(1/3).
```

Combining both ranges proves

```text
sup_(T>0)
||C_(mu_X,T)^(j)-C_T^(j)||_2
 <<1/K+delta_X^(1/3).
```

The exponent `1/3` is only the elementary balance between the low-time transport bound `T delta_X` and the high-time integrable-kernel bound `T^(-1/2)`. No sharpness is claimed.

For compact self-adjoint operators, the Hilbert--Schmidt Hoffman--Wielandt/Lidskii--Mirsky inequality gives

```text
sum_r |lambda_r(C)-lambda_r(D)|^2
 <=||C-D||_2^2,
```

which proves the eigenvalue-list statements.

## Exact Fourier-energy interpretation of the residual

There is an exact identity clarifying what information the `S_2` residual could have carried. Put

```text
sigma_X=mu_X-nu_X
```

and

```text
D_(X,T)=integral P_y d sigma_X(y).
```

Then

```text
||D_(X,T)||_2^2
 =integral integral
    |<nu_y,nu_z>|^2
    d sigma_X(y)d sigma_X(z).
```

Since

```text
|<nu_y,nu_z>|^2
 =(1/T) integral_(-T)^T
    (1-|u|/T)
    exp(iu(y-z))du,
```

Fubini gives

```text
boxed:
||D_(X,T)||_2^2
 =(1/T) integral_(-T)^T
   (1-|u|/T)
   |hat(sigma_X)(u)|^2 du.
```

Thus the empirical-versus-PNT covariance residual is exactly a triangularly averaged Fourier energy of the shell-counting discrepancy. This is ordinary Fejer/Wiener harmonic analysis, not a new zeta spectral object. The result above says that, after the `1/N_X` coherent normalization, this entire positive quadratic energy still vanishes uniformly in `T`.

For the shell-weighted covariance the same identity holds with the signed measure

```text
exp(-y) sigma_X(dy).
```

This exact formula is useful as a boundary statement: any future claim that an inverse-PNT-scale coherent covariance suddenly acquires a zero-sensitive `S_2` phase must overcome the uniform estimate above, not merely observe that the `S_1` Wasserstein bound from `PL-095` has stopped being small.

## Positive Fredholm determinants also remain universal

Hilbert--Schmidt convergence alone does not generally control an ordinary Fredholm determinant. Here positivity and the separately controlled trace remove that loophole.

For a positive trace-class operator `C` and `z>=0`,

```text
0
 <=z Tr C-log det(I+zC)
 <=(z^2/2) Tr(C^2).
```

For the weighted empirical covariance,

```text
Tr C_(mu_X,T)^(1)
 =integral exp(-y)d mu_X(y)
```

is independent of `T`. The same CDF/Wasserstein comparison used in `PL-095`, together with the `O(1/K)` smooth-envelope tilt, gives

```text
Tr C_(mu_X,T)^(1)
 =(1/Delta) integral_A^B exp(-y)dy
   +O_(a,b)(delta_X+1/K)

 =(1/Delta)(1/a-1/b)
   +O_(a,b)(delta_X+1/K).
```

The continuum comparator has exactly the limiting trace. For `T>delta_X^(-2/3)`, the preceding `S_2` estimates therefore imply, uniformly for `0<=z<=Z`,

```text
|log det(I+z C_(mu_X,T)^(1))
 -log det(I+z C_T^(1))|

 <<_(a,b,Z)
  1/K+delta_X+1/T

 <<1/K+delta_X^(2/3).
```

For `T<=delta_X^(-2/3)`, the trace-norm determinant estimate of `PL-095` gives the weaker but still vanishing bound

```text
<<1/K+delta_X^(1/3).
```

Hence the determinant comparison is uniform over **all** horizons.

If `T_X->infinity`, both empirical and continuum Hilbert--Schmidt norms tend to zero while their traces converge to the fixed shell mass. Therefore

```text
log det(I+z B_(X,T_X)/N_X)
 ->z/Delta*(1/a-1/b).
```

The corresponding unweighted trace is exactly one, giving the limit `z` for `log det(I+zG/N_X)`.

So the positive coherent determinant has only two asymptotic behaviors: at bounded time it tracks the classical prolate/Wiener--Hopf comparator of `PL-095`; at diverging time its nonlinear spectral content disappears and only the universal trace remains. Crossing inverse PNT accuracy does not create a third arithmetic phase.

## Prior-art and novelty audit

The analytic ingredients are classical and are not claimed as discoveries:

- `|<nu_y,nu_z>|^2` is the continuous sinc-squared/Fejer kernel associated with a finite time window;
- the Fourier-energy identity for a finite signed measure is standard Fourier--Stieltjes covariance calculus and is closely related to Wiener's classical atom-detection lemma;
- Hilbert--Schmidt eigenvalue perturbation and the inequality `x-log(1+x)<=x^2/2` are standard;
- the continuum comparator was already identified in `PL-095` with the classical Slepian--Pollak/Wiener--Hopf time-frequency limiting operator.

A targeted literature search over prime-power logarithmic Gram matrices, Hilbert--Schmidt covariance operators for prime shells, sinc/Fejer energies of prime-power counting measures, and Dirichlet-polynomial Gram spectra did not locate a specialized theorem asserting this all-horizon growing-depth closure. The searches instead return ordinary time-frequency limiting, Fourier--Stieltjes/Wiener measure theory, and standard Dirichlet-polynomial mean-value machinery. Absence from search is not used as novelty evidence.

No new literature anchor is required beyond the quantitative PNT and prolate sources already audited for `PL-095`. The substantive line-specific point is the **stitching**:

```text
low / mesoscopic T
    -> PNT CDF transport from PL-095;

large T
    -> integrability of the squared character kernel
       plus the same local PNT discrepancy;

all T
    -> uniform S_2 spectral universality
       and, by positivity + trace control,
       uniform fixed-z positive determinant universality.
```

This argument uses only coarse PNT-envelope control and therefore survives any Beurling/generalized-prime model with the same shellwise CDF discrepancy. It fails the line's rational-prime discrimination test by construction.

## Adversarial boundaries

1. **`S_2` is not `S_1`.** The result does not prove all-horizon trace-norm convergence of the empirical covariance to the continuum comparator. A large number of individually tiny eigenvalue shifts can have vanishing `ell^2` but nonvanishing `ell^1` mass.
2. **The unscaled hard edge is untouched.** Smallest eigenvalues of `B_(X,T)`, inverse moments, condition numbers, negative powers, and unscaled determinants can amplify effects invisible after division by `N_X`.
3. **The determinant statement uses positivity and fixed `z`.** It does not cover arbitrary determinant regularizations whose parameter grows with `N_X`, nor indefinite completed-Weil determinants.
4. **No target/completion is introduced.** Nyman-type pointed approximation, Schur complements against a distinguished vector, and functional-equation/Weil couplings remain outside this covariance no-go.
5. **The PNT input is still `Re(s)=1`-side information.** Nothing here analytically continues the Euler product or localizes Riemann zeros on `Re(s)=1/2`.
6. **The depth range remains `K=O(sqrt(log X))`.** The local CDF estimate is inherited from `PL-095`; larger depths need their own population and PNT control.
7. **Uniform `S_2` collapse is a coherent-scale statement.** It does not say that the exact prime-power point set is indistinguishable at arbitrarily fine resolution; it says that its positive covariance spectrum after `1/N_X` scaling cannot retain an order-one `S_2` signature.
8. **The Fourier-energy identity is a reduction, not a zero formula.** Rewriting the residual as `|hat(sigma_X)|^2` does not import the explicit formula or convert prime-counting error into a Hilbert--Polya spectrum.

## Consequence for the growing-depth branch

`PL-091`--`PL-095` progressively removed the raw half-weight amplitude, ordinary determinant volume, dimension-normalized bulk spectrum, depth population, one-point shell envelope, and sub-inverse-PNT coherent spectrum as candidate information carriers.

This finding removes the most immediate interpretation of the remaining inverse-PNT escape:

```text
push T past the PNT transport barrier
    -> coherent prime-specific eigenvalue outlier
       or positive Fredholm-determinant phase.
```

That route is closed. At the `1/N_X` scale, fixed extreme eigenvalues are uniformly controlled in `ell^2`, and the fixed positive determinant stays classical at every horizon.

A surviving rational-prime mechanism in this branch must therefore exploit a genuinely finer or different category:

```text
S_1-fine spectral mass beyond S_2;
unscaled hard-edge / inverse observables;
a distinguished arithmetic target;
indefinite completed-Weil coupling;
or a depth regime beyond K=O(sqrt(log X)).
```

Merely increasing the vertical observation time no longer qualifies as a surviving mechanism.