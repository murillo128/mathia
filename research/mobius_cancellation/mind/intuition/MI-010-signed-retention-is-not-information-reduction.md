# MI-010 — Signed retention needs genuine information reduction on both the omitted and retained sides

**Evidence level:** supported through MC-090 by exact parity controls, reconstruction thresholds, common-prime scale reduction, and the unsifted top-mode obstruction

## Core intuition

A useful Möbius carrier must retain signed arithmetic and also reduce the target information budget. Earlier controls showed that sign, source origin, proper truncation, sparsity, and selective geometry are not enough when a discarded complement can be restored generically at the target scale. The common-prime results sharpen that principle in both directions: a support-supercritical complement can nevertheless be genuinely cheaper when arithmetic self-similarity reduces it to smaller Mertens scales, but that gain is useless if the retained statistic still contains the unsifted top-scale target mode with coefficient one.

Information deficit is therefore not a support-counting property. It is an exact decomposition property of the whole retained/omitted split.

## Strongest justified principle

MC-082 shows that unsigned divisor-density information can erase Liouville parity. MC-083--MC-087 show that several signed, proper, and selective source carriers remain quantitatively Mertens-equivalent whenever their omitted contribution is generically target-subordinate.

MC-088 crosses that generic support barrier. Omitting pairs sharing one prime gives a set of supercritical cardinality, yet finite Euler-factor deletion rewrites its signed contribution as a geometric stack of the same Huxley--Watt/Mertens forms at strictly smaller scales. Under a prior exponent `beta`, the complement costs only the smaller exponent `beta L/(L+1)`.

MC-089 removes the prime-power scale restriction. For a moving prime `p=N^{delta+o(1)}`, the same complement is uniformly `O(N^{2 beta(1-delta)})` on every sufficiently large scale; with suitable `delta<1/2` it is even below the existing `N log N` interior budget. Thus generic support size is not an intrinsic information threshold.

MC-090 closes the naive contraction. The complementary gcd-sieve retention is exactly the unsifted top Huxley--Watt form minus lower-scale sifted corrections. More generally, any gcd mask with `w(1) != 0` retains the unsifted top block. Once the lower-scale correction is subordinate, a sub-old-exponent estimate for the retained statistic is equivalent to the improved Mertens estimate itself. Divisor-sieve recursion can cheapen the complement without cheapening the retained target mode.

## What remains possible

A surviving signed residual must make both sides structurally cheaper than the target in the relevant direction: the discarded component must be controlled by source arithmetic rather than a target-resolution reconstruction, and the retained component must avoid carrying the same top-scale Mertens mode algebraically.

Possible mechanisms remain a joint estimate in which retained and omitted pieces cancel before absolute values, a source-forced recurrence whose top coefficient is genuinely contractive, or a non-gcd coupling that changes the top-scale mode rather than adding independently bounded lower-scale corrections.

## Status / novelty

Möbius inversion, Euler-factor deletion, Huxley--Watt identities, divisor bounds, and Mertens partial summation are classical. The persisted synthesis is the information criterion: **supercritical support can still be recursively cheap, but a useful decomposition must reduce the target-bearing mode itself, not merely its complement**.

## Falsification criterion

Produce a covered gcd-sieve retention with nonzero unsifted coefficient that yields a strictly weaker bound than Mertens after the lower-scale terms are controlled, or construct a source-forced split whose omitted mass is supercritical yet recursively cheap and whose retained top target coefficient is genuinely reduced without assuming the improved Mertens estimate.

## Lean-formalizable core

- Common-prime Euler-factor decomposition into lower scales.
- Arbitrary-scale floor-mismatch error bound in the finite model.
- Gcd-mask divisor-basis decomposition and persistence of the unsifted top coefficient.
