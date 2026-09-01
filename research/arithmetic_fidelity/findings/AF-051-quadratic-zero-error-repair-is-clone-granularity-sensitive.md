# AF-051 — Quadratic zero-error repair is partition-exact but clone-granularity sensitive

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite nonempty sets, let

\[
d:X\to D,
\qquad
A=d(X),
\qquad
m=|A|,
\]

and assume `|Y|\ge m`. Let `K:X\rightsquigarrow Y` be a stochastic channel and fix a strictly positive prior

\[
\pi_x>0,
\qquad
\sum_x\pi_x=1.
\]

Write `\mathcal Z_d^{(0)}` for AF-011's zero-error faithful set: channels whose rows belonging to distinct discriminator classes have disjoint output supports. Instead of the row-separable Csiszár `f`-divergences classified in AF-050, consider the prior-weighted quadratic/Brier repair cost

\[
\mathcal E_{2,\pi}(K,L)
=
\sum_{x\in X}\pi_x\|K_x-L_x\|_2^2.
\]

Then:

1. **Projection onto one prescribed support face has an exact Euclidean formula.** For every probability vector `P` on `Y` and every nonempty `S\subseteq Y`, put

   \[
   r=P(S^c),
   \qquad
   k=|S|.
   \]

   Then

   \[
   \boxed{
   \inf_{Q:\operatorname{supp}(Q)\subseteq S}
   \|P-Q\|_2^2
   =
   \sum_{y\notin S}P(y)^2+\frac{r^2}{k}.
   }
   \]

   The minimizer is unique and equals

   \[
   Q^*(y)
   =
   \begin{cases}
   P(y)+r/k,&y\in S,\\
   0,&y\notin S.
   \end{cases}
   \]

2. **Zero-error repair still reduces exactly to a class partition.** For a partition into nonempty cells

   \[
   Y=\bigsqcup_{a\in A}Y_a
   \]

   define

   \[
   r_x(Y_\bullet)
   =
   K_x\!\left(Y\setminus Y_{d(x)}\right).
   \]

   Then

   \[
   \boxed{
   \inf_{L\in\mathcal Z_d^{(0)}}
   \mathcal E_{2,\pi}(K,L)
   =
   \min_{Y=\bigsqcup_aY_a}
   \sum_x\pi_x
   \left[
   \sum_{y\notin Y_{d(x)}}K_x(y)^2
   +
   \frac{r_x(Y_\bullet)^2}{|Y_{d(x)}|}
   \right].
   }
   \]

   Thus changing from `f`-divergence geometry to quadratic Bregman geometry does **not** remove the partition combinatorics imposed by the zero-error target itself.

3. **AF-050's retained-mass sufficiency fails outside the `f`-divergence class.** The quadratic cell cost is not a function of the single scalar `P(S)`. It depends additionally on the concentration of the discarded coordinates through

   \[
   \sum_{y\notin S}P(y)^2
   \]

   and on the cardinality `|S|` of the retained support face. Consequently the AF-047 class-output aggregate

   \[
   q_a(y)
   =
   \sum_{x:d(x)=a}\pi_xK(y\mid x)
   \]

   is no longer sufficient to determine the minimum repair cost. There exist two channels with identical `q_a(y)` for every class and output but different exact quadratic distances to `\mathcal Z_d^{(0)}`.

