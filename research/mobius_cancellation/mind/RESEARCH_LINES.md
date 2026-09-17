# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information, energy and inverse-conditioning control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-051-gaussian-readout-noise-converts-source-information-into-snr-cost`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 show that fixed-modulus bias energy, signed low-order processing, one common coefficient vector, low rank, low degree and apparent coordinate exclusion are not invariant endpoint restrictions. Source coordinates can reconstruct syntactically hidden phases cheaply, and exact source relations must be quotiented before a complexity claim is meaningful.

MC-338--MC-340 identify the invariant finite-source currencies. If `Y` is the complete admitted transcript and `X` the reciprocal source vector, bounded coefficient energy can produce nontrivial all-mode dephasing only when the transcript carries linear joint source information. For the punctured source law the intrinsic total-correlation surcharge is only `O(1)`, so bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`; near the matched-filter floor it requires almost the full source entropy.

MC-341 closes the obvious analog-coordinate loophole **once the transcript has a source-natural Euclidean metric**. If a deterministic transcript `T in R^d` carries the information required by MC-340, Euclidean packing forces exponentially many distinguishable transcript states and `spr(T) >= (1/2)(exp(L_R/d)-1)`.

MC-342 shows why the missing metric resource cannot be replaced by benign **forward** source regularity. On the exact even-rank punctured source cube, the scalar dyadic transcript `T_R(B)=sum 2^(-i)B_i` is injective and carries `Theta(R)` source information while its range, Hamming-to-Euclidean Lipschitz constant and every fixed positive-moment source-edge energy stay uniformly bounded. The information is hidden entirely in minimum separation `2^(-R)`: inverse Lipschitz distortion and required finite precision are exponential. Forward smoothness can therefore coexist with maximal analog capacity.

MC-343 converts that qualitative precision loophole into an exact noisy-channel obstruction. If a `d`-dimensional transcript `T` is read through additive Gaussian noise `Z=T+N`, `N~N(0,sigma^2 I)`, then

`I(X;Z) <= (d/2) log(1+V_T/(d sigma^2)) <= V_T/(2 sigma^2)`,

with the analogous diameter bound `I(X;Z) <= (d/2) log(1+D_T^2/(2d sigma^2))`. Combining this with the MC-340 information requirement forces `V_T/sigma^2 >= d(exp(2L_R/d)-1)` and the corresponding diameter-to-noise cost. Fixed transcript dimension therefore requires exponential SNR/spread; arbitrary dimension still pays at least the information-scale variance cost. Exact source recovery or exact dephasing is impossible at any positive Gaussian noise because distinct finite-source Gaussian output laws overlap.

The live arithmetic problem is narrower again. For any proposed Möbius-derived transcript with a declared positive readout-noise scale, MC-343 already prices the analog packing loophole by channel capacity. A surviving architecture must either derive enough source-dependent SNR/metric separation from genuine arithmetic structure, justify a different source-natural noise/readout model and prove its capacity, or explicitly rely on effectively noiseless/arbitrary-precision access and explain why that access is legitimate downstream. Range, forward coefficient sensitivity, forward source-gradient energy or nominal dimension alone remain irrelevant.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, joint transcript mutual information, intrinsic source dependence, transcript metric dimension/spread, forward source regularity, inverse distinguishability/precision, declared readout noise/SNR and source-natural coupling are different resources.

MC-338--MC-343 identify the current invariant endpoint chain: admitted observations determine joint source information; source information and coefficient energy bound achievable dephasing; a finite-dimensional metric realization must pay distinguishable-state packing; bounded forward regularity does not pay that bill; and once a positive Gaussian readout scale is declared, Shannon capacity turns the hidden precision directly into an SNR/spread lower bound. A useful arithmetic theorem must control these currencies for the **actual** source representation rather than choose coordinates or a noiseless readout in which the desired obstruction disappears.