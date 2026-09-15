# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Price one-sided near-left cancellation by reciprocal-scale radius and compare it with the exterior budget

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-028-arbitrarily-slow-scaled-escape-defeats-target-anchored-turan`.

RE-112--RE-138 reduce the attained finite-edge branch to a strong atom plus reciprocal-scale cancellation geometry. RE-139--RE-142 show that rightmost-anchored Turán visibility can lose an unusable transfer factor even under strong upper source envelopes. RE-143 removes that transfer by anchoring at the original algebraically strong atom and applying Turán's First Main Theorem only to zeros on or to its right.

RE-144 then closes the naive shrinking-slab hope: a matched simple spectrum can have a strong target with **exactly one** retained mode on or to its right, negligible far-left and high-height tails, and still hide the target on a fixed-relative observation window using a near-left cluster whose scaled radius `R(U)` tends to infinity as slowly as prescribed. The cluster may lie inside `o(log U/U)` width, and scaled radius only `O(log B)` already supports polynomial suppression in local cardinality `B`.

RE-145 adds the missing rate. For the positive empirical-measure representation underlying the Robin packet, every packet confined to scaled radius `R` has normalized local visibility at least `exp(-O_kappa(R))`, uniformly in cardinality and arrangement. This exponential dependence is the correct functional order in the matched class: the `RE-144` product packets attain exponential suppression in scaled radius after normalization. Hence `R(U)=o(log U)` still leaves a `U^{-o(1)}` local floor even though it does **not** restore a fixed positive floor and therefore still permits qualitative `o(M_0)` hiding.

The frontier is now a rate comparison, not a bounded/unbounded dichotomy. A useful source theorem may force the relevant actual-zero packet into a radius small enough that `exp(-O(R(U)))` dominates the exterior cancellation budget, or may prove that the exterior packet is polynomially smaller than this local floor. Otherwise one needs genuinely relational phase/sign/Euler-product information that forbids the `RE-144` product organization. Mere one-level sparsity, rightward mode count, or a shrinking unscaled neighborhood remains insufficient.

## Keep target anchoring, rightward complexity, radius loss, local cardinality and exterior cancellation separate

Target anchoring removes the rightmost-transfer loss, but it does not make the remaining left packet harmless. RE-144 shows that rightward count, far-left damping and high-height tails can all be benign while a growing near-left cluster carries the cancellation. RE-145 shows that the local price of that cluster is controlled by its scaled radius rather than its cardinality: positive empirical packets lose at most `exp(-O(R))`. Any closure should therefore compare this radius-dependent local floor explicitly with far-left/high-tail/exterior terms instead of folding all of them into “zero density.”

## Keep the exact binary tie local

The surviving first/depth-two Four-Exponentials contingency remains local and does not control the finite-edge packet analysis. A global argument should remain robust to that binary alternative unless exact transcendence becomes load-bearing.