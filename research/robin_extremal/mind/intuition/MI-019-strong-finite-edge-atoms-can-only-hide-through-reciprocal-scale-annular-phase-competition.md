# MI-019 — Dominant finite-edge hiding forces an inverse-window cancelling pair

**Evidence level:** exact consequence of [RE-125](../../findings/RE-125-invisible-algebraic-subedge-atoms-require-a-reciprocal-scale-ordinate-annulus.md)--[RE-129](../../findings/RE-129-hidden-dominant-subedge-atoms-force-inverse-window-cancelling-phase-companions.md), building on the full-packet phase transfer of RE-123. No theorem excludes the required zeta-zero pairs or the diffuse branch.

RE-125 gives a reinforcing inner radius: companions with `|gamma-gamma_0|<=c_*/U` lie in the same target-demodulated coefficient sector and cannot cancel the target. RE-128 then shows that hiding on an observation window of length `H=U^(1-theta)` forces logarithmically comparable mass into the narrow annulus

`c_*/U < |gamma_1-gamma_0| <= C H^-1 (log U)^(1+epsilon)`.

Before RE-129, the sign information lived only in the wider RE-127 annulus. RE-129 removes that separation by choosing an atom whose coefficient magnitude `M_K(U)` is maximal inside the packet. Every surviving annular coefficient is then at most `M_K(U)`, so the positive-order Taylor errors of the Gevrey filter remain small **after summing over the whole local zero packet**, not merely relative to each individual mode.

If the dominant algebraically strong packet is hidden, the narrow annulus must therefore contain a distinct companion with

`-Re(a_1(U) exp(i(gamma_1-gamma_0)U)) >= c M_K(U)/log U`,

and consequently `|a_1(U)|` is logarithmically comparable to the dominant target. The required spacing, magnitude and cancelling phase are now one object rather than separate resources.

This turns the strong-atom branch into a precise zero-geometry problem. Either such dominant near-edge cancelling pairs persist at the inverse-window scale, or the residual has an algebraic continuum excursion and the CA sampling theorem sees it. The remaining escape is the genuinely diffuse cloud where no individual coefficient is algebraically strong.

**Boundary.** The theorem is existential for a dominant atom, not for every preselected nonmaximal atom; the companion need not be consecutive and may depend on `U`. It does not contradict known zero-spacing results by itself.
