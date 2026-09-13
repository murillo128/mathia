# MI-011 — Exact branching turns finite continuation into an aliased prediction problem; source consistency alone does not price the future

**Evidence level:** supported by Nyman--Beurling results through NB-084. The stationary inverse controls NB-081--NB-083 are exact matched calibrations; NB-084 gives an exact actual-source radial Toeplitz certificate but no quantitative decay theorem for its periodized spectra.

NB-074--NB-082 show that stable-tail exclusion is a quantitative finite-future problem. A source can be exactly consistent with arbitrarily deep continuation while remaining unaffordable if the prediction error falls too slowly. In stationary controls the relevant excess must reach roughly the `1/R` scale after aggregation.

NB-083 calibrates the inverse boundary. A unit-circle zero of a stationary outer polynomial produces only reciprocal-depth prediction improvement, forcing `L=Omega(R)` and an exponential-size future for bounded screening. Strict exterior zeros instead give geometric prediction and logarithmic depth.

NB-084 identifies the corresponding object for the actual Nyman source rather than transferring this stationary heuristic. Exact integer branching makes dilated copies of one innovation genuine combinations of later innovations. Restricting to one integer-dilation ray yields an anchored Toeplitz prediction problem whose scalar density is the **alias-periodized boundary energy** `W_(j,q)`, not the continuous Mellin factor itself.

This aliasing changes the meaning of boundary singularity. One zeta zero kills at most one summand; a zero of the prediction density requires simultaneous vanishing across an entire two-sided frequency alias class. The periodized density is positive almost everywhere, but that fact alone gives no affordable rate because thin deep valleys can still make finite prediction badly conditioned.

The source-specific continuation question is therefore: **how rapidly do the anchored Toeplitz errors of the periodized descendant spectra fall relative to the visible causal innovations, and can their aggregate charge be bounded at a future horizon that is not exponentially expensive?** A good radial estimate is already sufficient to exclude a stable tail; a bad one is not conclusive because the full nonstationary future may use cross-ray combinations.

The broader lesson is that exact local source consistency can hide a quantitatively difficult global continuation boundary. The relevant inverse object must be derived after the actual branching/aliasing geometry is imposed; an unaliased source factor or qualitative cyclicity is not enough.

**Boundary.** NB-084 does not prove a rate for `W_(j,q)`, exclude complete aliased zero progressions, or show radial descendants are optimal. The stationary `1/L` law remains a control, not an arithmetic conclusion.