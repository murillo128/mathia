# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and its cost depends on anchor geometry

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-157](../../findings/FD-157-multi-parent-prime-face-coercivity-requires-cross-core-boolean-leakage.md).

For binary orientations anchored on `D`, finite-`L^q` recovery is controlled by anchored boundary exposure: `C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`. Connectivity only excludes zero boundary; stable recovery requires every admissible macroscopic flip to carry uniformly positive observed boundary mass.

FD-148--FD-153 price this for rank-aligned divisor-closed anchors. A fixed finite anchor forces large parent amplification; bounded parent distortion needs positive anchor mass. Central-rank anchors retain Gaussian-depth fluctuations, while bounded residual depth appears only as the rank anchor approaches total source mass.

FD-154 gives a qualitatively different geometry. For a finite prime set `S`, the prime-avoidance face `D_(S,T)` is divisor-closed, and every unanchored squarefree integer has an `S`-free core in the anchor at depth at most `|S|`. The direct core-to-child frame has exact cut exposure and bounded parent/child distortion for fixed `S`.

The cost appears when this coordinate face is thinned. FD-155 shows that reducing its anchored mass to `alpha` requires `s=exp(alpha^(-1+o(1)))` avoided prime coordinates and gives a double-exponential direct parent bill. FD-156 proves that this is not a bad choice of unique ancestry: every one-parent divisibility forest on the same face obeys `P/h >= 2^s-1`, with equality for the direct star. Rerouting can move the exponential price between anchor congestion and cut exposure but cannot remove it.

FD-157 identifies what multi-parent structure would actually have to buy. Write the squarefree vertex as its `S`-part times its `S`-free core. The forced Boolean packet consists of the `2^s-1` nontrivial `S`-parts above one core. Let `L` be the normalized positive edge mass that crosses from that packet to a child with a **different `S`-free core**. Then every positive multi-parent divisibility relation satisfies the exact resource inequality

`P + L >= h (2^s-1)`.

This is the correct replacement for “multi-parent may escape.” Extra parents that stay inside one core have `L=0` and inherit the full one-parent exponential law. To keep expansion fixed while reducing anchor load, a graph must leak an exponential amount of boundary mass across distinct cores. Under a uniform child-distortion bound `eta^+(m)<=K nu(m)`, this implies an exponential recipient-population requirement: cheap `P` forces `Omega(2^s/K)` outside-core children. At the FD-155 thinning scale that recipient population becomes double exponential in `alpha^(-1+o(1))`.

The reusable lesson is that **parent multiplicity is not the resource; source-fibre mixing is**. A representation can be highly connected while all edges remain inside fibres on which the difficult Boolean packet is conserved. Only edges that change the conserved core can relax the anchored bottleneck, and their total mass must be priced explicitly. This is analogous to a conductance problem with a hidden conserved label: adding edges inside components changes local degree but not the cut that matters.

This does not turn recipient count into an information lower bound. A deterministic rule can generate exponentially many children from a compact description. Nor does cross-core leakage supply the missing arithmetic orientation. A surviving Farey route still needs a source-native mechanism that produces the anchor/cross-core signs without reconstructing Möbius and a destination theorem showing that the resulting coefficient coercivity controls the nonlocal Franel--Landau quantity.

A source-valid ancestry proposal should therefore expose: anchor mass and geometry, parent load `P`, anchored expansion `h`, **cross-core leakage `L`**, residual depth, child distortion and recipient population, how those edges are generated from Farey data, and the final destination map. Calling a DAG “multi-parent” is not enough after FD-157; it must identify the conserved source fibre it actually crosses.

**Boundary.** FD-157 concerns positive divisibility-edge measures on the finite-prime avoidance face and the associated `S`-free core decomposition. It does not rule out signed observations, different anchor geometries, non-divisibility functionals, unbounded child distortion, or genuinely nonlocal Farey/Fourier mechanisms. The chain establishes coefficient-side resource laws, not RH-strength destination coercivity.
