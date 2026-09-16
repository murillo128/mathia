# MI-036 — Quantitative PNT fidelity rigidifies the terminal source before moment complexity

**Evidence level:** literature-backed/exact synthesis from [RE-015](../../findings/RE-015-pnt-remainder-controls-upper-robin-tail.md), [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-155](../../findings/RE-155-terminal-generalized-source-ambiguity.md) through [RE-163](../../findings/RE-163-chebyshev-modes-are-the-sharp-approximate-terminal-coordinates.md), and [RE-164](../../findings/RE-164-quantitative-pnt-fidelity-collapses-terminal-generalized-source-ambiguity.md). The quantitative PNT envelope is an explicit source-class hypothesis for matched controls; no claim is made that arbitrary generalized primes satisfy it.

The terminal moment hierarchy measures ambiguity only relative to the source class that is allowed. Under coarse PNT information `theta_Q(x)=x+o(x)`, one can modify a terminal shell, match many raw or Chebyshev moments, and still move the normalized Robin source coordinate by order one. RE-162--RE-163 precisely quantify that ambiguity through Chebyshev capacity and kernel-weighted leakage.

RE-164 shows that the ambiguity collapses if the comparison class is required to preserve the quantitative PNT remainder already used at the ordinary-source upper horizon. If two sources agree below `T`, their Robin-coordinate difference is exactly the terminal integral of `theta_(Q2)-theta_(Q1)` against the positive kernel. Consequently

`|A_p(Q1)-A_p(Q2)| << sqrt(p) log p M_12(T,U) log(log U/log T)`,

where `M_12` is the maximal relative Chebyshev discrepancy on `[T,U]`. On a terminal logarithmic shell of width `L`, an order-one destination displacement forces `M_12 >> eta_p/L`. Moment matching cannot hide this cumulative source excursion from the positive destination kernel.

If both sources satisfy a Korobov--Vinogradov-scale envelope `|theta_Q(t)-t| <= C t exp(-b V(t))`, the terminal difference is instead bounded by the same integrable PNT tail used in RE-015. At the canonical horizon `U_A(p)`, bounded terminal shells become `o(1)` once `b kappa_A>=1/2`; more generally, source freedom above a lower horizon `U_B(p)` is `o(1)` whenever `b kappa_B>1/2`.

The reusable lesson is **apply the strongest justified source-fidelity theorem before pricing internal approximation complexity**. Exact moment order, Chebyshev leakage and endpoint spectral migration are genuine currencies only in classes where the source is still free enough to realize them. A quantitative source theorem can make an entire terminal approximation hierarchy irrelevant by shrinking the admissible fibre before those coordinates are considered.

For Robin, this redirects the live source problem away from terminal generalized-source replacements that violate the known PNT envelope. Any surviving ordinary-prime/CA obstruction must live below the quantitative-PNT inversion scale, exploit selector-height coupling or another non-terminal source coordinate, or show that the actual destination consumes information not already rigidified by the PNT remainder.

**Boundary.** RE-164 does not prove Robin's inequality, control the middle annulus, or eliminate the zero-packet branch. RE-155--RE-163 remain valid sharp obstructions for coarse-PNT comparison classes. The intuition is source-class relative: it forbids treating a matched control that violates a load-bearing quantitative source theorem as evidence that the real source retains the same terminal ambiguity.
