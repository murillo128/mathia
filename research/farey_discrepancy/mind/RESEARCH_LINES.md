# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Separate source-side rigidity from the exact observation and recovery geometry

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-035-lowbit-shell-control-recovers-global-mertens-through-quotient-ladders`.

FD-187--FD-194 establish the source and observation gates. Prime-extension energy is a genuine Möbius relation currency, while dyadic signed-Fourier observation has a sharp geometric square-root threshold: below the critical band permanent quotient holes remain, while at and above it cumulative source recovery has an explicit uniformly stable inverse. The transition is therefore one of geometry and injectivity, not a conditioning pathology of the raw coordinate map.

FD-195--FD-201 show why stable coordinate recovery does not automatically survive quadratic compression. Classical Franel/Sobolev energies price the same geometric witnesses differently from the raw inverse; on reciprocal-prime shells the RH-facing positive diagonal budget is substantially more coercive than the square-root Mertens target. Fixed-mode cross-horizon differences do contain new Möbius interval increments, but independently squaring the shell rows restores the `H^(3/2+o(1))` random-multiplicative tariff.

FD-202 gives the first exact escape. Taking adjacent-prime differences before a positive quadratic norm collapses overlapping long Mertens intervals to endpoint slabs, and the shell-normalized path energy has squarefree-Rademacher mean `Theta(H)`. FD-203 then separates kernel removal from inverse conditioning: one scalar anchor closes the constant mode at the same critical random cost, yet any anchored path retains endpoint-difference squared dual norm `m-1` and hence `Theta(m)` resistance diameter.

FD-204 shows that this path-resistance obstruction is not universal. Reverse the prime shell and connect each index `j` to `j-2^(nu_2(j))`. The resulting lowbit tree has exact anchored point-evaluation dual norm `1+popcount(j)`, so the worst resistance falls to `Theta(log m)`. Every nonlocal edge is still exactly the difference of two Möbius source slabs, and each adjacent source boundary is reused by at most one edge per dyadic scale. Consequently the same squarefree-random comparator pays only `H^(1+o(1))`.

FD-205 showed that lowbit shell sensors can recover global Mertens values through quotient-coordinate telescoping. FD-206 sharpens and partly corrects that interpretation. At the source-independent horizons `H_n=n p_n`, where `p_n` is the largest prime at most `n`, the terminal shell prime is exactly `p_n` and the positive root anchor is exactly

`S_(2,H_n)(p_n)=M(2n)-M(n)`.

Since the anchored lowbit energy contains `K_n |M(2n)-M(n)|^2` as a nonnegative summand, a critical bound on this single horizon family already gives the square-root dyadic Mertens increment. Moreover the doubling increments alone recover arbitrary `M(N)`: an odd binary step differs from the corresponding doubling step only by the bounded coefficient `mu(2n+1)`. Thus `M(2n)-M(n)=O_epsilon(n^(1/2+epsilon))` is itself RH-equivalent.

This changes the theorem surface. The lowbit geometry still solves a genuine finite-dimensional conditioning/source-reuse problem, but the proposed positive energy target is not demonstrably easier than RH: on root-aligned horizons it already contains an RH-equivalent scalar coordinate before tree resistance is used. The live question is therefore whether Farey arithmetic supplies **additional signed or cross-scale structure that derives the root increment rather than assuming it as a positive standalone cost**, or whether the scalar anchor should be replaced by an observable in which the difficult coordinate can cancel before squaring.

## Apply information budgets only after fixing source class, observation family and destination norm

The same Farey representation can be complete, target-rigid or permanently noninjective depending on the source class, observation family and destination norm. The current sequence separates quotient coverage, raw inverse conditioning, diagonal quadratic coercivity, cross-horizon source information, covariance-preserving signed projection, kernel dimension, graph resistance, source-overlap cost and quotient-coordinate recovery across changing physical scales.

FD-206 adds another required audit: a near-critical random benchmark and favorable inverse geometry do not imply that the deterministic theorem is easier than the destination if a positive coordinate of the norm is already destination-complete. Before crediting an auxiliary energy, isolate its individual nonnegative anchors and ask whether any one of them already encodes an RH-equivalent estimate on a cofinal source family.

## Keep source coercivity, coordinate inversion and the Franel--Landau destination separate

Stable source recovery above the square-root observation threshold still does not prove the RH-critical discrepancy estimate. The lowbit tree gives a finite-dimensional geometry whose conditioning and random benchmark are simultaneously near-critical, and FD-205--FD-206 show that its quotient coordinates are strong enough to recover the global Mertens destination.

But FD-206 also shows that the present anchored positive norm crosses from recovery to circularity: its root coordinate is exactly an RH-equivalent dyadic Mertens increment on `H_n=n p_n`. The high-value frontier is no longer simply “prove the critical-power lowbit-energy estimate.” It is to find a source-forced mechanism that controls that scalar increment through genuinely additional signed/cross-scale relations, or to redesign the observable so the difficult anchor is not paid positively before the useful geometry acts.