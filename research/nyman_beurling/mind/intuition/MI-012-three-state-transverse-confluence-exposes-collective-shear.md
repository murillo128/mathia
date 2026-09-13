# MI-012 — Three-state transverse confluence exposes collective canonical shear

**Evidence level:** exact for the synthetic right-half-plane control family of [NB-098](../../findings/NB-098-transverse-three-state-confluence-forces-order-independent-collective-shear.md), building on unit canonical pivots and uniform two-state conditioning from NB-096--NB-097. No claim is made that actual zeta zeros realize the synthetic confluence path.

Canonical Blaschke deflation removes two natural crowding pathologies. Raw Cauchy determinant collapse disappears exactly, and every two-state transformed Gram remains uniformly conditioned. It is tempting to infer that the remaining unit-upper-triangular shear might admit a separation-insensitive dimension-free bound.

NB-098 proves that this inference already fails with three states. For

`lambda_1=a+i epsilon`, `lambda_2=a+c epsilon`, `lambda_3=a-i epsilon`,

with fixed `a>0`, `c!=0`, the canonical transformed Gram has positive-diagonal Cholesky factor `R_epsilon` whose pivots remain exactly one and whose pairwise subsystems stay uniformly controlled, but

`|R_13|, |R_23| ~ [4a|c|/(1+c^2)] epsilon^(-1)`

and therefore

`kappa_2(C_epsilon)=Theta(epsilon^(-4))`.

The same leading blow-up occurs for every permutation of the three deflation factors. The failure is thus **collective and order-independent**: it cannot be assigned to one bad pair, one vanishing Schur pivot, determinant volume or a poor causal ordering.

The geometry is also path-sensitive. If the transverse displacement parameter `c` vanishes, the leading inverse-`epsilon` shear vanishes. Hence “three points collide” is not itself the obstruction; the obstruction is a particular transverse relative geometry that the canonical triangular coordinates amplify collectively.

The reusable lesson is that **bounded low-dimensional marginals do not control a triangular many-state coordinate system**. Even exact unit pivots and uniformly conditioned pairs leave room for large higher-order shear. Any dimension-free theorem must control a genuinely collective invariant or restrict the admissible multi-state geometry.

For the Nyman program this turns the next question into a source theorem. Actual zeta zeros would have to exclude or quantitatively suppress the transverse crowded configurations that produce the synthetic blow-up, or one must use a representation whose confluent limit absorbs them differently. Zero-density, separation, functional-equation structure or a true derivative/Jordan state system are possible resources; canonical half-line geometry alone is not.

**Boundary.** NB-098 uses arbitrary distinct right-half-plane parameters, not known or hypothetical zeta zeros. A genuine repeated zero is not obtained by choosing one distinct-point collision path and taking a limit. The finding also does not show that poor half-line conditioning necessarily harms the final Nyman target; finite-window and target conversion remain separate gates.