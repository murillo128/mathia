# MI-042 — Faithful exact-law UCP readouts are rigid, and quadratic transport is the sharp moving-observable stability scale

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-338](../../findings/WP-338-quadratic-wasserstein-is-the-sharp-ucp-defect-threshold.md). Kadison--Schwarz, Stinespring dilation, multiplicative-domain theory, Bhatia--Davis variance and Wasserstein moment monotonicity are classical; the Mathia content is their sharp source-readout boundary at expanding Mangoldt cutoffs.

WP-329--WP-330 show that enriched variables can be universally positive/divisible while all source specificity sits only in an external scalar state or in a fluctuation sector annihilated by that state. WP-331--WP-332 show the opposite: if a faithful UCP readout preserves the exact second moment of the same self-adjoint source observable, the positive Kadison defect vanishes. The observable lies in the multiplicative domain and the off-diagonal Stinespring block that could have carried hidden coupling is zero.

WP-333--WP-335 expose the nonuniform moving-tail loophole. A support-preserving barycentric Markov/UCP map can retain an order-one Kadison defect on a rare moving state while weak metrics, fixed finite divergences, max-divergence and even the operator norm of the channel on bounded functions tend to zero. The observable `X_R` itself grows with the cutoff, so a vanishing transition probability can multiply a squared jump of reciprocal size.

WP-336 makes the exact-barycentric case sharp. For row escape mass `epsilon_x` and one-sided propagation radii `L_-(x),L_+(x)`, exact preservation `Psi(X)=X` gives

`0 <= Q(x) <= epsilon_x L_-(x)L_+(x)`,

while `||Psi-I||=2 sup_x epsilon_x`. WP-337 shows that approximate barycentric preservation adds an independent scale. Put `beta_x=Psi(X)(x)-x`; then

`Q(x) <= epsilon_x L_-(x)L_+(x) + beta_x(L_+(x)-L_-(x)) - beta_x^2`.

Thus channel error is amplified by bidirectional spread and barycentric bias by propagation asymmetry. Small raw errors do not imply rigidity unless these products vanish at the moving observable's scale.

WP-338 identifies the exact invariant behind that ledger. For the transition law `P_x` and the source atom `delta_x`, transport has a unique coupling, so

`W_2(P_x,delta_x)^2 = Q(x) + beta_x^2`.

With exact barycentric preservation this is simply `Q(x)=W_2^2`. For every `p>=2`, probability-space moment monotonicity gives

`Q(x) <= W_2(P_x,delta_x)^2 <= W_p(P_x,delta_x)^2`.

For every `1<=p<2`, however, a mass `a^(-2)` moved a distance `a h` has `W_p^p=h^p a^(p-2)->0` while retaining defect `h^2`. A symmetric version preserves the barycenter exactly on the dyadic prime-power ray; the one-sided WP-337 Mangoldt witness simultaneously keeps channel norm, max-divergence and absolute coordinate bias small. Thus exponent two is the sharp transport threshold on growing supports.

This closes a tempting but circular repair. Requiring rowwise `W_2->0` certainly restores multiplicative-domain stability, but only because `W_2^2` is exactly the desired second-moment defect plus squared first-moment bias. Subquadratic Wasserstein topology misses rare long jumps; superquadratic topology imposes more than the quadratic target requires. Ordinary rowwise transport therefore supplies no independent arithmetic sign theorem.

The reusable stability object is the **quadratic displacement energy**. The propagation formulas of WP-336--WP-337 are geometric upper bounds that can force it small under suitable source constraints; `W_2` measures it directly. A viable Weil route must derive decay of this quadratic energy from source-specific structure that matched controls cannot fake, or leave the commutative rowwise category for a genuinely global/noncommutative coupling with additional sign content.

**Boundary.** WP-336--WP-338 remain in the commutative Markov/UCP setting for one real coordinate. The `p=2` threshold uses growing support; on uniformly bounded support lower transport moments can control higher ones with diameter-dependent constants. None of these results generates the Gamma/polar terms, a source-selective sign, or Weil positivity, and `W_2` control should not be counted as a new mechanism when it merely restates vanishing Kadison defect.