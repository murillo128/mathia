# MI-055 — Derivative depth is a second left-tail scaling coordinate, with a sharp subcritical absolute-tail regime

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md), [AF-417](../../findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md), [AF-418](../../findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md), and [AF-419](../../findings/AF-419-subcritical-linear-shifts-admit-uniform-full-tail-resummation.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal `x=c/n`. AF-417 shows that this closure is not uniform in an independently moving derivative offset. For any fixed partition `lambda` of size `d`, if `s_n/n->sigma<infinity`, the normalized sector sees the Cauchy parameter multiplied by `e^sigma`. Thus bounded-complexity probes depend on the pair `(c,sigma)`: sublinear derivative depth is asymptotically invisible, linear depth renormalizes the fixed-degree limit, and superlinear depth already destroys baseline dominance in degree one.

AF-418 then shows that `(c,sigma)` is not sufficient for the complete growing partition family at and above a second threshold. For a fixed-width full-height rectangle `lambda=(r^n)`, with `a=c^2/(4pi^2)`,

`(1/n)log C_(n,r)=r((s_n/n)-2)log n+r log a-(s_n/n)log(r!)+o(1)`.

At `sigma>2` such sectors diverge in absolute value; at `sigma=2` the finer coordinate

`tau_n=((s_n/n)-2)log n`

remains visible to growing shapes even though every fixed partition forgets it.

AF-419 proves that the opposite side is genuinely controlled rather than merely free of this one obstruction. If `limsup s_n/n<2`, splitting partitions by column height and applying Pieri's rule gives a shape-uniform absolute majorant for the **entire** exceptional-`1` partition family. Nearly full-height columns are superexponentially suppressed, while the remaining shapes have a uniform Cauchy majorant. Consequently

`S_n^(s_n)(a)=exp(-a e^(s_n/n))+o(1)`

locally uniformly for bounded `a`; in particular, when `s_n/n->sigma<2`, the full exceptional-`1` sector converges to

`exp(-e^sigma c^2/(4pi^2))`.

So `sigma=2` is now the sharp boundary for this **absolute-uniform-integrability architecture**. Below it, the fixed-degree compression extends to the complete partition tail. At and above it, absolute domination fails in general and any persistence of the same exponential must come from genuinely signed cancellation among growing sectors. At the critical ratio, that cancellation problem must retain `tau_n` or equivalent finer scaling data.

The reusable lesson is two-sided. A moving parameter discovered in fixed-complexity sectors is not automatically enough for the complete growing family; but an obstruction seen in one growing family is also not enough to declare a whole regime nonuniform. The correct scaling state emerges only after a **uniform tail theorem** or a counterexample controls the whole complexity class. Here AF-419 certifies the entire subcritical regime, while AF-418 isolates the first place where such absolute control can fail.

**Boundary.** AF-419 controls the complete exceptional-`1` Cauchy--Binet sector under `limsup s_n/n<2`. It does not settle the critical/supercritical signed resummation, every omitted determinant sector at growing derivative depth, total positivity, or zero selection. The durable content is the sharp separation between a uniformly controlled subcritical phase and a critical/supercritical phase that requires new signed global structure.