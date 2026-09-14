# MI-017 — Selector, recovery and block maximality are one weighted stable-filter lobe

**Evidence level:** exact attained-edge reduction through RE-112--[RE-118](../../findings/RE-118-edge-normalized-block-maxima-are-weighted-stable-filter-lobe-records.md). No contradiction with false RH or theorem on the arithmetic placement of actual CA selectors is claimed.

Let `Theta` be an attained finite off-critical edge, `c=1-Theta`, and `J=F_Theta+G_Theta`. RE-114--RE-116 show that fixed rays and the self-consistent moving endpoint ray are spectrally compatible at syndetic phases. RE-117 then shows that the macroscopic first-recovery corridor is reconstructible from the same translated stable-filter state.

RE-118 adds the apparently stronger fact that the selected CA state is the **rightmost block maximum**. If `U=log log C` and `t=log(log N/log C)` stays in the first recovery corridor, then

`B_Theta(N) = (1+t/U) J(U+t) + o(1)`.

Hence block maximality becomes a forward record condition for the weighted state `u J(u)`, while first recovery is the end of its positive lobe. The actual packet also satisfies the moving-ray residual `J'(U)+J(U)/U=o(1)`.

This still does not distinguish the arithmetic selector. The same almost-periodic profile `J` contains syndetically many exact positive lobes whose rightmost global weighted maximum satisfies `(uJ(u))'=0`, remains the forward record until the first zero, has a uniform amplitude floor, and reaches that zero at bounded positive distance. Endpoint criticality, positive recovery and block-record maximality therefore remain mutually compatible inside the leading spectral control.

The missing datum is now unequivocally **placement below leading edge resolution**: how the discrete CA selector chooses among these compatible weighted lobes, a finer-than-`o(1)` discrepancy between the actual maximum and the continuous weighted record, or another source coordinate not reconstructible from `J`. Adding another leading-order extremality condition on the same lobe cannot supply it.

**Boundary.** The conclusion concerns the attained finite-edge branch and leading `Y^(-c)/log Y` normalization. It does not exclude lower-order arithmetic selection, the nonattained-edge branch or the separate `Theta=1` regime.
