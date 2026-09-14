# MI-019 — Strong finite-edge hiding separates inverse-window companion geometry from cancelling phase

**Evidence level:** exact consequence of [RE-125](../../findings/RE-125-invisible-algebraic-subedge-atoms-require-a-reciprocal-scale-ordinate-annulus.md)--[RE-128](../../findings/RE-128-gevrey-localization-squeezes-strong-atom-companions-to-inverse-window-spacing.md), building on the full-packet phase transfer of RE-123 and matched-filter localization of RE-124. No theorem excludes the required zeta-zero pairs, controls the diffuse branch, the nonattained edge or `Theta=1`.

RE-125 identifies a hard inner boundary for cancellation. After target demodulation, every positive-ordinate companion with

`|gamma-gamma_0| <= c_*/U`

lies in the same right-half-plane coefficient sector as the target, so exact multiplicity and tighter micro-clusters reinforce rather than cancel.

RE-126 uses the local zero count to show that hiding an algebraically strong target forces a distinct logarithmically comparable companion outside that reinforcing ball. RE-127 then preserves sign information: at least one companion in the original `U^(-1+eta)` annulus has negative target-demodulated center projection of size `gg |a_0|/log U`. Equivalently its scaled signed gap plus the source coefficient phase lies in a fixed cancellation arc modulo `2pi`.

RE-128 sharpens a different coordinate. If the residual is hidden on the full window `|u-U|<=H`, `H=U^(1-theta)`, a Gevrey matched filter forces a distinct companion with

`c_*/U < |gamma_1-gamma_0| <= C H^-1 (log U)^(1+epsilon)`

and

`|a_1(U)| >= c |a_0(U)|/log U`.

The companion remains in the `O(log U/U)` horizontal edge layer and at polynomial height. Thus the strong-atom cancellation cloud must already contain logarithmically comparable mass at essentially the inverse observation-window resolution.

The important boundary is that RE-128 is an **absolute-mass localization**, not a signed one. In the transition region of the Gevrey cutoff, small Taylor corrections relative to each annular coefficient need not be small relative to the target when that coefficient is larger. The proof therefore does not move the RE-127 negative projection into the narrower RE-128 annulus.

The live strong-atom problem is consequently more precise than a generic close-pair question. Hidden targets require both (i) a very close logarithmically comparable near-edge companion at inverse-window scale, and (ii) a logarithmically comparable cancelling-phase companion in the wider signed annulus. They may or may not be the same zero. A closing theorem can either force the signed companion into the narrow annulus, show that such narrow strong near-edge pairs cannot persist, or exploit another source relation tying companion magnitude to phase.

**Boundary.** Neither condition is sufficient for hiding, pair consecutiveness is not proved, and the diffuse many-mode branch is untouched. The durable refinement is the separation of two resources that were previously conflated: inverse-window spacing/magnitude and target-demodulated sign.