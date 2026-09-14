# MI-017 — Strong high-zero target rescue survives growing Nyman orthogonality at the inverse-section scale

**Evidence level:** exact finite-section reduction from NB-115--NB-117, sharpened by [NB-118](../../findings/NB-118-finite-nyman-orthogonality-forces-strong-zero-packet-target-capture-into-inverse-section-modes.md), [NB-119](../../findings/NB-119-fixed-finite-nyman-orthogonality-admits-perfect-target-capture-at-the-inverse-section-scale.md), and [NB-120](../../findings/NB-120-growing-nyman-orthogonality-still-admits-inverse-section-perfect-target-capture-in-the-mixed-tail-regime.md). These results constrain finite packets of actual zeta zeros through exact Nyman source orthogonality, but they do not exclude the required `1/R` compression mode even for a substantial growing family of source equations.

NB-115 proves that if a target-poor continuum packet captures a fixed positive fraction of the finite Nyman target, substantial target weight must pass through cell-compression modes. NB-116 identifies the high-zero height scale, and NB-117 turns finite target access into an exact interpolation problem: the cell primitive of a finite actual-zero packet is a confluent power sum, while the minimum-energy profile for fixed target endpoint difference is `C+D/n`.

NB-118 adds source information independent of zero height. Every finite actual-zero packet is orthogonal to each fixed Nyman generator, so capture above the finite residual baseline `d_M^2` forces the visible target correlation to be cancelled beyond the cutoff. The tail of a fixed Nyman section has squared norm `O_M(1/R)`, giving the inverse-section retention law.

NB-119 shows that this law is exactly saturable if one forgets the actual zero-power representation. For each fixed `M`, the periodic tail Gram satisfies `Gamma_(M,R)=C_M/R+O_M(1/R^2)`, and a minimum-norm invisible tail repairs the perfect visible target into `V_M^perp` with retained fraction `1/(kappa_M R)+O_M(1/R^2)`.

NB-120 shows that “let `M` grow” is not by itself the missing resource. When `M=M(R)->infinity` but `M^6(1+log M)/R->0`, exact matched controls still satisfy every equation `<f,g_b>=0`, `2<=b<=M`, while preserving `Q_R f=e_R` and

`||Q_R f||^2/||f||^2=(1+o(1))/(kappa_infty R)`.

The limiting repair constant is finite and positive. Its existence follows from an exact arithmetic factorization of the periodic tail Gram through a GCD-square kernel and Jordan totients; `kappa_M` converges instead of diverging. Thus an increasing number of exact Nyman constraints can remain asymptotically cheap in the destination retention currency.

The conceptual point is now sharper: **Nyman orthogonality is not enough unless its growth outruns the mixed-tail repair mechanism or is coupled to the actual zero-power representation across cutoffs**. Height controls continuum mass; Nyman equations force target rescue into an inverse-section mode; but that mode remains exactly feasible for a substantial growing source section if the witness may be rebuilt at each `R`.

The live theorem is therefore to separate actual off-critical zero powers from these growing matched controls. The missing input must use the confluent/exponential-polynomial structure of NB-117, a faster-growing Nyman section with quantitatively controlled transition, cross-cutoff coherence, or another source-specific identity. Merely increasing the number of exact equations while remaining in `M^6 log M << R` cannot improve the inverse-section exponent.

**Boundary.** NB-120 does not construct a packet of zeta zeros, does not satisfy the full infinite Nyman family at any finite cutoff, and does not claim that the sufficient exponent `1/6` is sharp. It closes only the substantial mixed-tail regime in which growing finite Nyman orthogonality still admits perfect visible target capture at `Theta(1/R)` retention.