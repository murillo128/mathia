# MI-015 — Finite-window confluent volume is curvature-blind but boundary resolution spends ordinate delay

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman volume by [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md) and its boundary double-scaling refinement [NB-104](../../findings/NB-104-boundary-confluence-has-an-ordinate-delay-laguerre-law.md), contrasted with the three-state conditioning law of NB-098--NB-102. No growing-multiplicity, genuine repeated-zero or target-conversion theorem is claimed.

NB-102 shows that local three-state conditioning is controlled by dimensionless Menger curvature. NB-103 proves that fixed-multiplicity **normalized determinant volume** is different: collision Vandermonde factors cancel in confluence, and for a fixed interior center the large-window coefficient depends only on multiplicity `d` and radial depth

`x=2 Re(lambda_*) log q`

through the Laguerre determinant `Delta_d(x)`. Curvature is therefore a conditioning currency, not a fixed-multiplicity volume currency.

NB-104 identifies the missing boundary variable when `a=Re(lambda_*)->0`. The continuum half-line Gram is still exactly invariant under common vertical translation, but a finite logarithmic cell cannot resolve the Mellin phase `t^(-i Gamma)` until the cell index reaches the ordinate scale. Define

`x=2a log q`,

`y=2a log^+(|Gamma|/m)`.

For fixed `d`, if `x_j->x` and `y_j->y`, the normalized confluent volume has the exact limit

`V_conf -> e^(-d y) Delta_d(x-y)` for `0<=y<x`,

and tends to `0` for `y>=x`.

Thus the finite window has a **dead radial depth** `y` before the arithmetic cells resolve the oscillation. The NB-103 law `Delta_d(x)` is boundary-uniform only when `2a log^+(|Gamma|/m)->0`. When `m<|Gamma|<mq`, the effective surviving depth is

`2a log(mq/|Gamma|)`,

not the nominal `2a log q`.

This is a discretization/synchronization effect rather than a contradiction with height-gauge invariance of the continuum geometry. Absolute ordinate re-enters only through the ratio between oscillation scale and finite-cell resolution. Moving the band start `m` can remove the delay, so `y` is not an intrinsic zero invariant by itself; it is a source-to-representation coupling.

The source-facing question must therefore specify which destination quantity is load-bearing **and** whether the chosen finite window resolves the source ordinate. Stable inversion may require curvature control; fixed-cardinality volume requires remaining radial depth after the ordinate delay; neither one implies the other.

**Boundary.** The law is fixed-multiplicity and concerns analytic confluence of the finite-window determinant, not a causal Jordan state of a repeated zeta zero. It does not decide how to choose `m,q` in a target-optimal Nyman approximation or whether the final target distance consumes determinant volume at all.