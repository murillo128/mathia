# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Convert early residual witnesses into a coercive finite target certificate

**Linked intuition:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale`.

NB-001--NB-006 establish the original target-information boundary: generator Gram geometry can be copied across multiplicative scale while losing the fixed target, fixed semigroup probes admit Mellin aliases, summable full-semigroup defect norms are noncoercive, and every finite harmonic cutoff can be defeated by scale-dependent aliases.

NB-007--NB-009 sharply separate infinite identification from finite source-selected observability. The untruncated harmonic `ell^2` defect is singular off the target line, but this does not give uniform finite coercivity. Periodicity alone locates a finite residual witness only at the exponential `lcm(2,...,N)` scale. For the **actual best residual**, however, the single normal equation against `g_2` already forces a tail-average witness by index `O(d_N^{-2})`; with the known Nyman lower bound this is `O(log N)`, with polynomially visible amplitude.

The live theorem is now to turn this early source-forced witness into a finite semigroup/dual estimate that materially constrains the approximation distance rather than merely detecting non-target mass. Determine how much truncated harmonic energy, or which additional normal equations, are forced once a witness occurs at polylogarithmic scale.

## Separate exact target identification, witness localization, and approximation-rate coercivity

The full harmonic semigroup identifies the target exactly but is an extended-valued singular selector. The lcm witness proves finite existence at a useless exponential scale. The parity normal equation proves much earlier localization, but it imports the known lower bound on `d_N` only to express the index/amplitude in `N`.

A useful asymptotic theorem must improve the **finite quantitative transport from residual structure to target distance**. Exact character identities, infinite divergence, and the existence of one early witness are controls unless they yield a new coercive rate.