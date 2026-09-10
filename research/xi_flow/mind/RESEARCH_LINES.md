# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into quantitative transition coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`.

XF-154--XF-168 separate source identification from RH transition control. Positive complete-monotone Jacobi-reflecting mixtures can have the wrong heat origin when scaled square lattices are allowed, while exact support on the single Xi lattice `pi n^2` forces the theta coefficients by Hamburger rigidity.

XF-169 identifies the residual freedom exactly. Positive log-scale mixtures preserving the normalized Riemann functional equation multiply the completed zeta function by a self-reciprocal entire Mellin factor; the same factor multiplies the time-zero Xi transform. Small lattice displacement is therefore spectrally active even though the functional equation does not see it. XF-170 proves the sharp quantitative boundary for this whole positive compact mixture class: if the logarithmic support displacement is `delta`, every newly introduced nonreal zero satisfies `delta |Re z| >= 4 pi`, with equality attainable by a three-point mixture.

XF-171 adds a compact-support-free stability modulus inside the same positive normalized scale-mixture gauge. The intrinsic central Mellin deficit `d=1-M(1/2)` obeys `|M(s)-M(1/2)| <= 4 d |s-1/2|^2` throughout the critical strip, so `d < 1/(4T^2+2)` excludes all added multiplier zeros through height `T`. The XF-167 three-point family has `d T^2 -> pi^2/16`, showing that the `T ~ d^{-1/2}` resolution scale is optimal in order even though the universal constant is not claimed sharp.

The live theorem should now propagate exact or approximate square-lattice rigidity at the resolution relevant to the de Bruijn--Newman transition. A concrete positive target is to derive `d(T)=o(T^{-2})`, or an atomwise analogue, from an approximate single-square-lattice source law; that would rule out added common-mixture off-critical zeros through height `T`. Otherwise one must leave the common scale-mixture gauge and show directly that the actual single-lattice source law supplies the mesoscopic mass/collision coercivity needed by the heat flow. Another qualitative source identifier is not enough.

## Treat functional-equation preservation and finite-height source resolution as separate gates

The normalized functional equation admits a nontrivial scale-mixture gauge. Positivity and compact support make that gauge quantitatively resolvable at the sharp inverse-displacement height of XF-170; XF-171 shows that even without compact support the central Mellin defect gives an order-sharp inverse-square-root height modulus. Future stability statements should therefore carry an explicit height-versus-source-resolution modulus. The unresolved step is no longer whether the common positive scale-mixture gauge is quantitatively visible, but whether approximate square-lattice information controls a strong enough defect at the height where the transition must be decided.