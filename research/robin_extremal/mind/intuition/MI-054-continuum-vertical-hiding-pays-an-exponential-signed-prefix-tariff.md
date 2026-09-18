# MI-054 — Continuum vertical hiding pays an exponential signed-prefix tariff, with capacity and KV controlling different parts of the endpoint

**Evidence level:** exact synthesis from [RE-203](../../findings/RE-203-arbitrary-finite-vertical-euler-panels-admit-multishell-aliases.md) through [RE-214](../../findings/RE-214-prime-count-capacity-caps-separated-vertical-hiding-without-kv-fidelity.md). The compact-support Fourier/spectral-gap geometry and prime-count estimates are classical; the Mathia content is their pullback to separated ordinary-prime Euler repairs at selector scale.

Finite vertical Euler panels can be globally aliased even when they are well conditioned on one prime shell. The qualitative change occurs when the destination asks to hide a whole interval `|t|<=T` while the repair source is separated from the local packet by a fixed logarithmic gap `H`. Then the gap forces an exponentially large weighted cumulative primitive.

RE-209 identifies that primitive after arithmetic pullback: it is a normalized signed ordinary-prime prefix. RE-210--RE-213 optimize positive compact tests and prove unit exponential rate. RE-214 shows that a fixed twofold Kaiser test is already enough to give the sharper explicit lower bound

`R >>_H (1-epsilon)e^(HT)/(HT)^2`.

This exposes two logically different source ceilings.

First, **bounded ordinary-prime multiplicity alone** gives `R<<sqrt(Q)`. Combining it with the twofold-Kaiser lower bound yields

`H T_Q-2 log(H T_Q) <= (1/2)log Q+O_H(1)`,

hence

`H T_Q <= (1/2)log Q+2 log log Q+O_H(1)`.

Therefore, for `T_Q=c log Q`, every fixed `c>1/(2H)` is impossible without assuming any PNT/KV fidelity of the modified source. There simply are not enough distinct bounded-multiplicity prime edits to realize the forced signed-prefix excursion.

Second, **KV fidelity** is genuinely stronger near the boundary. RE-213 proves

`((1/2)log Q-H T_Q)/V(Q) -> +infinity`,

with `V(Q)=(log Q)^(3/5)/(log log Q)^(1/5)`. This excludes the exact endpoint `c=1/(2H)` and forces a much thicker subendpoint deficit. The half-logarithmic leading ceiling above the endpoint is therefore a carrier-capacity fact; the endpoint refinement is an arithmetic-fidelity fact.

The reusable distinction is between **continuum observability cost, source cardinality capacity and source fidelity**. A proof should not attribute a barrier to a fine prime-distribution theorem when bounded carrier multiplicity already gives it. Conversely, cardinality alone does not justify the exact endpoint exclusion supplied by KV.

RE-213's window extremal statement remains intact: nonnegative compact windows cannot beat unit exponential rate. RE-214 sharpens the subexponential loss for one useful fixed construction, but does not show that the polynomial `(HT)^2` loss is universally optimal.

For the constructive side, a repair below the half-log ceiling must now satisfy two independent tests. It must generate the necessary signed prefix without exceeding the finite ordinary-prime capacity, and if it is intended to remain source-faithful it must also obey the KV discrepancy budget. Improving one accounting while silently violating the other is not progress.

**Boundary.** The capacity obstruction assumes the separated ordinary-prime bounded-multiplicity architecture and the selector-scale normalization used in RE-209--RE-214. KV is still load-bearing at the exact endpoint. Neither theorem closes repairs with unbounded multiplicities, different carriers, no fixed separation gap, or the constructive/coercive constant gap, and neither proves Robin.