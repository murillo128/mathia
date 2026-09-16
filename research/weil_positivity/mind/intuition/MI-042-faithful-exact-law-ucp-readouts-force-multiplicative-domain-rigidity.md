# MI-042 — Faithful exact-law UCP readouts are rigid, with a sharp channel-error × propagation stability threshold

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-336](../../findings/WP-336-ucp-kadison-defect-is-controlled-by-channel-norm-times-bidirectional-propagation.md). Kadison--Schwarz, Stinespring dilation, multiplicative-domain theory and the Bhatia--Davis variance inequality are classical; the Mathia content is their sharp source-readout boundary at expanding Mangoldt cutoffs.

WP-329--WP-330 show that enriched variables can be universally positive/divisible while all source specificity sits only in an external scalar state or in a fluctuation sector annihilated by that state. WP-331--WP-332 show the opposite: if a faithful UCP readout preserves the exact second moment of the same self-adjoint source observable, the positive Kadison defect vanishes. The observable lies in the multiplicative domain and the off-diagonal Stinespring block that could have carried hidden coupling is zero.

WP-333--WP-335 expose the nonuniform moving-tail loophole. A support-preserving barycentric Markov/UCP map can retain an order-one Kadison defect on a rare moving state while weak metrics, fixed finite divergences, max-divergence and even the operator norm of the channel on bounded functions tend to zero. The reason is not hidden scalar-law distance: the observable `X_R` itself grows with the cutoff, and a vanishing transition probability can multiply a squared jump of reciprocal size.

WP-336 turns that qualitative scale mismatch into an exact threshold. For each row `x`, let `epsilon_x` be the mass leaving `x`, and let `L_-(x),L_+(x)` be the largest source-coordinate displacements available to the left and right. Exact martingale preservation `Psi(X)=X` makes the Kadison defect a conditional variance, and Bhatia--Davis gives

`0 <= Q(x) <= epsilon_x L_-(x)L_+(x)`.

The channel norm records exactly the escape mass,

`||Psi-I|| = 2 sup_x epsilon_x`,

so globally

`||Psi(X^2)-X^2|| <= (1/2)||Psi-I|| sup_x L_-(x)L_+(x)`.

Therefore bounded-channel convergence is sufficient for asymptotic multiplicative-domain rigidity precisely when it is **subcritical relative to bidirectional propagation**:

`||Psi_R-I|| B_R -> 0`,  with  `B_R=sup_x L_(-,R)(x)L_(+,R)(x)`.

The asymmetric dyadic construction of WP-335 saturates the estimate: its channel error is `Theta(1/a_R)`, its propagation product is `Theta(a_R)`, and its defect remains exactly `(log 2)^2`. The surviving loophole is consequently not “bounded topologies can always miss the tail”; it is the critical/supercritical regime in which channel error and source-coordinate propagation compensate one another.

This is sharper than replacing sup norm by an unspecified energy or graph norm. Any proposed stronger topology for the same martingale coordinate should be audited by whether it controls the concrete product above or an equivalent second-moment quantity. Conversely, a construction that keeps a fixed defect while `||Psi_R-I||->0` must spend diverging bidirectional propagation at least on the reciprocal channel-error scale, or leave one of the theorem's hypotheses.

The mechanism remains generic rather than arithmetic. The sharp variance bound applies to every finite real spectrum and every barycentric Markov kernel; the dyadic Mangoldt ray supplies an intrinsic realization but not source-selective sign. A viable Weil route still needs a source-forced coupling whose destination sign matched martingale controls cannot reproduce, in addition to satisfying the correct moving-observable stability scale.

**Boundary.** WP-336 assumes a commutative Markov/UCP self-map preserving the same real coordinate exactly. It does not cover approximate barycentric preservation without an additional bias term, genuinely noncommutative observables, channels outside this category, or critical/supercritical propagation. It also does not generate the Gamma/polar terms or prove Weil positivity.
