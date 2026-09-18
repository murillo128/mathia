# MI-055 — Derivative depth is a second left-tail scaling coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md) and [AF-417](../../findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal `x=c/n`. AF-417 shows that this closure is not uniform in an independently moving derivative offset. For the shifted derivative-Hankel determinant `D_(n+1)^(s_n)` and any fixed partition `lambda` of size `d`, if `s_n/n -> sigma<infinity`, then

`T_(n,lambda)^(s_n)(c/n) / E_n^(s_n)(c/n) -> (-1)^d (e^sigma c^2/(4 pi^2))^d/H_lambda^2`.

Thus the natural local coordinates are not only `c=n x` but the pair `(c, sigma)` with `sigma=s/n`. Sublinear derivative depth is asymptotically invisible to every fixed excess degree. Linear depth renormalizes the effective Cauchy parameter from `c^2/(4pi^2)` to `e^sigma c^2/(4pi^2)`. Superlinear depth is already visible in the exact degree-one ratio, whose magnitude diverges, so the smallest exponent set ceases to dominate.

This is a fidelity statement about what survives the large-order compression. Holding determinant order and source coordinate in their critical balance does not freeze the asymptotics if derivative depth is allowed to grow. A proof that is uniform for each fixed shift can therefore fail exactly when the shift becomes another extensive coordinate.

The fixed-degree limits suggest the full exceptional-`1` sector should resum to `exp(-e^sigma c^2/(4pi^2))` for finite `sigma`, but AF-417 does **not** justify the required interchange with the moving partition tail. Nor does it show that the omitted-`1` or one-/zero-singular-block sectors remain negligible once `s` grows linearly. Those are separate uniformity questions rather than consequences of the fixed-shift Cauchy limit.

**Boundary.** The result concerns the left-tail analytic germ and normalized Cauchy--Binet sectors. It does not decide the compact order-five gate, total positivity, or any zero-selection statement. Its durable content is the sharp scaling transition `s~n`: derivative depth is an independent asymptotic resource and must be budgeted jointly with determinant order and source position.