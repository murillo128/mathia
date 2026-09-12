# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Match source sign complexity to a quantitative finite-order Euler modulus

**Linked intuition:** `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`.

AF-215--AF-220 force ordered sign complexity but leave the quantitative transfer into the shrinking Euler-log observation window open. The next theorem must relate the source sign budget to a separation or curvature modulus at the resolution actually consumed by the target.

## Price the actual target metric before calling a representation compressed

**Linked intuitions:** `MI-019-faithful-translation-lifts-are-affine`, `MI-020-prime-tail-localization-has-an-information-conservation-law`.

AF-221--AF-233 show that localization has a real information bill and that contraction can lower it only in the metric actually used downstream. A useful compression claim still needs both a cheaper target geometry and a theorem that the final arithmetic argument consumes only that target.

## Build cancellation-coherent source access to the Li root-rate class

**Linked intuitions:** `MI-021-coarse-rh-endpoints-can-still-require-deep-source-access`, `MI-022-prefix-truncation-must-respect-cancellation-orbits`.

AF-234--AF-243 show that the RH root-rate endpoint tolerates large output error but is extremely sensitive to breaking the binomial cancellation orbit in the source representation. The live bridge must assemble the required cancellation orbit before the root-rate quotient is formed.

## Separate source category, breadth, coupling, resolution, sampling, and timing geometry

**Linked intuitions:** `MI-003-fidelity-endpoints-are-category-dependent`, `MI-023-local-completeness-can-preserve-a-root-rate-discriminator-at-zero-density`, `MI-024-periodic-completeness-turns-li-cancellation-into-profinite-leakage`, `MI-025-regular-sampling-separates-aliasing-from-finite-window-stability`.

AF-244--AF-276 show that coarse symmetry, zero counting, endpoint jets, compact-open proximity, and periodic transport do not replace an exact source-category argument. Bounded Euler degree makes local prime-power depth finite and sharp, but global Euler fidelity still requires information at infinitely many prime locations. AF-275--AF-276 further show that finite collections of exact values or jets leave positive-dimensional tail fibers even inside degree-one Euler products.

AF-278--AF-281 separate continuous time breadth, one-lattice aliasing, marginal coupling loss, and exact mixed-channel recovery. If all mixed samples `F(c+i(k_1h_1+...+k_Jh_J))` are retained, ordinary Dirichlet coefficient fidelity is equivalent to `cap_j R_(h_j)={1}`; separate resonant marginals do not have the same information.

AF-282--AF-285 price the finite-prefix two-prime repair. On the known prefix `1,...,N`, joint phase spacing is `Theta(1/N)`, uniform stable coefficient recovery has sharp coordinatewise mixed degree `Theta(N)`, and linear-size raw acquisition is possible. AF-287 strengthens the sample-selection statement: classical frame sparsification yields an **unweighted `O(N)` subset of raw mixed samples with uniformly bounded condition number**. For arbitrary rowwise offsets `|tau_j|<=T`, the exact matrix expansion gives fixed relative `ell^2` coefficient distortion on the sharp scale `T=Theta(1/log N)`.

AF-288 separates that coefficient bill from the target: a common offset acts by `(a_n)->(a_n n^{-i tau})` and `F(s)->F(s+i tau)`, so horizontal zero geometry and the RH predicate are invariant under the common-clock orbit. AF-289 now performs the same separation for an arbitrary rowwise timing vector. Writing

\[
r(\tau)=\inf_{\sigma\in\mathbb R}\max_j|\tau_j-\sigma|
=\frac{\max_j\tau_j-\min_j\tau_j}{2},
\]

and decomposing `tau_j=sigma+epsilon_j`, the perturbed frame factors exactly as a common coefficient gauge followed by residual differential jitter. For a nominal frame with condition number at most `K`,

\[
\inf_\sigma
\frac{\|\widehat b-G_\sigma b\|_2}{\|b\|_2}
\le K\left(e^{r(\tau)\log N}-1\right).
\]

Thus an arbitrarily large common timing center is spectrally invisible; after quotienting the target's exact clock symmetry, the timing resource is the **differential jitter diameter** `osc(tau)=2r(tau)`. This is only a coefficient-orbit estimate. Turning it into a target theorem still requires a quantitative stability modulus for the actual target on that quotient, and targets depending on absolute phase, absolute zero ordinate, or fixed-height windows do not descend through the gauge.

The timing frontier is therefore narrower: determine the quotient stability of concrete RH-relevant intermediate observables under residual non-common jitter; decide which observables genuinely retain absolute imaginary-origin information; and extend the analysis beyond known finite support to unknown or infinite Dirichlet sources.

## Treat the information bills separately

Finite local degree determines prime-power depth at one prime, not prime breadth. Separate marginal channels can destroy joint interaction; complete mixed channels can restore exact separation. On the `log2/log3` prefix, label spacing, mixed degree, raw sample count, condition number, common-clock provenance, differential jitter diameter, and the downstream target quotient are distinct resources.

AF-288--AF-289 sharpen the warning that **recovering a nuisance parameter is unnecessary when the requested target is constant on its gauge orbit, and pricing residual noise should be done only after that quotient is taken**. Exact source anchors can remove a gauge without making the inverse globally stable, while a gauge-invariant target can avoid the lift entirely. Future fidelity claims must therefore state the source category, nuisance symmetry, residual perturbation geometry, and target metric before assigning an acquisition or calibration cost.