# MI-042 — Faithful exact-law UCP readouts are rigid, with sharp channel-error, bias and propagation stability scales

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-337](../../findings/WP-337-approximate-barycentric-preservation-needs-bias-times-propagation-control.md). Kadison--Schwarz, Stinespring dilation, multiplicative-domain theory and the Bhatia--Davis variance inequality are classical; the Mathia content is their sharp source-readout boundary at expanding Mangoldt cutoffs.

WP-329--WP-330 show that enriched variables can be universally positive/divisible while all source specificity sits only in an external scalar state or in a fluctuation sector annihilated by that state. WP-331--WP-332 show the opposite: if a faithful UCP readout preserves the exact second moment of the same self-adjoint source observable, the positive Kadison defect vanishes. The observable lies in the multiplicative domain and the off-diagonal Stinespring block that could have carried hidden coupling is zero.

WP-333--WP-335 expose the nonuniform moving-tail loophole. A support-preserving barycentric Markov/UCP map can retain an order-one Kadison defect on a rare moving state while weak metrics, fixed finite divergences, max-divergence and even the operator norm of the channel on bounded functions tend to zero. The observable `X_R` itself grows with the cutoff, so a vanishing transition probability can multiply a squared jump of reciprocal size.

WP-336 makes the exact-barycentric case sharp. For row escape mass `epsilon_x` and one-sided propagation radii `L_-(x),L_+(x)`, exact preservation `Psi(X)=X` gives

`0 <= Q(x) <= epsilon_x L_-(x)L_+(x)`,

while `||Psi-I||=2 sup_x epsilon_x`. Hence

`||Psi(X^2)-X^2|| <= (1/2)||Psi-I|| sup_x L_-(x)L_+(x)`.

WP-337 shows that approximate barycentric preservation adds a second independent scale. Put `beta_x=Psi(X)(x)-x`. The sharp rowwise bound is

`Q(x) <= epsilon_x L_-(x)L_+(x) + beta_x(L_+(x)-L_-(x)) - beta_x^2`.

Consequently a uniform stability estimate needs both

`||Psi-I|| * sup_x L_-(x)L_+(x) -> 0`

and

`||Psi(X)-X|| * sup_x |L_+(x)-L_-(x)| -> 0`.

Small absolute coordinate bias is not enough. WP-337 gives an intrinsic dyadic Mangoldt example with channel norm tending to zero, coordinate bias tending to zero, and even vanishing max-divergence diagnostics, yet a fixed Kadison defect survives because a tiny one-sided bias is multiplied by a growing propagation asymmetry. In that example the bidirectional product itself is zero: the entire defect sits in the bias-times-asymmetry term.

The moving-observable stability ledger therefore has at least two distinct geometric amplifiers. Escape mass couples to **bidirectional spread** `L_-L_+`; barycentric bias couples to **propagation asymmetry** `|L_+-L_-|`. Exact martingale structure kills the second term, but once preservation is approximate it must be controlled at its own scale. Replacing this pair by an unnamed stronger topology obscures the actual mechanism.

The result remains generic rather than arithmetic. The sharp bounds hold for finite real spectra and Markov/UCP kernels; the Mangoldt ray provides an intrinsic realization but not source-selective sign. A viable Weil route still needs a source-forced coupling whose destination sign matched controls cannot reproduce, in addition to satisfying the correct moving-observable scale conditions.

**Boundary.** WP-336--WP-337 remain in the commutative Markov/UCP setting for one real coordinate. They do not cover genuinely noncommutative observables or channels outside this category. Approximate preservation requires the two scale-corrected error terms above; neither small channel norm nor small coordinate bias alone implies multiplicative-domain rigidity. Nothing here generates the Gamma/polar terms or proves Weil positivity.