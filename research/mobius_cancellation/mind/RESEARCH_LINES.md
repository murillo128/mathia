# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information, energy and inverse-conditioning control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-052-bit-flip-noise-prices-coordinate-access-not-noise-alone`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 show that fixed-modulus bias energy, signed low-order processing, one common coefficient vector, low rank, low degree and apparent coordinate exclusion are not invariant endpoint restrictions. Source coordinates can reconstruct syntactically hidden phases cheaply, and exact source relations must be quotiented before a complexity claim is meaningful.

MC-338--MC-340 identify the invariant finite-source currencies. If `Y` is the complete admitted transcript and `X` the reciprocal source vector, bounded coefficient energy can produce nontrivial all-mode dephasing only when the transcript carries linear joint source information. For the punctured source law the intrinsic total-correlation surcharge is only `O(1)`, so bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`; near the matched-filter floor it requires almost the full source entropy.

MC-341 closes the obvious analog-coordinate loophole **once the transcript has a source-natural Euclidean metric**. If a deterministic transcript `T in R^d` carries the information required by MC-340, Euclidean packing forces exponentially many distinguishable transcript states and `spr(T) >= (1/2)(exp(L_R/d)-1)`.

MC-342 shows why the missing metric resource cannot be replaced by benign **forward** source regularity. On the exact even-rank punctured source cube, the scalar dyadic transcript `T_R(B)=sum 2^(-i)B_i` is injective and carries `Theta(R)` source information while its range, Hamming-to-Euclidean Lipschitz constant and every fixed positive-moment source-edge energy stay uniformly bounded. The information is hidden entirely in minimum separation `2^(-R)`: inverse Lipschitz distortion and required finite precision are exponential. Forward smoothness can therefore coexist with maximal analog capacity.

MC-343 converts that qualitative precision loophole into an exact noisy-channel obstruction. If a `d`-dimensional transcript `T` is read through additive Gaussian noise `Z=T+N`, `N~N(0,sigma^2 I)`, then

`I(X;Z) <= (d/2) log(1+V_T/(d sigma^2)) <= V_T/(2 sigma^2)`,

with the analogous diameter bound `I(X;Z) <= (d/2) log(1+D_T^2/(2d sigma^2))`. Combining this with the MC-340 information requirement forces explicit SNR/spread cost, exponential in `R` at fixed dimension.

MC-344 sharpens what readout noise does and does not buy. If only `k` source coordinates are observed through independent bit-flip noise with crossover `q`, then data processing gives

`I(X;Y) <= k c(q)`, with `c(q)=log 2-h(q)` in natural units.

Combining this with the MC-340 dephasing requirement forces a linear accessed-coordinate fraction for any fixed nontrivial bounded-energy gain. But when all `R` coordinates are exposed at any fixed `q<1/2`, the noisy readout still carries `R c(q)-o(R)=Theta(R)` information under the punctured source law. **Positive fixed noise is therefore not itself an endpoint obstruction.** The invariant resource is aggregate source-access capacity: sublinear coordinate access, nearly randomizing noise, low-dimensional SNR limits, or dependence that genuinely drives total channel capacity to `o(R)` can obstruct dephasing; an extensive positive-capacity channel cannot.

The live arithmetic problem is consequently narrower. For any proposed Möbius-derived transcript, identify the actual source-access channel and prove its aggregate information budget at the resolution consumed downstream. A surviving architecture may legitimately use `Theta(R)` source information, but then that extensive access must arise from genuine arithmetic observables and still be converted into the required coherent endpoint cancellation. Nominal noise, range, forward sensitivity, gradient energy or coordinate count without a capacity theorem are not enough.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, joint transcript mutual information, intrinsic source dependence, accessed source-coordinate count, per-coordinate channel capacity, transcript metric dimension/spread, forward source regularity, inverse distinguishability/precision, declared readout noise/SNR and source-natural coupling are different resources.

MC-338--MC-344 identify the current invariant endpoint chain: admitted observations determine joint source information; source information and coefficient energy bound achievable dephasing; a finite-dimensional metric realization must pay distinguishable-state packing; bounded forward regularity does not pay that bill; declared noise converts hidden precision into a channel-capacity budget; and coordinatewise noisy access shows that the decisive quantity is **total surviving capacity**, not noise presence by itself. A useful arithmetic theorem must control these currencies for the actual source representation rather than choose coordinates or a readout model in which the desired obstruction disappears.