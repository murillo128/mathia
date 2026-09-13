# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Transport coherent Jordan/Schur packets between separated frontier blocks without small terminal anchors

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-072--FD-084 push the physical occupation geometry from recurrence to full counting exponent and then to consecutive occupied blocks of length `H^(Theta-delta)` inside every sufficiently late fixed-power future window. FD-085 shows that this set geometry alone cannot supply the finite-entropy multiplicative chain required by the existing GCD-duality accumulation mechanism.

FD-086 restores source information before scalarization. The complete physical Jordan vector `V_(H,D)` has divisor-supported horizon increments, making every horizon in the whole `H^(Theta-delta)` block asymptotically collinear in normalized Jordan space; the normalized Schur equality direction and transverse defect are coherent on the same block.

FD-087 resolves the first exact common-multiple idea. Integer dilation embeds `V_(H,D)` inside `V_(qH,D)` with uniform condition number at most `sqrt(zeta(2))`, so large least common multiples are not themselves an information-loss problem. But every exact copy arising from an anchor `a<=L_H` lies in the terminal quotient sector `floor(N/r)<=L_H`, and the **entire** such sector has `o(1)` normalized near-frontier energy. Additive block thickness can force only anchors on this small scale, so even the union of all exact small-anchor copies cannot transport the bulk frontier packet.

The live inter-block theorem must therefore escape that terminal-sector capacity bound: force an anchor substantially larger than the block length, exploit a signed/bulk quantity outside the terminal quotient sector, prove a destination-energy saving that changes the normalization, or replace common-divisor transport by a multihorizon composition law adapted to coherent packets.

## Keep set occupation, within-block coherence, exact embedding and normalized capacity separate

The established hierarchy is now `recurrence -> full-counting occupation -> polynomial additive blocks -> source-specific projective coherence within each block -> uniformly conditioned exact dilation copies`. None of these implies that the available copies carry a nonvanishing fraction of the normalized frontier state.

FD-085 proves that coarse set geometry cannot imply multiplicative composability; FD-086 proves much stronger local vector coherence; FD-087 proves both that dilation itself is well conditioned and that the small-anchor sector forced by current block thickness is asymptotically negligible. The next theorem must control **where the transported mass lives**, not merely whether an exact copy exists.