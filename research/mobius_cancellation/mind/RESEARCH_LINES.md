# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove signed near-balance before the one-sided dense-model quotient

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`.

MC-188--MC-233 reduce the first-shell obstruction to a sparse source-coupled family of ordinary reduced-residue Möbius progression sums

\[
M_\mu(Z;q,a),
\qquad q=X^{2\alpha+o(1)},
\qquad Z=X^{1-\beta+o(1)}.
\]

Support closes `2\alpha+\beta\ge1/2`. In the strict hard region `2\alpha+\beta<1/2`, the componentwise sufficient target needs fixed-power relative cancellation `X^{-(1/2-2\alpha-\beta)+o(1)}`.

MC-234--MC-235 remove qualitative parity and polynomial sign scarcity. The Matomäki--Teräväinen Linnik machinery already gives both signs essentially full occupancy exponent in every fixed interior hard progression. The missing quantity is therefore their **difference**, not their separate abundance.

MC-236 identifies where the published dense-model route loses exactly that information. The sign-specific dense model preserves each principal-character mean exactly, so it transports any pre-existing sign bias rather than damping it. The subsequent threshold/product-set argument is deliberately one-sided, and the published separate-sign transference precision in the Möbius specialization is only `q^{-o(1)}` relative to its one-sided main scale. The first-shell target instead needs a fixed negative power of `q` at every fixed interior point.

Therefore the existing nonnegative pipeline cannot be upgraded by simply transferring `+` and `-` separately and subtracting at the end. A viable theorem must couple the signs **before** support thresholding and absolute-value errors, for example through a signed Fourier/convolution invariant with fixed-power resolution, or exploit coherent cancellation after recombining the subpower family of smooth dilations from MC-233.

## Treat gauge, support, Boolean conditioning, smooth inversion, sign abundance, transference resolution, and signed amplitude as separate gates

High incidence is cheap by support. Exact-cell membership and the Boolean transform cost only `X^{o(1)}`. At logarithmic smoothness, the primorial coprimality mask unfolds into only `X^{o(1)}` ordinary progression sums. Each Möbius sign already has essentially full-exponent abundance in every fixed strict hard component.

None of these reductions supplies near-balance. MC-236 adds a sharper warning: a nonnegative dense model can be excellent for coverage while preserving the principal sign bias exactly, and a subpower relative comparison error is too coarse for a fixed-power signed target. The remaining theorem must be genuinely signed or exploit aggregate cancellation that avoids the componentwise triangle inequality.

Future progress should therefore be credited only when it controls the source-selected **signed amplitude at the required power scale** or proves a recombination mechanism that makes that componentwise target unnecessary. More representative-existence theorems, unsigned density, or reuse of the current separate-sign transference bounds do not cross the live gate.