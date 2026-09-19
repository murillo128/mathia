# MI-071 — Source-frame exceptional geometry is directly priced by source codimension

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-392](../../findings/MC-392-source-codimension-controls-sparse-exception-budget.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, let `C=W^perp` with codimension resource `c=dim C`, and let `g` be the exact normalized Cayley correlation kernel.

MC-385--MC-389 show that an ambient exceptional count is meaningful only after pullback to the source-difference family. Rank at most `R` gives the generic Welch scale `H/R`, but the actual endpoint Bochner support is a high-dimensional projected simplex rather than a near-extremal low-dimensional coset. In the high-rank branch, if ordinary good modes satisfy `epsilon_R=o(R^(-1/2))`, this source geometry already forces more than the abstract `H/R` floor.

MC-390 adds an orthogonal obstruction. Up to a harmless global sign, the exact endpoint kernel is a weighted coordinate-sign sum. If the dual distance of `W` is at least five, the coordinate signs are four-wise independent and exact second/fourth moments force `Omega(H)` source differences to have correlation at the critical frame scale. High dual distance is therefore hostile to the desired `o(R^(-1/2))` good-mode theorem outside `O(H/R)` exceptions.

MC-391 identifies the additive invariant behind that split. Quotient the coordinate characters by `C`, merge equal classes, and write the resulting distinct classes as `a` with masses `w_a`. With

`sigma^2=sum_a w_a^2`,

the fourth moment is controlled by genuine four-character collisions. In particular, an analytic theorem with at most `K H/R` bad modes and all other modes `o(R^(-1/2))` requires linearly growing normalized quartic collision mass. This rules out Sidon-like or generic high-distance projected character systems.

MC-392 shows that the quartic collision resource is itself not free. Because the support comes from quotienting coordinate vertices by the `c`-dimensional relation space, every nonzero translate pairs at most `c+1` support points. For the weighted probability measure `p=sum_a w_a delta_a`, this gives

`||p*p||_2^2 <= (2c+3) sigma^4`,

and therefore, by Plancherel,

`E_W |g|^4 <= (2c+3)(E_W |g|^2)^2`.

If all nonzero modes outside `B` satisfy `|g(I)|<=epsilon` with `R epsilon^2<=1`, then

`|B|+1 >= H/(2c+3) (1-R epsilon^2)^2`.

At the target scale `epsilon=o(R^(-1/2))`,

`|B|+1 >= (1-o(1)) H/(2c+3)`.

Hence a sparse exceptional theorem `|B|<=K H/R` with fixed `K` requires

`c >= (1-o(1)) R/(2K)-3/2`.

The usable source relation resource is therefore **linear codimension**, not merely the existence or raw count of low-weight relations. Quartic collision mass can only become large enough if the quotient has enough independent source relations to support it. In the fixed-power source model of MC-381, where `c<=A/beta` with `beta=1/100`, MC-392 yields the concrete floor `|B|+1 >= (1-o(1))H/(200A+3)`; sublinear `A` cannot support any fixed `K H/R` exceptional budget.

This sharpens the reusable audit. First pull exceptional geometry back to the physical source frame. Then quotient duplicate characters exactly. Before trying to manufacture quartic collisions, price how many **independent quotient relations** are available. A proposed analytic theorem should be compared directly with the codimension/exception inequality; otherwise combinatorial collision counting can appear promising in a source regime that cannot carry enough total fourth-moment concentration.

The immediate arithmetic question is now whether the actual source package can provide `c=Omega(R)` independent relations at an admissible conductor/source cost, or whether the fixed-power incidence architecture forces `c=o(R)` in the regime where the analytic estimate would need only `O(H/R)` exceptions.

**Boundary.** MC-392 is a necessary resource inequality for the exact exponent-two endpoint quotient. It does not prove that linear codimension is sufficient, estimate the actual analytic good-mode bound, identify every source prime with an independent relation, bound `M(x)`, prove Möbius cancellation, or imply RH. The matching argument depends on the projected-coordinate-simplex origin and on the exponent-two quotient.
