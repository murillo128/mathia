# AF-009 — Conditional variance is the exact L2 fidelity defect under stochastic compression

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `(Omega,F,P)` be a probability space, let

\[
D\in L^2(\Omega;\mathbb R^q)
\]

be a square-integrable discriminator, and let `Y` be any retained observation/compressed representation. Write

\[
m_Y=\mathbb E[D\mid Y]
\]

and define the **L2 fidelity-defect matrix**

\[
\mathcal R_D(Y)
=
\mathbb E\!\left[(D-m_Y)(D-m_Y)^\top\right]
\succeq 0.
\]

Then:

1. for every square-integrable predictor `g(Y)`, there is an exact matrix Pythagorean decomposition
   \[
   \mathbb E[(D-g(Y))(D-g(Y))^\top]
   =
   \mathcal R_D(Y)
   +
   \mathbb E[(m_Y-g(Y))(m_Y-g(Y))^\top];
   \]
   hence `m_Y` is Loewner-optimal among all predictors using only `Y`, and `tr R_D(Y)` is the minimum achievable mean squared error;
2. exact recovery holds almost surely if and only if
   \[
   \mathcal R_D(Y)=0,
   \]
   equivalently if and only if `D` is measurable with respect to `sigma(Y)`;
3. a linear discriminator direction `a^T D` survives exactly if and only if
   \[
   a\in\ker \mathcal R_D(Y).
   \]
   Thus the kernel records the exactly surviving linear directions, while the positive spectrum quantifies the unresolved ones relative to the chosen Euclidean metric;
4. if `Z=S(Y)` is any deterministic downstream coarsening, then
   \[
   \mathcal R_D(Z)
   =
   \mathcal R_D(Y)
   +
   \mathbb E[(m_Y-m_Z)(m_Y-m_Z)^\top]
   \succeq
   \mathcal R_D(Y);
   \]
5. the same identity holds for a stochastic garbling `Y -> Z` whenever
   \[
   D\;\perp\!\!\!\perp\; Z\mid Y,
   \]
   i.e. when the downstream channel receives no side information about `D` except through `Y`;
6. for a binary discriminator `D in {0,1}`, if
   \[
   p_Y=\mathbb P(D=1\mid Y),
   \]
   then
   \[
   \mathcal R_D(Y)=\mathbb E[p_Y(1-p_Y)]
   \]
   as a scalar, while the optimal zero-one classification error
   \[
   e_Y=\mathbb E[\min(p_Y,1-p_Y)]
   \]
   satisfies
   \[
   \mathcal R_D(Y)\le e_Y\le 2\mathcal R_D(Y).
   \]
   Thus this quadratic defect vanishes exactly with perfect classification and controls binary Bayes error up to a universal factor two.

This gives Arithmetic Fidelity a quantitative extension of AF-001. Exact fiberwise survival is the zero-defect endpoint, but noisy or stochastic compressions can now be compared by the irreducible discriminator error they leave. Most importantly, downstream garbling has an exact **defect increment** rather than merely a qualitative data-processing inequality.

The mathematics is classical conditional expectation, Hilbert-space projection, Rao–Blackwell variance reduction, and Blackwell garbling. No novelty is claimed for those ingredients.

## Derivation

### Conditional expectation is the optimal retained predictor

Let

\[
e_Y=D-m_Y.
\]

For every square-integrable `Y`-measurable vector `h(Y)`, conditional expectation gives

\[
\mathbb E[e_Y h(Y)^\top]=0.
\]

Now write

\[
D-g(Y)=e_Y+(m_Y-g(Y)).
\]

Expanding the outer product and taking expectation kills the two cross terms, because `m_Y-g(Y)` is `Y`-measurable. Hence

\[
\mathbb E[(D-g)(D-g)^\top]
=
\mathbb E[e_Ye_Y^\top]
+
\mathbb E[(m_Y-g)(m_Y-g)^\top].
\]

The second term is positive semidefinite. Therefore `m_Y` is not merely trace-optimal: every other `Y`-based predictor has an error covariance larger in Loewner order.

Taking traces gives

\[
\inf_g \mathbb E\|D-g(Y)\|^2
=
\operatorname{tr}\mathcal R_D(Y).
\]

So `R_D(Y)` is an exact irreducible squared-loss defect for the specified discriminator.

### Zero defect is exact recovery

For every `a in R^q`,

