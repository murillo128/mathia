# PL-151 — Square-root-renormalized fixed-depth Weil boundary is an almost-periodic zero readout, not a limiting operator

## Claim

`PL-066` leaves open the most immediate amplitude escape from the natural completed-Weil boundary collapse: after the canonical `exp(-L)` boundary normalization has suppressed critical-line zeros by an additional factor `exp(-L)`, multiply the centered residual by `exp(L)` so that an RH zero has order-one amplitude.

For the **centered cross-end block** `D_(L,R)` of `PL-063`, that escape does retain the zero divisor, but it does not produce a static boundary operator. Fix `R>0` and take smooth probes `f,g in C_c^infinity(0,R)`. Put

`A_f(z)=integral_0^R f(a) exp(-za) da`.

Assuming RH, the exact zero expansion of `PL-063` gives

`exp(L) <g,D_(L,R)f> = - sum_(rho=1/2+i gamma) exp(2 i gamma L) A_f(i gamma) conjugate(A_g(-i gamma)) + O_R(exp(-5L)) ||f||_2 ||g||_2`.

The zero series converges absolutely and uniformly in `L` for these probes. Hence its leading term is a uniformly Bohr almost-periodic function of the boundary location `L`, with frequencies exactly `2 gamma`. Whenever at least one zero-frequency coefficient is nonzero, this function is nonconstant and therefore has **no limit as `L->infinity`**. Consequently the square-root-renormalized fixed-depth family cannot have a weak/form limit on the smooth core under RH.

Moreover, its ordinary long Cesaro mean is zero: linear averaging in `L` kills every nontrivial-zero frequency. Thus the second amplitude scale has a sharp dichotomy:

