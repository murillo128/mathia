# MI-042 — Subcritical Euler-jet depth does not change the leading KV sign-complexity exponent

**Evidence level:** exact synthesis from [RE-175](../../findings/RE-175-euler-boundary-jets-detect-delayed-prime-compensation.md), [RE-176](../../findings/RE-176-two-jet-repair-forces-kv-tail-inside-half-log-horizon.md), [RE-177](../../findings/RE-177-finite-sign-complexity-prices-remote-two-jet-repair.md), and [RE-178](../../findings/RE-178-subcritical-euler-jet-order-is-exponent-neutral-for-kv-tail-capacity.md).

RE-175--RE-177 show that one additional Euler boundary slope turns the delayed Robin compensator into a quantitative sign-phase problem. A tail beginning at `Y` with `M` sign-constant phases has first-slope capacity only

`(M+ell_KV(Y)) exp(-b V(Y))`,

so exact Mertens plus first-slope matching gives the leading placement law `bV(Y)<=(1/2+kappa+o(1))log p` when `M=p^(kappa+o(1))`.

RE-178 tests whether simply matching more right-boundary Euler derivatives strengthens that exponent. For the `j`-th jet and `j=o(V(Y))`, phasewise Abel summation gives

`sum_(q>=Y)|c_q||J_j(q)| << (log Y)^(j-1)(M+ell_KV(Y)) exp(-bV(Y))`.

Each derivative adds one logarithmic location factor but **does not change the linear dependence on the number of sign phases**. At the moving RE-177 horizon `V(Y)=Theta(log p)`, after normalizing by the selector-scale factor `(log p)^(j-1)`, the extra leverage is only

`(log Y/log p)^(j-1)`.

For every fixed `j`, and even for

`j=o(log p/log log p)`,

this factor is only `p^(o(1))`. Therefore a scalar residual debt of the natural normalized size yields the same leading polynomial tradeoff as the first slope. Repeating the same scalar KV-capacity argument with finitely many or subcritical growing jets cannot create a superlinear leading sign-complexity tariff.

The first jet order at which raw logarithmic leverage can alter the polynomial exponent is the crossover

`j_cap(p) asymp log p/log log p`.

This is only a capacity threshold. It does not say that Robin supplies that many jets, that their residual debts are independent, or that an ordinary-prime control can match them. Below that scale, any real improvement has to use **joint geometry among several moments**, integer/prime granularity, or another source constraint rather than scalarizing each jet separately.

The reusable lesson is that adding observables does not automatically strengthen an obstruction when their capacity estimates factor through the same one-dimensional envelope. One must ask whether the family creates genuinely joint constraints or merely multiplies each existing scalar workload by predictable logarithmic weights.

**Boundary.** Euler boundary jets remain extra source information not derived from Robin's selector. RE-178 is a tail-capacity upper bound and does not prove a corresponding independent debt for each higher jet. It also assumes finite sign complexity and the subcritical order regime; infinite oscillation or jet order at/above the crossover needs different control.