\[
a^\top\mathcal R_D(Y)a
=
\mathbb E\left[(a^\top(D-m_Y))^2\right].
\]

Therefore

\[
a\in\ker\mathcal R_D(Y)
\iff
a^\top D=a^\top m_Y\quad\text{a.s.}
\]

Since `m_Y` is `sigma(Y)`-measurable, this proves the directional survival statement. In particular,

\[
\mathcal R_D(Y)=0
\iff
D=m_Y\quad\text{a.s.}
\iff
D\text{ is }\sigma(Y)\text{-measurable a.s.}
\]

This is the probabilistic analogue of AF-001's deterministic fiber criterion, with equality understood modulo null sets.

### Exact defect growth under deterministic coarsening

Suppose `Z=S(Y)`. Then

\[
\sigma(Z)\subseteq\sigma(Y)
\]

and the tower property gives

\[
m_Z
=
\mathbb E[D\mid Z]
=
\mathbb E[m_Y\mid Z].
\]

Decompose

\[
D-m_Z=(D-m_Y)+(m_Y-m_Z).
\]

The first term is orthogonal to every `Y`-measurable vector, and the second term is `Y`-measurable. Thus the cross terms vanish and

\[
\boxed{
\mathcal R_D(Z)-\mathcal R_D(Y)
=
\mathbb E[(m_Y-m_Z)(m_Y-m_Z)^\top]
\succeq0.
}
\]

The increment has a concrete interpretation: it is exactly the portion of the previously predictable discriminator that the second compression makes unpredictable.

This is stronger than saying only that error cannot improve. It identifies what new component was lost at the downstream step.

### Stochastic garbling has the same decomposition

Now allow `Z` to be produced stochastically from `Y`. Assume the Markov condition

\[
D\;\perp\!\!\!\perp\;Z\mid Y.
\]

Then

\[
\mathbb E[D\mid Y,Z]
=
\mathbb E[D\mid Y]
=m_Y,
\]

and therefore

\[
m_Z
=
\mathbb E[D\mid Z]
=
\mathbb E[m_Y\mid Z].
\]

Using the same decomposition

\[
D-m_Z=(D-m_Y)+(m_Y-m_Z),
\]

the cross term vanishes after conditioning on `(Y,Z)` because

\[
\mathbb E[D-m_Y\mid Y,Z]=0.
\]

Hence the same positive-semidefinite defect increment holds for a genuine noisy garbling.

The Markov assumption is essential. If `Z` receives independent side information about `D`, it is no longer merely a downstream compression and its defect may be smaller than the defect of `Y`.

## Binary discriminator audit

Let `D` be `{0,1}`-valued. Then

\[
m_Y=p_Y
\]

and conditional variance gives

\[
\mathcal R_D(Y)
=
\mathbb E[p_Y(1-p_Y)].
\]

The Bayes classifier based on `Y` chooses the more probable class and has conditional error

\[
\min(p_Y,1-p_Y).
\]

For every `p in [0,1]`, put `r=min(p,1-p)`, so `0<=r<=1/2`. Then

\[
p(1-p)=r(1-r),
\]

and therefore

\[
\frac r2\le r(1-r)\le r.
\]

Averaging yields

\[
\boxed{
\mathcal R_D(Y)
\le e_Y
\le2\mathcal R_D(Y).
}
\]

Thus the quadratic defect is not just an abstract variance: for binary discrimination it is quantitatively equivalent, within a fixed factor, to the best achievable classification error from the compressed observation.

## Arithmetic Fidelity interpretation

AF-001 deliberately left approximate, noisy, and statistical fidelity open. The present result closes the simplest important case: a square-integrable discriminator under squared loss.

The key object is **discriminator-relative**. A compression may discard enormous information about the upstream state while having zero defect for one chosen `D`; conversely it may preserve large mutual information or many unrelated observables while leaving a positive defect for the one discriminator that matters. This matches the line's premise that raw information quantity is too coarse.

The matrix form also prevents a misleading scalarization. For vector-valued `D`, one number such as total MSE depends on the chosen metric and can hide which combinations survive. The residual matrix obeys

\[
\mathcal R_{AD}(Y)
=A\mathcal R_D(Y)A^\top
\]

for every linear change of discriminator coordinates `A`. Hence its kernel and rank transform canonically under invertible linear reparameterization even though its trace does not.

This produces a quantitative composition audit:

\[
\text{upstream discriminator}
\to Y
\to Z
\]

can be annotated by

\[
\mathcal R_D(Y)
\preceq
\mathcal R_D(Z),
\]

with the difference equal to the covariance of the predictor component erased by the second channel. Once that increment is positive in a discriminator direction, no later garbling of `Z` can make the direction exactly recoverable without new side information.

## Prior art and novelty assessment

The central mathematics is established probability and statistics.

Blackwell's 1947 paper proves the defining conditional-expectation orthogonality identity in the form

\[
\mathbb E[f(X)\mathbb E(Y\mid X)]
=
\mathbb E[f(X)Y]
\]

under appropriate integrability and derives the associated variance reduction for conditioned estimators. This is one classical root of the Rao–Blackwell theorem.

Modern probability texts such as Kallenberg's *Foundations of Modern Probability* treat conditional expectation as part of the standard conditioning/martingale framework; in `L^2`, its Hilbert-space interpretation as orthogonal projection is classical. Blackwell's 1953 comparison-of-experiments theorem supplies the broader decision-theoretic language in which a stochastic garbling cannot make an experiment more informative.

Accordingly, neither optimality of conditional expectation, total-variance decomposition, nor garbling monotonicity is new. The Arithmetic Fidelity contribution is organizational: it identifies the residual covariance matrix as an exact **discriminator-specific fidelity defect**, records its zero set as exact recoverability, and uses the Pythagorean difference formula to localize how much additional discriminator information each compression stage destroys.

## Boundaries and failure modes

- All recovery statements are almost-sure statements. Distinctions confined to null sets are invisible in this framework.
- The exact projection identity is tied to squared loss and the Hilbert geometry of `L^2`. Other losses require their own Bayes-risk or divergence theory and need not admit this matrix Pythagorean formula.
- `R_D(Y)` measures recoverability of the chosen discriminator, not reconstruction of the full upstream state or its distribution.
- The matrix depends on the linear coordinate/inner-product structure chosen on the discriminator space. Kernel and rank are stable under invertible linear coordinate changes; numerical eigenvalues and trace are not invariant under arbitrary rescaling.
- A small defect is an average statement. Rare but structurally important failures can be hidden by low probability and require worst-case, zero-error, tail, or adversarial criteria.
- For stochastic post-processing, monotonicity requires the Markov/no-side-channel condition. A later variable carrying fresh upstream information is a lift, not a garbling.
- As in AF-001, allowing the lift `L=D` makes exact recovery trivial. This finding quantifies loss but does not solve the natural/admissible-lift problem.
- No claim is made that an RH-relevant arithmetic discriminator has a natural probability law or Euclidean encoding for which this defect is the right notion of fidelity.

## Decisive audit test for noisy or statistical compressions

When a proposed construction replaces exact upstream structure by a random, averaged, sampled, learned, or noisy representation:

1. specify the discriminator `D` and the probability law rather than speaking about generic information loss;
2. compute or bound `m_Y=E[D|Y]` and `R_D(Y)`;
3. inspect the kernel of `R_D(Y)` to determine which linear discriminator directions survive exactly;
4. for every downstream channel, verify that it is genuinely a garbling with no extra side information before invoking monotonicity;
5. compute the defect increment when possible instead of merely asserting data processing;
6. test tail/worst-case behavior separately when an average quadratic defect could hide rare failures;
7. do not compare scalar traces across arbitrary discriminator rescalings without fixing a meaningful metric.

A positive defect is a quantitative no-go certificate for exact recovery from that representation alone. A zero defect is only a recovery statement for the specified discriminator; it is not evidence that the compression preserved all mathematically relevant structure.

## Consequence for the line

Add **conditional-variance / Bayes-risk compression** to the Arithmetic Fidelity model library as the canonical first treatment of approximate and stochastic loss.

Future probabilistic applications should distinguish at least three levels:

\[
\text{exact fiber recovery}
\quad\leftrightarrow\quad
\mathcal R_D=0,
\]

\[
\text{average quadratic fidelity}
\quad\leftrightarrow\quad
\mathcal R_D\succeq0,
\]

and

\[
\text{worst-case / zero-error fidelity},
\]

which is not controlled by a small average defect alone. The next probabilistic extension, if needed, should therefore change the loss/adversarial criterion rather than invent another scalar summary of the same `L^2` projection.