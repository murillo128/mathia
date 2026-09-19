# MI-037 — Growing dyadic root differencing has a sublogarithmic cost window, but common-depth control there remains RH-complete

**Evidence level:** exact synthesis from [FD-207](../../findings/FD-207-fixed-depth-dyadic-root-differences-remain-rh-equivalent-at-critical-random-cost.md), [FD-208](../../findings/FD-208-growing-dyadic-root-differencing-has-a-sublogarithmic-critical-random-window.md), and [FD-209](../../findings/FD-209-common-sublogarithmic-dyadic-depth-remains-rh-complete-on-scale-windows.md).

Write `Delta(n)=M(2n)-M(n)`, let `(TF)(n)=F(2n)`, and allow the signed root-difference depth to grow:

`C_q(n)=(T-I)^q Delta(n)`.

FD-207 shows that every **fixed** `q` remains pointwise RH-complete despite removing the literal positive root anchor before squaring. FD-208 prices what happens to the random comparator when `q=q(n)` is no longer fixed.

For the squarefree-Rademacher source the exact second-moment coefficient is

`D_q=sum_(j=0)^q binom(q,j)^2 2^j`,

the central Delannoy number `P_q(3)`, with `log D_q=Theta(q)`. On the root-aligned Farey horizon `H_n=n p_n`, the signed transform retains a **critical-power** random benchmark `H_n^(1+o(1))` exactly when

`q(n)=o(log n)`,

and only a polylogarithmic surcharge in the smaller regime `q(n)=O(log log n)`. The largest dyadic observation horizon used by the transform grows like `4^(q+o(q))`, so the same sublogarithmic condition keeps the observation span subpower.

FD-209 closes the first hoped-for escape inside exactly that window. Let a **common**, source-independent depth `q=q(X)=o(log X)` be used throughout the scale window `sqrt(X)/2 <= n <= X`. Then the critical estimate

`|C_(q(X))(n)| <<_epsilon X^epsilon n^(1/2)`

on that window is equivalent to RH. Growing depth does not lower the theorem surface as long as one depth is controlled coherently across the binary ancestors needed for inversion.

The inverse is explicit. If `F_s=(T-I)^s M` and `Q=q+1`, binary-prefix reconstruction uses negative-binomial Green weights `binom(t-1,Q-1)`. Their square-root-weighted total amplification is `(1+sqrt(2))^Q`; all initial-level and odd-step error terms have only `exp(o(log X))` mass when `Q=o(log X)`. Thus throughout the same sublogarithmic regime where the Delannoy comparator cost remains subpower, the **common-depth physical inverse also remains subpower**.

This removes “the inversion constant grows with `q`” as a mechanism. The remaining escape is more specific: the depth must vary with the evaluation scale so that no single `q(X)` controls an entire binary-prefix window, or the proof must exploit a collective signed relation across depths/root edges without first producing a common-depth pointwise square-root estimate.

The reusable lesson is that transform complexity has to be priced on **both sides**. FD-208 gives the forward/random tariff `D_q=exp(Theta(q))`; FD-209 gives the inverse tariff `(1+sqrt(2))^q` plus subpower floor errors. Both are still subpower for `q=o(log X)`. A growing signed transform becomes potentially new only when its variation across scales destroys the coherent inverse, not merely because its formal depth tends to infinity.

**Boundary.** FD-209 does not classify diagonal estimates where only `C_(q(n))(n)` is known and `q(n)` varies along the binary ancestor chain, nor collective inequalities that never imply one common-depth pointwise bound on a square-root window. The Delannoy and Green-kernel calculations are cost/inversion statements, not deterministic Möbius cancellation results by themselves.
