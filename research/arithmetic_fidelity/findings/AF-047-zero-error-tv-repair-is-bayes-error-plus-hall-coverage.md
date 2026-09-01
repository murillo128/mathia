# AF-047 — Zero-error TV repair is Bayes error plus a Hall coverage penalty

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D
\]

be a discriminator, and write

\[
A=d(X),
\qquad
m=|A|.
\]

Fix a strictly positive prior

\[
\pi_x>0,
\qquad
\sum_{x\in X}\pi_x=1,
\]

and let `K:X\rightsquigarrow Y` be a stochastic channel. For two channels on the same alphabets define the prior-weighted row total-variation metric

\[
\rho_\pi(K,L)
=
\sum_{x\in X}\pi_x\operatorname{TV}(K_x,L_x),
\]

where

\[
\operatorname{TV}(P,Q)
=
\frac12\sum_{y\in Y}|P(y)-Q(y)|.
\]

Equivalently, `\rho_\pi` is the total-variation distance between the two joint laws `\pi_xK(y\mid x)` and `\pi_xL(y\mid x)` when the upstream prior is held fixed.

Let `\mathcal Z_d^{(0)}` be AF-011's zero-error faithful set: channels for which rows belonging to distinct discriminator classes have disjoint output supports. Assume

\[
|Y|\ge m,
\]

which is exactly the condition for `\mathcal Z_d^{(0)}` to be nonempty.

For each discriminator class `a\in A` define the class-output subprobability mass

\[
q_a(y)
=
\sum_{x:d(x)=a}\pi_xK(y\mid x).
\]

For a surjective labeling

\[
\delta:Y\twoheadrightarrow A
\]

define its retained class mass by

\[
\operatorname{Acc}_{\mathrm{surj}}(K;\delta)
=
\sum_{y\in Y}q_{\delta(y)}(y),
\]

and let

\[
A_{\mathrm{surj}}(K,d,\pi)
=
\max_{\delta:Y\twoheadrightarrow A}
\operatorname{Acc}_{\mathrm{surj}}(K;\delta).
\]

Then:

1. **Distance to exact zero-error fidelity is a surjective classification problem.**
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   (K,\mathcal Z_d^{(0)})
   =
   1-A_{\mathrm{surj}}(K,d,\pi).
   }
   \]
   A nearest zero-error channel always exists.

2. **The projection depends only on class-output joint mass.** The detailed variation among rows inside one discriminator class affects which nearest channel is obtained, but not the minimum repair cost. All dependence of the distance on `K` passes through the finite matrix
   \[
   (q_a(y))_{a\in A,y\in Y}.
   \]

3. **Ordinary Bayes error is only the first part of the repair cost.** Define the unconstrained Bayes accuracy and Bayes error for predicting `d(X)` from one output by
   \[
   A_B(K)
   =
   \sum_{y\in Y}\max_{a\in A}q_a(y),
   \qquad
   R_B(K)=1-A_B(K).
   \]
   Put
   \[
   m(y)=\max_{a\in A}q_a(y),
   \qquad
   c(a,y)=m(y)-q_a(y)\ge0.
   \]
   The extra cost of forcing every discriminator class to remain represented is the rectangular assignment value
   \[
   \tau(K,d,\pi)
   =
   \min_{\iota:A\hookrightarrow Y}
   \sum_{a\in A}c(a,\iota(a)),
   \]
   where `\iota` ranges over injections. Then
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   (K,\mathcal Z_d^{(0)})
   =
   R_B(K)+\tau(K,d,\pi).
   }
   \]

4. **Bayes error equals exact repair distance precisely under a Hall coverage condition.** Form the bipartite graph `G_B` with left vertices `A`, right vertices `Y`, and edge
   \[
   a\sim y
   \iff
   q_a(y)=m(y),
   \]
   so an edge means that class `a` is Bayes-optimal at output `y`, allowing ties. Then
   \[
   \boxed{
   \tau=0
   \iff
   G_B\text{ has a matching saturating }A
   }
   \]
   and hence, by Hall's theorem,
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}
   (K,\mathcal Z_d^{(0)})=R_B(K)
   }
   \]
   if and only if
   \[
   |N(C)|\ge|C|
   \qquad
   \text{for every }C\subseteq A.
   \]

