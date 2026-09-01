# AF-048 — Row-sup zero-error repair is max-min allocation

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

and assume `|Y|\ge m`. Let `K:X\rightsquigarrow Y` be a stochastic channel and equip the channel space with the row-sup total-variation metric

\[
\rho_\infty(K,L)
=
\max_{x\in X}\operatorname{TV}(K_x,L_x),
\qquad
\operatorname{TV}(P,Q)=\frac12\sum_{y\in Y}|P(y)-Q(y)|.
\]

Let `\mathcal Z_d^{(0)}` be the AF-011 zero-error faithful set: rows from distinct discriminator classes have disjoint output supports.

For a partition into nonempty class cells

\[
Y=\bigsqcup_{a\in A}Y_a,
\]

define its worst retained row mass

\[
r(K;(Y_a))
=
\min_{x\in X}K_x(Y_{d(x)}),
\]

and define the robust allocation value

\[
R_\infty(K,d)
=
\max_{Y=\bigsqcup_{a\in A}Y_a\atop Y_a\ne\varnothing}
\min_{x\in X}K_x(Y_{d(x)}).
\]

Then:

1. **The exact row-sup repair distance is a max-min partition value.**
   \[
   \boxed{
   \operatorname{dist}_{\rho_\infty}(K,\mathcal Z_d^{(0)})
   =
   1-R_\infty(K,d).
   }
   \]
   A nearest zero-error channel always exists.

2. **The metric changes the global optimization problem.** AF-047's prior-weighted average-TV projection maximizes total retained class mass. Row-sup TV instead maximizes the least retained mass of any upstream row. The same zero-error target set therefore has different projection geometry under average and worst-case aggregation.

3. **With one row per discriminator class, the projection is exactly max-min allocation.** If `X=A` and `d` is the identity, every output `y` is an indivisible item, class `a` values a bundle `S\subseteq Y` by
   \[
   u_a(S)=\sum_{y\in S}K_a(y),
   \]
   and
   \[
   R_\infty(K,d)
   =
   \max_{Y=\bigsqcup_aY_a}
   \min_a u_a(Y_a).
   \]
   This is the classical max-min fair allocation / Santa Claus objective. For several rows in one class, the class utility becomes the robust bundle utility `\min_{x:d(x)=a}K_x(S)`.

4. **Exact row-sup repair is strongly NP-hard, even when all conflicting channel rows are identical.** For rational channel entries, the threshold decision problem is strongly NP-complete. The hardness already holds in the one-row-per-class case with
   \[
   K_a=K_b
   \qquad
   \text{for every }a,b.
   \]
   Thus the computational obstruction can come entirely from globally assigning indivisible output provenance, not from statistical differences between the channel laws.

5. **Average repair can be trivial exactly where worst-case repair is hard.** In the identical-row construction with the uniform prior on `m` discriminator classes, AF-047 gives
   \[
   \boxed{
   \operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)})
   =1-\frac1m
   }
   \]
   for every common row distribution. By contrast,
   \[
   \boxed{
   \operatorname{dist}_{\rho_\infty}(K,\mathcal Z_d^{(0)})
   =
   1-\max_{Y=\bigsqcup_aY_a}\min_a K(Y_a),
   }
   \]
   and deciding whether this equals `1-1/m` is strongly NP-complete.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{the geometry and even the computational complexity of structural repair depend on how local losses are aggregated, not only on the fidelity property being repaired.}
}
\]

A compression can therefore look completely understood under an average scalar defect while retaining a hard global compatibility problem under a worst-case structural requirement.

## Derivation

### Zero-error repairs determine classwise support cells

Take `L\in\mathcal Z_d^{(0)}`. For every discriminator class `a\in A`, put

\[
S_a
=
\bigcup_{x:d(x)=a}\operatorname{supp}(L_x).
\]

Each `S_a` is nonempty, and zero-error fidelity gives

\[
S_a\cap S_b=\varnothing
\qquad(a\ne b).
\]

For a probability distribution `P` and a distribution `Q` supported on `S`, total variation obeys

\[
\operatorname{TV}(P,Q)\ge P(Y\setminus S)=1-P(S).
\]

Hence, for every row `x`,

