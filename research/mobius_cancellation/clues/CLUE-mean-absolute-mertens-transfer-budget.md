---
id: CLUE-mobius-cancellation-mean-absolute-mertens-transfer-budget
type: research-clue
status: accepted
origin: master-researcher
target_line: mobius_cancellation
based_on:
  - research/mobius_cancellation/findings/MC-001-local-to-global-exceptional-mass-barrier.md
  - research/mobius_cancellation/findings/MC-006-averaged-chowla-vdc-logarithmic-ceiling.md
  - research/mobius_cancellation/findings/MC-115-mean-absolute-mertens-mellin-zero-free.md
  - research/mobius_cancellation/findings/MC-117-fractional-mertens-moment-transfer-ceiling.md
  - research/mobius_cancellation/findings/MC-118-balanced-prime-block-multiplicative-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-119-uniform-polynomial-window-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-120-fixed-function-lacunary-fractional-moment-barrier.md
  - research/mobius_cancellation/findings/MC-121-arbitrary-checkpoint-mean-absolute-rh-criterion.md
  - research/mobius_cancellation/findings/MC-122-weighted-amplitude-feedback-quadratic-energy-collapse.md
  - research/mobius_cancellation/findings/MC-123-state-local-feedback-tree-decomposition.md
  - research/mobius_cancellation/findings/MC-124-fixed-memory-sign-odd-logarithmic-invisibility.md
  - research/mobius_cancellation/findings/MC-125-local-factor-histogram-square-root-memory-barrier.md
  - research/mobius_cancellation/findings/MC-126-finite-additive-state-feedback-endpoint-collapse.md
  - research/mobius_cancellation/findings/MC-127-growing-modular-transition-type-excursion-blindness.md
  - research/mobius_cancellation/findings/MC-128-sub-square-root-state-time-binning-excursion-blindness.md
  - research/mobius_cancellation/findings/MC-129-joint-local-binned-modular-excursion-blindness.md
---

# Can a source-natural statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The useful endpoint is

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` shows that RH-scale control of this first absolute mean is RH-complete, while `MC-121` removes the final scale-density burden: such a bound for the **actual Möbius function** along any rigorously produced unbounded checkpoint sequence already excludes every off-critical zero. The unresolved problem is therefore source-side amplitude recovery, not endpoint interpolation.

The current obstruction surface rules out several increasingly rich but still order-forgetting summaries. `MC-117`--`MC-120` show that sub-`L^1` information can miss rare coherent excursions even with multiplicative controls. `MC-122`--`MC-124` close deterministic amplitude feedback, scalar state-local feedback, and fixed-memory sign-odd cylinder information. `MC-125`--`MC-128` then show that growing local histograms, additive modular state, complete modular transition types, and coarse time localization can all forget macroscopic lift order.

`MC-129` closes the simplest attempt to repair those failures by stacking the summaries. It gives exact bounded-increment controls that, **inside every coarse time bin**, have the same complete factor histogram through memory `k` and the same complete directed transition histogram modulo `q`, yet have first-absolute excursion means on opposite sides of square-root scale throughout an explicit joint sub-square-root regime. The remaining opportunity is therefore not “more coordinates of the same two quotients”; it must use information that couples or escapes them.

## Research question

Can a source-natural **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some controlled unbounded sequence `X_j -> infinity` without first proving an RH-equivalent Mertens bound, reconstructing Möbius tautologically from its complete prime law, or factoring through the excursion-blind local/state summaries already ruled out?

After `MC-129`, especially interesting escapes are a genuine cross-coupling between local arithmetic pattern and persistent state, ordered or noncommutative cross-scale information, non-additive state, prime/divisor-labelled long-range relations, or another arithmetic law whose information budget can be bounded explicitly.

## Why it may matter

The endpoint side is now unusually cheap: `MC-121` says the desired first-absolute bound need only be produced on an unbounded checkpoint sequence. That concentrates the research burden on one concrete question: **what source information retains macroscopic excursion amplitude?**

The negative findings also make the next test sharper. A candidate cannot justify itself merely by combining local memory, modular occupation, and coarse time labels; `MC-129` matches all of those simultaneously. Any positive mechanism should identify the exact extra relation that forbids the common-cycle reorderings used by the matched controls, preferably through arithmetic structure that the controls deliberately lack.

## Decisive test

Fix one explicit source-natural statistic and prove one of two outcomes:

1. derive a quantitative implication from that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on an explicitly controlled unbounded sequence for the actual Möbius function; or
2. construct a source-faithful matched control satisfying the proposed source hypothesis at the claimed strength while its first-absolute partial-sum mean retains exponent `>1/2`.

Kill a candidate if its input already contains an RH-equivalent Mertens/Riesz/coarse mode, if inversion reintroduces the original partial-sum burden, if its information factors through the local-histogram, additive-state, modular-transition, time-binned, or **separately stacked local-plus-modular** summaries covered by `MC-122`--`MC-129`, or if its apparent gain disappears after the exceptional-set, smoothing, weighting, and scale losses are restored.

A candidate survives this particular obstruction only if it uses additional information that `MC-129` does not match, such as the joint cross-tabulation of local pattern with contemporaneous modular/arithmetic state, finer transition order, non-additive memory, or an exact Möbius-specific constraint excluding the matched cycle reorderings.

## Evidence boundary

`MC-121` is only an endpoint reduction; it supplies no source-natural upper bound. `MC-117`--`MC-129` are obstruction results, and several of their matched controls are generic bounded-increment words rather than multiplicative functions. They therefore do **not** prove that Möbius arithmetic cannot supply the missing relation.

In particular, `MC-129` matches complete local factor counts and complete modular transition counts **as two separate bin-local summaries**. It does not match the finer cross-coupled tensor recording which local pattern occurs at which modular/arithmetic state, nor does it preserve Möbius multiplicativity, square-free placement, prime values, or divisor relations. Those are genuine remaining escape surfaces, not evidence that any one of them works.

## Research disposition

**Accepted, narrowed through `MC-129`.** The live residual is a source-to-amplitude theorem using genuinely cross-coupled, ordered, non-additive, or arithmetic information that does not factor through the common cycle-order kernel exposed by the current matched controls.