# Adversarial review — NB-116

**Finding:** `NB-116-selberg-density-upgrades-the-high-zero-burnol-tail-to-inverse-height.md`

**Review conclusion:** `PASS — NO OPEN MATERIAL ISSUES`.

## Correctness

The core reduction is sound. For right-half zeros counted with multiplicity,

\[
A(T)=\sum_{0<\gamma\le T,\,\beta>1/2}(\beta-1/2)
=\int_0^{1/2}N_>(1/2+u,T)\,du
\]

is an exact layer-cake identity. Applying Selberg's near-critical density estimate on the fixed interval `u in [0,1/4]` gives `O(T)`, while monotonicity and the estimate at `sigma=3/4` make the remaining fixed interval `o(T)`. The dyadic summation of `2(beta-1/2)/gamma^2` is then `O(1/G)`. Conjugation handles negative ordinates. The Burnol product comparison `1-e^{-S}<=tau<=S` and the substitution into the exact `NB-115` threshold are algebraically correct.

The finding correctly avoids using raw zero count where horizontal displacement is the actual observable. It also correctly states that the result is a necessary finite-section scale, not a contradiction or an RH proof.

## Source and citation integrity

The load-bearing external theorem is Selberg's zero-density estimate near the critical line. Simonič, J. Math. Anal. Appl. 491 (2020), 124303, DOI `10.1016/j.jmaa.2020.124303`, explicitly records Selberg's bound and develops an explicit version. The proof only requires uniformity on the fixed strip `[1/2,3/4]`, so it does not depend on a delicate endpoint near `sigma=1`. Burnol's product/projection formula is already anchored in `SOURCES.md`.

A new `SOURCES.md` anchor for Simonič is therefore appropriate and sufficient. No unanchored specialized theorem remains load-bearing.

## Novelty and prior-art boundary

The zero-density estimate and Burnol formula are classical and are not claimed as new. The finding's line-local content is explicitly limited to integrating the horizontal zero density in the coordinate already present in the Burnol defect, deriving the `O(1/G)` global right-half target tail, and feeding that sharper source budget into `NB-115`.

A targeted search did not identify a Nyman--Beurling paper making this exact synthesis. Even if the weighted-zero estimate `A(T)=O(T)` exists elsewhere as a routine corollary, the finding remains source-faithful because it claims a derived line-local reduction rather than priority for the zero-density corollary itself.

## Matched controls and overclaim audit

The matched-control discussion is valid. Raw Riemann--von Mangoldt supply alone allows an abstract `Theta(G log G)` packet at fixed horizontal displacement and therefore permits the older `Theta(log G/G)` target scale. Selberg density excludes that profile. Conversely, `Theta(G log G)` abstract centers at displacement `Theta(1/log G)` can respect the Selberg envelope up to constants and produce `Theta(1/G)` Burnol mass, so no `o(1/G)` conclusion follows from this density input alone.

The statement does not claim there are only `O(T)` off-critical zeros; it correctly distinguishes zero count from the weighted horizontal first moment. It also does not infer a lower bound on cell-compression retention, only that order-one finite target access requires target-bearing modes below the stated scale.

## Verification and issue log

- **Uniformity concern:** closed. The proof was deliberately written to use only a fixed compact strip `[1/2,3/4]`, covered by the cited Selberg-type estimate.
- **Endpoint/multiplicity concern:** closed. Strict `beta>sigma` versus equality affects a measure-zero set in the layer-cake integral, and multiplicities are retained throughout.
- **Infinite-product concern:** closed. The finite-packet `O(1/G)` bound is monotone and summable; exhaustion defines the full tail and `1-e^{-S}<=tau<=S` passes to the limit.
- **Finite-section overclaim concern:** closed. Equation `(5)` is stated only as the necessary spectral consequence supplied by `NB-115`.

No material issue remains.