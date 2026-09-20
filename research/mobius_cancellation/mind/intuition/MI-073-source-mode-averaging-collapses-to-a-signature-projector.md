# MI-073 — Positive stationary kernels pay Fejér bandwidth volume; channels are not translation axes

**Evidence level:** exact synthesis from MC-409--[MC-419](../../findings/MC-419-multivariable-positive-box-kernels-tensorized-fejer-floor.md), including the endpoint factorization of [MC-414](../../findings/MC-414-shift-position-kernel-is-endpoint-separable.md). No Möbius cancellation beyond the cited estimates is claimed.

The well-factorable frame creates a translated character before completion, and MC-414 localizes the genuinely source-sensitive information in the thin divisor-dependent endpoint domain. MC-415--MC-417 then identify the cost of imposing one-variable finite-band stationary positivity: the zero-shift diagonal cannot fall below the Fejér `1/H` floor after DC normalization. MC-418 shows that replacing scalar coefficients by an arbitrary Hilbert/operator-valued channel does not change that bound. Rank and channel multiplicity are not independent averaging directions.

MC-419 classifies the genuine positive multivariable extension. If `P` is a positive operator-valued trigonometric polynomial on `T^d` supported in the rectangular box `|h_j|<H_j`, with zero coefficient `K_0`, then for every point `xi`

`P(xi) <= (prod_j H_j) K_0`

in Loewner order. Equivalently, the normalized diagonal floor is `1/V_H` with `V_H=prod_j H_j`, and the tensor-product Fejér kernel attains equality. Independent translation axes can therefore multiply the positive-kernel bandwidth, but no additional gain comes from the target dimension carried at each axis.

This sharpens the architectural audit. A proposed tensor or channel construction earns the multivariable floor only if its coordinates arise from genuinely independent physical translations before positive closure and the target observable reconstructs from that joint state. Re-labeling one translation variable, diagonal embedding, or carrying many source coordinates through the same shift remains the one-variable MC-418 situation. Conversely, if independent axes are real, their product bandwidth is the exact positive-kernel resource that must be compared with the arithmetic cost of producing and controlling them.

The arithmetic difficulty is untouched by formal tensorization. The diagonal classification says how cheaply positivity can package already available translation structure; it does not supply the source-specific off-diagonal cancellation needed to exploit the package. For sparse or non-product support the rectangular `V_H` bound can also be nonsharp, so the correct extremal constant must follow the actual support geometry rather than ambient dimension.

**Boundary.** MC-419 concerns finite positive stationary multivariable kernels. It does not rule out nonstationary kernels, controlled indefinite forms, infinite-support limits, or source-specific off-diagonal estimates, and it does not prove that the Möbius architecture supplies more than one independent translation axis.
