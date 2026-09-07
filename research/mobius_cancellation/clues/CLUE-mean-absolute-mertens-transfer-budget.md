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
  - research/mobius_cancellation/findings/MC-133-divisibility-complex-betti-parity-mertens-annulus.md
  - research/mobius_cancellation/findings/MC-134-divisor-filtration-persistence-dyadic-barcode.md
---

# Can a source-natural statistic transfer polynomially to mean-absolute Mertens scale?

## Observation

The useful endpoint is

`D_M(X)=X^(-1) integral_1^X |M(x)| dx`.

`MC-115` shows that RH-scale control of this first absolute mean is RH-complete, while `MC-121` removes the final scale-density burden: such a bound for the **actual Möbius function** along any rigorously produced unbounded checkpoint sequence already excludes every off-critical zero. The unresolved problem is therefore source-side amplitude recovery, not endpoint interpolation.

The current obstruction surface rules out several increasingly rich but still order-forgetting summaries. `MC-117`--`MC-120` show that sub-`L^1` information can miss rare coherent excursions even with multiplicative controls. `MC-122`--`MC-124` close deterministic amplitude feedback, scalar state-local feedback, and fixed-memory sign-odd cylinder information. `MC-125`--`MC-128` then show that growing local histograms, additive modular state, complete modular transition types, and coarse time localization can all forget macroscopic lift order.

`MC-129` closes the simplest contemporaneous cross-coupling repair by matching, inside every coarse bin, the complete empirical transition type of `(last k-1 increments, partial sum mod q, current increment)` while placing the matched words on opposite sides of square-root excursion scale. `MC-130` strengthens the information boundary again: an empirical `h`-step path type with starting memory `k_0-1` is exactly a one-step type after enlarging the context to `K-1`, where `K=k_0+h-1`. Thus finite or growing finite-horizon product-state path histograms remain excursion-blind throughout the corresponding sub-square-root effective-context regime.

`MC-131` shows that adding a periodic time coordinate does not recover the missing order. `MC-132` closes the next natural timing repair: a Prouhet--Thue--Morse macro-order construction matches polynomial timestamp moments of **every** clocked product-state transition through any fixed degree, and even through a controlled logarithmically growing degree family, while mean-absolute excursions remain on opposite sides of square-root scale. Moment information about occurrence times is therefore still not occurrence order.

`MC-133` tests a qualitatively different survivor: exact rational-prime/divisor structure rather than another generic path summary. Björner's classical simplicial complex of squarefree prime-factor sets has Betti numbers equal to counts of odd squarefree integers in the terminal dyadic annulus `(n/2,n]`, split by number of prime factors. Its alternating Betti sum is exactly

`M(n)=sum_{n/2<m<=n, 2 does not divide m} mu(m)`,

while the **unsigned** total Betti mass is `2n/pi^2+o(n)`. Thus basic static divisor topology does not supply a cheaper source statistic: forgetting parity leaves linear mass, while retaining parity reconstructs the Mertens target exactly.

`MC-134` now audits the inter-scale escape left open there. Over every field, the reduced persistent barcode of the actual filtration `Delta_1 subset Delta_2 subset ...` consists exactly of bars `[m,2m)` in degree `Omega(m)-1`, one for each odd squarefree `m>1`. Hence every reduced homology map across a factor-two scale gap is zero and every logarithmic lifetime is exactly `log 2`. Ordinary one-parameter persistence therefore adds no hidden long-range topological carrier: its transport structure is rigid, while its birth data still encode the same squarefree/parity information whose signed live-bar count equals `M(n)`.

## Research question

Can a source-natural **Möbius-specific** statistic force

`D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))`

on some controlled unbounded sequence `X_j -> infinity` without first proving an RH-equivalent Mertens bound, reconstructing Möbius tautologically from its complete prime law, or factoring through the excursion-blind or representation-complete summaries already ruled out?

After `MC-134`, the divisor-topology residual can no longer be ordinary single-parameter persistent homology of Björner's filtration. Especially interesting possibilities are raw occurrence order; essentially full-resolution or genuinely non-polynomial/adaptive temporal information; nested or noncommutative multiscale relations that cannot be flattened into a longer finite context or bounded moment family; critical-or-larger effective memory; genuinely non-additive state; chain-level or additionally labelled divisor relations not determined by the dyadic barcode; a genuinely different/multiparameter arithmetic filtration; exact multiplicative constraints; or another arithmetic law whose information budget can be bounded explicitly.

