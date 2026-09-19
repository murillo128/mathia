# VIS-312 — the full Wang ratio spectrum has no isolated frequencies

## Claim

Keep the Wang prime-power packet and remainder from `VIS-309`--`VIS-311`,

`D_x(t)=sum_(q=p^k) a_q q^(-it)`,

`a_q=(Lambda(q)/sqrt(q)) min(q/x,x/q)`,

and

`R_(x,H)(T)=sum_(lambda) B_lambda exp(-i lambda T)`

after grouping equal ratio frequencies `lambda=log(q/r)`.

For every fixed `x>1` and `H>0`, the nonzero **cross-base prime-ratio** frequencies occurring in this grouped spectrum are dense in `R`. More precisely, the set

`Lambda_prime(H)={log(p/q): p,q distinct primes, K_H(log(p/q)) != 0}`,

where

`K_H(lambda)=integral_0^H exp(-i u lambda) du`,

is dense in `R`.

Consequently the full grouped Wang frequency set has no isolated points. If `lambda_0` is any fixed frequency with `B_(lambda_0) != 0` and

`delta_(lambda_0,Y)=min{|lambda_0-mu|: mu in Lambda_Y, mu != lambda_0}`

is its nearest-neighbor spacing inside the hard cutoff `Lambda_Y` of `VIS-311`, then

`delta_(lambda_0,Y) -> 0`

as `Y->infinity`.

In particular, the weighted nearest-neighbor energy

`W_(x,H)(Y)=sum_(lambda in Lambda_Y) |B_(lambda,Y)|^2/delta_(lambda,Y)`

cannot have a finite cutoff-free limit. In fact `W_(x,H)(Y)->infinity`: once one fixed nonzero cross-base coefficient is retained, its coefficient is independent of larger cutoffs while its nearest-neighbor spacing tends to zero.

