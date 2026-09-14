# MI-017 — Strong high-zero target rescue survives growing Nyman orthogonality and the entire nested cutoff prefix

**Evidence level:** exact finite-section reduction from NB-115--NB-117, sharpened by [NB-118](../../findings/NB-118-finite-nyman-orthogonality-forces-strong-zero-packet-target-capture-into-inverse-section-modes.md), [NB-119](../../findings/NB-119-fixed-finite-nyman-orthogonality-admits-perfect-target-capture-at-the-inverse-section-scale.md), [NB-120](../../findings/NB-120-growing-nyman-orthogonality-still-admits-inverse-section-perfect-target-capture-in-the-mixed-tail-regime.md), [NB-121](../../findings/NB-121-finite-nested-cutoff-coherence-collapses-to-the-maximal-section.md), and [NB-122](../../findings/NB-122-full-prefix-nested-coherence-still-admits-one-perfect-target-inverse-section-control.md). These results constrain finite packets of actual zeta zeros through exact Nyman source orthogonality, but the matched controls are broader Hilbert-space objects and do not construct actual zero-power packets.

NB-115 proves that if a target-poor continuum packet captures a fixed positive fraction of the finite Nyman target, substantial target weight must pass through cell-compression modes. NB-116 identifies the high-zero height scale, and NB-117 turns finite target access into an exact interpolation problem: the cell primitive of a finite actual-zero packet is a confluent power sum, while the minimum-energy profile for fixed target endpoint difference is `C+D/n`.

NB-118 adds source information independent of zero height. Every finite actual-zero packet is orthogonal to each fixed Nyman generator, so capture above the finite residual baseline `d_M^2` forces the visible target correlation to be cancelled beyond the cutoff. The tail of a fixed Nyman section has squared norm `O_M(1/R)`, giving the inverse-section retention law.

NB-119 shows that this law is exactly saturable if one forgets the actual zero-power representation. For each fixed `M`, a minimum-norm invisible tail repairs the perfect visible target into `V_M^perp` with retained fraction `1/(kappa_M R)+O_M(1/R^2)`. NB-120 shows that increasing the number of exact source equations does not by itself break the repair: when `M=M(R)->infinity` with `M^6(1+log M)/R->0`, exact controls remain in `V_M^perp`, satisfy `Q_R f=e_R`, and retain `(1+o(1))/(kappa_infty R)` with finite positive `kappa_infty`.

NB-121 proves that every fixed finite nested ladder is algebraically redundant with its maximal cutoff and maximal Nyman section. NB-122 removes the remaining “make the ladder widen” escape. The same maximal NB-120 repair satisfies

`Q_r f = e_r`

**exactly for every integer cutoff `2<=r<=R` simultaneously**, while remaining orthogonal to every `V_(M_r)` with `M_r<=M(R)`. Its retained fraction at cutoff `r` is

`L_r / ((kappa_infty+o(1)) R)`

uniformly across the full prefix. For early scales with `r/R->0`, this is even smaller than the nominal `1/r` inverse-section scale. Increasing the number of nested observations all the way to `R` therefore adds no independent source equation capable of excluding the matched control.

This identifies the exact coherence test. “Same source across scales” is real mathematical currency only if the joint constraints are **nonredundant under the nesting/projection algebra**. Here `Q_rQ_R=Q_r` and the generator spaces are nested, so the full prefix is still determined by the maximal section. The fact that early and late cutoffs share one vector does not itself impose an additional incompatibility.

The remaining source-faithful routes are consequently narrower: exploit the confluent/exponential-polynomial transformation law forced by actual zero powers; force a source-section transition outside the sufficient mixed-tail regime `M^6 log M << R`; or introduce genuinely non-nested, tail-sensitive or otherwise independent cross-scale information that cannot be recovered by projecting one maximal constraint.

**Boundary.** NB-122 does not show that an actual finite packet of zeta zeros realizes the matched control, and NB-120 does not classify source sections beyond its sufficient mixed-tail regime. The full infinite Nyman source law is not satisfied at a finite cutoff merely because every fixed generator equation is eventually included along a diagonal sequence. What is closed is narrower and exact: **nested natural-cell cutoffs, even the complete growing prefix, do not by themselves improve the inverse-section matched-control exponent.**