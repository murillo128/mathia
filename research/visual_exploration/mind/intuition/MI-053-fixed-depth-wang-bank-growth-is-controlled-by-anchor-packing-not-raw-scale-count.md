# MI-053 — Fixed-depth Wang bank growth is controlled by anchor packing, not raw scale count

**Evidence level:** exact finite-dimensional synthesis from [VIS-356](../../findings/VIS-356-fixed-depth-bank-growth-anchored-floor.md) and [VIS-357](../../findings/VIS-357-compact-wang-anchor-packing-collapse.md), extending the block-Vandermonde quotient geometry in VIS-354--VIS-355. Positive-semidefinite Gram monotonicity, Vandermonde conditioning and compact packing are classical; the line-specific content is the classification of the remaining compact fixed-depth escape.

At fixed tail depth `q`, appending scales cannot lower the smallest positive singular value of the full Wang moment map while one uniformly conditioned `q`-scale anchor survives. Column augmentation only adds positive-semidefinite Gram mass. Extra scales may enlarge the exact moment kernel, but after quotienting that known kernel they do not create a new conditioning gain.

Inside a fixed compact inverse-scale interval, VIS-357 makes loss of every such anchor explicit. If `delta_q(X)` is the best minimum separation of a `q`-point subset and `alpha_q(X)` the best `q`-column anchor singular value, then

`c delta_q(X)^(q(q-1)/2) <= alpha_q(X) <= C delta_q(X)`.

Hence all fixed-depth anchors degenerate exactly when `delta_q(X)->0`, equivalently when the whole bank becomes coverable at every fixed resolution by at most `q-1` shrinking clusters. There is no diffuse compact many-scale escape at the anchor level.

This does **not** yet classify the full rectangular map after cluster collapse. Growing occupancy inside shrinking clusters adds Gram mass and may compensate the bad square anchors. The remaining compact problem is therefore quantitative: price cluster widths together with occupancies/weights and coefficient normalization in the full quotient singular value. Raw scale count and qualitative pairwise collision are not independent resources.

**Boundary.** Growing tail depth, scale escape toward zero or infinity, changing coefficient topology, infinite-dimensional limits, nonlinear source operations and genuinely new signed arithmetic information remain outside this fixed-depth compact classification.