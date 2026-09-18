# MI-053 — Complementary harmonic and analytic-germ estimates make both order-five tails effective

**Evidence level:** exact synthesis from [AF-408](../../findings/AF-408-order-five-euler-failure-is-confined-to-compact-log-scale.md), [AF-409](../../findings/AF-409-order-five-euler-gate-explicit-right-tail.md), and [AF-410](../../findings/AF-410-order-five-euler-gate-explicit-left-tail.md). The Toda/Hankel reduction is classical; the Mathia content is the explicit Euler-log tail control.

For the Euler-log profile `f(t)=-log(1-exp(-e^t))`, order five is controlled by the scalar Toda gate `A_4(t)=-(log H_4(t))''`. AF-408 proved eventual positivity in both tails. AF-409 makes the right tail effective: with `x=e^t`, the first harmonic gives an exactly invertible `4 x 4` Hankel reference matrix and all higher harmonics are exponentially small, yielding

`A_4(t)>4e^t-3>0`

whenever `e^t>=50`, in particular for every `t>=4`.

AF-410 closes the left tail by a different mechanism. Write `x=e^t` and `u=-t`. The singular logarithmic piece separates as `f(t)=u+h(x)` with `h` analytic at `x=0`. Multilinearity then makes the relevant determinant affine in the unbounded variable,

`H_4(t)=u a(x)+b(x)`,

and the curvature numerator `N_4=(H_4')^2-H_4H_4''` becomes a quadratic polynomial in `u` whose coefficients are analytic germs in `x`. Explicit coefficient and Cauchy-remainder bounds show that the exponentially small `x=e^{-u}` dominates every polynomial factor in `u`; concretely `N_4(t)>0.533 e^{8t}>0` for `t<=-14`. Since `H_4>0`, this gives `A_4>0` on the whole left tail.

The reusable lesson is that the two tails need not share a proof technology. A dominant harmonic is the natural right-tail reference, while a logarithmic singularity plus analytic remainder is better treated by separating the unbounded log coordinate and reducing the sign problem to finitely many analytic coefficient bounds. Together the two estimates remove every semi-infinite region from the order-five problem.

The remaining order-five question is now purely compact: certify or refute `A_4(t)>0` on `[-14,4]`. If that compact gate is positive, AF-403/AF-404 promote the complete confluent flag to strict total positivity through order five and the first possible bad order moves to at least six.

**Boundary.** Neither tail argument accesses the continued zeta divisor or supplies a rational-prime discriminator. The result is a finite-order translation-positivity certificate for the universal Euler-log profile. It does not prove global order-five positivity until the compact interval is settled, and AF-217 still forces failure at some later finite order.