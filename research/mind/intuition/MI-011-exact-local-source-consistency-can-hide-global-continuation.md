# MI-011 — Exact local source consistency can hide global continuation or preserve a pre-compression joint defect

**Evidence level:** supported by NB-066--NB-069 and RE-068--RE-071; no operator or estimate is transferred between the lines.

Nyman--Beurling and Robin Extremal expose different staged failures of “local matching implies global harmlessness.”

In Nyman, NB-066--NB-067 make the stable-tail obstruction a global continuation cost visible through finite Schur complements. NB-068 showed that zero one-cell memory and fixed finite Gram bandwidth do not by themselves prevent a hidden boundary mode. NB-069 then adds a source-specific correction: the actual innovations obey exact integer-dilation branching, and bounded fixed-band branching forces diagonal Gram geometry. The cheap nearest-neighbor boundary chain is therefore not a valid matched control once cross-scale source covariance is included.

The Nyman survivor is now more constrained: any genuine obstruction must preserve branching while using nonlocal or scale-growing Gram structure, and the finite Schur geometry remains the natural place to measure its continuation cost.

In Robin, RE-068 fixes the prime multiset exactly and RE-069 suppresses direct timing through the final kernel. RE-070 finds a surviving selector-density defect in `Z-vartheta(Z)`. RE-071 shows that the same adaptive packet simultaneously forces the logarithmic Mertens-product error to drift in the opposite direction. The surviving coordinate is therefore a joint pre-compression trajectory, not an unmatched source label.

The common discipline is: **match the exact source covariance first, identify what the local quotient/readout removes, and only then ask which global or geometric variable survives**. A control that matches local flags but not dilation branching is not source-faithful; a readout that kills direct timing need not kill selector-induced joint error drift.

**Boundary.** No Nyman Schur theorem transfers to Robin prime errors, and no Chebyshev--Mertens drift theorem transfers to Nyman continuation. The synthesis concerns the staged source/destination test only.