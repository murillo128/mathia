# MI-056 — Deep-band positivity beats the first-row ceiling only after a source-demand exponent threshold

**Evidence level:** exact source-capacity calibration from [FD-261](../../findings/FD-261-deep-band-depletion-needs-superlinear-depth-amplification-to-beat-first-row-ceiling.md), the exact full-grid inverse ceiling of [FD-262](../../findings/FD-262-full-grid-mertens-repair-has-only-linear-log-depth-amplification.md), and the sharp block-replication ledger of [FD-263](../../findings/FD-263-full-grid-repair-demand-obeys-a-sharp-block-replication-ledger.md), combined with the depletion laws of MI-054/MI-055.

Let `beta=log_2(3/2)`. For the scale-adapted positive cushion at divisor depth `D`, FD-260 implies a physical dyadic-band capacity

`P_N(D) << N D^(1-beta)/log N`.

If a source theorem forces negative repair demand of size `N^(theta-o(1)) D^(alpha-o(1))` on that band, with `D=N^(lambda+o(1))`, the positive-capacity ceiling can contradict it only when

`theta + alpha lambda > 1 + (1-beta) lambda`.

A demand merely linear in divisor depth (`alpha=1`) becomes contradictory only for `lambda>(1-theta)/beta`, strictly later than the independent first-row ceiling `lambda<=1-theta`. To make the general deep-band mechanism decisive no later than that first-row scale, one needs `alpha>2-beta=1.415037...` at the same arithmetic-amplitude exponent.

FD-262 closes repeated full-grid divisor inversion as a hidden source of that exponent, and FD-263 identifies the sharper reason. Writing `F_N(q)=Delta R_N(q)-B_q(N)`, exact inversion gives

`2 c_d = sum_(q|d) F_N(q)`

and therefore on `x<d<=2x`

`sum |c_d| <= (1/2) sum_(q<=2x) |F_N(q)| m_x(q)`,

where `m_x(q)=floor(2x/q)-floor(x/q)` is the exact number of copies of forcing coordinate `q` reaching the band. In particular `m_x(q)=1` for `x<q<=2x`: an isolated deep Mertens spike is copied only once. The coarse harmonic form is `sum |c_d| <= x sum |F_N(q)|/q`.

For the canonical rounded full-grid repair, `|Delta R_N(q)|<=2`, so the live arithmetic quantity is the replication-weighted block variation `sum |B_q(N)|m_x(q)`, not the maximum block increment. If a shell `Q=D^(rho+o(1))` contains `K=D^(kappa+o(1))` blocks of size at most `A_N D^(delta+o(1))`, its total contribution is at most

`A_N D^(1-rho+kappa+delta+o(1))`.

Consequently crossing the general FD-260 threshold requires

`kappa + delta - rho > 1-beta = 0.415037...`.

At the deepest scale `Q~D`, this becomes `kappa+delta>2-beta=1.415037...`. Equivalently, if `K/Q` is the density of relevant blocks and `T` their amplitude relative to `A_N`, one needs `(K/Q)T >= D^(1-beta+epsilon-o(1))`. Strong arithmetic forcing must therefore be both amplified and sufficiently populated in the replication measure; a larger isolated maximum is not enough.

This separates arithmetic amplitude, block density and divisor-depth replication. Same-amplitude forcing (`delta=0`) remains at most linear in depth because `kappa<=rho`, irrespective of where a polynomial shell sits. A switched-only repair is genuinely different because its uncontrolled intermediate integer residual increments need not obey the rounded full-grid ledger.

The monotone-response cone remains qualitatively different. If `mu*b>=0`, FD-259 removes the depth factor from the physical capacity ceiling, leaving `O(N/log N)`. Then linear depth accumulation is already exponent-critical at the first-row scale. Proving such a sign structure can matter more than improving the general positive-kernel exponent.

The durable audit is therefore two-stage: compare a proposed source lower bound with the strongest applicable capacity/first-row law, then express its forcing in the exact replication ledger of the repair operator. In the general positive cone, the canonical full-grid route can beat the first-row ceiling only through a genuinely large amplitude-density population of consecutive Mertens blocks, not through inversion depth itself.

**Boundary.** FD-263 is an upper-bound route restriction, not a Mertens theorem. It does not prove that actual consecutive Mertens blocks fail the amplitude-density threshold, does not obstruct arbitrary switched-only repairs, and does not prove monotone response. The exponent inequalities remain strength tests for future source lower bounds, not existence statements.