## Why it may matter

The endpoint side is unusually cheap: `MC-121` says the desired first-absolute bound need only be produced on an unbounded checkpoint sequence. That concentrates the research burden on one concrete question: **what source information retains macroscopic excursion amplitude?**

The negative findings now calibrate both generic and exact arithmetic representations. A candidate cannot justify itself merely by combining local memory, modular occupation, coarse time labels, finite-horizon empirical paths, periodic clocks, polynomial timestamp moments, static divisor homology, or the ordinary persistent homology of that divisor filtration. `MC-129`--`MC-132` match the generic summaries in explicit subcritical regimes; `MC-133` shows static homology has linear unsigned mass and an alternating projection equal to `M`; `MC-134` shows the complete one-parameter persistence module is only the explicit dyadic barcode. Any positive mechanism must identify extra structure not already exhausted by these collapses without merely storing the endpoint.

## Decisive test

Fix one explicit source-natural statistic and prove one of two outcomes:

1. derive a quantitative implication from that statistic to `D_M(X_j)=O_epsilon(X_j^(1/2+epsilon))` on an explicitly controlled unbounded sequence for the actual Möbius function; or
2. construct a source-faithful matched control satisfying the proposed source hypothesis at the claimed strength while its first-absolute partial-sum mean retains exponent `>1/2`.

Kill a candidate if its input already contains an RH-equivalent Mertens/Riesz/coarse mode; if inversion reintroduces the original partial-sum burden; if its information factors through the local-histogram, additive-state, modular-transition, time-binned, cross-coupled one-step, finite-horizon empirical path, periodic-clock, or polynomial/quasi-polynomial timestamp-moment summaries covered by `MC-122`--`MC-132`; if a static divisor-topology invariant reduces to the Betti/Euler package in `MC-133`; **or if an inter-scale topological proposal factors through the ordinary one-parameter persistence module explicitly classified in `MC-134`**. Also kill it if the apparent gain disappears after exceptional-set, smoothing, weighting, and scale losses are restored.

A candidate survives this obstruction surface only if it uses information the current controls do not match: genuine occurrence order or near-full timing resolution; a multiscale relation not reducible to one longer empirical context or bounded polynomial-moment family; effective memory at or above the unresolved critical scale; non-additive arithmetic state; divisor/prime structure beyond the static Betti vector and dyadic persistence barcode; exact multiplicative constraints; or another proved Möbius-specific relation excluding both the matched reorderings and exact reconstruction collapses.

## Evidence boundary

`MC-121` is only an endpoint reduction; it supplies no source-natural upper bound. `MC-117`--`MC-132` are obstruction results, and several of their matched controls are generic bounded-increment words rather than multiplicative functions. They therefore do **not** prove that Möbius arithmetic cannot supply the missing relation.

`MC-133` and `MC-134` are exact arithmetic/topological audits with deliberately limited scope. `MC-133` closes single-scale ordinary homology/homotopy. `MC-134` closes **ordinary one-parameter persistent homology over a field** by determining its full barcode and all factor-two transport maps. Neither finding analyzes chain-level arithmetic labels, additional algebraic operations, genuinely different or multiparameter filtrations, or another Möbius-specific inter-scale invariant not determined by that barcode. Those remain possible escape surfaces, not evidence that any one of them works.

Likewise, `MC-130` matches empirical finite-horizon product-state path types, `MC-131` adds periodic timing, and `MC-132` matches polynomial timestamp moments of each clocked transition state through the declared degree. None matches the complete ordered trajectory or arbitrary adaptive temporal information.

## Research disposition

**Accepted, further narrowed by `MC-134`.** The live residual is a source-to-amplitude theorem using genuinely occurrence-ordered or essentially full-resolution timing information, non-flattenable multiscale structure, non-additive or critical-memory state, or Möbius-specific arithmetic structure that survives the generic order-forgetting controls and is not exhausted by the static or one-parameter-persistent topology of the exact divisor filtration.