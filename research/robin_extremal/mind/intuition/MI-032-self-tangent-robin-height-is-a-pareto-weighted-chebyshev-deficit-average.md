# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral from RE-022 has a canonical positive kernel. After normalization to a probability measure `nu_p` and rescaling `t=py`, that kernel converges to

`(1/2) y^(-3/2) 1_(y>=1) dy`.

Its total mass tends to `2`; asymptotically half of the normalized weight lies below `4p` and half above it, while every additive selector window `[p,p+p^alpha]`, `alpha<1`, carries vanishing mass. The historical height seen by the Robin functional is therefore multiplicatively broad rather than concentrated near the frontier prime.

After this normalization the deterministic Mertens correction is `o(1)`, and the counterexample condition becomes the scale-invariant source requirement

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

This is weaker in form than a pointwise square-root Chebyshev bound and sharper than a vague statement that Robin height depends on prime history. It identifies the exact average that a self-tangent counterexample must pay.

The selector-height question is consequently a propagation problem. Local CA event geometry near `p` controls a vanishing portion of the canonical height measure. A useful source theorem must propagate information over multiplicative scales, control the Pareto-weighted Chebyshev deficit directly on the selected frontier family, or exploit cancellation/correlation across those scales. Improving only a sublinear additive neighborhood cannot cover a nonvanishing fraction of the relevant weight.

**Boundary.** RE-153 does not prove the required upper bound `sqrt(2)-eta`, nor a pointwise Chebyshev estimate. The Pareto law is the deterministic scaling limit of the exact kernel, not a probabilistic model for primes. The opportunity is source-specific control of this selected average, not generic PNT improvement.