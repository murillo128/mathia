# MI-076 — Fixed-depth factor lifts cannot amplify the short-shell state exponent

**Evidence level:** exact arithmetic/geometric synthesis from [MC-419](../../findings/MC-419-multiaxis-positive-kernels-can-multiply-bandwidth.md), [MC-420](../../findings/MC-420-support-lattice-rank-controls-stationary-positive-bandwidth.md), [MC-422](../../findings/MC-422-hyperbolic-shell-taxes-factor-axis-bandwidth.md), [MC-423](../../findings/MC-423-exact-product-fibers-have-subpolynomial-tangent-volume.md), and [MC-424](../../findings/MC-424-fixed-depth-factor-lifts-cannot-amplify-shell-state-exponent.md). This is a necessary state-count obstruction, not an analytic cancellation theorem.

For factor depth `d>=2`, let

`S_d(X,Delta)={(u_1,...,u_d) in N^d : X<u_1...u_d<=X+Delta}`.

Grouping tuples by product gives the exact identity

`|S_d(X,Delta)| = sum_(X<n<=X+Delta) d_d(n)`.

For every fixed `d`, `d_d(n)=n^(o(1))`. Hence if `Delta=X^(theta+o(1))` with `0<theta<=1`,

`|S_d(X,Delta)|=X^(theta+o(1))`.

The lower exponent comes already from the states `(n,1,...,1)`, while the upper exponent follows by summing the maximal-order divisor bound across the shell. Therefore **no fixed-depth reparameterization of ordered factor tuples can turn shell width `X^theta` into `X^(theta+delta)` distinct support-preserving arithmetic states for any fixed `delta>0`**. A shear, tilted lattice, curved tangent patch or piecewise chart may avoid the axis-box obstruction of MC-422, but after collisions are quotiented its effective state family still lies inside `S_d(X,Delta)`.

This is stronger than the axis-box bound only in its coordinate invariance. It is weaker analytically: cardinality does not certify stationary translation rank, independent Fourier frequencies or reconstruction by a positive kernel. Those requirements can reduce usable bandwidth further, but the count alone cannot bound oscillatory weights or signed cancellation on the available states.

Growing factor depth has an explicit admission price. In the Norton/Pollack regime `d=o(log X)`, MC-424 gives

`|S_d(X,Delta)| <= (Delta+1) X^((1+o(1)) log d / log log X)`.

If `Delta=X^(theta+o(1))` and a construction needs an additional fixed state-volume exponent `delta>0`, then this route requires

`d >= (log X)^(delta-o(1))`.

Thus constant depth, and even `d=(log X)^(o(1))`, contributes only subpolynomial multiplicity beyond the shell width. Growing depth can become combinatorially relevant only at a corresponding polylogarithmic scale, after which the decomposition, coefficient, source-phase and closure costs still have to be paid.

**Boundary.** The count applies when effective cells are represented by distinct ordered factor tuples that remain inside the short shell. It does not constrain zero-extended shift correlations whose parameter orbit leaves the shell, extra conductor/residue/position labels that genuinely survive quotienting, transformed nonseparable phases, source-dependent weights, or analytic cancellation within the bounded state set. The growing-depth estimate is used only in its stated `d=o(log X)` regime. No Möbius, character-sum, Mertens or RH consequence follows from the count.