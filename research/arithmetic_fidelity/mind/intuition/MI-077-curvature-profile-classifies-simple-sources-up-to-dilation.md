# MI-077 — A full curvature profile canonically recovers a simple positive source modulo dilation

**Evidence level:** exact source-classification and constructive-recovery theorems from [AF-509](../../findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md) and [AF-510](../../findings/AF-510-curvature-has-explicit-canonical-inverse-on-dilation-quotient.md), sharpened by the instability and transport results [AF-511](../../findings/AF-511-remote-prime-replacement-destroys-positive-relative-curvature-provenance-margin.md)--[AF-519](../../findings/AF-519-curvature-visibility-is-governed-by-zeroth-vs-second-log-moment-participation.md), and contrasted with the finite-sample deformation results AF-483--AF-490.

For a simple locally finite unit-weight source `Q={q_1<q_2<...}`, let `P_Q(s)=sum_q q^(-s)` on a common half-plane of convergence and

`kappa_Q(s)=(log P_Q)''(s)=Var_(mu_(Q,s))(log q)`.

AF-509 identifies this logarithmic curvature as an exact gauge-classifying observable. If two such sources have the same curvature on a nonempty open interval, analyticity forces their log partition functions to differ by an affine function. Unit weights remove the independent mass factor, leaving precisely geometric dilation: `R=cQ`. Conversely dilation changes `log P` only by a linear term and therefore leaves the curvature profile unchanged.

AF-510 makes that quotient statement constructive. Writing `lambda_n=log(q_n/q_1)`, the quotient representative with smallest atom normalized to one is recovered directly from curvature by

`H_Q(s)=int_s^infinity (t-s) kappa_Q(t) dt = log(q_1^s P_Q(s))`

and hence

`F_Q(s)=exp(H_Q(s))-1=sum_(n>=2) exp(-s lambda_n)`.

The two integration constants are not extra choices: on the normalized quotient section the positive unit leading atom forces the boundary conditions at infinity. The normalized atoms can then be peeled from the positive exponential sum. In particular the first ratio is already encoded in the curvature tail: if `delta=log(q_2/q_1)`, then `kappa_Q(s)~delta^2 exp(-delta s)` and `delta=-lim_(s->infinity) s^(-1) log kappa_Q(s)`.

AF-511--AF-514 show that exact injectivity has essentially no robust prime-provenance margin in the natural full-domain relative topology. A remote neighboring prime-to-composite replacement becomes uniformly invisible on `(1,infinity)`, and even moving the whole cofinite prime tail by sublinear additive amounts can leave the complete relative-curvature profile converging to the prime profile. The singularity at `s=1` dilutes those remote perturbations rather than exposing them.

AF-515--AF-518 identify two robust deformation endpoints. If a cofinite tail is moved by a fixed multiplicative factor `c>1`, the interface between the retained prefix and dilated tail leaves a nonzero mesoscopic curvature gap; sublinear rounding of `cp` does not remove it. The same phenomenon survives on a fixed positive-PNT-density selected tail, with an explicit defect depending on both participation density and dilation. By contrast, if the entire remote tail has uniformly vanishing logarithmic displacement,

`sup_(p>A) log(q_p/p) -> 0`,

then the global relative-curvature error tends uniformly to zero. This remains true for all-composite shifts of order `p/log p`, even though the earlier AF-514 absolute weighted transport budget can diverge.

AF-519 identifies the leading visibility statistic inside the scale-dependent selected-set regime for fixed proportional transport. If `E_A` is the selected prime set at the observation scale `s_A=1+t_A`, define its normalized zeroth and second logarithmic-moment participations by

`alpha_0 = lim T_A(s_A)/P(s_A)`, `alpha_2 = lim T_A''(s_A)/P''(s_A)`

when the limits exist. For `p -> cp` on `E_A`, with `beta_0=1-1/c`,

`kappa_A(s_A)/kappa_P(s_A) -> (1-beta_0 alpha_2)/(1-beta_0 alpha_0)`.

The first logarithmic moment is asymptotically suppressed by the extra logarithm in the squared log-derivative. Consequently point density and even vanishing Dirichlet-value share are insufficient: a moving logarithmic shell can satisfy `alpha_0=0<alpha_2` and still produce an order-one relative curvature defect. The positive-density formula of AF-517 is one regular specialization in which `alpha_0` and `alpha_2` are linked by the PNT-density geometry.

The reusable geometric picture is therefore more precise than “remote atoms are exponentially shielded.” Curvature is exactly blind to a common global log-translation, robustly blind to uniformly vanishing tail log-displacement, but for fixed order-one proportional transport its leading mesoscopic response is governed by the mismatch between **zeroth and second logarithmic-moment participation**. Counting density works only in regular families that determine both moments. In the remaining nonuniform-amplitude regime, visibility must depend jointly on transport amplitude and a scale-resolved participation profile rather than on point count or the AF-514 absolute budget alone.

This separates exact inversion from robust classification. The full profile determines the normalized source exactly, yet rational-prime provenance can have zero isolation radius under large families of remote transports. A robust prime discriminator based on curvature must either identify the correct transport-weighted log-moment topology, add independent arithmetic incidence such as additive/congruence/factorization structure, or ask for a coarser property whose decision classes are positively separated.

**Boundary.** AF-509--AF-519 concern simple unit-weight positive sources and the specific prime-tail transport families proved there. AF-518 establishes uniform invisibility under uniformly vanishing relative displacement. AF-519 classifies the leading boundary response for fixed proportional moves on arbitrary scale-dependent selected sets when the zeroth and second participation limits exist; it does not supply a full-domain necessary-and-sufficient criterion for variable displacements, oscillatory/blockwise amplitudes, or general sparse transports. It also does not prove that curvature alone robustly distinguishes rational primes in a stronger source-aware topology.