# MI-037 — Growing dyadic root differencing has a sublogarithmic random-cost window, not a free escape

**Evidence level:** exact synthesis from [FD-207](../../findings/FD-207-fixed-depth-dyadic-root-differences-remain-rh-equivalent-at-critical-random-cost.md) and [FD-208](../../findings/FD-208-growing-dyadic-root-differencing-has-a-sublogarithmic-critical-random-window.md).

Write `Delta(n)=M(2n)-M(n)`, let `(TF)(n)=F(2n)`, and allow the signed root-difference depth to grow:

`C_q(n)=(T-I)^q Delta(n)`.

FD-207 shows that every **fixed** `q` remains pointwise RH-complete despite removing the literal positive root anchor before squaring. FD-208 prices what happens to the random comparator when `q=q(n)` is no longer fixed.

For the squarefree-Rademacher source the exact second-moment coefficient is

`D_q=sum_(j=0)^q binom(q,j)^2 2^j`,

the central Delannoy number `P_q(3)`, and uniformly in `q`

`E|C_q^f(n)|^2=(6/pi^2)n D_q+O(n^(1/2)D_q)`.

The elementary bounds

`2^((5/2)q-1)/(q+1)^2 <= D_q <= 8^q`

show `log D_q=Theta(q)`. On the root-aligned Farey horizon `H_n=n p_n`, this gives

`E[K_n |C_(q(n))^f(n)|^2]=(6/pi^2+o(1)) H_n D_(q(n))`.

Therefore the signed transform retains a **critical-power** random benchmark `H_n^(1+o(1))` exactly when

`q(n)=o(log n)`,

and retains only a polylogarithmic surcharge exactly in the smaller regime `q(n)=O(log log n)`. The largest dyadic observation horizon used by the transform grows like `H_(2^q n)/H_n=4^(q+o(q))`, so the same sublogarithmic condition is also the threshold for keeping the observation span subpower in `n`.

This turns the vague “let depth grow” escape left by FD-207 into a priced window. Depth comparable with `log n` already pays a genuine power surcharge in the comparator and in the observed scale range. Only `q=o(log n)` can plausibly change the inversion mechanism while preserving the near-critical source-cost regime.

What FD-208 does **not** provide is the corresponding deterministic Möbius theorem. The fixed-depth inversion from FD-207 is not uniform in `q`, but its failure to be uniform is not itself evidence that growing depth escapes RH-completeness. The remaining analytic question is whether one can prove a uniform source-side inversion for some sublogarithmic `q(n)`, or instead exploit the lack of such an inverse through a genuinely collective/nonpointwise estimate.

The concrete frontier is thus an overlap of two constraints: the transform must grow fast enough to defeat the finite-depth destination inverse, yet slowly enough that `D_q` and the dyadic span remain subpower. Any proposed growing-depth mechanism outside `q=o(log n)` has already lost the critical random-cost calibration before Möbius cancellation is addressed.

**Boundary.** The Delannoy calculation is a comparator/cost statement, not a deterministic cancellation result. FD-208 does not prove that any sublogarithmic depth defeats binary-prefix recovery, and it does not classify aggregate inequalities that control many `C_q` jointly rather than pointwise. The random model supplies no evidence for RH beyond calibrating how much signed differencing costs.