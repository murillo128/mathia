# MI-055 — Derivative depth and source amplitude form a joint left-tail critical coordinate

**Evidence level:** exact synthesis from [AF-416](../../findings/AF-416-full-left-tail-diagonal-has-positive-cauchy-limit.md), [AF-417](../../findings/AF-417-linear-derivative-shift-renormalizes-left-tail-plancherel-sectors.md), [AF-418](../../findings/AF-418-full-height-rectangles-expose-sigma-2-absolute-tail-transition.md), [AF-419](../../findings/AF-419-subcritical-linear-shifts-admit-uniform-full-tail-resummation.md), and [AF-420](../../findings/AF-420-critical-derivative-window-has-sharp-subthreshold-absolute-resummation-domain.md).

AF-416 closes the full fixed-shift determinant on the reciprocal-order left-tail diagonal. AF-417 shows that this closure is not uniform in an independently moving derivative offset: fixed partition sectors see `s_n/n->sigma` by multiplying the Cauchy parameter by `e^sigma`. AF-418 then shows that the complete growing partition family detects a finer critical coordinate at `sigma=2`, namely

`tau_n=((s_n/n)-2)log n`.

AF-419 proves that the opposite side is genuinely controlled: if `limsup s_n/n<2`, a shape-uniform absolute majorant closes the entire exceptional-`1` partition family and gives

`S_n^(s_n)(a)=exp(-a e^(s_n/n))+o(1)`

locally uniformly for bounded `a`, where `a=c^2/(4pi^2)`.

AF-420 sharpens the phase boundary. In the critical window `s_n/n->2`, derivative depth and source amplitude no longer separate. The effective coordinate is

`b_n(a)=a n^(s_n/n-2)=a e^(tau_n)`.

If `limsup b_n(A)<1`, absolute resummation survives uniformly on `0<=a<=A`. If `tau_n->tau`, the controlled domain is every compact `a<e^(-tau)`. On the exact sequence `s_n=2n`, this means every compact `a<1`, equivalently `c<2pi`.

The threshold is sharp for this **absolute-uniform-integrability mechanism**. When `a e^tau>1`, the full-height column already grows exponentially; at `s_n=2n,a=1` that one normalized term grows linearly. This does not prove that the signed determinant diverges there. It proves that the absolute-tail proof architecture has reached its exact combined boundary.

The reusable lesson is stronger than “a second moving parameter matters.” A critical regime can require a **joint scaling coordinate assembled from complexity and source amplitude**. Declaring a phase boundary from `sigma` alone is too coarse: at `sigma=2`, part of the critical window is still uniformly controlled and part is not. Conversely, failure of absolute domination at `b>=1` cannot be promoted to failure of the signed object without a separate cancellation theorem or obstruction.

**Boundary.** The synthesis concerns the exceptional-`1` Cauchy--Binet sector. It does not settle other determinant sectors, total positivity, signed resummation at or beyond `b=1`, or zero selection. The durable content is the exact joint coordinate `a n^(s_n/n-2)` and the separation between an absolutely controlled subthreshold domain and a genuinely signed boundary/superthreshold problem.