# MI-035 — Lowbit shell control recovers global Mertens through quotient ladders rather than fixed physical modes

**Evidence level:** exact synthesis from [FD-204](../../findings/FD-204-lowbit-tree-achieves-logarithmic-resistance-at-near-critical-random-cost.md) and [FD-205](../../findings/FD-205-binary-quotient-ladders-promote-lowbit-shell-control-to-an-rh-criterion.md).

FD-204 constructs a source-localized multiscale observation geometry with two properties that had previously competed: anchored inverse resistance is only logarithmic, while each physical Möbius slab is reused only once per dyadic scale, so the squarefree-random comparator pays `H^(1+o(1))` rather than the older `H^(3/2)` tariff.

FD-205 proves that this near-critical auxiliary energy is not merely a well-conditioned local surrogate. For every target integer `n`, choose a prime `p_n` with `n/2<p_n<=n` and two nearby horizons so that the relevant shell quotient coordinates are `n` and `2n+b`, with `b in {0,1}`. The corresponding lowbit edge is exactly the Mertens increment

`M(2n+b)-M(n)`.

Iterating these increments along the binary quotient ancestry of an arbitrary `N` telescopes from `N` to a bounded base point. The physical prime and horizon may change at every step; what stays coherent is the internal quotient coordinate. Consequently a uniform critical-power estimate

`G_(2,H)^lb = O_epsilon(H^(1+epsilon))`

for all sufficiently large horizons promotes to square-root Mertens control and hence RH. More quantitatively, a bound `G_(2,H)^lb=O(H log^A H)` yields the corresponding square-root Mertens bound with only the accumulated logarithmic ladder loss.

The reusable insight is that **cross-scale coherence need not mean holding the physical sensor fixed**. A representation can change prime, horizon and shell from one scale to the next while remaining globally coherent if an exact internal coordinate is preserved and its local increments telescope to the destination quantity. This distinguishes genuine transport from fixed-mode aesthetics: the invariant to preserve is whatever coordinate makes the source relation exact.

**Boundary.** FD-205 proves the recovery implication, not the required deterministic lowbit-energy estimate. The random comparator is evidence that the source-overlap geometry is near the desired power scale, not evidence that Möbius arithmetic satisfies the same bound. The current theorem surface is precisely the uniform critical-power estimate for the physical lowbit energy.