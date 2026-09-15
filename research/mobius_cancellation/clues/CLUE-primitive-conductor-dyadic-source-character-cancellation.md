---
id: CLUE-mobius-cancellation-primitive-conductor-dyadic-source-character-cancellation
type: research-clue
status: resolved
origin: research-watch
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-296-endpoint-defect-partitions-force-source-cost-inflation.md
  - research/mobius_cancellation/findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md
  - research/mobius_cancellation/findings/MC-320-smooth-modulus-interval-cancellation-prime-shell-conductor-inflation.md
---

# Can primitive source conductors recover the dyadic prime cancellation lost by common-modulus smoothing?

## Observation

`MC-319` shows that the exact natural-scale endpoint forces all relevant Legendre characters into one exceptionally smooth common modulus `q=4P`, but the available Rodosskii conversion of the joint zero-free region is too coarse to resolve one dyadic prime shell at the required harmonic scale `o(1/log y)`.

`MC-320` now closes a tempting substitute: common-modulus smoothness plus even extremely strong ordinary interval cancellation is not a prime-shell discriminator. An explicit character induced from primitive conductor `4` to a source-scale-matched smooth `q` has polylogarithmically bounded sums on every integer interval while taking the constant value `+1` on every shell prime `r congruent to 1 mod 4`.

The control differs from the actual endpoint family in one load-bearing feature. The endpoint characters are primitive quadratic characters built from lower-prime source products, and `MC-296` forces almost the whole endpoint Fourier subspace to have large source cost. The inflated `chi_4` control has primitive conductor `4`; its large smooth modulus is bookkeeping rather than provenance.

## Research question

Can the primitive conductor/source-cost spectrum of the endpoint family be combined with smoothness to prove genuinely dyadic prime-character cancellation at `x asymp y`, at least for one of the many endpoint-biased nonexceptional modes?

The desired statement need not control every character. It is enough to show that among the subset characters forced by the endpoint partition there exists a nonexceptional primitive character `chi` (or the corresponding `chi chi_4` twist needed for the `1 mod 4` projector) for which

\[
\sum_{y<p\le2y}\chi(p)\log p=o(y),
\]

or equivalently a harmonic estimate strong enough to contradict the endpoint bias. A useful theorem must depend on the **primitive** conductor and its lower-prime factorization/source provenance, not merely on the ambient modulus to which all characters can be induced.

## Why it may matter

This is the first analytic discriminator left by the paired obstructions `MC-319` and `MC-320`. The generic binary-code controls can reproduce the endpoint weight hierarchy, and an imprimitive conductor-inflation control can reproduce the common-modulus smoothness plus ordinary interval cancellation. Primitive source provenance is therefore a concrete arithmetic feature not reproduced by either matched control.

If it yields a dyadic prime estimate, the result would attack the exact realizability gap rather than another representation of it. If it does not, the failure should identify whether the obstruction is conductor size, one-prime-shell resolution, a possible exceptional real zero, or lack of a family theorem for the selected multiquadratic character group.

## Decisive test

Audit the primitive conductors `f_I` of the subset characters from the exact natural-scale endpoint package, not just their common multiple `P`.

First partition the endpoint-biased modes by conductor scale relative to `y` and record what `MC-296`, `MC-303`, `MC-305`, and `MC-319` actually force about `f_I`, `P^+(f_I)`, and the number of modes in each scale. Then test the strongest applicable prime-sensitive results for smooth primitive characters: explicit-formula bounds, zero-density/Deuring-Heilbronn refinements, Vaughan/Heath-Brown decompositions coupled to smooth-conductor character sums, or a genuinely collective theorem for the multiquadratic family.

Keep the direction only if the primitive/source information produces a bound strictly sharper than the `MC-319` Rodosskii resolution at `x asymp y`. Kill or narrow it if the endpoint can place all substantially biased nonexceptional modes at conductor scales where known unconditional prime-sensitive estimates remain compatible with an order-`y` dyadic `Lambda` sum, or if every proposed gain survives unchanged for the conductor-`4` inflation control of `MC-320`.

## Evidence boundary

No primitive-conductor dyadic estimate has been proved here. `MC-296` supplies source-cost inflation, not a distribution theorem for the primitive conductor spectrum at the exact scale needed above. `MC-319` supplies a common-modulus joint zero-free region but not the required shell resolution, and `MC-320` supplies a matched obstruction showing why ordinary character sums cannot substitute for prime-sensitive control.

The clue therefore identifies a falsifiable theorem surface; it is not evidence that the endpoint is impossible, not an estimate for `M(x)`, and not an RH consequence.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/mobius_cancellation/findings/MC-321-prime-halasz-montgomery-closes-natural-endpoint-family.md]]

The clue's proposed primitive-conductor discriminator turned out to be stronger than necessary. The KMT/Puchta prime Halász–Montgomery mean-square estimate applies directly to arbitrary prime-supported coefficients and a small set of distinct characters modulo the common `q`. At the exact natural endpoint, the `R` simultaneous one-defect shell biases force an `R`-fold lower bound that contradicts that estimate already from `q\le4y^2`. Thus the dyadic prime-sensitive step exists, but it is a collective family theorem and does not require primitive conductor, smoothness, or zero-free information.