# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-derived sign theorem outside finite Pick universality and positive-Laplace sign regularity

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation` through `MI-036-positive-laplace-mixtures-have-the-wrong-translation-sign-and-universal-hankel-positivity`.

WP-293--WP-318 close the natural pure-measure scalar Julia orbit at one node: derivative normalization reduces the response to a universal Pick/Boolean self-energy form. WP-319--WP-321 then show that source-specific gap laws, sparse common-source coherence and even the full unthinned bounded-gap Julia family remain matched-control realizable in the natural weak topology by one atomlessly smoothed positive source.

WP-322 closes the canonical exact finite-node escape. For any positive scalar Herglotz source, the boundary Loewner matrix at arbitrary regular real nodes is a resolvent Gram, so every finite multipoint Pick matrix, its principal minors and finite Julia reductions are positive for universal reasons.

WP-323 closes the immediate higher-derivative escape as well. For finitely many nodes `t_i` and finite jet orders `r,s`, the normalized confluent Pick matrix is exactly

`C_(i,r),(j,s) = a delta_(r0)delta_(s0) + int dmu(x)/[(x-t_i)^(r+1)(x-t_j)^(s+1)]`,

hence the Gram matrix of the higher resolvent vectors `(x-t_i)^(-r-1)`. Higher exact arithmetic derivatives can change the entries, but they still do not change the **provenance of the sign**.

WP-324 tests the first canonical passage into the different Schoenberg translation-total-positivity geometry suggested by Arithmetic Fidelity. The positive-energy Mangoldt source has Laplace transform `L(s)`, but its ordered translation kernel `L(x-y)` has the exact all-order sign law

`sgn det[L(x_i-y_j)] = (-1)^(m(m-1)/2)`

whenever all differences lie in the positive Laplace domain. In particular its `2x2` and `3x3` ordered translation minors are strictly negative. This is not arithmetic: the same sign-regularity holds for every nondegenerate positive measure. Reversing orientation to `L(x+y)` gives strict Hankel total positivity, but again for every positive measure. Moreover the Mangoldt transform is only defined for positive real Laplace parameter and behaves like `1/s` at the boundary, so it is not itself the globally defined translation profile required by Schoenberg's Pólya-frequency theorem.

The next scalar theorem therefore cannot be another finite Pick determinant or finite jet inequality, nor can it be the direct positive-measure Laplace translation/Hankel construction. A surviving route must use exact support/mass/multiplicative information through a **source-forced nonlinear or non-positive-mixture relation whose sign is nonautomatic**, or change category to genuinely matrix/operator-valued, indefinite-to-positive, infinite-domain, or direct finite--archimedean structure with its own positivity theorem.

## Separate source fingerprint from source-selective sign

Shifted-lattice support, quantized Mangoldt coefficients, tight derivative-biased laws, exact multipoint matrix entries and arbitrary fixed finite boundary derivatives can all be source-specific. The positivity of their scalar Pick-kernel matrices is not. WP-321 says weakly continuous scalar family statistics are reproducible after atomwise smoothing; WP-322 says finite exact multipoint Pick positivity is universal; WP-323 says increasing the finite jet order only enlarges the universal resolvent Gram.

WP-324 adds a different universal matched-control category. Positive source measure forces `log L` to be convex and hence gives the **wrong** `PF_2` translation orientation; at all orders the translation minors are sign-regular. Flipping the orientation makes the kernel Hankel-totally-positive for universal composition reasons. Therefore neither “positive measure” nor “total positivity after an orientation choice” is source-selective by itself.

Future scalar arguments should identify the precise feature that fails all these controls: it must survive as exact arithmetic information while its sign theorem fails for a broad positive-measure class. Numerical arithmetic detail inside a universally positive Gram, a universally sign-regular Laplace kernel, or a universally Hankel-positive kernel is not enough.

## Preserve mass class, curvature, topology, determinant orientation, domain and global coupling as distinct gates

WP-314--WP-324 expose successive independent gates: universal moving tangents, noncompact atom-mass scaling, universal normalized positivity, source-specific compact limits with matched controls, sparse/common-source grafting, all-gap smoothing, exact finite multipoint Gram universality, finite confluent-jet Gram universality, and now positive-Laplace translation sign regularity plus one-sided-domain failure. Passing one gate does not imply the next.

A viable route must change the topology, algebraic category, nonlinear source operation, infinite-domain behavior, or direct finite--archimedean coupling. Infinite jets/nodes are a genuine category change because domain, closability and completion become part of the theorem; they must not be inferred from finite-section positivity. Likewise a Schoenberg-style translation route must derive a globally admissible profile and the correct determinant orientation from the source, rather than treating the source Laplace transform as if it were already the Pólya-frequency object. Each candidate still needs its own matched-control and sign audit.
