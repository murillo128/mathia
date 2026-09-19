# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Convert the explicit endpoint source-frame gap into analytic cancellation

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-071-exceptional-sets-must-be-measured-on-the-source-difference-frame`.

MC-366--MC-381 separate exact-real source leakage, finite-resolution quotienting, shell stability and the geometry of a hypothetical exact endpoint. After removing avoidable combinatorial losses, the current common-source obstruction is already linear in rank until an analytic ceiling intervenes:

`log P/log y >= c min{R, log log y}`.

MC-382--MC-384 show why stronger-looking character estimates need not move that horizon: q-van der Corput can pay an exponential depth tax, exponential family breadth cannot defeat a fixed positive power of one full modulus, and Chang's factorization-sensitive theorem has excellent terminal saving only after an admission condition that already forces a very large source modulus.

MC-385 adds the source-family exceptional-geometry gate: ambient exceptional-set counts must be measured on the structured source-difference family actually used by the endpoint frame. MC-386 sharpens that gate to the natural quadratic threshold. If `W` is a surviving endpoint subspace, `H=|W|`, and normalized rows have rank at most `R`, Welch energy forces

`H/R-1 <= E+(H-1-E)epsilon^2`.

Thus good modes only need `epsilon=o(R^(-1/2))`, while the generic exceptional budget is `E=o(H/R)`. An annihilator-subgroup Cayley frame attains the `H/R` scale, so abstract PSD/rank geometry cannot improve it.

MC-387 classifies the near-extremizers of that abstract bound. Near-Welch energy together with physical concentration on the minimal `H/R` scale forces the dual Bochner support close to a subgroup coset and the physical exceptional set close to the corresponding annihilator subgroup.

MC-388 pulls that extremizer class through the **actual endpoint source map**. The endpoint Bochner measure is the push-forward of defect weights on the translated coordinate simplex `1+e_z`, whose projected support has affine dimension at least `d-1` when `d=dim W`. In the rank-linear branch this excludes the low-dimensional coset support required by the generic near-extremizer.

MC-389 now makes the resulting gap elementary and explicit. For a finite set `A` in a binary vector space with `r=|A|` and affine dimension `k`, every nonzero translate overlap satisfies

`|A cap (A+t)| <= 2(r-k)`.

Summing these overlaps gives

`E(A) <= r^2+2(r-k)(r^2-r)`.

For the projected endpoint simplex in the high-rank branch `d>=3R/4`, this yields `E(S)<=3r^3/4` for large `R`. After the near-Welch weight reduction, if good nonzero modes satisfy `epsilon_R=o(R^(-1/2))`, every exceptional set obeys the explicit bound

`|B| >= (1+1/4096) H/R`.

The live frontier is no longer “prove that the endpoint avoids the annihilator extremizer” or “make the source gap effective.” The source-side threshold improvement is already explicit. The immediate bottleneck is now the analytic good-mode estimate at the `R^(-1/2)` frame scale; a secondary structural question is whether the projected-simplex geometry yields a larger optimal constant than the deliberately non-optimized `1/4096`.

## Keep resolution, source incidence, conductor, theorem admission, exceptional geometry and terminal saving distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution quotienting, source-incidence balance, package conductor, common-radical size, q-vdC factor depth, collective family size, global-modulus exponent, theorem-admission range, terminal saving exponent, ambient exceptional volume, bad-neighbor degree, source-frame correlation energy, near-extremizer shape, affine rank of the exact source support, additive-energy deficit and the resulting endpoint exceptional gap.

These currencies are not interchangeable. MC-386--MC-389 give a particularly clean sequence: a generic frame lower bound is sharp abstractly; stability identifies the shape of abstract near-sharp examples; the arithmetic source image excludes that rigid class; and the exact affine dimension of the projected simplex then supplies a direct translate-overlap bound and an explicit fixed improvement over the ambient count threshold. Further generic Gram inequalities are unlikely to help unless they deliver the missing analytic `o(R^(-1/2))` good-mode control or exploit more source structure to improve the endpoint constant beyond `1/4096`.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

The endpoint results add the same control at the theorem interface. A plausible comparator must not hide the exact source architecture inside an ambient modulus class or an abstract frame class whose admission, conductor or extremizer geometry is impossible after pullback to the source. MC-389 strengthens the rule: source admissibility can alter not only the extremizer's shape but the **numerical threshold itself**, and in the present high-rank endpoint branch that improvement can be quantified explicitly before the analytic cancellation theorem is supplied.
