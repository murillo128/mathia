# MI-003 — Fixed-time Xi memory is mesoscopic; the live localization tradeoff is boundary capacity versus span control

**Evidence level:** supported through XF-018; finite-jet and linearized-scale statements are exact in their stated regimes, XF-014's convergence repair has passed adversarial review, and the nonlinear localization identities are used only where the real-simple flow applies

## Core intuition

Order-one heat-time memory at height `T` lives on about `log^2 T` gaps, not in a finite collision jet or bounded stencil. The Cauchy/`H^{1/2}` boundary model explains why a fixed-shape cutoff cannot make boundary leakage lower order, but the newer results show that this obstruction is not universal: a diverging capacitary buffer can reduce pure Cauchy leakage, and an uncentered localization renormalizes singular nonlinear conductances into a bounded cross-ratio kernel.

The remaining burden has moved. It is no longer simply “control every small gap.” A successful source theorem must control the **large-gap/cumulative-span geometry and endpoint span/flux** needed to remove the neutral mean mode while retaining the small capacitary boundary budget.

## Strongest justified principle

XF-006 rules out every robust finite collision jet as Xi-specific; XF-007--XF-013 identify the mesoscopic `log^2 T` scale and the endpoint `L log L`/Cauchy carrier. The repaired XF-014 is now admissible evidence: telescoping gives the exact real-simple adjacent-gap diffusion and supports the finite-block identities without a uniform remote-gap bound.

XF-015 supplies finite-amplitude bulk coercivity under its stated envelope hypotheses. XF-016 shows that a fixed-ratio self-similar cutoff is scale critical: useful bulk and boundary leakage remain the same order.

XF-017 breaks that fixed-ratio no-go. A logarithmic capacitary taper whose outer/inner ratio `R` diverges has Cauchy localization cost `O(1/log R)`. Thus the correct boundary model must include the scalable ratio; a fixed-shape obstruction is not fundamental.

XF-018 changes the nonlinear carrier again. Localizing the uncentered gap square gives leakage weight `w_ik=c_ik g_i g_k`, with `0<w_ik<=1`; for nonadjacent gaps it is a bounded cross-ratio function dominated by the exact Cauchy interaction of the physical gap intervals. Its far tails telescope to endpoint-gap/cumulative-span ratios without a lower bound on every remote gap. The price is the neutral constant-gap mode: subtracting the block mean introduces a span/endpoint term that still needs source control.

## What remains possible

The live theorem should combine a slowly diverging capacitary buffer with Xi-specific control of endpoint gaps relative to cumulative spans and of the block-span/endpoint flux needed for centering. A positive would turn the existing bulk-minus-boundary identities into a fixed backward-time margin; a negative would exhibit source-compatible large-gap/span configurations that defeat every such assembly.

## Status / novelty

Fractional localization, capacity, cross-ratios, and Cauchy interactions are classical. The synthesis is the moving boundary gate: **fixed-time memory is mesoscopic, fixed-ratio leakage can be beaten, and the nonlinear collision singularity can be renormalized; source-level span/flux control is now the bottleneck**.

## Falsification criterion

Derive the required cumulative-span and endpoint-flux bounds from unconditional Xi data and close a fixed backward interval, or construct source-admissible real-simple configurations satisfying current mesoscopic constraints while violating those bounds strongly enough to erase the capacitary gain.

## Lean-formalizable core

- Mesoscopic `log^2 T` scale.
- Capacitary `O(1/log R)` cutoff cost.
- Bounded cross-ratio leakage identity and telescoping tails.
- Block variance as uncentered square minus span mode.
