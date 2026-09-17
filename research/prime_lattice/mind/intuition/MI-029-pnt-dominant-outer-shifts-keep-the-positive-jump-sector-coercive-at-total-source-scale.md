# MI-029 — PNT-dominant outer shifts keep the positive jump sector coercive at total source scale

**Evidence level:** exact/operator synthesis from [PL-337](../../findings/PL-337-positive-jump-decomposition-for-active-prime-shifts.md), [PL-338](../../findings/PL-338-all-prime-activation-flatness.md), and [PL-339](../../findings/PL-339-prime-shift-path-gap-global-coercivity.md), with the prime number theorem used only for the source-mass asymptotic.

For the zero-exterior compressed translation `S_h` on the fixed interval, put `D_h=2I-S_h-S_h*`. PL-339 identifies the exact path-chain spectrum:

`||S_h+S_h*|| = 2 cos(pi/(ceil(2/h)+1))`,

so `D_h` has a positive gap for every active `0<h<=2`. In the outer half-window `1<=h<2` the gap is uniformly at least one.

For prime-power lags `h_n(a)=log n/a`, the outer window `a<=log n<2a` therefore contributes

`J_a >= W_a^out I`,

where `J_a=sum Lambda(n)/sqrt(n) D_(h_n(a))`. The weighted PNT gives `W_a^out~W_a~2e^a`, hence

`J_a >= (1-o(1)) W_a I`.

The favorable jump sector does not become soft as more source channels activate. Almost all weighted von-Mangoldt mass lies in a shell where every individual compressed shift already has a unit Poincare gap.

This closes one previously plausible many-channel failure mode, but it does not make the prime block positive. The exact decomposition remains

`P_a = J_a - 2W_a I`,

and PL-339 only improves the norm scale to `||P_a|| <= (1+o(1))W_a`. The scalar compensation is still negative at the same exponential source scale. Global branch ordering, boundary-trace noncollapse and interaction with the completion remain separate obligations.

The reusable point is that **a scalable positive bulk can be completely controlled while the destination sign remains in a thinner compensation/branch variable**. Once the bulk coercivity is PNT-scale, further estimates proving that `J_a` stays positive attack a solved resource. The next information must distinguish rational-prime structure beyond the universal PNT mass shell or control how the compensation and completion act on the selected branch.

**Boundary.** The path-gap theorem is source-agnostic once positive weights and lag geometry are fixed, and the leading PNT mass asymptotic is reproducible by matched generalized-prime sources. No rational-prime discriminator, global eigenbranch persistence, completed-Weil positivity or RH implication follows.