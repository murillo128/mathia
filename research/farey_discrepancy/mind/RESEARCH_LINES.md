# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond log-log growing switched blocks to genuinely cofinal source coherence

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-187--FD-214 separate source information, observation geometry and destination completeness, culminating in a bounded-depth periodic switched filter with a physical super-square-root Floquet blind mode. FD-215--FD-221 then show that every **fixed** switched block remains noncoercive below literal Euler-prefix coverage: exact Euler laws, small scheduled observations and a macroscopic earlier-prefix defect can coexist through any fixed number of dyadic horizons.

FD-222 crosses the first growing-quantifier boundary. For every fixed `C>0` and `0<beta<1`, one can still build a deterministic squarefree comparison source for every block length `J<=C log log N` with exact Euler relations through all primes `p<=beta N`, all switched observations only `O_{C,beta}(2^J)`, and an earlier defect `X_N(N) asymp_{C,beta} N/(2^J log N)`, which remains super-square-root in this regime. The latest Euler window still reaches only `beta N<N`, so literal prefix coverage has not occurred.

The extension is quantitative rather than formal. The positive divisor-reservoir null cycle remains dimension-free, the common floor cells shrink only like `2^{-J}`, and each reservoir still contains enough primes when `2^J` is polylogarithmic. The triangular repair loses at most exponentially in `J`, which a fixed-power Davenport saving absorbs throughout `J=O(log log N)`.

The live frontier has therefore moved again. A stronger theorem must either push the same capacity/conditioning competition to faster-growing `J`, show where it genuinely fails before literal coverage, or impose **one persistent source/cofinal compatibility law** that cannot be rebuilt separately for each `(N,J)`. Another fixed block, or even another `O(log log N)` block with the same per-scale source freedom, no longer changes the information boundary.

## Keep finite-block repair, growing-block capacity, prefix coverage and permanent source identity distinct

The switched observation rank is not the load-bearing quantity. Equal reservoir occupancy creates a constant response that every positive-order difference kills; additional rows matter only through the capacity and conditioning of the repair needed to keep all constraints simultaneous.

FD-222 shows that those quantitative costs remain affordable through logarithmically growing sample depth `E=O(log log N)`: divisor reservoirs have size about `N/(2^J log N)`, while the crude triangular inverse grows exponentially in `J`, and classical Möbius cancellation with a sufficiently large fixed logarithmic exponent dominates that loss. This is a real growing-family theorem, but its comparison source still depends on the horizon scale.

Future work should therefore separate three possible transitions: a faster `J(N)` at which reservoir capacity or repair conditioning breaks, literal Euler-prefix coverage, and cofinal source identity across unbounded horizons. Only the last two change the source information itself; failure of the current construction at some faster growth rate would not by itself prove coercivity unless the obstruction is shown to be intrinsic rather than technical.