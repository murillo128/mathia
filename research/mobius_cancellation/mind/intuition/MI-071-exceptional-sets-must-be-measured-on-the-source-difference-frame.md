# MI-071 — Source-frame exceptional geometry is priced jointly by codimension and conductor

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-393](../../findings/MC-393-near-full-rank-source-cost-from-codimension-feedback.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381.

The endpoint frame does not require uniform cancellation for every source character, but exceptional geometry must be measured after pullback to the actual source-difference family. Let `W` be a surviving endpoint-mode space, `H=|W|`, `C=W^perp` and `c=dim C`. MC-386--MC-391 show that abstract Welch extremizers, high dual distance and Sidon-like projected character systems do not model the exact source quotient correctly: sparse endpoint exceptions require substantial genuine four-character collision mass.

MC-392 prices that fourth-moment resource directly by independent source relations. After quotienting duplicate coordinate characters, the exact kernel satisfies

`E_W |g|^4 <= (2c+3)(E_W |g|^2)^2`.

If all nonzero modes outside `B` obey `|g|<=epsilon` with `R epsilon^2<=1`, then

`|B|+1 >= H/(2c+3) (1-R epsilon^2)^2`.

Thus at the desired `epsilon=o(R^(-1/2))`, an exceptional budget `|B|<=K H/R` forces `c=Omega(R)`. Additive collision mass is not an independent knob: linearly many independent quotient relations must exist first.

MC-393 closes the next source-cost loophole. If a trial endpoint source package satisfies `P<=y^A`, then for every fixed `0<beta<1` killing all source primes above `y^beta` costs at most `A/beta` dimensions. The remaining rough-squarefree characters still admit the needed power saving because their prime factors can be packed into blocks below `y^gamma`, `gamma=(1+beta)/2<1`. Feeding this codimension bound into MC-392 gives, for each fixed `eta>0`,

`log P/log y >= min{(1-eta)R, a_eta log log y}`.

The rank coefficient can therefore be made arbitrarily close to one. The source relation budget demanded by sparse endpoint exceptions is not merely linear in rank; inside this fixed-power architecture it costs **near full rank in logarithmic conductor** until the separate `log log y` ceiling takes over.

The reusable audit is now two-stage. First pull exceptional geometry back to the source quotient and compute the codimension needed to support the required moment concentration. Then price that codimension through the physical incidence/conductor map. A combinatorial abundance of relations is not useful if buying those relations already consumes essentially one source unit per endpoint rank.

**Boundary.** MC-393 gives a necessary source-cost lower bound in the exact endpoint/fixed-power package and does not prove linear codimension sufficient, estimate the desired good-mode theorem, bound `M(x)` or imply RH. The `log log y` branch remains, and constants deteriorate as the cutoff exponent tends to one.
