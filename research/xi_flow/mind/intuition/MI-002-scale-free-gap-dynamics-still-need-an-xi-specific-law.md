# MI-002 — Exact gap diffusion has nonperturbative Cauchy coercivity; Xi-specific boundary control remains the gate

**Evidence level:** exact for XF-004--XF-005 and XF-014--XF-015 on real-simple slices; RH/de Bruijn--Newman consequence remains open

## Core intuition

An absolute gap is the wrong currency for height-uniform backward heat because the natural spacing tends to zero. The scale-free normalized exterior field avoids that dimensional degeneration, and the full nonlinear zero dynamics reveal why its sign law is robust: the adjacent-gap vector evolves by a symmetric positive-conductance graph diffusion.

XF-015 now removes another possible weakness. The Cauchy/half-Laplacian bulk coercivity is not merely perturbative near an arithmetic lattice: on any finite block with a uniform upper gap envelope, the exact nonlinear conductances dominate the inverse-square kernel. Small gaps strengthen rather than weaken the bulk smoothing. The remaining failures are large-gap excursions, external flux, or loss of the real-simple regime.

## Strongest justified principle

XF-004 shows that absolute-gap continuation budgets shrink like `O(1/log^2 T)`. XF-005 introduces `R=qS` and obtains the exact scale-free pair law `q'=4(2-R)`.

XF-014 upgrades that local identity to the complete ordered gap field. On every real-simple slice,

`g_i' = 2 sum_{k != i} c_{ik}(g_k-g_i)`

with symmetric positive conductances

`c_{ik}=1/[(x_i-x_k)(x_{i+1}-x_{k+1})]`.

The normalized exterior field is exactly the nonlinear gap Laplacian, `2-R_i=g_i(L_x g)_i`. Every finite-block convex entropy has a nonpositive internal Dirichlet term plus a boundary interaction with gaps outside the block.

XF-015 identifies the finite-amplitude fractional scale. If `0<g_r<=Mh` on a block, then

`c_{ik} >= 1/[M^2 h^2 (k-i)^2]`,

so the quadratic bulk dissipation dominates the inverse-square discrete `H^{1/2}` seminorm by a constant depending only on `M`. A lower gap bound is unnecessary for this coercive direction. With a two-sided envelope the conductances are fully comparable to the Cauchy kernel and retain its algebraic tail.

For `N~A/h^2`, the induced finite-block variance decay has order-one bulk rate `Theta(1/A)`, uniformly as `h->0`. Thus the `N~log^2 T` fixed-time scale survives finite-amplitude nonlinear deformation whenever a height-uniform upper gap envelope is available.

## Evidence synthesis and boundaries

The positivity and envelope coercivity are universal for ordered logarithmic repulsion. They do not distinguish Xi from matched real-zero systems and do not control the external boundary term. A single large gap can also deteriorate the comparison by making `M` large.

The live theorem is therefore a source-specific envelope-plus-flux statement: use unconditional Xi information to control large-gap excursions and the external interaction of a `Theta(log^2 T)` block strongly enough that the universal bulk coercivity yields a fixed backward-time gain.

## Status / novelty

Positive graph diffusion, convex entropy dissipation, inverse-square fractional forms, and maximum principles are classical mechanisms; the exact conductance/envelope identities are persisted for this zero flow. The synthesis is the shift in obstruction: **nonlinear bulk coercivity survives finite amplitude, while source specificity now sits in upper-gap control, boundary flux, and global continuation**.

## Falsification criterion

Find a bounded-envelope real-simple block violating the XF-015 inverse-square lower conductance bound, or derive an Xi source theorem giving the required uniform envelope and flux control and hence fixed backward time.

## Lean-formalizable core

- Exact differenced zero ODE and positive conductances.
- Finite-amplitude inverse-square conductance lower bound.
- Nonlinear `H^{1/2}` bulk coercivity and finite-block Poincare scale.
- Convex entropy balance with boundary flux.
