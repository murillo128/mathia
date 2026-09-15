---
id: RG-weil-positivity-scalar-julia-derivative-biased-laws
type: research-graph-relation
scope: weil_positivity
derived: true
---

# Scalar Julia reduction leaves derivative-biased laws

[[research/weil_positivity/graph/weil-positivity|Weil Positivity research graph]]

## Persisted classification

[[research/weil_positivity/findings/WP-316-scalar-julia-reduction-erases-every-asymptotically-isolated-mangoldt-pole|WP-316]] shows that a focal pole dominating the positive boundary derivative gives only a removable real constant after the declared normalization. Nonconstant scalar tangents therefore require an order-one collective background.

[[research/weil_positivity/findings/WP-317-finite-multipole-julia-reduction-is-interlacing-degree-reduction|WP-317]] classifies finite pure positive atomic input: one normalized regular reduction replaces `N` atoms with `N-1` interlacing positive atoms. Finite repetition terminates in a real constant. This is generic rational Herglotz geometry, not a prime-specific sign.

[[research/weil_positivity/findings/WP-318-scalar-julia-tangents-are-boolean-self-energies-of-derivative-biased-measures|WP-318]] explicitly unifies those cases with infinite pure-measure input. At a support-free regular node `t`, with `d=f'(t)` finite and positive, the probability law is `d nu_t(x)=d^(-1)(t-x)^(-2)d mu(x)`. The normalized response is exactly `d(t-K_nu_t(z))`. Every probability law supported away from the node has a positive Herglotz matched control realizing it. The sign is therefore universal even with infinitely many atoms.

## Classical mechanisms and surviving boundary

The persisted dependency on [[research/prior_art/incremental/PA-julia-nevanlinna-boundary-reduction|Julia–Nevanlinna boundary reduction]] is distinct from WP-318's identification with [[research/prior_art/incremental/PA-boolean-convolution-self-energy|Boolean self-energy]]. Neither requires a new arithmetic positivity theorem. The canonical findings link those prior-art identities directly in existing prose; their mutual finding references in inline code remain unchanged, so this note supplies a mediated mechanism view rather than claiming new direct finding-to-finding links.

[[research/weil_positivity/mind/intuition/MI-031-scalar-julia-positivity-is-universal-boolean-self-energy-arithmetic-survives-only-in-the-derivative-biased-law-and-its-coupling|MI-031]] preserves the remaining source-specific question: prove something special about the Mangoldt derivative-biased laws and independently obtain the finite–archimedean coupling. Positivity of the scalar transform alone supplies neither task.

The closure concerns the pure-measure scalar class at regular nodes with finite nonzero derivative. It does not classify an order-one affine Herglotz term, matrix/operator-valued reduction, generalized resolvents or nonseparable finite–archimedean constructions. It is not a refutation of Weil positivity or RH.
