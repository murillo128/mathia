---
id: RGR-WP-SELECTOR-PAIRING-001
type: research-graph-relation
scope: weil_positivity
relation: positive-selector-pairing-collapse
derived: true
---

# Positive selector readouts do not supply the Weil pairing

[[research/weil_positivity/findings/WP-043-cycle-laplacian-shell-logdet-recovers-mangoldt-but-spectral-positivity-is-the-wrong-pairing|WP-043]] shows that the compatible positive cycle geometry really can recover `Lambda(n)` through primitive-shell log-determinants and a nonnegative scalar spectral multiplier. The obstruction is not loss of the finite selector itself: scalar spectral positivity is diagonal in exact-order Fourier shells, while the finite Weil birth matrix lives in pointwise cross-shell couplings.

Two sign-preserving radial reductions then test whether positivity can isolate that birth term without changing category:

- [[research/weil_positivity/findings/WP-044-radial-gram-contrasts-cancel-boundary-weil-birth-term|WP-044]] shows that the universal collision divergence and the Weil birth operator occupy the same radial common-mode channel, so any fixed positive radial contrast that removes the former removes the latter as well.
- [[research/weil_positivity/findings/WP-045-radial-schur-elimination-loses-boundary-weil-birth-term|WP-045]] shows that ordinary positive Schur/Feshbach elimination has the same fate: the leading Schur limit is universal and shell-diagonal, while the arithmetic birth operator survives only in a vanishing correction.

The source-backed mechanism is:

```text
intrinsic positive finite operator can recover Mangoldt data
    -> scalar spectral pairing is nevertheless the wrong pairing
positive radial differencing
    -> removes universal mode and arithmetic birth together
positive shell-blind Schur elimination
    -> retains positivity but loses the birth term at leading order
```

This narrows, but does not close, the coupled selector/completion territory. The current Weil-positivity synthesis leaves shell-dependent, singular, nonseparable, determinant/intersection, and genuinely finite-plus-archimedean operations open when they come with an independent sign theorem.