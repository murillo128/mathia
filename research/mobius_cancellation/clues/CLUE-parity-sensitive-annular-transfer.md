---
id: CLUE-mobius-cancellation-parity-sensitive-annular-transfer
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-027-analytic-scale-doubling-iteration-threshold.md
  - research/mobius_cancellation/findings/MC-033-annular-product-fiber-sign-coherence.md
  - research/mobius_cancellation/findings/MC-071-signed-feedback-inverse-zero-free-barrier.md
  - research/mobius_cancellation/findings/MC-082-liouville-parity-sieve-divisor-density-blindness.md
  - research/mobius_cancellation/findings/MC-083-constant-weight-annular-parity-contrast-mertens-square-equivalence.md
  - research/mobius_cancellation/findings/MC-084-source-coupled-exact-sawtooth-annulus-mertens-equivalence.md
  - research/prime_lattice/findings/PL-172-hilbert-schmidt-affine-liouville-chowla-trace-removal.md
---

# Can one source-forced signed annular statistic retain parity and deliver an iterable gain?

## Observation

MC-082's controls `w_+=(1+lambda)/2` and `w_-=(1-lambda)/2` share divisor-density main terms; their difference is in signed Liouville remainders. MC-033 retains signed product-fiber structure, while MC-027 requires a strict gain with controlled iteration losses. MC-071 warns that estimating an isolated inverse at the desired power scale may already assume the target zero-free region.

A separate representation audit in PL-172 gives a concrete additional warning: the diagonal operator with entries `lambda(n)lambda(n+h)n^-s` is Hilbert--Schmidt for `Re(s)>1/2`, but `det_2` deletes its first trace, exactly the unresolved fixed-shift correlation at scale `s`. All retained powers there are already absolutely convergent. Operator existence does not supply the missing signed estimate.

## Research question

Does the existing product-annulus decomposition supply a bounded bilinear or coupled statistic that distinguishes parity controls before absolute values are taken, and whose independently available estimate produces a strict improvement under the MC-027 scale iteration? The test concerns a parity-sensitive residual, rather than another regular factorization or scalar local-density statistic.

## Why it may matter

It asks for the missing arithmetic input in a form that can actually change a cancellation exponent. It can also reveal that an apparently new observable merely stores the full summatory target or a comparably difficult correlation.

## Decisive test

Choose one weight and factor range forced by the exact annular identity, before testing its sign. Calculate its response to the parity controls, explicitly accounting for square-free support when passing from Liouville to Möbius. Preserve the signed remainder through the entire proposed transfer.

Then write the complete recurrence with exceptional ranges, truncation errors, and iteration losses. Derive its exponent consequence from a precisely stated arithmetic input, and audit whether that input is already an equivalent Mertens/inverse bound or an unproved fixed-shift correlation. The direction survives only with a nontrivial parity response and an independent quantitative input capable of a strict net gain. An exact reduction back to the target, a regularization deleting the response, or a recurrence with no gain kills this candidate.

## Evidence boundary

No source-forced nonconstant statistic with an independently available power estimate is established here. Parity sensitivity alone proves no cancellation, and failure of one annular statistic would not rule out all bilinear or sieve methods. This question does not reopen the accepted local mean-absolute-transfer clue as a duplicate.

## Research disposition

Accepted in further narrowed form. `MC-083` performs the first calibration: the constant-weight complete product annulus is an exact square-free parity contrast, but for every exponent above `1/2` it is equivalent, up to an `O(N log N)` hyperbola interior, to the corresponding global Mertens bound; the RH epsilon-family is equivalent as well. Thus merely retaining parity is insufficient, and the constant-weight candidate is dead.

`MC-084` tests the opposite extreme. The complete exact sawtooth annulus is genuinely nonconstant, but once it is kept with the source-prescribed coarse counterterms `N^2 H(N)^2 - M(N)^2/2`, the resulting annular residual is `2M(N)-M(N^2)` up to another `O(N log N)` interior. Its `O(N^{2 beta})` bound is therefore equivalent to the global `M(x)=O(x^beta)` bound for every `beta>1/2`, and its epsilon-family is RH-equivalent. Full sawtooth coupling is not an independently cheaper input.

The unresolved question is now restricted to **strict partial** source-forced weights or couplings before full sawtooth recombination—most naturally a proper finite Fourier family or a justified proper slab subfamily. Such a candidate must avoid both the constant-weight recovery of `MC-083` and the complete-coupling recovery of `MC-084`, come with an independently available quantitative estimate, and still pay the `MC-031` truncation budget plus the full `MC-027` iteration and scale-coverage ledger.