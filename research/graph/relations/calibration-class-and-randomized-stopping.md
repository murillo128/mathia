---
id: RG-calibration-class-and-randomized-stopping
type: research-graph-relation
scope: arithmetic_fidelity-xi_flow
derived: true
---

# Calibration class and randomized stopping

This projects the explicit AF-to-Jacobi transfer in XF-204 and the function-class boundary in [[research/mind/intuition/MI-039-calibration-gluing-transfers-randomized-stopping-bounds-only-in-the-admitted-function-class|global MI-039]]. The common mechanism has different admissibility proofs and noise assumptions in the two lines.

## A fixed pair before the seed

[[research/arithmetic_fidelity/findings/AF-575-unknown-calibration-slack-requires-unbounded-sampling-depth|AF-575]] supplies finite exact stopping on each noiseless input with unknown strictly subcritical derivative calibration. [[research/arithmetic_fidelity/findings/AF-576-randomized-calibration-recovery-has-a-sharp-error-stopping-tail|AF-576]], equations (6)–(15), upgrades its finite-prefix obstruction to a randomized theorem: two fixed admissible inputs agree with the midpoint outside a shrinking interval near the excluded endpoint. For any capped adaptive policy, the probability of entering that interval tends to zero. The pair is selected after the policy and cap, before its seed.

[[research/xi_flow/findings/XF-204-randomized-jacobi-detection-has-a-sharp-error-stopping-tail|XF-204]], equations (7)–(17), explicitly transfers that coupling question but must preserve the queryable endpoint of a complex response. Its convex-velocity join matches both the endpoint value and the tail's value and derivative while retaining strict derivative slack. [[research/xi_flow/findings/XF-201-vanishing-jacobi-calibration-slack-has-quartic-row-cost|XF-201]], equations (6)–(11), supplies the strict speed decrease for the complete response, including the reciprocal term. [[research/xi_flow/findings/XF-203-unknown-jacobi-calibration-slack-admits-finite-certified-stopping|XF-203]], equations (8)–(12), supplies the pointwise finite certificate under one known total squared-noise budget.

In each binary experiment the capped minimax error is \(1/2\). Truncation and fair guessing give the sharp worst-case stopping tail \(1-2\alpha\) for error allowance \(\alpha<1/2\), despite finite cost at every input for an attaining policy. The worst-case input may change with the cap. These are explicit applications of [[research/prior_art/incremental/PA-le-cam-two-point-testing|classical two-point testing]], not a new general testing principle.

## Polynomial calibration changes the experiment

[[research/arithmetic_fidelity/findings/AF-577-unknown-polynomial-calibration-separates-continuous-randomness-from-finite-certification|AF-577]], equations (2)–(6), assumes a known finite family of real-analytic sources with nonpolynomial pairwise gaps and one polynomial nuisance of unknown finite, unbounded degree. Every finite deterministic transcript has another-label extension. Yet one continuously random exact validation coordinate, independent of all fitted interpolants, rejects every false analytic residual almost surely for each fixed input; degree \(d\) needs at most \(d+2\) observations, taking \(d=0\) for zero calibration. The interpolation-and-validation idea has [[research/prior_art/incremental/PA-polynomial-interpolation-early-termination|classical early-termination prior art]].

AF-577, equations (6a)–(6d), now gives the sharp finite-bit return/error law. For \(m\) labels, let \(e\) be the worst-case unconditional probability of returning a wrong label. On every fixed input \(y\),
\[
e\ge(1-1/m)\Pr_y(\text{return}).
\]
A finite collection of returning coin words has a finite union of queried coordinates. One polynomial per competing label matches all of those transcripts simultaneously, before the seed is drawn. Exhaustion of the returning cylinders proves the bound without a uniform or expected resource cap. Almost-sure return therefore has minimax error \(1-1/m\), attained by blind guessing, including under a fixed query budget. The distinction from AF-576 persists: arbitrary simultaneous interpolation need not preserve a derivative bound, and smooth gluing need not preserve polynomial calibration. [[research/arithmetic_fidelity/mind/intuition/MI-079-unknown-polynomial-calibration-separates-random-identification-from-certification|AF MI-079]] retains these quantifiers.

## Continuous randomness still has a fixed-budget polynomial barrier

[[research/arithmetic_fidelity/findings/AF-578-continuous-randomness-retains-fixed-budget-polynomial-calibration-obstruction|AF-578]], equations (2)–(10), closes AF-577's fixed-cap question under bounded source derivatives through order \(N-1\) on the closed bounded window. With \(m\) labels, every cap \(N\ge1\) has minimax error \(c_m=1-1/m\), already for degree-at-most-\(N-1\) calibration with unrestricted coefficients. A smooth source gap has a uniformly bounded monomial interpolation lift, including at arbitrarily close nodes. One broad Gaussian coefficient prior then gives transcript total variation at most \(B_N(g)/(2L)\), uniformly over adaptive policies; its scale \(L\) may grow because coefficients are unbounded. This is uncertainty over fixed calibrations, not measurement noise.

