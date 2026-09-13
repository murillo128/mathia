# MI-012 — Source-conditioned pair kernels close the sampled-host theorem and lower the mixed depth-two frontier

**Evidence level:** exact for the host-to-frontier conversion through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md), the deformed-quadratic host reduction through RE-096, the ambient-packing obstruction through RE-097, fourth-moment diagnostics through RE-098--RE-099, the lower-strip second-moment splice through RE-100, and the full pair-kernel closure through [RE-101](../../findings/RE-101-pair-kernel-second-moments-close-the-sparse-host-tail-and-break-173-over-200.md).

The residual bad hosts are sampled at the deformed-quadratic points `x(n)=eta_1^(-1)(eta_2(n))`, `n~X^(1/2)`. RE-095 shows that any fixed power saving for prime-free intervals of length `X^vartheta`, with `vartheta<73/200`, lowers the mixed first/depth-two Robin frontier.

RE-098--RE-099 identify a genuine `3/8` floor inside a global fourth-moment architecture. RE-100 then shows the destination does not need that statistic on most of the critical strip: a trigonometric-large-sieve second moment plus zero-density bounds already gives polynomial sampled-host savings through `beta~0.814--0.815`.

RE-101 closes the remaining high-beta tail by refusing the full frequency-span relaxation. Expand the **same second moment** directly over zero pairs with difference `Delta=gamma-gamma'`. The deformed sample has enough phase structure to give two deterministic kernel regimes: Kusmin--Landau yields `M/(1+|Delta|)` for near differences, while second-derivative van der Corput gives a `T^(1/2)` bound for far differences. Unit-bin zero counts make the near-pair total essentially linear in `N(sigma,T)`; the far pairs may pay `N(sigma,T)^2` because the kernel is cheaper.

The resulting slab second moment carries the cost

`M N(sigma,T) + T^(1/2) N(sigma,T)^2`

instead of `T N(sigma,T)`. Bourgain density then controls the finite high-beta strip, and the remaining `beta>=15/16` contribution is absolutely `o(H)` after the high-sigma density estimate and zero-free edge are charged. No zero-pair correlation or unproved spacing input is needed.

Therefore every fixed `1901/5216 < vartheta < 73/200` gives a polynomial saving for the complete sampled bad-host set. Balancing that saving in RE-095 yields the explicit mixed first/depth-two frontier

`Theta > 265657/307200 = 0.8647688802...`,

strictly below `173/200`.

The durable lesson is stronger than “second moments are cheaper.” **Once the source sample has nontrivial phase curvature, expand the destination moment against that exact source geometry before replacing it by a generic large-sieve span cost.** Near and far frequency pairs can consume different resources, and a theorem that is too expensive globally may become sufficient after this source-conditioned split.

The previous fourth-moment `3/8` obstruction remains valid for that method; it simply does not limit the sampled-host destination. The active Robin obstruction has moved out of this channel, so further high-beta optimization here should be justified only if another surviving channel later makes this exponent dominant again.

**Boundary.** RE-101 improves the residual mixed first/depth-two scalar frontier, not every Robin channel and not RH. The pair-kernel theorem depends on the exact deformed-quadratic phase geometry and current zero-density/zero-free inputs; it is not a generic theorem for arbitrary sparse samples.