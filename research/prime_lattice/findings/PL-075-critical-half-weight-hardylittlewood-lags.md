# PL-075 — Critical half-weight fixed lags are universal; the von Mangoldt channel is Hardy–Littlewood prime-pair data

## Claim

The most immediate non-unimodular escape left open by `PL-074` can be classified at fixed additive lag. Insert a power weight into the critical positive-cone Dirichlet polynomial

```text
I_T={n in N : a T < n <= b T},

D_(b,sigma,T)(t)
  =sum_(n in I_T) b(n) n^(-sigma-it),

Q_(b,sigma)(T)
  =(1/T) integral_0^T |D_(b,sigma,T)(t)|^2 dt,
```

where `0<a<b<infinity` are fixed. For a fixed lag `h>=1`, suppose the coefficient sequence has an ordinary correlation density

```text
sum_(n<=X) b(n) conjugate(b(n+h))
  = c_h X + o(X).
```

Then the exact finite-time Gram kernel from `PL-074` gives

```text
T^(2 sigma) C_(b,sigma,h)(T)
 -> c_h integral_a^b x^(-2 sigma) kappa_h(x) dx,

kappa_h(x)=exp(+i h/(2x)) sinc(h/(2x)),
```

where `C_(b,sigma,h)` is normalized as in the lag decomposition

```text
Q_(b,sigma)(T)
 = diagonal
   +2 T Re sum_(h>=1) C_(b,sigma,h)(T).
```

Hence the contribution of every fixed lag has deterministic scale

```text
T^(1-2 sigma).
```

The exponent `sigma=1/2` is therefore the unique power weight at which a nonzero fixed-lag correlation density becomes order one at the `N~T` Fourier-resolution scale. This does **not** single out the Riemann critical line: exactly the same half-weight transition occurs for any coefficient system with a nonzero fixed-lag density. In particular, taking `b(n)=mu(n)^2` and Mirsky's square-free-pair theorem gives this `sigma=1/2` transition unconditionally, with no zeta zeros or analytic continuation.

For the canonical non-unimodular prime weight `b(n)=Lambda(n)`, the correlation density is precisely the Hardy--Littlewood prime-pair problem:

```text
(1/X) sum_(n<=X) Lambda(n) Lambda(n+h)
  -> S_HL(h).
```

Thus, conditionally on the fixed-shift Hardy--Littlewood conjecture,

```text
T^(2 sigma) C_(Lambda,sigma,h)(T)
 -> S_HL(h) integral_a^b x^(-2 sigma) kappa_h(x) dx.
```

At `sigma=1/2`, the fixed-lag prime-pair correction is order one; for `sigma>1/2` it vanishes as a power, and for `sigma<1/2` it grows as a power, subject to the displayed correlation asymptotic. The arithmetic constant is the classical prime-pair singular series, not a new exponent-lattice spectral invariant.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART/REDIRECT` for the route

```text
critical positive-cone finite-time Gram
+ canonical non-unimodular von Mangoldt coefficients
+ n^(-sigma) weighting
    -> new lattice mechanism selecting sigma=1/2 / RH.
```

The result is deliberately limited to fixed additive lags. It does **not** classify the full sum over lags growing with `T`, Montgomery pair correlation, prime variance in short intervals, or explicit-formula operators. Those are separate global/mesoscopic questions.

## Exact weighted lag asymptotic

Reuse the corrected kernel convention from `PL-074`:

```text
K_T(u)
  =(1/T) integral_0^T exp(+i t u) dt
  =exp(+i T u/2) sinc(T u/2).
```

For coefficients

```text
a_(sigma)(n)=b(n)n^(-sigma),
```

the fixed-lag term is

```text
C_(b,sigma,h)(T)
 =(1/T) sum_(n,n+h in I_T)
   b(n) conjugate(b(n+h))
   [n(n+h)]^(-sigma)
   K_T(log((n+h)/n)).
```

Write `x=n/T`. Since `x` remains in `[a,b]` and `h` is fixed,

```text
T log((n+h)/n)
 =h/x+O_h(1/T),
