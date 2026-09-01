# PL-083 — Critical prime-support sharp Gram has the Poisson second moment under local Hardy–Littlewood

## Claim

The exact bulk scale left open by `PL-081`,

```text
T ~ X/log X,
```

already has a classical local-statistics prediction at the level of the first nontrivial spectral moment. Fix

```text
0<a<b<infinity,
c>0,
P_X={p prime : aX<p<=bX},
M_X=|P_X|,
T_X=c X/log X,
```

and form the sharp finite-time Gram matrix

```text
G_X(p,q)
 =(1/T_X) integral_0^(T_X) exp(i t(log p-log q)) dt,
p,q in P_X.
```

Assume the following local uniform Hardy--Littlewood prime-pair input: for every fixed `A>0`, uniformly for integer `1<=h<=A log X`, prime pairs `p,p+h` in fixed sub-bands of `[aX,bX]` have the Hardy--Littlewood asymptotic with singular series `S(h)`, with an error `o(X/(log X)^2)` uniform in `h`. Equivalently for the derivation below, this may be assumed in the weighted form needed for bounded continuous functions of `(p/X,h/log X)`.

Then

```text
boxed:
(1/M_X) Tr(G_X^2)
   -> 1 + pi(a+b)/c.
```

The off-diagonal constant is exactly the second-moment constant of a unit-intensity homogeneous Poisson point process after rescaling ordinary prime gaps by `log X`. Thus the first nontrivial bulk spectral moment at the mean-prime-gap time scale is **not** a new RH-sensitive invariant of the exponent lattice: under the classical Hardy--Littlewood/Gallagher local model it is the generic Poisson sampling constant.

This is a conditional routing theorem, not evidence for the Hardy--Littlewood conjecture and not a theorem about the full empirical spectral distribution. `PL-082` remains simultaneously relevant: at the same scale `T_X=o(X)`, arbitrarily large bounded prime clusters force subsequential `lambda_min ->0` and `lambda_max ->infinity`, while the normalized second moment can still have the finite classical bulk limit above.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + CONJECTURAL-INPUT + PRIOR-ART/REDIRECT`, with a `NEGATIVE/OBSTRUCTION` conclusion for the route

```text
unweighted prime basis directions
+ sharp finite-time Gram
+ exact mean-gap horizon T=cX/log X
+ low bulk spectral moments
    -> new RH-sensitive prime-lattice phase.
```

The result does not rule out higher-order statistics not implied by the local Hardy--Littlewood hierarchy, distinguished arithmetic weights, target-relative/Nyman observables, explicit-formula couplings, or other structures that genuinely import analytic continuation.

## Exact reduction of the second moment to prime-pair gaps

Centering the time interval changes `G_X` only by diagonal unitary conjugacy. Hence

```text
|G_X(p,q)|^2
 =sinc^2((T_X/2) log(p/q)),

sinc(u)=sin(u)/u.
```

Because `G_X` is Hermitian positive semidefinite,

```text
Tr(G_X^2)
 =sum_(p,q in P_X) |G_X(p,q)|^2.
```

Writing `q=p+h` for the positive gaps gives the exact identity

```text
(1/M_X)Tr(G_X^2)
 =1
  +(2/M_X)
    sum_(h>=1)
    sum_(p,p+h in P_X)
      sinc^2((T_X/2)log((p+h)/p)).
```

Thus only the pair process of primes enters this spectral moment. There is no determinant, Euler product, zero divisor, or analytic continuation hidden in the formula.

## The critical scaling turns additive gaps into order-one sinc coordinates

For

```text
p=xX,
h=u log X,
```

with `x in [a,b]` and `u` in a fixed bounded interval,

```text
(T_X/2) log((p+h)/p)

 =(cX/(2 log X))
   [h/p+O(h^2/X^2)]

 = c u/(2x)+o(1),
```

uniformly on compact `u`-ranges. Therefore

```text
sinc^2((T_X/2)log((p+h)/p))
 -> sinc^2(cu/(2x)).
```

This is exactly why the scale `T~X/log X` survived `PL-081`: one Fourier-resolution cell has ordinary width

```text
X/T_X ~ (log X)/c,
```

which is the mean-prime-gap scale.

## Local Hardy--Littlewood plus Gallagher averaging gives the truncated limit

Let `S(h)` be the classical prime-pair singular series, normalized by

```text
S(h)=0                       for h odd,

S(h)=2 C_2 product_(r|h,r>2) (r-1)/(r-2)
                             for h even.