5. **Small Bayes error can substantially understate structural repair cost.** A Bayes classifier is free never to predict a low-prior discriminator class. A zero-error faithful channel cannot erase such a class: because every upstream class occurs with positive prior, each must retain at least one output in its disjoint support. The difference is exactly `\tau`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{average decision accuracy measures mass assigned to a best label, while exact support fidelity additionally requires coverage of every discriminator class.}
}
\]

Thus a scalar Bayes-risk summary can be close to optimal while the channel remains far, in the same total-variation geometry, from any representation that preserves the discriminator with zero error.

## Derivation

### Zero-error channels are classwise support partitions

Take `L\in\mathcal Z_d^{(0)}`. For each class `a\in A`, let

\[
S_a
=
\bigcup_{x:d(x)=a}\operatorname{supp}(L_x).
\]

Because each class contains at least one upstream state and every row is a probability distribution, every `S_a` is nonempty. AF-011 zero-error fidelity says that

\[
S_a\cap S_b=\varnothing
\qquad(a\ne b).
\]

Conversely, if nonempty disjoint subsets `S_a\subseteq Y` are chosen and every row with `d(x)=a` is supported on `S_a`, then cross-class supports are disjoint and the resulting channel belongs to `\mathcal Z_d^{(0)}`.

Therefore zero-error repair can be studied by deciding which outputs are reserved for which discriminator classes.

The nonemptiness boundary is immediate. If `|Y|<|A|`, no family of `m` nonempty pairwise disjoint supports can exist. If `|Y|\ge m`, assign one distinct output to each class and use point-mass rows. Hence

\[
\boxed{
\mathcal Z_d^{(0)}\ne\varnothing
\iff
|Y|\ge|A|.
}
\]

The theorem below works on the nonempty side of this boundary.

### Lower bound from any zero-error repair

For a probability measure `P` and a nonempty subset `S\subseteq Y`, every probability measure `Q` supported on `S` satisfies

\[
\operatorname{TV}(P,Q)
\ge
P(Y\setminus S),
\]

because total variation dominates the discrepancy on the event `Y\setminus S` and `Q(Y\setminus S)=0`.

Apply this to each row of `K` and the corresponding zero-error support `S_{d(x)}` of `L`. Then

\[
\begin{aligned}
\rho_\pi(K,L)
&\ge
\sum_x\pi_xK_x(Y\setminus S_{d(x)})\\
&=
1-
\sum_{a\in A}
\sum_{x:d(x)=a}\pi_xK_x(S_a)\\
&=
1-
\sum_{a\in A}q_a(S_a).
\end{aligned}
\]

The `S_a` need not cover all of `Y`. Assign each unused output arbitrarily to one class. This enlarges the disjoint nonempty family to a partition

\[
Y=\bigsqcup_{a\in A}Y_a
\]

with `S_a\subseteq Y_a`. Since every `q_a` is nonnegative,

\[
\sum_aq_a(S_a)
\le
\sum_aq_a(Y_a)
\le
A_{\mathrm{surj}}(K,d,\pi).
\]

Thus every zero-error repair obeys

\[
\rho_\pi(K,L)
\ge
1-A_{\mathrm{surj}}(K,d,\pi).
\]

### An optimal partition attains the lower bound

Choose an optimal surjective labeling `\delta`, equivalently a partition into nonempty cells

\[
Y_a=\delta^{-1}(a),
\qquad
Y=\bigsqcup_aY_a.
\]

For each class choose one representative output

\[
y_a\in Y_a.
\]

For a row `x` with `d(x)=a`, let

\[
r_x=K_x(Y\setminus Y_a)
\]

be the mass currently lying outside its assigned class cell. Define `L_x` by deleting all mass outside `Y_a` and placing exactly that deleted mass at `y_a`:

\[
L_x(y)
=
\begin{cases}
0,&y\notin Y_a,\\
K_x(y),&y\in Y_a\setminus\{y_a\},\\
K_x(y_a)+r_x,&y=y_a.
\end{cases}
\]

