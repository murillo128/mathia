# MI-056 — Deep-band positivity beats the first-row ceiling only after a source-demand exponent threshold

**Evidence level:** exact source-capacity calibration from [FD-261](../../findings/FD-261-deep-band-depletion-needs-superlinear-depth-amplification-to-beat-first-row-ceiling.md), now combined with the exact full-grid inverse ceiling of [FD-262](../../findings/FD-262-full-grid-mertens-repair-has-only-linear-log-depth-amplification.md), and the depletion laws of MI-054/MI-055.

Let `beta=log_2(3/2)`. For the scale-adapted positive cushion at divisor depth `D`, FD-260 implies a physical dyadic-band capacity

`P_N(D) << N D^(1-beta)/log N`.

If a source theorem forces negative repair demand of size `N^(theta-o(1)) D^(alpha-o(1))` on that band, with `D=N^(lambda+o(1))`, the positive-capacity ceiling can contradict it only when

`theta + alpha lambda > 1 + (1-beta) lambda`.

A demand merely linear in divisor depth (`alpha=1`) becomes contradictory only for `lambda>(1-theta)/beta`, which is strictly later than the independent first-row ceiling `lambda<=1-theta`. To make the general deep-band mechanism decisive no later than that first-row scale, one needs `alpha>2-beta=1.415037...` at the same arithmetic-amplitude exponent.

FD-262 now closes the canonical full-grid divisor inverse as a source of that missing exponent. If `R_N(m)` is the repaired full-grid residual and `B_q(N)=M(qN)-M((q-1)N)`, exact Möbius inversion gives

`2 c_d = sum_(q|d) (Delta R_N(q)-B_q(N))`.

Consequently a dyadic band `x<d<=2x` has total repair mass at most

`(B_N(2x)+E_N(2x)) x (1+log(2x))`,

where `B_N(T)=max_(q<=T)|B_q(N)|` and `E_N(T)=max_(q<=T)|Delta R_N(q)|`. For the FD-225 rounded full-grid flattening `E_N=O(1)`. Thus, after its own block-Mertens forcing amplitude is factored out, the canonical repair has only `D log D=D^(1+o(1))` depth amplification. It cannot supply the `alpha>2-beta` mechanism required by the general FD-260 cone.

This separates arithmetic amplitude from divisor-depth accumulation. Larger block-Mertens forcing at deep multiples may increase the `N`-amplitude exponent `theta`, but repeated full-grid inversion itself contributes only linear-log depth. A switched-only repair is genuinely different because its unconstrained intermediate integer rows can have large `Delta R_N(q)`; FD-262 does not bound that class.

The monotone-response cone remains qualitatively different. If the additional condition `mu*b>=0` is available, FD-259 removes the depth factor from the physical capacity ceiling, leaving `O(N/log N)`. Then linear depth accumulation is already exponent-critical at the first-row scale. Proving such a sign structure can therefore matter more than improving the general positive-kernel exponent.

The durable audit is to compare a proposed source lower bound with the strongest applicable capacity law **and with the exact inverse structure that generates the repair**. In the general positive cone, the canonical full-grid correction is now ruled out as the missing superlinear depth resource. A surviving route must instead obtain stronger deep arithmetic forcing, leave the full-grid-flattening class in a way that materially changes intermediate residual increments, or prove a structural upgrade such as monotone divisor response.

**Boundary.** FD-262 is an upper bound for full-grid repairs controlled through all integer-multiple residual increments. It does not obstruct arbitrary switched-only repairs, does not prove monotone response, and does not invalidate the existing subpolynomial-depth construction. The exponent inequalities remain strength tests for future source lower bounds, not existence statements.