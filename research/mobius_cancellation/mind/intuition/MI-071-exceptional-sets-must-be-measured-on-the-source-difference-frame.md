# MI-071 — Exceptional sets must be measured on the source frame, whose near-sharp geometry is annihilator-rigid

**Evidence level:** exact synthesis from [MC-385](../../findings/MC-385-fixed-power-exceptional-moduli-cannot-feed-rank-linear-source-frame.md) through [MC-387](../../findings/MC-387-near-welch-concentration-forces-annihilator-stability.md), interpreted against the endpoint source-frame bounds of MC-374 and MC-381 and the analytic ceilings MC-382--MC-384.

The endpoint frame does not require uniform cancellation for every source character. Let `W` be a surviving endpoint-mode subspace, `H=|W|`, and let `G` be the Gram matrix of its normalized source rows. Exact endpoint constancy puts all rows in an `R`-dimensional space.

MC-385 used the operator row-sum bound to show that a bad-difference set must be measured after pullback to the source Cayley frame rather than in ambient conductor space. MC-386 identifies the sharper generic scale by using the exact frame potential. Rank at most `R` forces

`sum_(I,J) |G_(I,J)|^2 >= H^2/R`,

hence total off-diagonal squared correlation at least `H^2/R-H`. If only `E` nonzero difference modes are exceptional with trivial bound one and every other difference has correlation at most `epsilon`, Cayley multiplicity gives

`H/R-1 <= E+(H-1-E)epsilon^2`.

Therefore the frame contradiction survives whenever `E=o(H/R)` and `epsilon=o(R^(-1/2))`. The exceptional threshold is essentially sharp for abstract source frames: annihilator-subgroup Cayley examples concentrate all nontrivial correlation on about `H/R` difference modes while saturating the rank/Welch energy.

MC-387 proves that this sharp model is also the only asymptotic near-extremal geometry once the correlation energy is concentrated on the minimal physical scale. A PSD Cayley kernel has a finite Bochner representation `g(x)=sum_xi p(xi)xi(x)` with `p` a probability measure. Near-Welch equality forces `p` nearly uniform on an `R`-sized support. Concentrating almost all physical `L^2` mass on about `H/R` points forces near equality in the `l^1*l^2 -> l^2` Young contraction, hence near-maximal additive energy of the Fourier support. Stability of near-maximal additive energy then forces that support close to a subgroup coset; inverse Fourier transform sends the model coset to the corresponding annihilator subgroup in physical space.

Thus **source-conditioned exceptional incidence has both a scale and a shape**. The generic allowed budget is `H/R`, but approaching that budget requires an almost-coset dual spectrum and an almost-annihilator physical exceptional set. A source-adapted theorem no longer has to beat every abstract PSD frame; it can instead attack whether the actual arithmetic source map is compatible with this rigid near-extremizer class.

This sharpens the original pullback principle. A small ambient exceptional fraction can cover all destination-visible source points, so ambient counts remain insufficient. But once the exceptional set is pulled back, merely counting it is also incomplete near the sharp threshold: the relevant question is whether the source-difference frame can organize those exceptional modes into the additive subgroup geometry required by near equality.

**Boundary.** MC-387 is an abstract finite-harmonic stability theorem, not an arithmetic exclusion. It does not show that quadratic-character source rows cannot approach a coset/annihilator frame, and it does not improve the common-source lower bound or imply an estimate for `M(x)` or RH. The unresolved object is the compatibility of near-coset Fourier support with conductor reduction, character multiplication and source-prime reuse in the actual endpoint family.