```

For every fixed `A`, the assumed uniform Hardy--Littlewood pair asymptotic gives, after partitioning the macroscopic `p/X` band and using uniform continuity of the sinc kernel,

```text
sum_(1<=h<=A log X)
 sum_(p,p+h in P_X)
 sinc^2((T_X/2)log((p+h)/p))

 = X/(log X)^2
   sum_(1<=h<=A log X)
     S(h)
     integral_a^b
       sinc^2(
         c(h/log X)/(2x)
       ) dx
   +o(X/log X).
```

Gallagher's classical singular-series mean theorem, specialized to prime pairs, says

```text
sum_(h<=H) S(h) ~ H.
```

Partial summation therefore gives the weighted Riemann-sum limit

```text
(1/log X)
 sum_(h<=A log X)
   S(h) f(h/log X)

 -> integral_0^A f(u) du
```

for every continuous `f` on `[0,A]`. Since

```text
M_X~(b-a)X/log X,
```

the normalized off-diagonal contribution from `h<=A log X` tends to

```text
(2/(b-a))
 integral_a^b
 integral_0^A
   sinc^2(cu/(2x)) du dx.
```

The singular-series arithmetic has disappeared from the limit after averaging over the `O(log X)` available local gaps. Its only surviving role is to enforce the classical mean-one local intensity.

## The long-gap tail is uniformly negligible

The passage `A->infinity` does not require Hardy--Littlewood information at large shifts. Reuse the unconditional pair-sieve estimate from `PL-081`: for the number `N_h(X)` of prime pairs in the band at gap `h`,

```text
N_h(X)
 <<_(a,b)
 X/(log X)^2 S_+(h),
```

where the positive local factor `S_+(h)` has bounded mean,

```text
sum_(h<=Y) S_+(h) << Y.
```

For `p,q~X`,

```text
|sinc((T_X/2)log(p/q))|^2
 <<_(a,b,c)
 min(1,(log X/h)^2).
```

Hence, for fixed sufficiently large `A`,

```text
sum_(h>A log X)
 N_h(X)
 min(1,(log X/h)^2)

 <<_(a,b,c)
 X/(log X)^2
 * (log X)/A.
```

After division by `M_X~X/log X`, this is `O(1/A)`. Therefore the truncated limit may be sent to `A=infinity`.

This tail bound is an important audit point: the constant below is not obtained by assuming an unjustified Hardy--Littlewood asymptotic uniformly over all macroscopic shifts. Only the logarithmic local range needs the conjectural pair asymptotic; the oscillatory sharp-kernel tail is removed by the unconditional sieve majorant already established in `PL-081`.

## The constant is exactly the Poisson sampling constant

The remaining integral is elementary:

```text
integral_0^infinity sinc^2(alpha u) du
 = pi/(2 alpha)
```

for `alpha>0`. With `alpha=c/(2x)`,

```text
integral_0^infinity
 sinc^2(cu/(2x)) du
 =pi x/c.
```

Therefore

```text
(2/(b-a))
 integral_a^b pi x/c dx

 =pi(a+b)/c.
```

Adding the unit diagonal proves

```text
boxed:
(1/M_X)Tr(G_X^2)
 ->1+pi(a+b)/c.
```

The factor can be checked independently against the Palm second moment of a homogeneous Poisson process. At a fixed macroscopic position `x`, rescale ordinary offsets by `log X` so that the conjectural local prime intensity is one. The limiting Gram kernel is

```text
k_x(u)=sinc(cu/(2x)).
```

For a unit-intensity Poisson process, Campbell's formula gives the per-point squared Gram mass

```text
1+integral_R |k_x(u)|^2 du
 =1+2 pi x/c.
```

Averaging `x` uniformly across `[a,b]` gives

```text
1+(1/(b-a))integral_a^b 2 pi x/c dx
 =1+pi(a+b)/c,
