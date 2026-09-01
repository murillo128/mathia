# PL-102 — Critical prime Nyquist `S_1` separation is already forced by the Poisson bulk law

## Claim

The `S_1` question left open by `PL-098`--`PL-101` has a sharp negative answer for the **prime-basis-direction band** at its own global Nyquist ratio, conditional on the same full local Hardy--Littlewood hierarchy used in `PL-085`.

Fix

```text
0<a<b<infinity,
A=log a,
B=log b,
Delta=B-A=log(b/a),
P_X={p prime : aX<p<=bX},
M_X=|P_X|.
```

Choose the critical observation time

```text
c_* = 2 pi (b-a)/Delta,
T_X = c_* X/log X.
```

Since

```text
M_X~(b-a)X/log X,
```

this is exactly asymptotic Nyquist for the logarithmic prime band:

```text
boxed:
T_X Delta/(2 pi M_X) ->1.
```

On

```text
H_X=L^2([0,T_X],dt/T_X),
nu_y(t)=exp(i t y),
P_y=|nu_y><nu_y|,
```

define the empirical prime covariance

```text
A_X=(1/M_X) sum_(p in P_X) P_(log(p/X)).
```

Its nonzero eigenvalues are exactly

```text
lambda_j(A_X)=lambda_j(G_X)/M_X,
```

where `G_X` is the sharp prime Gram of `PL-083`--`PL-085` at `c=c_*`.

The correct first-order PNT continuum comparator is **not** log-uniform for a fixed prime layer. In the coordinate

```text
y=log(p/X),
```

prime counting gives the probability density

```text
w(y)=exp(y)/(b-a),
A<=y<=B,
```

and hence the positive trace-one continuum covariance

```text
B_X=integral_A^B w(y) P_y dy.
```

Assume the full local Hardy--Littlewood hierarchy of `PL-085`. Then there exists a constant

```text
boxed:
kappa_(a,b)>0
```

such that

```text
boxed:
liminf_(X->infinity) ||A_X-B_X||_(S_1)
 >=kappa_(a,b)>0.
```

The lower bound is not an arithmetic rigidity signal. Its witness is precisely the **generic Poisson self-correlation term** already present in the Poisson sinc bulk law of `PL-085`. At critical sampling the prime empirical spectrum and the smooth PNT continuum have second moments differing by exactly `1` on the natural `M_X`-scaled eigenvalue scale:

```text
boxed:
lim (1/M_X) Tr[(M_X A_X)^2]
 =1+Delta(a+b)/(2(b-a)),

lim (1/M_X) Tr[(M_X B_X)^2]
 =  Delta(a+b)/(2(b-a)).
```

Thus a positive critical `S_1` excess can occur even when the whole prime bulk has already been classicalized to a generic local Poisson process. The deterministic midpoint controls of `PL-100`--`PL-101` and the prime cloud therefore sit on opposite sides of an ordinary sampling-regularity distinction:

```text
near-Nyquist regular midpoint cloud
    -> S_1 continuum matching;

critical locally Poisson cloud
    -> positive S_1 spectral separation from the smooth continuum.
```

Consequently, **failure of prime support to converge in trace norm to its PNT continuum at Nyquist is not, by itself, evidence of an RH-sensitive lattice invariant**. It can be caused by classical local prime-gap/Poisson shot noise before analytic continuation or the zeta zero divisor enters.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + CONJECTURAL-INPUT + DECISIVE-NEGATIVE` for the route

```text
prime basis directions
+ sharp finite-time logarithmic covariance
+ global Nyquist ratio T Delta/(2 pi M)->1
+ nonzero raw S_1 distance from the smooth PNT continuum
    -> rational-prime-specific or RH-sensitive evidence by itself.
```

The Hardy--Littlewood input is conjectural and is used only to identify the prime scaled spectral law with the Poisson sinc law of `PL-085`. The continuum calculation and the spectral `S_1` lower-bound mechanism are deterministic.

## 1. The fixed-prime-layer PNT continuum has density `exp(y)` in log coordinate

The shell variable is

```text
p=X exp(y),
A<=y<=B.
```

At first PNT order,

```text
d pi(p)
 ~ dp/log p
 =X exp(y)dy/(log X+y).
```

After division by

```text
M_X~(b-a)X/log X,
```

the normalized density tends uniformly to

```text
w(y)=exp(y)/(b-a).
```

It is normalized because

```text
integral_A^B w(y)dy
 =(b-a)/(b-a)=1.
