# MI-040 — First-slope matching prices the terminal KV tail

**Evidence level:** exact synthesis from [RE-175](../../findings/RE-175-boundary-euler-jets-force-oscillation-and-detect-delayed-compensation.md) and [RE-176](../../findings/RE-176-first-slope-matching-forces-a-kv-terminal-tail-capacity.md), under the stated ordinary-prime, minimal-sign-pattern and Korobov--Vinogradov source-fidelity hypotheses.

RE-175 shows that matching the Mertens boundary value and the first Euler boundary slope forces at least two sign changes in a sufficiently far-out prime-supported multiplicity perturbation. For the delayed-compensation control of RE-173, the first slope already detects the excursion at its natural Robin normalization `1/(sqrt(p) log p)`.

A tempting repair is therefore to use the minimal sign pattern `- + -`: keep the original deletion packet near `p`, add a positive compensating phase, and push the required final negative phase arbitrarily far away so that its Mertens mass becomes tiny. RE-176 shows that the first slope prevents this remote exile under a KV source envelope.

Let `h_D,h_P,h_N` be the unsigned Mertens-weight masses of the negative, positive and terminal-negative phases and let `a_D,a_P,a_N` be their corresponding first-slope/Mertens barycentric locations. Exact matching of the first two boundary jets gives

`h_D(a_P-a_D)=h_N(a_N-a_P)`.

If the positive phase starts a fixed multiplicative distance beyond the original deletion packet, then `a_P-a_D` is bounded below by a positive constant. The terminal first-slope mass `b_N=h_N a_N` therefore retains a fixed debt

`b_N >> 1/(sqrt(p) log p)`.

Moving the final phase outward can trade Mertens mass for logarithmic leverage, but it cannot make that first-slope workload disappear.

The KV envelope supplies only limited one-sign capacity for that debt. If the terminal negative phase begins at `Y`, Stieltjes summation of the monotone Chebyshev discrepancy gives

`b_N <<_b ell_KV(Y) e^(-b V(Y))`,

where `ell_KV(Y)=log(Y)/V(Y)`. Combining the lower debt with this tail capacity forces

`sqrt(p) log(p) ell_KV(Y) e^(-b V(Y)) >>_b 1`,

hence

`b V(Y) <= (1/2+o(1)) log p`.

So the cheapest two-jet repair has a genuine moving placement horizon: the second sign change may move, but not beyond the point where the one-sign KV tail no longer has enough first-slope capacity. This is a stronger statement than local detectability of the compensator. It connects a destination-aligned boundary moment to the spatial capacity of the allowed source tail.

The reusable lesson is that **a matched moment can price not only how much compensating mass is needed but where a minimal-sign repair is allowed to live**. A weighted conservation law whose kernel grows with logarithmic location converts remote displacement into leverage, while the source envelope bounds how much weighted mass a one-sign tail can supply. The resulting balance creates a placement constraint even when the unweighted compensating mass can shrink.

The next escape is structurally clear: use more sign alternations so that the terminal monotonicity behind the one-sign KV capacity estimate disappears. Any continuation must therefore find a quantity that survives those cancellations — for example an iterated one-sign decomposition, bounded-variation/transport cost, or higher boundary-jet debt — rather than repeat the same terminal-tail argument unchanged.

**Boundary.** The theorem is necessary, not sufficient: it does not construct or rule out a two-sign-change control inside the capacity horizon. It assumes the first boundary slope is matched; the original Robin problem does not currently provide that condition for free. It also does not cover controls with further sign changes, where remote positive and negative phases can cancel Chebyshev discrepancy inside the tail.