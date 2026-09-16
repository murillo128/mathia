# MI-007 — Moment-null shrinking packets are limited by destination regularity and sharp order-matched conditioning

**Evidence level:** exact synthesis from the finite-window moment/capacity chain VIS-145--VIS-147 and the sine-kernel cusp results [VIS-256](../../findings/VIS-256-finite-moments-do-not-beat-sine-kernel-cusp.md)--[VIS-258](../../findings/VIS-258-cusp-plus-quadratic-null-sharp-quartic-conditioning.md).

Vanishing moments are useful only relative to the regularity of the function they are asked to annihilate. In the smooth finite-window regime, VIS-145 shows that a zero second frequency moment removes the common quadratic centered-cosine response. VIS-146 then gives the exact conditioning bill `|m_(2j)(nu_b)|<=b^(2j)||nu_b||_TV`; keeping an order-one `2j`-th moment on bandwidth `b` costs at least `b^(-2j)` variation.

VIS-256 shows that this Taylor-order picture is incomplete at a nonsmooth destination. The centered sine-kernel/CUE form-factor increment is `T(q)=min(|q|,1)`, so near zero the destination is the cusp `|q|`. For every fixed polynomial cancellation order there are bounded-normalization packets that annihilate that entire finite Taylor jet while retaining an exact `Theta(b)` cusp response. Ordinary moments do not control the singular profile.

VIS-257 answers the first cusp-adapted question. For every symmetric signed measure on `[-b,b]` with zero mass and zero `|q|` pairing,

`|m_2(nu)| <= (b^2/8)||nu||_TV`.

The constant is sharp, so retaining unit quadratic signal after cancelling the cusp costs exactly `8b^(-2)` total variation at the optimum.

VIS-258 closes the next branch as sharply. If the packet also annihilates the quadratic moment, then

`|m_4(nu)| <= E_* b^4 ||nu||_TV`,

with `E_*=0.06346155...`; equivalently unit quartic signal costs

`K_* b^(-4)`,  `K_*=E_*^(-1)=15.75757...`.

The extremizer is symmetric on four radii `0, u b, v b, b`, with `u≈0.28443` and `v≈0.77708`, and the sharp constant comes from the best degree-two uniform approximation of `t^4` on `[0,1]`. Thus the quartic bill is not just dimensional `Theta(b^(-4))`: the exact destination-independent constant and optimizer are known.

The finite-window null must be calibrated at the same order. After cancelling both the cusp and quadratic channel, any transfer/covariance uncertainty `epsilon_b` is amplified by the quartic normalization. To isolate a quartic coefficient `A_4`, strong separation requires

`epsilon_b/(E_* |A_4| b^4) -> 0`.

The correct design principle is therefore recursive and exact: identify the singular part of the destination, annihilate it in its natural dual coordinate, decide which smooth moment carries source signal, and then price that first surviving moment against the **sharp approximation-theoretic conditioning constant** and the finite-window error at the same order. More cancellations can improve nuisance rejection only if the source and transfer theorem survive the matching power of `b`.

**Boundary.** VIS-258 is a sharp deterministic quartic inequality for symmetric finite signed packets. It does not supply the zeta-specific quartic coefficient, its sign, or a uniform finite-height transfer theorem with `o(b^4)` error. Higher cancellations require a new extremal approximation problem; the quartic constant cannot be extrapolated to them. Nothing here proves an RH-sensitive residual.