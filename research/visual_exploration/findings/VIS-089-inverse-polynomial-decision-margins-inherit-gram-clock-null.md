# VIS-089 — inverse-polynomial decision margins inherit the finite-order Gram-clock null

## Claim

Use the corrected Gram/prime-phase block and chord sup metric from `VIS-087` and `VIS-088`:

`R_(m,n)=(R_(m,n,h)(p))_(0<=h<=H_n,p<=P_n)`,

`d_infty(z,w)=max_(h,p)|z_(h,p)-w_(h,p)|`.

Let `Q_n` be **any** block readout with values in an arbitrary set `S_n`; no continuity, Lipschitz, differentiability, or linearity is assumed. Define its decision margin around the deterministic clock-null block `1` by

`mu_n = inf { d_infty(z,1) : Q_n(z) != Q_n(1) }`,

with the convention `inf(empty set)=+infinity`.

Then the following implication is immediate and exact:

`d_infty(R_(m,n),1) < mu_n`
`  => Q_n(R_(m,n)) = Q_n(1)`.

Combining this with `VIS-087`, for every fixed `m`,

`d_infty(R_(m,n),1)`
` <<_m H_n^(m+1) log P_n / [g_n^m (log g_n)^(m+2)].`

Now assume polynomial prime support `P_n<=g_n^A`, a fixed sublinear power-law block

`H_n=O(g_n^alpha (log g_n)^B)`, `alpha<1`,

and an inverse-polynomial decision-margin lower bound

`mu_n >= c g_n^(-kappa) (log g_n)^(-D)`

for fixed `c>0`, `kappa>=0`, and real `D`. Choose any fixed integer `m` satisfying

`m(1-alpha) > alpha+kappa`.

Then

`d_infty(R_(m,n),1)=o(mu_n)`,

so eventually

`Q_n(R_(m,n)) = Q_n(1)`.

Therefore **a hard threshold, binning rule, sign pattern, nearest-template identity, combinatorial label, or other discontinuous visual statistic does not escape the finite-order Gram-clock hierarchy merely by being discontinuous when its null decision has an inverse-polynomially robust metric margin**.

**Evidence/status:** `EXACT-DERIVED + ELEMENTARY METRIC-MARGIN COROLLARY OF VIS-087 + NEGATIVE/CONTROL + NO-NOVELTY-CLAIM`.

This does not control nearly linear/nonlocal Gram blocks, decision rules whose null margin has no inverse-polynomial lower bound, growing Taylor order `m=m(n)`, prime support outside the admitted regime, additional analytic source coordinates, zeta approximation, or RH.

## 1. Discontinuity is harmless away from the decision boundary

The definition of `mu_n` isolates the only issue created by a discontinuous readout. By construction, every point in the open metric ball

`B(1,mu_n)={z:d_infty(z,1)<mu_n}`

has the same output as `1`. Otherwise there would be a point with changed output at distance strictly below the infimum defining `mu_n`.

Hence no regularity of `Q_n` is required. If the corrected prime-phase block lies inside that ball, the readout is exactly frozen at its deterministic clock-null value.

This is the metric form of the usual robust-margin principle: a discrete decision cannot change under a perturbation smaller than its distance to the nearest decision-changing input.

## 2. Any fixed inverse-polynomial margin is swallowed on a fixed sublinear power scale

Under `P_n<=g_n^A` and

`H_n=O(g_n^alpha(log g_n)^B)`,

`VIS-087` gives

`d_infty(R_(m,n),1)`
` = O_m(g_n^(alpha(m+1)-m)`
`       (log g_n)^(B(m+1)-m-1)).`

Divide this by the assumed margin lower bound. The ratio is

`O_m(g_n^(kappa+alpha-m(1-alpha))`
`       (log g_n)^(D+B(m+1)-m-1)).`

If

`m(1-alpha)>alpha+kappa`,

the power of `g_n` is strictly negative and dominates every fixed logarithmic factor. Thus the ratio tends to zero and the corrected block eventually remains strictly inside the decision-margin ball.

The order `m` is still fixed. Nothing here requires uniform control of the inverse-theta expansion as `m` grows with height.

