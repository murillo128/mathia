# MI-017 — Strong high-zero target rescue must compress to the inverse-section scale once it exceeds a finite Nyman baseline

**Evidence level:** exact finite-section reduction from NB-115--NB-117, sharpened by [NB-118](../../findings/NB-118-finite-nyman-orthogonality-forces-strong-zero-packet-target-capture-into-inverse-section-modes.md). The result constrains finite packets of actual zeta zeros through exact Nyman source orthogonality; it does not exclude the required `O(1/R)` compression mode or prove a Nyman distance estimate.

NB-115 proves that if a target-poor continuum packet captures a fixed positive fraction of the finite Nyman target, substantial target weight must pass through cell-compression modes. NB-116 identifies the high-zero height scale: a packet above ordinate `G` has Burnol mass `O(1/G)`, leading to retained-energy fraction `O(1/G+1/R)`. NB-117 turns this into an exact interpolation problem: the cell primitive of a finite actual-zero packet is a confluent power sum, and the unique minimum-energy profile for fixed target endpoint difference is `C+D/n`.

NB-118 adds a source constraint independent of zero height. Every finite actual-zero packet is orthogonal to each fixed Nyman generator `g_b`, hence to every fixed finite space `V_M=span{g_2,...,g_M}`. Let `p_M=P_(V_M)e`, `r_M=e-p_M`, and `d_M=||r_M||`. If a packet captures a target fraction `c>d_M^2`, then the visible correlation exceeding the residual baseline cannot come from `r_M`; it must use `p_M` and, by exact source orthogonality, be cancelled in the cells beyond the cutoff.

The tail of a fixed `p_M` has squared norm `O_M(1/R)`. Consequently every sufficiently large finite section with capture `c>d_M^2` contains a target-bearing witness satisfying

`||Q_R f||^2/||f||^2 = O_(M,c)(1/R)`.

This removes the inverse-height branch for strong capture when `R/G->infinity`. The first thresholds are already nontrivial: `d_2^2=1-log 2≈0.30685`, while `M=3` gives `d_3^2≈0.09575`. Thus two fixed Nyman source equations force any capture above about `9.6%` onto the inverse-section retention scale, with no zero-counting, zero-density or packet-width input.

The conceptual point is that **source orthogonality can strengthen a target-bearing compression law without improving ambient conditioning**. Height controls how expensive the packet is in continuum norm; finite Nyman equations control how much of a strongly target-aligned packet may remain visible before the cutoff. These are independent resources, and after NB-118 the latter dominates the retention scale for capture above a fixed source baseline.

The live theorem is therefore to rule out, for actual off-critical zero powers, simultaneous strong target alignment and `O(1/R)` visible retention in the exact weighted harmonic-profile geometry of NB-117. Sending `M` upward is not a free way to drive the target baseline to zero: `d_M->0` is itself the Nyman approximation/RH problem, and the tail constants of `p_M` can deteriorate.

**Boundary.** Abstract exponential-polynomial packets may still possess such compression modes, and an arbitrarily large invisible tail can enforce the finite Nyman orthogonality equations. A fixed `M` gives no constraint below `d_M^2`. NB-118 narrows the source-specific escape; it does not close it.