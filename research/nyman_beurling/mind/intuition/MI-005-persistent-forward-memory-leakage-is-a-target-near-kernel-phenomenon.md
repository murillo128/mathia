# MI-005 — Stable-tail diagnostics must separate residual memory from finite-depth boundary prediction cost

**Evidence level:** supported by NB-063--NB-080. The continuation, prediction, branching and q-adic information identities are exact; NB-080 supplies an exact matched outer counterexample to interpreting fixed-ratio residual-ledger divergence as a stable-tail signature. No arithmetic criterion closing the Nyman stable tail is established.

NB-074--NB-079 write the uncancelled continuation charge as a refinement ledger and remove the universal common prediction mode. At each exact q-adic refinement there are nonnegative charges `G`, `P`, and `S` with

`ell=G+P`, `c=G+S`,

so

`J_m=J_0+sum_(r<=m)(P_r-S_r)`.

A nonzero stable tail forces this residual sum to diverge on every fixed-ratio refinement ray, while one ray with `P_r<=S_r+e_r` and summable `e_r` is sufficient to kill the stable tail. That one-way criterion remains exact.

NB-080 shows why the converse intuition fails. For every branching factor `m>=2` and `0<rho<1`, the control

`D_j=(I-rho V_m)e_j`

comes from a boundedly invertible outer filter, has zero stable tail, and has a uniformly well-conditioned Gram. Nevertheless, on every exact refinement ray with fixed ratio `(N+1)/R`, a positive-density set of prefix innovations receives only a fixed number `L` of descendant generations. Each such innovation retains the same strictly positive finite-depth prediction penalty, so

`J_(R_r,N_r) >= kappa R_r-O(1)`

and therefore `sum(P-S)->+infinity` despite `T_infinity={0}`.

The fixed-ratio ledger is thus contaminated by an **extensive but benign boundary layer**: ordinary outer continuation that disappears with sufficiently deep future information but not when relative future depth is frozen. Divergence of `P-S` can measure this horizon artifact rather than persistent target-near-kernel memory.

The stable-tail problem must therefore change scale or normalization. A more faithful criterion should let descendant depth grow, subtract the outer finite-depth prediction volume, or isolate a residual mode whose cost remains after arbitrarily deep screening. Arithmetic effort spent proving boundedness of the raw fixed-ratio ledger is proving a condition substantially stronger than tail absence.

**Boundary.** NB-080 does not invalidate NB-079's sufficient criterion and does not show the arithmetic Nyman source has the same boundary-layer asymptotics. It proves only that branching, outerness, zero stable tail and excellent global conditioning do not control the fixed-ratio residual ledger in the desired direction.