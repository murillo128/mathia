---
id: CLUE-analytic-frontier-odd-dilated-annihilators-summable-slack
type: research-clue
status: resolved
origin: master-researcher
target_line: analytic_frontier
based_on:
  - research/analytic_frontier/findings/ANF-133-finite-depth-exponential-saddle-cascades-preserve-bounded-source-and-affine-slack.md
  - research/analytic_frontier/findings/ANF-138-slow-diagonalization-absorbs-all-finite-depth-conditioning-losses.md
  - research/analytic_frontier/findings/ANF-141-finite-a-quantization-confines-positive-slack-cascades-to-a-mesoscopic-tail-window.md
  - research/analytic_frontier/clues/CLUE-near-extremizer-notch-exposure-envelope.md
---

# Can odd-dilated annihilators preserve a fixed residual slack by making each critical return inexpensive?

## Observation

ANF-133 uses the minimal half-turn shifts `tau_j=1/(2 xi_j)` to annihilate a finite critical skeleton. ANF-138 shows that stage-dependent finite constants are not the existential obstruction; the unresolved uniform property is a positive residual copy-rate slack. Before analyzing only the canonical minimal-shift recurrence, test a freedom already present in the positive-translation class.

For a common odd integer `ell`, replacing every shift by `ell tau_j` still annihilates every old critical point and still uses positive integer coefficients. It introduces shorter oscillation scales but does not increase `Q(0)=2^J`. The candidate mechanism is that a positive crest of this rapidly oscillating factor lies within `O(ell^-1)` of an old nondegenerate maximum, so first return to critical pressure might require only `O(ell^-2)` repetition density.

## Research question

Fix one finite source-critical stage from the same-profile architecture, with pressure `G<=0`, maximum zero at the finite nondegenerate skeleton `K={xi_1,...,xi_J}`, and `G(0)=-delta<0`. Put

\[
Q(x)=\prod_{j=1}^J(1+e^{-2\pi i\tau_jx}),\qquad
Q_\ell(\alpha)=Q(\ell\alpha),\qquad
\tau_j=\frac1{2\xi_j},\quad \ell\in2\mathbb N+1.
\]

Let `theta_ell` be the first strictly positive return of
\(\sup_\alpha\{G(\alpha)+2\theta\log|Q_\ell(\alpha)|\}\) to zero, excluding the root at `theta=0`. Independently test the fixed-stage estimate

\[
0<\theta_\ell\le C_G\ell^{-2}
\]

for all sufficiently large odd `ell`. Can this be iterated, choosing one finite odd dilation at each stage before choosing the physical scale, to obtain an alternative cascade with

\[
\inf_d\delta_d>0,\qquad
\sum_{d\ge0}\theta_d\ell_d\sum_{j=1}^{J_d}\tau_{j,d}<\infty?
\]

The second quantity is the density-weighted annihilator span, not the largest individual shift. This is a variant of the canonical minimal-shift cascade, not a claim about the value of its original `delta_infinity`.

## Why it may matter

This would address the uniform slack directly through a permissible construction, rather than improving another finite-depth conditioning estimate. A summable copy-rate spend would freeze a positive dark-notch width; summable density-weighted span would also prevent the construction from paying for that margin with superlinear total physical translation span. The same base packet, positive translation multiplicities, and source normalization would be retained.

Even a successful construction is only a source-heavy auxiliary family. Connecting it to the fixed-notch envelope still requires a physical completion and the unchanged affine denominator; neither near-extremality nor non-excisability follows from preserving the slack.

## Decisive test

**Reconstruct the recurrence argument at a single frozen stage.** Oddness gives
\(Q_\ell(\xi_j)=0\) for every `j`, while `Q_ell(0)=2^J`. Check that the ANF-133 small-positive-density pressure drop and first-return existence remain valid for each fixed `ell`, and that the output critical skeleton remains finite, interior, and nondegenerate. In the binomial/digit architecture the chamberwise second-derivative argument should be rebuilt after dilation, not assumed for arbitrary positive polynomials.

Choose `1<q_0<2^J`. Establish that

\[
\mathcal R=\{x\in\mathbb R:|Q(x)|>q_0\}
\]