```

and therefore

```text
K_T(log((n+h)/n))
 =kappa_h(x)+O_h(1/T)
```

uniformly on the band. Likewise, for every fixed real `sigma`,

```text
[n(n+h)]^(-sigma)
 =T^(-2 sigma) x^(-2 sigma)(1+O_(h,sigma)(1/T)).
```

Assume

```text
A_h(X)
 =sum_(n<=X)b(n)conjugate(b(n+h))
 =c_h X+o(X).
```

Abel summation against the fixed smooth weight

```text
f_(sigma,h)(x)=x^(-2 sigma) kappa_h(x)
```

gives

```text
(1/T) sum_(aT<n<=bT)
 b(n)conjugate(b(n+h)) f_(sigma,h)(n/T)

 -> c_h integral_a^b f_(sigma,h)(x) dx.
```

The endpoint loss from also requiring `n+h in I_T` is negligible for fixed `h`. Combining the three displays yields

```text
C_(b,sigma,h)(T)
 =T^(-2 sigma)
  [ c_h integral_a^b x^(-2 sigma)kappa_h(x) dx + o(1) ].
```

Multiplication by the exact outer factor `2T` in `Q_(b,sigma)` gives the claimed scale `T^(1-2 sigma)`.

No Euler product or continuation argument is hidden here. The half exponent is produced by three elementary pieces only:

```text
macroscopic band cardinality  ~ T,
coefficient amplitude          ~ T^(-sigma) per side,
finite-time lag normalization  = exact PL-074 kernel.
```

## Square-free support is an unconditional half-weight control

Take

```text
b(n)=mu(n)^2.
```

For every fixed `h`, Mirsky's theorem gives

```text
(1/X) sum_(n<=X) mu(n)^2 mu(n+h)^2
 -> S_sf(h),
```

with

```text
S_sf(h)=product_p (1-nu_p(h)/p^2),

nu_p(h)=1 if p^2 divides h,
          2 otherwise.
```

Therefore

```text
T^(2 sigma) C_(mu^2,sigma,h)(T)
 -> S_sf(h) integral_a^b x^(-2 sigma) kappa_h(x) dx.
```

This is an especially strong falsification control for interpreting `sigma=1/2` as a zero-localization mechanism. The same power transition already occurs in the square-free **support** channel that `PL-074` classified as local sieve-density data. There is no Möbius orientation, no zeta zero divisor, and no analytic continuation.

More generally, any bounded or suitably controlled sequence with a nonzero fixed-lag Cesàro correlation has the same exponent. The value `1/2` is therefore a universal balance exponent for this one-dimensional critical-band quadratic statistic, even though the coefficient-dependent constant may be highly arithmetic.

## Von Mangoldt orientation becomes Hardy--Littlewood prime-pair correlation

Now take

```text
b(n)=Lambda(n).
```

The standard weighted Hardy--Littlewood prime-pair conjecture states, for fixed nonzero `h`,

```text
sum_(n<=X) Lambda(n)Lambda(n+h)
 = S_HL(h) X + o(X),
```

where equivalently

```text
S_HL(h)
 = product_p
   (1-1/p)^(-2) (1-nu_p({0,h})/p).
```

For odd `h` this singular series is zero; for even `h` it is the usual positive prime-pair singular series

```text
2 C_2 product_(p|h, p>2) (p-1)/(p-2).
```

Consequently the fixed-lag pointed Gram term is exactly a smooth weighted version of this classical correlation problem. Under Hardy--Littlewood,

```text
T^(2 sigma) C_(Lambda,sigma,h)(T)
 -> S_HL(h)
    integral_a^b x^(-2 sigma) kappa_h(x) dx.
```

At `sigma=1/2`,

```text
2T C_(Lambda,1/2,h)(T)
 -> 2 S_HL(h)
    integral_a^b x^(-1) kappa_h(x) dx
