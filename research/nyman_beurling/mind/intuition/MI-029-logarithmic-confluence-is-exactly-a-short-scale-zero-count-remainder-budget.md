# MI-029 — Logarithmic confluence is exactly a short-scale zero-count remainder budget

**Evidence level:** exact source/geometry splice from [NB-142](../../findings/NB-142-logarithmic-confluence-cells-force-order-log-zero-count-remainder-jumps.md), built on the target-poor cell theorem [NB-140](../../findings/NB-140-complex-confluent-cells-are-target-poor-without-gap-control.md) and the global-density matched-control boundary [NB-141](../../findings/NB-141-selberg-density-makes-confluence-cells-rare-but-not-impossible.md).

NB-140 shows that a simple packet of rank `d_G~c log G` inside a sufficiently small two-dimensional polynomial cell can have vanishing normalized Nyman-target projection. NB-141 shows that Selberg zero density makes such cells rare in height but cannot exclude a sparse infinite sequence.

NB-142 identifies exactly what an actual exceptional sequence would consume. Write

`N(T)=M(T)+R(T)`,

with `M(T)` the smooth Riemann--von Mangoldt main term. On an interval of polynomial length `G^-B`, the main-term increment is `O(G^-B log G)=o(1)`, so the local zero count is the positive increment of `R` up to `o(1)`. A right-half confluence cell containing `c log G` zeros contributes at least `2c log G` zeros after functional-equation reflection and therefore forces an order-`log G` upward jump of `R`, equivalently of the classical argument function `S(T)`.

Consequently the exact source law needed to kill the current matched packet is not another global density exponent. It is the local modulus

`Omega_B(G)=sup_(v-u<=O(G^-B)) (R(v)-R(u)) = o(log G)`

on the polynomial scales used by NB-140. The stronger global condition `R(T)=o(log T)` is sufficient. Via Backlund/Cramér, Lindelöf supplies such a sublogarithmic bound and therefore excludes this particular logarithmic-rank confluence mechanism; RH is not needed merely for that exclusion.

The reusable distinction is **population rarity versus worst-cell remainder oscillation**. Zero density controls how often a crowded right-half cell can occur. The target obstruction needs to know whether even one logarithmic-rank cell can occur along an infinite sequence. At polynomial window size, that worst-cell question is literally a question about positive short increments of the zero-count remainder.

This sharpens the live source frontier. Either prove the sublogarithmic short-increment law for actual zeta zeros at the relevant polynomial scales, or bypass occupancy entirely by proving that an actually crowded cell is target-bearing despite the general confluent matched controls. Improving average density or minimum-gap information does not address the same resource.

**Boundary.** NB-142 does not prove `Omega_B(G)=o(log G)` unconditionally and does not claim equivalence with Lindelöf. Lindelöf is only a sufficient classical benchmark. The target-poor construction still concerns the NB-140 simple-state packet; excluding that packet does not show that every smaller or differently organized zero packet is target-bearing.