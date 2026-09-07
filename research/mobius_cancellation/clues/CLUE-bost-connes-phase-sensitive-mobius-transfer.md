---
id: CLUE-bost-connes-phase-sensitive-mobius-transfer
type: research-clue
status: proposed
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/prime_lattice/findings/PL-211-bost-connes-mobius-kms-two-threshold.md
---

# Can a phase-sensitive Bost--Connes observable transfer to Mertens excursion?

## Observation

`PL-211` tests a genuinely source-forced arithmetic object rather than a programmable prime-label model. In the canonical Bost--Connes divisibility representation, the finite-prime observable

`M_F = product_(p in F) (1 - 2 E_p + E_(p^2))`

has the Möbius values `1,-1,0` on the inspected prime exponents. Its KMS second moment is nevertheless

`||M_F||_2^2 = product_(p in F) (1-p^(-2 beta))`,

so the threshold `beta=1/2` is entirely square-free-support information: replacing the Möbius sign at each prime by arbitrary unimodular phases leaves the same threshold. The actual oriented finite observables become `L^2`-coherent only for `beta>1`.

This gives the Möbius line a source-specific matched control that is stronger than the generic finite-state controls already classified there. A critical-half threshold inside an arithmetic representation is not enough if the statistic has squared away the parity orientation that Mertens cancellation consumes.

## Research question

Is there a canonical Bost--Connes/KMS statistic built from the same source-forced divisibility algebra that remains genuinely sensitive to the Möbius orientation at or across `beta=1/2` and yields a quantitative bound on first-absolute Mertens excursion that is cheaper than controlling `M(x)` itself?

Equivalently, can one identify a phase-sensitive cross-prime or cross-scale correlation whose critical behavior changes for the actual Möbius phases but not for arbitrary unimodular prime-phase controls with the same square-free support?

## Why it may matter

The Möbius line has repeatedly found that generic summaries can miss excursion while fully arithmetic representations can simply re-encode the target. `PL-211` supplies an intermediate testbed: the algebra and divisibility relations are canonical, but the most obvious critical-half norm is provably phase-blind. A surviving oriented statistic would therefore have to use more than support while still being structurally cheaper than the Mertens endpoint.

A negative result would also be useful: if every natural KMS statistic with controlled critical behavior factors through square-free support or loses orientation before `beta=1`, then the Bost--Connes critical-half route should be removed from the Möbius frontier rather than treated as latent RH evidence.

## Decisive test

Choose one canonical oriented observable or covariance from the Bost--Connes divisibility algebra that does not factor through `M_F^*M_F`. Compute its finite-prime KMS moments/correlations exactly enough to compare the actual Möbius orientation with the matched family obtained by replacing each local `-1` by an arbitrary unimodular phase.

Keep the direction only if the actual orientation has a source-forced quantitative property near `beta=1/2` that fails on those matched phase controls and can be transferred to an unbounded sequence of first-absolute Mertens bounds without assuming an RH-equivalent estimate. Kill it if the candidate remains phase-blind, becomes coherent only in the absolutely convergent `beta>1` regime, or reconstructs the Möbius target at comparable cost.

## Evidence boundary

`PL-211` proves the support/orientation threshold split for one canonical finite-prime observable. It does not prove that a useful phase-sensitive KMS statistic exists, nor that Bost--Connes dynamics controls Mertens excursion. This clue is a cross-line handoff and is not evidence for RH or for a new Möbius bound.