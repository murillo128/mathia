# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Move from fixed-block blindness to growing-horizon source coherence

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-187--FD-214 separate source information, observation geometry and destination completeness, culminating in a bounded-depth periodic switched filter with a physical super-square-root Floquet blind mode. FD-215--FD-220 then show, for increasingly long explicit horizon blocks, that exact Euler laws can coexist with bounded switched observations and a macroscopic earlier-prefix defect until a later Euler window literally covers the earlier prefix.

FD-221 closes the remaining fixed-block question. For the periodic depth schedule `(0,3,3)`, **every fixed number of horizons `J`** admits one deterministic squarefree comparison source with exact Euler laws through each horizon's cutoff, all `J` scheduled observations `O_J(1)`, and an `N/log N` defect at the first horizon whenever `theta<2^{-(J-1)}`. At `theta>=2^{-(J-1)}`, the final Euler window contains every prime up to `N` and identifies the earlier squarefree prefix with Möbius.

The mechanism is structural rather than an extrapolation of the half/quarter/eighth examples. Equal occupancy of suitable divisor reservoirs gives a positive null cycle with constant response at all sampled dyadic points, so every positive-order finite-difference filter kills it. A triangular family of positive reservoir pivots then repairs the finitely many remaining observations. Thus no **fixed finite block** of this switched schedule creates a coercive mechanism before literal source coverage.

The live frontier is consequently a quantifier change. FD-221 is nonuniform in `J`; it neither produces one source valid for infinitely many horizons nor controls a growing block `J=J(N)`. A genuinely stronger theorem must exploit coherence that only appears when the horizon depth grows, or prove that approximate/source-realizable Euler constraints accumulate enough rigidity before literal coverage in such a growing regime.

## Keep finite-block repair, prefix coverage and cofinal source identity distinct

A fixed observation panel can be arbitrarily long and still admit positive reservoir repair. What changes at the proven threshold is not the rank of the switched filter but the source information: the latest Euler window has finally covered every prime coordinate that can affect the earlier prefix.

Future work should therefore ask for a uniform-in-`J` capacity law, a single persistent source across an unbounded horizon sequence, or another cofinal compatibility constraint that cannot be solved by the finite positive null cycle. Constructing another fixed block, increasing the finite difference depth, or counting more exact Euler relations without changing this quantifier cannot by itself cross the FD-221 boundary.