```

The more literal smooth PNT envelope

```text
w_X(y)
 =C_X exp(y)/(log X+y)
```

with `C_X` chosen to have mass one satisfies

```text
||w_X-w||_(L^1[A,B])=O_(a,b)(1/log X).
```

Since every `P_y` has trace norm one,

```text
||
 integral (w_X-w)P_y dy
||_1
 <=||w_X-w||_1
 =O(1/log X).
```

Hence replacing `w` by the exact normalized `li` envelope changes none of the conclusions below. The comparator is genuinely the PNT continuum, not an arbitrarily selected smooth reference measure.

This also explains why the log-uniform continuum in `PL-094`--`PL-101` does not apply here. That later branch mixes growing prime-power depths `k->infinity`, for which every layer becomes asymptotically flat across a fixed multiplicative shell. A single prime layer `k=1` retains the deterministic Jacobian `exp(y)`.

## 2. `PL-085` supplies the prime scaled eigenvalue law

Let

```text
mu_X=(1/M_X) sum_(j=1)^(M_X)
       delta_(lambda_j(G_X)).
```

Under the full local Hardy--Littlewood hierarchy, `PL-085` proves

```text
boxed:
mu_X -> nu_(a,b,c_*)
in W_2.
```

The limiting law `nu_(a,b,c_*)` is the macroscopic mixture of the unit-intensity Poisson sinc Euclidean-random-matrix bulk law. In particular, `PL-083` gives its second moment:

```text
int lambda^2 d nu_(a,b,c_*)(lambda)
 =1+pi(a+b)/c_*.
```

Substituting

```text
c_*=2 pi(b-a)/Delta
```

gives

```text
boxed:
int lambda^2 d nu_(a,b,c_*)
 =1+Delta(a+b)/(2(b-a)).
```

The leading `1` is the exact diagonal contribution

```text
(1/M_X) sum_(p in P_X) |G_X(p,p)|^2=1.
```

The remaining term is the continuum pair contribution after the Hardy--Littlewood singular series averages to the local Poisson intensity. This is already the matched generic-Poisson mechanism established in `PL-083`--`PL-085`.

No RH or zero information is being inferred from this conditional law. The Hardy--Littlewood hierarchy is an input.

## 3. The smooth continuum has the same pair term but no atomic self term

For the continuum covariance,

```text
Tr(B_X^2)
 =integral_A^B integral_A^B
    w(y)w(z)
    |<nu_y,nu_z>|^2
   dy dz.
```

The character overlap is

```text
|<nu_y,nu_z>|^2
 =sinc^2(T_X(y-z)/2),
```

so the standard Fejer approximate-identity relation gives

```text
T_X Tr(B_X^2)
 ->2 pi integral_A^B w(y)^2dy.
```

This can be checked directly from

```text
integral_R sinc^2(Tu/2)du=2 pi/T
```

plus dominated/approximate-identity convergence on the fixed compact band. Since

```text
2 pi M_X/T_X ->Delta,
```

we obtain

```text
M_X Tr(B_X^2)
 ->Delta integral_A^B w(y)^2dy.
```

Now

```text
integral_A^B w(y)^2dy
 =(1/(b-a)^2)
   integral_A^B exp(2y)dy

 =(b^2-a^2)/(2(b-a)^2)
 =(a+b)/(2(b-a)).
```

Therefore

```text
boxed:
lim M_X Tr(B_X^2)
 =Delta(a+b)/(2(b-a)).
```

Equivalently,

```text
(1/M_X)Tr[(M_XB_X)^2]
 ->Delta(a+b)/(2(b-a)).
```

Comparing with the previous section gives the exact gap

```text
boxed:
lim (1/M_X)Tr[(M_XA_X)^2]
 -lim (1/M_X)Tr[(M_XB_X)^2]
 =1.
```

The same `+1` is the classical self-shot-noise contribution of an empirical point process. It would be present for an ordinary Poisson sample with the same local intensity; it is not tied to multiplication, an Euler product, the functional equation, or zeta zeros.

## 4. The second-moment gap forces a positive trace-class spectral gap

A second-moment difference alone does not generally control `S_1`, because a vanishing fraction of very large eigenvalues can carry quadratic mass. Here `PL-085` supplies enough uniform-integrability information to turn the gap into a rigorous `S_1` lower bound without assuming bounded prime eigenvalues.

Let

```text
h_R(x)
 =x^2,                    0<=x<=R,
 =2Rx-R^2,                x>R.
