# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify cross-horizon overlap rather than one-horizon prime count

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-187--FD-214 separate source information, observation geometry and destination completeness, culminating in a bounded-depth periodic switched filter with a physical super-square-root Floquet blind mode. FD-215--FD-217 then show that a horizon-indexed source may satisfy very large families of exact Möbius Euler sign relations and remain blind at one target: every fixed fractional cutoff `p<=theta N`, `theta<1`, still leaves a prime reservoir that can be retuned.

FD-218 shows that merely requiring one source at two horizons is also insufficient below a geometric threshold. The same deterministic source can serve `N` and `2N`, satisfy the exact Euler laws through `p<=theta H` at each horizon, and retain a macroscopic earlier-prefix defect for every fixed `theta<1/2`. At `theta>=1/2`, the later cutoff reaches all primes up to the earlier horizon and forces the earlier squarefree prefix to be Möbius.

FD-219 extends that first-crossing law through one complete `(0,3,3)` switched period. A single source can serve `N,2N,4N`, keep all three switched observations `O(1)`, obey every required Euler relation, and still carry an `N/log N` defect at the initial horizon for every fixed `theta<1/4`. At `theta>=1/4`, the `4N` cutoff reaches every prime up to `N` and identifies the earlier squarefree prefix. The threshold again comes from literal coverage geometry, not the number of horizons or the fact that a full switching period has elapsed.

The next discriminator is not a formal iteration of the quarter-scale rule. At the fourth horizon `8N` the schedule wraps from depth `3` back to depth `0`, so the sampled-support geometry used by the three-horizon reservoir construction is no longer monotone. Useful continuations should determine whether a common repair reservoir survives this wraparound, or whether the changing observation geometry creates coercivity before literal prime-prefix coverage does.

## Keep local fidelity, persistent identity, overlap geometry and observation support distinct

The source can be exact on many Euler relations without being globally Möbius, and it can persist through an entire switching period while still exploiting uncovered primes. FD-218 and FD-219 provide concrete first-crossing controls: persistence gains prefix rigidity when a later exact-prime window reaches the earlier prefix, but that does not yet classify arbitrary longer nonstationary observation blocks.

A future theorem should therefore state which source coordinates are common across scales, how much of the earlier prefix is covered by later exact constraints, which sampled multiples enter each switched observation, and why any remaining reservoir cannot repair those observations simultaneously. Neither another fixed filter nor a larger isolated prime family addresses that obstruction by itself.