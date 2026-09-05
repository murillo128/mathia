# PL-166 — FMZ’s unconditional comparison step imposes a primorial frequency horizon on growing-prime full-support detectors

## Claim

The most direct unconditional way to extend the finite-prime zero-phase program of `PL-162`--`PL-165` to a growing set of primes runs into a quantitative frequency barrier before the available first-order prime bias can compete with the zero-count baseline.

Ford--Meng--Zaharescu (FMZ) prove, as Lemma 2 in their simultaneous-distribution paper, that for

`1 < x <= exp(log T / (50 log log T))`,

one has

`sum_(0<gamma<=T) (x^(i gamma) - x^(rho-1/2))`
` << T log^2(x)/log T + T/log^10(T)`.

This is the unconditional step that replaces the phase `x^(i gamma)` by the normalized zero quantity `x^(rho-1/2)`; on RH the two are identical and the step is unnecessary.

Now take the first `pi(y)` prime coordinates

`alpha_p = log p / (2 pi),    p <= y`,

so a Fourier character `m=(m_p)` has multiplicative frequency

`x_m = exp(2 pi <m,alpha>) = product_(p<=y) p^(m_p)`

when `<m,alpha> > 0`. A full-support product detector with fixed coordinate degree `J>=1` contains the positive extreme character `m_p=J` for every `p<=y`, hence

`log x_max = J theta(y)`,

where `theta(y)=sum_(p<=y) log p` is Chebyshev's function. Therefore any argument that applies the FMZ unconditional comparison termwise to the detector's full Fourier support must at least satisfy

`J theta(y) <= log T/(50 log log T)`.

For fixed `J`, the prime number theorem gives the necessary horizon

`y << log T/log log T`.

This already lies far below the scale at which the sum of all available first-order prime-power biases can become comparable with `N(T)`. For a normalized nonnegative torus polynomial, every Fourier coefficient has modulus at most `1`, while FMZ's Landau term is supported only when `x_m` is a prime power. Consequently the total contribution of the one-prime fundamental modes `m=e_p` is at most of order

`T sum_(p<=y) log p/sqrt(p) = O(T sqrt(y))`.

Since `N(T) asymp T log T`, its normalized size is `O(sqrt(y)/log T)`. Throughout the FMZ-compatible primorial horizon this is

`O(1/sqrt(log T log log T)) = o(1)`.

To make even this maximal additive first-order bias comparable to the baseline would require roughly `y asymp (log T)^2`; a full-support degree-`J` detector there reaches

`log x_max = J theta(y) asymp J (log T)^2`,

which is enormously beyond FMZ's unconditional comparison range.

