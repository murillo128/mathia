# AF-128 — Optimal finite deficiency witnesses can be identity-calibrated

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `QUANTITATIVE-FIDELITY`, `CALIBRATED-WITNESS`, `NO-NOVELTY-CLAIM`

## Claim

AF-127 expresses finite recovery deficiency through bounded reconstruction losses, but deliberately warns that its original-data benchmark is the **identity reconstruction rule**, not the Bayes-optimal decision rule for an arbitrary loss. In the finite setting this distinction disappears at the optimum: an exact deficiency witness can always be chosen so that returning the observed source symbol is itself Bayes-optimal before compression.

Let

\[
\mathcal E=(P_\theta)_{\theta\in\Theta}
\]

be a statistical experiment on a finite sample space `X`, with finite parameter set `Theta`. Let

\[
K:X\rightsquigarrow Y,
\qquad
Q_\theta=P_\theta K,
\]

and use the normalized total variation convention

\[
\|P-Q\|_{\rm TV}=\frac12\sum_x|P(x)-Q(x)|.
\]

As in AF-126, define the one-sided recovery deficiency

\[
\delta_{\rm rec}(K;\mathcal E)
:=
\min_{R:Y\rightsquigarrow X}
\max_{\theta\in\Theta}
\|P_\theta-Q_\theta R\|_{\rm TV}.
\tag{1}
\]

For a prior `lambda in Delta(Theta)` and a bounded payoff

\[
u:\Theta\times X\to[-1,1],
\]

define the Bayes-optimal payoff from the original observation by

\[
V^*_{\mathcal E}(\lambda,u)
:=
\sum_{x\in X}
\max_{a\in X}
\sum_{\theta\in\Theta}
\lambda_\theta P_\theta(x)u(\theta,a),
\tag{2}
\]

and the Bayes-optimal payoff from the compressed observation by

\[
V^*_{\mathcal E K}(\lambda,u)
:=
\sum_{y\in Y}
\max_{a\in X}
\sum_{\theta\in\Theta}
\lambda_\theta Q_\theta(y)u(\theta,a).
\tag{3}
\]

The action alphabet is the reconstruction alphabet `X`. Then

\[
\boxed{
2\,\delta_{\rm rec}(K;\mathcal E)
=
\max_{\lambda\in\Delta(\Theta)}
\max_{u\in[-1,1]^{\Theta\times X}}
\left[
V^*_{\mathcal E}(\lambda,u)
-
V^*_{\mathcal E K}(\lambda,u)
\right].
}
\tag{4}
\]

Moreover, the maximum in `(4)` has a maximizer `(lambda_*,u_*)` for which the identity action `a=x` is Bayes-optimal at every source observation with positive prior-predictive mass:

\[
\sum_\theta
\lambda_{*,\theta}P_\theta(x)u_*(\theta,x)
\ge
\sum_\theta
\lambda_{*,\theta}P_\theta(x)u_*(\theta,a)
\qquad
\forall a\in X
\tag{5}
\]

whenever

\[
m_{\lambda_*}(x):=
\sum_\theta\lambda_{*,\theta}P_\theta(x)>0.
\]

Equivalently, after writing

\[
\ell(\theta,a)=\frac{1-u(\theta,a)}2\in[0,1],
\]

and denoting the ordinary Bayes risks by `R^*`,

\[
\boxed{
\delta_{\rm rec}(K;\mathcal E)
=
\max_{\lambda,\ell}
\left[
\mathcal R^*(\mathcal E K;\lambda,\ell)
-
\mathcal R^*(\mathcal E;\lambda,\ell)
\right],
}
\tag{6}
\]

and the maximum may be restricted, without changing its value, to losses satisfying

\[
\sum_\theta
\lambda_\theta P_\theta(x)\ell(\theta,x)
\le
\sum_\theta
\lambda_\theta P_\theta(x)\ell(\theta,a)
\qquad
\forall a\in X
\tag{7}
\]

for every `x` of positive prior-predictive mass. Under the posterior

\[
\pi_\lambda(\theta\mid x)
=
\frac{\lambda_\theta P_\theta(x)}{m_\lambda(x)},
\]

condition `(7)` simply says that action `x` minimizes posterior expected loss after observing `x`.

Thus AF-127's reconstructive dual is not exact only because it permits an artificial benchmark. At least one optimal witness is **self-calibrated to reconstruction**: the original symbol is already the correct Bayes action upstream, while compression makes some bounded reconstruction task strictly harder by exactly the deficiency.

## Derivation

### Any reverse simulation transfers every original decision rule

Choose a recovery channel `R_*:Y\rightsquigarrow X` attaining `(1)`, whose existence follows from finite compactness as in AF-126. Let

\[
D:X\rightsquigarrow X
\]

