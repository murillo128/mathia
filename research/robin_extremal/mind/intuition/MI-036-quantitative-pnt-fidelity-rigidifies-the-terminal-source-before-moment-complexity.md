# MI-036 — Quantitative PNT fidelity has a sharp terminal inversion capacity before moment complexity

**Evidence level:** literature-backed/exact synthesis from [RE-015](../../findings/RE-015-pnt-remainder-controls-upper-robin-tail.md), [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-155](../../findings/RE-155-terminal-generalized-source-ambiguity.md) through [RE-163](../../findings/RE-163-chebyshev-modes-are-the-sharp-approximate-terminal-coordinates.md), [RE-164](../../findings/RE-164-quantitative-pnt-fidelity-collapses-terminal-generalized-source-ambiguity.md), and [RE-165](../../findings/RE-165-kv-envelope-capacity-is-sharp-and-critical-equality-remains-ambiguous.md). The quantitative PNT envelope is an explicit source-class hypothesis for matched controls; no claim is made that arbitrary generalized primes satisfy it.

The terminal moment hierarchy measures ambiguity only relative to the source class that is allowed. Under coarse PNT information `theta_Q(x)=x+o(x)`, one can modify a terminal shell, match many raw or Chebyshev moments, and still move the normalized Robin source coordinate by order one. RE-162--RE-163 precisely quantify that ambiguity through Chebyshev capacity and kernel-weighted leakage.

RE-164 shows how a quantitative PNT remainder can collapse that freedom. If two sources agree below `T`, their Robin-coordinate difference is exactly the terminal integral of `theta_(Q2)-theta_(Q1)` against the positive kernel. Consequently

`|A_p(Q1)-A_p(Q2)| << sqrt(p) log p M_12(T,U) log(log U/log T)`,

where `M_12` is the maximal relative Chebyshev discrepancy on `[T,U]`. On a terminal logarithmic shell of width `L`, an order-one destination displacement forces `M_12 >> eta_p/L`. Moment matching cannot hide this cumulative source excursion from the positive destination kernel.

For a Korobov--Vinogradov-scale envelope `|theta_Q(t)-t| <= C t exp(-b V(t))`, the correct remote inversion currency is not merely the leading exponent but

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`.

RE-164 gives the upper implication `K_b(p,T)->0 => o(1)` terminal ambiguity. RE-165 proves that this scale is essentially sharp in the generalized insertion class: an increasing fraction of the allowed PNT envelope can be discretized into positive generalized-prime insertions whose Robin displacement is asymptotic to a fixed constant times `K_b`, while the modified source remains in the same quantitative PNT exponent class. Thus when `K_b` stays bounded away from zero or diverges, quantitative PNT fidelity alone does not identify the terminal coordinate.

This sharpness corrects the critical fixed-horizon reading. For `T=U_B(p)`, let `kappa_B=B^(3/5)(3/5)^(1/5)`. The strict regime

`b kappa_B > 1/2`

implies `K_b->0` and terminal rigidity. But the nominal equality `b kappa_B=1/2` is **not** rigid. The next term in `V(U_B)` has the sign that makes `K_b->infinity`, so generalized insertion controls with nonvanishing Robin displacement still fit inside the same PNT envelope. The exact transition is therefore `K_b->0`, not the shorthand `b kappa_B>=1/2`.

The reusable lesson is **apply the strongest justified source-fidelity theorem, at its correct quantitative inversion scale, before pricing internal approximation complexity**. Exact moment order, Chebyshev leakage and endpoint spectral migration are genuine currencies only in classes where the source is still free enough to realize them. A quantitative source theorem can make the terminal approximation hierarchy irrelevant above its inversion boundary, but leading-exponent heuristics must not be allowed to erase a critical slowly varying term that leaves the admissible fibre nontrivial.

For Robin, this redirects the live source problem away from terminal generalized-source replacements above the strict quantitative-PNT inversion scale. Any surviving ordinary-prime/CA obstruction must live below that scale, exploit selector-height coupling or another non-terminal source coordinate, or show that the actual destination consumes information not already rigidified by the PNT remainder. At the critical fixed canonical equality, matched generalized-source ambiguity remains a legitimate control and must not be dismissed by RE-164's leading asymptotic alone.

**Boundary.** RE-164--RE-165 do not prove Robin's inequality, control the middle annulus, or eliminate the zero-packet branch. RE-155--RE-163 remain valid sharp obstructions for coarse-PNT comparison classes. RE-165's lower construction is for generalized-prime insertions inside the declared quantitative envelope and establishes sharpness of the remote capacity scale there; it is not a claim that the ordinary primes themselves realize those perturbations. The intuition is source-class relative and cutoff-sensitive: a matched control is informative only when it preserves the load-bearing quantitative source theorem and lies on the correct side of the exact `K_b` inversion parameter.
