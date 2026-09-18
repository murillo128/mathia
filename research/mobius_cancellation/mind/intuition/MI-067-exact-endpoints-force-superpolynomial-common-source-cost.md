# MI-067 — Exact endpoints force a quantitatively superpolynomial common source cost

**Evidence level:** exact synthesis from [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md), [MC-378](../../findings/MC-378-moving-smooth-frame-forces-iterated-log-source-cost-rate.md), [MC-379](../../findings/MC-379-rough-squarefree-terminal-block-lifts-moving-source-cost-ceiling.md), and [MC-380](../../findings/MC-380-tiny-source-primes-can-be-packed-before-terminal-differencing.md).

Let `P` be the common lower-prime source radical of an exact endpoint package at shell scale `y`, with source rank `R`. MC-377 proves the qualitative escape

`log P / log y -> infinity`,

so every fixed `A>0` eventually fails as an upper bound `P<=y^A`.

MC-378 gives the first moving-parameter rate. Its generic smooth-modulus argument rules out `P<=y^A` when

`A^2=o(R)` and `A 2^(C A)=o(log log y)`,

and yields a rank-sensitive term of order `sqrt(R/log R)` but only a generic `log log log y` analytic ceiling.

MC-379 shows that the analytic ceiling is not intrinsic to the endpoint source class. After removing both very large and very small source primes, every surviving canonical conductor is primitive, squarefree and rough from below, so a terminal squarefree complete-sum saving raises the analytic ceiling to `log log y`. Its price is the `2^(O(A))` codimension consumed by pruning the tiny source coordinates.

MC-380 removes that rank-side price. Under a hypothetical `P<=y^A`, collect the source primes below `T_A=2^(K A)` into a preliminary factor `S`. The primorial bound makes `S=y^(o(1))` in the moving range, so it can be carried through the early differencing stages without spending the large smooth mode subspace. Only the terminal factor has to be rough enough for the product complete-sum estimate. Thus the small primes are **packed rather than deleted**.

The resulting contradiction holds whenever

`A^2=o(R)` and `2^(C A) log log y=o(log y)`,

and gives the current combined source-cost lower bound

`log P/log y >= c min{sqrt(R/log(R+2)), log log y}`

for an absolute nonoptimized `c>0` and all sufficiently large shells.

The conceptual improvement is reusable. A local nuisance coordinate need not be paid as a dimension/codimension loss if the proof architecture has an earlier exact stage that can absorb it while leaving the terminal cancellation mechanism in the good class. Here the distinction between **preliminary factor** and **terminal rough factor** lets one keep MC-378's rank geometry and MC-379's endpoint-specific analytic gain simultaneously.

This should not be generalized mechanically. Packing succeeds because the product of tiny source primes has subpower size in the admissible moving range and because the complete-sum saving only needs roughness at the terminal block. In another architecture the nuisance coordinates may interact nonlocally with the terminal estimate and genuinely require deletion.

**Boundary.** These are source-realization obstructions, not bounds for `M(x)` and not RH implications. They do not prove the displayed rate optimal, nor that every alternative endpoint representation pays a common-radical cost. What is ruled out is one exact endpoint architecture whose shared lower-prime radical remains below the stated moving thresholds.