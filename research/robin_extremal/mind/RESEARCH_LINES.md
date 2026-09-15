# Robin-extremal research lines

This file holds the current mathematical questions suggested by the durable robin-extremal intuitions. It is not a roadmap, task queue, status page, or history.

## Price one-sided near-left cancellation by reciprocal-scale radius and compare it with the exterior budget

**Linked intuitions:** `MI-001-robin-failure-requires-self-tangent-half-mass-event-gaps` through `MI-030-scale-maximal-anchoring-converts-rightward-horizontal-advantage-into-an-exponential-shell-budget`.

RE-112--RE-138 reduce the attained finite-edge branch to a strong atom plus reciprocal-scale cancellation geometry. RE-139--RE-142 show that rightmost-anchored Turán visibility can lose an unusable transfer factor even under strong upper source envelopes. RE-143 removes that transfer by anchoring at the original algebraically strong atom and applying Turán's First Main Theorem only to zeros on or to its right.

RE-144 then closes the naive shrinking-slab hope: a matched simple spectrum can have a strong target with **exactly one** retained mode on or to its right, negligible far-left and high-height tails, and still hide the target on a fixed-relative observation window using a near-left cluster whose scaled radius `R(U)` tends to infinity as slowly as prescribed. The cluster may lie inside `o(log U/U)` width, and scaled radius only `O(log B)` already supports polynomial suppression in local cardinality `B`.

RE-145 adds the missing rate. For the positive empirical-measure representation underlying the Robin packet, every packet confined to scaled radius `R` has normalized local visibility at least `exp(-O_kappa(R))`, uniformly in cardinality and arrangement. This exponential dependence is the correct functional order in the matched class: the `RE-144` product packets attain exponential suppression in scaled radius after normalization. Hence `R(U)=o(log U)` still leaves a `U^{-o(1)}` local floor even though it does **not** restore a fixed positive floor and therefore still permits qualitative `o(M_0)` hiding.

RE-146 prices the first actual-zeta exterior piece in the same variable. If the anchor is chosen to maximize the leading Robin atom at scale `U`, then a rightward displacement `R/U` forces its coefficient ratio to be at most `e^{-R}` and therefore forces exponential ordinate inflation. On a fixed earlier subwindow this becomes a fractional coefficient moment; Ingham zero density then gives a rightward-shell budget of the form

\[
(1+|\gamma_0|)^{\nu+\varepsilon}
\exp\!\left[-\left(\eta-\frac{\nu+\varepsilon}{2}\right)R\right],
\]

relative to the anchor, provided `2 eta>nu=nu_I(sigma_-)`. For an algebraically strong anchor, `1+|gamma_0|<<U^(A/2)`, so `R=lambda log U` with sufficiently large fixed `lambda` makes this shell negligible. This does not yet control the near-left layer, nor zeros horizontally within `R/U` but vertically remote, and the `RE-145` witness still has to be synchronized with the early subwindow where the shell estimate is summable.

The frontier is therefore now a three-way rate comparison rather than a generic “exterior” problem: local reciprocal-box visibility `exp(-O(R))`, the explicit rightward-shell budget from `RE-146`, and the two unresolved pieces consisting of near-left cancellation and vertically remote near-horizontal modes. A useful source theorem may control either unresolved piece strongly enough to leave one common `R(U)` and one common observation point where the local floor wins. Otherwise one needs genuinely relational phase/sign/Euler-product information that forbids the `RE-144` product organization. Mere one-level sparsity or a shrinking unscaled neighborhood remains insufficient.

## Keep target anchoring, rightward complexity, radius loss, local cardinality and exterior cancellation separate

Target anchoring removes the rightmost-transfer loss, but it does not make the remaining left packet harmless. RE-144 shows that rightward count, far-left damping and high-height tails can all be benign while a growing near-left cluster carries the cancellation. RE-145 shows that the local price of that cluster is controlled by its scaled radius rather than its cardinality: positive empirical packets lose at most `exp(-O(R))`. RE-146 shows that one particular exterior component, the sufficiently-rightward horizontal shell of a scale-maximal anchor, can also be priced exponentially in `R` using actual zero density. Any closure should keep that shell distinct from the near-left and vertically remote pieces instead of folding all of them into “zero density.”

## Keep the exact binary tie local

The surviving first/depth-two Four-Exponentials contingency remains local and does not control the finite-edge packet analysis. A global argument should remain robust to that binary alternative unless exact transcendence becomes load-bearing.