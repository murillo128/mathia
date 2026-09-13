# MI-005 — Source-neutral carrier descent spends a strict finite row potential

**Evidence level:** proved for the exact carrier genealogies covered by FD-091, FD-093 and FD-100. No theorem yet lifts the potential to the adaptive energy packets used by the full predecessor argument.

FD-099 shows that horizon descent can be arbitrarily deep while the sampled source quotient stays fixed: repeated-square inventory can prepay many genuine `4/9` contractions. Taken alone, that makes multiplicative horizon motion a poor proxy for source progress.

FD-100 identifies the missing finite resource. On an exact carrier state `H=rX` with nonsquarefree `r>=4`, every currently available source-neutral non-head repair replaces `r` by a nonsquarefree `r'` satisfying `4 <= r' <= r/2`. Therefore

`I(r)=log_2(r/4)`

is a strict integer-scale potential: each source-neutral repair spends at least one unit, and after at most `ceil(log_2(r_0/4))` steps the genealogy reaches the unique minimal nonsquarefree row `r=4`, where the next dyadic deflation is the source-moving head atom.

The obstruction has therefore changed category. A fixed exact carrier cannot hide forever behind quotient-preserving factorization transport. What remains is to **lift the finite inventory charge through adaptive packet selection** without losing the projective quality that made the predecessor argument useful, and then to accumulate the much weaker source-moving head displacement.

This suggests a sharper invariant than horizon scale alone: couple packet quality to a carrier-inventory budget that is conserved or decreases under non-head transport and can only be replenished by changing the sampled source scale. A proof at the packet level would turn source refresh from an informal requirement into an amortized theorem.

**Boundary.** The strict potential is exact for carrier-coordinate genealogies. It does not yet control how the energy argument reselects rows between steps, how much mass follows one genealogy, or whether repeated source-moving head steps accumulate fast enough for an RH contradiction.