```

Then

```text
h_R(0)=0,
Lip(h_R)=2R,
0<=h_R(x)<=x^2,
```

and `h_R(x)` increases pointwise to `x^2` as `R->infinity`.

Because `mu_X->nu_(a,b,c_*)` in `W_2`, in particular in `W_1`, every fixed `h_R` satisfies

```text
(1/M_X)Tr h_R(M_XA_X)
 =int h_R d mu_X
 ->int h_R d nu_(a,b,c_*).
```

For the continuum, Plancherel gives the operator bound

```text
||B_X||
 <=(2 pi/T_X)||w||_infinity.
```

Hence

```text
M_X||B_X||
 <=(2 pi M_X/T_X)||w||_infinity
 ->Delta b/(b-a).
```

Choose `R` larger than this limiting bound. Then for all sufficiently large `X`, every eigenvalue of `M_XB_X` lies below `R`, so

```text
(1/M_X)Tr h_R(M_XB_X)
 =(1/M_X)Tr[(M_XB_X)^2]
 ->q_(a,b),
```

where

```text
q_(a,b)=Delta(a+b)/(2(b-a)).
```

On the prime side, monotone convergence and the second-moment identity give

```text
int h_R d nu_(a,b,c_*)
 ↑ q_(a,b)+1
```

as `R->infinity`. We may therefore fix one finite `R` satisfying both the continuum norm condition and

```text
int h_R d nu_(a,b,c_*)
 >q_(a,b)+1/2.
```

Let the decreasing eigenvalue lists of `A_X` and `B_X` be `alpha_j` and `beta_j`, padding the finite-rank `A_X` list by zeros. Since `h_R` is `2R`-Lipschitz,

```text
|sum_j h_R(M_X alpha_j)
 -sum_j h_R(M_X beta_j)|

 <=2R M_X sum_j |alpha_j-beta_j|.
```

The compact self-adjoint Lidskii--Mirsky inequality gives

```text
sum_j |alpha_j-beta_j|
 <=||A_X-B_X||_1.
```

Combining the two displays and passing to `liminf` yields

```text
liminf ||A_X-B_X||_1
 >=[int h_R d nu_(a,b,c_*)-q_(a,b)]/(2R)
 >1/(4R).
```

Thus one may take

```text
boxed:
kappa_(a,b)=1/(4R)>0
```

for any sufficiently large `R` chosen as above. No claim of an optimal constant is made.

The argument is intentionally spectral rather than entrywise: it proves that the ordered eigenvalue lists themselves have a positive `ell^1` separation after undoing the `M_X` scaling. Therefore the lower bound cannot be removed by rotating eigenvectors or changing only the covariance basis.

## 5. Why this is a Poisson sampling obstruction rather than zeta structure

At critical time `T~X/log X`, `PL-083`--`PL-085` already route every fixed-order support-only bulk statistic into the classical Hardy--Littlewood/Gallagher local-prime process, and under the full hierarchy the entire empirical bulk law is the generic Poisson sinc law.

The present calculation shows that this generic bulk law is already enough to prevent trace-norm matching with the smooth PNT continuum. The mechanism is elementary:

```text
smooth continuum pair energy
    = q_(a,b);

empirical locally-Poisson pair energy
    = self term 1 + q_(a,b).
