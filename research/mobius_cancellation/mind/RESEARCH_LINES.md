# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information, energy, inverse-conditioning and access-capacity control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-052-bit-flip-noise-prices-coordinate-access-not-noise-alone`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 show that fixed-modulus bias energy, signed low-order processing, one common coefficient vector, low rank, low degree and apparent coordinate exclusion are not invariant endpoint restrictions. Source coordinates can reconstruct syntactically hidden phases cheaply, and exact source relations must be quotiented before a complexity claim is meaningful.

MC-338--MC-340 identify the invariant finite-source currencies. If `Y` is the complete admitted transcript and `X` the reciprocal source vector, bounded coefficient energy can produce nontrivial all-mode dephasing only when the transcript carries linear joint source information. For the punctured source law the intrinsic total-correlation surcharge is only `O(1)`, so bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`; near the matched-filter floor it requires almost the full source entropy.

MC-341 closes the obvious analog-coordinate loophole **once the transcript has a source-natural Euclidean metric**. If a deterministic transcript `T in R^d` carries the information required by MC-340, Euclidean packing forces exponentially many distinguishable transcript states and corresponding spread. MC-342 shows why benign forward source regularity is not a substitute: a scalar dyadic transcript can carry `Theta(R)` source information with bounded range and forward regularity by hiding it in exponentially small separation.

MC-343 turns that precision loophole into a channel-capacity obstruction under additive Gaussian readout. MC-344 gives the discrete analogue: if only `k` source coordinates are exposed through independent bit-flip noise with crossover `q`, then `I(X;Y)<=k c(q)`. Fixed gain therefore requires `k=Omega(R)` at fixed `q`, but exposing all `R` coordinates at any fixed `q<1/2` still leaves `Theta(R)` information. Positive noise alone is not an endpoint obstruction.

MC-345 now shows that **adaptive coordinate choice does not evade this access budget**. The controller may choose each next coordinate from the entire previous noisy transcript, revisit coordinates and stop adaptively. For a memoryless BSC each actual query contributes at most `c(q)` conditional mutual information, so

`I(X;T) <= c(q) E[tau]`.

Combining this with MC-340 forces a linear expected number of source accesses for fixed bounded-energy gain. Adaptivity can allocate the access budget but cannot create extra information through the query indices once their selection history is retained. With positive BSC noise, finite expected time cannot even give exact zero-error source recovery because every finite transcript has common support across source states.

The live arithmetic problem is consequently narrower. For any proposed Möbius-derived transcript, identify the actual source-access primitive, include every selector side channel in the admitted observation, and prove its aggregate information budget at the resolution consumed downstream. A surviving architecture may legitimately use `Theta(R)` source information or `Theta(R)` positive-capacity accesses, but then that extensive access must arise from genuine arithmetic observables and still be converted into the required coherent endpoint cancellation. Nominal noise, range, forward sensitivity, gradient energy, coordinate syntax or online selection without a capacity theorem are not enough.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, joint transcript mutual information, intrinsic source dependence, accessed source-coordinate count, adaptive query policy, per-access channel capacity, transcript metric dimension/spread, forward source regularity, inverse distinguishability/precision, declared readout noise/SNR and source-natural coupling are different resources.

MC-338--MC-345 identify the current invariant endpoint chain: admitted observations determine joint source information; source information and coefficient energy bound achievable dephasing; a finite-dimensional metric realization must pay distinguishable-state packing; bounded forward regularity does not pay that bill; declared noise converts hidden precision into a channel-capacity budget; coordinatewise noisy access prices total surviving capacity; and feedback/adaptive selection cannot increase the per-access capacity of the memoryless source channel. A useful arithmetic theorem must control these currencies for the actual source representation rather than choose coordinates or an observation policy in which the desired obstruction disappears.