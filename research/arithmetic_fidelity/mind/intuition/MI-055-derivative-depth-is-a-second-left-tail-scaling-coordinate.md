# MI-055 — Derivative depth is a second left-tail scaling coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md), [AF-417](../../findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md), and [AF-418](../../findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal `x=c/n`. AF-417 shows that this closure is not uniform in an independently moving derivative offset. For the shifted derivative-Hankel determinant `D_(n+1)^(s_n)` and any fixed partition `lambda` of size `d`, if `s_n/n -> sigma<infinity`, then

`T_(n,lambda)^(s_n)(c/n) / E_n^(s_n)(c/n) -> (-1)^d (e^sigma c^2/(4 pi^2))^d/H_lambda^2`.

Thus bounded-complexity sectors see the pair `(c,sigma)`: sublinear derivative depth is asymptotically invisible, linear depth renormalizes the Cauchy parameter by `e^sigma`, and superlinear depth already destroys baseline dominance in degree one.

AF-418 shows that `(c,sigma)` is **not** the complete scaling state once partition complexity is allowed to grow with `n`. Put `a=c^2/(4pi^2)` and take the full-height rectangle `lambda=(r^n)` with fixed `r>=1`. Its exact normalized magnitude satisfies

`(1/n) log C_(n,r) = r((s_n/n)-2)log n + r log a - (s_n/n)log(r!) + o(1)`.

For `sigma<2`, every fixed-width full-height rectangle is superexponentially negligible. For `sigma>2`, every such sector diverges in absolute value for every fixed `a>0`, so no `n`-uniform absolute Schur majorant of the AF-415 type can justify the complete-tail interchange. At the critical ratio `sigma=2`, even the limit of `s_n/n` forgets relevant information. If

`tau_n=((s_n/n)-2)log n -> tau`,

then

`(C_(n,r))^(1/n) -> e^(r tau) a^r/(r!)^2`.

For the exact sequence `s_n=2n`, the column `(1^n)` therefore grows exponentially whenever `c>2pi`.

The durable scaling lesson is now two-level. `sigma=s_n/n` controls every **fixed** partition sector, but the complete partition tail has a second transition at `sigma=2`; there the finer window `tau_n` is visible to growing shapes although it is invisible to every fixed partition. Taking the fixed-partition limit is therefore an information-losing compression of the full determinant ensemble.

This does not show that the signed complete sector fails to converge to `exp(-e^sigma c^2/(4pi^2))`. For `sigma>=2`, however, such a limit could only be established through global cancellation among growing alternating sectors, not through the absolute domination used at fixed shift. For `sigma<2`, the rectangular obstruction disappears but a genuinely shape-uniform bound over all partitions is still required.

**Boundary.** The result concerns the left-tail analytic germ and normalized Cauchy--Binet sectors. It does not decide total positivity, the compact order-five gate, the omitted determinant sectors at growing derivative depth, or any zero-selection statement. Its reusable content is that asymptotic coordinates sufficient for every bounded-complexity probe can be insufficient for the complete growing family.