## 3. What visual readouts this closes

The result is deliberately stated for an arbitrary codomain because many visually tempting statistics become discontinuous only at their final readout stage.

Examples include assigning the corrected block to a finite bin, recording a sign vector, choosing the nearest element of a template dictionary, declaring whether a threshold is crossed, retaining only the top-ranked component, or converting a continuous score into a categorical label. If the clock-null block is separated from every output-changing configuration by a metric margin at least inverse-polynomial in `g_n`, all such outputs are eventually identical to the deterministic null after a sufficiently high fixed clock correction.

This complements `VIS-088`. That finding controls quantitatively Lipschitz observables even when their total sensitivity grows polynomially. The present finding controls the opposite-looking case — an arbitrary discontinuous final decision — whenever the decision itself has a quantitatively robust neighborhood around the null.

A proposed threshold route therefore has two honest options. It can prove a stable margin, in which case the theorem above tests whether the clock collapse is already smaller than that margin; or it can place the decision boundary arbitrarily close to the null, in which case the apparent amplification must be justified as meaningful rather than assumed from finite-height label flips.

## 4. What remains genuinely open

The theorem is silent when `mu_n=0`, when the output-changing set accumulates at the null block, or when no inverse-polynomial lower bound for `mu_n` is available. A highly sharpened threshold may therefore remain formally outside this control.

That failure is not positive evidence. It means only that the readout can react to perturbations on a scale smaller than the deterministic bound currently being used. To turn such a route into a mathematical separator, one must independently show that the vanishing margin is stable, intrinsic, and linked to an additional arithmetic or analytic source rather than chosen precisely to magnify the residual clock error.

Likewise, a nearly linear or genuinely nonlocal Gram window remains outside the fixed-sublinear hierarchy and requires its own sampling theorem.

## Prior art and novelty assessment

The abstract statement that a discrete decision is invariant under perturbations smaller than its distance to the decision boundary is definition-level metric geometry. In statistical and adversarial classification, this distance is routinely called a margin or input-space margin; for example Gavin W. Ding, Yash Sharma, Kry Yik Chau Lui, and Ruitong Huang, **MMA Training: Direct Input Space Margin Maximization through Adversarial Training**, ICLR 2020, arXiv `1812.02637`, explicitly formulates robustness through distance to the decision boundary.

No novelty is claimed for that margin principle. The only number-theoretic input is the already audited fixed-order Gram-clock estimate in `VIS-087`. The durable Mathia contribution is the control interpretation: discontinuous visual readouts with any fixed inverse-polynomial null margin are no more an escape from local Gram sampling geometry than the polynomial-Lipschitz observables closed by `VIS-088`.

## Boundary and falsification

The decisive quantity is the metric decision margin `mu_n`, not the apparent visual sharpness of `Q_n`. Falsify an application by showing that the claimed lower bound on `mu_n` is wrong, that the chosen metric is too weak for the actual decision semantics, or that the corrected block lies outside the `VIS-087` corridor used to bound `d_infty`.

At equality `d_infty(R_(m,n),1)=mu_n`, no conclusion is asserted because the infimum need not be attained and boundary conventions can matter. The theorem uses the strict inequality only.

A finite-height output flip does not contradict the asymptotic statement unless it occurs beyond the regime where the proven phase error is already smaller than the verified decision margin.

## Visual consequence

No canonical PNG is retained. A threshold plot would make the visually chosen boundary look like additional structure, while the relevant invariant is the distance from the deterministic null block to the nearest output-changing configuration. The exact metric statement is the safer representation.

## Research consequence

`CLUE-zeta-prime-phase-recursive-geometry` should no longer treat a robust hard threshold or binning rule as a generic non-Lipschitz escape on fixed sublinear power-law Gram blocks with polynomial prime support. Any such readout with an inverse-polynomial decision margin is swallowed by a sufficiently high fixed-order Gram-clock correction.

The local prime-phase frontier is narrower again: nearly linear/nonlocal sampling, a decision boundary with no inverse-polynomially robust neighborhood whose extreme sensitivity is independently justified, prime support outside the admitted quantitative regime, or a genuinely independent analytic source coordinate.