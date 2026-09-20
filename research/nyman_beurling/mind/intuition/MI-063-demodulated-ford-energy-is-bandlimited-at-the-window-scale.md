# MI-063 — Ford bandwidth counts only when carrier coherence does not renormalize the critical layer

**Evidence level:** exact harmonic/source-specific synthesis from NB-246--[NB-253](../../findings/NB-253-positive-multi-shell-comb-recreates-the-ford-obstruction-at-shallower-depth.md), including the Hardy projection identity of NB-249, carrier representation NB-250, matched-packet crossover NB-251 and single-shell scale covariance NB-252. The matched packets are compatibility controls, not claims about actual zeta zeros.

NB-248--NB-250 fix the legal order of operations. The Ford-scaled pole must be Hardy-projected through positive Mellin frequencies before Hilbert-space squaring, which exactly recovers the finite depth-marked zero current. The resulting carrier band has natural width `Theta(H)=Theta(X/J)`, while pair phases still resolve ordinate differences at the finer `1/X` scale.

NB-251 shows that an independently available carrier span `W` with `W/H->infinity` would disperse the standard matched packet even before full `1/X`-cell orthogonality. NB-252 shows that literal single-shell dilation does not realize that premise: replacing `H` by `B_J H` simultaneously replaces `J` by `J/B_J` and transports the dangerous Ford layer.

NB-253 tests the first canonical fixed-`H` multi-carrier realization. For a positive equal-weight comb of `K` translated `H`-scale shells,

`L_K(v)=e^(iXv) F(Hv) P_K(CHv)`

with the normalized Dirichlet factor `P_K`. Although the convex carrier span is `Theta(KH)`, `P_K` creates a coherence peak of width `Theta(1/(KH))`. The selected-height capacity therefore becomes

`J_eff=R/(KH)=J/K`,

and the matched obstruction reappears at the shallower Ford coordinate

`d_crit=-log K+O(1)`.

Thus super-`H` support is not itself independent bandwidth. The source operation must supply carrier energy across that span **without** converting the same span into a narrower unit-height coherence peak and a correspondingly smaller effective population. Single-shell dilation and the positive normalized multi-shell comb fail by different mechanisms, but both export the apparent averaging gain into a renormalized critical geometry.

The remaining escape is sharper. Signed or complex carrier coefficients, a genuinely vector-valued family retained separately until after projection, or a nonuniform carrier architecture could still work, but it must keep the old Ford normalization and selected-height capacity while adding super-`H` carrier energy. If its Fourier recombination creates a dominant peak of width `1/W`, the matched layer must be re-audited at the population supported by that peak rather than at the original `J`.

**Boundary.** NB-253 is source-side and assumes the positive equal-weight mesoscopic regime stated there. It neither proves that zeta zeros realize the replacement packet nor excludes all multi-carrier constructions. Zeta-specific cancellation on the legal band and architectures whose coherence geometry is genuinely different remain open.