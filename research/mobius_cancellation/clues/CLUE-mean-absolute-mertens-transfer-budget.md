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

## Research question

Can a source-natural signed, bilinear, multiplicative, occupation, correlation, ordered-memory, or multiscale **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some unbounded sequence `X_j -> infinity`, without first proving a pointwise RH-scale bound for `M`, inserting an RH-equivalent coarse statistic into the hypotheses, reconstructing Möbius tautologically from its complete prime law, or reducing the source information to a translation-invariant local histogram that is excursion-blind?

After `MC-122`--`MC-125`, a viable source condition should identify where its information lives beyond fixed potentials, fixed cylinder correlations, and sub-square-root empirical memory. Candidate escapes include quantitatively controlled edge/loop occupation, ordered rather than histogrammed growing memory, prime-label or divisor coupling across distant positions, genuinely multiscale correlations, or another arithmetic law with an explicit polynomial information budget.

## Why it may matter

Mean-absolute control is weaker than pointwise Mertens control but remains RH-complete, and `MC-121` says it may be established on arbitrarily sparse output scales. This allows a source mechanism to focus on the one hard issue that remains: **amplitude recovery**.

The newer obstructions also separate two notions that were easy to conflate. More local memory is not automatically more excursion information: `MC-125` shows that the full local empirical law may still forget the order in which closed local cycles are arranged. A successful route should therefore make explicit which arithmetic relation prevents the bad reorderings rather than assuming that enough local correlations must eventually recover the path.

## Decisive test

Fix one explicit source-natural statistic and prove one of two outcomes:

1. derive a quantitatively polynomial implication from that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on an explicitly controlled unbounded sequence; or
2. construct a source-faithful matched control satisfying the proposed source hypothesis at the claimed strength while its first-absolute partial-sum mean retains exponent `>1/2`.

Kill a candidate if its input already contains an RH-equivalent Mertens/Riesz/coarse mode, if inversion reintroduces the original partial-sum burden, if smoothing or a sub-`L^1` norm discards rare coherent amplitude without a recovery theorem, if deterministic weighting collapses by `MC-122`, if it remains state-local under `MC-123`, if it is only a fixed sign-odd cylinder under `MC-124`, or if its entire source data factor through a sub-square-root local factor histogram without an additional arithmetic constraint that rules out the `MC-125` cycle-reordering controls.

Scale density of the final `D_M` output is not a failure criterion. If actual Möbius satisfies the target estimate on any unbounded sequence, `MC-121` closes RH.

## Evidence boundary

`MC-121` is a target reduction, not a source-natural cancellation mechanism. `MC-117`--`MC-120` are multiplicative matched-control obstructions but do not preserve all quantitative Möbius correlation information. `MC-122`--`MC-124` close broad local feedback classes without controlling the surviving nonlocal information.

`MC-125` is deliberately generic: its binary words do not preserve Möbius multiplicativity, square-free support by integer position, prime values, or divisor relations. It therefore does **not** rule out a theorem combining local statistics with genuine arithmetic structure. Its contribution is to remove “complete local frequency information with growing sub-square-root memory” as a sufficient carrier by itself.

No polynomial source-to-`D_M` transfer is currently established by these findings. The clue remains a research question rather than evidence.

## Research disposition

**Accepted, narrowed through `MC-121`--`MC-125`.** The active residual is now an order-sensitive arithmetic information-recovery problem. A surviving route must preserve enough Möbius-specific nonlocal or multiplicative structure to recover first-absolute excursion amplitude; increasing local memory or enriching a translation-invariant cylinder vocabulary alone is not enough.