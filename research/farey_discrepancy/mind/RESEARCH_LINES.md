# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify cross-horizon overlap rather than one-horizon prime count

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-187--FD-214 separate source information, observation geometry and destination completeness, culminating in a bounded-depth periodic switched filter with a physical super-square-root Floquet blind mode. FD-215--FD-217 then show that a horizon-indexed source may satisfy very large families of exact Möbius Euler sign relations and remain blind at one target: every fixed fractional cutoff `p<=theta N`, `theta<1`, still leaves a prime reservoir that can be retuned.

FD-218 shows that merely requiring one source at two horizons is also insufficient below a geometric threshold. The same deterministic source can serve `N` and `2N`, satisfy the exact Euler laws through `p<=theta H` at each horizon, and retain a macroscopic earlier-prefix defect for every fixed `theta<1/2`. At `theta>=1/2`, the later cutoff reaches all primes up to the earlier horizon and forces the earlier squarefree prefix to be Möbius.

The live discriminator is therefore **coverage overlap on the prefix being tested**. Useful continuations should classify more general horizon ratios, several coupled horizons, shrinking cutoffs or source-independent observables that create equivalent overlap without assuming full Möbius data. Relation count and persistence are not enough unless the moving constraint windows actually close the repair reservoir.

## Keep local fidelity, persistent identity and overlap geometry distinct

The source can be exact on many Euler relations without being globally Möbius, and it can persist across multiple scales while still exploiting uncovered primes. The first-crossing threshold in FD-218 is a concrete control: persistence gains coercivity only when the later information reaches the earlier prefix.

A future theorem should therefore state which source coordinates are common across scales, how much of the earlier prefix is covered by later exact constraints, and why any remaining reservoir cannot repair the switched observation. Neither another fixed filter nor a larger isolated prime family addresses that obstruction by itself.