Every `L_x` is a probability distribution supported on `Y_a`, so `L\in\mathcal Z_d^{(0)}`. The removed `\ell^1` mass is `r_x` and the added mass is also `r_x`, hence

\[
\operatorname{TV}(K_x,L_x)=r_x.
\]

Therefore

\[
\begin{aligned}
\rho_\pi(K,L)
&=
\sum_x\pi_xr_x\\
&=
1-
\sum_aq_a(Y_a)\\
&=
1-A_{\mathrm{surj}}(K,d,\pi).
\end{aligned}
\]

This matches the lower bound and proves

\[
\boxed{
\operatorname{dist}_{\rho_\pi}
(K,\mathcal Z_d^{(0)})
=
1-A_{\mathrm{surj}}.
}
\]

The explicit construction also proves that a nearest zero-error channel exists.

Because the right-hand side depends only on `q_a(y)`, the minimum distance forgets every distinction among rows inside the same discriminator class. That loss is legitimate here: the target property itself asks only whether `d(X)` is determined with zero error, not whether the original state `X` is recoverable.

## Bayes error plus a surjectivity penalty

For an arbitrary labeling `\delta:Y\to A`, define its penalty relative to pointwise Bayes choice by

\[
\operatorname{pen}(\delta)
=
\sum_{y\in Y}
\bigl(m(y)-q_{\delta(y)}(y)\bigr)
=
\sum_y c(\delta(y),y).
\]

Since

\[
A_B
=
\sum_y m(y),
\]

we have

\[
\sum_yq_{\delta(y)}(y)
=
A_B-\operatorname{pen}(\delta).
\]

Thus

\[
A_{\mathrm{surj}}
=
A_B-
\min_{\delta:Y\twoheadrightarrow A}
\operatorname{pen}(\delta).
\]

It remains to identify the minimum surjectivity penalty.

Take any surjective `\delta`. For each class `a`, choose one representative

\[
y_a\in\delta^{-1}(a).
\]

The representatives are distinct, so `a\mapsto y_a` is an injection. Since all costs are nonnegative,

\[
\operatorname{pen}(\delta)
\ge
\sum_ac(a,y_a)
\ge
\tau.
\]

Conversely, let `\iota:A\hookrightarrow Y` attain `\tau`. Define a labeling by forcing

\[
\delta(\iota(a))=a
\qquad(a\in A)
\]

and assigning every remaining output to any Bayes-optimal class at that output. This labeling is surjective, its non-representative outputs have zero cost, and

\[
\operatorname{pen}(\delta)
=
\sum_ac(a,\iota(a))
=
\tau.
\]

Hence

\[
\min_{\delta:Y\twoheadrightarrow A}
\operatorname{pen}(\delta)
=
\tau
\]

and therefore

\[
\boxed{
\operatorname{dist}_{\rho_\pi}
(K,\mathcal Z_d^{(0)})
=
R_B(K)+\tau(K,d,\pi).
}
\]

The extra term is a minimum-cost matching problem, not another probabilistic approximation.

## Hall criterion for when Bayes error is already exact

By construction,

\[
c(a,y)=0
\iff
q_a(y)=m(y).
\]

Therefore `\tau=0` exactly when there exists an injection `\iota:A\hookrightarrow Y` selecting, for every class `a`, a distinct output at which `a` is Bayes-optimal. This is exactly a matching saturating the class side of the bipartite graph `G_B`.

Hall's marriage theorem gives the equivalent criterion

\[
\boxed{
|N(C)|\ge|C|
\quad
\text{for all }C\subseteq A.
}
\]

Thus Bayes error is the exact distance to zero-error fidelity only when pointwise-optimal labels collectively contain enough distinct outputs to represent every discriminator class.

This distinguishes **local optimality** from **global coverage**. Bayes classification decides each output independently. Zero-error repair imposes a global partition constraint because the post-repair support cells must be nonempty and disjoint across all classes simultaneously.

## Exact control: low Bayes error but large repair cost

Let

