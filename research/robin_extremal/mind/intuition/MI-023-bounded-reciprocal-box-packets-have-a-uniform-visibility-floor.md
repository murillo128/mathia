# MI-023 — Bounded reciprocal-box packets have a uniform fixed-relative visibility floor

**Evidence level:** exact finite-packet compactness/visibility theorem from [RE-134](../../findings/RE-134-bounded-reciprocal-box-packets-have-a-fixed-relative-visibility-floor.md)

For the attained finite-edge Robin/CA packet, fix a relative observation window, a bounded scaled reciprocal box around a target subedge zero, and a uniform bound `B` on the number of positive-ordinate coordinates in that box. RE-134 proves that the real packet contributed by those coordinates cannot hide uniformly relative to the target coefficient: there is a constant `c_0>0`, depending only on the fixed box/window/strip parameters, such that

`sup_((1-kappa)U<=u<=U) |S_(C_U,K)(u)| >= c_0 |a_(rho_0,K)(U)|`.

The mechanism is compactness rather than zero density. After reciprocal scaling and demodulation, a bounded packet becomes a bounded-term exponential polynomial with exponents in a compact box and coefficients converging uniformly to the same positive orientation. Such a family has a uniform `L^2` floor; rapid target-carrier averaging transfers that floor to the actual real packet.

This turns local hiding into a concentration--compactness alternative. If the full normalized packet is `o(M_K(U))` on a fixed-relative window, then cancellation cannot remain inside a bounded-complexity fixed reciprocal box. It must escape through **growing local cardinality**, through order-one cancelling mass outside every such fixed box, or through both. If the exterior contribution is reciprocal-scale tight, hiding forces the occupancy of a fixed box to diverge.

The source-specific target is therefore sharper than “prove more zero sparsity.” A closure theorem could combine a bounded-occupancy statement for actual near-edge zeta zeros with a tightness statement preventing order-`M_K(U)` cancelling mass from migrating to larger reciprocal radii. Either ingredient alone is insufficient; together they contradict macroscopic hiding.

**Boundary.** This theorem is independent of whether the current RE-133 matched control survives its open adversarial review. It does not assert that actual zeta zeros satisfy bounded reciprocal-box occupancy or tightness, and it gives no quantitative floor when the cardinality bound or scaled box radius is allowed to grow. The nonattained edge and `Theta=1` remain separate.