\[
\operatorname{TV}(K_x,L_x)
\ge
1-K_x(S_{d(x)}),
\]

so

\[
\rho_\infty(K,L)
\ge
1-
\min_xK_x(S_{d(x)}).
\]

The disjoint family `(S_a)` need not cover `Y`. Assign every unused output to an arbitrary class. This produces a partition

\[
Y=\bigsqcup_aY_a,
\qquad
S_a\subseteq Y_a,
\]

and therefore

\[
\min_xK_x(S_{d(x)})
\le
\min_xK_x(Y_{d(x)})
\le
R_\infty(K,d).
\]

Thus every zero-error repair satisfies

\[
\boxed{
\rho_\infty(K,L)
\ge
1-R_\infty(K,d).
}
\]

### An optimal partition attains the lower bound

There are finitely many partitions of finite `Y`, so choose one attaining `R_\infty`:

\[
Y=\bigsqcup_aY_a.
\]

Choose one representative output `y_a\in Y_a` for every class. For a row `x` with `d(x)=a`, let

\[
r_x=K_x(Y\setminus Y_a).
\]

Construct `L_x` by deleting all mass outside `Y_a` and moving the deleted mass to `y_a`:

\[
L_x(y)
=
\begin{cases}
0,&y\notin Y_a,\\
K_x(y),&y\in Y_a\setminus\{y_a\},\\
K_x(y_a)+r_x,&y=y_a.
\end{cases}
\]

Every row in class `a` is now supported on `Y_a`; the cells are disjoint, so `L\in\mathcal Z_d^{(0)}`. The removed and added `\ell^1` masses are both `r_x`, hence

\[
\operatorname{TV}(K_x,L_x)
=r_x
=1-K_x(Y_a).
\]

Consequently

\[
\begin{aligned}
\rho_\infty(K,L)
&=
\max_x\bigl(1-K_x(Y_{d(x)})\bigr)\\
&=
1-\min_xK_x(Y_{d(x)})\\
&=
1-R_\infty(K,d).
\end{aligned}
\]

This matches the lower bound and proves both the exact distance formula and existence of a nearest repair.

## Max-min allocation specialization

Suppose there is exactly one row per discriminator class. Then an admissible zero-error support pattern is exactly a partition of the output alphabet into bundles `Y_a`, and each row contributes the additive bundle value

\[
K_a(Y_a)=\sum_{y\in Y_a}K_a(y).
\]

Therefore `R_\infty` is exactly the classical max-min allocation objective: distribute indivisible goods so as to maximize the utility of the least well-served agent.

Standard Santa Claus formulations may permit unassigned items or do not explicitly require every bundle to be nonempty. This does not change the optimum here. Utilities are nonnegative, so leftover items can be assigned without decreasing the minimum. If the optimum is positive, every agent already receives nonzero value and therefore at least one item. If the optimum is zero, `|Y|\ge m` permits a nonempty complete partition with the same value zero.

For multiple rows per class, the same partition survives but class `a` must protect all rows in that class:

\[
u_a(S)
=
\min_{x:d(x)=a}K_x(S).
\]

This is a robust max-min allocation problem rather than ordinary additive Santa Claus. The exact projection theorem itself does not require any complexity claim about this more general case.

## Strong NP-completeness even for identical channel rows

Reduce from `3-PARTITION`. Take a standard restricted instance with `3m` positive integers

\[
w_1,\ldots,w_{3m},
\qquad
\sum_{j=1}^{3m}w_j=mB,
\qquad
\frac B4<w_j<\frac B2.
\]

The question is whether the numbers can be partitioned into `m` triples, each summing to `B`. This restricted problem is strongly NP-complete.

Construct the channel instance

\[
X=A=\{1,\ldots,m\},
\qquad
d(a)=a,
\qquad
Y=\{1,\ldots,3m\},
\]

with **identical rows**

\[
K_a(j)
=
p_j
=
\frac{w_j}{mB}
\qquad
\text{for every }a.
\]

The common row is a probability distribution because `\sum_jp_j=1`. For every partition `Y=\bigsqcup_aY_a`,

\[
\sum_{a=1}^mK(Y_a)=1,
\]

so

\[
\min_aK(Y_a)\le\frac1m.
\]

