# MI-067 — Exact endpoints force a quantitatively superpolynomial common source cost

**Evidence level:** exact synthesis from [MC-377](../../findings/MC-377-smooth-subspace-prime-frame-forces-superpolynomial-source-cost.md), [MC-378](../../findings/MC-378-moving-smooth-frame-forces-iterated-log-source-cost-rate.md), and [MC-379](../../findings/MC-379-rough-squarefree-terminal-block-lifts-moving-source-cost-ceiling.md).

Let `P` be the common lower-prime source radical of an exact endpoint package at shell scale `y`, with source rank `R`. MC-377 proves the qualitative escape

`log P / log y -> infinity`,

so every fixed `A>0` eventually fails as an upper bound `P<=y^A`.

MC-378 gives the first moving-parameter rate. Its generic smooth-modulus argument rules out `P<=y^A` when

`A^2=o(R)` and `A 2^(C A)=o(log log y)`,

and yields, with a nonoptimized absolute constant,

`log P/log y >= c min{sqrt(R/log(R+2)), log log log y}`.

MC-379 shows that the `log log log y` analytic ceiling is not intrinsic to the endpoint source class. Assuming `P<=y^A`, remove source coordinates from primes above `y^(1/(32A))` and from primes below `2^(K A)`. The codimension cost is only `2^(O(A))`, while every surviving canonical source conductor is primitive, squarefree and rough from below. For the terminal squarefree block `Q`, the prime-local complete-sum estimate can then be multiplied before the final differencing root; the collision average costs only a factor of the form

`prod_(p|Q) (1+k/sqrt(p))`,

which roughness absorbs into a fixed negative power of `Q`. This avoids the generic moving-depth condition `k 2^k << log log Q` inherited by MC-378.

The resulting contradiction holds whenever

`2^(C A)=o(R)` and `2^(C A) log log y=o(log y)`,

so every exact endpoint package also satisfies

`log P/log y >= c min{log(R+2), log log y}`

for a possibly different absolute `c>0` and all sufficiently large shells.

The MC-378 and MC-379 bounds are complementary rather than ordered. MC-378 retains a stronger `sqrt(R/log R)` rank-side scale in some regimes; MC-379 raises the source-specific analytic ceiling from `log log log y` to `log log y` but pays `2^(O(A))` small-prime pruning and final differencing costs. The current lower bound should therefore be read through the stronger theorem in the relevant `(R,y)` regime, not compressed to one universal displayed asymptotic.

This sharpens the source-cost lesson: a generic theorem's moving-parameter tariff need not be the tariff of the actual source family. Here the endpoint incidence structure forces squarefree primitive conductors and permits an extra roughness projection; those source-specific facts materially improve the available cancellation estimate before the destination frame argument is applied.

**Boundary.** These are source-realization obstructions, not bounds for `M(x)` and not RH implications. They do not prove either quantitative rate optimal, nor that every alternative endpoint representation pays a common-radical cost. What is ruled out is one exact endpoint architecture whose shared lower-prime radical remains below the stated moving thresholds.