```

before taking the real part in `Q`. Thus the canonical `Lambda(n)n^(-1/2)` weighting does make fixed prime-pair lags survive at order one. But the input needed to compute those constants at a prescribed even lag is exactly the classical Hardy--Littlewood/twin-prime correlation, not information generated by the exponent-vector geometry.

The fixed-shift conjecture remains open. Modern work proves the expected asymptotic for `sum Lambda(n)Lambda(n+h)` for **almost all** shifts in substantial growing ranges. Matomäki--Radziwill--Tao prove such an averaged result for `X^(8/33+epsilon)<=H<=X^(1-epsilon)`. Tao--Teräväinen formulate the fixed-tuple Hardy--Littlewood--Chowla conjecture explicitly and obtain conditional progress in the presence of a Siegel zero. These results place the surviving coefficient term squarely in established additive prime-correlation theory.

## Why the half exponent is not the Riemann critical line

The numerical coincidence `sigma=1/2` is real but its mechanism is too generic.

At the `N~T` resolution threshold, a fixed lag samples `O(T)` pairs. Two copies of the radial weight contribute `T^(-2 sigma)`. The exact finite-time normalization contributes the remaining factor shown above. The net power is therefore

```text
T^(1-2 sigma).
```

Nothing in this counting uses

```text
zeta(s)=zeta(1-s) * completion factors,
```

Weil positivity, the zero divisor, or the self-dual adelic axis. The same transition survives after replacing `Lambda` by `mu^2`, or by any matched coefficient process with a nonzero fixed-lag density.

There is also no claim that the **whole quadratic form** has a phase transition at `sigma=1/2`. For `Lambda`, for example, the diagonal

```text
sum_(n in I_T) Lambda(n)^2 n^(-2 sigma)
```

has its own logarithmic size at the half weight. The finding isolates only the fixed-lag off-diagonal power law. Treating that local balance as a Hilbert--Polya or RH selector would therefore overinterpret a normalization effect.

## Relation to Montgomery pair correlation

There is a classical zero-side context, but it is broader than the exact fixed-lag statement proved here. Montgomery's pair-correlation program connects weighted zero-pair statistics, via explicit-formula methods and prime Dirichlet polynomials, to second-moment information about primes. Goldston--Montgomery and later Chan show under RH that strong pair correlation is equivalent to suitable prime short-interval variance asymptotics; later work studies the `|alpha|>1` range using long Dirichlet polynomials.

This reinforces the prior-art redirect rather than supplying a new lattice mechanism. Once a von Mangoldt weight and enough aggregation are inserted, one is entering a classical theory where prime correlations and zero correlations are already coupled by the explicit formula. The present finding does **not** identify the `PL-074` full lag sum with Montgomery's `F(alpha,T)` and does not import any RH-dependent pair-correlation theorem into the exact fixed-lag derivation.

In particular, one must distinguish two statements:

```text
fixed-lag PL-074 Gram asymptotic
    -> elementary kernel + Hardy--Littlewood correlation;

zero pair correlation / prime short-interval variance
    -> classical explicit-formula theory, often studied under RH.
