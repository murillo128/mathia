# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Earn genuinely independent translation axes, or beat the positive-kernel diagonal arithmetically

**Linked intuition:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`.

MC-414 localizes the surviving character information in the thin divisor-dependent endpoint domain. MC-415 shows that ordinary positive differencing re-squares the sieve on the zero-shift diagonal. MC-416--MC-417 optimize that diagonal over every scalar positive finite-band stationary kernel: after DC normalization the zero shift is at least `1/H`, with the Fejér kernel extremal. MC-418 shows that positive operator-valued channel lifting does not change this one-variable floor, independently of rank or channel dimension.

MC-419 identifies the exact multivariable escape and its price. For a positive operator-valued trigonometric polynomial on `T^d` with rectangular bandwidths `H_1,...,H_d`, the zero coefficient is bounded below by the point response divided by the bandwidth volume `V_H=prod_j H_j`, and the product Fejér kernel is sharp. Thus extra channel labels are not extra averaging directions; only genuinely independent translation variables multiply the positive-kernel capacity.

The live Möbius question is therefore structural before it is numerical. Can the arithmetic source produce a finite-dimensional state with genuinely independent translation axes, a target reconstruction using those axes, and off-diagonal control that survives their joint positive closure? If not, one remains in the one-variable `1/H` cone and must pay its diagonal with source-specific incomplete endpoint cancellation. If yes, the attainable gain is at best reciprocal bandwidth volume, and the source cost of manufacturing those independent axes must be included rather than treating formal labels as free dimensions.

## Do not count channel multiplicity or formal tensorization as a new escape

A scalar filter bank, positive Toeplitz form, sum of positive shift energies or nonnegative trigonometric multiplier stays inside the MC-417 cone. Replacing the scalar sequence by a finite- or infinite-dimensional source vector stays inside MC-418. MC-419 adds that merely indexing the same physical translation by several formal coordinates does not earn a product bandwidth: the variables must correspond to independent source translations before positivity is imposed. For nonrectangular or sparse multivariable support, even the product Fejér constant need not be the right extremal quantity, so the actual support geometry must be audited rather than inferred from ambient dimension.