```

This is the familiar distinction between a smooth intensity measure and an empirical point process with atomic self-correlation. The prime arithmetic enters only through the conjectural statement that the local point process has the Hardy--Littlewood/Gallagher Poisson limit; once that input is made, the `S_1` defect needs no zero divisor or analytic continuation.

The contrast with `PL-100`--`PL-101` is therefore informative rather than contradictory. Their midpoint cloud is an extremely regular deterministic sampling design whose local discreteness is tuned to the Fourier lattice and can track the continuum in trace norm through Nyquist. A locally Poisson cloud has order-one shot noise at the same coarse rank/time-bandwidth ratio. `S_1` is fine enough to distinguish those two **sampling microgeometries**.

Accordingly, observing that the rational primes fail an `S_1` continuum test at critical sampling would at most detect their microscopic local statistics. It would not distinguish an RH world from a matched non-arithmetic Poisson control.

## 6. Prior-art and novelty audit

No novelty is claimed for any ingredient used here.

- `PL-083` derives the critical prime Gram second moment from the local Hardy--Littlewood pair conjecture and identifies the extra diagonal `1` with the generic unit-intensity Poisson sampling constant.
- `PL-085` upgrades the full fixed-order hierarchy to `W_2` convergence of the prime bulk law to a generic Poisson sinc Euclidean-random-matrix law, using Gallagher/Freiberg local-prime prior art and Bordenave's Euclidean-random-matrix moment framework. Those references are already `SOURCES.md` 65--67.
- The continuum calculation is standard finite-time Fourier/Fejer covariance calculus of the same kind already used in `PL-096`.
- Lidskii--Mirsky eigenvalue majorization and the Lipschitz spectral test are standard operator theory already used repeatedly in this line.
- A fresh novelty check against current random Fourier/sinc-kernel discretization literature found active work comparing random sinc matrices with their continuum/integral-operator estimators, but no reason to reinterpret the present conditional prime statement as a new random-matrix theorem. The durable content is the **line-specific collision** between the `PL-085` Poisson bulk and the `PL-098`--`PL-101` Nyquist `S_1` question.

No `SOURCES.md` update is required: every load-bearing external theorem is already recorded for `PL-083`, `PL-085`, and `PL-096`; the new step is an exact derived comparison of those stored results.

## 7. Adversarial boundaries

1. **The prime conclusion is conditional.** The full local Hardy--Littlewood hierarchy required by `PL-085` is unproved. The finding is a decisive falsification control for interpreting a future positive `S_1` defect, not an unconditional theorem that the rational-prime covariance has that defect.
2. **This is the prime layer `k=1`, not the growing-depth mixed prime-power shell of `PL-094`--`PL-101`.** Its PNT continuum density is `exp(y)/(b-a)`, not the log-uniform density produced by large exponent depth.
3. **Only a positive lower bound is proved.** The argument does not identify the exact limit of `||A_X-B_X||_1`; eigenvector mismatch and finer spectral structure can make the true distance larger than the ordered-eigenvalue witness.
4. **The second moment is used only after `W_2` control.** Without the `PL-085` uniform-integrability input, a raw second-moment discrepancy would not by itself imply positive trace distance.
5. **Hard-edge and extreme observables remain different questions.** `PL-082` already shows that rare bounded prime clusters can drive extreme eigenvalues. The present argument uses the stable bulk law, not the smallest eigenvalue, inverse moments, condition numbers, or determinant zeros.
6. **Weights and targets are excluded.** Von Mangoldt/Mobius amplitudes, Nyman target couplings, perturbation determinants, and indefinite completed-Weil forms can import arithmetic structure absent from the support-only covariance.
7. **No analytic continuation occurs.** Every operator is defined from finite prime frequencies and a smooth PNT intensity. The Hardy--Littlewood conjecture is a statement about prime tuples, not a continuation of the Euler product into the critical strip.
8. **A positive `S_1` defect is not equivalent to Poisson statistics.** Many irregular non-arithmetic point clouds can fail trace-norm continuum matching. The result says only that the classical Poisson control already suffices to reproduce such a defect.
9. **The exact mixed-depth analogue remains open.** `PL-101` proves near-Nyquist matching for a deterministic midpoint control of the growing-depth log-uniform shell, but the actual mixed prime-power local point process may have correlations different from a single prime layer. That requires a separate depth-coupled audit rather than importing the present theorem verbatim.

## 8. Consequence for the surviving Nyquist branch

The `S_1` phase diagram now has an additional discriminator between coarse sampling geometry and microscopic regularity:

```text
continuum time-bandwidth exceeds rank
    -> universal positive rank floor (PL-098);

regular midpoint control,
ratio ->1 from either side
    -> S_1 continuum matching (PL-100, PL-101);

prime basis directions at their global Nyquist ratio,
under the full local Hardy--Littlewood hierarchy
    -> positive S_1 spectral separation from the PNT continuum
       already forced by the generic Poisson bulk (this finding).
```

Therefore the raw question

```text
"does the arithmetic cloud converge to its PNT continuum in S_1?"
```

is not a zeta-zero discriminator. Both outcomes are available in ordinary non-arithmetic sampling theory depending on microscopic point-process regularity.

For the prime-lattice program, a surviving `S_1`-based mechanism must subtract or otherwise neutralize this local shot-noise background and then exhibit a **rational-prime-specific excess** that survives matched point-process controls. Alternatively it must use a distinguished arithmetic weight/target or completed indefinite form whose information is not reducible to local sampling statistics. In particular, the unresolved mixed-depth question after `PL-101` should be attacked through its local cross-depth spacing/correlation structure, not by treating any eventual positive trace-class defect as intrinsically RH-sensitive.