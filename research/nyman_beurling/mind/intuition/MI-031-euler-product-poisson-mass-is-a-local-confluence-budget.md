# MI-031 — Euler-product Poisson mass is a local confluence budget, and positive resampling cannot improve its fixed-interior coefficient

**Evidence level:** exact source-specific local occupancy theorem from [NB-144](../../findings/NB-144-euler-product-poisson-mass-forces-logarithmic-confluence-away-from-the-one-line.md), with method-optimality of the full positive exterior-sampling cone from [NB-145](../../findings/NB-145-positive-exterior-poisson-sampling-cannot-beat-the-NB-144-coefficient.md), applied to the target-poor logarithmic packet obstruction isolated in NB-140--NB-143.

The absolutely convergent Euler product to the right of `Re s=1` supplies a local resource that generic xi-type zero geometry does not have. For `sigma>1`, every nontrivial zero contributes positively to the real logarithmic-derivative Poisson sum, while

`|zeta'/zeta(sigma+it)| <= -zeta'/zeta(sigma) ~ 1/(sigma-1)`.

Functional-equation symmetry makes a right-half zero and its reflected partner pay a combined positive charge. For a polynomially small cell centered at `beta_0=1-epsilon`, NB-144 obtains

`d_G <= (epsilon(1-epsilon)/2+o(1)) log G`.

If the center moves with `epsilon_G->0` and `epsilon_G log G->infinity`, the same mechanism gives

`d_G <= (1/2+o(1)) epsilon_G(1-epsilon_G) log G=o(log G)`.

Thus the actual Euler-product source excludes near-one logarithmic-rank packets that remain compatible with the xi-type matched controls of NB-143.

NB-145 identifies the exact limitation of this positive mechanism. Replace the single exterior sample by any finite positive measure of sample points, allow arbitrary `G`-dependent placement and weights, and use only Poisson positivity on the zero side plus the pointwise absolute Euler-product majorant on the prime side. The resulting certificate can never beat the asymptotic coefficient

`epsilon_G(1-epsilon_G)/2`.

The one-point choice in NB-144 already attains that floor, including in the moving near-one regime. **More samples inside the same positive cone do not constitute more arithmetic information.** They merely redistribute one source budget whose per-zero charge has the same geometric ceiling.

The reusable intuition is therefore two-stage. A source-side positive kernel can turn distance from an arithmetic convergence boundary into a local multiplicity tax, but once the corresponding positive cone is optimized, further averaging or positive resampling cannot cross the remaining endpoint. At fixed interior `epsilon>0` the optimal tax is still `Theta(log G)`, exactly large enough to leave room for the target-poor logarithmic-rank obstruction.

The next source theorem must therefore change mathematical resource rather than sampling density: a signed or oscillatory combination with a controlled indefinite zero side, prime-side cancellation/correlation beyond the pointwise absolute majorant, a stronger local moment/pair law, or a theorem that every actual packet surviving below the positive Poisson ceiling is necessarily Nyman-target-bearing.

**Boundary.** NB-145 is an optimality theorem for a proof architecture, not a universal impossibility theorem for Euler-product information. It assumes positive exterior weights and the same pointwise absolute majorant. Signed combinations, correlations, higher moments, different source identities and target-projection information remain outside its scope. The Poisson budget is still an occupancy theorem, not a proof of RH or Nyman approximation.