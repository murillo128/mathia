# MI-036 — Growing local moment cancellation must pay in Poisson-width support or exponential conditioning

**Evidence level:** exact synthesis from [NB-161](../../findings/NB-161-collapsing-jordan-transport-loses-fixed-target-gain.md) through [NB-164](../../findings/NB-164-growing-moment-cancellation-forces-linear-poisson-width-support-or-exponential-conditioning.md). The minimax duality and Chebyshev approximation ingredients are classical; the line-specific consequence concerns the exterior signed Poisson sampler architecture.

NB-163 shows that every fixed finite moment order is governed by one normalized currency: if moments through order `r-1` vanish, the first uncontrolled absolute moment controls both the Poisson target and the generic Euler response at the natural boundary scale. It leaves `r->infinity` open because fixed-order Taylor constants need not remain uniform.

NB-164 closes that escape on the target side without Taylor expansion. After scaling a sampler of radius `L` around the target ordinate, annihilation of all polynomials of degree below `r` means that its normalized Poisson response is bounded by the distance of

`g_delta(y)=delta^2/(delta^2+y^2)`, `delta=x/L`,

to polynomials of degree below `r` in `C[-1,1]`. Hahn--Banach/Riesz duality makes this not merely an estimate but the exact signed-measure capacity under unit total variation.

The Chebyshev series of `g_delta` has geometric tail parameter

`q_delta=sqrt(1+delta^2)-delta=exp(-arsinh(delta))`.

If `d_r` is the first even degree not below `r`, the minimax error is trapped, up to the explicit adjacent powers, between constants times `q_delta^(d_r)`. Therefore a sampler confined to any fixed number of Poisson widths has normalized target capacity decaying exponentially in the number of vanished moments.

This produces a sharp resource tradeoff. If the support radius satisfies `L<=Lambda x` and the sampler must retain a fixed fraction of natural target gain, its total-variation conditioning must obey an exponential lower bound in `r`. At one Poisson width the base is `1+sqrt(2)`. Conversely, if conditioning stays bounded, the support radius must grow at least linearly in `r` measured in Poisson widths; polynomial conditioning still forces at least `Omega(r/log r)` spreading.

The important point is that this obstruction happens **before any Euler-side arithmetic is used**. Even perfect von Mangoldt phase cancellation cannot rescue a growing-order sampler that remains genuinely local with bounded conditioning, because the target itself has already been projected exponentially close to the annihilated polynomial space. Increasing formal cancellation order is not a new arithmetic currency unless the construction also pays for nonlocal support or deteriorating conditioning.

The bounded-conditioning frontier is therefore narrower than after NB-163. One-Poisson-width local interlacing can remain viable only through genuinely source-specific cancellation at bounded or otherwise controlled effective order. An increasing-order construction must become nonlocal, and its support growth must then be analyzed together with the separated-sign/adverse-zero mechanisms already known at larger scales.

**Boundary.** NB-164 is a target-side capacity theorem. It does not rule out arithmetic phase cancellation at fixed/slowly controlled order, and it does not prove that the support growth required for large `r` is sufficient to build a useful sampler. The exact exponential rate is for fixed scaled support radius; once `L/x` diverges, the theorem supplies a necessary spreading law rather than a complete classification. The result does not replace source-faithful finite-section Nyman--Beurling analysis or imply RH.