Therefore the `VIS-311` weighted Montgomery--Vaughan estimate **cannot be made nontruncated merely by sending `Y->infinity` in the same nearest-neighbor-spacing functional**. Any cutoff-free finite-window argument must replace pointwise frequency isolation by scale-local density, block separation, an integral-kernel estimate, or another energy notion that remains meaningful for a dense frequency set.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL PRIME-QUOTIENT DENSITY + NEGATIVE/PROOF-METHOD OBSTRUCTION + NO-NOVELTY-CLAIM`.

This does not show that the true finite-window mean square is large and does not supply a lower bound on the required averaging horizon. It closes only the direct infinite-spectrum continuation of the nearest-neighbor Hilbert representation used in `VIS-311`.

## 1. Prime quotients already make the log-frequency set dense

A classical theorem states that the quotient set of rational primes

`{p/q: p,q prime}`

is dense in the positive real numbers. Equivalently, because `log:(0,infinity)->R` is a homeomorphism,

`{log(p/q): p,q prime}`

is dense in `R`.

The density can also be seen directly from the prime number theorem. Fix `c>0` and let `eta_j downarrow 0`. For each fixed `eta_j`, the PNT implies that sufficiently large multiplicative intervals `[X,(1+eta_j)X]` and `[cX,(1+eta_j)cX]` contain primes. Choosing such primes `q_j` and `p_j` gives

`c/(1+eta_j) <= p_j/q_j <= c(1+eta_j)`,

hence

`log(p_j/q_j) -> log c`.

Choosing the scales increasingly large gives infinitely many distinct approximants. For `c=1`, the same PNT interval contains arbitrarily many primes for large enough `X`, so the numerator and denominator may be chosen distinct; alternatively use two adjacent multiplicative subintervals whose relative separation tends to zero.

Since ordinary primes are themselves prime powers, these frequencies are a subset of the Wang ratio spectrum. No prime-power-specific density theorem is required.

## 2. The Wang kernel removes only a discrete set of frequencies

For `lambda != 0`,

`K_H(lambda)=(1-exp(-iH lambda))/(i lambda)`,

with continuous value `K_H(0)=H`. Its zero set is the discrete lattice

`{2 pi n/H: n in Z, n != 0}`.

Every open interval contains infinitely many distinct prime-quotient log frequencies by the preceding construction. Removing the discrete kernel-zero set therefore leaves a dense set of prime-ratio frequencies for which `K_H(lambda) != 0`.

For distinct primes `p,q`, unique factorization makes the ratio `p/q` a unique cross-base representation in the prime-power spectrum. Hence its grouped coefficient is simply

`B_(log(p/q))=a_p a_q K_H(log(p/q))`

up to the fixed orientation convention. The taper coefficients `a_p,a_q` are strictly positive, so these retained frequencies have nonzero grouped coefficient.

Thus the **nonzero coefficient support itself**, not merely an ambient superset of possible ratios, is dense.

## 3. Every fixed retained frequency loses nearest-neighbor isolation

Let `lambda_0` be a fixed grouped frequency with nonzero coefficient. Because the nonzero cross-base support is dense, for every `epsilon>0` there is another supported prime-ratio frequency `mu` with

`0<|mu-lambda_0|<epsilon`.

That approximating ratio uses finite primes, so it belongs to `Lambda_Y` once `Y` exceeds those primes. Therefore, as the hard cutoff grows,

`delta_(lambda_0,Y)<=|mu-lambda_0|<epsilon`.

Since `epsilon` is arbitrary,

`delta_(lambda_0,Y)->0`.

For a fixed cross-base `lambda_0=log(p/q)`, the grouped coefficient stabilizes exactly once `Y>=max(p,q)`, because no other prime-power pair represents the same reduced ratio. Choose any such frequency with `K_H(lambda_0) != 0`. Then

`W_(x,H)(Y) >= |B_(lambda_0)|^2/delta_(lambda_0,Y) -> infinity`.

This divergence is fully compatible with the finite-cutoff upper bound of `VIS-311`,

`W_(x,H)(Y) << Y x^2 log^3(3x)`.

That estimate was never uniform in the cutoff; the present result identifies why a cutoff-free nearest-neighbor limit cannot exist.

## 4. What this rules out — and what remains live

`VIS-311` showed that keeping coefficient-weighted local spacing instead of one global minimum gap removes two powers of `x` from the sufficient finite-window horizon. A natural next thought is to avoid the hard tail entirely and apply the same weighted Hilbert inequality directly to the infinite grouped series.

The dense-spectrum result rules out exactly that move. The obstruction appears before any delicate coefficient estimate: an infinite nearest-neighbor spacing `delta_lambda` is identically zero on the full support, so the same denominator used by the finite Montgomery--Vaughan inequality no longer defines a useful global weight.

This does **not** rule out energy-sensitive infinite-tail control. It points to the structure such a proof must retain. Plausible surviving representations include:

- dyadic or smooth frequency/height blocks with finite local density estimates inside each block;
- large-sieve or nonharmonic-Fourier bounds formulated through counts of frequencies in intervals rather than individual nearest-neighbor gaps;
- direct control of the finite-window kernel `min(V,1/|lambda-mu|)` against coefficient energy;
- decompositions separating the dense high-height tail from the coefficient-heavy near-`x` spectrum before recombination.

The next useful theorem should quantify one of those aggregate-density mechanisms, or exhibit a sparse resonant family that defeats it. Reapplying the `VIS-311` nearest-neighbor functional to the unpartitioned infinite spectrum is now a closed branch.

## Prior art and novelty boundary

David Hobby and D. M. Silberger, **Quotients of Primes**, *American Mathematical Monthly* 100:1 (1993), 50--52, DOI `10.1080/00029890.1993.11990364`, is direct prior art for density of quotients of rational primes. Later quotient-set literature treats this density as classical. No novelty is claimed for that theorem or for its logarithmic reformulation.

The weighted nearest-neighbor Hilbert input remains the classical Montgomery--Vaughan inequality already audited in `VIS-194` and `VIS-311`. The durable Mathia content here is only the specialization of classical prime-quotient density to Wang's exact grouped ratio support and the resulting negative conclusion for the proposed cutoff-free limit of the `VIS-311` spacing functional.

## Boundaries and falsification

The conclusion concerns the **representation used by the nearest-neighbor Hilbert bound**, not the true dephasing rate of `R_(x,H)`. Dense frequencies may carry rapidly decaying coefficients, and a different aggregate-density inequality may still give a strong finite-window estimate.

The density proof uses arbitrarily large primes. It therefore says nothing by itself about the quantitative rate at which `delta_(lambda_0,Y)` collapses with `Y`; deriving that rate would require stronger information about primes in short multiplicative intervals. No such rate is used here.

The divergence statement needs only one fixed nonzero grouped coefficient. It would fail only if all cross-base prime-ratio coefficients vanished for the chosen `H`, but the kernel zero set is discrete while the prime-ratio support is dense, so that cannot occur.

Falsify the finding by exhibiting an isolated nonzero frequency in the full Wang ratio support, a failure of prime-quotient density in the required positive-real topology, an additional collision that makes a cross-base prime ratio coefficient cutoff-dependent, or a version of the claimed nearest-neighbor functional whose spacing remains positive after the full dense support is included.

## Dependencies

- `VIS-309`: exact full Bohr spectrum and second moment of the Wang remainder.
- `VIS-310`: hard-cutoff finite-window reduction.
- `VIS-311`: coefficient-weighted nearest-neighbor spacing functional and cubic sufficient horizon.
- `CLUE-wang-fixed-source-packet-localization`: accepted finite-window localization clue.

## Research consequence

The hard cutoff in `VIS-311` cannot be removed by a formal `Y->infinity` passage inside the same nearest-neighbor spacing inequality. The full Wang ratio spectrum is dense, so a genuinely nontruncated argument must be **density-sensitive rather than isolation-sensitive**.

This sharpens the live branch without resolving it: the next coherent attack is an aggregate local-density/energy estimate for the infinite spectrum, or an explicit exceptional-resonance construction showing why such an estimate cannot reach the natural Wang window.