Thus **the existing FMZ normalization cannot by itself turn growing prime dimension into an order-one RH-sensitive full-support phase detector**. Before one even confronts the lack of dimension-uniform constants in the fixed-dimensional FMZ theorem or the accumulation of errors over exponentially many Fourier modes, the primorial frequency of the natural mixed characters has already outrun the available off-RH comparison range.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + NEGATIVE/OBSTRUCTION + METHOD-HORIZON`. The FMZ lemma and its range are literature facts; the primorial horizon and bias comparison are direct consequences. This is a restriction on a proof method, not a theorem that the actual growing-dimensional zero-phase distribution is Haar or that shrinking-target mechanisms cannot work.

## The FMZ bridge is exactly the off-RH step that growing prime phases need

For a zero `rho=beta+i gamma`, a prime-lattice character along the vertical orbit is

`x^(i gamma)`.

Landau-type formulas are naturally stated with `x^rho`, whose size depends on `beta`. FMZ isolate this issue by comparing the actual phase sum with the normalized expression `x^(rho-1/2)`. Their Lemma 2 states that, unconditionally and uniformly in the displayed range,

`sum_(0<gamma<=T) (x^(i gamma)-x^(rho-1/2))`
` << T log^2(x)/log T + T/log^10(T)`

for

`1<x<=exp(log T/(50 log log T))`.

The restriction is therefore not an arbitrary Fourier cutoff imported from the prime-lattice language. It is attached to precisely the operation needed to erase the unknown real parts of zeros without assuming RH. FMZ then use this estimate inside a fixed-dimensional Fourier expansion of a torus test function.

For the prime coordinates `alpha_p=log p/(2 pi)`, the usual torus/Fourier duality becomes the exponent lattice exactly:

`exp(2 pi i <m, gamma alpha>) = exp(i gamma sum_p m_p log p)`
` = x_m^(i gamma)`,

with `x_m=product_p p^(m_p)` for positive logarithmic frequency. Hence the size of a Fourier mode is measured not by `||m||` alone but by the arithmetic energy

`log x_m = <m,(log p)_p>`.

This is the same prime-log linear functional that defines `log n` on exponent vectors. A detector that genuinely couples many prime coordinates necessarily creates multiplicative frequencies whose logarithms add across those coordinates.

## Full-support product Fourier geometry produces a primorial ceiling

Let `P(y)={p:p<=y}`. Suppose a trigonometric detector has coordinate degree at most `J` and includes its full positive corner `m=(J,...,J)`. This includes the standard product constructions obtained by multiplying nonconstant one-coordinate positive kernels. The corner frequency is

`x_max = product_(p<=y) p^J`,

so

`log x_max = J theta(y)`.

If every Fourier mode is to pass through the FMZ comparison lemma, the corner alone forces

`J theta(y) <= log T/(50 log log T)`.

Using `theta(y)~y`, fixed degree gives

`y <= (1+o(1)) log T/(50 J log log T)`.

This is only a necessary condition for the naive growing-dimensional extension. It is not sufficient: FMZ's main simultaneous-distribution theorem fixes the dimension `n`, its smoothness hypotheses and constants are not supplied uniformly for `n=pi(y)`, and a product detector can have exponentially many modes whose individual error terms would also have to be summed. Those additional difficulties can only tighten the accessible range; they cannot remove the corner-frequency obstruction.

The same calculation exposes why using only low coordinate degree does not solve the problem. Even at `J=1`, the all-prime corner is the primorial

`product_(p<=y) p = exp(theta(y))`.

Thus the obstacle comes from **cross-prime support**, not from high powers on any individual prime axis.

## The first-order arithmetic bias remains subcritical inside that horizon

FMZ's Landau term is supported on multiplicative frequencies that are prime powers. For the rationally independent prime-log coordinates, a mixed vector involving at least two distinct primes gives a composite with at least two prime factors and hence has von Mangoldt weight zero. The first-order resonant contribution therefore comes from axis modes `m=k e_p`, not from generic mixed-prime corners.

For the fundamental axis modes `e_p`, the arithmetic weight is `Lambda(p)/sqrt(p)=log p/sqrt(p)`. If `F>=0` has normalized Haar mean `1`, then every Fourier coefficient satisfies

`|c_m| = |integral F(theta) exp(-i<m,theta>) dtheta| <= integral F = 1`.

Consequently even the optimally aligned sum of all fundamental prime biases up to `y` is bounded by

`sum_(p<=y) log p/sqrt(p) = O(sqrt(y))`,

and in fact is asymptotic to `2 sqrt(y)` by partial summation and the prime number theorem. The corresponding raw FMZ discrepancy has scale at most `T sqrt(y)`, while

`N(T) = (T/(2 pi)) log(T/(2 pi e)) + O(log T)`.

Hence its relative scale is at most

`O(sqrt(y)/log T)`.

At the largest `y` compatible with the primorial corner and fixed `J`, this becomes

`O(1/sqrt(log T log log T))`.

The additive first-order bias therefore vanishes after normalization throughout the region where the direct FMZ comparison can still see every full-support mode. Reaching relative order one from this additive mechanism alone would demand `sqrt(y)` of order `log T`, i.e. `y` of order `(log T)^2`, far outside the comparison horizon.

Higher prime powers do not change the conclusion at first order: for each fixed prime their weights form a rapidly convergent tail on the `sqrt{x}` scale. What remains potentially interesting is not a larger sum of independent axis biases but a genuinely nonlinear or higher-order coupling among many prime coordinates.

## Relation to PL-163 and PL-165

`PL-163` found a one-dimensional Fourier-resolution obstruction: shrinking phase windows require modes whose multiplicative frequency eventually exceeds the useful Landau--Gonek range. `PL-165` then showed that merely enlarging the ambient prime torus does not help when arithmetic control remains confined to a fixed finite set of coordinates.

The present finding quantifies the first obvious attempt to fill that gap with the known simultaneous-distribution machinery. If one lets the controlled set itself grow through `p<=y`, the Fourier dual of a full-support detector contains multiplicative frequencies up to a primorial power. FMZ's unconditional normalization only reaches `log x << log T/log log T`, which translates into `y << log T/log log T` even at fixed degree. At that scale the sum of the first-order prime biases is still `o(N(T))`.

So the missing theorem after `PL-165` is not merely "FMZ with the number of coordinates allowed to grow." A useful result would need substantially more: either uniform control for mixed frequencies far beyond the primorial horizon, a mechanism that suppresses those high mixed modes while retaining genuine cross-prime coupling, or an approach that avoids the off-RH normalization step entirely without assuming the conclusion.

## Adversarial audit and limits

1. **This is a method obstruction, not a distribution theorem.** Nothing here proves that the actual vectors `(gamma log p mod 2 pi)_(p<=y)` are asymptotically Haar in growing dimension, nor that they miss shrinking exceptional sets. A stronger theorem could bypass the FMZ range.

2. **The full-support hypothesis is load-bearing.** A sparse Fourier statistic can omit the primorial corner and therefore avoid the exact inequality `J theta(y)<=log T/(50 log log T)`. But a statistic using only single-coordinate or finitely supported modes falls back toward the marginal/additive limitations isolated in `PL-165`. A viable sparse construction would have to demonstrate nontrivial cross-prime information without recreating large multiplicative frequencies.

3. **Tiny high-mode coefficients may permit truncation.** A product detector can contain extreme modes with coefficients so small that one need not estimate them individually. The finding does not rule out such a design. It says that the direct termwise FMZ treatment of the full Fourier support, or any argument requiring uniform control of all non-negligible full-support modes, hits the stated ceiling.

4. **FMZ's theorem itself is fixed-dimensional.** The derivation does not apply their final asymptotic theorem as a black box with `n=pi(y)`. It uses the explicit one-frequency range in Lemma 2 to obtain a necessary condition for a naive growing-dimensional extension. Uniform smoothness constants and error accumulation are separate unsolved issues.

5. **On RH the normalization barrier disappears.** If every zero has `beta=1/2`, then `x^(i gamma)=x^(rho-1/2)` identically. That does not weaken the obstruction for an RH proof: an unconditional argument designed to exclude off-line zeros cannot assume this identity. It does show that the ceiling belongs to the off-RH comparison method rather than to the abstract torus flow.

6. **Other explicit formulas can have different `x` ranges.** Landau--Gonek variants, weighted formulas, or hypotheses on zero density may extend useful frequency ranges in particular settings. The literature audit did not locate a replacement theorem giving the unconditional, simultaneous, growing-dimensional prime-phase control needed here. The durable claim is therefore tied specifically to the FMZ comparison route, not to all possible explicit-formula technology.

7. **The `O(sqrt(y))` bias is only first-order.** It bounds the additive prime-power resonances visible in the FMZ first moment. It does not exclude higher correlations, determinants, nonlinear observables, or a zero-conditioned mechanism in which mixed-prime modes acquire information not present in the first Landau term.

A decisive falsification of the stated method barrier would be an unconditional comparison replacing FMZ Lemma 2 over a frequency range large enough to include `x=exp(c (log T)^2)` with sufficiently uniform errors for growing-dimensional mixed-prime Fourier families, or a detector theorem proving that the high mixed modes may be discarded while still producing an order-one RH-sensitive signal from growing prime phases.

## Prior-art and novelty audit

The primary source is Kevin Ford, Xianchang Meng, and Alexandru Zaharescu, “Simultaneous distribution of the fractional parts of Riemann zeta zeros,” *Bulletin of the London Mathematical Society* **49**(1) (2017), 1--9, DOI `10.1112/blms.12001`, arXiv:1511.06814. Their theorem studies a **fixed** vector of frequencies, and their Lemma 2 gives the exact unconditional range used above. The paper also makes explicit that the nonzero first-order terms arise when the multiplicative frequency is a prime power.

The earlier Ford--Zaharescu one-dimensional work and later variants on fractional parts of zero ordinates are close prior art for the phase-distribution side, while classical Landau--Gonek formulas are prior art for the prime-power resonance. A targeted audit for growing-dimensional zeta-zero torus distribution, shrinking targets with prime-log coordinates, and uniform Landau--Gonek/Fourier control did not locate the specific primorial-horizon comparison above or a theorem that removes it in the required unconditional growing-dimensional setting.

Accordingly, no novelty is claimed for FMZ's lemma, the prime number theorem estimates, or the fact that Fourier characters become multiplicative frequencies. The durable derived content is the quantitative conjunction: **full-support growth through the first primes converts the FMZ frequency ceiling into a primorial cutoff `y << log T/log log T`, while the entire first-order prime bias available below that cutoff remains `o(1)` relative to the zero-count baseline.**

## Consequence for the research line

The next useful target should not be another fixed-dimensional equidistribution statement. The line now has three nested barriers: fixed finite marginals do not control growing exceptional fibers (`PL-165`); shrinking one-coordinate windows outrun useful Fourier resolution (`PL-163`); and the obvious simultaneous FMZ bridge reaches only a primorially small growing prime set before first-order arithmetic bias becomes significant.

A genuinely new escape must therefore supply **uniform mixed-prime information at growing support** rather than simply accumulate more axis biases. Plausible targets include a sparse cross-prime statistic whose maximal arithmetic energy stays low while its coupling strength grows, a higher-order zero correlation with prime-lattice support that survives normalization, or a target-relative mechanism in which near-frontier zeros themselves force correlations among many prime phases. Any such proposal should be tested first against the primorial frequency accounting above before more elaborate geometry is built around it.