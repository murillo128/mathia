# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with a terminal moment hierarchy

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstructions [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md), [RE-155](../../findings/RE-155-pnt-stable-source-surgery-survives-to-any-fixed-fraction-of-the-robin-horizon.md), the ordinary-prime relocation capacity law [RE-156](../../findings/RE-156-terminal-source-relocation-capacity-has-a-fourth-root-transition.md), the first-order generalized insertion boundary [RE-157](../../findings/RE-157-pnt-small-insertion-placement-squares-the-terminal-ambiguity-scale.md), and the endpoint-count/Chebyshev-matched curvature law [RE-158](../../findings/RE-158-terminal-count-and-chebyshev-mass-matching-restore-the-fourth-root-ambiguity-scale.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral has a canonical positive kernel. After normalization and rescaling `t=py`, the kernel converges to the Pareto law `(1/2)y^(-3/2)dy`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154--RE-155 show that this destination remains highly sensitive to coherent post-selector source placement even when the control agrees exactly with the ordinary source through most of the canonical horizon `U=U_A(p)` and remains PNT-indistinguishable.

RE-156 identifies the capacity boundary for **equal-cardinality ordinary-prime relocation** inside the shrinking terminal layer `T_p(epsilon)=[(1-epsilon)U,U]`:

`Cap_p(epsilon) asymp epsilon^2 sqrt(p) log p / log U`.

The transition is

`epsilon_*(p)=sqrt(log U/(sqrt(p)log p))`.

The square in this law has two origins: one factor `epsilon` is the influence range across the terminal layer, while the second comes from the number `Theta(epsilon U/log U)` of ordinary primes locally available to delete and relocate. Thus `epsilon_*` is a genuine **ordinary-source local-supply boundary**, not automatically an information threshold for coarse PNT data.

RE-157 separates those notions. Allow matched generalized-prime controls that add `m_p=delta_p U/log U` non-prime labels in the terminal layer with `delta_p->0`, comparing equal-cardinality packets placed near opposite ends. There is no local deletion cap, and the first placement moment gives separation

`(1/2+o(1)) delta_p epsilon_p / epsilon_PNT(p)`,

where

`epsilon_PNT(p)=log U/(sqrt(p)log p)=epsilon_*(p)^2`.

Whenever `epsilon_p/epsilon_PNT(p)->infinity`, one can choose `delta_p->0` and still obtain any prescribed order-one separation while counting and Chebyshev perturbations remain globally PNT-small. This identifies the first-moment ambiguity left by coarse terminal control.

RE-158 then matches one more source statistic **exactly**. Equal cardinality fixes the terminal counting increment; equality of total `sum log q_i` fixes the terminal Chebyshev increment and, in logarithmic terminal coordinates `z_i=log(U/q_i)`, cancels the entire linear placement moment. The exact Robin influence then begins at quadratic order in the difference of packet spreads:

`Cap_p^(theta)(epsilon,delta) asymp delta epsilon^2 sqrt(p) log p / log U = delta (epsilon/epsilon_*)^2`.

Therefore endpoint `pi` and endpoint `theta` matching raises the lower ambiguity scale back to `epsilon_*`: if `epsilon/epsilon_*->infinity`, a vanishing insertion budget can still create order-one source separation, while every such endpoint-matched insertion family is `o(1)`-stable for `epsilon=O(epsilon_*)`.

The reappearance of `epsilon_*` must not be conflated with RE-156. In ordinary relocation the second `epsilon` is a **supply factor**. In RE-158 it is a **moment-cancellation factor** exposing the curvature of the influence kernel. Two architectures can therefore share the same exponent while consuming different source resources.

The source audit is now a moment hierarchy rather than a single “PNT resolution” threshold. Coarse PNT plus terminal count leaves first-order placement freedom down to `epsilon_PNT`. Exact terminal count plus total Chebyshev mass kills that linear mode but still leaves quadratic spread above `epsilon_*`. A positive theorem must say what controls the *internal placement* of Chebyshev mass inside the terminal layer—through stronger short-interval information, higher matched moments, or source-specific CA/ordinary-prime structure—rather than treating endpoint values as sufficient.

The reusable distinction is between ambient source closeness, local source supply, matched endpoint moments and destination-weighted curvature. A perturbation can be negligible for prime counting and exact in low-order endpoint summaries while retaining order-one destination leverage through the next unresolved placement moment. A transition should therefore be attributed to the exact resource that creates it, not merely to its exponent.

**Boundary.** RE-156 classifies ordinary equal-cardinality terminal relocation; RE-157 classifies vanishing-budget generalized insertion placement with unmatched first moment; RE-158 classifies the subclass with exact endpoint count and Chebyshev-mass matching. None says the ordinary primes realize the synthetic controls, proves source control at or below `epsilon_*`, or excludes higher-moment, signed/nonlocal, explicit-formula or global CA constraints. The scales identify what the known matched controls consume, not a positive Robin theorem.
