# Weil-positivity research lines

This file holds the current mathematical lines of investigation suggested by the durable Weil-positivity intuitions. It is not a roadmap, task queue, status page, or history.

## Build a closable nonseparable source-forced pairing that preserves the Mangoldt half-density

**Linked intuitions:** `MI-001-positivity-needs-a-sign-producing-global-operation`, `MI-010-source-forced-critical-gram-can-have-the-wrong-weil-orientation`, `MI-011-prime-ray-marginals-do-not-determine-mixed-prime-coupling`, `MI-012-automorphic-multiplicity-does-not-prevent-global-scalarization`, `MI-013-critical-sector-transport-needs-new-global-arithmetic-structure`.

WP-216--WP-255 show that canonical gauge/Toeplitz/Morita/KMS routes either miss the critical sector, scalarize the needed relation, or cannot pack independent prime channels into a normalized `KMS_1` state.

WP-256--WP-259 give the positive intermediate carrier. Free-prime multiplicity canonically produces the exact diagonal `Lambda(n)/sqrt(n)`, and the permutation-fixed sector restores the Gibbs boundary to `beta=1` without losing that diagonal.

WP-260 closes the canonical one-body positivity upgrade: the bosonic Gibbs/Fisher Hessian inserts an extra occupation factor and therefore has the wrong prime-power law. WP-261 then tests coherent cross-prime mixing through the compressed symmetric-Fock boundary. Finite truncations are positive, the diagonal remains exactly Mangoldt half-density, and the first prime layer gains forced off-diagonal entries because every prime maps to the same vacuum. Globally, however, the boundary form is nonclosable for every `0<sigma<=1`; the same obstruction holds for any fixed finite-dimensional boundary receiving the exact prime-layer norms.

This leaves a sharp dichotomy. Retaining orthogonal prime labels gives a bounded exact carrier but no cross-prime coherence. Collapsing them coherently into finite dimension creates interaction but destroys closability at the Weil exponent. The live theorem must therefore construct a **source-forced infinite-dimensional closable correspondence**, or justify a genuinely different operator category, that keeps the half-density while supplying the completed Weil orientation and Gamma/polar sectors.

## Treat coefficient sourcing, criticality, interaction, closability, and Weil orientation as separate gates

The Fock hierarchy now solves coefficient sourcing and symmetric-sector criticality. It also supplies a canonical operation that begins to mix prime channels, but WP-261 shows that finite-dimensional coherent mixing is analytically inadmissible at critical scale. Future proposals must state separately how they preserve the exact diagonal, create nonseparable interaction, remain closable on the infinite prime system, and recover the signed completed Weil form.
