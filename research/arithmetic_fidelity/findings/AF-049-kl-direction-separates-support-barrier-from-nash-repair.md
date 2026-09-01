# AF-049 — KL direction separates support barriers from Nash-welfare repair

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D,
\qquad
A=d(X),
\qquad
m=|A|,
\]

and assume `|Y|\ge m`. Let `K:X\rightsquigarrow Y` be a stochastic channel, fix a strictly positive prior

\[
\pi_x>0,
\qquad
\sum_{x\in X}\pi_x=1,
\]

and let `\mathcal Z_d^{(0)}` be AF-011's zero-error faithful set: rows from distinct discriminator classes have disjoint output supports.

For probability distributions `P,Q` on `Y`, use extended-valued Kullback--Leibler divergence

\[
D(P\|Q)
=
\sum_{y:P(y)>0}P(y)\log\frac{P(y)}{Q(y)},
\]

with `D(P\|Q)=+\infty` whenever `P` is not absolutely continuous with respect to `Q`. Define the two directional channel divergences

\[
\rho_{\to}(K,L)
=
\sum_x\pi_xD(K_x\|L_x),
\qquad
\rho_{\leftarrow}(K,L)
=
\sum_x\pi_xD(L_x\|K_x).
\]

Then:

1. **Forward KL gives an all-or-nothing zero-error repair barrier.**
   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}\rho_{\to}(K,L)
   =
   \begin{cases}
   0,&K\in\mathcal Z_d^{(0)},\\
   +\infty,&K\notin\mathcal Z_d^{(0)}.
   \end{cases}
   }
   \]
   A support conflict in `K` cannot be repaired at any finite forward-KL cost because every zero-error repair must set at least one positive conflicting transition to zero.

2. **Reverse KL has an exact partition projection.** For a partition into nonempty class cells
   \[
   Y=\bigsqcup_{a\in A}Y_a,
   \]
   put
   \[
   J_{\mathrm{KL}}(K;(Y_a))
   =
   \sum_{x\in X}
   \pi_x\bigl[-\log K_x(Y_{d(x)})\bigr],
   \]
   with `-\log0=+\infty`. Then
   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}
   \rho_{\leftarrow}(K,L)
   =
   \min_{Y=\bigsqcup_aY_a}
   J_{\mathrm{KL}}(K;(Y_a)).
   }
   \]
   Whenever the value is finite, a nearest repair is obtained rowwise by conditioning:
   \[
   L_x
   =
   K_x(\,\cdot\mid Y_{d(x)}).
   \]

3. **The reverse-KL projection maximizes retained geometric mean.** Define
   \[
   G_{\mathrm{KL}}(K,d,\pi)
   =
   \max_{Y=\bigsqcup_aY_a}
   \prod_{x\in X}
   K_x(Y_{d(x)})^{\pi_x},
   \]
   with product value zero when any required retained mass is zero. Then
   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}
   \rho_{\leftarrow}(K,L)
   =
   -\log G_{\mathrm{KL}}(K,d,\pi).
   }
   \]
   Thus reverse relative entropy does not aggregate retained mass additively as AF-047 does and does not optimize the worst row as AF-048 does: it optimizes a weighted geometric mean.

4. **With one row per discriminator class, reverse-KL repair is weighted Nash social welfare.** If `X=A` and `d` is the identity, each output `y` is an indivisible item, class `a` has additive bundle utility
   \[
   u_a(S)=K_a(S)=\sum_{y\in S}K_a(y),
   \]
   and the reverse-KL projection maximizes
   \[
   \prod_{a\in A}u_a(Y_a)^{\pi_a}.
   \]
   This is exactly the weighted Nash-social-welfare allocation objective.

5. **Identical rows still produce a hard global partition problem.** Suppose there is one row per class, all rows equal the same rational distribution `p`, and `\pi_a=1/m`. Then
   \[
   \inf_{L\in\mathcal Z_d^{(0)}}
   \rho_{\leftarrow}(K,L)
   =
   -\log
   \left(
   \max_{Y=\bigsqcup_aY_a}
   \Bigl[\prod_{a=1}^m p(Y_a)\Bigr]^{1/m}
   \right).
   \]
   Since `\sum_ap(Y_a)=1`, AM--GM gives
   \[
   \boxed{
   \inf\rho_{\leftarrow}\ge\log m,
   }
   \]
   with equality exactly when the output symbols can be partitioned into `m` cells of common-row mass `1/m`. Restricted `3-PARTITION` therefore makes recognition of this equality strongly NP-complete. The equivalent exact reverse-KL repair optimization is strongly NP-hard even though the channel laws contain no discriminator information before repair.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{support-sensitive repair is not determined by the target property alone: divergence direction decides whether deleting a conflict is forbidden, finite, or a global allocation problem.}
}
\]

