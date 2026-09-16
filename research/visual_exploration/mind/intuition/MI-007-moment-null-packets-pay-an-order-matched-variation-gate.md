# MI-007 — Moment-null shrinking packets are limited by destination regularity and conditioning

**Evidence level:** exact synthesis from the finite-window moment/capacity chain VIS-145--VIS-147 and the sine-kernel cusp results [VIS-256](../../findings/VIS-256-finite-moments-do-not-beat-sine-kernel-cusp.md)--[VIS-257](../../findings/VIS-257-cusp-annihilation-exposes-finite-window-quadratic-conditioning.md).

Vanishing moments are useful only relative to the regularity of the function they are asked to annihilate. In the smooth finite-window regime, VIS-145 shows that a zero second frequency moment removes the common quadratic centered-cosine response. VIS-146 then gives the exact conditioning bill `|m_(2j)(nu_b)|<=b^(2j)||nu_b||_TV`; keeping an order-one `2j`-th moment on bandwidth `b` costs at least `b^(-2j)` variation.

VIS-256 shows that this Taylor-order picture is incomplete at a nonsmooth destination. The centered sine-kernel/CUE form-factor increment is `T(q)=min(|q|,1)`, so near zero the destination is the cusp `|q|`. For every fixed polynomial cancellation order there are bounded-normalization packets that annihilate that entire finite Taylor jet while retaining an exact `Theta(b)` cusp response. Ordinary moments do not control the singular profile.

VIS-257 answers the obvious next question: cancel the cusp itself. For every symmetric signed measure on `[-b,b]` with zero mass and zero `|q|` pairing,

`|m_2(nu)| <= (b^2/8)||nu||_TV`.

The constant is sharp, attained by `nu_b*=delta_0-2 sigma_(b/2)+sigma_b`. Therefore a cusp-annihilating packet normalized by `m_2=1` necessarily has `||nu||_TV>=8/b^2`. Cusp adaptation is possible, but it converts the former `O(b)` universal response into a sharp quadratic conditioning problem.

This matters because the finite-window null is not exactly the limiting cusp. In the small-frequency regime its centered CUE correction contains the quadratic term `2 pi^2 mu_2 q^2` plus quartic remainder. Pairing the extremal cusp-null packet gives a leading finite-window contribution of order `mu_2 b^2`; when the packet is renormalized to fixed quadratic signal, the same `b^(-2)` factor exposes whatever uncertainty remains in that quadratic null channel.

The correct design principle is therefore a fork, not a generic call for more moments. **If the source signal lives in the quadratic channel**, kill the cusp but keep `m_2` and prove/calibrate the finite-window null and source errors at the corresponding `o(b^2)` scale before variation amplification. **If the quadratic channel is also nuisance**, impose `m_2=0` and accept that the first possible signal moves to quartic or higher order with the associated conditioning cost.

This gives a reusable order of operations: identify the actual singular part of the destination, annihilate it in its natural dual coordinate, then price the first surviving smooth moment against total variation and finite-window error. Polynomial moment count alone is neither the right regularity descriptor nor a conditioning budget.

**Boundary.** VIS-257 gives a sharp deterministic inequality for symmetric finite signed packets and the current finite-window quadratic expansion. It does not prove a zeta-specific arithmetic residual, a uniform finite-height transfer theorem, or that the quadratic source channel has favorable sign. If cancellation order grows or the finite-window profile changes scale before `bM->0`, the conditioning analysis must be redone.
