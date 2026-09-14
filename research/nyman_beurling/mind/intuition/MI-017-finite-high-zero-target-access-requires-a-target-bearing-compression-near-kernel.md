# MI-017 — Strong high-zero target rescue hits a sharp inverse-section matched-control boundary under fixed Nyman equations

**Evidence level:** exact finite-section reduction from NB-115--NB-117, sharpened by [NB-118](../../findings/NB-118-finite-nyman-orthogonality-forces-strong-zero-packet-target-capture-into-inverse-section-modes.md) and the matched-control saturation in [NB-119](../../findings/NB-119-fixed-finite-nyman-orthogonality-admits-perfect-target-capture-at-the-inverse-section-scale.md). These results constrain finite packets of actual zeta zeros through exact Nyman source orthogonality, but fixed finite source equations alone do not exclude the required `1/R` compression mode.

NB-115 proves that if a target-poor continuum packet captures a fixed positive fraction of the finite Nyman target, substantial target weight must pass through cell-compression modes. NB-116 identifies the high-zero height scale: a packet above ordinate `G` has Burnol mass `O(1/G)`, leading to retained-energy fraction `O(1/G+1/R)`. NB-117 turns this into an exact interpolation problem: the cell primitive of a finite actual-zero packet is a confluent power sum, and the unique minimum-energy profile for fixed target endpoint difference is `C+D/n`.

NB-118 adds a source constraint independent of zero height. Every finite actual-zero packet is orthogonal to each fixed Nyman generator `g_b`, hence to every fixed finite space `V_M=span{g_2,...,g_M}`. Let `p_M=P_(V_M)e`, `r_M=e-p_M`, and `d_M=||r_M||`. If a packet captures a target fraction `c>d_M^2`, then the visible correlation exceeding the residual baseline cannot come from `r_M`; it must use `p_M` and, by exact source orthogonality, be cancelled in the cells beyond the cutoff. Since the tail of a fixed `p_M` has squared norm `O_M(1/R)`, every sufficiently large finite section with capture `c>d_M^2` contains a target-bearing witness with retained fraction `O_(M,c)(1/R)`.

NB-119 shows that this exponent is the exact boundary of fixed finite source information. For fixed `M`, let `h_(b,R)=(I-Q_R)g_b` and let `Gamma_(M,R)` be their tail Gram matrix. Periodicity of the cell coefficients `{n/b}` gives

`Gamma_(M,R) = C_M/R + O_M(1/R^2)`,

where the periodic mean Gram matrix `C_M` is positive definite. The unique minimum-norm invisible tail that repairs the perfect visible target `e_R` into `V_M^perp` therefore has squared norm

`kappa_M R + O_M(1)`,

with `kappa_M=a_M^* C_M^(-1) a_M>0` and `a_M=(log b/b)_(2<=b<=M)`. Thus there are exact matched controls satisfying every fixed equation `<f,g_b>=0`, `2<=b<=M`, while

`Q_R f=e_R`, `q_R(f)=1`, and `||Q_R f||^2/||f||^2 = 1/(kappa_M R)+O_M(1/R^2)`.

For `M=2`, `kappa_2=2(log 2)^2`, so `R` times the retained fraction tends to `1/[2(log 2)^2]≈1.04068`. Adding any fixed number of Nyman equations changes the constant but not the inverse-section exponent.

The conceptual point is now sharper: **source orthogonality strengthens the compression law, but fixed finite source truth is itself saturated by source-equation-faithful matched controls**. Height controls continuum mass; finite Nyman equations force strong target alignment into an inverse-section mode; the natural-cell tail Gram geometry then shows that such a mode is exactly feasible if one forgets the actual zero-power representation.

The live theorem is therefore to separate actual off-critical zero powers from these matched controls. The missing input must use the confluent/exponential-polynomial structure of NB-117, a growing family of source equations with controlled constants, cross-cutoff coherence, or another source-specific identity. Sending `M` upward is not free: `d_M->0` is itself the Nyman approximation/RH problem and the repair constants can deteriorate.

**Boundary.** NB-119 does not construct a packet of zeta zeros and does not satisfy all Nyman equations at once. Its witness is rebuilt for each cutoff and is only required to lie in `V_M^perp` for fixed `M`. What it closes is the possibility that fixed finite Nyman orthogonality by itself could improve `NB-118` from `O(1/R)` to `o(1/R)` or forbid perfect visible target capture at that scale.