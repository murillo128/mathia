# MI-012 — Robin's sparse-host route needs shifted-quartet information, not pointwise phase cancellation alone

**Evidence level:** exact for the host-to-frontier conversion through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md), the deformed-quadratic host reduction through RE-096, the ambient-packing obstruction through RE-097, the resonant four-zero budget through RE-098, and the high-shift separability obstruction through [RE-099](../../findings/RE-099-high-shift-separability-has-a-three-eighths-floor.md). The required joint shifted-energy estimate remains open.

After the higher-depth reductions, the residual bad hosts are sampled at `x(n)=eta_1^(-1)(eta_2(n))`, `n~X^(1/2)`. RE-095 shows that any fixed power saving for intervals of length `X^vartheta` with `vartheta<73/200` improves the Robin frontier. RE-096 supplies stable logarithmic phase geometry, while RE-097 proves that ordinary ambient exceptional-set packing cannot create the needed gain.

RE-098 shows that the near-resonant four-zero population is already adequate: the known additive-energy estimate yields a power saving for

`vartheta > (69-16 sqrt(3))/121 = 0.341216...`,

leaving a nonempty interval below `73/200=0.365`.

The bottleneck is the nonresonant quartet shift `Omega=gamma_1+gamma_2-gamma_3-gamma_4` coupled to

`S_X(Omega)=sum_(n~X^(1/2)) exp(i Omega log x(n))`.

RE-099 proves that **separating these two objects by absolute values cannot work**. At the critical zero slab, even the unrealistically strong pointwise bound `|S_X(Omega)|=X^o(1)` combined with the unstructured `T^4` quartet count requires `vartheta>3/8`, already outside the Robin window. If the effective high-shift quartet mass is `T^(4-eta)` and the pointwise kernel costs `X^kappa`, the separable bookkeeping needs

`eta > (8+200 kappa)/127`.

Thus even ideal pointwise phase control (`kappa=0`) still needs a genuine quartet saving `eta>8/127`. Better exponent-pair technology for `S_X` alone cannot finish the route.

The live theorem must therefore either prove a shifted four-zero saving of at least this scale while retaining the correct weights, or exploit **joint oscillation** between the zero shift and the deformed-quadratic sample without first taking absolute values. The exact target is the weighted high-shift fourth-moment object, not unshifted additive energy and not a standalone exponential sum.

**Boundary.** The `3/8` floor is a limitation of the separable absolute-value architecture, not a lower bound for the true fourth moment. RE-099 does not rule out cancellation in the coupled sum.