# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information, energy, inverse-conditioning, access-capacity and destination-relative reliability control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-054-reliability-is-priced-by-the-destination-cut-not-output-size`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 show that fixed-modulus bias energy, signed low-order processing, one common coefficient vector, low rank, low degree and apparent coordinate exclusion are not invariant endpoint restrictions. Source coordinates can reconstruct syntactically hidden phases cheaply, and exact source relations must be quotiented before a complexity claim is meaningful.

MC-338--MC-340 identify the invariant finite-source currencies. If `Y` is the complete admitted transcript and `X` the reciprocal source vector, bounded coefficient energy can produce nontrivial all-mode dephasing only when the transcript carries linear joint source information. For the punctured source law the intrinsic total-correlation surcharge is only `O(1)`, so bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`; near the matched-filter floor it requires almost the full source entropy.

MC-341 closes the obvious analog-coordinate loophole once the transcript has a source-natural Euclidean metric. MC-342 shows why benign forward source regularity is not a substitute: a scalar dyadic transcript can carry `Theta(R)` source information with bounded range and forward regularity by hiding it in exponentially small separation. MC-343 turns that precision loophole into a channel-capacity obstruction under additive Gaussian readout.

MC-344--MC-345 give the discrete capacity analogue: fixed-quality noisy coordinate access contributes at most channel capacity per actual access even under feedback, revisiting and adaptive stopping. MC-346 then separates reliability from capacity: vanishing average raw-coordinate error costs `Omega_q(R log(1/bar p))` expected accesses at fixed BSC quality. MC-347 removes fixed channel quality as an invariant and charges accumulated directional discrimination divergence instead of nominal event count.

MC-348 removes the raw-coordinate acquisition model itself. For an arbitrary complete transcript law `P_x`, put the natural neighboring-state graph on the reciprocal source support and charge each edge by the symmetrized KL divergence between `P_x` and `P_x'`. The source-averaged edge budget `mathfrak J` obeys

`mathfrak J = Omega(R log(1/bar p))`

whenever average Hamming error tends to zero, with explicit even/odd-rank constants. No transcript factorization, query syntax, finite alphabet, dimension or adaptive structure is assumed. Raw-coordinate protocols become corollaries by upper-bounding `mathfrak J` with their accumulated query divergence; noisy joint Euclidean encodings pay through source-edge Dirichlet energy.

MC-349 now makes the reliability theorem destination-relative. For a quotient `q` of the source, let `E_q` be the neighboring-state edges on which `q` changes, `kappa_q` their average cut degree, `Delta_q` their maximum cut degree, and `mathfrak J_q` the source-averaged symmetrized KL carried only by those cut edges. If the destination error is `p_q`, then

`p_q >= (kappa_q/(4 Delta_q)) exp(-mathfrak J_q/kappa_q)`,

so

`mathfrak J_q >= kappa_q [log(kappa_q/(4 Delta_q p_q))]_+`.

Thus a one-bit endpoint can still require extensive reliability when its cut crosses `Theta(R)` source directions, while a high-dimensional source may have a cheap destination if the quotient is constant along almost all neighboring directions. Output size, source dimension and full-vector reconstruction cost are not substitutes for destination-cut geometry.

For endpoint dephasing this leaves a sharply stated arithmetic problem. First identify the actual destination quotient of the reciprocal source and its cut geometry inside the admissible source graph. Then bound the complete analytic transcript's divergence on exactly those cut edges using the resources genuinely supplied by the construction. A full-vector `Omega(R log(1/bar p))` tariff is justified only when the endpoint really requires that many neighboring source directions to remain distinguishable.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, joint transcript mutual information, intrinsic source dependence, accessed source-coordinate count, adaptive query policy, per-access channel capacity, target reconstruction error, accumulated query divergence, source-edge transcript divergence, destination-cut degree/geometry, destination-cut transcript divergence, source-graph Dirichlet energy, transcript metric dimension/spread, forward source regularity, inverse distinguishability/precision, declared readout noise/SNR and source-natural coupling are different resources.

MC-338--MC-349 identify the current invariant endpoint chain: admitted observations determine joint source information; source information and coefficient energy bound achievable dephasing; a metric realization must pay distinguishable-state packing; declared noise converts hidden precision into capacity; feedback cannot increase per-access memoryless capacity; and vanishing destination error has a logarithmic reliability price on the source edges that actually cross the destination quotient. A useful arithmetic theorem must first identify that quotient and then control the cut-relative currencies required by the actual endpoint.