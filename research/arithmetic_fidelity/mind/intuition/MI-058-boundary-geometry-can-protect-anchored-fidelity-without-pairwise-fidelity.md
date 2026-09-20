# MI-058 — Boundary geometry can protect anchored fidelity without pairwise fidelity

**Evidence level:** exact source-geometry synthesis from [AF-462](../../findings/AF-462-finite-support-simplex-boundaries-separate-anchored-from-pairwise-hilbert-fidelity.md), interpreted against the paired-cube obstruction of AF-459--AF-461. This is a generic simplex-boundary statement, not an arithmetic-source theorem.

At a probability law `mu_0` with finite support `S`, the normalized directions reachable from that anchor are not the unit sphere of a large linear tangent space. Positivity forces every negative coordinate of a reachable direction to remain inside `S`, while positive mass may spread over arbitrarily many fresh coordinates. The resulting carrier has a fixed negative-coordinate budget `s=|S|`.

That one-sided constraint is strong enough to defeat the paired-cube completion mechanism. If `D_k` denotes the AF-459 average cube-completion defect, AF-462 proves

`D_k >= (1-s/k)_+`.

So the carrier stays macroscopically far from large paired sign cubes even though the ambient alphabet is infinite. This is a genuine source-side escape from the regular finite-codimension and regular smooth-fiber obstructions of AF-460--AF-461.

But the escape is **anchored, not pairwise**. For the canonical one-hot Hilbert embedding, displacement from the distinguished finite-support law has exact positive TV gain `1/sqrt(s)`. Inside every neighborhood of that law, however, two admissible sources can move the same depleted anchor mass onto two large disjoint fresh supports; their `ell^1` distance stays fixed while their Hilbert distance tends to zero. The pairwise local lower gain is therefore zero.

The reusable distinction is that **one-sided provenance can preserve distance from a distinguished source without metrizing the whole local source class**. A boundary theorem must state whether the downstream task is anchored discrimination or arbitrary pairwise recovery. Showing that a carrier is cube-poor removes one collapse certificate, but does not by itself supply pairwise stability.

**Boundary.** Finite support is essential to the fixed negative-coordinate budget used by AF-462, and the sharp anchored modulus is for the canonical one-hot Hilbert embedding. No arithmetic conclusion follows until the physical source identifies a distinguished boundary law and proves that its relevant perturbations obey this one-sided provenance geometry. If arbitrary nearby source pairs must be distinguished, positivity plus finite support at the anchor is insufficient.