be any decision rule on the original experiment. The compressed experiment can imitate it by first applying `R_*` and then `D`.

For each parameter `theta`, total variation contracts under the stochastic map `D`, so

\[
\|P_\theta D-Q_\theta R_*D\|_{\rm TV}
\le
\|P_\theta-Q_\theta R_*\|_{\rm TV}
\le
\delta_{\rm rec}.
\tag{8}
\]

For a payoff bounded by `[-1,1]`, the difference of expectations under two probability laws is at most twice their normalized total variation. Therefore, for every prior `lambda`,

\[
V(D;\mathcal E,\lambda,u)
-
V(R_*D;\mathcal E K,\lambda,u)
\le
2\delta_{\rm rec}.
\tag{9}
\]

Take `D_*` Bayes-optimal for the original experiment. Since `R_*D_*` is only one of the decision rules available after compression,

\[
V^*_{\mathcal E K}(\lambda,u)
\ge
V(R_*D_*;\mathcal E K,\lambda,u).
\]

Hence

\[
\boxed{
V^*_{\mathcal E}(\lambda,u)
-
V^*_{\mathcal E K}(\lambda,u)
\le
2\delta_{\rm rec}
}
\tag{10}
\]

for every prior and every bounded payoff. This is the finite Bayes-risk/randomization direction of the classical comparison-of-experiments theorem specialized to the reconstruction action alphabet `X`.

### AF-127 forces equality and calibrates the identity action

AF-127 proves the exact reconstructive dual

\[
2\delta_{\rm rec}
=
\max_{\lambda,u}
\left[
V_{\rm id}(\mathcal E;\lambda,u)
-
V^*_{\mathcal E K}(\lambda,u)
\right],
\tag{11}
\]

where

\[
V_{\rm id}(\mathcal E;\lambda,u)
=
\sum_{\theta,x}
\lambda_\theta P_\theta(x)u(\theta,x).
\tag{12}
\]

For every `(lambda,u)`, the identity rule is merely one admissible original-data decision rule, so

\[
V_{\rm id}(\mathcal E;\lambda,u)
\le
V^*_{\mathcal E}(\lambda,u).
\tag{13}
\]

Let `(lambda_*,u_*)` attain the finite maximum in `(11)`. Combining `(10)`, `(11)`, and `(13)` gives

\[
\begin{aligned}
2\delta_{\rm rec}
&=
V_{\rm id}(\mathcal E;\lambda_*,u_*)
-
V^*_{\mathcal E K}(\lambda_*,u_*)\\
&\le
V^*_{\mathcal E}(\lambda_*,u_*)
-
V^*_{\mathcal E K}(\lambda_*,u_*)\\
&\le
2\delta_{\rm rec}.
\end{aligned}
\tag{14}
\]

Every inequality in `(14)` is therefore an equality. In particular,

\[
V_{\rm id}(\mathcal E;\lambda_*,u_*)
=
V^*_{\mathcal E}(\lambda_*,u_*).
\tag{15}
\]

The original Bayes optimization in `(2)` separates over observed symbols `x`. Equality `(15)` is therefore equivalent to the pointwise optimality condition `(5)` at every `x` carrying positive prior-predictive mass. Symbols with zero mass impose no condition because they do not contribute to the objective.

This proves both `(4)` and the existence of an identity-calibrated maximizer. No additional minimax theorem beyond AF-127 is required for the calibration step: it is forced by sandwiching the reconstructive optimum between the classical Bayes optimum and the reverse-simulation upper bound.

### Loss normalization gives the Bayes-risk form

Set `u=1-2 ell`. For any decision rule, expected payoff equals one minus twice expected loss. Consequently

\[
V^*_{\mathcal E}
-
V^*_{\mathcal E K}
=
2\left(
\mathcal R^*(\mathcal E K)
-
\mathcal R^*(\mathcal E)
\right).
\tag{16}
\]

Substituting `(16)` into `(4)` gives `(6)`. Equality of the identity payoff with the original Bayes-optimal payoff becomes equality of the identity loss with the original Bayes risk, and the pointwise condition becomes `(7)`.

The calibration constraint therefore does not weaken the complete finite witness class at the optimum. It removes losses for which the source observation itself would already call for a nontrivial decision post-processing, because such losses are unnecessary to attain the deficiency.

## Relationship to AF-126 and AF-127

AF-126 introduces the whole-experiment quantitative defect: one common reverse channel must approximately regenerate every member of the declared control family. It also shows that selected pairwise divergence losses may fail to detect a positive defect.

AF-127 identifies an exact finite dual witness: one bounded reconstruction loss and one prior expose every positive deficiency. Its boundary analysis correctly warns that the identity reconstruction benchmark should not be confused with the Bayes-optimal original-data rule for an arbitrary loss.

