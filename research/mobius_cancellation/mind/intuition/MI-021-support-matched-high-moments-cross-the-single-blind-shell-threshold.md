# MI-021 — Endpoint-optimal low-support detection leaves only arithmetic control of the Legendre sign image

**Evidence level:** exact for the support threshold and basis reductions through [MC-264](../../findings/MC-264-support-matched-high-moment-blind-threshold.md), [MC-265](../../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md), [MC-266](../../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md), [MC-267](../../findings/MC-267-krawtchouk-source-hierarchy-amplitude-duality.md), and for the endpoint-optimal positive detector through [MC-268](../../findings/MC-268-christoffel-endpoint-detector.md). The required arithmetic estimate is still open.

Let `b_y(T)` be the Hamming weight of negative lower-prime Legendre signs for a shell subset `T`; a blind relation is exactly the endpoint event `b_y(T)=0`. MC-267 shows that the support layers `H_s` are the Krawtchouk transform of the empirical histogram of `b_y(T)`. Universal Krawtchouk identities therefore reorganize the same scalar distribution and do not supply arithmetic cancellation.

MC-268 corrects the detector used at this boundary. Among degree-`m` polynomials with `P(0)=1`, the Christoffel extremal polynomial

`P_m(b)=Z_m(k)^(-1) sum_(s=0)^m K_s(b;k)`, with `Z_m(k)=sum_(s=0)^m binom(k,s)`,

minimizes binomial `L^2` mass and satisfies

`sum_b 2^(-k) binom(k,b) P_m(b)^2 = 1/Z_m(k)`.

Because `P_m^2` has degree `2m`, its actual shell average is an explicit linear combination of `H_0,...,H_(2m)`. No new information is added, but the available low-support information is combined in the endpoint-optimal positive way instead of through the monomial `B^(2m)`.

At the live support `t~(log log y)/(log 2)`, degree `2t` already reaches the natural one-blind-atom scale: `binom(N_y,t)/Z_t(k_y)=1-2 log log y/log y+o(log log y/log y)`. Thus the earlier need for `m=t+1` was a penalty of the monomial detector, not an intrinsic resolution limit. Keeping `m=t+1` gives much more slack: the baseline is `(t+1)/k_y`, improving the monomial scale by order `log y/sqrt(log log y)`.

The remaining theorem is consequently very specific. Prove an arithmetic comparison for the Christoffel-weighted combination of support layers—or a still stronger source-specific positive certificate—at a loss small enough to beat `binom(N_y,t)/Z_m(k_y)`. At `m=t`, the required relative loss is extremely sharp; at `m=t+1`, losses as large as `o(k_y/(t+1))` are compatible with exclusion.

**Boundary.** MC-268 excludes no blind relation. Christoffel optimality is classical for the binomial/Krawtchouk measure and cannot replace arithmetic information about the actual Legendre sign image. It only identifies the least wasteful positive use of the support-depth budget already available.