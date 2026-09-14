# MI-016 — Growing confluent rank is limited by the Laguerre turning scale, and true one-zero multiplicity stays below it

**Evidence level:** exact growing-rank target-poorness reduction from [NB-109](../../findings/NB-109-near-logarithmic-confluent-rank-remains-target-poor-after-full-backfill.md), sharpened by the explicit weighted coercivity theorem [NB-111](../../findings/NB-111-laguerre-tail-coercion-opens-an-explicit-one-eighth-logarithmic-window.md) and closed for the full true multiplicity of one off-critical zeta zero by [NB-112](../../findings/NB-112-zero-counting-symmetry-eliminates-the-one-zero-multiplicity-rescue.md). No theorem is claimed for several-distinct-zero state spaces or for state constructions outside the NB-111 terminal-band/full-backfill geometry.

For one hypothetical off-critical zero at height `G`, let `S^(d)` be the span of its first `d` confluent derivative states after complete early-cell backfill. NB-109 already showed that the relevant loss is polynomial extrapolation rather than a bad monomial Gram basis. NB-111 identifies the natural weighted geometry and removes the avoidable fixed-base losses behind the earlier `log G/log log G` window.

In the affine coordinate

`z = 2(1-a) log(m/n)`, 

the exact early-cell radial weight is `e^(-z)`, so the derivative packet is a degree-`<d` polynomial subspace in the Laguerre norm. The fixed target endpoint sits at intrinsic depth

`T = 2(1-a) log(m/r)`.

After resolving the physical cells down to approximately half this depth, the observable weighted interval reaches `X=T/2+o(T)`. Laguerre polynomials have their deterministic turning scale at `X=4d`: below that threshold their weighted mass cannot hide in the unobserved tail, while the same generating-function estimate makes the target endpoint jet exponentially small relative to the total Laguerre norm. Therefore

`limsup d/T < 1/8  =>  ||P_(S^(d))e||/||e|| -> 0`.

Uniformly in the horizontal displacement this implies

`d <= (1/8-epsilon) log G  =>  delta -> 0`.

NB-112 then supplies the source-specific fact that the actual multiplicity of an off-critical zeta zero cannot reach this deterministic transition. Functional-equation symmetry pairs `beta+i gamma` with a distinct zero `1-beta+i gamma` of the same multiplicity, so a zero-counting jump spends the multiplicity twice. The Bellotti--Wong explicit error coefficient therefore yields

`mult(beta+i gamma) <= (0.10076+o(1)) log gamma`,

and `0.10076<1/8`. Hence the **entire derivative packet supplied by the true multiplicity of any sufficiently high off-critical zero lies inside the NB-111 target-poor window**. The factor-two same-ordinate symmetry is load-bearing: without it the available jump bound would have coefficient `0.20152`, which is too large.

The one-zero branch is consequently closed at the level of true zeta multiplicity within this geometry. There is no need to improve the `1/8` constant merely to defeat an ever-higher derivative packet from one off-critical zero. Any surviving zero-state mechanism must obtain growing rank from several distinct zeros, or leave the terminal-band/full-backfill representation on which the Laguerre theorem acts.

Once the whole packet has vanishing principal angle to the target, NB-108's leverage-target Pareto law remains dimension-free: `sup_(eta>=theta) chi = 1-theta+o(1)`. The true one-zero packet therefore cannot hide a simultaneous high-leverage/high-target direction either.

**Boundary.** The constant `1/8` remains a deterministic method boundary, not a universal multiplicity theorem. NB-112 uses an external explicit zero-counting estimate plus classical off-critical symmetry and applies only to a single zero's true multiplicity. It does not prevent many distinct off-critical zeros from producing a genuinely multi-center growing-rank state space, and it does not address state constructions outside the NB-111 geometry.