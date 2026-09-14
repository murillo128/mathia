# MI-024 — Arithmetic-image blind exclusion is directional leverage, not a uniform decoder norm

**Evidence level:** exact reduction and certificate from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md). No theorem is claimed that the required rank/leverage alternative actually holds for the arithmetic shell matrix.

Let `A` be the degree-`m` feature matrix of the actual fixed-weight arithmetic shell and let `v=1_Z` be the virtual blind feature row. Instead of constructing a scalar decoder that is uniformly sharp on the full Boolean cube, optimize only on the arithmetic image:

`C = inf_{v^* a=1} ||A a||_2^2`.

Every blind row contributes exactly one to this energy, so the blind count satisfies `A_y(t)<=C`; in particular `C<1` is an exact blind-exclusion certificate. This uses the same degree-`m` source features as the earlier flat Christoffel detector and can only improve that detector.

The dual quantity is the minimum signed shell-synthesis cost

`Lambda = inf{ ||c||_2^2 : A^* c = v }`,

with `C=1/Lambda`. If `v` is outside `ran(A^*)`, then a kernel vector gives a degree-`m` polynomial that vanishes on every actual shell row and equals one at the blind endpoint, so `C=0`. If `v` lies in the row span, then `Lambda=v^*(A^*A)^+v` and blindness is excluded once `Lambda>1`.

Thus the surviving low-depth question is **directional endpoint geometry**: the orientation of the blind vector relative to the arithmetic row span, and conditional on membership, its inverse-Gram leverage. A wide matrix or large kernel is not enough; the kernel must have a component in the blind direction.

Generic coefficient-uniform large-sieve/operator-norm control cannot cross this threshold. The row norm forces any uniform bound `||Aa||_2^2<=D||a||_2^2` to have `D>=Z`, while the dual argument yields only `Lambda>=Z/D<=1`. Such a theorem can neither force `Lambda>1` nor prove the rank-increment alternative.

This identifies precisely what the arithmetic-image escape left by MC-280 would need: signed cancellation across actual target rows before scalarization, strong enough to separate the virtual blind endpoint in one distinguished direction. It is not another full-cube approximation problem.

**Boundary.** MC-281 gives a rigorous certificate and exact variational reformulation, not an unconditional estimate of `Lambda` or proof that `v` leaves the arithmetic row span. Determining that directional geometry may encode the same exceptional-row arithmetic one is trying to control.
