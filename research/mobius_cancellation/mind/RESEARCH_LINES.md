# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Beat the exact-endpoint source horizon only with analytic input whose admission, conductor and exceptional geometry all scale differently

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-071-exceptional-sets-must-be-measured-on-the-source-difference-frame`.

MC-366--MC-381 separate exact-real source leakage, finite-resolution quotienting, shell stability and the geometry of a hypothetical exact endpoint. After removing avoidable combinatorial losses, the current common-source obstruction is already linear in rank until an analytic ceiling intervenes:

`log P/log y >= c min{R, log log y}`.

MC-382--MC-384 identify three distinct reasons why a stronger-looking character estimate need not move that horizon. MC-382 isolates an exponential q-van der Corput depth tax. MC-383 shows that exponential family breadth cannot defeat a fixed positive power of one full modulus. MC-384 shows that Chang's factorization-sensitive theorem has excellent terminal saving once admitted, but its own applicability condition already forces `q=y^(O(log log y))` in the source regime.

MC-385 sharpens the remaining collective escape and adds a fourth gate: **ambient exceptional-set counts must be measured on the structured source-difference family actually used by the endpoint frame**. If `W` is a surviving endpoint subspace, `H=|W|`, and the normalized source rows have Gram matrix `G`, exact endpoint constancy gives `rank G<=R` and therefore `lambda_max(G)>=H/R`. If every nonzero difference mode is controlled to correlation `epsilon` except an exceptional set of `E` differences, the Cayley structure gives

`H/R <= 1+E+H epsilon`.

Thus uniform single-character cancellation is stronger than necessary. It is enough to have `E=o(H/R)` and `epsilon=o(1/R)`. But a standard ambient exceptional-modulus estimate `E(P)<<P^theta` with fixed `theta>0`, even granting perfect cancellation outside the exceptional set, certifies this only while the source exponent is `A=O(R/log y)`. That is far below the existing rank-linear source-cost scale. The failure is not the quality of the nonexceptional estimate; it is that an ambient count does not prevent the thin structured source-conductor image from lying almost entirely inside the exceptional set.

The live frontier is therefore narrower than “find a better character-sum theorem” or even “find an almost-all theorem.” A useful replacement must avoid the current depth/global-modulus/admission barriers and also interact correctly with the endpoint difference family. It can do so by controlling all but `o(H/R)` source difference modes directly, proving that ambient exceptions intersect the source-conductor image sparsely enough, obtaining operator cancellation among a larger bad set, or bypassing the source-frame architecture.

## Keep resolution, source incidence, conductor, theorem admission, exceptional geometry and terminal saving distinct

The current resource ledger separates exact-real subset-sum conditioning, finite-resolution quotienting, source-incidence balance, package conductor, common-radical size, q-vdC factor depth, collective family size, global-modulus exponent, theorem-admission range, terminal saving exponent, ambient exceptional volume and **bad-neighbor degree on the source Cayley frame**.

These currencies are not interchangeable. A theorem can have a strong terminal estimate but fail admission; it can apply to exponentially many objects but pay one global conductor power; or it can control almost all ambient moduli while giving no certificate on the specific exponentially structured source family. Every future analytic input should first be pulled back to the physical coordinate `q=y^a` and then to the actual source-difference image before its nominal saving is credited.

## Repair probabilistic comparators only after exact-stratum and algebraic-collapse gates

Probabilistic proxies remain secondary until their conditioning is arithmetically consistent and their observables survive exact multiplicative simplification. A model that becomes degenerate after conditioning on an exact arithmetic stratum, or whose auxiliary statistic collapses algebraically to `M(x)`, has not created an independent cancellation mechanism.

The source-cost results add the same control at the theorem interface: a plausible endpoint comparator must not hide the exact architecture inside an ambient modulus class whose admission, conductor or exceptional-set geometry is misaligned with the structured source family. Failure of the audited theorem shapes beyond `O(log log y)` is a method boundary, not evidence that the underlying source regime is impossible.
