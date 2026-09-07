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
---

# Can a source-natural statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The useful endpoint is

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` shows that RH-scale control of this first absolute mean is already RH-complete. `MC-121` then removes the final scale-density burden: Pintz's 1987 lower bound implies that

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

for every `epsilon>0` along **any rigorously produced unbounded checkpoint sequence** already excludes every off-critical zero. The unresolved problem is therefore purely source-side: recover the first absolute excursion exponent from information genuinely weaker than an RH-equivalent Mertens observable.

The obstruction surface has become much sharper. `MC-117`--`MC-120` show that sub-`L^1` information can miss rare coherent excursions even after exact square-free support, multiplicativity, polynomial scale windows, and one fixed multiplicative comparator are imposed. `MC-122` shows that deterministic amplitude weighting is exactly quadratic path energy after the square-free correction. `MC-123` classifies every scalar state-local one-step feedback as a potential plus unoriented occupation. `MC-124` then shows that every fixed-memory globally sign-odd Möbius cylinder observable lies inside the qualitative logarithmic fixed-correlation class.

`MC-125` closes the simplest growing-memory repair at the representation level. It constructs, for every memory exponent `alpha<1/2`, pairs of bounded-increment words with **identical complete factor histograms through length `N^(alpha+o(1))`** but mean-absolute excursion scales `N^(alpha+o(1))` and `N^(1-alpha+o(1))`. Thus merely collecting all local frequencies, even with growing sub-square-root memory, does not retain global excursion ordering. The controls are not multiplicative, so the surviving opportunity is precisely to exploit arithmetic/nonlocal structure that excludes this local-cycle-reordering ambiguity.

`MC-126` closes another superficially nonlocal repair: a fixed finite persistent state driven only by cumulative Möbius increments is a finite additive cycle. Every one-step observable on that state splits into a bounded periodic potential, one harmonic circulation proportional to `mu(n)`, and reversal-even transition/loop occupation. The unweighted harmonic contribution is therefore just a constant multiple of `M(N)`; deterministic weighting exposes an explicit weighted functional of the original Mertens path. Fixed modular memory such as `M mod q` can retain occupation information, but it does not create a new oriented excursion carrier.

`MC-127` now shows that simply letting the modular accumulator grow does not repair the occupation escape either. For every `q,m`, two zero-endpoint `+/-1` paths can have **identical counts of every directed transition `(S_{n-1} mod q, increment_n)`** while their first-absolute means are exactly `N/4` and `q/2`, with ratio `N/(2q)`. Thus even a polynomially growing state together with its complete aggregate first-order transition occupation can forget macroscopic excursion order. A surviving modular-state proposal must retain temporal ordering or prove a genuinely Möbius-specific constraint that excludes these matched cycle reorderings.

## Research question

Can a source-natural signed, bilinear, multiplicative, occupation, correlation, ordered-memory, or multiscale **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some unbounded sequence `X_j -> infinity`, without first proving a pointwise RH-scale bound for `M`, inserting an RH-equivalent coarse statistic into the hypotheses, reconstructing Möbius tautologically from its complete prime law, or reducing the source information to a translation-invariant local histogram or additive modular transition type that is excursion-blind?

After `MC-122`--`MC-127`, a viable source condition should identify where its information lives beyond fixed potentials, fixed cylinder correlations, sub-square-root empirical memory, and aggregate additive-state transition occupations even when the modular state grows. Candidate escapes include quantitatively controlled **ordered** occupation, prime-label or divisor coupling across distant positions, genuinely multiscale correlations, non-additive persistent state, or another arithmetic law with an explicit polynomial information budget.

## Why it may matter

Mean-absolute control is weaker than pointwise Mertens control but remains RH-complete, and `MC-121` says it may be established on arbitrarily sparse output scales. This allows a source mechanism to focus on the one hard issue that remains: **amplitude recovery**.

The newer obstructions separate several notions that were easy to conflate. More local memory is not automatically more excursion information: `MC-125` shows that the full local empirical law may still forget the order in which closed local cycles are arranged. Persistent state is not automatically better: `MC-126` shows that fixed additive state remembers only a periodic position whose unique oriented circulation lifts to the ordinary endpoint, while `MC-127` shows that increasing the number of modular states and retaining their full directed occupation histogram still does not recover the ordering of integer windings. A successful route should therefore make explicit which arithmetic relation retains macroscopic excursion amplitude rather than assuming that richer state bookkeeping must eventually recover the path.

## Decisive test

Fix one explicit source-natural statistic and prove one of two outcomes:

1. derive a quantitatively polynomial implication from that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on an explicitly controlled unbounded sequence; or
2. construct a source-faithful matched control satisfying the proposed source hypothesis at the claimed strength while its first-absolute partial-sum mean retains exponent `>1/2`.

Kill a candidate if its input already contains an RH-equivalent Mertens/Riesz/coarse mode, if inversion reintroduces the original partial-sum burden, if smoothing or a sub-`L^1` norm discards rare coherent amplitude without a recovery theorem, if deterministic weighting collapses by `MC-122`, if it remains scalar state-local under `MC-123`, if it is only a fixed sign-odd cylinder under `MC-124`, if its entire source data factor through a sub-square-root local factor histogram without an additional arithmetic constraint that rules out the `MC-125` cycle-reordering controls, if its persistent oriented state is only a fixed additive finite accumulator covered by `MC-126`, or if its growing additive-state information factors only through the aggregate directed transition type covered by `MC-127`.

Scale density of the final `D_M` output is not a failure criterion. If actual Möbius satisfies the target estimate on any unbounded sequence, `MC-121` closes RH.

## Evidence boundary

`MC-121` is a target reduction, not a source-natural cancellation mechanism. `MC-117`--`MC-120` are multiplicative matched-control obstructions but do not preserve all quantitative Möbius correlation information. `MC-122`--`MC-124` close broad local feedback classes without controlling the surviving nonlocal information.

`MC-125` is deliberately generic: its binary words do not preserve Möbius multiplicativity, square-free support by integer position, prime values, or divisor relations. It therefore does **not** rule out a theorem combining local statistics with genuine arithmetic structure. Its contribution is to remove “complete local frequency information with growing sub-square-root memory” as a sufficient carrier by itself.

`MC-126` is also a representation-level obstruction. It does not rule out growing state, non-additive automata, arithmetic-labelled transitions, multiscale state, or reversal-even occupation estimates. It says only that fixed finite state generated additively from the cumulative Möbius increments has no independent oriented circulation beyond the Mertens endpoint.

`MC-127` remains representation-level as well. Its matched paths preserve the complete aggregate directed modular transition histogram but not Möbius multiplicativity, square-free placement, divisor relations, temporal transition order, or cross-modulus coupling. It therefore does not rule out arithmetic occupation theorems; it rules out treating a growing modular transition histogram **by itself** as an excursion-complete carrier.

No polynomial source-to-`D_M` transfer is currently established by these findings. The clue remains a research question rather than evidence.

## Research disposition

**Accepted, narrowed through `MC-121`--`MC-127`.** The active residual is now an order-sensitive arithmetic information-recovery problem. A surviving route must preserve enough Möbius-specific nonlocal, ordered-occupation, multiplicative, multiscale, non-additive, or otherwise arithmetic structure to recover first-absolute excursion amplitude; increasing local memory, enriching a translation-invariant cylinder vocabulary, or adding/growing an additive modular accumulator together with only its aggregate transition counts is not enough.