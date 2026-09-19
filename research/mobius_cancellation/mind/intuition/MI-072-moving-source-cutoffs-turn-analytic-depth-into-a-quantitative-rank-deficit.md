# MI-072 — Paired source packing separates the genuine analytic tariff from the moving-gap artifact

**Evidence level:** exact synthesis from `MC-392`--`MC-396`.

Write `A=log P/log y`, `R=endpoint rank`, and `L=log log y`. MC-392 shows that after restricting to a surviving source-mode space, an `O(H/R)` exceptional family at critical accuracy cannot coexist with low relation codimension: the exact projected-simplex fourth moment forces essentially linear codimension. MC-393 then prices that codimension through the physical source package, and MC-394 gives `liminf A/R>=1` throughout `R=o(L)`.

MC-395 reopened the explicit q-van-der-Corput/differencing inequality with a moving smoothness gap `delta`. Its greedy modulus factorization bounded each closed block separately from below and therefore used `O(A/delta)` differencing stages, producing a power-saving tariff of the form `2^(-O(A/delta))` and the quantitative deficit

`R-A = O(R^2/L + log R)`.

MC-396 identifies the `1/delta` stage count as an artifact of that intermediate packing estimate. For next-fit greedy blocks below the cap `B=y^(1-delta/2)`, every consecutive pair satisfies

`B_j B_(j+1) > B`.

Since the total conductor is at most `y^A`, pairing consecutive blocks gives only `O(A)` blocks uniformly as `delta->0`. The rough terminal and differencing calculation then has

`σ_(A,delta) >= c delta 2^(-C A)`

for absolute `c,C>0`. The gap still weakens the final saving, but it no longer multiplies the proof depth.

Feeding that corrected analytic estimate back into the exact codimension inequality sharpens the source-cost conclusion to

`A >= R-O(log(R+2))`

for every `R=o(L)`. More strongly, the same logarithmic unpaid rank persists for `R<=kappa_0 L` for some absolute `kappa_0>0`. The former `R^2/L` deficit was therefore not the intrinsic transition-scale obstruction.

The reusable point is more precise than “moving parameters cost proof depth.” **Expose the internal combinatorics before declaring that parameter dependence intrinsic.** A moving cutoff can genuinely weaken the analytic saving, but a lossy factorization can add a second, artificial dependence. Here the invariant of two consecutive greedy blocks removes the artificial inverse-gap depth while leaving the genuine `2^(O(A))` tariff and the linear `delta` loss visible.

**Boundary.** This remains an obstruction inside the current exact endpoint/source-package architecture, not an estimate for `M(x)` and not an RH consequence. The constant `kappa_0` is not optimized. Beyond the fixed-fraction logarithmic range, the genuine `2^(O(A))` differencing tariff, the `O(R)` exceptional family, source incidence, or the destination theorem may still become decisive.