AF-128 closes precisely that boundary at the **maximizing witness**. The arbitrary-loss distinction remains true pointwise, but it is irrelevant to the optimum: there always exists a deficiency-attaining loss for which identity reconstruction is Bayes-optimal upstream. Hence the exact finite picture can be stated as

\[
\text{reverse-simulation deficiency}
=
\text{largest Bayes-risk gap}
=
\text{largest calibrated reconstruction-risk gap}.
\tag{17}
\]

This is useful for later restricted-admissibility questions. Before imposing symmetry, locality, positivity, spectral, geometric, or arithmetic constraints on decision witnesses, one may already require the unconstrained witness to be posterior-calibrated to the original representation without sacrificing completeness.

## Prior art and novelty assessment

The Bayes-risk/randomization equivalence underlying `(4)` and `(6)` is classical comparison-of-statistical-experiments theory, not a new theorem.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`. Role: exact comparison of experiments by randomization and decision performance.
- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/AOMS/1177700372`. Role: foundational approximate-sufficiency and deficiency framework.
- Erik Torgersen, ***Comparison of Statistical Experiments***, Cambridge University Press (1991), Chapter 6, **“Deficiencies,”** pp. 222–328, DOI `10.1017/CBO9780511666353.007`. Role: authoritative systematic treatment in which deficiency has equivalent formulations through randomizations, risk functions, Bayes risks, and restricted decision classes.

The literature audit therefore rules out any novelty claim for the deficiency/Bayes-risk equality itself. The Arithmetic Fidelity-specific derived consequence is narrower: **AF-127's exact reconstructive maximizer can be chosen from the posterior-calibrated subclass where the source symbol is already a Bayes-optimal action.** This is an immediate but useful bridge between the line's reconstruction semantics and the classical Bayes-risk semantics.

No claim is made that this calibration property is absent from the statistical-decision-theory literature under another formulation. Its value here is as a reusable audit normalization, not as a new statistical principle.

## Boundary conditions and falsification checks

The statement has several strict boundaries.

1. **Finite spaces and finite parameter sets.** The proof uses attainment of the reverse channel and of the bounded witness, plus finite pointwise Bayes optimization. General measurable experiments require the full topological and measurability machinery of Le Cam theory.

2. **The action alphabet is `X`.** Equation `(4)` is already complete for the recovery deficiency because AF-127's dual uses reconstructed source symbols. This finding does not claim that arbitrary statistical decision problems can always be reduced to this alphabet for every other comparison notion.

3. **Calibration is existential, not universal.** An arbitrary maximizing Bayes-risk witness need not use identity as its upstream optimal rule, and an arbitrary loss certainly need not. The theorem says that at least one exact maximizer can be chosen with the calibration property.

4. **Calibration depends on the prior.** Condition `(7)` is posterior/Bayes calibration for the same `lambda` that witnesses the deficiency. It is not a parameterwise statement that `a=x` minimizes `ell(theta,a)` for every `theta` separately.

5. **Zero-mass symbols are unconstrained.** No posterior is defined and no calibration is required where `m_lambda(x)=0`.

6. **Restricted witness families can still lose completeness.** Requiring symmetry, locality, continuity, positivity, a spectral form, an arithmetic form, or another structural admissibility condition is much stronger than posterior calibration. Equation `(17)` does not imply that such a restricted family still attains the deficiency.

7. **The factor two depends on the payoff normalization.** With payoffs in `[-1,1]` and normalized total variation, expectation differences are bounded by `2 TV`; with losses in `[0,1]`, the exact risk gap is `delta_rec` as in `(6)`.

A finite falsification check is direct: solve the primal reverse-channel linear program for `(1)`, then solve the Bayes-gap maximization or AF-127 dual and verify that an optimal witness can be selected satisfying the linear inequalities `(7)`. Any finite instance for which the optimal calibrated gap is strictly smaller than `delta_rec` would refute the claim.

## Consequences for Arithmetic Fidelity

The result removes one artificial freedom from exact finite fidelity witnesses. A compression does not need to be declared defective because of a loss function under which the original representation was itself badly aligned with the task. If the recovery deficiency is positive, there is an equally strong witness whose decision semantics are already native to the source: observe `x`, and `x` is a Bayes-optimal reconstruction action.

This sharpens the next admissibility question left by AF-127. The genuinely nontrivial restriction is no longer “can the witness be made reconstruction-like?” It can. The remaining question is whether the witness can also be chosen inside a **mathematically intrinsic constrained class** imposed by the compression under study—equivariant, local, positive, spectral, geometric, arithmetic, or otherwise natural. Failure of such a constrained class to attain the unrestricted calibrated optimum would quantify exactly how much of the generic decision-theoretic witness language is unavailable to that mathematical mechanism.
