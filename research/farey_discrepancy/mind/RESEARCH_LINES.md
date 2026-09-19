# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation and recovery geometry

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-034-cheap-kernel-closure-can-still-have-large-resistance`.

FD-187--FD-194 establish the source and observation gates. Prime-extension energy is a genuine Möbius relation currency, while dyadic signed-Fourier observation has a sharp geometric square-root threshold: below the critical band permanent quotient holes remain, while at and above it cumulative source recovery has an explicit uniformly stable inverse. The transition is therefore one of geometry and injectivity, not a conditioning pathology of the raw coordinate map.

FD-195--FD-201 show why stable coordinate recovery does not automatically survive quadratic compression. Classical Franel/Sobolev energies price the same geometric witnesses differently from the raw inverse; on reciprocal-prime shells the RH-facing positive diagonal budget is substantially more coercive than the square-root Mertens target. Fixed-mode cross-horizon differences do contain new Möbius interval increments, but independently squaring the shell rows restores the `H^(3/2+o(1))` random-multiplicative tariff.

FD-202 gives the first exact escape. Taking adjacent-prime differences before a positive quadratic norm collapses overlapping long Mertens intervals to endpoint slabs, and the shell-normalized path energy has squarefree-Rademacher mean `Theta(H)`. FD-203 then separates kernel removal from inverse conditioning: one scalar anchor closes the constant mode at the same critical random cost, yet any anchored path retains endpoint-difference squared dual norm `m-1` and hence `Theta(m)` resistance diameter.

FD-204 shows that this path-resistance obstruction is not universal. Reverse the prime shell and connect each index `j` to `j-2^(nu_2(j))`. The resulting lowbit tree has exact anchored point-evaluation dual norm

`||e_(m-j)||_*^2 = 1+popcount(j)`,

so the worst resistance falls to `Theta(log m)`. Every nonlocal edge is still exactly the difference of two Möbius source slabs, and each adjacent source boundary is reused by at most one edge per dyadic scale. Consequently the same squarefree-random comparator pays only

`E G_(r,H)^lb = O(H log K)=H^(1+o(1))`.

Thus signed nonlocal enrichment can jointly improve conditioning and preserve the critical **power** exponent when its source-side overlap is controlled. The old `H^(3/2)` diagonal tariff and the `Theta(m)` path resistance are no longer structural barriers for this observation family.

The live gap has moved. A physical Möbius bound `G_(r,H)^lb=O(H log^C H)` would give square-root-sized cross-horizon increments uniformly on the shell, but no such analytic bound is proved. Even that would control interval increments `M(floor(rH/p))-M(floor(H/p))`, not absolute Mertens values. The current questions are therefore whether the lowbit energy admits a representation-native Farey/Franel estimate at only polylogarithmic loss, whether an outer cross-scale anchoring/telescoping mechanism recovers absolute `M(n)`, and whether the logarithmic source-reuse/resistance tradeoff can be improved without losing source locality.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. The current sequence separates quotient coverage, raw inverse conditioning, diagonal quadratic coercivity, cross-horizon source information, covariance-preserving signed projection, kernel dimension, graph resistance and now source-overlap cost of nonlocal edges.

Sample count and algebraic injectivity are not enough. A proposed improvement must say which source coordinates are acquired, which cross-coordinate relations the source class forces, what projection occurs before the norm, how often source slabs are reused, what random-multiplicative cost that reuse pays, and what dual/effective-resistance price remains for the intended witness.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root observation threshold still does not prove the RH-critical discrepancy estimate. Conversely, the lowbit tree now gives a finite-dimensional geometry whose conditioning and random benchmark are simultaneously near-critical, but this auxiliary norm is not itself the Franel--Landau destination.

The high-value frontier is therefore no longer another diagonal reweighting, low-rank anchor or path repair. It is a deterministic Möbius/Farey theorem controlling the multiscale source-localized energy and a cross-scale mechanism connecting its interval increments to the absolute Mertens/Farey quantity required downstream. Any further graph optimization should be judged by the joint source-overlap/effective-resistance budget rather than by graph density alone.