Relative entropy is therefore not merely another smooth scalar defect to substitute for total variation. Its absolute-continuity asymmetry changes the admissible support surgery, while its logarithmic geometry changes the global objective from utilitarian retained mass or max-min retention to multiplicative retained mass.

## Derivation

### Forward KL cannot delete a conflicting positive transition

Suppose first that `K\notin\mathcal Z_d^{(0)}`. By AF-011 there exist `x,x'\in X` and `y\in Y` such that

\[
d(x)\ne d(x'),
\qquad
K_x(y)>0,
\qquad
K_{x'}(y)>0.
\]

Take any `L\in\mathcal Z_d^{(0)}`. Zero-error faithfulness forbids the same output from lying in the supports of rows from two different discriminator classes. Hence at least one of

\[
L_x(y),\qquad L_{x'}(y)
\]

must equal zero.

If `L_x(y)=0`, then `K_x(y)>0` while `L_x(y)=0`, so

\[
D(K_x\|L_x)=+\infty.
\]

If instead `L_{x'}(y)=0`, then

\[
D(K_{x'}\|L_{x'})=+\infty.
\]

Because every prior weight is strictly positive,

\[
\rho_{\to}(K,L)=+\infty.
\]

This holds for every zero-error repair `L`, proving

\[
\inf_{L\in\mathcal Z_d^{(0)}}\rho_{\to}(K,L)=+\infty.
\]

Conversely, if `K\in\mathcal Z_d^{(0)}`, choose `L=K`; then the divergence is zero. This proves the forward formula.

The strict positivity of `\pi` is essential to the stated discriminator-wide result. If a conflicting row had zero prior weight, the weighted divergence could ignore the infinite row cost even though the channel itself still violated zero-error fidelity.

### Reverse KL projection onto one support cell

Fix a probability distribution `P` on `Y` and a nonempty subset `S\subseteq Y`.

If `P(S)=0`, every probability distribution `Q` supported on `S` places positive mass where `P` is zero, so

\[
D(Q\|P)=+\infty.
\]

Now assume `P(S)>0` and write

\[
P_S=P(\,\cdot\mid S).
\]

For every probability distribution `Q` supported on `S`,

\[
\begin{aligned}
D(Q\|P)
&=
\sum_{y\in S}Q(y)
\log\frac{Q(y)}{P(y)}\\
&=
\sum_{y\in S}Q(y)
\log\frac{Q(y)}{P_S(y)}
-
\log P(S)\\
&=
D(Q\|P_S)-\log P(S).
\end{aligned}
\]

Gibbs' inequality therefore gives the exact support-projection identity

\[
\boxed{
\min_{Q:\operatorname{supp}(Q)\subseteq S}
D(Q\|P)
=
-\log P(S),
}
\]

with unique minimizer `Q=P_S` whenever `P(S)>0`.

This is the elementary finite-support specialization of classical relative-entropy / I-divergence projection geometry.

### Every zero-error repair induces disjoint class cells

Take `L\in\mathcal Z_d^{(0)}`. For each discriminator class `a\in A`, let

\[
S_a
=
\bigcup_{x:d(x)=a}\operatorname{supp}(L_x).
\]

Every `S_a` is nonempty and

\[
S_a\cap S_b=\varnothing
\qquad(a\ne b).
\]

For each row `x` of class `a`, the preceding support-projection identity implies

\[
D(L_x\|K_x)
\ge
-\log K_x(S_a),
\]

with the convention that the right side is `+\infty` if `K_x(S_a)=0`.

Assign every unused output symbol to an arbitrary class, producing a partition

\[
Y=\bigsqcup_{a\in A}Y_a,
\qquad
S_a\subseteq Y_a.
\]

Since `K_x(Y_a)\ge K_x(S_a)` and `-\log` is decreasing,

\[
D(L_x\|K_x)
\ge
-\log K_x(Y_a).
\]

Summing with prior weights yields

\[
\rho_{\leftarrow}(K,L)
\ge
\sum_x\pi_x[-\log K_x(Y_{d(x)})].
\]

Therefore every reverse-KL repair obeys

\[
\rho_{\leftarrow}(K,L)
\ge
\min_{Y=\bigsqcup_aY_a}
J_{\mathrm{KL}}(K;(Y_a)).
\]

### Conditioning on an optimal partition attains the bound

There are finitely many partitions of finite `Y`, so an extended-valued minimum exists. Choose a minimizing partition

\[
Y=\bigsqcup_aY_a.
\]

If its objective is finite, then

\[
K_x(Y_{d(x)})>0
\qquad
\text{for every }x.
\]

Define

\[
L_x
=
K_x(\,\cdot\mid Y_{d(x)}).
\]

Rows belonging to class `a` are supported inside `Y_a`, and the cells are disjoint, so

\[
L\in\mathcal Z_d^{(0)}.
\]

The support-projection identity gives rowwise

\[
D(L_x\|K_x)
=
-\log K_x(Y_{d(x)}).
\]

Hence

\[
\rho_{\leftarrow}(K,L)
=
J_{\mathrm{KL}}(K;(Y_a)),
\]

which matches the lower bound.

If every partition has infinite objective, then the lower-bound argument shows that every zero-error `L` has infinite reverse divergence, so the infimum is also `+\infty`. Thus the partition formula remains exact in the extended sense.

Exponentiating the finite formula gives

\[
\exp(-\rho_{\leftarrow})
=
\prod_xK_x(Y_{d(x)})^{\pi_x},
\]

so minimizing reverse KL is exactly maximizing weighted retained geometric mean.

## Feasibility boundary for finite reverse-KL repair

Reverse KL is not automatically finite. Its exact finiteness condition is

\[
\boxed{
\exists\;Y=\bigsqcup_{a\in A}Y_a
\text{ such that }
K_x(Y_{d(x)})>0
\text{ for every }x.
}
\]

Equivalently, the output alphabet can be assigned to discriminator classes so that every row retains some positive original mass inside its own class cell.

This condition is strictly weaker than requiring the original channel to be zero-error, but stronger than the mere nonemptiness of `\mathcal Z_d^{(0)}`.

For example, with

\[
X=A=\{0,1\},
\qquad
Y=\{a,b\},
\]

and

\[
K_0=(0.9,0.1),
\qquad
K_1=(0.2,0.8),
\]

the original channel has complete support overlap and therefore fails AF-011. Forward-KL repair is infinite. Reverse-KL repair is finite: choose `Y_0=\{a\}`, `Y_1=\{b\}` and condition the rows.

In contrast, if both rows equal the same point mass `\delta_a`, then no disjoint class partition gives positive retained mass to both classes. Both forward and reverse KL distances to zero-error fidelity are infinite even though `|Y|\ge2` makes the abstract zero-error target set nonempty.

Thus reverse KL permits **deleting** original mass but cannot create positive mass at a previously impossible transition. Forward KL has the opposite absolute-continuity requirement relative to the repair target: it cannot delete any positive original transition at finite cost. This directional support rule is the mechanism behind the asymmetry.

## One-row-per-class specialization: Nash social welfare

Assume `X=A` and `d(a)=a`. For a partition `(Y_a)`, define additive bundle utility

\[
u_a(Y_a)=K_a(Y_a).
\]

Then

\[
G_{\mathrm{KL}}(K,d,\pi)
=
\max_{Y=\bigsqcup_aY_a}
\prod_a u_a(Y_a)^{\pi_a}.
\]

The weighted geometric mean of additive utilities is exactly weighted Nash social welfare. Hence the same fixed zero-error repair target that produced

- a **utilitarian retained-mass** objective under AF-047's prior-weighted average TV;
- a **max-min retained-mass** objective under AF-048's row-sup TV;

produces a **multiplicative / Nash-welfare retained-mass** objective under reverse KL.

This is not a metaphor: the optimization variables, indivisible output items, additive valuations, partition constraint, and weighted geometric objective coincide exactly.

With multiple upstream rows in one discriminator class, a class cell `Y_a` simultaneously serves all rows of that class, and its contribution becomes

\[
\prod_{x:d(x)=a}K_x(Y_a)^{\pi_x}.
\]

The projection remains exact, but this grouped robust/product utility is no longer the ordinary one-agent-per-row Nash-welfare model.

## Strong hardness with identical rows

Take a restricted `3-PARTITION` instance

\[
w_1,\ldots,w_{3m},
\qquad
\sum_{j=1}^{3m}w_j=mB,
\qquad
\frac B4<w_j<\frac B2.
\]

Construct

\[
X=A=\{1,\ldots,m\},
\qquad
Y=\{1,\ldots,3m\},
\qquad
\pi_a=\frac1m,
\]

and give every class the identical row

\[
K_a(j)=p_j=\frac{w_j}{mB}.
\]

For every partition `Y=\bigsqcup_aY_a`,

\[
\sum_{a=1}^m p(Y_a)=1.
\]

Therefore AM--GM yields

\[
\left(\prod_{a=1}^m p(Y_a)\right)^{1/m}
\le
\frac1m,
\]

with equality exactly when

\[
p(Y_a)=\frac1m
\qquad
\text{for every }a.
\]

That is equivalent to

\[
\sum_{j\in Y_a}w_j=B
\qquad
\text{for every }a.
\]

The restricted weight bounds force every such cell to contain exactly three items. Hence

\[
\max_{Y=\bigsqcup_aY_a}
\left(\prod_ap(Y_a)\right)^{1/m}
=
\frac1m
\]

if and only if the original `3-PARTITION` instance is feasible.

Equivalently,

\[
\boxed{
\inf_{L\in\mathcal Z_d^{(0)}}
\rho_{\leftarrow}(K,L)
=
\log m
\iff
3\text{-PARTITION is feasible}.
}
\]

Recognizing whether the optimal retained Nash product reaches the rational threshold `m^{-m}` is therefore strongly NP-complete, and exact reverse-KL repair optimization is strongly NP-hard.

As in AF-048, all original rows are identical. The hardness is not statistical inference from `K`; it is global compatibility of the provenance assignment required to build a zero-error representation on an indivisible output alphabet.

## Relationship to AF-011, AF-046, AF-047, and AF-048

AF-011 identifies support overlap as the exact one-sample zero-error obstruction. AF-046 then shows that the zero-error set is nowhere dense under total variation: arbitrarily small activation of a zero transition destroys exact recovery.

AF-047 asks instead how far an arbitrary channel lies from the zero-error set under **average TV** and obtains a maximum retained total mass, or Bayes error plus a Hall coverage penalty. AF-048 changes only the row aggregation to **row-sup TV** and obtains max-min allocation, including strong hardness on identical-row channels.

AF-049 keeps the same target set and prior but changes the discrepancy geometry. Two effects appear:

1. **directional support admissibility:** forward KL makes every genuine support conflict infinitely expensive to repair, while reverse KL permits support deletion by conditioning whenever a compatible class partition exists;
2. **multiplicative aggregation:** the reverse-KL projection converts retained row masses into a weighted geometric mean and therefore into Nash-welfare allocation in the one-row-per-class case.

The sequence now gives three exact projection geometries for the same structural target:

\[
\begin{array}{c|c}
\text{repair geometry} & \text{global retained-mass objective}\\
\hline
\text{prior-weighted average TV (AF-047)} & \text{sum / utilitarian}\\
\text{row-sup TV (AF-048)} & \text{minimum / egalitarian}\\
\text{reverse KL (AF-049)} & \text{geometric mean / Nash welfare}
\end{array}
\]

and forward KL supplies a fourth behavior: a support barrier with no finite graded projection away from the zero-error set.

This is a clean instance of the line's mandate. A scalar notion of "distance to faithful structure" is not intrinsic until both the admissible support changes and the aggregation geometry of the discrepancy have been fixed.

## Prior art and novelty audit

The relative-entropy ingredients are classical.

- Solomon Kullback and Richard A. Leibler, **"On Information and Sufficiency,"** *The Annals of Mathematical Statistics* 22(1), 79--86 (1951), DOI `10.1214/aoms/1177729694`, is the primary source for the divergence and its relation to statistical sufficiency.
- Imre Csiszár, **"I-Divergence Geometry of Probability Distributions and Minimization Problems,"** *The Annals of Probability* 3(1), 146--158 (1975), DOI `10.1214/aop/1176996454`, develops the classical projection geometry of relative entropy onto constrained families. The one-cell conditioning identity used here is an elementary finite-support specialization.
- Richard Cole and Vasilis Gkatzelis, **"Approximating the Nash Social Welfare with Indivisible Items,"** *SIAM Journal on Computing* 47(3), 1211--1236 (2018), DOI `10.1137/15M1053682`, is direct allocation prior art for maximizing the geometric mean of additive bundle utilities and records the classical computational hardness of the indivisible-item Nash-welfare problem.
- Michael R. Garey and David S. Johnson, ***Computers and Intractability: A Guide to the Theory of NP-Completeness***, W. H. Freeman (1979), is the standard source for the strongly NP-complete restricted `3-PARTITION` problem used in the explicit identical-row reduction.

No novelty is claimed for KL projection, Gibbs' inequality, Nash social welfare, AM--GM, or `3-PARTITION` hardness individually.

The Arithmetic Fidelity contribution is the exact comparative classification for the **same zero-error structural target**: forward relative entropy forbids the support deletion that every nontrivial zero-error repair requires, while reverse relative entropy turns that support deletion into a multiplicative allocation objective. Together with AF-047 and AF-048, this shows that repair geometry controls not just the numerical defect but the admissible structural surgery, welfare functional, and computational problem exposed by the projection.

A literature search found mature bodies of work on I-projections and on Nash-welfare allocation, but no reason to treat their conjunction here as a new external theorem. The durable point is the reduction/audit rule for Mathia: before interpreting a small divergence to a faithful set, specify the divergence direction and verify that its support absolute-continuity convention permits the structural modification the argument is supposed to measure.

## Boundary conditions and falsification checks

- `|Y|\ge|A|` is assumed so that the abstract zero-error set is nonempty. If `|Y|<|A|`, both repair problems have an empty target and require a separate convention for distance to the empty set.
- Strict positivity of every `\pi_x` is necessary for the forward all-or-nothing statement to audit every upstream row.
- The reverse-KL formula is extended-valued. It can be infinite even when zero-error channels exist, because a finite reverse projection cannot place repaired mass on an output that had zero mass in the corresponding original row.
- The nearest reverse projection need not be unique: several class partitions can attain the same optimum, although conditioning is the unique row minimizer for each fixed positive-mass cell.
- The result is not a metric statement. KL is asymmetric and does not satisfy the triangle inequality; the directional asymmetry is the mechanism, not a defect to be hidden.
- Replacing KL by a symmetrized or bounded divergence can change both support feasibility and objective geometry. No such extension is claimed here.
- The Nash-welfare identification is exact only in the one-row-per-discriminator-class specialization. Multiple rows sharing one class induce a grouped product utility.
- The hardness reduction concerns the discrete fixed-output-alphabet repair problem. Allowing an output symbol to be fractionally split among several discriminator classes changes the feasible set and removes the exact indivisibility mechanism used by the reduction.

## Consequences for Arithmetic Fidelity

1. **Divergence direction is part of the structural model.** Any fidelity claim based on KL must say which argument is the source representation and which is the repair. Swapping them can change a finite optimization problem into an infinite barrier.
2. **Support surgery must be audited before scalar optimization.** A divergence that assigns infinite cost to the required deletion or creation of support cannot serve as a graded measure of that structural repair.
3. **Aggregation geometry selects a welfare principle.** For zero-error support repair, sum, minimum, and geometric mean arise naturally from average TV, row-sup TV, and reverse KL respectively. These are mathematically different projections, not interchangeable norms on one latent notion of fidelity.
4. **A low-dimensional scalar defect can hide global combinatorics.** Even identical original rows can produce strongly hard repair because structural faithfulness requires a discrete assignment of output provenance.
5. **For later arithmetic applications, "close to a faithful representation" is meaningless without the discrepancy category.** A proposed prime-preserving repair must justify not only the retained discriminator but why its chosen topology/divergence allows the exact structural changes being invoked.