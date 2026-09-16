# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with a fixed-order terminal moment hierarchy

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstructions [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md), [RE-155](../../findings/RE-155-pnt-stable-source-surgery-survives-to-any-fixed-fraction-of-the-robin-horizon.md), the ordinary-prime relocation capacity law [RE-156](../../findings/RE-156-terminal-source-relocation-capacity-has-a-fourth-root-transition.md), the first-order generalized insertion boundary [RE-157](../../findings/RE-157-pnt-small-insertion-placement-squares-the-terminal-ambiguity-scale.md), the endpoint-count/Chebyshev-matched curvature law [RE-158](../../findings/RE-158-terminal-count-and-chebyshev-mass-matching-restore-the-fourth-root-ambiguity-scale.md), and the all-fixed-order terminal moment hierarchy [RE-159](../../findings/RE-159-fixed-terminal-moment-matching-has-a-sharp-root-scale-ambiguity-hierarchy.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral has a canonical positive kernel. After normalization and rescaling `t=py`, the kernel converges to the Pareto law `(1/2)y^(-3/2)dy`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154--RE-155 show that this destination remains highly sensitive to coherent post-selector source placement even when the control agrees exactly with the ordinary source through most of the canonical horizon `U=U_A(p)` and remains PNT-indistinguishable.

RE-156 identifies the capacity boundary for **equal-cardinality ordinary-prime relocation** inside the shrinking terminal layer. Its capacity is

`Cap_p(epsilon) asymp epsilon^2 sqrt(p) log p / log U`,

with transition

`epsilon_*(p)=sqrt(log U/(sqrt(p)log p))`.

The square has two origins: one factor `epsilon` is terminal influence variation, while the second is the local ordinary-prime supply available to relocate. Thus `epsilon_*` is an ordinary-source supply boundary, not automatically a coarse-PNT information threshold.

RE-157 separates those notions. Matched generalized-prime controls with equal cardinality but unconstrained terminal placement retain a first-order mode whose transition is

`epsilon_PNT(p)=log U/(sqrt(p)log p)=epsilon_*(p)^2`.

Whenever `epsilon/epsilon_PNT->infinity`, a vanishing insertion budget can still yield order-one destination separation while global counting/Chebyshev perturbations remain PNT-small.

RE-158 matches one more source statistic exactly. Equality of total `sum log q_i` cancels the entire linear placement moment in logarithmic terminal coordinates `z_i=log(U/q_i)`, so the first surviving source freedom is quadratic spread and the transition returns to `epsilon_*`. The same exponent therefore has different causes in RE-156 and RE-158: local supply versus moment cancellation.

RE-159 proves that this is not a two-level accident. For every fixed integer `r>=1`, if two equal-cardinality terminal packets match their logarithmic-position power sums through order `r-1`, the first unconstrained Robin influence is the `r`-th placement moment. The sharp scale is

`epsilon_r(p)=[log U/(sqrt(p)log p)]^(1/r)`.

More precisely, the destination separation has leading term proportional to the difference of `sum z_i^r`, with coefficient `b_r(U)=1/r!+O_r(U^-1)` for `r>=2`, and an `O_r(m epsilon^(r+1))` remainder. Prouhet--Thue--Morse equal-power partitions give matched packets whose `r`-th moment separation is `asymp_r m epsilon^r`, so the upper bound is sharp. For a vanishing insertion intensity `m~delta U/log U`,

`Cap_p^(r)(epsilon,delta) asymp_r delta (epsilon/epsilon_r)^r`.

Thus every additional fixed matched terminal moment takes **one more root of the same coarse-PNT scale**. Order-one ambiguity persists above `epsilon_r` with `delta->0`, while this fixed-`r` matched class is `o(1)`-stable at `epsilon=O(epsilon_r)`.

The source audit is therefore a genuine moment hierarchy, not a single terminal-resolution threshold. Endpoint count controls the zeroth moment; total Chebyshev mass controls the first logarithmic placement moment; matching further terminal power sums pushes ambiguity into successively higher derivatives of the exact Robin influence kernel. A positive theorem must identify what *source-native* arithmetic structure controls this hierarchy or replaces it by a stronger non-moment constraint. Merely adding finitely many terminal summaries cannot be treated as complete source identification without pricing the next unresolved moment.

The reusable distinction is between ambient source closeness, local source supply, the number/order of matched terminal moments and destination-weighted Taylor sensitivity. A perturbation can be negligible for prime counting and exact in any prescribed fixed set of terminal moments while retaining order-one destination leverage through the next unresolved placement moment at its corresponding root scale.

**Boundary.** RE-159 classifies every fixed matched moment order for the generalized insertion model and proves sharp matched controls using classical equal-power constructions. It does not let `r` grow with `p`, prove that ordinary primes realize the synthetic controls, establish positive source control at the moving root scales, or exclude non-moment, signed/nonlocal, explicit-formula or global colossally-abundant constraints. The hierarchy identifies what fixed-order summaries fail to determine, not a positive Robin theorem.
