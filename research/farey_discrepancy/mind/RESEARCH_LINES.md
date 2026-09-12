# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Couple persistent source-spike packets to the same-horizon denominator

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-066 isolates the direct coherent-packet threshold, FD-068 shows that very low normalized nonsquarefree occupation cannot dominate logarithmic scale for q-subcovariant heads, and FD-069 proves that a single source spike becomes visible in the nonsquarefree numerator at every sufficiently later admissible horizon.

FD-070 now strengthens the pointwise witness to an automatic packet. The physical source is one-Lipschitz, so a spike of height `A_X` forces a backward interval of length comparable with `A_X` on which the source remains comparable. At horizon `T`, reciprocal-floor geometry expands that interval into about `T A_X / X^2` rows, with a fixed fraction divisible by four. Once this quantity diverges,

`U_(T,D) >= (1/(32 zeta(2)) - o(1)) T A_X^3 / X^2`

whenever the packet survives the head.

For a zero-frontier spike `A_X = X^(Theta+o(1))`, this stronger persistence still does not improve the final scalar normalization by waiting longer. The best lower bound from this mechanism occurs at the earliest packet onset. Its fixed-head exponent is `2 Theta (1-Theta)/(2-Theta)`, and comparison with the terminal mechanism reproduces exactly the `Theta = 2/3` boundary already isolated by the coherent-packet analysis.

The remaining theorem is therefore genuinely denominator-coupled. More rows, later horizons, and automatic Lipschitz coherence are no longer missing resources. One must improve the same-horizon bound for the total energy `E_(T,D)` on horizons carrying the forced packet, or find a different source-to-target currency whose normalization does not dilute the captured spike.

## Keep coherence, capture, recurrence, head survival, leverage, and denominator growth separate

FD-066, FD-068, FD-069, and FD-070 control different losses. The new cubic packet closes the possibility that the pointwise witness was too sparse, but it also shows that absolute numerator growth can be neutralized by a faster destination normalization. Future progress should target that exact coupling rather than repeat host-selection or packet-multiplicity arguments.