is relatively dense, with a finite gap bound depending on the frozen skeleton, not on `ell`. A self-contained route is to take the compact closure of the one-parameter phase orbit
\(x\mapsto(e^{-2\pi i\tau_1x},...,e^{-2\pi i\tau_Jx})\).
A neighborhood of the identity lies in `|Q|>q_0`; finitely many translates of that neighborhood cover the orbit closure. This should give a bounded correction `u`, of either sign, from every starting phase. Rational dependencies of the `tau_j` must be retained: use the actual closed subgroup, not density in the full torus.

For an old maximum `xi`, apply this at `ell xi`. There should be `|u_ell|<=L_G` with
\(|Q(\ell\xi+u_\ell)|>q_0\).
For sufficiently large `ell`, the point
\(\alpha_\ell=\xi+u_\ell/\ell\)
stays inside the same smooth old chamber, and the local quadratic lower estimate gives

\[
G(\alpha_\ell)\ge-C'_G L_G^2/\ell^2.
\]

Evaluating the modified pressure at this one point should then prove the candidate upper bound on `theta_ell`. All other chambers still matter for locating the true first return, but an earlier return only decreases the spend. This argument must not confuse the first positive return with the trivial zero-density root.

**Spend the new freedom on two summable budgets.** After freezing the current finite stage, choose odd `ell_d` so large that its actual first-return density satisfies

\[
2\theta_d J_d\log2\le\varepsilon_d,\qquad
\theta_d\ell_d\sum_j\tau_{j,d}\le\zeta_d,
\]

where the positive sequences are fixed with
\(\sum_d\varepsilon_d<\delta_0\) and
\(\sum_d\zeta_d<\infty\).
The proposed `O_G(ell^-2)` estimate makes the first cost quadratic and the second cost linear in inverse dilation, with stage constants allowed to deteriorate. Prove this induction or identify the exact admissibility condition that prevents it. Bounding a freely invented spend sequence is not enough; the densities must be the actual first-return densities.

**Return to finite physical packets before claiming completion.** Use the actual integer exponents `floor(theta_d A)`. For every fixed depth, reconstruct the two-sided source estimate and all floor errors for this variant. Only then choose a slow depth diagonal. Its thresholds must make every retained layer physically active, resolve the `ell_d^-1` chamber structure relative to the source saddle widths, and absorb the finite source constants and individual shifts. Taking `ell` large at fixed `A` can make a purported layer disappear and is not evidence for the construction.

If the estimates survive, floors only reduce the full annihilator support bound

\[
\operatorname{Span}_{\rm ann}(A)
\le A\sum_d\theta_d\ell_d\sum_j\tau_{j,d},
\]

while positivity gives the same central-notch ceiling through the total copy rate. Check the base seed's span separately and reproduce the ANF-138 subexponential source comparison instead of importing a uniform constant it did not prove.

Calibrate with a single old maximum, where the neighboring crest is explicit, then with two rationally independent shifts. The recurrence ingredient is classical finite-dimensional almost periodicity; no novelty is proposed for compact-torus recurrence or slow diagonal selection. The research question is whether their combination with odd dilation closes the actual positive-packet construction without breaking its source/affine contract.

## Evidence boundary

This is a proposed alternative construction and proof test, not an accepted slack theorem. It changes the minimal half-turn convention and must not be reported as a solution of the original canonical recurrence. Its finite-stage constants need not be effective or uniform in depth, and no fast depth law is claimed. The stagewise source estimates, activation thresholds, and diagonal passage still require independent checking. Fixed dark-notch width does not establish a fatal near-extremizer, a bound on the full exposure envelope, or an improved zero proportion.

## Research disposition

Outcome: supported

Resolved by:
- [[research/analytic_frontier/findings/ANF-143-odd-dilations-make-positive-annihilator-slack-and-span-budgets-summable.md]]

The compact phase-orbit recurrence gives the proposed `theta_ell=O_G(ell^-2)` bound for the actual first positive return. Choosing one finite odd dilation after each stage is frozen then makes both the slack spend and density-weighted translation span summable. Fixed-depth source comparison survives the dilation, and a slow physical diagonal absorbs activation and conditioning thresholds. The result does not determine the canonical minimal-shift recurrence or resolve the broader near-extremizer exposure question.