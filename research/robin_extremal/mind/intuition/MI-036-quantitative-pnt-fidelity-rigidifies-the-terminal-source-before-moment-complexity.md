# MI-036 — Quantitative PNT fidelity has distinct local and remote moving capacity transitions

**Evidence level:** literature-backed/exact synthesis from [RE-015](../../findings/RE-015-pnt-remainder-controls-upper-robin-tail.md), [RE-153](../../findings/RE-153-self-tangent-robin-height-is-a-pareto-weighted-chebyshev-deficit-average.md), and [RE-155](../../findings/RE-155-terminal-generalized-source-ambiguity.md) through [RE-167](../../findings/RE-167-fixed-width-kv-shells-have-a-distinct-local-capacity-center.md). The quantitative PNT envelope is an explicit source-class hypothesis; no claim is made that arbitrary generalized primes satisfy it.

The terminal moment hierarchy measures ambiguity only inside the source class still allowed after stronger source information is imposed. RE-164--RE-166 identify a sharp Korobov--Vinogradov **remote-tail** capacity

`K_b(p,T)=sqrt(p) log p exp(-b V(T))/V(T)`,

where `V(T)=(log T)^(3/5)/(log log T)^(1/5)`. If `K_b->0`, matched sources agreeing below `T` have vanishing Robin-coordinate separation; generalized positive insertions show that positive or divergent capacity leaves order-one remote-tail ambiguity possible. RE-166 inverts this capacity and shows that the transition is an additive `O(1)` layer in the intrinsic `V` coordinate around a moving Lambert-W center.

RE-167 adds the spatial-support variable that the remote capacity suppresses. If the discrepancy is confined to one fixed multiplicative shell `[T,CT]`, the sharp capacity is instead

`L_b(p,T)=sqrt(p) log p exp(-b V(T))/log T`.

The extra denominator is structural: a proportional shell samples only logarithmic width `O(1/log T)` of the positive Robin kernel, whereas a remote tail can spend its PNT budget across many scales and accumulates the larger `1/V(T)` factor. Exact mass-balanced generalized-prime relocations attain the local scale while restoring the Chebyshev discrepancy to zero above the shell.

Because `V(T)<<log T`, the local-shell transition occurs strictly earlier. If `v_loc=V(T_loc)` solves `L_b=1` and `v_*=V(T_*)` solves `K_b=1`, then

`v_* - v_loc = (2/(3b)) log log p + (1/(3b)) log log log p + O(1)`.

This separation diverges, while each individual fixed-capacity contour still has only `O(1)` width in `V`. There is therefore no single “KV rigidity height”: the correct inversion target depends on whether the unresolved source is allowed to occupy one shell or the entire tail.

The bounded-multiplicative selector regime remains far from even the lower local boundary. At `T=Bp`,

`L_b(p,Bp)=p^(1/2-o(1))->infinity`.

Hence order-one post-selector relocations can be made quantitatively PNT-faithful with an `o(1)` deterioration of the envelope constant. Knowing the ordinary source through a fixed multiple of `p` and imposing the full KV remainder afterwards still does not identify the normalized Robin source coordinate.

The reusable lesson is that a quantitative source theorem has **two independent inputs: error envelope and admissible spatial support of the discrepancy**. A destination kernel can assign different capacities to a localized perturbation and a distributed tail even when both obey the same pointwise source bound. Pricing only the envelope can therefore overstate the amount of unresolved information.

For Robin, moment matching is relevant only after the actual selector/source geometry is placed relative to the appropriate capacity. If CA geometry localizes the missing source to bounded-width shells, crossing `T_loc` could already be enough for that restricted uncertainty; if remote rearrangement remains admissible, only the higher `T_*` center gives worst-case rigidity. RE-167 does not prove either selector coupling. It supplies the sharper target and shows that bounded-multiplicative selection plus quantitative PNT is insufficient.

**Boundary.** The lower sharpness constructions use generalized-prime relocations in the declared quantitative envelope and do not assert that ordinary primes realize them. The local theorem assumes fixed multiplicative shell width; the remote theorem allows distributed tail modifications. Neither controls the middle annulus, proves Robin's inequality, removes the zero-packet branch, or replaces the missing ordinary-prime/CA selector theorem.
