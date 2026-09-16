# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Work inside the forced half-loaded source band with source-relative information and energy control

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-047-low-degree-mode-dependence-is-an-endpoint-anti-dephasing-resource`.

MC-307--MC-328 reduce the reciprocal endpoint to a character/source geometry with a quartic common-radical floor. Near saturation, almost all logarithmic source mass lies in columns of occupancy `R/2+o(R)`, where nonnegative endpoint-polynomial weights of degree `o(R)` are blind.

MC-329--MC-337 separate several apparent complexity controls. Fixed-modulus bias energy, signed low-order processing and one common coefficient vector do not close the endpoint. Arbitrary mode-dependent rows contain the exact conjugate-character matched filter. Rank, Frobenius energy, cross-mode variation and polynomial degree are distinct resources, and low degree is meaningful only after expressing the architecture in source coordinates and quotienting exact source relations. Syntactically hiding a coefficient's own phase is insufficient when the remaining variables reconstruct it cheaply.

MC-338 replaces these coordinate-dependent restrictions by an exact observation/energy tradeoff. If coefficient `i` sees an observation subspace `H_i`, let `rho_i` be the `L^2` norm of the projection of its own source phase onto that subspace and let `rho^2` be the average squared predictability. For normalized coefficient energy `E`, uniform RMS dephasing error obeys

`delta >= (1-rho sqrt(E))_+`.

Thus exact or near dephasing requires paying either large **own-source predictability** or large coefficient energy. Degree, variable exclusion and quotient structure matter only through how much of the phase they reveal and at what energy cost.

MC-339 makes the predictability currency representation-invariant for binary source phases. The excess `rho_i^2-m^{-2}` is exactly controlled by Hirschfeld--Gebelein--Rényi maximal correlation with the admitted observation, composes multiplicatively through Markov information channels, and is bounded by mutual information through Pinsker. Under bounded normalized coefficient energy, vanishing average information about each coefficient's own phase forces the dephasing error back to the full target scale.

The live linear route is therefore to identify a **source-natural information channel** for the actual arithmetic coefficients and prove simultaneously that (i) its own-phase maximal correlation/information is small enough, and (ii) the analytic coefficient family cannot compensate by spending diverging energy or conditioning. Low rank, low degree or variable exclusion are useful only when they imply those invariant quantities after all exact source relations are taken into account.

## Repair probabilistic Möbius comparators only after exact-stratum and algebraic-collapse gates

**Linked intuition:** `MI-040-probabilistic-mobius-proxies-must-survive-exact-arithmetic-consistency`.

MC-318 shows that a probabilistic Möbius route can fail before delicate asymptotics: conditioning on `Omega(n)=1` forces squarefreeness, contradicting an asserted independence, and its auxiliary sum collapses exactly to `lambda(n)M(x)`. A repaired probabilistic route needs a dependence law valid on a nondegenerate arithmetic stratum and an observable whose exact multiplicative simplification leaves information beyond `M(x)`.

## Keep the resource ledger explicit

Source loading, common-modulus analytic horizon, placement relative to energy compression, rowspace rank, total coefficient energy/conditioning, cross-mode variation, coordinate degree, own-phase access, quotient reconstruction cost, maximal correlation/mutual information and source-natural coupling are different resources. MC-338--MC-339 identify the invariant endpoint combination: **how well each coefficient can infer the phase it needs to cancel, multiplied by how much energy the coefficient family is allowed to spend**. Future analytic estimates should be stated in that same information/energy geometry rather than in a coordinate complexity that a reparameterization can erase.