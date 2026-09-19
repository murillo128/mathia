# MI-050 — Full localized Weil energy turns any RH failure into a finite-radius first crossing whose prime thresholds are form-small, not norm-small

**Evidence level:** exact synthesis from `WI-355` and `WI-356`, using Suzuki's localized Weil-form framework.

For the localized Weil form on `(-a,a)`, let

`lambda(a)=inf_(v!=0) Q_W(v)/||v||_2^2`.

Suzuki's framework identifies this as the lowest eigenvalue of a localized self-adjoint Weil operator, proves continuity in `a`, positivity for sufficiently small `a`, and that failure of RH is equivalent to `lambda(a)<0` for some finite radius. Nested variational domains give the exact monotonicity `lambda(b)<=lambda(a)` for `b>a`. Therefore under `not RH` there is a canonical first radius `a_*=inf{a:lambda(a)<=0}` with `lambda(a_*)=0`; zero is then an actual ground-state eigenvalue. At radius `a`, the arithmetic kernel uses only prime powers up to `e^(2a)`.

WI-356 resolves the local topology of one newly activated prime-power channel. For `q=p^k`, activation occurs at `a_q=(log q)/2`. On the fixed interval `(-1,1)`, let `t=log(q)/a=2-epsilon`. The channel is a compressed translation with coefficient `c_q=Lambda(q)/sqrt(q)`. For every `a>a_q` sufficiently close to threshold, its self-adjoint `L^2` operator norm is exactly `c_q`; at `a=a_q` it is zero. Thus the arithmetic perturbation is not norm-continuous at activation, no matter how short the new overlap strip becomes.

The same channel is small in the topology supplied by Suzuki's universal logarithmic form `L(w)`. WI-356 proves the endpoint estimate

`|C_w(2-epsilon)| <= L(w)/log(1/(2 epsilon))`,

hence

`|P_(q,a)(w)| <= [2 c_q/log(1/(2 epsilon))] L(w)`.

The relative-form coefficient tends to zero as `a downarrow a_q`. The apparent paradox is resolved by the witnesses: vectors that nearly saturate the `L^2` norm jump put order-one mass into shrinking endpoint strips, forcing their logarithmic form energy to diverge. They escape every bounded-`L` set.

This sharpens the first-crossing program. The threshold step cannot be controlled by ordinary bounded-operator perturbation theory in `L^2`; a viable induction must use the logarithmic form topology together with a quantitative coercive reserve, a bound on the `L`-energy of a hypothetical null state, or additional source constraints from the exact null equation. Form-smallness makes threshold propagation compatible with the source formula, but does not prove it.

The reusable distinction is between **defect sensitivity** and **perturbation topology**. The full localized form detects every RH failure at finite radius, unlike zero-count-normalized pair correlation, but the discrete arithmetic channels entering that form are only small relative to the endpoint-singular energy that penalizes their concentration.

**Boundary.** Finite prime-power input does not make the localized operator finite-dimensional or automatically decidable. WI-356 controls only the newly activated channel; the already-active prime terms, archimedean contribution and continuous remainder also vary with `a`. No spectral gap, global coercivity theorem or threshold-propagation theorem is established.
