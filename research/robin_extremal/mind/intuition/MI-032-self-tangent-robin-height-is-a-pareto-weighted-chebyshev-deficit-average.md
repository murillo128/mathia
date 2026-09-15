# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with terminal-horizon sensitivity

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstructions [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md) and [RE-155](../../findings/RE-155-pnt-stable-source-surgery-survives-to-any-fixed-fraction-of-the-robin-horizon.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral has a canonical positive kernel. After normalization and rescaling `t=py`, the kernel converges to the Pareto law `(1/2)y^(-3/2)dy`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154 shows that at fixed multiplicative distance only `sqrt(p)/log p` coherent post-selector relocations are enough to move this exact average by order one. Such controls can agree exactly with the ordinary primes below any fixed `Bp`, remain PNT-dense and alter only a vanishing fraction of labels.

RE-155 shows that the fixed-`B` qualifier was not the real boundary. Let `U=U_A(p)` be the full RE-022 horizon. For labels at fixed fractions `yU<zU`, equal-cardinality relocation cancels the leading endpoint subtraction and leaves the influence difference

`Lambda_p(yU)-Lambda_p(zU) ~ [sqrt(p) log p/(2U)](1/y-1/z)`.

Therefore `m_p~U/(sqrt(p)log p)` relocations inside any fixed terminal fractional annulus move the normalized source coordinate by a fixed amount while the source agrees exactly with the ordinary primes and generalized CA event history through `cU`, for arbitrary fixed `c<1`, and remains `o(1)`-close at PNT scale.

The propagation interpretation is now sharp: **knowing the source exactly through every fixed fraction `(1-epsilon)U_A(p)` does not determine the destination average if the remaining terminal information is only PNT-scale density**. The live source bill sits in a shrinking relative terminal layer or in stronger arithmetic information capable of forbidding coherent terminal relocation.

The reusable distinction is between ambient source closeness and destination-weighted closeness. A perturbation that is negligible for prime counting and exact on almost the whole finite horizon can remain order-one in the Robin functional because the terminal labels carry a coherent signed influence. Any approximation theorem should therefore be tested in the exact Pareto/Robin kernel norm rather than by propagation radius or PNT density alone.

**Boundary.** RE-155 does not treat propagation to `(1-o(1))U_A(p)`, where a fixed fractional relocation shell no longer fits, and it does not claim the ordinary primes admit the synthetic surgery. Strong short-interval information, a signed square-root estimate, an explicit-formula restriction or an exact global CA identity can distinguish the controls. The result identifies the remaining information requirement; it does not prove the required `sqrt(2)-eta` bound.