\[
X=A=\{1,2\},
\qquad
Y=\{u,v\},
\qquad
d(x)=x,
\]

with prior

\[
\pi_1=0.9,
\qquad
\pi_2=0.1,
\]

and identical channel rows

\[
K_1=K_2=
\left(\frac12,\frac12\right).
\]

Then for both outputs,

\[
q_1(y)=0.45,
\qquad
q_2(y)=0.05.
\]

Bayes always predicts class `1`, giving

\[
A_B=0.9,
\qquad
R_B=0.1.
\]

But class `2` is never Bayes-optimal. For either output,

\[
c(2,y)=0.45-0.05=0.40,
\]

while class `1` has zero cost. Any injection representing both classes therefore has

\[
\tau=0.40.
\]

The theorem gives

\[
\boxed{
\operatorname{dist}_{\rho_\pi}
(K,\mathcal Z_d^{(0)})
=0.1+0.4
=0.5.
}
\]

This can also be checked directly. With only two outputs, a zero-error repair must put the two discriminator classes on opposite singleton supports. Each original uniform row is at TV distance `1/2` from either point mass, so every such repair costs

\[
0.9\cdot\frac12
+
0.1\cdot\frac12
=
\frac12.
\]

The average decision problem therefore reports only `10%` error while exact discriminator fidelity is still half of the maximum possible joint-TV repair distance away.

## Relationship to AF-009, AF-011, and AF-046

AF-009 studies probability-weighted `L^2` and Bayes defects. AF-011 identifies the exact support-confusability condition for one-sample zero-error recovery. AF-046 then shows that zero-error fidelity has **zero safety radius** against failure under row-sup total variation: an arbitrarily small activation of a forbidden support coordinate destroys exactness.

The present result asks the opposite one-sided question:

\[
\text{not ``how far can a faithful channel move before failing?''}
\]

but

\[
\text{``how far is an arbitrary channel from the nearest faithful one?''}
\]

Under the prior-weighted TV geometry this repair distance is generally positive and exactly computable. There is no contradiction with AF-046. A set may have empty interior and still be a positive distance away from many points outside it.

The Bayes decomposition sharpens the line's recurring distinction between scalar performance and structural provenance. Ordinary Bayes risk measures how much probability mass is assigned to the wrong best label. It does not require every discriminator value to survive as a separately represented possibility. The Hall term is exactly the missing global coverage constraint.

This is a concrete example of the README's broader warning:

\[
\boxed{
\text{good compressed performance}
\not\Rightarrow
\text{proximity to a representation that preserves the full discriminator.}
}
\]

## Prior art and novelty assessment

The ingredients surrounding this result are classical.

- David Blackwell, **“Equivalent Comparisons of Experiments,”** *The Annals of Mathematical Statistics* 24(2), 265–272 (1953), DOI `10.1214/aoms/1177729032`, is foundational prior art for comparing statistical experiments by the decision problems they support. It establishes the conceptual boundary that preservation of one Bayes decision problem is weaker than preservation of the whole experiment.
- Lucien Le Cam, **“Sufficiency and Approximate Sufficiency,”** *The Annals of Mathematical Statistics* 35(4), 1419–1455 (1964), DOI `10.1214/aoms/1177700372`, supplies the classical approximate-experiment / total-variation deficiency framework. Le Cam deficiency optimizes a Markov simulation between experiments and uses a worst-parameter comparison; `\rho_\pi` here instead directly perturbs the fixed channel rows under one declared prior, so the present metric projection is not a restatement of deficiency.
- P. Hall, **“On Representatives of Subsets,”** *Journal of the London Mathematical Society* s1-10(1), 26–30 (1935), DOI `10.1112/jlms/s1-10.37.26`, is the primary source for the matching criterion used to characterize when every discriminator class has a distinct Bayes-optimal representative output.
- Shannon/Witsenhausen zero-error and confusability-graph prior art is already audited in AF-011 and `SOURCES.md`; multiclass experiment and Bayes-risk prior art is already audited in AF-013.

No novelty is claimed for Bayes classification, total variation, Blackwell comparison, Le Cam deficiency, Hall matching, or zero-error confusability.

