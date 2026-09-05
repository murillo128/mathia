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
  - research/mobius_cancellation/findings/MC-085-low-frequency-annular-coupling-resolution-equivalence.md
  - research/mobius_cancellation/findings/MC-086-initial-reciprocal-slab-resolution-equivalence.md
  - research/mobius_cancellation/findings/MC-087-sparse-annular-omission-reconstruction-barrier.md
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

`MC-085` closes the most natural strict-partial Fourier interpolation between those extremes. For the source-prescribed initial Fourier family `1<=h<=K`, coupled only to the annular part and the exact coarse counterterms, the reverse-recovery identity shows that whenever the published Huxley--Watt truncation remainder is made subordinate to a target power, the proper Fourier coupling is already equivalent to that Mertens power. In particular, the epsilon-family remains RH-equivalent even with the genuinely proper cutoffs `K_epsilon=N^(1-epsilon/2)`.

`MC-086` closes the analogous **physical-space initial reciprocal-slab family**. Keeping the source-natural slabs `1<=k<K` and the exact coarse counterterms leaves a high-index tail supported on `N<mn<=N^2/K`, whose generic absolute size is `O(N^2(1+log K)/K)`. Once `K=N^theta` is large enough to push that complement below `N^(2 beta)`, namely `theta>2-2 beta`, the proper slab coupling is again equivalent to `M(x)=O(x^beta)`. The epsilon-family remains RH-equivalent for the proper cutoffs `K_epsilon=N^(1-epsilon/2)`. Thus changing from frequency space to the natural floor-slab partition does not lower the power-level reconstruction threshold.

`MC-087` removes the initial-slab restriction for physical-space support selection. For an arbitrary omitted subset `E_N` of annular pairs, boundedness of the exact sawtooth gives `|T_N(E_N)|<=#E_N/2`; whenever `#E_N=O(N^(2 beta))`, the retained annulus plus the exact coarse counterterms is again equivalent to `M(x)=O(x^beta)`. Thus a selective or noninitial slab mask is not a weaker carrier merely because its omitted support is small enough to restore absolutely at the target scale.

The unresolved question is now narrower than finding a proper or selective source-natural truncation. A physical-space survivor must omit **supercritical pair mass** and obtain genuinely arithmetic signed control of that complement, or estimate retained and omitted contributions jointly before absolute values. A Fourier or other weighted survivor must likewise control a genuinely information-losing coefficient complement rather than reconstruct the full residual at target resolution. A genuinely bilinear/joint coupling that avoids exact target recovery remains open. Any survivor must still close the full `MC-027` iteration and scale-coverage ledger.