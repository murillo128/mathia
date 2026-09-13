# MI-004 — Multiplicative horizon descent can preserve the source quotient exactly

**Evidence level:** exact under the false-RH source-record hypothesis through [FD-099](../../findings/FD-099-record-seeded-odd-square-cascades-separate-horizon-descent-from-source-descent.md). It is an obstruction to a class of predecessor-composition arguments, not evidence that source-scale descent is impossible by stronger mechanisms.

FD-099 exposes a second scale inside the Farey predecessor state. The physical horizon `H` is not the sampled source scale; a row `r` probes the quotient `H/r`. A predecessor can contract `H` strongly while changing `r` in the same proportion and leaving `H/r` unchanged.

For every fixed depth `m`, choose a suitable false-RH source record `X` and set

`q_j=4^j 9^(m-j)`, `H_j=q_j X`, for `0<=j<=m`.

Every edge is the exact odd-prime repair already present in the canonical predecessor calculus:

`H_(j+1)=(4/9)H_j`, `q_(j+1)=(4/9)q_j`.

Yet

`H_j/q_j=X`

for the entire chain. Each contraction consumes one stored factor `3^2` in the row and replaces it by `2^2`; the chain ends only when the prepaid odd-square inventory is exhausted. Thus the exponential relative horizon descent `(4/9)^m` is factorization transport of one source spike, not descent through successively smaller source events.

The construction survives the quantitative gates that had looked capable of forcing progress. Every state is frontier-sharp, nonsquarefree-occupied and bounded in normalized record defect for fixed `m`; after a diagonal choice of source records, the occupation/defect deterioration over depths tending to infinity is only subpower. Even a chain with 100% genuinely multiplicative predecessor steps can therefore be source-neutral.

The durable lesson is that **branch type and horizon contraction are not source progress variables**. Any contradiction from growing predecessor depth must either make the sampled quotient decrease, prove that quotient-preserving arithmetic inventory is too small to support the required depth, force source refueling at new scales, or use an exact signed/divisibility invariant that distinguishes reused source mass from fresh source information.

This also clarifies the role of projective quality from MI-003. Projective quality correctly removes a spurious composition loss, but precisely because it is scale-free it cannot by itself distinguish genuine source descent from the FD-099 quotient-preserving cascade. The missing invariant must retain a non-projective source-scale ledger.

**Boundary.** FD-099 diagonalizes finite cascades whose source record depends on the desired depth; it does not construct one infinite chain from a fixed source event. The obstruction applies to arguments that infer source descent from horizon contraction, branch density and projective quality alone. A theorem that forces quotient refresh or quantitatively charges the repeated-prime inventory lies outside it.