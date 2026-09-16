# MI-036 — Quantitative PNT fidelity has a sharp moving Lambert-W transition before moment complexity

**Evidence level:** literature-backed/exact synthesis from [RE-015](../../findings/RE-015-pnt-remainder-controls-upper-robin-tail.md), [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), [RE-155](../../findings/RE-155-terminal-generalized-source-ambiguity.md) through [RE-166](../../findings/RE-166-lambert-w-inversion-localizes-the-kv-capacity-transition.md). The quantitative PNT envelope is an explicit source-class hypothesis for matched controls; no claim is made that arbitrary generalized primes satisfy it.

The terminal moment hierarchy measures ambiguity only relative to the source class that remains admissible. Under coarse PNT information `theta_Q(x)=x+o(x)`, terminal generalized-source modifications can match many raw or Chebyshev moments while moving the normalized Robin source coordinate by order one. RE-162--RE-163 quantify that coarse-information ambiguity through Chebyshev capacity and kernel-weighted leakage.

RE-164--RE-165 place a stronger source-fidelity gate before this hierarchy. For a Korobov--Vinogradov-scale envelope the correct remote inversion currency is

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

with `V(T)=(log T)^(3/5)/(log log T)^(1/5)`. Quantitative PNT rigidity holds when `K_b(p,T)->0`, while generalized positive insertions inside the same exponent class show that a positive or divergent capacity leaves order-one terminal ambiguity possible. The nominal fixed-horizon equality `b kappa_B=1/2` is therefore not rigid: the slowly varying correction has the wrong sign and sends `K_b` to infinity.

RE-166 inverts this capacity exactly. The capacity-one center in the intrinsic `V` coordinate is

`v_*(p)=b^(-1) W_0(b log(p) sqrt(p))`,

with the corresponding terminal horizon determined by `V(T_*)=v_*` and explicitly invertible through the `W_{-1}` branch. For every terminal horizon,

`K_b(p,T)=exp(-b Delta_p)/(1+Delta_p/v_*)`,

where `Delta_p=V(T)-v_*(p)`. Hence `Delta_p->+infinity` is the rigidity regime, bounded `Delta_p` leaves nonvanishing generalized-source capacity, and `Delta_p->-infinity` gives divergent capacity.

The important sharpening is that the transition is much thinner than the leading fixed-`B` scale suggests. Every fixed positive capacity contour lies only an additive `O(1)` distance from every other one in `V`. The moving center itself has

`v_*(p)=log(p)/(2b)+log(2b)/b+o(1)`,

while its canonical-height coefficient contains a slowly varying relative displacement of order `log log log p / log log p`. That displacement is far larger than the actual transition layer. In `log T` coordinates an `O(1)` `V` layer has width `O((log p)^(2/3)(log log p)^(1/3))`; in the normalized `B` coordinate it has width only `O(1/log p)`.

The reusable lesson is stronger than “use the exact capacity rather than a leading exponent.” When a source theorem and a destination kernel define a sharp monotone capacity, the meaningful boundary is a **moving inversion contour**, and the scale on which source rigidity changes can be parametrically thinner than the scale on which its leading asymptotic center moves. Equality at a coarse exponent is therefore not a boundary theorem. One must resolve the capacity on its own transition coordinate before pricing downstream approximation or moment complexity.

For Robin, exact or approximate moment matching is relevant only after the source class and terminal position are shown to remain on the ambiguous side of this moving center. To force source rigidity from KV-strength information, the actual ordinary-prime/CA selector must place the effective terminal horizon above `T_*(p)` by an unbounded amount in `V`, not merely reach the leading equality coefficient. RE-166 does not supply that selector-height coupling; it gives the quantitative target that such a theorem would have to cross.

**Boundary.** RE-164--RE-166 do not prove Robin's inequality, control the middle annulus, or eliminate the zero-packet branch. Their lower sharpness uses generalized-prime insertions in the declared quantitative envelope and does not assert that ordinary primes realize those perturbations. The live arithmetic issue remains the coupling between the actual CA selector/source geometry and this moving terminal horizon, or another non-terminal source channel that bypasses the capacity altogether.