For sources smooth on the closed window, truncation gives \(e+c_mq_N\ge c_m\), with worst-case unconditional wrong-return probability \(e\) and \(q_N=\sup_x\Pr_x(T>N)\). Analytic nonpolynomial gaps permit the matching per-input exact continuous-validation branch from AF-577. With known degree \(d\), the exact continuous-query threshold is \(d+1\) queries at blind-guess minimax error versus \(d+2\) for almost-sure zero error. AF-571's implicit equation verifies the prime-edit source's endpoint regularity. No assertion covers arbitrary endpoint-singular analytic gaps, bounded coefficients, or an unbounded observation window.

## Positive noise retains the analytic Xi obstruction

[[research/xi_flow/findings/XF-205-analytic-jacobi-calibration-retains-the-noisy-stopping-obstruction|XF-205]], equations (7)–(12), supplies a different witness within baselines holomorphic on a fixed right half-plane. For a minimizing complete response \(F\), the scalar baselines \(\pm(1-\varepsilon)F/2\) have strictly subcritical derivative norm and yield opposite-label curves differing by \(\varepsilon F\). For each fixed row cap \(N\) and **positive** total-noise allowance \(\sigma\), priors on fixed bounded-energy noise sequences give
\[
\operatorname{TV}(P_{0,\varepsilon}^{\mathcal A},P_{1,\varepsilon}^{\mathcal A})
\le\min\{1,N^{3/2}\varepsilon\|F\|_\infty/\sigma\}.
\]
The sequences are chosen independently of the policy's seed. Sending \(\varepsilon\) to zero at fixed \(N,\sigma>0\) recovers capped error \(1/2\) and stopping tail \(1-2\alpha\). The exponent is a sufficient coupling estimate, not a sharp slack-dependent rate. XF-203's finite certificate remains valid on this subclass.

This extends the unknown-slack stopping obstruction without using XF-204's nonanalytic tail join. [[research/xi_flow/mind/intuition/MI-014-endpoint-preserving-calibration-joins-force-sharp-randomized-stopping-tails|Xi MI-014]] and [[research/xi_flow/mind/intuition/MI-015-positive-noise-retains-analytic-calibration-stopping-obstruction|Xi MI-015]] retain the two different witnesses. In the restricted known-direction model \(B=cF\), \(|c|<1/2\), a single noiseless query at a nonzero source value determines the label. XF-205 alone therefore does not settle the noiseless full analytic class; XF-206 supplies a different witness below.

## Noiseless holomorphic Xi requires additional polynomial directions

[[research/xi_flow/findings/XF-206-noiseless-analytic-calibration-retains-sharp-stopping-tails|XF-206]], equations (7)–(20), closes the full-class noiseless boundary. For the minimizing complete source, XF-201's strict speed decrease supplies \(v=|F'|\), \(v(Q)=D\), and \(\kappa=\min(-v')>0\). At cap \(N\), the polynomial space spanned by \(1,s^2,\ldots,s^{2N-2}\), \(s=(r-Q)/Q\), has full evaluation rank on every at-most-\(N\) distinct real node bank, including the endpoint. Every polynomial in this space has first derivative zero at that endpoint. The coefficient region \(\sum_{k=1}^{N-1}2k|a_k|\le\kappa Q^2/4\) leaves strictly subcritical derivative room when added to the two scalar baselines from XF-205, independently of their shrinking gap parameter \(\varepsilon\).

A small Gaussian coefficient prior has arbitrarily high mass inside that region. For each fixed policy, common-history conditional Gaussian continuity gives convergence of the capped transcript laws as \(\varepsilon\to0\); conditioning the prior costs at most \(\eta\) per label. The bound is \(2\eta+o_{\varepsilon\to0}(1)\), with the positive Gaussian scale fixed before taking the gap limit. There is no policy-uniform rate or uniform lower conditional variance. Each supported polynomial is fixed before the seed. No two analytic curves are asserted to agree on an interval.

The capped error is \(1/2\) and the sharp stopping tail is \(1-2\alpha\), now for every total-noise allowance \(\sigma\ge0\); XF-203 supplies the separate finite per-input certificate. This does not extend the noiseless claim to the restricted supplied scalar class, which retains its one-query test. The affine control has \(\kappa=0\) and is distinguished by two endpoint values. A supplied slack floor, derivative oracle or prescribed smaller analytic class changes the experiment.

Both new findings explicitly use [[research/prior_art/incremental/PA-gaussian-conditioning-adaptive-linear-information|classical Gaussian conditioning under adaptive linear information]]. Global MI-039 documents their precise correspondence: AF permits broad coefficient uncertainty and a uniform smooth-gap interpolation bound; Xi requires endpoint-flat uncertainty with bounded nonconstant coefficients and a shrinking source gap, with only fixed-policy convergence. Their shared prior art alone would not establish this bridge. The findings prove their own source admissibility and testing limits; the classical linear-approximation results are not substituted for discrete-label recovery.

## Limits of the bridge

The AF derivative slack convention is twice the Xi convention after identifying the critical derivative magnitude. Global MI-039 explicitly compares the intersecting uniform closures: AF-577's supremum-bounded errors can alias whole curves, whereas XF-205 uses a total-energy constraint to obtain near-indistinguishable finite transcript laws. This does not alias all infinite observations; Xi retains pointwise exact stopping. The two noise conclusions are not interchangeable. Neither source supplies physical Xi access, ordinary-prime identification, or an RH implication. There is no proved classification of all analytic or quasianalytic calibration classes. The direct AF-576-to-XF-204 relation is supported by XF-204's explicit transfer passage, independently of their shared prior-art citation.
