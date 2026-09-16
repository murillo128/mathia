# MI-032 — Self-tangent Robin height is a Pareto-weighted Chebyshev-deficit average with distinct ordinary-supply and coarse-PNT terminal scales

**Evidence level:** exact-derived source-side reformulation from [RE-153](../../findings/RE-153-self-tangent-counterexamples-force-a-pareto-chebyshev-deficit-barrier.md), sharpened by the matched synthetic-source obstructions [RE-154](../../findings/RE-154-square-root-over-log-post-selector-relocations-move-pareto-robin-source-by-order-one.md), [RE-155](../../findings/RE-155-pnt-stable-source-surgery-survives-to-any-fixed-fraction-of-the-robin-horizon.md), the ordinary-prime relocation capacity law [RE-156](../../findings/RE-156-terminal-source-relocation-capacity-has-a-fourth-root-transition.md), and the coarse-PNT insertion-placement boundary [RE-157](../../findings/RE-157-pnt-small-insertion-placement-squares-the-terminal-ambiguity-scale.md), using the canonical finite-annulus threshold of RE-022.

For a sufficiently large regular self-tangent Robin counterexample with largest active first-layer prime `p`, the mixed Mertens--Chebyshev height integral has a canonical positive kernel. After normalization and rescaling `t=py`, the kernel converges to the Pareto law `(1/2)y^(-3/2)dy`, and the counterexample condition becomes

`E_(nu_p)[(t-vartheta(t))/sqrt(t)] >= sqrt(2)-o(1)`.

RE-154--RE-155 show that this destination remains highly sensitive to coherent post-selector source placement even when the control agrees exactly with the ordinary source through most of the canonical horizon `U=U_A(p)` and remains PNT-indistinguishable.

RE-156 identifies the capacity boundary for **equal-cardinality ordinary-prime relocation** inside the shrinking terminal layer `T_p(epsilon)=[(1-epsilon)U,U]`:

`Cap_p(epsilon) asymp epsilon^2 sqrt(p) log p / log U`.

The transition is

`epsilon_*(p)=sqrt(log U/(sqrt(p)log p))`.

The square in this law has two origins: one factor `epsilon` is the influence range across the terminal layer, while the second comes from the number `Theta(epsilon U/log U)` of ordinary primes locally available to delete and relocate. Thus `epsilon_*` is a genuine **ordinary-source local-supply boundary**, not automatically an information threshold for coarse PNT data.

RE-157 separates those notions. Allow matched generalized-prime controls that add `m_p=delta_p U/log U` non-prime labels in the terminal layer with `delta_p->0`, comparing equal-cardinality packets placed near opposite ends. There is no local deletion cap, and their source-coordinate separation is

`(1/2+o(1)) delta_p epsilon_p / epsilon_PNT(p)`,

where

`epsilon_PNT(p)=log U/(sqrt(p)log p)=epsilon_*(p)^2`.

Whenever `epsilon_p/epsilon_PNT(p)->infinity`, one can choose `delta_p->0` and still obtain any prescribed order-one separation while the counting and Chebyshev perturbations remain `o(U/log U)` and `o(U)`. At the RE-156 scale `epsilon=epsilon_*`, order-one ambiguity already survives with only `delta_p asymp epsilon_* ->0`. Therefore the fourth-root threshold cannot be interpreted as the point where PNT information begins to determine the terminal Robin source.

Conversely, for insertion-placement controls using only `o(U/log U)` terminal labels, `epsilon=O(epsilon_PNT)` makes their placement leverage `o(1)`. The squared scale is thus the sharp lower envelope for this **vanishing coarse-PNT insertion class**, not a theorem that all generalized perturbations or the actual ordinary source are controlled there.

The propagation audit now has two distinct bills. To beat the ordinary relocation control, source information must cross `epsilon_*`. To infer the terminal source from coarse PNT information alone, it must survive the much thinner `epsilon_PNT=epsilon_*^2` ambiguity or introduce a genuinely local ordinary-prime/CA constraint that forbids generalized-source placement freedom. Global prime-density approximation by itself cannot supply that rigidity.

The reusable distinction is between ambient source closeness, local source supply and destination-weighted capacity. A perturbation can be negligible for prime counting, exact on almost the whole finite horizon, and still carry order-one destination leverage. A transition found under an ordinary-source relocation model should not be promoted to an identifiability threshold until the local supply assumption responsible for it has been isolated.

**Boundary.** RE-156 classifies ordinary equal-cardinality terminal relocation; RE-157 classifies vanishing-budget generalized insertion placement. Neither says the ordinary primes realize the synthetic controls, proves source control below `epsilon_PNT`, or excludes signed/nonlocal perturbations, stronger short-interval information, explicit-formula restrictions or global CA identities. The two scales identify what the known matched controls consume, not a positive Robin theorem.
