# MI-001 — Farey frontier blocks carry coherent super-block anchor packets, but composition remains row-adaptive

**Evidence level:** supported by the exact physical occupation reductions through FD-084, the matched geometric control FD-085, the divisor-supported transport inequality FD-086, the exact dilation/terminal-sector bounds FD-087, and the repeated-prime deflation construction FD-088. No theorem yet composes separated frontier blocks into the finite-entropy multiplicative transport needed by the current accumulation route.

FD-071--FD-084 show that every sufficiently late fixed-power future window contains a constant-strength occupied block of length `L_H=H^(Theta-delta)`. FD-085 proves that abundance and even linear additive blocks do not by themselves imply a bounded-ratio integer chain, while FD-086 shows that the complete physical Jordan vectors are projectively coherent throughout each such block.

FD-087 tests exact inter-block transport and separates two issues. Integer dilation is uniformly well conditioned, so exact copies themselves are not information-destroying. But every exact copy forced from an anchor `a<=L_H` lies in the terminal quotient sector, and the normalized energy of the entire sector tends to zero. Small common anchors therefore cannot transport the bulk frontier packet.

FD-088 realizes the first genuine escape from that capacity obstruction. On the false-RH near-frontier blocks, almost all occupied nonsquarefree energy lies in the complementary core. Moving each core row to its next multiple inside the same block changes the stitched vector by only `o(sqrt(E_H))`. Removing one copy of a repeated prime factor preserves the Jordan weight exactly and turns each nonsquarefree stitched coordinate into an exact dilation witness from a lower physical horizon `a_r`.

These anchors are parametrically larger than the additive block length:

`a_r >> sqrt(H L_H) >> L_H`,

while remaining genuinely earlier than the destination horizon. At the minimal head `D=1`, a fixed positive fraction of the near-frontier energy is carried by this row-adaptive packet, with unit weight distortion, and every destination state stays inside the same vanishing projective cap.

The obstruction has therefore moved. Bulk exact anchors exist, but they do not collapse to one common lower horizon: `a_r` depends on the row, and no current GCD-duality or Schur identity composes the packet into one physical lower-state energy across separated frontier blocks. The next theorem must be a **multihorizon composition law** or another exact aggregation mechanism that preserves the coherent packet without forcing it back through a negligible common-anchor sector.

**Boundary.** The clean positive-mass statement is at `D=1`; for a fixed general head there is only a finite exceptional band. FD-088 is conditional on the false-RH frontier setup used by the line and does not itself produce an inter-block multiplicative chain, contradiction, or RH proof.