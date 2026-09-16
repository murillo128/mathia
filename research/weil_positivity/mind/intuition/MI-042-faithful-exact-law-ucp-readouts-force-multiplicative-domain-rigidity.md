# MI-042 — Faithful exact-law UCP readouts are rigid, but averaged scalar convergence misses rare moving defects

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-334](../../findings/WP-334-finite-information-divergences-miss-bounded-likelihood-ucp-tail-defects.md). Kadison--Schwarz, Stinespring dilation, multiplicative-domain theory and standard information divergences are classical; the Mathia content is their source-readout boundary at expanding Mangoldt cutoffs.

The operator-valued route has two opposite failure modes. WP-329--WP-330 show that enriched variables can be universally positive/divisible while all source specificity sits only in an external scalar state or in a fluctuation sector annihilated by that state. WP-331--WP-332 show the opposite: if a faithful UCP readout preserves the exact second moment of the same self-adjoint source observable, the positive Kadison defect must vanish. The observable lies in the multiplicative domain, and the off-diagonal Stinespring block that could have carried hidden coupling is zero.

At a finite atomic cutoff the exact stability modulus is

`||D_R|| <= tau_R(D_R)/m_R`,

where `m_R` is the least output-state atom. Approximate scalar second-moment preservation therefore implies approximate multiplicative-domain rigidity only at the **relative** scale `tau_R(D_R)=o(m_R)`. A sequence of faithful states need not be uniformly faithful, and the finite Mangoldt least mass decays rapidly along a moving prime-power tail.

WP-333 makes this sharp inside the exact Mangoldt support. On three consecutive dyadic log points `y_R-h,y_R,y_R+h`, `h=log2`, a Markov/UCP self-map can fix the coordinate observable pointwise while retaining Kadison defect `(log2)^2` at the middle atom and Stinespring coupling `log2`. As that atom moves into vanishing source mass, the induced scalar laws converge in total variation, every fixed polynomial moment and every fixed Wasserstein metric, while the maps remain order-one apart in operator norm.

WP-334 shows that this is not repaired by ordinary information-theoretic topology. Add a fixed laziness parameter `epsilon` to preserve the same support and obtain mutually absolutely continuous laws with likelihood ratio `L_R` satisfying fixed bounds

`epsilon <= L_R <= 1+(1-epsilon)2^s`.

Only three atoms change and their total source mass is `O(r_R)`. Therefore every continuous finite-valued Csiszar `f`-divergence on the compact likelihood-ratio range tends to zero in **both directions**. The same holds for every fixed finite Renyi order. In particular two-sided KL, chi-square, Hellinger and Jensen--Shannon convergence can coexist with the same order-one operator defect and fixed map-level separation.

The endpoint `alpha=infinity` behaves differently. Max-divergence records the worst likelihood ratio rather than averaging it against source mass: one direction equals `log(1/epsilon)` and the other tends to `log(1+(1-epsilon)2^s)`. Thus the constructed tail defect defines a clean topology threshold:

**finite averaged divergence can forget a rare moving coupling even under bounded likelihood ratios; essential-supremum likelihood control cannot.**

This strengthens the readout principle. Exact faithful same-observable recovery is rigid at each fixed cutoff, but asymptotic scalar-law recovery is not a substitute for uniform map control. “Use a stronger divergence” is too vague: any topology whose cost is integrated against vanishing source mass can still ignore an order-one defect unless its modulus is explicitly tied to the smallest visible atom.

The support-preserving construction remains a matched martingale mechanism, not arithmetic leverage. Arithmetic supplies an intrinsic equally spaced thin ray, but the same barycentric move is generic. A positive Weil route therefore needs either relative faithfulness strong enough to beat the moving atom, a max/uniform likelihood or direct map topology, a different observable/interface, or a source-forced coupling whose destination sign cannot be reproduced by the matched control.

**Boundary.** The exact rigidity concerns the same self-adjoint observable and its second moment under a faithful output state. WP-334 calibrates scalar topologies on one explicit intrinsic tail escape; it does not prove that max-divergence is sufficient for Weil positivity, trivialize the full dilation algebra, or rule out couplings through other observables. The finite-divergence no-go is about averaged scalar readouts, not every possible operator topology.
