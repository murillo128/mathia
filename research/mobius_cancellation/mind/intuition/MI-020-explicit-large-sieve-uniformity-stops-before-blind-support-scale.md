# MI-020 — Explicit quadratic-large-sieve uniformity ends far below the first possible blind support

**Evidence level:** literature-backed and exact for the shell-product specialization in MC-262. Zihao Liu's 2026 explicit quadratic-large-sieve dependence is external prior art; the Mathia conclusion is a quantitative obstruction to the current black-box all-moduli route, not an impossibility theorem for shell parity balance itself.

For a `t`-prime shell subset `T`, the parity correlation is a quadratic character sum modulo the squarefree product `m_T`. Liu's explicit form of Heath-Brown's inequality replaces the hidden `epsilon` constant by a factor of the form

`exp_4(C/epsilon) (MN)^epsilon`.

After embedding all shell products into the ambient squarefree moduli up to about `y^t`, that dependence is strong enough to extend fixed-order parity balance to the genuine growing range `t=o(log^(4) y)`. In that range the normalized mean-square shell bias is still `y^(-1+o(1))`.

But the first support on which a quadratic blind relation can survive is already of order `(1/log 2) log log y`. The scales do not approach each other. If `t/log^(4)y -> infinity`, then for every choice of `epsilon` either the factor `(y^t)^epsilon` or the explicit `exp_4(C/epsilon)` term alone costs at least a factor of order `y`. Once the sparse shell family is compared with the ambient modulus interval, that cost erases the only global saving that could certify normalized balance.

The obstruction is therefore **the combination of explicit uniformity and ambient-family wastage**, not evidence that high-order shell balance fails. Improving a generic `(MN)^{o(1)}(M+N)` statement without controlling how the `o(1)` depends on the growing shell order will not touch the live blind-support scale. A useful analytic exit must sum over the structured product family at a cost closer to its actual cardinality and remain uniform through `t~log log y`, or bypass this parity-rank route via shell generation or direct cancellation of the surviving source-selected blind pretender.

**Boundary.** The `o(log^(4)y)` range is sufficient, not asserted sharp. MC-262 does not raise the existing blind-support floor, prove a blind vector exists, or yield a new Mertens bound.