Equality holds if and only if every cell has common-row mass exactly `1/m`, equivalently

\[
\sum_{j\in Y_a}w_j=B
\qquad
\text{for every }a.
\]

The bounds `B/4<w_j<B/2` force every such cell to contain exactly three items. Therefore

\[
R_\infty(K,d)=\frac1m
\]

if and only if the original `3-PARTITION` instance is a yes-instance. By the projection theorem,

\[
\boxed{
\operatorname{dist}_{\rho_\infty}(K,\mathcal Z_d^{(0)})
\le
1-\frac1m
\iff
\operatorname{dist}_{\rho_\infty}(K,\mathcal Z_d^{(0)})
=
1-\frac1m
\iff
3\text{-PARTITION is feasible}.
}
\]

For rational channel entries the decision problem is in NP: a partition is a certificate, and its retained masses can be checked exactly in polynomial time. The reduction preserves the strong form of `3-PARTITION`; normalization by `mB` has polynomial encoding length. Hence this row-sup repair threshold problem is strongly NP-complete, and exact distance computation is strongly NP-hard.

The striking point is that every row of `K` is identical. Before repair, the output law contains no statistical information at all about the discriminator. The hardness is instead caused by the requirement that the repaired representation assign the finite output symbols to mutually exclusive class supports while minimizing the worst row perturbation.

## Exact separation from AF-047's average geometry

Use the same one-row-per-class identical-row channel and put the uniform prior

\[
\pi_a=\frac1m.
\]

AF-047 uses class-output masses

\[
q_a(y)
=
\pi_aK_a(y)
=
\frac1m p_y.
\]

They are identical across `a`. For every surjective labeling `\delta:Y\twoheadrightarrow A`,

\[
\sum_{y\in Y}q_{\delta(y)}(y)
=
\frac1m\sum_yp_y
=
\frac1m.
\]

Thus AF-047 gives, without solving any partition problem,

\[
\boxed{
\operatorname{dist}_{\rho_\pi}(K,\mathcal Z_d^{(0)})
=1-\frac1m.
}
\]

Equivalently, ordinary Bayes error is already `1-1/m`; every class is tied as Bayes-optimal at every output, so Hall coverage has zero penalty whenever `|Y|\ge m`.

Under row-sup TV, however,

\[
\operatorname{dist}_{\rho_\infty}(K,\mathcal Z_d^{(0)})
=
1-\max_{Y=\bigsqcup_aY_a}\min_a p(Y_a),
\]

and reaching the lower bound `1-1/m` requires an exactly balanced indivisible partition, which the reduction above makes strongly NP-complete to recognize.

Hence the difference between AF-047 and AF-048 is not merely a different constant or norm equivalence. On the same channels and the same target set,

\[
\boxed{
\text{average-TV projection collapses the global partition structure, while row-sup projection retains it.}
}
\]

A fractional relaxation could split output mass among several classes and equalize the identical-row example at `1/m`; that relaxation is not an admissible zero-error repair on the fixed output alphabet. The discrete gap is precisely the indivisibility of output provenance.

## Relationship to AF-011, AF-046, and AF-047

AF-011 identifies the exact support-confusability condition for one-sample zero-error recovery. AF-046 shows that this exact property has no positive row-sup-TV safety radius from the inside: arbitrarily small support activation creates failure. AF-047 computes the nearest faithful repair from the outside under **prior-weighted average** row TV.

AF-048 closes the corresponding row-sup projection question. It shows that a faithful set can simultaneously be nowhere robust from the inside and have a nontrivial, exactly characterized distance from arbitrary outside points. More importantly, changing only the aggregation of rowwise perturbations changes the outside projection from a weighted assignment objective to a max-min allocation problem.

This gives a clean finite model for a broader warning in the line: a downstream scalarization can erase the compatibility structure that becomes decisive once every discriminator component must be protected uniformly.

## Prior art and novelty assessment

The surrounding optimization and complexity theory is classical.

