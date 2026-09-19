# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Classify finite-block repair cones rather than counting horizons

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-187--FD-214 separate source information, observation geometry and destination completeness, culminating in a bounded-depth periodic switched filter with a physical super-square-root Floquet blind mode. FD-215--FD-217 then show that a horizon-indexed source may satisfy very large families of exact Möbius Euler sign relations and remain blind at one target: every fixed fractional cutoff `p<=theta N`, `theta<1`, still leaves a prime reservoir that can be retuned.

FD-218 turns persistence into a geometric overlap threshold. The same deterministic source can serve `N` and `2N`, satisfy the exact Euler laws through `p<=theta H` at both horizons, and retain a macroscopic earlier-prefix defect for every fixed `theta<1/2`. At `theta>=1/2`, the later cutoff reaches all primes up to the earlier horizon and forces the earlier squarefree prefix to be Möbius.

FD-219 extends the same first-crossing law through one complete `(0,3,3)` switched period. One source can serve `N,2N,4N`, keep all three scheduled observations `O(1)`, and retain an `N/log N` defect for every fixed `theta<1/4`; at `theta>=1/4`, literal prime-prefix coverage identifies the earlier prefix.

FD-220 resolves the first scheduler wraparound. For the four horizons `N,2N,4N,8N` with depths `(0,3,3,0)`, one common source still remains blind for every fixed `theta<1/8`. The exact repair system has a four-dimensional high-reservoir response matrix with determinant `112`, and the low-reservoir response lies in its positive cone with coefficients `(1,3/7,10/7,11/7)`. Thus the wrapped depth-zero observation can be repaired while preserving an `N/log N` prefix defect. At `theta>=1/8`, the `8N` Euler window reaches every prime up to `N` and again forces the earlier squarefree prefix to be Möbius.

So the first wrap itself is **not** a new coercive mechanism. Through four horizons, the sharp boundary is still literal source coverage, while observation geometry enters through the existence of enough positive repair directions. The next question is structural: for an arbitrary fixed finite block of the periodic schedule, do the corresponding response vectors always admit a positive-cone repair of the low-prefix defect until prime-prefix coverage becomes exhaustive, or is there a first later block whose response cone fails earlier? FD-220 does not establish either alternative.

## Keep local fidelity, persistent identity, overlap geometry and reachable-cone support distinct

The source can be exact on many Euler relations without being globally Möbius, and it can persist through a complete period plus the first wrap while still exploiting uncovered primes. The relevant object is no longer merely the number of horizons or monotonicity of sampled support. For each finite block one must identify the common source coordinates, the latest exact-prime coverage, the observation response vectors of the remaining prime reservoirs, and whether the required correction lies in their **positive reachable cone** with enough asymptotic capacity.

A future theorem should therefore either prove a uniform reservoir/cone mechanism for every fixed block or isolate a concrete block where positivity/rank/capacity fails before literal coverage. Extrapolating `1/2,1/4,1/8` to all horizons without that response-cone theorem would exceed the current evidence, and another isolated fixed filter or larger prime family would not answer the structural question.