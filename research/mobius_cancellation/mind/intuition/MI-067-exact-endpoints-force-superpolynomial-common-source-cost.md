# MI-067 — Exact endpoints force a common source cost linear in rank until the analytic ceiling

**Evidence level:** exact synthesis from [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md), [MC-378](../../findings/MC-378-moving-smooth-frame-forces-iterated-log-source-cost-rate.md), [MC-379](../../findings/MC-379-rough-squarefree-terminal-block-lifts-moving-source-cost-ceiling.md), [MC-380](../../findings/MC-380-tiny-source-primes-can-be-packed-before-terminal-differencing.md), and [MC-381](../../findings/MC-381-fixed-power-smoothness-makes-source-cost-linear-in-rank.md).

Let `P` be the common lower-prime source radical of an exact endpoint package at shell scale `y`, with source rank `R`. MC-377 first proves qualitative escape from every fixed-power regime: `log P/log y -> infinity`.

MC-378 makes this moving but pays an `A^2` source-coordinate cost under a trial `P<=y^A`. MC-379 raises the analytic ceiling by exploiting primitive rough-squarefree terminal conductors, while MC-380 shows that tiny source primes can be packed into a preliminary exact factor rather than deleted.

MC-381 removes the remaining rank artifact. Instead of forcing every surviving source prime below a moving threshold, cut only at one fixed shell power `y^beta`. Under `P<=y^A`, at most `O(A)` source primes lie above that cutoff, so the smooth character subspace loses only `O(A)` dimensions. More importantly, the prime-frame contradiction needs exponentially many surviving rows, not `2^(R-o(R))` rows. A fixed positive fraction of the `R` endpoint dimensions is enough.

The contradiction therefore applies whenever

`A<=c_0 R` and `2^(C A) log log y=o(log y)`,

and yields the current bound

`log P/log y >= c min{R, log log y}`.

The reusable lesson has two parts. First, a nuisance coordinate should not be charged as codimension when an earlier exact factor can carry it until the terminal argument. Second, **the right rank budget is determined by how much combinatorial mass the contradiction actually needs**. Requiring near-full dimension can create a fictitious square-root barrier when a positive-density subspace already leaves exponentially many witnesses.

This is a general proof-design warning rather than a universal rank theorem. The improvement works because the terminal character-sum estimate tolerates a fixed-power smoothness cutoff, the tiny-prime product is packable, and the frame argument is exponentially redundant. Another architecture may genuinely need almost all source directions.

**Boundary.** These are source-realization obstructions, not bounds for `M(x)` and not RH implications. The linear-in-`R` rate is not claimed optimal, and the `log log y` analytic ceiling remains. The result applies to this exact endpoint architecture and its common-radical resource, not to arbitrary representations of Möbius cancellation.