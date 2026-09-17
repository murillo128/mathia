# MI-043 — KV-weighted reset budget replaces raw sign-phase count

**Evidence level:** exact synthesis from [RE-175](../../findings/RE-175-euler-boundary-jets-detect-remote-compensators.md), [RE-177](../../findings/RE-177-finite-sign-complexity-cannot-delay-two-jet-repair-past-the-kv-horizon.md), [RE-178](../../findings/RE-178-subcritical-euler-jets-do-not-improve-kv-sign-complexity-exponent.md), and [RE-179](../../findings/RE-179-two-jet-matching-forces-a-kv-weighted-reset-budget.md).

RE-177 prices delayed two-jet repair by the number of sign-constant phases beyond a cutoff. RE-179 identifies the invariant hidden inside that count. A reset beginning at prime scale `z` is worth only the local KV allowance `exp(-bV(z))`, so the natural complexity is

`R_b^-(Y)=sum_j exp(-bV(z_j))`,

not the raw number of sign changes.

Two exact Euler coordinates make this budget coercive. After centering the first-slope kernel at the deletion packet's Mertens barycenter, exact value and slope matching force a Robin-scale amount of negative centered repair. If only `N_p^-(Y)` of that debt has appeared before `Y`, then the tail satisfies

`(delta_(lambda,p)d_p-N_p^-(Y))_+ << R_b^-(Y)+ell_KV(Y)exp(-bV(Y))`.

Thus infinitely many alternations can still be ineffective: if their starting scales drift rapidly enough, their weighted budget may converge and become too small to pay the debt. Conversely, a small weighted tail forces substantial repair to occur near the selector. The finite-phase law of RE-177 follows by the crude bound `R_b^-(Y)<=M_-(Y)exp(-bV(Y))`.

The conceptual gain is that **oscillation complexity must be measured in the same source geometry that limits transport**. A sign reset is not a unit-cost combinatorial event; its leverage decays with location. This is analogous to replacing raw rank or feature count by a conditioned resource that reflects how much of the destination can still be moved from that scale.

RE-178 and RE-179 together also narrow the next route. Shallow scalar jet depth does not improve the leading exponent, and raw infinite oscillation does not evade it. A real strengthening must constrain early repair, force a large weighted reset budget from genuine arithmetic structure, or use joint/non-scalar source geometry ignored by the phasewise KV estimate.

**Boundary.** The first Euler slope is still additional source information rather than a consequence of Robin's criterion. RE-179 deliberately leaves early interlaced repair and divergent weighted reset budget open. The weighted-reset principle prices a matched-control escape; it does not close Robin's inequality.