4. **The extra geometry is representation-sensitive.** Let `C_k` be the statistically reversible uniform output-cloning map

   \[
   C_k:\Delta(Y)\to\Delta(Y\times\{1,\ldots,k\}),
   \qquad
   (C_kP)(y,j)=\frac{P(y)}{k}.
   \]

   Then for every pair of probability vectors,

   \[
   \boxed{
   \|C_kP-C_kQ\|_2^2
   =
   \frac1k\|P-Q\|_2^2.
   }
   \]

   Since `C_k` preserves zero-error disjointness,

   \[
   \boxed{
   \inf_{L'\in\mathcal Z_{d,k}^{(0)}}
   \mathcal E_{2,\pi}(C_kK,L')
   \le
   \frac1k
   \inf_{L\in\mathcal Z_d^{(0)}}
   \mathcal E_{2,\pi}(K,L),
   }
   \]

   where `\mathcal Z_{d,k}^{(0)}` is the zero-error set on the cloned output alphabet. Yet `K` and `C_kK` are Blackwell-equivalent experiments: cloning is a downstream randomization and deterministic merging of the clones recovers `K` exactly.

5. **The clone sensitivity can collapse a positive repair cost all the way to zero in the limit without changing the statistical experiment.** Take two discriminator classes with equal prior and identical channel rows

   \[
   K_0=K_1=\left(\frac12,\frac12\right).
   \]

   On the original two-output alphabet,

   \[
   \inf_{L\in\mathcal Z_d^{(0)}}\mathcal E_{2,\pi}(K,L)
   =
   \frac12.
   \]

   After cloning each output into `k` equiprobable copies, the exact optimum is

   \[
   \boxed{
   \inf_{L'\in\mathcal Z_{d,k}^{(0)}}
   \mathcal E_{2,\pi}(C_kK,L')
   =
   \frac{1}{2k}
   \longrightarrow0.
   }
   \]

   Thus the raw quadratic repair radius can be made arbitrarily small by a reversible refinement of output labels alone.

6. **Changing the divergence family creates a real but conditional escape from AF-050.** Quadratic/Brier repair genuinely escapes the universal binary retained-mass penalty of row-separable `f`-divergences, but the new degrees of freedom are partly tied to coordinate granularity. Therefore a richer repair cost is not automatically a more intrinsic fidelity notion. If output splitting, basis refinement, discretization, or another statistically sufficient presentation change is mathematically inessential, a quadratic fidelity margin must first be quotient-normalized or otherwise shown invariant under that equivalence before it can be interpreted as structural robustness.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{target geometry determines the partition constraint,}
\quad
\text{divergence geometry determines the local repair cost,}
\quad
\text{and presentation invariance determines whether that cost is intrinsic.}
}
\]

AF-050 shows that all row-separable Csiszár `f`-divergences share one binary support-penalty skeleton. The present result shows that leaving that family can alter the repair geometry, but also exposes a new falsification gate: **a fidelity margin that changes under a reversible refinement of the retained representation is a coordinate-dependent diagnostic unless that refinement is forbidden by intrinsic structure.**

## Derivation

### Euclidean projection onto a fixed simplex face

Fix a probability vector `P` and a nonempty cell `S`. Every probability vector `Q` supported on `S` satisfies

\[
\sum_{y\in S}Q(y)=1.
\]

For `y\in S`, write

\[
u_y=Q(y)-P(y).
\]

Since `P(S)=1-r`,

\[
\sum_{y\in S}u_y
=
1-P(S)
=
r.
\]

The squared Euclidean cost separates as

\[
\|P-Q\|_2^2
=
\sum_{y\notin S}P(y)^2
+
\sum_{y\in S}u_y^2.
\]

The first term is fixed. By Cauchy--Schwarz,

\[
\sum_{y\in S}u_y^2
\ge
\frac{\left(\sum_{y\in S}u_y\right)^2}{|S|}
=
\frac{r^2}{k},
\]

with equality if and only if

\[
u_y=\frac{r}{k}
\qquad
(y\in S).
\]

Because `r\ge0`, the equality candidate

\[
Q^*(y)=P(y)+r/k
\]

is nonnegative on `S`; it sums to one and is therefore admissible. Strict convexity of the Euclidean objective makes it the unique minimizer.

This is a particularly simple fixed-face specialization of the classical Euclidean projection problem on a probability simplex. The important structural point is visible directly in the formula: the loss is controlled by the **squared profile** of discarded mass plus a face-cardinality term, not by discarded mass alone.

### Every zero-error channel again induces a class partition

Take any

\[
L\in\mathcal Z_d^{(0)}.
\]

For each discriminator class `a`, define the union of supports used by that class,

\[
S_a
=
\bigcup_{x:d(x)=a}\operatorname{supp}(L_x).
\]

Every `S_a` is nonempty, and AF-011 gives

\[
S_a\cap S_b=\varnothing
\qquad
(a\ne b).
\]

Assign every output unused by `L` to an arbitrary discriminator class. This enlarges the support unions to a partition

\[
Y=\bigsqcup_{a\in A}Y_a,
\qquad
S_a\subseteq Y_a.
\]

For every row `x` of class `a`,

\[
\|K_x-L_x\|_2^2
\ge
\inf_{Q:\operatorname{supp}(Q)\subseteq S_a}
\|K_x-Q\|_2^2
\ge
\inf_{Q:\operatorname{supp}(Q)\subseteq Y_a}
\|K_x-Q\|_2^2.
\]

Applying the fixed-face formula and summing with `\pi_x` gives the partition lower bound.

Conversely, choose any partition `Y=\bigsqcup_aY_a` and replace each row `K_x` by its unique Euclidean projection onto the simplex face supported on `Y_{d(x)}`. Rows from different discriminator classes then have disjoint supports, so the projected channel lies in `\mathcal Z_d^{(0)}` and attains the displayed partition objective.

Hence the partition formula is exact.

This separates two logically different sources of structure:

\[
\text{zero-error target}
\Longrightarrow
\text{disjoint class cells},
\]

while

\[
\text{chosen divergence}
\Longrightarrow
\text{cost of projecting each row onto its cell}.
\]

The former survives the change from AF-050; the latter does not.

### Identical class-output mass does not determine quadratic repair

The collapse of AF-047's aggregate sufficiency can be seen on the smallest useful example.

Let

\[
X=\{x_1,x_2,x_3\},
\qquad
A=\{a,b\},
\qquad
d(x_1)=d(x_2)=a,
\qquad
d(x_3)=b,
\]

with

\[
\pi_{x_1}=\pi_{x_2}=\frac14,
\qquad
\pi_{x_3}=\frac12,
\]

and output alphabet

\[
Y=\{u,v\}.
\]

Define

\[
K^{\mathrm{spike}}_{x_1}=(1,0),
\qquad
K^{\mathrm{spike}}_{x_2}=(0,1),
\qquad
K^{\mathrm{spike}}_{x_3}=(0,1),
\]

whereas

\[
K^{\mathrm{mix}}_{x_1}
=
K^{\mathrm{mix}}_{x_2}
=
\left(\frac12,\frac12\right),
\qquad
K^{\mathrm{mix}}_{x_3}=(0,1).
\]

For both channels the class-output joint masses are exactly

\[
q_a(u)=q_a(v)=\frac14,
\qquad
q_b(u)=0,
\qquad
q_b(v)=\frac12.
\]

Thus AF-047's full matrix `(q_a(y))` is identical.

Because there are two classes and two outputs, a zero-error repair must assign one singleton output to each class. The optimal assignment gives class `a` the output `u` and class `b` the output `v`.

For `K^{\mathrm{spike}}`, only row `x_2` needs repair. Moving the point mass at `v` to the point mass at `u` has squared Euclidean cost

\[
\|(0,1)-(1,0)\|_2^2=2,
\]

so

\[
\boxed{
\inf_{L\in\mathcal Z_d^{(0)}}
\mathcal E_{2,\pi}(K^{\mathrm{spike}},L)
=
\frac14\cdot2
=
\frac12.
}
\]

For `K^{\mathrm{mix}}`, each class-`a` row projects from `(1/2,1/2)` to `(1,0)`, at cost

\[
\left(\frac12\right)^2+\left(\frac12\right)^2
=
\frac12.
\]

Together the two rows have total prior `1/2`, so

\[
\boxed{
\inf_{L\in\mathcal Z_d^{(0)}}
\mathcal E_{2,\pi}(K^{\mathrm{mix}},L)
=
\frac12\cdot\frac12
=
\frac14.
}
\]

The reverse singleton assignment costs `3/2` and `5/4` respectively, so these are the exact optima.

Therefore

\[
(q_a(y))\text{ identical}
\quad\not\Rightarrow\quad
\text{quadratic repair cost identical}.
\]

The difference is precisely the within-class row concentration that AF-047 legitimately forgets for total variation but Euclidean geometry retains.

### Uniform cloning is statistically reversible but contracts quadratic geometry

For an integer `k\ge1`, define the cloning channel

\[
C_k(y,j\mid y')
=
\begin{cases}
1/k,&y'=y,\\
0,&y'\ne y,
\end{cases}
\]

from `Y` to `Y\times\{1,\ldots,k\}`. At the level of row distributions,

\[
(C_kP)(y,j)=P(y)/k.
\]

Let `M_k` deterministically forget the clone index:

\[
M_k(y\mid(y',j))
=
1_{\{y=y'\}}.
\]

Then

\[
M_k\circ C_k=\operatorname{id}_{Y}.
\]

Consequently, for every upstream experiment `K`,

\[
C_k\circ K
\]

is a garbling of `K`, while `K=M_k\circ C_k\circ K` is a garbling of the cloned experiment. The two are Blackwell-equivalent: the clone index contains no information about the upstream state beyond the original output.

Nevertheless,

\[
\begin{aligned}
\|C_kP-C_kQ\|_2^2
&=
\sum_{y\in Y}\sum_{j=1}^k
\left(\frac{P(y)-Q(y)}{k}\right)^2\\
&=
\frac1k
\sum_y(P(y)-Q(y))^2\\
&=
\frac1k\|P-Q\|_2^2.
\end{aligned}
\]

If `L` is zero-error faithful on the original alphabet, then `C_kL` is zero-error faithful on the cloned alphabet because cloning cannot create overlap between two originally disjoint class supports. Hence

\[
\begin{aligned}
\inf_{L'\in\mathcal Z_{d,k}^{(0)}}
\mathcal E_{2,\pi}(C_kK,L')
&\le
\inf_{L\in\mathcal Z_d^{(0)}}
\mathcal E_{2,\pi}(C_kK,C_kL)\\
&=
\frac1k
\inf_{L\in\mathcal Z_d^{(0)}}
\mathcal E_{2,\pi}(K,L).
\end{aligned}
\]

This is already enough to show that quadratic distance to the zero-error set does not define an invariant robustness scale on Blackwell-equivalence classes of experiments.

### Exact clone-collapse family

The inequality above is sharp on a symmetric family.

Take

\[
X=A=\{0,1\},
\qquad
d(x)=x,
\qquad
\pi_0=\pi_1=\frac12,
\]

and let both rows of the original two-output channel be

\[
P=\left(\frac12,\frac12\right).
\]

On two outputs, every zero-error partition has two singleton cells. Each row is at squared Euclidean distance `1/2` from its assigned point mass, so

\[
\mathcal R_1
:=
\inf_{L\in\mathcal Z_d^{(0)}}\mathcal E_{2,\pi}(K,L)
=
\frac12.
\]

After `k`-fold uniform cloning of each original output, every row is uniform on `2k` outputs:

\[
P_k(j)=\frac1{2k}.
\]

A two-class zero-error partition is determined, up to labels, by the size

\[
s\in\{1,\ldots,2k-1\}
\]

of the first class cell. The fixed-face formula gives the first row cost

\[
c_k(s)
=
\frac{2k-s}{2ks},
\]

and the second row cost

\[
c_k(2k-s)
=
\frac{s}{2k(2k-s)}.
\]

Therefore the prior-weighted repair cost is

\[
\mathcal R_k(s)
=
\frac1{4k}
\left(
\frac{2k-s}{s}
+
\frac{s}{2k-s}
\right).
\]

For positive `a`, `a+a^{-1}\ge2`, with equality only at `a=1`. Taking

\[
a=\frac{2k-s}{s}
\]

shows that the minimum occurs at `s=k` and equals

\[
\boxed{
\mathcal R_k
=
\frac1{2k}.
}
\]

Thus

\[
\boxed{
K
\sim_{\mathrm{Blackwell}}
C_kK
\quad\text{for every }k,
\qquad
\mathcal R_k=\frac1{2k}\to0.
}
\]

The underlying experiment has not become closer to zero-error in any statistical-information sense; only the Euclidean coordinate presentation has been refined.

## Relationship to AF-047 and AF-050

AF-047 showed that total-variation repair of zero-error fidelity depends only on the class-output joint mass matrix and decomposes as Bayes error plus a Hall-coverage penalty. AF-050 then showed that every prior-weighted row-separable Csiszár `f`-divergence uses the same class-partition combinatorics and reduces each row/cell interaction to a scalar penalty depending only on retained mass.

The present result identifies exactly what happens when one crosses that family boundary.

The **partition survives** because it belongs to the zero-error target `\mathcal Z_d^{(0)}`. No choice of rowwise discrepancy can avoid the fact that different discriminator classes must occupy disjoint output cells.

The **binary retained-mass reduction fails** because Euclidean/Bregman geometry is coordinate-sensitive. The cost sees how omitted probability is distributed and how many coordinates remain available to absorb it.

The **new detail is not automatically structural information**. Uniformly cloning output symbols changes neither the Blackwell experiment nor the recoverability of the discriminator, but it changes the quadratic repair scale and can drive it to zero. Thus escaping the `f`-divergence taxonomy is mathematically real but does not by itself produce a more canonical fidelity notion.

This supplies a second gate after AF-050:

\[
\boxed{
\text{after changing the divergence family, audit invariance under the natural equivalences of the destination category.}
}
\]

A metric can be perfectly useful computationally while failing that structural gate.

## Prior art and novelty assessment

No novelty is claimed for Euclidean projection onto a simplex, the quadratic/Brier score, Bregman divergences, Blackwell sufficiency, or the fact that general Bregman distances need not obey a universal data-processing inequality.

Christian Michelot's 1986 paper *A finite algorithm for finding the projection of a point onto the canonical simplex of R^n* gives classical Euclidean-simplex projection prior art. The fixed-support-face formula above is an elementary special case in which the active coordinates are prescribed in advance.

Tilmann Gneiting and Adrian Raftery's 2007 paper *Strictly Proper Scoring Rules, Prediction, and Estimation* (JASA 102(477), 359--378, DOI `10.1198/016214506000001437`) places the quadratic/Brier score in the classical proper-scoring-rule framework. The expected excess quadratic score is the squared Euclidean discrepancy between categorical probability vectors, so the repair cost used here has an established statistical interpretation.

Wolfgang Stummer and Igor Vajda's *On Bregman Distances and Divergences of Probability Measures* (IEEE Transactions on Information Theory 58(3), 1277--1288, 2012, DOI `10.1109/TIT.2011.2178139`) is the decisive prior-art boundary for the information-processing issue. They establish an information-processing statement for scaled Bregman distances in a sufficiency/invariance sense rather than universal monotonicity, and explicitly exhibit coding situations in which a classical Bregman distance can increase. Thus representation sensitivity of Bregman geometry is classical and must not be presented as a new phenomenon.

Peter Harremoës' *Divergence and Sufficiency for Convex Optimization* (Entropy 19(5), 206, 2017, DOI `10.3390/e19050206`) gives a neighboring rigidity perspective: under its stated convex-optimization hypotheses, imposing sufficiency/locality/monotonicity strongly restricts Bregman regret and selects information-divergence structure. It reinforces the methodological boundary that a convenient convex repair loss and an information-monotone structural divergence are different requirements.

The derived contribution here is narrower and specific to the Arithmetic Fidelity program:

- the exact prescribed-face quadratic projection is inserted into AF-011's zero-error support geometry;
- the resulting global repair is proved to retain the same partition skeleton while losing AF-050's retained-mass sufficiency;
- an exact matched pair shows that AF-047's class-output aggregate ceases to determine repair;
- a reversible output-cloning family shows that the resulting repair radius can collapse to zero inside one Blackwell-equivalence class.

The point is therefore not a new divergence theorem. It is a **category audit**: richer local repair geometry can be purchased by becoming sensitive to distinctions that the destination category itself regards as inessential.

## Boundaries and failure modes

- The result is finite-dimensional. For countable or continuous output spaces, squared density distances depend on a dominating/reference measure and the same representation issue becomes more severe rather than automatically disappearing.
- The cost `\mathcal E_{2,\pi}` is a squared Hilbert/Brier discrepancy, not itself a metric because the square removes the triangle inequality. Its square root is a metric on the fixed finite row-coordinate space; under uniform cloning that metric contracts by `k^{-1/2}` instead of `k^{-1}`.
- The clone objection applies only when clone refinement is mathematically inessential. If the individual output atoms carry independently fixed physical, geometric, arithmetic, or measure-theoretic meaning, merging them may not be an admissible equivalence and Euclidean geometry may be appropriate.
- Blackwell equivalence is an information-theoretic equivalence of experiments, not a universal notion of sameness for every Mathia line. The correct invariance group/category must be declared by the application.
- The global partition formula assumes `|Y|\ge|A|`. If there are fewer outputs than discriminator classes, the zero-error target is empty, exactly as in AF-047/AF-050.
- The same class-output aggregate counterexample does not say that within-class row information is irrelevant in general. It says specifically that total variation can quotient it out for the AF-047 repair objective whereas quadratic repair cannot.
- The cloning theorem gives an upper bound for an arbitrary channel because the refined zero-error set may contain repairs that do not descend to the original alphabet. The symmetric example separately proves exact `1/k` decay, so the non-invariance conclusion does not depend on that possible slack.
- General Bregman divergences need not behave exactly like squared Euclidean distance. The finding classifies the quadratic member and uses prior art only to mark the broader absence of automatic data-processing naturality; it does not claim one formula for every Bregman generator.
- No claim is made that `f`-divergence repair is automatically invariant under every enlargement of the *repair target* caused by output refinement. The contrast used here is only that pairwise `f`-divergence has the classical data-processing/sufficiency structure that raw Euclidean coordinate distance lacks.
- No RH-specific consequence follows merely from this repair taxonomy. An arithmetic application must first justify why stochastic-channel repair and its output equivalences model the actual compression under study.

## Decisive audit test for non-`f` repair geometries

When a proposed fidelity margin leaves the AF-050 `f`-divergence class:

1. derive the exact projection onto one admissible target fiber/face rather than infer its behavior from analogy;
2. separate combinatorics forced by the target property from geometry introduced by the chosen loss;
3. test whether coarse retained summaries that were sufficient before remain sufficient;
4. identify the natural equivalences of the retained representation -- relabeling, refinement/merging, sufficient statistics, gauge, basis change, or another category-specific notion;
5. compute whether the repair value is invariant, monotone in the intended direction, or arbitrarily rescalable inside one equivalence class;
6. if it is presentation-sensitive, treat it as an algorithmic/coordinate diagnostic unless the application independently fixes that presentation;
7. only after this invariance audit interpret a positive repair radius as structural robustness.

For finite stochastic experiments, uniform output cloning is a particularly cheap falsifier because it preserves Blackwell information exactly while exposing coordinate-count dependence immediately.

## Consequence for the line

AF-050 closed one natural search loop: varying the generator inside row-separable Csiszár `f`-divergences cannot alter zero-error partition geometry and changes only the scalar retained-mass penalty.

AF-051 shows that leaving the family can indeed reveal additional geometric structure, so AF-050 is not a universal theorem about all repair losses. But the first explicit escape also demonstrates why **destination-category invariance has to be part of Arithmetic Fidelity's notion of a meaningful robustness margin**.

The line should therefore distinguish three layers whenever it studies distance to a fidelity boundary:

\[
\text{fidelity target}
\quad\Rightarrow\quad
\text{collision/fiber/support constraint},
\]

\[
\text{repair geometry}
\quad\Rightarrow\quad
\text{cost of moving into that target},
\]

and

\[
\text{destination equivalence}
\quad\Rightarrow\quad
\text{which parts of that cost are intrinsic rather than presentation artifacts}.
\]

This is directly relevant to the broader program of robust fidelity as distance to collision. A distance-to-loss formula is only as canonical as the topology and presentation on which the distance is measured. For arithmetic, spectral, or operator applications, a positive margin should not be treated as evidence that a prime-specific discriminator robustly survives compression until the margin is shown stable under the harmless equivalences of the exact destination category.