- without averaging it remains an oscillatory zero-spectrum readout;
- with ordinary linear averaging its first-order zero signal disappears.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION`, and `DECISIVE-NEGATIVE` for the route

`fixed boundary depth + centered completed-Weil residual + exp(L) second amplitude normalization -> nontrivial static weak/form limit -> RH rigidity`.

This does **not** rule out an almost-periodic hull, correlation/spectral measure of the `L`-dynamics, nonlinear averaging, a genuinely growing depth `R(L)`, or another topology. It says that the most direct fixed-depth second-amplitude repair proposed after `PL-066` does not stabilize: under RH itself it becomes the classical zero-phase dynamics in operator-matrix-coefficient clothing.

## Exact second-scale expansion

`PL-063` proves, with `X=exp(2L)`,

`<g,D_(L,R)f> = - sum_rho X^(rho-1) A_f(rho-1/2) conjugate(A_g(conjugate(rho)-1/2)) + O_R(X^(-3)) ||f||_2 ||g||_2`,

where the sum is over nontrivial zeta zeros with multiplicity. This identity comes from the already-continued completed von Mangoldt/Weil explicit formula tested against a compact boundary correlation; it is not a formal continuation of the Euler product.

Multiplying by `exp(L)=X^(1/2)` gives

`exp(L) <g,D_(L,R)f> = - sum_rho exp((2rho-1)L) c_rho(f,g) + O_R(exp(-5L)) ||f||_2 ||g||_2`,

with

`c_rho(f,g)=A_f(rho-1/2) conjugate(A_g(conjugate(rho)-1/2))`.

Under RH, `rho=1/2+i gamma`, so every exponential amplitude becomes unimodular:

`exp((2rho-1)L)=exp(2 i gamma L)`.

This is exactly the square-root centering one expects from the explicit formula: the real-part information has been removed by assuming the critical line, leaving only the zero ordinates as temporal frequencies.

## Absolute convergence on a smooth core

For `f in C_c^infinity(0,R)`, repeated integration by parts on the imaginary axis gives, for every integer `m>=0`,

`|A_f(i gamma)| <= C_(f,m) (1+|gamma|)^(-m)`.

The same holds for `g`. The Riemann--von Mangoldt zero count gives `N(T)=O(T log T)`. Choosing `m` large enough therefore yields

`sum_rho |A_f(i gamma) A_g(-i gamma)| < infinity`.

Hence the RH zero series

`Z_(f,g)(L) := - sum_gamma exp(2 i gamma L) A_f(i gamma) conjugate(A_g(-i gamma))`

converges absolutely and uniformly on the whole real line. It is consequently a uniformly almost-periodic function in Bohr's classical sense, obtained as a uniform limit of finite trigonometric sums.

This smooth-core restriction is intentional. It avoids any endpoint regularity issue and is already enough to falsify weak convergence of the operator family: a weak/form limit would force convergence of every smooth-core matrix coefficient.

## Why a nontrivial almost-periodic coefficient cannot converge

A uniformly almost-periodic function on `R` that has a finite limit as `L->+infinity` must be constant. One quick proof uses relative compactness of its translates together with the relatively dense set of almost periods: recurrence transports values from arbitrarily large `L`, where the function is close to its putative limit, back to any fixed compact region.

The zeta function has no nontrivial zero with ordinate `gamma=0`. Thus every Fourier mode in `Z_(f,g)` is nonzero. For any fixed nontrivial zero ordinate `gamma_0`, the linear functional

`f -> A_f(i gamma_0)`

is not identically zero on `C_c^infinity(0,R)`. We can therefore choose `f` and `g` with

`A_f(i gamma_0) conjugate(A_g(-i gamma_0)) != 0`.

After grouping multiplicities at the same ordinate, the corresponding Fourier coefficient is nonzero, so `Z_(f,g)` is nonconstant. Since

`exp(L)<g,D_(L,R)f> = Z_(f,g)(L)+o(1)`,

that matrix coefficient cannot converge. Therefore the family `exp(L)D_(L,R)` has no weak operator/form limit on any realization whose weak topology tests this smooth core.

This is stronger than saying that the second scale is hard to control. **RH itself predicts persistent recurrence rather than convergence at this scale.**

## Linear averaging erases the zero-sensitive component

Absolute summability also allows termwise Cesaro averaging. For every nonzero `gamma`,

`(1/T) integral_0^T exp(2 i gamma L) dL -> 0`.

Therefore

`lim_(T->infinity) (1/T) integral_0^T Z_(f,g)(L) dL = 0`.

So the obvious repair for the absence of a pointwise limit—ordinary linear time averaging—removes exactly the zero-sensitive part that motivated the second normalization. This statement is only about the first moment. Correlations such as the mean of `|Z_(f,g)|^2`, its Bohr spectrum, or the translation hull can retain the ordinates and are not ruled out here; they are, however, harmonic readouts of an already-inserted explicit-formula divisor rather than a mechanism that forces the divisor onto the critical line.

## Off-line audit

Without RH the same exact expansion contains factors

`exp((2 beta-1)L) exp(2 i gamma L)`

for a zero `rho=beta+i gamma`. Thus the second scale is indeed sensitive to the real parts of zeros: `beta=1/2` is precisely the neutral-amplitude line. But this observation is not promoted to a converse boundedness criterion here. An off-line divisor can contain many frequencies and possible cancellations, and proving that one matrix coefficient must grow would require a separate zero-isolation argument.

The present negative conclusion is cleaner: a candidate static limit already fails in the world where RH is true. Hence it cannot serve as an RH-compatible limiting-operator mechanism.

## Prior-art and novelty audit

The almost-periodic interpretation of square-root-centered explicit-formula data is classical. A. P. Guinand, “Concordance and the harmonic analysis of sequences,” *Acta Mathematica* **101** (1959), 235–271, DOI `10.1007/BF02559556`, developed harmonic reciprocity for almost-periodic weighted sequences. Jeffrey C. Lagarias, “Mathematical quasicrystals and the problem of diffraction,” in *Directions in Mathematical Quasicrystals*, CRM Monograph Series **13** (AMS, 2000), 61–93, DOI `10.1090/crmm/013/03`, explicitly summarizes Guinand's zeta application: under RH the weighted prime-power logarithms and the zero ordinates form a Fourier-dual almost-periodic structure.

Modern limiting-distribution work gives the same warning in a different topology. Amir Akbary, Nathan Ng, and Majid Shahabi, “Limiting distributions of the classical error terms of prime number theory,” *Quarterly Journal of Mathematics* **65**(3) (2014), 743–780, DOI `10.1093/qmath/hat059`, develops `B^2`-almost-periodic explicit-formula expansions for normalized number-theoretic error terms and recalls Wintner's RH-conditional limiting distribution for `exp(-y/2)(psi(exp y)-exp y)`.

Accordingly, no novelty is claimed for “critical-line zeros become oscillatory frequencies after square-root centering.” The line-specific content is the exact bridge to the `PL-063` fixed-depth completed-Weil boundary matrix coefficients and the resulting no-limit theorem for the specific second-amplitude escape left open by `PL-066`.

A targeted search did not locate this exact boundary-Hankel formulation. Search absence is not evidence of originality.

## Prime-lattice and matched-control audit

On the geometric side of the explicit formula, the centered shell still samples the prime-power axis vectors `k e_p`, with phase

`exp(-i xi log(p^k)) = exp(-i xi <k e_p,(log q)_q>)`.

The second amplitude normalization does not manufacture a new interaction among those prime directions. After the completed explicit formula is invoked, it simply converts the zero term from the decaying factor `exp(-L)` under RH into the neutral phase `exp(2 i gamma L)`.

That mechanism is not specific to the rational-prime exponent lattice. Any generalized-prime or trace-formula system with a comparable explicit formula and a divisor on a symmetry line produces the same neutral oscillatory behavior after centering at that line. The rational primes enter through the particular explicit formula whose divisor is being read; almost periodicity itself supplies no new arithmetic rigidity.

This passes the requested falsification test negatively: the construction retains zeta information, but only because the completed explicit formula has already supplied it.

## Analytic-continuation audit

No Euler-product identity is used outside `Re(s)>1`. For each fixed `L`, the prime shell in `D_(L,R)` is finite. The passage from that shell to the zero series is precisely the completed von Mangoldt/Weil explicit formula already audited in `PL-063`. The second normalization is multiplication by the scalar `exp(L)` after that valid identity has been established.

The RH specialization changes `exp((2rho-1)L)` into a phase only after the continued zero divisor is present. Therefore the argument does not smuggle the Euler product into the critical strip.

## Decisive falsification checks

The conclusion rests on five checkable points:

1. `PL-063` supplies the exact centered cross-end zero expansion with remainder `O_R(X^(-3))`, `X=exp(2L)`.
2. Multiplication by `exp(L)=X^(1/2)` changes the remainder to `O_R(exp(-5L))` and the zero factor to `exp((2rho-1)L)`.
3. Under RH those factors are the pure phases `exp(2 i gamma L)`.
4. Smooth compactly supported probes make the zero coefficients absolutely summable, so the resulting Fourier series is uniformly almost periodic.
5. A nonconstant uniformly almost-periodic function cannot converge at `+infinity`, while its ordinary Cesaro mean contains no nonzero-frequency mode.

Failure of the inherited `PL-063` zero expansion would invalidate the finding. Changing to growing depth, an `L`-dependent probe family, nonlinear observables, or an almost-periodic-hull topology lies outside the claim.

## Consequence for the research line

The fixed-depth amplitude branch of `CLUE-mesoscopic-weil-boundary-topology` is narrowed again. The natural `exp(-L)` normalization collapses under RH by `PL-066`; multiplying the centered cross-end residual by the compensating `exp(L)` does keep RH-zero amplitudes at order one, but the result is a recurrent Guinand-type zero-frequency signal, not a static operator limit. Ordinary averaging then deletes that signal.

A surviving mesoscopic construction must therefore do something genuinely different: let the geometry or probe scale move with `L`, retain an almost-periodic dynamical invariant while showing that it adds arithmetic rigidity rather than merely reading the zero divisor, or couple the boundary family to a rational-prime-specific structure not already supplied by the explicit formula. Merely changing the amplitude at fixed depth is no longer an open route.