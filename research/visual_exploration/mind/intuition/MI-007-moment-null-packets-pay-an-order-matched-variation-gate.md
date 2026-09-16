# MI-007 — Cusp-adapted moment-null packets are exactly governed by uniform-approximation duality

**Evidence level:** exact synthesis from the finite-window moment/capacity chain VIS-145--VIS-147 and the sine-kernel cusp results [VIS-256](../../findings/VIS-256-finite-moments-do-not-beat-sine-kernel-cusp.md) through [VIS-259](../../findings/VIS-259-cusp-moment-packet-conditioning-is-uniform-approximation-duality.md).

Vanishing moments are useful only relative to the regularity of the destination they are asked to annihilate. In the smooth finite-window regime, removing successive Taylor channels forces the first retained `2m`-th moment to pay a `b^(-2m)` total-variation scale on a shrinking band. VIS-256 shows that the sine-kernel/CUE support edge changes the nuisance basis because the limiting centered profile is the cusp `|q|`, which finite polynomial moments do not remove.

VIS-257 and VIS-258 solve the first two cusp-adapted stages sharply: after cancelling mass and `|q|`, unit quadratic signal costs exactly `8b^(-2)`; after cancelling the quadratic channel too, unit quartic signal costs `E_*^(-1)b^(-4)` with `E_*=0.06346155...`.

VIS-259 identifies the general structure. For order `m>=1`, impose zero mass, zero `|q|` pairing and vanishing even moments through `2m-2`. Put

`V_m = span{1,t,t^2,t^4,...,t^(2m-2)}`

on `[0,1]` and

`E_m = dist_infinity(t^(2m), V_m)`.

Then every admissible signed packet on `[-b,b]` satisfies the **sharp** inequality

`|m_(2m)(nu)| <= E_m b^(2m) ||nu||_TV`,

and equality is attained. Hahn--Banach identifies the quotient norm with an annihilating functional and Riesz represents that functional by the extremal signed measure. Thus the best possible unit-carrier cost over *all* packet shapes is exactly `E_m^(-1)b^(-2m)`.

This turns the cancellation ladder into a complete dual-conditioning problem. The nuisance constraints define a finite-dimensional approximation space; the retained carrier is useful only to the extent that it lies a positive uniform distance from that space; total variation is the dual norm that pays for extracting it. Changing the signed packet ansatz cannot beat this minimax constant.

The destination error must be priced at the same order. If the source contribution is `A_(2m)q^(2m)` and the residual deterministic uncertainty is bounded by `epsilon_b` in sup norm, worst-case separation requires

`epsilon_b < E_m |A_(2m)| b^(2m)`,

with strong asymptotic separation requiring the corresponding ratio to vanish. Extra cancellations are therefore valuable only when the actual source supplies the next coefficient and the transfer/covariance theorem improves fast enough to pay the new conditioning exponent.

The practical consequence is to stop optimizing higher universal packet shapes in isolation. After VIS-259, the scarce resource is **source-carrier existence and same-order error control**, not the extremal measure problem. The quadratic/quartic fork remains live because those are the first source coefficients that could plausibly be derived; higher orders need evidence before their approximation constants matter.

**Boundary.** The theorem is deterministic and uses total variation against sup-norm uncertainty. Structured covariance, sign restrictions or another error norm produce a different dual problem. VIS-259 does not establish any zeta-specific higher coefficient, finite-height transfer law or RH-sensitive residual.