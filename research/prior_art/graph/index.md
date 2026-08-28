---
id: RG-prior-art
type: research-graph
scope: prior_art
source_root: experiments/riemann_corpus
status: partial
derived: true
---

# Prior-art research graph

This first curator pass exposes **research findings that explicitly redirect into known territory**. It does not invent mappings into the #42/#46 corpus when the finding note does not persist a stable corpus-object ID.

<!-- graph:start -->
## Explicit prior-art / universality redirects from live research

### Prime Circle
- [[research/prime_circle/findings/PC-006-critical-gcd-kernel-and-potential-theory-downgrade-PC005]]
- [[research/prime_circle/findings/PC-007-cumulative-new-vertices-are-farey-rh-geometry-is-classical]]
- [[research/prime_circle/findings/PC-008-single-polygon-riesz-and-cycle-spectral-zeta-are-known-rh-reformulations]]
- [[research/prime_circle/findings/PC-010-abstract-refinement-dynamics-is-the-bost-connes-cyclotomic-tower]]
- [[research/prime_circle/findings/PC-011-common-vertex-chord-correlations-are-dedekind-vasyunin-sums]]

### Prime Flute
- [[research/prime_flute/findings/PF-031-sojourn-gap-ratio-is-the-standard-shear-coordinate]]
- [[research/prime_flute/findings/PF-044-one-gap-tangent-is-gamma2-and-zeta-scattering-is-universal]]
- [[research/prime_flute/findings/PF-067-generalized-cusp-scattering-already-solves-the-full-inverse-tangent-problem]]
- [[research/prime_flute/findings/PF-088-quarter-threshold-is-one-dimensional-not-prime-specific]]
- [[research/prime_flute/findings/PF-097-finite-prime-tangents-are-moduli-complete-and-primality-blind]]

### Prime Lattice
- [[research/prime_lattice/findings/PL-004-prime-exponent-gas-prior-art]]
- [[research/prime_lattice/findings/PL-005-bagchi-prime-flow-recurrence-rh]]
- [[research/prime_lattice/findings/PL-006-random-bohr-boundary-gmc]]

## Missing edge data — intentionally not guessed

The broad #42/#46 corpus exists, but these research findings generally cite literature by theorem/source rather than by the stable IDs of `full_corpus_v2/mixed_manifest.json` objects. Therefore this pass stops before claiming exact `finding -> corpus object` edges.

To materialize those exact edges safely, the next curator pass needs one of:

1. existing stable corpus-object IDs already recoverable from source/title metadata in `mixed_manifest.json`; or
2. an explicit mapping persisted by the research watch when a prior-art audit is performed.

Until then, the nodes above are valid **prior-art redirects**, but not claimed exact links to a particular #42 interpretation/synthesis object.
<!-- graph:end -->
