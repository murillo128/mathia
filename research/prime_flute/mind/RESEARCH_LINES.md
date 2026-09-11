# Prime-flute research lines

This file holds the current mathematical questions suggested by the durable prime-flute intuitions. It is not a roadmap, task queue, status page, or history.

## Stop using the fixed-axis Robin normalization as a supercritical low-output escape

**Linked intuition:** `MI-007-square-root-functional-calculus-closes-the-finite-seam-mass-gap`.

PF-271--PF-278 show why separated propagation initially looked promising and why the fixed-axis route nevertheless closes at the critical continuum threshold. The fully Robin-normalized fixed-row shell leakage is `asymp N^(-1)(log N)^(-3/2)`: logarithmically improved, but not supercritical by any fixed power. The fixed-axis Robin-homotopy route is closed rather than merely unresolved.

## Estimate the physical energy-normalized low/high cross form, not the unprojected cut

**Linked intuition:** `MI-008-complete-cut-transmission-needs-extension-mass-not-only-boundary-impedance`.

PF-228--PF-279 show that local corridor attenuation does not control an **unprojected** complete cut in a variable scalar reservoir. The exact Schur invariant includes endpoint-extension mass, and a positive reservoir can amplify that mass enough to erase the isolated edge gain.

PF-280 separates this matched control from the actual physical low/high leakage. For a genuine `P/H` frequency split, same-sector reservoir completion cannot worsen the symmetric-ideal class of a one-sided decoupled cross transfer: the mixed inverse block factors through contractions. The scalar PF-279 amplifier, when it remains inside one sector, is therefore not by itself a counterexample to the mixed physical-frequency commutator.

PF-281 removes the remaining raw-operator-domain artifact. The positive quadratic form canonically defines the bounded energy-normalized cross operator `T=A^(-1/2) B C^(-1/2)` even when the raw block `B` is unbounded. If `T` lies in the required symmetric ideal, then the full mixed inverse block and the reciprocal-prime commutator inherit that ideal membership. Positivity alone is insufficient: `T` can approach unit norm and the mixed inverse can remain noncompact.

The live theorem is now concrete: estimate the **complete physical energy-normalized `P/H` cross form `T`**, including finite-pant completion and neighboring-cell coupling, in the weak-trace or stronger ideal consumed by the coefficient-transfer endpoint. Reservoir extension mass remains a mandatory control for unprojected statements, but it should not be imported as an obstruction to the projected route without proving that it survives energy normalization and the physical frequency split.

## Treat branch singularity, same-sector reservoir amplification, and cross-frequency conversion as distinct failure modes

The fixed-axis source fails supercritical decay through a threshold branch. Variable same-sector reservoirs can erase an isolated unprojected seam gain. A genuine mixed low/high conversion channel can independently fail compactness even after energy normalization. A new Prime-Flute architecture must state which of these three mechanisms it controls rather than transfer conclusions from one to another.