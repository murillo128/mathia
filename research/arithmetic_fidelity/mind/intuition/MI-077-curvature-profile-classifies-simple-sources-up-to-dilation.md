# MI-077 — A full curvature profile canonically recovers a simple positive source modulo dilation

**Evidence level:** exact source-classification and constructive-recovery theorems from [AF-509](../../findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md) and [AF-510](../../findings/AF-510-curvature-has-explicit-canonical-inverse-on-dilation-quotient.md), sharpened by the instability and transport results [AF-511](../../findings/AF-511-remote-prime-replacement-destroys-positive-relative-curvature-provenance-margin.md)--[AF-521](../../findings/AF-521-inward-transport-promotes-first-log-moment-to-leading-curvature.md), and contrasted with the finite-sample deformation results AF-483--AF-490.

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

AF-520 shows that this moment compression is not a peculiarity of one proportional transport. At a moving boundary scale `s_A=1+t_A`, every arbitrary outward transport of the remote tail with nonvanishing normalized source survival `rho_0=Q_A/P>=c>0` satisfies

`kappa_A(s_A)/kappa_P(s_A) = rho_2/rho_0 + O_c(1/log(1/t_A))`,

where `rho_2=Q_A''/P''`. Equivalently, if `d_0=1-rho_0` and `d_2=1-rho_2`, the leading ratio is `(1-d_2)/(1-d_0)`. Outwardness controls the first derivative strongly enough that its squared log-derivative contribution is lower order. At one boundary scale, detailed block structure, oscillatory displacement and the first logarithmic moment can therefore be different microscopically while producing the same leading curvature whenever they agree on these two normalized defects.

AF-521 identifies exactly what fails beyond that domination. For every positive Dirichlet source, not only transports, define `rho_j=M_j^Q/M_j^P` for the zeroth, first and second logarithmic moments and `r=(M_1^P)^2/(M_0^P M_2^P)`. Then pointwise

`kappa_Q/kappa_P = [rho_2/rho_0-r(rho_1/rho_0)^2]/(1-r)`.

At the prime-zeta boundary `s=1+t`, `r~1/log(1/t)`. Therefore the first-moment term remains negligible precisely when `r(rho_1/rho_0)^2->0`; with `rho_0` bounded below, `rho_1=o(sqrt(log(1/t)))` is sufficient. AF-521 also gives literal simple unit-weight inward prime-to-composite controls with the same leading `(rho_0,rho_2)` but different `rho_1/sqrt(log(1/t))`, hence different order-one curvature limits. The two-defect quotient of AF-520 is therefore not universal once first-moment domination is removed: scalar one-point curvature has the exact three-moment carrier `(rho_0,rho_1,rho_2)`.

The reusable geometric picture is consequently sharper than “remote atoms are exponentially shielded.” Curvature is exactly blind to a common global log-translation and robustly blind to uniformly vanishing tail log-displacement. Under outward source-surviving transport, one boundary scale compresses leading response to normalized value survival and second-log-moment survival. Without first-moment domination, one additional coordinate is promoted at the sharp `sqrt(log(1/t))` scale; detailed source incidence is still absent from the one-point carrier.

This separates exact inversion from robust classification. The full profile determines the normalized source exactly, yet rational-prime provenance can have zero isolation radius under large families of remote transports, and one-scale curvature can identify only a small moment quotient whose dimension itself depends on the domination regime. A robust prime discriminator based on curvature must therefore use lower-order or multi-scale profile information, handle source extinction `rho_0->0`, signed/complex sources or richer observables, add independent arithmetic incidence, or ask for a coarser property whose decision classes are positively separated.

**Boundary.** AF-509--AF-521 concern positive sources and, for the transport results, the specific prime-tail regimes proved there. AF-520 is a leading one-scale law under outward transport and `rho_0>=c>0`; AF-521 removes outwardness only for the exact scalar one-point moment formula and its positive-source boundary asymptotics. Neither settles source extinction, lower-order/full-profile robustness, multi-scale recovery, signed/complex cancellation, or a full-domain necessary-and-sufficient stability criterion. Exact whole-profile injectivity modulo dilation remains intact, so finite-moment compression is a statement about destination-visible robust information at one scale, not loss of formal recoverability.