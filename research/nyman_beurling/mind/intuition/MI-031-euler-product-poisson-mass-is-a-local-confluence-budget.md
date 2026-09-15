# MI-031 — Euler-product Poisson mass is a local confluence budget

**Evidence level:** exact source-specific local occupancy theorem from [NB-144](../../findings/NB-144-euler-product-poisson-mass-forces-logarithmic-confluence-away-from-the-one-line.md), applied to the target-poor logarithmic packet obstruction isolated in NB-140--NB-143.

The absolutely convergent Euler product to the right of `Re s=1` supplies a local resource that generic xi-type zero geometry does not have. For `sigma>1`, every nontrivial zero contributes positively to the real logarithmic-derivative Poisson sum, while

`|zeta'/zeta(sigma+it)| <= -zeta'/zeta(sigma) ~ 1/(sigma-1)`.

Functional-equation symmetry makes a right-half zero and its reflected partner pay a combined positive charge. For a polynomially small cell centered at `beta_0=1-epsilon`, this yields the occupancy ceiling

`d_G <= (epsilon(1-epsilon)/2+o(1)) log G`.

The coefficient has geometric meaning: approaching the one-line makes each pair increasingly expensive in the exterior Poisson budget. If the center moves with `epsilon_G->0` and `epsilon_G log G->infinity`, then

`d_G <= (1/2+o(1)) epsilon_G(1-epsilon_G) log G = o(log G)`.

For actual zeta zeros the Vinogradov--Korobov zero-free region keeps `epsilon_G log G` large enough for this conclusion. Thus logarithmic-rank target-poor confluence cannot drift arbitrarily close to the one-line even though the xi-type matched control of NB-143 can realize such packets under the same coarse analytic constraints.

The reusable intuition is that **a source-side positive kernel can turn distance from an arithmetic convergence boundary into a local multiplicity tax**. This is stronger than a global zero-density envelope because it charges the exact packet seen by the destination, and stronger than generic xi realizability because its budget comes from the Dirichlet-series/Euler-product half-plane.

The remaining obstruction is equally precise. At fixed interior `epsilon>0`, the budget is still `Theta(log G)` and therefore leaves room for the logarithmic rank needed by the target-poor confluence construction. The next useful source theorem must either make the per-zero charge effectively grow at fixed interior location, add an independent positive/source constraint that reduces the admissible rank to `o(log G)`, or prove that packets below the Poisson ceiling are necessarily target-bearing.

**Boundary.** The Poisson budget is an occupancy theorem, not a target-projection theorem. It excludes a concrete region of matched-control geometry but does not prove RH, simplicity, a fixed-interior `o(log G)` law, or Nyman approximation. Its force comes specifically from the actual zeta Euler-product source.