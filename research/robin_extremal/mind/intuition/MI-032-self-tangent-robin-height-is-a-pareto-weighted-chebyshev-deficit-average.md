# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with an exact post-selector sensitivity scale

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstruction [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral from RE-022 has a canonical positive kernel. After normalization to a probability measure `nu_p` and rescaling `t=py`, that kernel converges to

`(1/2) y^(-3/2) 1_(y>=1) dy`.

Its total mass tends to `2`; asymptotically half of the normalized weight lies below `4p` and half above it, while every additive selector window `[p,p+p^alpha]`, `alpha<1`, carries vanishing mass. After normalization the deterministic Mertens correction is `o(1)`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154 computes how sensitive this exact average is to post-selector source changes. If one label at `q=yp` is inserted or deleted at fixed `y>1`, its normalized influence satisfies

`Lambda_p(yp) = (log p)/(2 sqrt p) * y^(-1) + o(log p/sqrt p)`.

Therefore only `m_p asymp sqrt(p)/log p` coherently relocated labels are enough to move the Pareto-weighted source average by a fixed order-one amount. Such controls can agree exactly with the ordinary primes below any fixed multiplicative cutoff `Bp`, remain PNT-dense, and have only `O(sqrt p)` Chebyshev discrepancy on the affected shell; the altered proportion of labels in that shell is merely `asymp p^(-1/2)`.

This turns the selector-height problem into a quantified propagation problem. Local CA event geometry near `p` controls vanishing kernel mass, while even exact knowledge through `Bp` plus coarse PNT information leaves an order-one destination ambiguity. A useful source theorem must couple the selected CA state to later multiplicative shells, control the Pareto-weighted Chebyshev deficit directly with a sharp signed/constant-level estimate, or derive another ordinary-prime constraint that forbids the coherent relocation mechanism.

The reusable distinction is between **ambient source closeness and destination-weighted closeness**. A perturbation affecting a vanishing fraction of labels can remain large in the exact Robin functional because each affected label carries influence `asymp log p/sqrt p`. Any proposed approximation theorem should therefore be tested in the Pareto kernel norm, not only through PNT density, finite selector agreement or unweighted counting distance.

**Boundary.** RE-153--RE-154 do not prove the required upper bound `sqrt(2)-eta`, nor a pointwise Chebyshev estimate. The Pareto law is the deterministic scaling limit of the exact kernel, not a probabilistic model for primes. The RE-154 controls are synthetic increasing real prime-like sources, not ordinary-prime systems preserving CA arithmetic. Their role is to show exactly which source coupling a successful theorem must use.