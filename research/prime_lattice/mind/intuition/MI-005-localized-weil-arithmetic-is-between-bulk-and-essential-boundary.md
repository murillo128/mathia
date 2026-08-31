# MI-005 — Completed Weil localization has a wide collapse regime before essential prime-log recurrence

**Evidence level:** supported by exact localized-operator limits, completion cancellation, and zero-free sampling bounds

## Core intuition

The localized Weil operator still has a topology-sensitive split, but the unexplored “mesoscopic middle” is now much narrower. Completion itself cancels the universal PNT boundary mode. Fixed smoothing, growing spatial depth, compensated spatial recentering, and very large moving frequency bands then collapse. The order-one prime-log recurrence seen in norm/Calkin topology survives only on moving states beyond these collapse estimates, at scales already controlled by classical zero-free-region technology rather than by an RH selector.

## Strongest justified principle

PL-044 and PL-049--PL-054 establish the original three-way split: finite localized spectral reality can be prime-free; fixed-depth strong boundary limits vanish or universalize to a rank-one PNT model; operator norm and essential norm retain order-one prime-power partial reflections through Kronecker recurrence.

PL-055--PL-058 close several natural intermediate repairs. Every fixed Sobolev smoothing kills the essential recurrence in norm, including the critical `det_2` endpoint; raw growing boundary depth remains tight near the same endpoint layers; and inward spatial recentering with the natural amplitude compensation is exactly the original problem at a smaller effective half-length. Pure spatial decompactification therefore creates no new topology.

PL-059 identifies the canonical centering: the zeta-pole term converges to the same rank-one PNT boundary operator with opposite sign. The completed pole-minus-prime sector tends strongly to zero while finite-rank completion cannot remove the essential recurrence. The subtraction is no longer a free modeling choice.

PL-060--PL-064 then push norm collapse into genuinely moving regularity regimes. Dirichlet bands with `N(L) r_(L,R)→0` collapse, and the full completed Weil form has negligible archimedean cost throughout the PNT-resolution band. Vinogradov--Korobov and the sharper zero-free sampling estimates rule out all bands with `log N` far below the corresponding classical zero-free scale; in particular every `N=exp(L^α)` with `α<3/2` lies in the audited collapse regime. PL-065 shows the dual consequence: coherent prime-log recurrence witnesses must occur only at extremely large frequencies (up to the stated logarithmic losses).

## What remains possible

A surviving topology must operate near or beyond that ultra-high frequency transition, or be genuinely different from the present Dirichlet-band/Sobolev/spatial families. Reaching the transition is not itself RH evidence: the lower bound is produced by classical zero-free/PNT information and Diophantine recurrence. Any candidate must still survive Beurling controls and produce an invariant not equivalent to inserting the explicit formula.

## Status / novelty

The completion cancellation, smoothing/spatial no-go results, moving-band bounds, and recurrence-delay estimates are persisted findings. The exact location or existence of a rational-prime-specific intermediate limit remains open.

## Falsification criterion

Construct an intrinsic completed-Weil topology inside one of the ruled-out band/smoothing/spatial regimes with a nonzero stable residual; this would contradict the corresponding findings. A positive advance outside them must define the scale before inspecting zeros, prove convergence, and distinguish rational primes from matched generalized-prime systems.

## Lean-formalizable core

- Pole/PNT rank-one cancellation in the localized boundary model.
- Exact spatial recentering self-similarity.
- Abstract band-collapse implication from a uniform discrepancy bound.
