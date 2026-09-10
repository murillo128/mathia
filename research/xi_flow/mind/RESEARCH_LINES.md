# Xi-flow research lines

This file holds the current mathematical questions suggested by the durable Xi-flow intuitions. It is not a roadmap, task queue, status page, or history.

## Convert exact square-lattice identification into quantitative transition coercivity

**Linked intuitions:** `MI-004-endpoint-prime-free-fourier-sector-is-volterra-triangular`, `MI-008-gaussian-reference-localization-is-relatively-exact-but-not-global`, `MI-011-cross-scale-observability-can-compress-to-one-off-circle-heat-trace`, `MI-012-xi-tail-hazard-is-source-specific-but-not-yet-coercive`.

XF-154--XF-168 separate source identification from RH transition control. Positive complete-monotone Jacobi-reflecting mixtures can have the wrong heat origin when scaled square lattices are allowed, while exact support on the single Xi lattice `pi n^2` forces the theta coefficients by Hamburger rigidity.

XF-169 identifies the residual freedom exactly. Positive log-scale mixtures preserving the normalized Riemann functional equation multiply the completed zeta function by a self-reciprocal entire Mellin factor; the same factor multiplies the time-zero Xi transform. Small lattice displacement is therefore spectrally active even though the functional equation does not see it. XF-170 proves the sharp quantitative boundary for this whole positive compact mixture class: if the logarithmic support displacement is `delta`, every newly introduced nonreal zero satisfies `delta |Re z| >= 4 pi`, with equality attainable by a three-point mixture.

The live theorem should now propagate exact or approximate square-lattice rigidity at the resolution relevant to the de Bruijn--Newman transition. Either derive an intrinsic source condition that bounds the allowed support displacement as a function of zero height, or show directly that the actual single-lattice source law supplies the mesoscopic mass/collision coercivity needed by the heat flow. Another qualitative source identifier is not enough.

## Treat functional-equation preservation and finite-height source resolution as separate gates

The normalized functional equation admits a nontrivial scale-mixture gauge. Positivity and compact support make that gauge quantitatively resolvable only at inverse-displacement height, not at all heights uniformly. Future stability statements should therefore carry an explicit height-versus-support-resolution modulus; otherwise an arbitrarily small source perturbation can move its first failure beyond the tested spectral window without being harmless globally.