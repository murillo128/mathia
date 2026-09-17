# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information, energy, inverse-conditioning, access-capacity and reliability control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-053-vanishing-raw-bit-error-costs-r-log-inverse-error-accesses`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 show that fixed-modulus bias energy, signed low-order processing, one common coefficient vector, low rank, low degree and apparent coordinate exclusion are not invariant endpoint restrictions. Source coordinates can reconstruct syntactically hidden phases cheaply, and exact source relations must be quotiented before a complexity claim is meaningful.

MC-338--MC-340 identify the invariant finite-source currencies. If `Y` is the complete admitted transcript and `X` the reciprocal source vector, bounded coefficient energy can produce nontrivial all-mode dephasing only when the transcript carries linear joint source information. For the punctured source law the intrinsic total-correlation surcharge is only `O(1)`, so bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`; near the matched-filter floor it requires almost the full source entropy.

MC-341 closes the obvious analog-coordinate loophole once the transcript has a source-natural Euclidean metric. MC-342 shows why benign forward source regularity is not a substitute: a scalar dyadic transcript can carry `Theta(R)` source information with bounded range and forward regularity by hiding it in exponentially small separation. MC-343 turns that precision loophole into a channel-capacity obstruction under additive Gaussian readout.

MC-344 gives the discrete capacity analogue: if only `k` source coordinates are exposed through independent bit-flip noise with crossover `q`, then `I(X;Y)<=k c(q)`. MC-345 shows that adaptive coordinate choice, revisiting and adaptive stopping do not evade the same per-access budget:

`I(X;T) <= c(q) E[tau]`.

This closes the fixed-quality capacity question: bounded-energy constant-factor gain requires `Omega(R)` expected accesses at fixed noise, but positive noise by itself does not prohibit such a gain.

MC-346 separates **reliability** from capacity. If the final decoder must recover the raw source coordinates with average bit error `bar p`, pairwise change-of-measure across cube edges gives

`E[tau] >= const * (R/D_q) [log(const/bar p)]_+`,

where `D_q` is the one-query BSC divergence scale. At fixed `q`, driving `bar p->0` therefore costs `Omega_q(R log(1/bar p))` expected raw accesses; polynomially small error costs `Omega(R log R)`, and exact zero error requires infinite expected access. Repetition with majority decoding matches this order up to constants.

MC-347 removes the fixed-channel artifact. If the adaptive controller can choose different raw-coordinate experiments at different times and histories, raw query count is no longer invariant: one very accurate experiment may replace many weak ones. The source-natural reliability currency is the accumulated directional discrimination divergence

`mathfrak D = E sum_(t<=tau) D(K_t(.|X_(J_t)) || K_t(.|-X_(J_t)))`.

For the reciprocal source law, vanishing average Hamming error still forces

`mathfrak D = Omega(R log(1/bar p))`.

The fixed BSC theorem is exactly the special case `mathfrak D=D_q E[tau]`. Thus variable fidelity can trade event count against per-event quality, but it cannot erase the total pairwise discrimination evidence required by the destination.

For endpoint dephasing this creates two nested regimes. A fixed nontrivial gain is governed by linear joint information/capacity. Approaching the matched-filter floor with vanishing coordinate error requires a logarithmic reliability tariff, and under variable-quality raw access that tariff must be paid in accumulated discrimination KL rather than nominal query count. An architecture that claims arbitrarily accurate source alignment must state the actual acquisition primitive and price the resolution consumed downstream.

The live arithmetic problem is consequently narrower. For any proposed Möbius-derived transcript, identify the actual source-access primitive, include every selector side channel in the admitted observation, and prove both its aggregate information budget and, when the destination requires vanishing reconstruction error, its reliability budget at the resolution consumed downstream. If measurement quality varies, price the total discrimination divergence; if observations code several source coordinates jointly, derive the corresponding experiment geometry rather than importing the raw-coordinate theorem. Nominal noise, range, forward sensitivity, gradient energy, coordinate syntax, access count or online selection without such a theorem are not enough.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, joint transcript mutual information, intrinsic source dependence, accessed source-coordinate count, adaptive query policy, per-access channel capacity, target reconstruction error, reliability divergence, accumulated discrimination divergence, transcript metric dimension/spread, forward source regularity, inverse distinguishability/precision, declared readout noise/SNR and source-natural coupling are different resources.

MC-338--MC-347 identify the current invariant endpoint chain: admitted observations determine joint source information; source information and coefficient energy bound achievable dephasing; a metric realization must pay distinguishable-state packing; declared noise converts hidden precision into capacity; feedback cannot increase per-access memoryless capacity; vanishing raw-coordinate error has an additional logarithmic reliability price; and changing measurement fidelity only converts query count into accumulated pairwise discrimination divergence. A useful arithmetic theorem must control the currencies required by the actual destination rather than choose an observation policy in which the obstruction disappears.