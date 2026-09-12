# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Couple a source episode to its denominator near the capture scale

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-066 isolates the direct coherent-packet threshold, FD-068 shows that very low normalized nonsquarefree occupation cannot dominate logarithmic scale for q-subcovariant heads, and FD-069 proves that a single source spike becomes visible in the nonsquarefree numerator at every sufficiently later admissible horizon.

FD-070 strengthens the pointwise witness to an automatic packet. A spike of height `A_X` forces a backward source interval of comparable length and, at horizon `T`, reciprocal-floor geometry expands it into about `T A_X/X^2` rows. Once this quantity diverges, the forced nonsquarefree packet has energy of order `T A_X^3/X^2`.

FD-071 now shows that **waiting longer cannot itself solve the denominator problem**. The complete reciprocal image of the earlier coherent episode has the same cubic-linear order, while an arbitrarily later zero-frontier spike can be sampled on one fixed squarefree prime row and contribute denominator energy of frontier size. For `Theta>1/2`, there are paired frontier episodes and horizons on which the earlier packet has diverging absolute energy but its share of `E_(T,D)` tends to zero.

The remaining theorem must therefore be tied to the episode being exploited. Either prove a favorable denominator estimate at or near the reciprocal onset of that episode, before later source spikes dominate, or obtain a source-specific coupling that controls those later quotient contributions. Arbitrary-horizon persistence is no longer a candidate substitute for such a theorem.

## Keep coherence, capture, recurrence, head survival, leverage, episode location, and denominator growth separate

FD-066--FD-071 control different losses. The cubic packet closes pointwise sparsity, and FD-071 closes the stronger idea that persistent absolute mass must eventually dominate its normalization. Future progress should target the causal relation between the selected source episode and the same-horizon denominator, not repeat host-selection or packet-multiplicity arguments.