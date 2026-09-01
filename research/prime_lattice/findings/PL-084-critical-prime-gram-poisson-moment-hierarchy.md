# PL-084 — Critical prime-support sharp Gram has the Poisson fixed-moment hierarchy under local Hardy–Littlewood

## Claim

The second-moment Poisson control in `PL-083` extends to **every fixed bulk spectral moment** at the exact mean-prime-gap horizon, provided one assumes the corresponding finite Hardy--Littlewood prime-tuple hierarchy.

Fix

```text
0<a<b<infinity,
c>0,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
T_X=c X/log X,
```

and let

```text
G_X(p,q)
 =(1/T_X) integral_0^(T_X) exp(i t(log p-log q)) dt,
p,q in P_X.
```

For an integer `m>=2`, assume the following local uniform Hardy--Littlewood input through order `m`: for every fixed `A>0` and every `1<=r<=m`, uniformly for distinct integer shifts

```text
H={0,h_1,...,h_(r-1)} subset [-A log X,A log X]
```

and for fixed macroscopic sub-bands of `[aX,bX]`, the corresponding prime `r`-tuple count has the Hardy--Littlewood asymptotic with singular series `S(H)`, with error `o(X/(log X)^r)` uniform in the shifts. This is the fixed-order local hypothesis used below; it is conjectural.

Let `Pi` be a homogeneous Poisson point process of intensity one on `R`, viewed under its Palm law so that `0` is a distinguished point. For `x in [a,b]` define

```text
k_(x,c)(u,v)=sinc(c(u-v)/(2x)),
sinc(y)=sin(y)/y,
```

and let `mu_m(x;c)` be the Palm per-point closed-walk moment of the associated Poisson sinc Gram matrix:

```text
mu_m(x;c)
 = E^0 [
     sum_(y_1,...,y_(m-1) in Pi union {0})
       product_(j=0)^(m-1)
       k_(x,c)(y_j,y_(j+1))
   ],

y_0=y_m=0.
```

For every fixed `m`, this moment is finite. Under the local Hardy--Littlewood hierarchy above,

```text
boxed:
(1/M_X) Tr(G_X^m)
   ->
(1/(b-a)) integral_a^b mu_m(x;c) dx.
```

Thus **all fixed normalized trace moments of the unweighted prime-support sharp Gram matrix at `T=cX/log X` are exactly the moments of a generic unit-intensity Poisson Euclidean random matrix with the same sinc kernel**. The prime singular series disappears after the classical Gallagher averaging that produces the Poisson local process.

The first two nontrivial checks are

```text
m=2:
(1/M_X) Tr(G_X^2)
 -> 1 + pi(a+b)/c,
```

recovering `PL-083`, and

```text
m=3:
(1/M_X) Tr(G_X^3)
 -> 1
    + 3 pi(a+b)/c
    + (4 pi^2/(3 c^2))(a^2+ab+b^2).
```

The conclusion is a **negative/prior-art redirect** for the route

```text
prime basis directions
+ unweighted sharp finite-time Gram
+ critical horizon T=cX/log X
+ any fixed collection of bulk trace moments
    -> new RH-sensitive spectral invariant.
```

Under the classical Hardy--Littlewood/Gallagher local model, that entire fixed-moment hierarchy is a Poisson point-process statistic. No analytic continuation, functional equation, zeta zero divisor, or critical-line structure enters.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + CONJECTURAL-INPUT + PRIOR-ART/REDIRECT`, with a `DECISIVE-NEGATIVE` conclusion only for fixed-order, support-only critical-Gram bulk moments.

## Exact reduction to closed walks on logarithmic prime frequencies

Centering the time interval changes `G_X` only by diagonal unitary conjugacy. Hence all trace moments are unchanged if we replace it by the real symmetric matrix

```text
A_X(p,q)
 = sinc((T_X/2) log(p/q)).
```

Therefore

```text
Tr(G_X^m)=Tr(A_X^m)

 = sum_(p_0,...,p_(m-1) in P_X)
     product_(j=0)^(m-1)
       sinc((T_X/2)log(p_j/p_(j+1))),

p_m=p_0.
```

This is an exact finite identity. Each term is a closed walk of length `m` through the prime-frequency set `{log p}`. The only arithmetic input needed to average it is the local joint distribution of the participating primes.

Split the tuples according to their equality pattern. If the ordered walk uses exactly `r` distinct primes, its equality pattern is a partition of the cyclic positions into `r` blocks. After choosing `p_0` as the distinguished prime, the remaining `r-1` distinct primes are described by additive offsets from `p_0`. This partition expansion is exactly the same combinatorics that appears in the Campbell--Mecke/Palm moment expansion for a Poisson point process.

## The critical scale converts prime offsets into a unit-intensity spatial process

Write

```text
p_0=xX,
p_j=p_0+h_j,
h_j=u_j log X,
```

with `x in [a,b]` and bounded `u_j`. Since `T_X=cX/log X`, uniformly on bounded offset boxes,

```text
(T_X/2) log(p_i/p_j)

 = (c/(2x)) (u_i-u_j) + o(1).
