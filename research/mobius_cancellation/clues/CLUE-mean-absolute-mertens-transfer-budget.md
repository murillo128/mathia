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
  - research/mobius_cancellation/findings/MC-130-finite-horizon-product-state-type-folding.md
  - research/mobius_cancellation/findings/MC-131-periodic-clock-product-state-excursion-blindness.md
  - research/mobius_cancellation/findings/MC-132-polynomial-clock-moment-excursion-blindness.md
---

# Can a source-natural statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The useful endpoint is

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` shows that RH-scale control of this first absolute mean is RH-complete, while `MC-121` removes the final scale-density burden: such a bound for the **actual Möbius function** along any rigorously produced unbounded checkpoint sequence already excludes every off-critical zero. The unresolved problem is therefore source-side amplitude recovery, not endpoint interpolation.

The current obstruction surface rules out several increasingly rich but still order-forgetting summaries. `MC-117`--`MC-120` show that sub-`L^1` information can miss rare coherent excursions even with multiplicative controls. `MC-122`--`MC-124` close deterministic amplitude feedback, scalar state-local feedback, and fixed-memory sign-odd cylinder information. `MC-125`--`MC-128` then show that growing local histograms, additive modular state, complete modular transition types, and coarse time localization can all forget macroscopic lift order.

`MC-129` closes the simplest contemporaneous cross-coupling repair by matching, inside every coarse bin, the complete empirical transition type of `(last k-1 increments, partial sum mod q, current increment)` while placing the matched words on opposite sides of square-root excursion scale. `MC-130` strengthens the information boundary again: an empirical `h`-step path type with starting memory `k_0-1` is exactly a one-step type after enlarging the context to `K-1`, where `K=k_0+h-1`. Thus finite or growing finite-horizon product-state path histograms remain excursion-blind throughout the corresponding sub-square-root effective-context regime.

`MC-131` then shows that adding a periodic time coordinate does not recover the missing order: the full local/modular/periodic transition tensor remains matchable whenever the joint clock/modular resolution stays below its explicit threshold. `MC-132` closes the next natural timing repair. Using a Prouhet--Thue--Morse macro-order construction, two paths can have identical polynomial timestamp moments of **every** clocked product-state transition through any fixed degree, and even through a controlled logarithmically growing degree family, while their mean-absolute excursions still lie on opposite sides of square-root scale. Moment information about occurrence times is therefore still not occurrence order.

## Research question

Can a source-natural **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some controlled unbounded sequence `X_j -> infinity` without first proving an RH-equivalent Mertens bound, reconstructing Möbius tautologically from its complete prime law, or factoring through the excursion-blind local/state/path/time summaries already ruled out?

After `MC-132`, the timing escape is narrower than merely retaining timestamps in compressed form. Especially interesting residuals are the raw order of state/path occurrences, an essentially full-resolution or genuinely non-polynomial/adaptive temporal measure, nested or noncommutative multiscale relations that cannot be flattened into a longer finite context or a bounded moment family at the same information budget, critical-or-larger effective memory, genuinely non-additive state, prime/divisor-labelled long-range relations, exact multiplicative constraints, or another arithmetic law whose information budget can be bounded explicitly.

## Why it may matter

The endpoint side is unusually cheap: `MC-121` says the desired first-absolute bound need only be produced on an unbounded checkpoint sequence. That concentrates the research burden on one concrete question: **what source information retains macroscopic excursion amplitude?**

The negative findings make the next test sharper. A candidate cannot justify itself merely by combining local memory, modular occupation, coarse time labels, their contemporaneous cross-tabulation, finitely many consecutive product-state transitions summarized as empirical path types, periodic clocks, or finitely/moderately many polynomial moments of their occurrence times. `MC-129`--`MC-132` match all of those in explicit subcritical regimes. Any positive mechanism should identify the exact extra relation that forbids the common-cycle/Prouhet reorderings used by the matched controls, preferably through arithmetic structure that the controls deliberately lack.

## Decisive test

Fix one explicit source-natural statistic and prove one of two outcomes:

1. derive a quantitative implication from that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on an explicitly controlled unbounded sequence for the actual Möbius function; or
2. construct a source-faithful matched control satisfying the proposed source hypothesis at the claimed strength while its first-absolute partial-sum mean retains exponent `>1/2`.

Kill a candidate if its input already contains an RH-equivalent Mertens/Riesz/coarse mode, if inversion reintroduces the original partial-sum burden, if its information factors through the local-histogram, additive-state, modular-transition, time-binned, cross-coupled one-step, finite-horizon empirical path, periodic-clock, or polynomial/quasi-polynomial timestamp-moment summaries covered by `MC-122`--`MC-132`, or if its apparent gain disappears after exceptional-set, smoothing, weighting, and scale losses are restored.

A candidate survives this obstruction surface only if it uses information the current controls do not match: genuine occurrence order or near-full timing resolution rather than a low-moment compression, a multiscale relation not reducible to one longer empirical context or bounded polynomial-moment family, effective memory at or above the unresolved critical scale, non-additive arithmetic state, prime/divisor-labelled structure, exact multiplicative constraints, or another proved Möbius-specific relation excluding the matched reorderings.

## Evidence boundary

`MC-121` is only an endpoint reduction; it supplies no source-natural upper bound. `MC-117`--`MC-132` are obstruction results, and several of their matched controls are generic bounded-increment words rather than multiplicative functions. They therefore do **not** prove that Möbius arithmetic cannot supply the missing relation.

`MC-130` matches empirical finite-horizon product-state path types, `MC-131` adds periodic timing, and `MC-132` matches polynomial timestamp moments of each clocked transition state through the declared degree. None of them matches the full ordered trajectory, the raw empirical measure on absolute occurrence times, arbitrary non-polynomial/adaptive temporal weights, genuinely non-flattenable nested multiscale data, non-additive state, Möbius multiplicativity, square-free placement, prime values, or divisor relations. Those remain genuine escape surfaces, not evidence that any one of them works.

## Research disposition

**Accepted, further narrowed by `MC-132`.** The live residual is a source-to-amplitude theorem using genuinely occurrence-ordered or essentially full-resolution timing information, non-flattenable multiscale structure, non-additive or critical-memory state, or Möbius-specific arithmetic constraints outside the empirical finite-horizon/periodic/polynomial-moment quotient.