- Nikhil Bansal and Maxim Sviridenko, **“The Santa Claus problem,”** *Proceedings of the 38th Annual ACM Symposium on Theory of Computing (STOC 2006)*, 31–40, DOI `10.1145/1132516.1132522`, formulate the max-min allocation objective as distributing indivisible presents with agent-dependent additive values to maximize the utility of the least fortunate agent.
- Arash Asadpour and Amin Saberi, **“An Approximation Algorithm for Max-Min Fair Allocation of Indivisible Goods,”** *SIAM Journal on Computing* 39(7), 2970–2989 (2010), DOI `10.1137/080723491`, is direct prior art for max-min fair allocation with indivisible goods and additive utilities.
- M. R. Garey and D. S. Johnson, **“Complexity Results for Multiprocessor Scheduling under Resource Constraints,”** *SIAM Journal on Computing* 4(4), 397–411 (1975), DOI `10.1137/0204035`, is the original complexity source associated with `3-PARTITION`; their later monograph *Computers and Intractability* (1979) gives the standard strongly NP-complete restricted formulation used above.
- Blackwell comparison, Le Cam deficiency, Shannon/Witsenhausen zero-error theory, and the average-TV projection context were already audited in AF-009, AF-011, AF-013, AF-046, and AF-047.

No novelty is claimed for max-min allocation, Santa Claus, `3-PARTITION`, fair-allocation hardness, total variation, or zero-error confusability.

A bounded literature audit did not locate the exact statement that the row-sup-TV metric projection of a finite channel onto the discriminator-relative zero-error support-faithful set is `1-R_\infty`, nor the resulting exact separation from AF-047 on identical-row channels. Absence from that audit is not evidence of novelty. The result is therefore classified conservatively as a derived structural synthesis: its value is the exact translation between repair geometry and a classical allocation problem, plus the proof that aggregation choice can expose or erase a discrete compatibility obstruction.

## Boundaries and failure modes

- The theorem is finite-alphabet. Countable or continuous outputs require measurable partitions, essential-support choices, and attainment arguments not supplied here.
- `|Y|\ge|A|` is necessary and sufficient for the zero-error faithful target set to be nonempty. When it fails, no finite repair distance to that empty set is defined in the present convention.
- The target is exact recovery of `d(X)`, not recovery of the full upstream state. Rows inside one discriminator class may remain mutually confusable.
- The repair may arbitrarily alter channel probabilities while preserving the fixed alphabets. If locality, symmetry, sparsity, a physical channel family, or another admissibility constraint is imposed, `1-R_\infty` is only a lower bound unless the explicit repaired channel remains admissible.
- The metric is row-sup total variation. The theorem is not a statement about prior-weighted TV, Le Cam deficiency, Wasserstein distance, KL divergence, or a topology that freezes support.
- The strong NP-completeness claim concerns variable finite alphabets/classes with rationally encoded probabilities. Fixed `m`, special support families, or divisible-output relaxations can have different complexity.
- Identical rows make the statistical discrimination problem maximally uninformative; they are used deliberately to isolate the global support-allocation obstruction. This does not say typical channels are hard for the same reason.
- The fractional allocation remark is an optimization comparison only. Splitting one output symbol among discriminator support cells would change the representation and is not a zero-error channel repair on the declared fixed alphabet.

## Decisive audit rule

For a finite stochastic compression whose downstream requirement is exact discriminator survival and whose repair cost is row-sup total variation:

1. partition the retained output alphabet into one nonempty support cell per discriminator class;
2. for each proposed cell allocation compute the retained mass of **every** upstream row in its class cell;
3. maximize the minimum retained row mass;
4. subtract that max-min value from `1` to obtain the exact distance to zero-error fidelity.

Do not substitute AF-047's Bayes-risk/Hall calculation when the scientific requirement is worst-case row protection. Average and row-sup aggregation can disagree structurally even when every channel row is identical.

## Consequence for the line

AF-047 showed that average structural repair contains a global Hall-coverage term beyond ordinary Bayes error. AF-048 shows that this is still not the end of the hierarchy: replacing average protection by uniform protection converts global coverage into a max-min allocation problem, and indivisibility can make the exact projection strongly NP-hard.

The broader lesson is not computational complexity for its own sake. It is a fidelity principle:

\[
\boxed{
\text{a compression audit must specify both what discriminator is to survive and how failure across its components is aggregated.}
}
\]

Without the second choice, a scalar fidelity score can silently average away the very global compatibility obstruction that the retained structure was supposed to preserve.