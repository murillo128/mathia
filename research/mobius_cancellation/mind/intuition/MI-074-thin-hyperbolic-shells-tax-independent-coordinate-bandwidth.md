# MI-074 — Thin hyperbolic shells tax independent coordinate bandwidth

**Evidence level:** exact geometric synthesis from [MC-419](../../findings/MC-419-multiaxis-positive-kernels-can-multiply-bandwidth.md), [MC-420](../../findings/MC-420-support-lattice-rank-controls-stationary-positive-bandwidth.md), [MC-421](../../findings/MC-421-iterated-vdc-creates-source-free-codimension-one-faces.md), and [MC-422](../../findings/MC-422-hyperbolic-shell-taxes-factor-axis-bandwidth.md). MC-422 is a support-geometry obstruction for axis-aligned positive boxes; it does not classify tilted or multiplicative tangent coordinates.

Suppose a physical factor tuple `u=(u_1,...,u_d)` is confined to the thin product shell `X < prod_j u_j <= X+Delta`. If a full positive coordinate box `prod_j[U_j,U_j+B_j]` lies inside the shell, MC-422 proves

`sum_j B_j/U_j <= Delta/P_0`,

and hence

`prod_j B_j <= Delta^d/(d^d P_0^(d-1))`,

where `P_0=prod_j U_j`. At the natural regime `P_0 asymp X`, a growing full `d`-axis box is possible only when `Delta=X^theta` satisfies `theta>1-1/d`.

This converts the abstract rank requirement of MC-419--MC-420 into a physical bandwidth budget. Formal factor count is not the same as usable independent stationary translation volume. A thin hyperbolic shell may expose many algebraic coordinates while allowing only a tiny axis-aligned box in those coordinates; the shell normal consumes the sum of the relative bandwidths.

At the currently relevant `theta` near `0.55`, two positive coordinate axes can have at most `X^0.10` product bandwidth, while three axes cannot all have growing integer width. Thus a proposed tensor Fejer gain must certify not merely rank two or rank three support, but enough **physically admissible joint bandwidth inside the shell** to beat the one-axis floor after all closure faces are paid.

The geometric escape is also explicit. Product-preserving or mixed-sign tangent directions in logarithmic coordinates can avoid the first-order shell-normal cost, as can tilted lattices not containing a full axis box. Those possibilities are not established arithmetic resources: they still require stationary source phases, localization, reconstruction and positive-closure control on the actual source.

**Boundary.** The bound is for full positive axis-aligned boxes in a multiplicative shell. It does not rule out sheared/tangent lattices, nonlinear coordinates, sparse sets with large cardinality, or arithmetic cancellation along product-preserving directions. Such mechanisms must be analyzed in their own geometry rather than credited by ambient factor dimension.