```

exactly the same constant. This matched control is stronger than merely observing that prime gaps have average size `log X`: the entire second spectral moment agrees with the generic Poisson local point process.

## Prior art and novelty audit

None of the number-theoretic ingredients is new.

- **P. X. Gallagher**, “On the distribution of primes in short intervals,” *Mathematika* **23**(1) (1976), 4--9, DOI `10.1112/S0025579300016442`, proves that a suitable uniform Hardy--Littlewood prime-tuple conjecture implies Poisson statistics for prime counts in intervals of length `lambda log X`. His proof uses the asymptotic mean-one behavior of the singular series over fixed-size shift sets. The `k=2` singular-series average is the exact arithmetic input used above.
- **Salvatore Torquato, Ge Zhang, Matthew De Courcy-Ireland**, “Hidden multiscale order in the primes,” *Journal of Physics A: Mathematical and Theoretical* **52**(13) (2019), 135002, DOI `10.1088/1751-8121/ab0588`, study prime pair correlations conditionally on Hardy--Littlewood and identify a transition from multiscale/hyperuniform order on macroscopic intervals to uncorrelated behavior when the interval length is only logarithmic in the prime height. This is close prior art for the statement that the mean-gap scale is a classical local-statistics regime rather than a new zeta-spectral phase.
- The unconditional tail domination is the Selberg/Brun pair-sieve estimate already derived and sourced in `PL-081`.

A targeted search around prime-supported sinc Gram matrices, logarithmic prime frequencies, Hardy--Littlewood pair kernels, prime point-process spectra, and nonharmonic Fourier frames did not locate a source stating the displayed Gram-trace constant in this notation. The line-specific content is therefore an **exact conditional transform** of classical local prime-pair statistics through the sharp logarithmic Gram kernel, not a claim that the Poisson prediction or singular-series averaging is new.

The novelty audit is negative for the RH mechanism. The same limiting constant is reproduced by a generic Poisson point process with the same local density, and no analytic-continuation or functional-equation information enters the derivation.

## Adversarial boundaries

1. **The Hardy--Littlewood input is conjectural.** The formula is conditional. It must not be cited as an unconditional asymptotic for the rational primes.
2. **Only the second empirical moment is classified.** The result does not prove convergence of the full empirical spectral distribution, nor does it determine its higher moments.
3. **Poisson agreement at this moment is not a full Poisson-process theorem.** The matched control shows non-discrimination of this statistic, not equality of every local prime statistic to a Poisson process.
4. **Extreme eigenvalues remain uncontrolled by the bulk moment.** `PL-082` gives subsequences at this same horizon with `lambda_min->0` and `lambda_max->infinity`; their spectral proportion can vanish while the normalized second moment has a finite limit.
5. **The result is support-only and unweighted.** Inserting `Lambda`, Möbius orientation, or another arithmetic amplitude changes the pair measure. `PL-075`--`PL-077` show that such weighted channels route into Hardy--Littlewood, Selberg variance, and zero pair-correlation theory rather than into this support-only constant.
6. **The constant does not single out `Re(s)=1/2`.** It depends only on the observation ratio `c`, the macroscopic prime band, and local pair intensity. There is no complex `sigma` parameter in the support-only Gram.
7. **No Euler product is continued.** Every identity before the Hardy--Littlewood input is a finite Gram/pair-count identity. The conjectural input concerns primes on the integer line and does not provide analytic continuation of zeta.
8. **The logarithmic-scale local regime is classical prior art.** Gallagher's Poisson theorem and the Torquato--Zhang--De Courcy-Ireland transition prevent interpreting the critical support scale itself as a newly discovered arithmetic phase.
9. **Higher-order escapes require their own controls.** A candidate based on `Tr(G^k)` for `k>=3` would have to be tested against the full Hardy--Littlewood `k`-tuple/Gallagher hierarchy and generic Poisson sampling before it could count as zeta-specific structure.

## Consequence for the prime-lattice search

The unweighted prime-support sharp-Gram branch is now separated more sharply:

```text
T >> X/log X
    -> empirical bulk delta_1 (`PL-081`);

T = c X/log X
    -> first nontrivial bulk moment is,
       under local Hardy--Littlewood,
       exactly the generic Poisson sampling constant (this finding);

any T=o(X)
    -> rare bounded prime clusters force
       two-sided extreme spectral instability
       along subsequences (`PL-082`).
```

Thus the previously unresolved mean-gap scale does not automatically rescue the raw support-only spectral program. At least at second-moment level, the nontrivial bulk is completely explained by classical local prime statistics and survives a generic Poisson control, while the extremes are already contaminated by unconditional prime clustering.

A surviving finite-horizon mechanism must therefore add information not captured by the local support point process alone: a distinguished arithmetic weight or target, a completion/explicit-formula coupling, a higher-order invariant that survives the Hardy--Littlewood/Poisson controls but is not merely another local correlation statistic, or another structure that genuinely transports analytic-continuation information into the finite prime lattice.