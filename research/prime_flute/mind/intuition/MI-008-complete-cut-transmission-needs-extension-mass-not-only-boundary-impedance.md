# MI-008 — Complete-cut transmission needs extension mass, not only boundary impedance

**Evidence level:** proved

## Core intuition

Local corridor attenuation does not determine transmission across the same edge after it is embedded in variable reservoirs. The exact scalar Schur invariant contains a second quantity besides boundary impedance: the norm of the endpoint-normalized harmonic extension into each reservoir, equivalently the spectral derivative of the boundary impedance.

A variable background can make those extension masses diverge and erase a small isolated-edge factor while keeping the whole operator positive and scalar. Complete-cut control therefore needs a reservoir theorem, not just a seam theorem.

## Strongest justified claim

PF-228 computes the isolated straight-corridor edge and obtains the favorable local attenuation scale. PF-229 shows that a translation-invariant scalar serial completion preserves that scale up to a fixed factor, suggesting that the local gain might survive embedding.

PF-279 gives the exact general two-reservoir formula. If `beta_L,beta_R` are the inverse endpoint Green values and `c` is the cut conductance, then

`||1_R M_eta^(-1) 1_L|| = c sqrt(beta_L'(eta) beta_R'(eta)) / (beta_L(eta) beta_R(eta)-c^2)`.

The derivative `beta'` is exactly the squared Hilbert norm of the endpoint-normalized harmonic extension. PF-279 constructs a positive variable Jacobi family for which the isolated edge transmission is `O(w/s)` while the complete half-chain cut converges to a strictly positive constant because the reservoir extension mass compensates the local small factor.

## Synthesis of evidence

The translation-invariant success of PF-229 was a special reservoir-control theorem in disguise. Once the background varies, scalar positivity and the endpoint Weyl value do not fix how much mass the normalized boundary state acquires in the bulk. That mass is exactly what the full cross-cut norm multiplies.

This identifies a concrete invariant for the physical nested-cut problem: control the left/right extension Gram forms, or show that the low/high projections consumed by the Prime-Flute endpoint kill the dangerous extension directions.

## Counterevidence / boundary cases

PF-279 is a matched scalar Jacobi control, not the physical flute. It proves that local gain cannot be extrapolated from positivity/scalarity alone; it does not prove that the physical reservoirs amplify. Additional monotonicity, geometry, or projection structure could bound the extension masses.

The formula concerns one scalar cut after Schur reduction. Matrix-valued or genuinely nonlocal couplings may require a different invariant rather than a scalar `beta'`.

## Epistemic status

**Exact operator-theoretic boundary:** complete-cut transmission depends on boundary impedance and endpoint-extension mass; the latter can erase the isolated corridor gain in a positive variable scalar system.

## Novelty/prior-art status

PF-279 treats the Schur/Weyl ingredients as standard operator theory. The Mathia contribution here is their role as the exact missing invariant in the current Prime-Flute cut extrapolation.

## Falsification criterion

Prove from the physical Prime-Flute reservoir equations that `beta_L'` and `beta_R'` remain uniformly controlled at the required seam scale, or that the consumed projections annihilate the extension amplification even when the unprojected cut norm is large. Either would show that PF-279's matched control does not obstruct the physical nested cut.

## Lean-formalizable core

The finite-dimensional Schur-complement identity expressing the off-diagonal inverse block through endpoint Green values and their resolvent derivatives is a natural formalizable linear-algebra statement.
