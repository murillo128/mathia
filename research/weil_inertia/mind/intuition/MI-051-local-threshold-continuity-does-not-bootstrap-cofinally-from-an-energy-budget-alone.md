# MI-051 — Local threshold continuity does not bootstrap cofinally from an energy budget alone

**Evidence level:** exact synthesis from [WI-357](../../findings/WI-357-null-equation-gives-threshold-continuity-on-the-ground-state-class.md) and [WI-358](../../findings/WI-358-log-energy-budget-does-not-give-cofinal-threshold-continuity.md).

WI-357 establishes the correct local topology at a prime-power activation threshold. On actual normalized null states, Suzuki's null equation bounds logarithmic energy, and bounded logarithmic energy gives an inverse-logarithmic modulus for the autocorrelations entering the finite source ledger. A single newly activated prime channel is therefore form-small even though it jumps in ambient operator norm.

WI-358 shows why this cannot be promoted to a global threshold-by-threshold argument using the energy budget alone. There are normalized tests with the allowed logarithmic-energy scale for which an already-present source autocorrelation changes by an order-one amount between consecutive thresholds. The witnesses are not null states, so they do not contradict WI-357; they show that the budget class itself has no cofinal uniform modulus strong enough to carry positivity indefinitely.

The distinction is structural. **Local continuity is state-selected; cofinal control needs additional source structure.** At one threshold the exact null equation places the relevant state in a compact enough form class. Across an unbounded sequence of thresholds, a scalar energy ceiling by itself does not keep the state family coherent.

A global first-crossing exclusion therefore has to use more than repeated continuity estimates: a positive reserve that survives the threshold sequence, source-specific cancellation from the null equation, or another invariant that couples successive ground states. Improving the generic modulus on the whole energy ball attacks a class WI-358 has already shown to be too large.

**Boundary.** WI-358 does not construct first-crossing null states and does not refute the local continuity theorem of WI-357. Its obstruction is specifically to a cofinal bootstrap based only on the stated logarithmic-energy budget; actual null-equation structure may still provide the missing coherence or reserve.