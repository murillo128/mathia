# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Earn genuinely independent translation axes, or beat the positive-kernel diagonal arithmetically

**Linked intuition:** `MI-073-source-mode-averaging-collapses-to-a-signature-projector`.

MC-414 localizes the surviving character information in the thin divisor-dependent endpoint domain. MC-415 shows that ordinary positive differencing re-squares the sieve on the zero-shift diagonal. MC-416--MC-417 optimize that diagonal over every scalar positive finite-band stationary kernel: after DC normalization the zero shift is at least `1/H`, with the Fejér kernel extremal. MC-418 shows that positive operator-valued channel lifting does not change this one-variable floor, independently of rank or channel dimension.

MC-419 identifies the exact multivariable escape and its price. For a positive operator-valued trigonometric polynomial on `T^d` with rectangular bandwidths `H_1,...,H_d`, the zero coefficient is bounded below by the point response divided by the bandwidth volume `V_H=prod_j H_j`, and the product Fejér kernel is sharp. Thus extra channel labels are not extra averaging directions; only genuinely independent translation variables multiply the positive-kernel capacity.

MC-420 makes “independent” algebraic rather than notational. If the Fourier support lies in the image of an injective lattice map `A:Z^r->Z^d`, the whole positive symbol factors through the smaller torus `T^r` by `A^T`, with positivity and the mean preserved. The Fejér cost is therefore controlled by the effective integer-lattice support, not by the ambient number of coordinates. In particular the anti-diagonal embedding `h -> (h,-h)` still has the one-dimensional `1/H` floor rather than `1/H^2`.

The live Möbius question is now structural before it is numerical. Can the arithmetic source produce at least two `Z`-linearly independent physical translation directions in the Fourier support before positive closure, together with a target reconstruction and off-diagonal estimates that survive that joint state? If not, a formal two-endpoint or tensor presentation still factors through one translation axis and must pay the one-variable diagonal. If yes, the usable gain is priced by the actual support geometry, not ambient dimension, and the source cost of manufacturing those directions must be included.

## Do not count channel multiplicity, ambient coordinates or formal tensorization as a new escape

A scalar filter bank, positive Toeplitz form, sum of positive shift energies or nonnegative trigonometric multiplier stays inside the MC-417 cone. Replacing the scalar sequence by a finite- or infinite-dimensional source vector stays inside MC-418. MC-419--MC-420 add that merely indexing the same physical translation by several coordinates does not earn a product bandwidth: the Fourier support must have the corresponding integer rank before positivity is imposed. Even then rank alone does not determine the sharp constant for sparse or nonrectangular support, so the actual support geometry must be audited rather than inferred from ambient dimension.
