# MI-062 — Own-phase revealment is the exact acquisition currency for adaptive coordinate-query dephasing

**Evidence level:** exact synthesis from [MC-338](../../findings/MC-338-information-energy-obstruction-for-reciprocal-source-dephasing.md), [MC-365](../../findings/MC-365-coordinatewise-bsc-endpoint-tariff-sharpness.md), and [MC-366](../../findings/MC-366-adaptive-coordinate-query-own-phase-revealment-tariff.md). Decision-tree revealment is classical; the Mathia content is the exact punctured-cube predictor bound and its composition with the reciprocal endpoint energy obstruction. No estimate for `M(x)` follows.

The generic information/Hellinger/Bhattacharyya tariffs become non-obstructive once MC-365 supplies a coordinatewise BSC that pays all of them at the forced endpoint scale. The source-side question is therefore not whether a transcript contains a large abstract amount of information, but **which physical source coordinate it had to expose in order to obtain that information**.

For the even-rank reciprocal source, `X` is uniform on the punctured cube `{+/-1}^R \ {(1,...,1)}` and `m=2^R-1`. Fix a cell `i`. Let `Y_i` be the complete transcript of any randomized adaptive noiseless coordinate-query algorithm whose internal randomness is source-independent and which has no other source side channel. If `Q_i` is the event that the algorithm ever reads `X_i` and `p_i=P(Q_i)`, then MC-366 proves

`rho_i^2 := E|E[X_i|Y_i]|^2 <= p_i + 1/m`.

The `1/m` term is exact, not a proof loss. Conditional on all other coordinates, `X_i` is unbiased except on the unique all-other-plus state, where the deleted all-plus source word forces `X_i=-1`. On the event that `i` is never queried, adaptivity and stopping can only coarsen information contained in the other coordinates and source-independent randomness, so they cannot create more squared predictor norm than this puncture leakage.

Averaging over cells gives `rho^2<=min(1,pbar+1/m)`. Composing with the MC-338 dephasing-energy inequality yields, for normalized coefficient energy `E(W)<=C`,

`delta(W) >= (1-sqrt(C)*sqrt(pbar+1/m))_+`.

Hence any fixed improvement over trivial dephasing at bounded energy requires positive-density own-coordinate revealment. At the matched-filter floor `C=1`, exact dephasing requires

`pbar >= 1-1/(2^R-1)`.

This rate is attained: query all other coordinates first, infer `X_i` only on the unique puncture atom, and otherwise query `i`. Thus the theorem does not merely lower-bound a generic complexity surrogate; it identifies the exact direct-access resource within the coordinate-query architecture.

The BSC equality family from MC-365 sits on the expensive side of this boundary rather than defeating it. A BSC readout takes `X_i` itself as input before adding noise, so its revealment is `p_i=1`. The generic tariff could be paid because the abstract channel was allowed essentially full own-source access. MC-366 converts that hidden access into an explicit source-side coordinate.

The reusable lesson is that **source acquisition must be priced by provenance when generic information is attainable**. For coordinate-query constructions, the decisive quantity is not total query count or transcript dimension but the probability of directly exposing the particular phase that the destination coefficient must cancel. Other-coordinate computation is unrestricted in the theorem and still cannot bypass the tariff beyond the single puncture atom.

The next arithmetic gate is concrete: for a proposed Möbius-derived coefficient/transcript attached to source cell `i`, identify every path by which `X_i` can enter before scalarization and prove a quantitative upper bound on its average own-phase revealment. A bound `pbar=o(1)` would contradict bounded-energy constant dephasing immediately. If the construction uses parity queries, arbitrary linear measurements, joint functions of many source cells, source-dependent latent choices or hidden side information, then own-coordinate revealment is no longer the right complete currency; that richer architecture needs an analogous source-specific predictor/revealment theorem rather than another architecture-free divergence bound.

**Boundary.** Even rank is load-bearing: at odd rank the reciprocal source relation lets the other phases determine `X_i`. The theorem prices noiseless coordinate queries with source-independent randomness and no additional side channel; it does not cover arbitrary joint measurements. It is an endpoint admission theorem, not a Möbius cancellation estimate, until a concrete arithmetic transcript is proved to fit the acquisition model with subcritical revealment.