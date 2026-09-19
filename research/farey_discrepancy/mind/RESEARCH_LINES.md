# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation and recovery geometry

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-035-lowbit-shell-control-recovers-global-mertens-through-quotient-ladders`.

FD-187--FD-194 establish the source and observation gates. Prime-extension energy is a genuine Möbius relation currency, while dyadic signed-Fourier observation has a sharp geometric square-root threshold: below the critical band permanent quotient holes remain, while at and above it cumulative source recovery has an explicit uniformly stable inverse. The transition is therefore one of geometry and injectivity, not a conditioning pathology of the raw coordinate map.

FD-195--FD-201 show why stable coordinate recovery does not automatically survive quadratic compression. Classical Franel/Sobolev energies price the same geometric witnesses differently from the raw inverse; on reciprocal-prime shells the RH-facing positive diagonal budget is substantially more coercive than the square-root Mertens target. Fixed-mode cross-horizon differences do contain new Möbius interval increments, but independently squaring the shell rows restores the `H^(3/2+o(1))` random-multiplicative tariff.

FD-202 gives the first exact escape. Taking adjacent-prime differences before a positive quadratic norm collapses overlapping long Mertens intervals to endpoint slabs, and the shell-normalized path energy has squarefree-Rademacher mean `Theta(H)`. FD-203 then separates kernel removal from inverse conditioning: one scalar anchor closes the constant mode at the same critical random cost, yet any anchored path retains endpoint-difference squared dual norm `m-1` and hence `Theta(m)` resistance diameter.

FD-204 shows that this path-resistance obstruction is not universal. Reverse the prime shell and connect each index `j` to `j-2^(nu_2(j))`. The resulting lowbit tree has exact anchored point-evaluation dual norm `1+popcount(j)`, so the worst resistance falls to `Theta(log m)`. Every nonlocal edge is still exactly the difference of two Möbius source slabs, and each adjacent source boundary is reused by at most one edge per dyadic scale. Consequently the same squarefree-random comparator pays only `H^(1+o(1))`.

FD-205 closes the remaining cross-scale recovery gap for this geometry. For each target index `n`, choose a prime `p_n` with `n/2<p_n<=n` and two nearby horizons whose quotient coordinates satisfy `floor(H/p_n)=n` and `floor(2H/p_n)=2n+b`. The corresponding lowbit shell sensor is exactly a dyadic Mertens increment `M(2n+b)-M(n)`. Iterating these quotient ladders recovers arbitrary `M(N)` by binary telescoping. Hence a deterministic bound `G_(2,H)^lb=O_epsilon(H^(1+epsilon))` for all large `H` implies the square-root Mertens bound and therefore RH; a polylogarithmic loss gives the corresponding explicit logarithmic loss for `M(N)`.

The physical mode and horizon may vary from scale to scale. The coherent coordinate is the **internal quotient index**, not a fixed Fourier mode or fixed physical shell. This matters because the lowbit energy is now both near-critical under the random comparator and strong enough, if bounded deterministically at that scale, to recover the global Mertens quantity required downstream.

The live gap has therefore collapsed to one analytic interface: prove the critical-power lowbit-energy estimate from Farey/Möbius arithmetic. Further graph optimization or outer anchoring is secondary unless it reduces that analytic burden without increasing source reuse. The cross-scale recovery mechanism itself is no longer missing.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. The current sequence separates quotient coverage, raw inverse conditioning, diagonal quadratic coercivity, cross-horizon source information, covariance-preserving signed projection, kernel dimension, graph resistance, source-overlap cost and now quotient-coordinate recovery across changing physical scales.

Sample count and algebraic injectivity are not enough. A proposed improvement must say which source coordinates are acquired, which cross-coordinate relations the source class forces, what projection occurs before the norm, how often source slabs are reused, what random-multiplicative cost that reuse pays, what dual/effective-resistance price remains for the intended witness, and which internal coordinate stays coherent when the physical sensor changes with scale.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root observation threshold still does not prove the RH-critical discrepancy estimate. Conversely, the lowbit tree now gives a finite-dimensional geometry whose conditioning and random benchmark are simultaneously near-critical, and FD-205 proves that critical control of that auxiliary energy would already recover the global Mertens/RH destination through exact quotient ladders.

The high-value frontier is therefore sharply analytic: establish the deterministic critical-power lowbit-energy bound, or identify an exact obstruction showing why Farey arithmetic cannot satisfy it. Any further representation change should be judged by whether it changes that theorem surface rather than by graph density, fixed-mode coherence or local conditioning alone.