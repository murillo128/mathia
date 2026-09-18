# MI-040 — Wang's pointwise upper ceiling is a localization coherence budget

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md), [VIS-299](../../findings/VIS-299-wang-pointwise-moving-ceiling-h-over-log-cubed.md), and [VIS-300](../../findings/VIS-300-wang-localization-cross-coherence.md), using Wang's displayed localization identities and bounds as audited there.

VIS-298 removes the lower moving-source crossover by exact gamma recentering but states the pointwise asymptotic under one fixed exponent ceiling `x<=T^lambda`, `lambda<theta`, with `H=T^theta`. VIS-299 shows that the fixed gap is not the true proof-level resource: re-running Wang's localization argument yields the same asymptotic whenever

`x log^3 T / H -> 0`.

VIS-300 then decomposes the first unresolved layer. Let `A_I` be the interval-restricted field and `R_I=A-A_I` the omitted-zero tail. The exact localization-energy identity separates two pure leakage energies from one bilinear term. Both leakage energies are `O(x log^2 T)`, so at `x=O(H/log^3 T)` they are already `o(H)`. The only term that can still live at absolute `H` scale is

`C_I(x)=int_I A_I(x,t) overline(R_I(x,t)) dt`.

The extra logarithm in Wang's `O(x log^3 T)` estimate enters when this cross term is bounded by absolute values near the interval endpoints. Thus the apparent upper ceiling is not an energy-size wall for the omitted tail. It is a **coherence problem between the inside field and the outside-zero tail**.

The reusable lesson has two levels. First, when a theorem is stated uniformly on a fixed parameter family, distinguish the stated family from the quantitative dependence visible in its proof before promoting a parameter boundary to structure. Second, when a big-O bound reaches the target scale, decompose it before trying to improve all constituents: pure error energies may already be negligible while a single cross term carries the entire loss.

This complements MI-039. There an apparent lower transition disappeared because deterministic pieces were recombined before norm estimates. Here the upper boundary first retreats after proof-level uniformity is exposed, then localizes to one bilinear coherence term after the energy identity is unpacked. In both cases, a moving frontier is credible only after exact structure and quantitative uniformity are expressed in the native observable.

At `x~H/log^3 T`, the decisive question is now whether `Re C_I(x)=o(H)`, has a computable `H`-scale deterministic correction, or can survive in a matched admissible model. Merely lowering the `L^2` mass of `R_I` or the exterior mass of `A_I` cannot resolve the current boundary because those terms are already small enough.

**Boundary.** This is pointwise and proof-structural. It does not control the integrated theorem with moving test support, prove cancellation in `C_I`, show that `H/log^3 T` is intrinsic, or improve the arithmetic prime-source input. The unresolved mechanism is the specific inside--outside coherence, not a theorem that pair correlation changes regime there.