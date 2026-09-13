# MI-015 — Fixed-multiplicity volume is controlled by terminal resolution depth after optimal band placement

**Evidence level:** exact for the fixed-multiplicity finite-window Nyman volume by [NB-103](../../findings/NB-103-confluent-nyman-volume-is-curvature-blind-and-controlled-by-radial-depth.md)--[NB-105](../../findings/NB-105-terminal-budget-makes-the-ordinate-scale-the-optimal-band-start.md), contrasted with the three-state conditioning law of NB-098--NB-102. No growing-multiplicity, genuine repeated-zero or target-conversion theorem is claimed.

NB-102 shows that local three-state conditioning is controlled by dimensionless Menger curvature. NB-103 proves that fixed-multiplicity **normalized determinant volume** is different: collision Vandermonde factors cancel in confluence, and for a fixed interior center the large-window coefficient depends only on multiplicity `d` and radial depth

`x=2 Re(lambda_*) log q`

through the Laguerre determinant `Delta_d(x)`. Curvature is therefore a conditioning currency, not a fixed-multiplicity volume currency.

NB-104 identifies the boundary resolution cost when `a=Re(lambda_*)->0`. A finite logarithmic cell cannot resolve the Mellin phase `t^(-i Gamma)` until the cell index reaches the ordinate scale. With

`x=2a log q`, `y=2a log^+(|Gamma|/m)`,

the confluent volume tends to `e^(-d y) Delta_d(x-y)` for `0<=y<x` and to zero for `y>=x`. Nominal radial depth therefore overstates the usable finite-window resource when the band starts below the ordinate-resolution scale.

NB-105 shows that moving the start is not a free repair once the finite section has a terminal natural-index budget `B`. Put `G=max(1,|Gamma|)`,

`L=2a log(B/G)`, `s=2a log(m/G)`, `tau=2a log(B/(mq))`.

The exact limiting placement profile is

`F_(d,L)(s,tau)=e^(ds) Delta_d(L-tau)` for `s<=0`,

and

`F_(d,L)(s,tau)=Delta_d(L-s-tau)` for `0<=s<L-tau`,

with zero outside the resolved interval. Strict monotonicity of `Delta_d` makes the optimum unique at `s=0`, `tau=0`. Thus the best finite window starts at the ordinate scale on the radial `1/a` scale and uses the terminal budget completely.

The separate NB-104 currencies collapse after optimization into one **terminal resolution depth**:

`L=2(beta-1/2) log(B/|gamma|)`

for an off-critical zero `rho=beta+i gamma`. Moving the band above `|gamma|` removes delay but shortens the available radial interval one-for-one; moving below it pays the factor `e^(ds)`. For any fixed retained volume fraction `eta`, the budget must satisfy

`B >= |gamma| exp((Delta_d^(-1)(eta)+o(1))/(2(beta-1/2)))`.

The reusable distinction is therefore sharper than “radial depth versus ordinate delay.” **At fixed terminal scale, band placement can be optimized exactly, and the irreducible resource is depth measured relative to the source ordinate.** This closes a representation-tuning loophole but still does not convert determinant volume into Nyman target distance.

The next theorem must decide whether actual finite Nyman sections can supply enough terminal resolution depth for a hypothetical off-critical packet and whether the resulting `Delta_d(L)` volume is load-bearing for the target norm or a dual certificate. Growing multiplicity, Jordan-state geometry and diagonal normalization remain separate resources.

**Boundary.** The law is fixed-multiplicity and concerns analytic confluence of the finite-window determinant, not a causal Jordan state of a repeated zeta zero. The terminal budget `B` is essential: without fixing it there is no meaningful placement optimization. Equality at `s=0` is a radial-scale statement and does not require `m/|Gamma|->1` multiplicatively.
