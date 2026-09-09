---
id: CLUE-prime-flute-critical-jacobi-square-root-decay-window
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-243-fixed-seam-robin-homotopy-reduces-high-high-shear-to-one-sided-separated-poisson-smoothing.md
  - research/prime_flute/findings/PF-247-fixed-axis-compactification-is-parity-jacobi-in-corridor-modes.md
  - research/prime_flute/findings/PF-248-parity-jacobi-tail-is-trace-class-but-first-moment-critical.md
  - research/prime_flute/findings/PF-249-positive-separation-preserves-free-jacobi-square-root-threshold.md
  - research/prime_flute/findings/PF-250-half-line-fractional-edge-powers-retain-supercritical-separated-window.md
  - research/prime_flute/findings/PF-251-exact-zero-edge-solutions-select-growing-inverse-square-jacobi-branch.md
  - research/prime_flute/findings/PF-252-zero-edge-ground-state-transform-has-bessel-four-scaling.md
  - research/prime_flute/findings/PF-253-bessel-four-jacobi-fractional-powers-have-sharp-separated-window.md
  - research/prime_flute/clues/CLUE-robin-homotopy-separated-poisson-shear-estimate.md
---

# Does the critical Jacobi edge leave a supercritical smoothing window for the actual Robin factor?

## Observation

PF-247 reduces the fixed-axis compactification to two asymptotically constant parity Jacobi chains. PF-248--PF-250 establish the free Dirichlet calibration: for `0<\sigma<1`, the half-line image term improves the fixed-row fractional-power tail to `n^{-2-2\sigma}`, and fixed positive output separation gives the sharp full-output threshold

\[
R<\frac32+2\sigma.
\]

PF-251 then shows why generic trace-class transfer is unavailable for the actual chain: the full half-line zero condition selects a positive solution growing like `j^{3/2}`, while the independent tail solution is `j^{-1/2}`. PF-252 converts that exact positive branch into a weighted nearest-neighbor operator with cubic mass and conductance and radial Bessel-four scaling.

PF-253 now proves the previously conjectural fractional-kernel consequence for the **actual** PF-247 parity chains. In the separated cone,

\[
\left|\langle e_i,J_\varepsilon^\sigma e_j\rangle\right|
\asymp
(i+1)^{3/2}(j+1)^{-5/2-2\sigma},
\qquad j\ge2i+2,
\]

and after any fixed positive output separation,

\[
\boxed{
E_dJ_\varepsilon^\sigma N^R\in\mathcal S_2
\iff R<2+2\sigma,
}
\]

with no bounded extension at or above the endpoint. Thus a literal square-root factor has the sharp actual-chain window `R<3`. The first-moment-critical inverse-square tail does not close PF-243's required `R>1` window; its exact Bessel-four geometry strengthens the free calibration by one half-power.

## Research question

What is the exact scalar function, operator mean, or finite functional-calculus expression in the fixed-axis relative operator `J_\varepsilon` that occurs in the **seam-normalized far-leg Robin-Poisson factor** from PF-243, and what is its leading non-smooth behavior at `\lambda=0`?

Once that factor is identified, does its edge behavior reduce to positive fractional powers (or another explicitly controlled functional-calculus class) strongly enough that PF-253's proven `R>1` margin survives the actual `K_a=T_a^{1/2}` replacement, Hardy ends, and PF-235's `O(w^2)` hypercycle-to-axis coordinate defect?

The question is no longer whether the Bessel-four model fractional tail exists. PF-253 settles that subproblem. The live issue is whether the **operator actually consumed by the Robin source map** belongs to the favorable class and whether later geometric perturbations preserve enough of the now-quantified margin.

## Why it may matter

PF-243 reduces the remaining high-high shear gate to one-sided separated-Poisson smoothing of any fixed order `R>1`. PF-253 provides substantially more than that for every literal positive fractional edge power: its sharp threshold is `R<2+2\sigma`, and for the square root it is `R<3`.

A positive identification of the actual Robin factor could therefore turn the endpoint problem from an unknown critical-Jacobi smoothing question into a finite exponent-budget transport problem. A negative identification would be equally decisive: if the exact factor has a zero-edge singularity not covered by positive fractional powers or otherwise creates a long-range mode tail beyond `R>1`, the fixed-axis functional-calculus route can be closed before spending effort on the later geometric perturbations.

## Decisive test

Derive the fixed-axis seam-normalized Robin source-to-bulk factor from the PF-238/PF-243 variational construction without replacing the actual complete-lift seam by a commuting proxy. Express the resulting mode-conversion factor directly in terms of `J_\varepsilon` and the corridor weight, and determine its exact leading behavior as `\lambda\downarrow0`.

If the leading nonlocal term is a positive fractional power `J_\varepsilon^\sigma`, or a finite combination for which PF-253 gives the load-bearing tail, propagate the sharp threshold `R<2+2\sigma` through the remaining fixed-axis factors and verify that some uniform `R>1` survives. Only after this succeeds should the route spend margin on the `T_a` replacement and the width-dependent hypercycle/axis deformation.

Kill the route if the actual factor has a worse zero-edge singularity that defeats every `R>1` separated estimate, if a required functional-calculus operation reintroduces a non-summable high-to-low tail not controlled by PF-253, or if one of the canonical later perturbations consumes the entire proven margin. Do not reopen the generic first-moment perturbation question: PF-253 bypasses it using the exact ground-state geometry.

## Evidence boundary

PF-253 is canonical evidence for literal powers `J_\varepsilon^\sigma`, `0<\sigma<1`: it proves the Bessel-four off-diagonal exponent and the sharp separated full-output threshold `R<2+2\sigma`. The earlier `n^{-5/2-2\sigma}` prediction and the square-root threshold `R<3` are no longer heuristic calibrations.

PF-253 does **not** identify the normalized complete-lift Robin factor as `J_\varepsilon^\sigma`, does not prove a general theorem for arbitrary functions of `J_\varepsilon`, and does not control `T_a`, Hardy ends, hypercycle reparameterization, physical `P/H` recoupling, finite-pant completion, neighboring-module extension, or global weak-`S_1` reassembly. No new theorem about zeta zeros or RH is claimed.

## Research disposition

Accepted for continued investigation. PF-248--PF-250 established the free half-line window; PF-251 identified the boundary-selected inverse-square threshold branch; PF-252 supplied the exact Bessel-four ground-state geometry; PF-253 now proves the corresponding actual-chain fractional kernel and sharp separated window.

The surviving question is narrower and more structural: **identify the exact Robin functional factor and transport the proven Bessel-four exponent budget to the physical separated Poisson maps.** The clue remains accepted rather than resolved because that operator identification and transport are precisely the parts PF-243 ultimately needs.