---
id: CLUE-mobius-cancellation-power-cancellation-aware-pretentiousness
type: research-clue
status: proposed
origin: adversarial
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-002-prime-harmonic-ceiling-single-scale-pretentiousness.md
---

# Can power-cancellation-aware pretentiousness evade the MC-002 ceiling for Möbius?

## Observation

`MC-002` correctly isolates an `O(log log x)` information ceiling for the standard prime-only pretentious distance when it is fed through the usual single-scale Halász exponential. A directly relevant prior-art branch goes further: Jung and Lemke Oliver, *Pretentiously detecting power cancellation* (Math. Proc. Camb. Phil. Soc. 154 (2013), 481–498, DOI `10.1017/S0305004112000655`, arXiv `1111.1921`), explicitly shows that classical pretentiousness does not by itself detect power cancellation and introduces stronger, prime-power-sensitive notions intended to do so.

That literature does not invalidate `MC-002`; it suggests a concrete candidate for the "additional datum" that `MC-002` says an RH-relevant pretentious route would need. It is especially natural here because the standard distance cannot distinguish Möbius from Liouville at primes, whereas their prime-power values differ immediately at `p^2`.

## Research question

When the Jung–Lemke Oliver power-cancellation-aware distances and transfer criteria are specialized to Möbius, Liouville, and other tractable multiplicative comparators, do they retain quantitatively useful information beyond the standard `1/p` prime-harmonic scalar without merely repackaging an already RH-equivalent power-cancellation hypothesis?

In particular, determine whether the prime-power contribution distinguishing `mu` from `lambda` can support a genuinely stronger unconditional exponent for `M(x)`, or whether the generalized-distance hypotheses become finite/useful only at exponents for which the needed comparator cancellation is already as hard as the Möbius target.

## Why it may matter

This is a literature-supplied candidate mechanism aimed exactly at the gap identified by `MC-002`: enrich the information carrier rather than trying to make the same standard distance larger. A positive result would give the Möbius line a mathematically established framework for tracking information that the prime-only distance discards. A negative result would sharpen `MC-002` by showing that even a known power-cancellation-aware refinement does not yield an RH-relevant bootstrap for Möbius.

## Decisive test

Reconstruct the exact generalized distances and transfer theorems of Jung–Lemke Oliver and apply them first to the pair `(mu, lambda)`, where the prime values agree but the prime-power values differ. Compute the convergence/scale thresholds of the generalized distance explicitly, then combine them with the strongest unconditional partial-sum bounds available for the comparator.

Kill the direction if every parameter range capable of transferring an exponent `1/2+epsilon` requires as input an equally strong power-cancellation estimate for the comparator, or if the relevant generalized quantity collapses to already-known information. Keep it only if the prime-power-sensitive datum yields a strict, non-circular quantitative improvement for Möbius or exposes a new intermediate estimate whose proof obligation is genuinely weaker than RH-scale cancellation itself.

## Evidence boundary

No stronger Möbius bound is established here. The cited paper proves general power-cancellation transfer results for strengthened notions of pretentiousness; it does not establish that their hypotheses give new unconditional control of `M(x)`. The proposed Möbius/Liouville specialization and non-circularity audit remain to be carried out by the owning Research Watch.