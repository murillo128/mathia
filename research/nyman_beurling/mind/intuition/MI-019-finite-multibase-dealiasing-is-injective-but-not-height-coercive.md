# MI-019 — Height coercivity requires observation complexity to grow with the height window

**Evidence level:** exact representation-level obstruction from [NB-127](../../findings/NB-127-finite-multibase-dealiasing-remains-globally-unstable-under-simultaneous-near-aliases.md), sharpened positively by [NB-128](../../findings/NB-128-natural-grid-phase-data-have-logarithmic-resolution-through-linear-height.md). The translated packets are formal zero-power controls, not asserted actual zeta-zero packets, and NB-128 is a phase-scaffold theorem rather than a Burnol-mass bound.

A fixed finite family of geometric bases can remove exact aliasing without providing stable absolute-height information. Simultaneous Diophantine recurrence gives unbounded common shifts for which every fixed base phase returns arbitrarily close, while the Burnol target mass of the translated formal packet tends to zero. Thus finite multibase injectivity is not a quantitative inverse modulus.

NB-128 identifies the missing scaling explicitly. Once the observation family grows to the full natural prefix `2<=n<=R`, the phase map satisfies

`d_R(S,T) >= min(c_*, c_1 floor(log_2 R)|T-S|)` for `|T-S|<=R-1`.

So a fixed phase accuracy below `c_*` determines common vertical translation to `O(1/log R)` throughout a height window of size `Theta(R)`. The proof uses the largest dyadic point for tiny shifts and an adjacent integer pair near `|T-S|` for larger shifts. The observation set grows precisely enough to supply a local frequency ruler at the candidate height scale.

This converts the old qualitative prescription “use growing sampling complexity” into a concrete resource law: **linear height coverage costs a natural prefix of comparable size, while local ordinate resolution improves only logarithmically**. Farther simultaneous recurrence is not excluded, so this is a mesoscopic modulus rather than global de-aliasing.

The remaining destination problem is amplitude-weighted. Under common translation, `P_(F_T)(n)=n^(iT)P_F(n)`. A phase coordinate can separate strongly while `P_F(n)` is tiny at that witnessing cell. A source-faithful Nyman theorem must therefore combine the phase modulus with a nonconcentration/Dirichlet-energy statement forcing enough primitive mass onto phase-visible natural cells.

**Boundary.** NB-128 does not prove a target-angle or Burnol-mass lower bound, does not forbid far aliases beyond the linear window, and does not assert that actual zeta zeros occur in translated packets. The durable distinction is now three-way: fixed-data injectivity, scale-growing phase stability, and amplitude-weighted destination visibility.
