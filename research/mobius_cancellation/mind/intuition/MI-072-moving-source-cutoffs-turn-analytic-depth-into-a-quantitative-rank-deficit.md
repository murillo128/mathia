# MI-072 — Moving source cutoffs turn analytic depth into a quantitative rank deficit

**Evidence level:** exact synthesis from `MC-392`--`MC-395`.

Write

`A=log P/log y`, `R=endpoint rank`, `L=log log y`.

MC-392 shows that after restricting to a surviving source-mode space, an `O(H/R)` exceptional family at critical accuracy cannot coexist with low relation codimension: the exact projected-simplex fourth moment forces essentially linear codimension. MC-393 then prices that codimension through the physical source package. For every fixed source cutoff below the shell scale, the relation budget already gives a source-cost coefficient arbitrarily close to one until an independent `log log y` analytic ceiling intervenes.

MC-394 makes the fixed-cutoff quantifiers decisive. If `R=o(L)`, every fixed proportional deficit is eventually impossible, so

`liminf A/R >= 1`.

At a fixed cutoff, only `O(log R)` source dimensions can remain unpaid after the exceptional-family and fourth-moment constraints are combined.

MC-395 makes the conclusion quantitative by allowing the cutoff gap `delta` to move. Reopening the explicit q-van-der-Corput/differencing inequality shows that approaching the shell scale requires `O(A/delta)` stages and therefore pays an analytic tariff of the form

`2^{O(A/delta)}`.

Choosing `delta` from the hypothetical deficit `D=R-A` and feeding the resulting good-mode bound back into the exact codimension inequality yields

`D = O(R^2/L + log R)`

throughout `R=o(L)`. In particular, sufficiently far below the logarithmic horizon the exact endpoint package pays nearly one full source unit per rank, with only the displayed quantitative deficit.

The reusable point is that **a moving structural cutoff and its analytic proof depth are one coupled resource**. A fixed-parameter theorem may hide the tariff that becomes decisive when the cutoff itself is optimized. To claim a stronger source-cost result, one must expose the parameter dependence of the analytic estimate and optimize it jointly with the source codimension rather than tune either side in isolation.

**Boundary.** This is an obstruction inside the current exact endpoint/source-package architecture, not an estimate for `M(x)` and not an RH consequence. The transition `R~log log y` remains open because the term `R^2/L` is then already of order `R`. A different source relation, exceptional geometry, terminal estimate, or destination theorem can change the ledger rather than merely improve the constants in this one.
