# MI-028 — Sparse midpoint rigidity comes from cross-coordinate multiplicativity, not coefficient fidelity

**Evidence level:** exact synthesis from [FD-170](../../findings/FD-170-consecutive-midpoint-history-inverts-the-entire-source.md) through [FD-175](../../findings/FD-175-geometric-midpoint-ladders-admit-sparse-squarefree-deletion-null-sources-without-multiplicativity.md).

The midpoint sequence is a changing linear observation of the source. Consecutive horizons invert it exactly, while `FD-172`--`FD-174` show that geometric sparse horizons still certify Möbius inside a squarefree multiplicative cone. It is tempting to attribute that recovery to coefficient sparsity, the ternary Möbius alphabet, or correct prime signs. `FD-175` separates those effects.

A counterexample can keep `a(n)` in `{0,mu(n)}`, preserve every prime coefficient, preserve any prescribed finite prefix and even preserve every fixed finite multiplicative-rank layer, yet agree with Möbius at every horizon `B^m`. The only missing structure is the global rule coupling a high-rank squarefree composite to the product of its prime coordinates.

The reusable geometric mechanism is a **balanced-row dilation plus fresh-shell repair**. If the midpoint row at `h` is already balanced, then at `Bh` the leading scaled part cancels and each old modified coordinate contributes only the bounded rounding defect

`|W_(Bh)(d)-B W_h(d)| <= floor(B/2)`.

The top half-shell `(Bh/2,Bh]` consists of fresh unit-weight coordinates. Möbius supplies linearly many squarefree coefficients of either sign there, so a small set of sign-compatible deletions can pay the entire old-support debt and restore the next sampled equality. Repeating this produces one permanent sparse null source; for `B>=3` the repair set can have density zero.

The lesson is broader than this midpoint formula. Sparse observation can look coercive after imposing many coordinatewise source restrictions and still fail if the admissible class lacks **cross-coordinate compatibility** strong enough to stop fresh degrees of freedom from repairing each new row. In the present line, multiplicativity is exactly such a compatibility: it turns independently selectable composite coefficients into products of already-exposed prime defects, removing the repair reservoir.

**Boundary.** This does not weaken the geometric target-rigidity theorems inside the multiplicative cone, identify the weakest multiplicative substitute, give pairwise sparse inversion, or improve the Franel--Landau destination estimate. The next structural target is a quantitative compatibility condition between isolated coefficient fidelity and full multiplicativity that makes recursive shell repair impossible.
