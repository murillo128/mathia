# MI-012 — Hamming endpoint cancellation lives beyond every sub-log-log radial truncation

**Evidence level:** exact source decomposition plus classical approximation/almost-prime input through MC-106

## Core intuition

The Hamming deformation does not hide its Möbius cancellation in a favorable low-bias window or in a finite collection of low radial shells. The known source spike propagates into every moving interval unless the interval is already very narrow, while every fixed Hamming shell above degree one has a positive Landau main term and the same positive cascade persists uniformly through all degrees `o(log log N)`.

The hard endpoint is much smaller than those positive partial sums. Its cancellation must therefore be carried by degrees at least on the first `Theta(log log N)` scale, or by a non-radial relation that bypasses radial truncation altogether.

## Strongest justified principle

MC-104 combines the source spike with the exact degree ceiling and Chebyshev extrapolation. Interval location is irrelevant at this level: a moving window of width `(log N)^(-A+o(1))` must contain amplitude at least `N^(2-2A-o(1))`, so a critical-scale uniform bound requires width at most `(log N)^(-1/2+o(1))`. Broad moving-window search is therefore not an escape from the low-bias obstruction.

MC-105 then identifies the source-specific shell structure. For every fixed `k>=2`, the radial coefficient `C_{k,N}` has a positive asymptotic proportional to `(2 log log N)^(k-2)/(k-2)!`, consecutive shells grow by `2 log log N/(k-1)`, and every fixed signed truncation is dominated by its last shell. Since the actual endpoint is logarithmically smaller, the tail beyond every fixed cutoff must cancel that partial sum.

MC-106 upgrades the statement uniformly to every moving cutoff `K_N=o(log log N)`. Hence **no radial mechanism that sees only sub-log-logarithmic Hamming degree can contain the endpoint cancellation**. The first genuinely unresolved radial regime is `k=Theta(log log N)`, where a uniform Sathe--Selberg-scale analysis of the signed source kernel would be needed.

## What remains possible

The central `Theta(log log N)` shell regime may contain a source-specific signed relation not visible in the fixed/sub-log-log asymptotics. A recurrence whose order grows with `N`, an observable coupling many shells at once, or a non-radial/product-fiber relation can also evade the truncation theorem.

A narrow or pointwise window remains useful only if it comes with such a source-specific signed relation. Width or favorable location alone no longer supplies evidence of endpoint cancellation.

## Status / novelty

Chebyshev/Remez extrapolation, Landau almost-prime asymptotics, and Sathe--Selberg uniformity are classical. The durable line synthesis is the scale localization: **the actual signed endpoint cancellation is forced out of every `o(log log N)` radial truncation and cannot be recovered by broad moving-window amplitude control.**

## Falsification criterion

Invalidate the moving-window Chebyshev transfer, exhibit a nonpositive shell within the claimed uniform `o(log log N)` regime, or produce an exact source-valid radial identity using only `o(log log N)` degrees that already reproduces the hard endpoint without importing an equivalent endpoint estimate. Otherwise the next radial analysis must enter the `Theta(log log N)` scale.
