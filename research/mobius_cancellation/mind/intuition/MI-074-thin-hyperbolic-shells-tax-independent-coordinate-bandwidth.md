# MI-074 — Thin hyperbolic shells tax independent coordinate bandwidth

**Evidence level:** exact geometric synthesis from [MC-419](../../findings/MC-419-multiaxis-positive-kernels-can-multiply-bandwidth.md), [MC-420](../../findings/MC-420-support-lattice-rank-controls-stationary-positive-bandwidth.md), [MC-421](../../findings/MC-421-iterated-vdc-creates-source-free-codimension-one-faces.md), [MC-422](../../findings/MC-422-hyperbolic-shell-taxes-factor-axis-bandwidth.md), and the coordinate-free state-count refinement [MC-424](../../findings/MC-424-fixed-depth-factor-lifts-cannot-amplify-shell-state-exponent.md). MC-422 is the sharper support-geometry obstruction for axis-aligned positive boxes; MC-424 separately limits the total number of fixed-depth factor states in the whole shell.

Suppose a physical factor tuple `u=(u_1,...,u_d)` is confined to the thin product shell `X < prod_j u_j <= X+Delta`. If a full positive coordinate box `prod_j[U_j,U_j+B_j]` lies inside the shell, MC-422 proves

`sum_j B_j/U_j <= Delta/P_0`,

and hence

`prod_j B_j <= Delta^d/(d^d P_0^(d-1))`,

where `P_0=prod_j U_j`. At the natural regime `P_0 asymp X`, a growing full `d`-axis box is possible only when `Delta=X^theta` satisfies `theta>1-1/d`.

This converts the abstract rank requirement of MC-419--MC-420 into a physical bandwidth budget. Formal factor count is not the same as usable independent stationary translation volume. A thin hyperbolic shell may expose many algebraic coordinates while allowing only a tiny axis-aligned box in those coordinates; the shell normal consumes the sum of the relative bandwidths.

At the currently relevant `theta` near `0.55`, two positive coordinate axes can have at most `X^0.10` product bandwidth, while three axes cannot all have growing integer width. Thus a proposed tensor Fejer gain must certify not merely rank two or rank three support, but enough **physically admissible joint bandwidth inside the shell** to beat the one-axis floor after all closure faces are paid.

Product-preserving or mixed-sign tangent directions in logarithmic coordinates avoid the first-order shell-normal cost, and tilted lattices need not contain a full axis box, so MC-422 alone does not classify them. MC-424 closes the corresponding *state-count* escape at fixed factor depth: even after allowing arbitrary shears, curved patches or piecewise tangent parameterizations, all distinct ordered factor tuples in a shell of width `X^(theta+o(1))` number only `X^(theta+o(1))`. Such coordinates can matter only through analytic organization of those states, extra source variables not determined by the tuple, boundary-crossing correlations, or growing factor depth—not by manufacturing extra polynomial state volume.

**Boundary.** The axis-box inequalities above remain specific to full positive axis-aligned boxes. MC-424 supplies only a cardinality ceiling for arbitrary fixed-depth support-preserving state families; it does not prove those states form a stationary translation action, bound oscillatory cancellation in their weights, or constrain parameter families whose correlations are not represented by distinct states inside the shell.