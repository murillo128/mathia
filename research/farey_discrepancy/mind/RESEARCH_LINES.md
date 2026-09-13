# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Couple sharp occupied frontier packets to bounded normalized-energy record defect

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`, `MI-002-odd-prime-square-reembedding-localizes-recursive-failure-to-dyadic-channel`, `MI-003-normalized-record-defect-is-the-composition-loss`.

The false-RH frontier construction has already passed the abundance and predecessor-entropy gates. Repeated-prime deflation transports fixed positive parent shares to exact lower nonsquarefree masks, and every dyadic terminal coordinate except the row-two/source-head atom has an exact lower repair.

[FD-094](../findings/FD-094-normalized-schur-energy-records-upgrade-frontier-carriers-to-fixed-occupation.md) identifies the composition loss for every repairable carrier. For

`F_sigma(N)=E_(N,1)/N^(2 sigma)`

and

`R_sigma(H)=max(1, sup_(N<H) F_sigma(N)/F_sigma(H))`,

a frontier-normalized lower carrier occupies at least a fixed transport constant divided by `R_sigma(H)`. At an `F_sigma` record this is automatically a fixed lower-state occupation fraction; any uniform bound `R_sigma(H)=O(1)` is enough.

[FD-095](../findings/FD-095-bounded-record-defect-turns-the-source-head-into-an-amplitude-scale-predecessor.md) removes the source-head atom as a separate gate under the same hypothesis. If the head value `|mathcal H(B)|^2` carries a fixed parent share and `R_sigma(H)<=K`, move backward by a fixed fraction of `|mathcal H(B)|` and reembed the nearby source value on row `4`. The resulting horizon `C<H` has fixed nonsquarefree occupation, comparable normalized energy, and bounded inherited record defect. On a sharp frontier the retreat has additive length at least `H^(Theta-o(1))` while staying on the same power scale.

Thus the current one-step composition problem has a single residual: **show bounded normalized-energy record defect along some sufficiently sharp occupied packet sequence**, or find another mechanism that supplies the same historical denominator control. False RH gives infinitely many strict `F_sigma` records for `1/2<sigma<Theta`, while `FD-083`--`FD-084` give abundant sharp occupied horizons and long occupied additive blocks; the missing theorem is a quantitative coupling between those two structures.

## Control constant degradation under repeated predecessor descent

`FD-094` and `FD-095` now give one-step closure: a sharp occupied state with bounded `R_sigma` has some lower sharp occupied state whose `R_sigma` is again bounded. This is not yet a uniform infinite descent. In the repairable branches the new defect bound loses the inverse transport constant, while in the source-head branch it loses roughly the reciprocal of the retained head fraction. Repeated use can therefore make the constants deteriorate even though each individual step remains independent of the physical horizon.

The geometry is also mixed. Odd-prime repairs can contract by a fixed factor, whereas a sharp source-head step retreats only additively by `H^(Theta-o(1))` when `Theta<1`. A multistep argument therefore needs an invariant, a periodic return to fresh normalized-energy records, or another mechanism preventing the occupation/record constants from degrading over the number of predecessor steps required to reach a genuinely smaller scale.

## Keep one-step closure, record coupling and iterated composition separate

Exact lower representation is no longer the residual issue. At bounded record defect, every current branch including the source head has fixed lower occupation and bounded inherited defect. What remains are two logically different questions: first, whether sharp occupied frontier packets ever occur with bounded historical defect; second, if they do, whether the one-step constants can be stabilized across enough successive descents. Future work should not reintroduce the source-head atom as an independent local representability obstruction unless the bounded-record hypothesis has first been shown to fail.
