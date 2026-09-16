# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Find a source-derived sign theorem outside finite Pick universality, positive-Laplace sign regularity and universal Bernstein constructions

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation` through `MI-036-positive-laplace-mixtures-have-the-wrong-translation-sign-and-universal-hankel-positivity`.

WP-293--WP-318 close the natural pure-measure scalar Julia orbit at one node: derivative normalization reduces the response to a universal Pick/Boolean self-energy form. WP-319--WP-321 then show that source-specific gap laws, sparse common-source coherence and even the full unthinned bounded-gap Julia family remain matched-control realizable in the natural weak topology by one atomlessly smoothed positive source.

WP-322 closes the canonical exact finite-node escape. For any positive scalar Herglotz source, the boundary Loewner matrix at arbitrary regular real nodes is a resolvent Gram, so every finite multipoint Pick matrix, its principal minors and finite Julia reductions are positive for universal reasons.

WP-323 closes the immediate higher-derivative escape as well. For finitely many nodes `t_i` and finite jet orders `r,s`, the normalized confluent Pick matrix is exactly the Gram matrix of the higher resolvent vectors `(x-t_i)^(-r-1)`. Higher exact arithmetic derivatives can change the entries, but they still do not change the **provenance of the sign**.

WP-324 tests the first canonical passage into Schoenberg translation-total-positivity geometry. The positive-energy Mangoldt source has Laplace transform `L(s)`, but its ordered translation kernel `L(x-y)` has the universal alternating sign law for every nondegenerate positive measure; reversing orientation to `L(x+y)` gives universal Hankel total positivity. The Mangoldt transform is also only defined for positive real Laplace parameter and is not itself the globally defined translation profile required by Schoenberg's theorem.

WP-325 closes the most natural nonlinear convolution-semigroup escape. Normalize a positive Laplace tilt of the pole-normalized Mangoldt prime-power source to a probability `nu_s` with transform `R_s(t)=L(s+t)/L(s)`. If `-log R_s` were Bernstein, `nu_s` would be infinitely divisible. It is not even two-divisible: the first atoms at `log 2` and `log 3`, together with the gap between them, force any hypothetical convolution square root to create mass at `2 log 3-log 2=log(9/2)`, outside the prime-power support. Equivalently `sqrt(R_s)` is not completely monotone for every `s>0`.

The matched control is equally important. `1-R_s(t)` **is** Bernstein for every probability law, because it is a compound-Poisson exponent, but that construction is universal and immediately fills mixed sums of source energies, losing prime-power localization. Thus the two canonical Bernstein routes split cleanly: the source-selective log-Laplace semigroup is forbidden by exact arithmetic support, while the available positive semigroup has universal sign provenance and expands the state space beyond the source carrier.

The next scalar theorem therefore cannot be another finite Pick determinant or finite jet inequality, the direct positive-measure Laplace translation/Hankel construction, or a generic compound-Poisson/Bernstein transform. A surviving route must use exact support/mass/multiplicative information through a **source-forced nonlinear relation whose positivity is both nonautomatic and compatible with the actual prime-power support**, or change category to genuinely matrix/operator-valued, indefinite-to-positive, infinite-domain, or direct finite--archimedean structure with its own positivity theorem.

## Separate source fingerprint from source-selective sign

Shifted-lattice support, quantized Mangoldt coefficients, tight derivative-biased laws, exact multipoint matrix entries and arbitrary fixed finite boundary derivatives can all be source-specific. The positivity of their scalar Pick-kernel matrices is not. WP-321 says weakly continuous scalar family statistics are reproducible after atomwise smoothing; WP-322 says finite exact multipoint Pick positivity is universal; WP-323 says increasing the finite jet order only enlarges the universal resolvent Gram.

WP-324 adds a different universal matched-control category. Positive source measure forces the wrong translation-determinant orientation and universal Hankel positivity after reversal. WP-325 adds a complementary nonlinear boundary: exact prime-power support is selective enough to **destroy** the desired infinite-divisibility sign structure, while the nearby Bernstein construction that always works is universal and loses that support. Source specificity can therefore appear either in the entries or in the failure of a positivity mechanism; neither is useful until a positive theorem is both source-selective and pointed in the Weil direction.

Future scalar arguments should identify the precise feature that fails all these controls: it must survive as exact arithmetic information while its sign theorem fails for a broad positive-measure class **and** remains actually true for the Mangoldt source. Numerical arithmetic detail inside a universally positive Gram, a universally sign-regular Laplace kernel, a universally Hankel-positive kernel, or a universally Bernstein compound-Poisson exponent is not enough.

## Preserve mass class, curvature, topology, determinant orientation, domain, divisibility and global coupling as distinct gates

WP-314--WP-325 expose successive independent gates: universal moving tangents, noncompact atom-mass scaling, universal normalized positivity, source-specific compact limits with matched controls, sparse/common-source grafting, all-gap smoothing, exact finite multipoint Gram universality, finite confluent-jet Gram universality, positive-Laplace translation sign regularity plus one-sided-domain failure, and now exact-support failure of log-Laplace infinite divisibility. Passing one gate does not imply the next.

A viable route must change the topology, algebraic category, nonlinear source operation, infinite-domain behavior, divisibility structure, or direct finite--archimedean coupling. Infinite jets/nodes are a genuine category change because domain, closability and completion become part of the theorem; they must not be inferred from finite-section positivity. Likewise a source-semigroup route must distinguish the arithmetic carrier from a universal compound-Poisson completion rather than treating any Bernstein exponent as source-selective. Each candidate still needs its own matched-control and sign audit.
