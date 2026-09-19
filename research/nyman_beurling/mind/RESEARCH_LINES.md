# Nyman--Beurling research lines

This file records current mathematical questions for the Nyman--Beurling line. It is a mutable synthesis, not a task queue or history.

## Control the horizontally marked microlocal Landau--Gonek remainder at the Ford transition

**Linked intuition:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`.

NB-230--NB-233 show that population-only control, global pair statistics and unweighted local phase equidistribution do not determine the carrier-width Ford transition. NB-234 identifies the exact nonlinear depth mark and shows that a slowly growing hierarchy of profiled depth--phase moments reconstructs it with factorial accuracy, while every fixed finite hierarchy remains blind in a matched Bellotti-compatible packet.

NB-235 changes representation from abstract growing moments to a classical zeta object. On the critical layer, the unresolved coefficient is, up to `o(1)`, a horizontally truncated smooth Landau zero sum

`x^(-s_X) sum_{|X(1-beta)-log J|<=C} m(rho) x^rho F(H(gamma-t))`.

Because the logarithmic shell profile has zero integral, the ordinary prime-power Landau diagonal is annihilated. But feeding the classical global cumulative Landau--Gonek formula into this microscopic weight by bounded-variation smoothing gives no shrinking factor from the `1/H` window; its generic remainder yields only an `O(Q)` normalized guarantee, far from `o(1)`. The missing theorem is therefore a genuinely microlocal, horizontally sensitive remainder estimate or an equivalent zeta-specific relation coupling depth and ordinate phase before absolute values destroy the cancellation.

The live source question is now sharper than “prove enough growing moments.” Those moments are one sufficient surrogate for the exact local remainder. A direct theorem for the remainder, or another identity that controls the same coefficient with actual zeta structure, would attack the load-bearing object without introducing an intermediate hierarchy.

## Keep carrier width, horizontal depth, microscopic ordinate scale, diagonal cancellation and global remainder separate

NB-235 removes one tempting shortcut: the ordinary Landau prime-power main term is not the desired arithmetic resource because the shell localization kills it. It also shows that a strong global cumulative formula need not survive localization at the scale consumed by the destination; total variation can price the cumulative error at full strength.

Future work should preserve the coupled Ford geometry explicitly: the ordinate window, the horizontal layer `X(1-beta)-log J`, the shell profile and the final `o(1)` normalization. A theorem that drops the horizontal mark or pays a global sup-norm remainder has changed the problem. The decisive progress would be local cancellation in this exact marked sum, not another population estimate or a reformulation of the global explicit formula.