A bounded literature search did not locate the exact combined statement that the prior-weighted TV metric projection of a finite channel onto AF-011's zero-error support-faithful set equals a **surjective Bayes assignment loss**, with the excess over ordinary Bayes error given by the minimum Hall-coverage matching cost. Absence from that search is not a proof of novelty. The result should therefore be treated conservatively as an exact derived synthesis whose value is the structural decomposition and audit rule, not as a claim that the surrounding theories lack equivalent formulations.

## Boundaries and failure modes

- The theorem is finite-alphabet. Countable or continuous outputs require measurable partitions, support or essential-support choices, and existence/compactness arguments that are not covered here.
- The prior is strictly positive on every upstream state. If zero prior is allowed, `\rho_\pi` becomes a pseudometric and classes supported only on zero-prior states can be altered at no cost. One should first restrict to the positive-prior support.
- The assumption `|Y|\ge|A|` is structural, not technical. Otherwise the zero-error faithful set is empty because nonempty disjoint class supports cannot fit in the output alphabet.
- The metric `\rho_\pi` is prior-weighted average row TV. It is not AF-046's row-sup metric, Le Cam deficiency, Blackwell order, Wasserstein distance, KL divergence, or a topology that fixes support. The projection formula must not be transferred to those geometries without proof.
- The target property is exact recovery of the discriminator `d(X)`, not the full state `X`. Within-class row differences are intentionally irrelevant to the minimum cost because zero-error fidelity permits arbitrary confusability among states sharing the same discriminator value.
- The construction allows arbitrary changes of the channel probabilities while keeping the alphabets and prior fixed. If admissible repairs are constrained by physics, locality, symmetry, sparsity, a parametric family, or another intrinsic category, `1-A_{\mathrm{surj}}` is only a lower bound unless the explicit repaired channel remains admissible.
- `R_B` is the one-sample `0-1` Bayes risk for the declared prior. A small value can result entirely from prior imbalance, as the exact control shows. It should not be interpreted as preservation of rare discriminator classes.
- The Hall condition concerns Bayes-optimal ties in the current channel. If it fails, a positive matching penalty is unavoidable for exact supportwise repair, but this does not imply any particular class must be preserved by a different downstream scientific objective.
- The result says nothing about asymptotic zero-error capacity, repeated channel uses, coding blocklength, or error exponents.

## Decisive audit rule

For a stochastic compression whose downstream mathematics requires exact discriminator survival and whose perturbation cost is prior-weighted total variation:

1. form the class-output masses
   \[
   q_a(y)=\sum_{x:d(x)=a}\pi_xK(y\mid x);
   \]
2. compute ordinary Bayes error
   \[
   R_B=1-\sum_y\max_aq_a(y);
   \]
3. build the Bayes-optimal bipartite graph `a\sim y` when `q_a(y)=\max_bq_b(y)`;
4. test Hall coverage. If every class can receive a distinct Bayes-optimal output, then
   \[
   \operatorname{dist}(K,\mathcal Z_d^{(0)})=R_B;
   \]
5. if Hall coverage fails, solve the minimum-cost injection with costs
   \[
   c(a,y)=\max_bq_b(y)-q_a(y)
   \]
   and add its value `\tau` to `R_B`.

Do not use a small Bayes error by itself as evidence that the channel is close to exact structural fidelity. The missing certificate is global class coverage.

## Consequence for the line

AF-046 showed that exact support fidelity can be **infinitesimally fragile from the inside**. AF-047 shows that it nevertheless has an exact and often nontrivial **repair geometry from the outside**.

More importantly, the repair distance splits into two conceptually distinct terms:

\[
\boxed{
\text{local decision error}
+
\text{global discriminator-coverage penalty}.
}
\]

The second term vanishes exactly under a matching theorem. This is a clean finite model of a recurring Arithmetic Fidelity theme: preserving each locally optimal statistic is not enough when the intended upstream structure imposes a global relational requirement across the retained outputs.

Future compression audits should therefore ask not only whether each retained observable is locally informative, but whether the collection of retained observables admits a globally compatible witness for every discriminator component that must survive.