```

Thus every fixed closed-walk kernel converges to

```text
product_(j=0)^(m-1)
 sinc(c(u_j-u_(j+1))/(2x)).
```

The prime number theorem gives

```text
(1/M_X) sum_(p in P_X) F(p/X)
 -> (1/(b-a)) integral_a^b F(x) dx
```

for continuous `F`. The macroscopic prime base point is therefore asymptotically uniform in `x`, while the microscopic additive coordinate is measured in units of `log X`, the local mean prime gap.

## Hardy--Littlewood plus Gallagher gives the Poisson factorial measures

For an equality pattern with `r` distinct primes, restrict first to

```text
|h_j|<=A log X.
```

The assumed uniform Hardy--Littlewood `r`-tuple asymptotic replaces the count of each fixed shift pattern by

```text
S(H) X/(log X)^r.
```

Gallagher's fixed-order singular-series theorem states that the average of `S(H)` over distinct shift sets in a growing box tends to one. Equivalently, after scaling `h_j=u_j log X`, the local factorial moment measures converge to ordinary Lebesgue measure

```text
du_1 ... du_(r-1),
```

which is precisely the factorial moment measure of a homogeneous unit-intensity Poisson process.

Summing over every equality partition of the cyclic positions gives the Palm closed-walk moment `mu_m(x;c)`. This is not a new prime-statistics theorem: it is the spectral transform of the same fixed-order Hardy--Littlewood/Gallagher mechanism that gives Poisson prime counts in logarithmic intervals.

The passage from one interval count to the needed finite-dimensional local process is also classical in spirit. Tristan Freiberg proved, under a Hardy--Littlewood prime-tuple hypothesis, joint asymptotic independence for prime counts in finitely many adjacent logarithmic intervals. The present calculation does not require a new source of local arithmetic randomness; it only integrates that classical Poisson factorial hierarchy against the sinc closed-walk kernel.

## The sinc tail does not import a hidden long-range arithmetic term

The compact-offset calculation must be audited because the sinc kernel has infinite support. For `p,q` in the fixed macroscopic band,

```text
|A_X(p,q)|
 <<_(a,b,c)
 min(1, log X/|p-q|).
```

For every fixed number `r` of distinct primes, the standard upper-bound sieve gives a prime-tuple majorant of size

```text
<<_m S_+(H) X/(log X)^r,
```

where the positive local factor has bounded fixed-order average over shift boxes. Gallagher's singular-series averaging, and standard fixed-order upper-bound variants, give the required box estimate.

After scaling by `log X`, each equality pattern is majorized by a finite closed-walk product of functions

```text
g(u)=min(1,C/|u|).
```

The quotient graph of a cyclic walk is connected and every nontrivial vertex has degree at least two. A fixed finite dyadic/Young-convolution estimate therefore makes the corresponding product integrable over all relative coordinates. Consequently the contribution with some scaled offset larger than `A` is `o_A(1)` uniformly in `X`, and then tends to zero as `A->infinity`.

This tail step is important: the Poisson moment limit is not obtained by assuming an unjustified Hardy--Littlewood asymptotic for macroscopic shifts. The conjectural asymptotic is needed only on each fixed multiple of the logarithmic prime-gap scale; the long-range sinc tail is disposed of by classical upper-bound sieve domination.

## Explicit third-moment audit

The `m=3` case gives a useful exact check beyond `PL-083`. Put

```text
alpha=c/(2x),
k(u)=sinc(alpha u).
```

Under the Palm Poisson model there are three equality types.

All three positions equal the distinguished point, contributing `1`. Exactly two distinct points give three choices of the repeated position and therefore

```text
3 integral_R k(u)^2 du.
```

All three points distinct give

```text
integral_R integral_R
 k(u) k(v-u) k(v) du dv.
```

The elementary Fourier identities

```text
integral_R sinc(alpha u)^2 du = pi/alpha,

Fourier[sinc(alpha u)](xi)
 = (pi/alpha) 1_(|xi|<alpha)
```

imply

```text
integral_R integral_R
 k(u) k(v-u) k(v) du dv
 = pi^2/alpha^2.
```

Hence

```text
mu_3(x;c)
 = 1 + 6 pi x/c + 4 pi^2 x^2/c^2.
