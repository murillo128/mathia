# MI-071 — Exceptional sets must be measured on the source-difference frame, not only in the ambient modulus space

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) and [MC-386](../../findings/MC-386-welch-energy-makes-source-exception-threshold-sharp.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space.

MC-385 used the operator row-sum bound to show that a bad-difference set must be measured after pullback to the source Cayley frame rather than in ambient conductor space. MC-386 identifies the sharper generic scale by using the exact frame potential. Rank at most `R` forces

`sum_(I,J) |G_(I,J)|^2 >= H^2/R`,

hence total off-diagonal squared correlation at least `H^2/R-H`. If only `E` nonzero difference modes are exceptional with trivial bound one and every other difference has correlation at most `epsilon`, Cayley multiplicity gives

`H/R-1 <= E+(H-1-E)epsilon^2`.

Therefore the frame contradiction survives whenever

`E=o(H/R)` and `epsilon=o(R^(-1/2))`.

The second threshold is strictly weaker than the earlier row-sum sufficient condition `epsilon=o(1/R)` and is the natural quadratic-correlation scale. The first threshold is essentially sharp for abstract source frames: annihilator-subgroup Cayley examples concentrate all nontrivial correlation on about `H/R` difference modes while saturating the rank/Welch energy, exactly on powers of two and within a constant factor more generally.

MC-385 still explains why standard fixed-power exceptional-modulus counts miss this target. Under a trial source bound `P<=y^A`, an ambient theorem with at most `P^theta` exceptional conductors need not control the intersection with the thin structured source-conductor image. MC-386 adds that generic PSD/rank geometry cannot lower the required exceptional incidence below `H/R`; an improvement has to exploit arithmetic restrictions on which near-extremal Cayley frames the source can realize.

The reusable lesson is twofold. **Almost-all information must be pulled back through the exact source map before it is priced, and its quality should then be measured in the natural source-frame energy rather than an unnecessarily strong pointwise norm.** A small ambient exceptional fraction can cover all destination-visible source points, while a source-conditioned theorem can tolerate many bad modes provided their incidence and the remaining squared correlation stay below the Welch budget.

**Boundary.** MC-386 gives a sharp abstract frame benchmark, not an arithmetic extremizer for the actual Möbius source family. A source-adapted theorem could exclude annihilator-like near-extremizers or obtain signed/operator cancellation among a larger bad set. Neither MC-385 nor MC-386 improves the source-cost lower bound or implies an estimate for `M(x)` or RH.