```

Conflating them would turn a clean negative audit into an unjustified equivalence.

## Prior-art and novelty audit

No novelty is claimed for the general ingredients.

- L. Mirsky, “Note on an asymptotic formula connected with r-free integers,” *Quarterly Journal of Mathematics* **os-18**(1) (1947), 178--182, DOI `10.1093/qmath/os-18.1.178`, is the square-free pair-density anchor already used in `PL-074`.
- K. Matomäki, M. Radziwill, T. Tao, “Correlations of the von Mangoldt and higher divisor functions I. Long shift ranges,” *Proceedings of the London Mathematical Society* **118**(2) (2019), 284--350, DOI `10.1112/plms.12181`, proves the expected von-Mangoldt shifted-correlation asymptotic for almost all shifts in long ranges.
- T. Tao, J. Teräväinen, “The Hardy--Littlewood--Chowla conjecture in the presence of a Siegel zero,” *Journal of the London Mathematical Society* **106**(4) (2022), 3317--3378, DOI `10.1112/jlms.12663`, states the fixed-tuple Hardy--Littlewood correlation conjecture in von-Mangoldt form and gives conditional progress.
- H. L. Montgomery, “The pair correlation of zeros of the zeta function,” *Proceedings of Symposia in Pure Mathematics* **24** (1973), 181--193, DOI `10.1090/pspum/024/9944`, is the classical zero-pair-correlation anchor.
- T. H. Chan, “More Precise Pair Correlation of Zeros and Primes in Short Intervals,” *Journal of the London Mathematical Society* **68**(3) (2003), 579--598, DOI `10.1112/S0024610703004769`, records and refines the Goldston--Montgomery equivalence, under RH, between strong pair correlation and prime short-interval second moments.

The `T^(1-2 sigma)` formula is an exact specialization of the corrected finite-time lag identity in `PL-074` plus Abel summation. It is stored because it answers a line-specific question that remained open there: what happens when the first canonical non-unimodular zeta coefficient, `Lambda`, is inserted together with the radial half-weight? The answer is a classicalized prime-pair channel, and the apparent half exponent is already reproduced by a zero-insensitive square-free control.

A targeted literature audit around von Mangoldt shifted correlations, Hardy--Littlewood prime pairs, Dirichlet-polynomial mean values, and Montgomery pair correlation recovered established additive-correlation and explicit-formula theories rather than a theorem in which this critical-band half-weight forces Riemann-zero localization. The line-specific scaling identity is treated as derived routing information, not as a novelty claim.

## Analytic-continuation and adversarial audit

No analytic continuation is used in the exact result. `Lambda(n)` is inserted as an arithmetic coefficient, and every displayed `C_(b,sigma,h)(T)` is a finite sum arising from a finite Dirichlet polynomial.

Several possible overclaims are excluded explicitly.

1. **Fixed lags only.** The full `Q_(b,sigma)(T)` contains lags growing with `T`; summing their collective contribution can require much stronger information than any fixed-shift asymptotic.
2. **Hardy--Littlewood is not evidence.** The `Lambda` limit is conditional at a prescribed even shift. It is used to identify the arithmetic content, not to establish a new theorem about primes.
3. **The half exponent is only a power balance.** It does not prove a nonzero limit if the weighted integral or correlation constant vanishes, and it does not identify a self-adjoint spectrum.
4. **Diagonal behavior is separate.** For spiky coefficients such as `Lambda`, the diagonal can carry additional logarithmic factors; no whole-form criticality is claimed.
5. **Montgomery pair correlation is not derived here.** Its relation to primes uses explicit-formula machinery and global averaging not present in the fixed-lag calculation.
6. **No Euler product is continued.** If one later identifies `Lambda` with `-zeta'/zeta`, that Dirichlet series is initially valid only in `Re(s)>1`; continuation toward the critical strip must come from the classical meromorphic continuation/explicit formula or another independently justified mechanism.
7. **Matched controls survive.** `mu^2` already gives the same `sigma=1/2` scale unconditionally, and generic coefficient systems with a fixed-lag density give the same power law. Therefore the exponent alone fails the line's rational-prime/RH discrimination test.
8. **Other target-relative observables remain open.** Nyman/Bagchi targets, completed Weil forms, higher moments, long-lag collective structure, or a coupling that uses the zeta divisor in a non-universal way are not ruled out.

## Consequence for the research line

The finite-horizon coefficient branch now has a sharper map:

```text
bare positive characters
    -> universal N~T sinc geometry (`PL-072`);

Möbius sign orientation
    -> unpointed torus/Gram gauge (`PL-073`);

pointed mu / mu^2 at fixed lag
    -> Chowla orientation / Mirsky support (`PL-074`);

pointed Lambda n^(-sigma) at fixed lag
    -> Hardy--Littlewood prime pairs,
       with universal T^(1-2 sigma) scaling (this finding).
```

Thus merely adding the most canonical non-unimodular prime coefficient and observing that `n^(-1/2)` is the neutral scaling does not produce new RH rigidity. A surviving finite-horizon construction must use information not reducible to fixed additive pair correlations and not reproduced by the `mu^2` half-weight control. The remaining plausible escapes are genuinely collective growing-lag structure, a completion-sensitive target/form, higher-order arithmetic coupling, or an explicit-formula mechanism whose positivity/localization content is stronger than the classical correlation identities themselves.
