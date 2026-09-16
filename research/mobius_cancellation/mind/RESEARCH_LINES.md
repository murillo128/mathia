# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with joint information and energy control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-048-bounded-energy-dephasing-needs-linear-joint-source-information`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 separate several apparent complexity controls. Fixed-modulus bias energy, signed low-order processing and one common coefficient vector do not close the endpoint. Arbitrary mode-dependent rows contain the exact conjugate-character matched filter. Rank, Frobenius energy, cross-mode variation and polynomial degree are distinct resources, and low degree is meaningful only after expressing the architecture in source coordinates and quotienting exact source relations. Syntactically hiding a coefficient's own phase is insufficient when the remaining variables reconstruct it cheaply.

MC-338 replaces those coordinate-dependent restrictions by an exact observation/energy tradeoff. If coefficient `i` sees an observation subspace `H_i`, let `rho_i` be the `L^2` norm of the projection of its own source phase onto that subspace and let `rho^2` be the average squared predictability. For normalized coefficient energy `E`, uniform RMS dephasing error obeys

`delta >= (1-rho sqrt(E))_+`.

MC-339 makes the predictability currency representation-invariant for binary source phases. The excess `rho_i^2-m^(-2)` is controlled exactly by HGR maximal correlation with the admitted observation, composes through Markov information channels, and is bounded by mutual information. This shows how local observation restrictions can protect a coefficient from cheap matched filtering.

MC-340 adds the missing **global transcript** gate. If `Y=(Y_1,...,Y_R)` is the complete architecture transcript and `X=(X_1,...,X_R)` the joint source vector, then

`rho^2 <= m^(-2) + (2/R)(I(X;Y)+TC(X))`.

For the punctured reciprocal source law the total-correlation surcharge is only `O(1)` nats: it tends to `0` for even rank and to `log 2` for odd rank. Consequently bounded-energy constant-factor dephasing requires `I(X;Y)=Omega(R)`. If the transcript has `K_R` states, subexponential state growth `log K_R=o(R)` forces `delta -> 1` at bounded energy. At matched-filter energy `E<=1`, near-exact dephasing requires nearly the full source entropy, and exact dephasing determines the complete source vector.

The live linear route is therefore stronger than bounding each coefficient's own local information separately. Many individually weak observations can jointly encode the source vector. A source-natural analytic architecture must control the **joint mutual information/capacity of the complete admitted transcript** and normalized coefficient energy at the same time. Low rank, low degree, variable exclusion, per-coordinate leakage or small syntactic output dimension matter only when they imply that invariant joint bound after all exact source relations are taken into account.

The next useful theorem should therefore identify the actual arithmetic transcript exposed to the coefficient family and prove one of two things: either its joint source information is `o(R)` while the energy remains bounded, which would force asymptotically full dephasing error by MC-340, or any transcript with linear information necessarily pays an analytic energy/conditioning cost large enough to prevent endpoint cancellation. Counting real coordinates is not enough: one real-valued statistic may carry full discrete source information.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, per-coordinate maximal correlation, **joint transcript mutual information**, intrinsic source dependence and source-natural coupling are different resources. MC-338--MC-340 identify the invariant endpoint combination: how much source information the architecture can jointly expose and exploit, multiplied by how much coefficient energy it can spend. Future analytic estimates should be stated in that information/energy geometry rather than in a coordinate complexity that a reparameterization or joint decoder can erase.