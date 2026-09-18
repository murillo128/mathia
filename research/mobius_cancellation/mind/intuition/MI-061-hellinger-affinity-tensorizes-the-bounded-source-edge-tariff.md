# MI-061 — Hellinger affinity tensorizes the bounded source-edge tariff, but the generic tariff is attainable

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-bounded-energy-dephasing-forces-linear-joint-source-information.md), [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md), [MC-360](../../findings/MC-360-hellinger-product-component-edge-tariff.md), [MC-361](../../findings/MC-361-binary-entropy-sharpens-reciprocal-endpoint-information-floor.md), [MC-362](../../findings/MC-362-tv-to-hellinger-near-endpoint-transfer.md), [MC-363](../../findings/MC-363-sharp-js-hellinger-endpoint-envelope.md), [MC-364](../../findings/MC-364-product-affinity-log-depth-tariff.md), and [MC-365](../../findings/MC-365-coordinatewise-bsc-endpoint-tariff-sharpness.md). The binary-symmetric channel, Hellinger/Bhattacharyya identities and product tensorization are classical; the Mathia content is their joint specialization to the reciprocal endpoint and the resulting frontier classification.

Total variation is the natural bounded currency for a genuine common-seed architecture, while squared Hellinger distance is the natural bounded currency for a genuine latent/product architecture because affinity multiplies through conditionally independent components. MC-360 therefore prevents source sensitivity from disappearing merely by splitting a transcript into many weak pieces.

MC-363 makes the destination requirement endpoint-sharp. If `H_1=(2/m)sum_e H^2(P_x,P_x')`, matched-filter dephasing error `epsilon` forces

`liminf H_1/R >= 1-sqrt(2 epsilon-epsilon^2)`.

MC-364 exposes the stronger additive coordinate hidden behind that product statement. For source-independent latent randomness and conditionally independent components, write `lambda_(j,i)=-log(1-alpha_(j,i))` and `Lambda_i=sum_j lambda_(j,i)`. Product affinity gives

`H^2(P_x,P_x') <= 1-exp(-Lambda_i)`,

hence

`(1/R) sum_i Lambda_i >= -log beta_R`,

and near exact matched-filter dephasing the lower bound is asymptotically `(1/2)log(1/epsilon)`. The corresponding quantile bound prevents the tariff from being hidden in a small exceptional set of source directions.

MC-365 supplies the equality calibration that changes the interpretation of the whole chain. Pass each source bit independently through a binary-symmetric channel with crossover `delta`. Every one-bit source edge then has

`Aff=2sqrt(delta(1-delta))`,

`H^2=1-2sqrt(delta(1-delta))`,

and directional depth `Lambda_i=-log(2sqrt(delta(1-delta)))`. The sharp JS/Hellinger envelope is attained exactly, all surviving edges have the same cost, and the mutual-information floor is attained up to the exponentially small puncture correction. With `delta=epsilon/2`, the channel simultaneously realizes the MC-363 Hellinger scale and the MC-364 logarithmic depth scale.

The consequence is structural: **the generic endpoint tariffs are admission conditions, not generic impossibility theorems**. Their endpoint growth is real, but an abstract coordinatewise product channel can pay it at exactly the forced scale. Further architecture-free optimization of information, Hellinger or Bhattacharyya lower bounds cannot by itself create the missing Möbius contradiction.

The load-bearing theorem must now be source-side. For the actual Möbius-derived acquisition map, prove an upper bound on source-direction discrimination that excludes or quantitatively prices the BSC-like equality family: a precision/noise floor, restricted source-coordinate incidence, bounded Bhattacharyya depth, shared low-capacity statistic, or another arithmetic constraint that is genuinely independent of the destination lower bound.

**Boundary.** MC-365 does not realize the BSC as a Möbius channel and gives no estimate for `M(x)`. Source-dependent latent selection must still be charged separately, and arbitrary dependent components do not inherit product affinity. The conclusion is only that the present architecture-free tariff chain is sharp enough to be attainable; any obstruction now requires a Möbius-specific acquisition upper theorem or a different source-sensitive mechanism.