```

Averaging `x` uniformly over `[a,b]` yields

```text
boxed:
1
+3 pi(a+b)/c
+(4 pi^2/(3c^2))(a^2+ab+b^2).
```

This confirms directly that the first moment beyond `PL-083` contains no surviving singular-series arithmetic after local averaging.

## Prior art and novelty audit

None of the ingredients that produce the Poisson hierarchy is new.

- **P. X. Gallagher**, “On the distribution of primes in short intervals,” *Mathematika* **23**(1) (1976), 4--9, DOI `10.1112/S0025579300016442`, proves that suitable uniform Hardy--Littlewood prime-tuple conjectures imply Poisson statistics for prime counts in intervals of length `lambda log X`; his fixed-order singular-series average is the exact arithmetic input used here.
- **Tristan Freiberg**, “A Note on the Distribution of Primes in Intervals,” in *Irregularities in the Distribution of Prime Numbers*, Springer, 2018, pp. 23--44, DOI `10.1007/978-3-319-92777-0_2`, derives joint Poisson laws for counts in finitely many adjacent logarithmic intervals under a Hardy--Littlewood hypothesis. This is close prior art for interpreting the whole local finite-dimensional prime process as Poisson rather than only one interval count.
- **Charles Bordenave**, “Eigenvalues of Euclidean random matrices,” *Random Structures & Algorithms* **33**(4) (2008), 515--532, DOI `10.1002/rsa.20228`, studies limiting spectral measures and moment formulae for matrices whose entries are functions of random spatial point differences. This is close matched-control prior art for the random-matrix side once the rescaled prime support has become a Poisson spatial process. The present finding does not claim that every technical hypothesis of Bordenave's theorem specializes verbatim to the non-`L^1` sinc kernel; the Palm cycle moments above are derived directly.

A targeted search around prime-supported sinc Gram matrices, logarithmic prime frequencies, Hardy--Littlewood tuple statistics, Poisson Euclidean random matrices, random Fourier/Vandermonde Grams, and spectral-moment formulae did not locate a source stating this exact prime-Gram transform. The line-specific statement is therefore an **exact conditional transform of classical local prime statistics**, not a novelty claim for the underlying Poisson law, singular-series hierarchy, or Euclidean-random-matrix moment method.

The novelty audit is decisively negative for the RH mechanism: a generic Poisson point process with the same local density reproduces every fixed trace moment under the stated arithmetic hypothesis.

## Adversarial boundaries

1. **The result is conditional.** Uniform local Hardy--Littlewood asymptotics through order `m` are unproved for every `m>=2`; the theorem must not be quoted as an unconditional prime spectral law.
2. **`m` is fixed before `X->infinity`.** Nothing here controls moments whose order grows with `X`, large deviations of the spectral measure, or a characteristic determinant requiring effectively unbounded moment information.
3. **Fixed moments do not settle the full empirical spectral distribution.** Moment determinacy and tightness at the matrix level are separate questions. The result identifies every fixed moment under its matching finite tuple hypothesis; it does not claim an unconditional or all-orders limiting ESD theorem.
4. **Extreme eigenvalues remain a different channel.** `PL-082` gives subsequences at the same `T=o(X)` range with `lambda_min->0` and `lambda_max->infinity` from bounded prime clusters. Such rare extremes may have vanishing empirical mass and are compatible with classical fixed bulk moments.
5. **The matched control is local and support-only.** Arithmetic weights such as `Lambda`, Möbius orientation, target-relative Nyman observables, or completed explicit-formula couplings alter the correlation measures and are not covered.
6. **No `Re(s)=1/2` is selected.** The only criticality here is the sampling relation `T~X/log X`, where Fourier resolution matches the mean prime gap. It is unrelated to the analytic critical line.
7. **No continuation is used.** All exact identities are finite Gram identities. Hardy--Littlewood describes prime tuples on the integer line; it supplies no analytic continuation of zeta.
8. **Poisson agreement is not independence of the actual primes.** The singular series is highly arithmetic for each fixed configuration. It disappears only after the Gallagher average relevant to these normalized local trace moments.
9. **The Bordenave comparison is a matched-control classification, not a black-box proof.** The sinc kernel has slow `1/u` decay, so the prime-to-Poisson passage is justified here by the closed-walk tail estimate rather than by silently invoking a random-matrix theorem with unchecked kernel assumptions.
10. **An escape must beat the full local Hardy--Littlewood hierarchy, not merely the pair statistic.** Testing `Tr(G^4)`, `Tr(G^5)`, and so on at fixed order cannot by itself rescue the support-only branch: under the corresponding classical tuple conjectures those statistics remain Poisson Euclidean-random-matrix moments.

## Consequence for the prime-lattice search

The unweighted prime-basis sharp-Gram branch now has a sharper routing diagram:

```text
T >> X/log X
    -> empirical bulk collapses to delta_1 (`PL-081`);

T = c X/log X
    -> every fixed bulk trace moment is,
       under the corresponding local Hardy--Littlewood hierarchy,
       exactly the generic Poisson sinc-Gram moment (this finding);

any T=o(X)
    -> bounded prime clusters produce subsequential
       two-sided extreme spectral instability (`PL-082`).
```

Therefore the exact mean-gap scale is not a surviving RH mechanism merely because its Gram spectrum is nontrivial. Its **fixed-order bulk** is governed by classical local prime-tuple statistics and has a generic Poisson matched control, while its **extremes** are already contaminated by unconditional bounded clustering.

A materially different finite-horizon mechanism must transport information that this local point-process quotient discards: distinguished arithmetic amplitudes, a target-relative/Nyman coupling, completed explicit-formula data, a genuinely global determinant or growing-order statistic with a separate arithmetic rigidity theorem, or another construction that actually carries analytic-continuation information into the finite prime lattice.