# MI-011 — Same-horizon physical laws can be cheap, finite horizon entropy forces a Cesàro gap, and the superexponential escape is real

**Evidence level:** exact for the floor-quotient Fourier skeleton through [FD-117](../../findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md)--[FD-125](../../findings/FD-125-square-root-common-sources-saturate-the-fourier-skeleton-on-repeated-square-horizons.md). The same-horizon countermodels and the FD-125 repeated-square source are synthetic quotient sources; FD-125 does not satisfy the full physical Mertens increment/multiplicative laws.

FD-117 shows that the complete cumulative Farey discrepancy field is invertibly equivalent to the quotient-Mertens staircase. FD-118 compresses its same-horizon Fourier data to the divisor-closed floor-quotient skeleton `Q_N`, of size `2 sqrt(N)+O(1)`, without losing that source.

FD-119 identifies the coercivity obstruction inside this reversible carrier. In reindexed source coordinates the skeleton has an exact Möbius equality ray. Any fixed true Mertens prefix plus the exact divisor identity can be grafted onto that ray with only bounded additional energy. FD-120 goes further: a complete single-horizon squarefree/nonsquarefree increment alphabet, `a_N(1)=1`, the exact divisor identity and terminal size `sqrt(N)+O(1)` still permit critical near-saturation when the witness may be reprogrammed with the horizon.

FD-121--FD-124 quantify what one common source costs. Fixed squarefree dilation edges force pair gaps, bounded-ratio integer chains force a positive Cesàro deficit for polynomially bounded sources, and the ratio ceiling can be removed. If

`Lambda_n=(1/n)log(H_n/H_0)`

stays bounded along an infinite subsequence, then the average of `1-S_(H_j)` along that subsequence stays bounded away from zero. Hence Cesàro saturation requires `Lambda_n->infinity`: the horizons must be superexponentially sparse in the chain index.

FD-125 shows that this condition is qualitatively sharp for the abstract common-source skeleton. Take `H_0=4` and `H_(j+1)=H_j^2`. There exists one horizon-independent source `Y` on the nested quotient carriers with

`|Y(n)|<=2 sqrt(n)`, `Y(H_j)=sqrt(H_j)`,

and

`E_(H_j)^Q(Y)=H_j+O(H_(j-1)(log H_(j-1))^3)`.

Therefore `S_(H_j)=1-o(1)` on every repeated-square horizon. The construction already obeys the critical square-root pointwise envelope. Generic common-source coherence plus polynomial growth is thus insufficient to force a pointwise endpoint gap once logarithmic horizon entropy is allowed to diverge.

This turns the previous loophole into a matched control. A theorem cannot now close the line by proving a more elaborate version of generic cross-horizon coherence under the same abstract source class: FD-125 is an explicit member of that class at the target scale. The missing restriction must distinguish the actual Mertens/Farey source from the synthetic nested-carrier source.

The obvious remaining candidates are genuinely physical arithmetic laws: the global squarefree/unit increment rule, multiplicative compatibility, or another nonredundant identity that couples carrier values not already free in the FD-125 recursion. Such a law is useful only if it can be shown to charge the repeated-square source at critical scale; merely adding another representation of the cumulative discrepancy is redundant.

The reusable distinction is now four-way. Same-horizon admissibility can be asymptotically invisible. Finite-entropy multihorizon compatibility creates an average cost. Superexponential scheduling can evade that generic cost even with a square-root source envelope. Physical-source admissibility may still forbid the escape, but that is a new arithmetic theorem rather than a continuation of the generic coherence argument.

**Boundary.** FD-125 does not construct the true Mertens function, satisfy its full increment/multiplicative laws, prove or refute RH, or show that every superexponential chain admits saturation. It proves that the superexponential escape left by FD-124 is real in the audited relaxed class. The next theorem must use arithmetic structure that FD-125 deliberately omits and show that this structure survives the floor-quotient compression with pointwise force.