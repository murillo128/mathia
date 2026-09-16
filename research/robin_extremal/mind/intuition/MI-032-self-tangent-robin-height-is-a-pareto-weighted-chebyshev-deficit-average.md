# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with a fourth-root terminal-capacity boundary

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstructions [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md), [RE-155](../../findings/RE-155-pnt-stable-source-surgery-survives-to-any-fixed-fraction-of-the-robin-horizon.md), and the shrinking-layer capacity law [RE-156](../../findings/RE-156-terminal-source-relocation-capacity-has-a-fourth-root-transition.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral has a canonical positive kernel. After normalization and rescaling `t=py`, the kernel converges to the Pareto law `(1/2)y^(-3/2)dy`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154 shows that at fixed multiplicative distance only `sqrt(p)/log p` coherent post-selector relocations are enough to move this exact average by order one. RE-155 shows that the fixed-distance qualifier is not the real boundary: equal-cardinality relocation inside any fixed terminal fraction of the full horizon `U=U_A(p)` can still change the normalized source coordinate by order one while exact source/generalized-CA agreement holds below that fraction and the modified source remains PNT-indistinguishable.

RE-156 identifies the first quantitative boundary of that control architecture. For the shrinking terminal layer

`T_p(epsilon)=[(1-epsilon)U,U]`,

the total equal-cardinality relocation capacity satisfies

`Cap_p(epsilon) asymp epsilon^2 sqrt(p) log p / log U`

whenever the layer is above the PNT remainder scale. The dimensionless capacity is therefore

`K_p(epsilon)=(epsilon/epsilon_*(p))^2`,

with

`epsilon_*(p)=sqrt(log U/(sqrt(p)log p)) = sqrt(A) p^(-1/4)(log p)^(1/3)(log log p)^(1/6)`.

The existing unconditional PNT remainder is already smaller than this transition. Consequently an asymptotically vanishing fraction of available terminal labels still produces any fixed displacement when `epsilon/epsilon_* -> infinity`; at `epsilon asymp epsilon_*` the relocation class has order-one total capacity; only when `epsilon=o(epsilon_*)` does this particular equal-cardinality surgery become `o(1)` in the Robin functional.

The propagation interpretation is now quantitative: **exact source agreement through `(1-epsilon_p)U_A(p)` is still insufficient at PNT information level throughout the supercritical fourth-root regime.** A propagation theorem only begins to outrun this matched control once the unresolved relative terminal width is below `epsilon_*`; even there, RE-156 does not say that the Pareto source is controlled, because other structured signed perturbations may remain.

The reusable distinction is between ambient source closeness and destination-weighted capacity. A perturbation can be negligible for prime counting, exact on almost the whole finite horizon, and still carry order-one destination leverage because the number of movable labels times their local influence slope remains finite. The right audit variable is the capacity product, not propagation radius alone.

**Boundary.** RE-156 classifies one equal-cardinality terminal-relocation mechanism in the PNT-valid shrinking-layer regime. It does not claim the ordinary primes realize the surgery, does not prove source control below `epsilon_*`, and does not exclude stronger short-interval/signed controls, explicit-formula restrictions, global CA identities or different structured perturbations. Crossing the fourth-root scale is a necessary improvement over the known matched control, not a proof of the required `sqrt(2)-eta` bound.
