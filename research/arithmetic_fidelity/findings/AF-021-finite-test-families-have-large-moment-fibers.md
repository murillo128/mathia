# AF-021 — Finite test families have arbitrarily large moment fibers

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` be a set, let

\[
\mathcal F=(f_1,\ldots,f_d),\qquad f_i:X\to\mathbb R,
\]

be a finite family of real-valued observables, and define the evaluation map

\[
\Phi:X\to\mathbb R^d,
\qquad
\Phi(x)=(f_1(x),\ldots,f_d(x)).
\]

For a finitely supported probability measure `\mu` on `X`, retain only the exact test vector

\[
M_{\mathcal F}(\mu)
=
\left(\int f_1\,d\mu,\ldots,\int f_d\,d\mu\right)
=
\int \Phi\,d\mu.
\]

Then finite-dimensional linear testing has a sharp convex-geometric fidelity boundary.

1. **Exact recovery of arbitrary probability measures is equivalent to affine independence of the evaluation family.** The map `M_\mathcal F` is injective on all finitely supported probability measures on `X` if and only if the indexed family
   \[
   \{\Phi(x):x\in X\}
   \]
   is affinely independent. Consequently, exact recovery is impossible whenever `X` has more than `d+1` points.

2. **Every `d+2` source points already force a same-destination pair.** Given any `d+2` distinct points of `X`, there exist two distinct probability measures supported on disjoint subsets of those points such that
   \[
   \boxed{M_\mathcal F(\mu)=M_\mathcal F(\nu).}
   \]
   This is the measure-theoretic form of Radon's theorem, or equivalently of elementary affine dependence in `\mathbb R^d`.

3. **The ambiguity can be arbitrarily large, not merely binary.** For every integer `r\ge2`, if `X` contains at least
   \[
   N=(d+1)(r-1)+1
   \]
   distinct points, then there exist `r` pairwise mutually singular finitely supported probability measures
   \[
   \mu_1,\ldots,\mu_r
   \]
   with one common exact test vector:
   \[
   \boxed{
   M_\mathcal F(\mu_1)=\cdots=M_\mathcal F(\mu_r).
   }
   \]
   This follows directly from Tverberg's theorem applied to the evaluation vectors.

4. More sharply, if the affine hull of `\Phi(X)` has dimension `k\le d`, replace `d` by `k` in the bounds above. Thus redundant observables do not buy fidelity merely by increasing the nominal number of coordinates.

5. Therefore a finite test family can be fully faithful only after **source-side structural restrictions** shrink the admissible measure class enough to make representations identifiable. Infinite numerical precision in finitely many test values does not defeat this obstruction for the unrestricted positive-measure class.

This supplies the missing resolution axis left open by AF-020. A complete test family on `(0,A)` can determine the entire retained measure below the support horizon, but replacing that infinite family by a fixed finite-dimensional test space creates an additional within-horizon ambiguity. Support radius controls **which scales can be seen**; test-space dimension controls **how finely arbitrary positive mass inside the visible scale can be resolved**.

The theorem does **not** yet imply that finitely many Weil tests fail on the much narrower family of prime-power measures `\omega_Q`. Tverberg's witnesses are arbitrary positive atomic measures. An arithmetic no-go requires either realizing such collisions inside the constrained image `Q\mapsto\omega_Q` or proving a different collision theorem for that image.

## Exact recovery is affine independence

Suppose first that the indexed evaluation family is affinely independent. Let

\[
\mu=\sum_{x\in S}a_x\delta_x,
\qquad
\nu=\sum_{x\in T}b_x\delta_x
\]

be finitely supported probability measures with equal test vectors. Extending the coefficients by zero to the finite set `S\cup T`, equality of total mass and test values gives

\[
\sum_x(a_x-b_x)=0,
\qquad
\sum_x(a_x-b_x)\Phi(x)=0.
\]

Affine independence forces every coefficient `a_x-b_x` to vanish, so `\mu=\nu`.

Conversely, if the indexed evaluation family is affinely dependent, there are finitely many distinct source points `x_1,\ldots,x_n` and real coefficients, not all zero, such that

\[
\sum_{i=1}^n c_i=0,
\qquad
\sum_{i=1}^n c_i\Phi(x_i)=0.
\]

Because the coefficients sum to zero and are not all zero, both positive and negative coefficients occur. Put

\[
I_+=\{i:c_i>0\},
\qquad
I_-=\{i:c_i<0\},
\]

and

\[
C=\sum_{i\in I_+}c_i
=-\sum_{i\in I_-}c_i>0.
\]

Define

\[
\mu
=\frac1C\sum_{i\in I_+}c_i\delta_{x_i},
\qquad
\nu
=\frac1C\sum_{i\in I_-}(-c_i)\delta_{x_i}.
\]

These are probability measures with disjoint supports, and the affine relation gives

\[
M_\mathcal F(\mu)=M_\mathcal F(\nu).
\]

Hence

\[
\boxed{
M_\mathcal F\text{ injective on finitely supported probabilities}
\iff
\{\Phi(x)\}_{x\in X}\text{ is affinely independent}.
}
\]

An affinely independent family in `\mathbb R^d` has at most `d+1` members. Thus no choice of `d` exact real linear tests can encode every probability measure on a source set with more than `d+1` states.

This conclusion is stronger than a dimension-counting heuristic: it gives explicit positive normalized witnesses with disjoint supports, so the loss cannot be blamed on signed cancellation, finite precision, or numerical instability.

## Radon gives the minimal pairwise obstruction

Take any `d+2` distinct source points. Their evaluation vectors lie in `\mathbb R^d`, so Radon's theorem partitions the indexed points into two nonempty groups whose convex hulls intersect.

Let `y` lie in that intersection. There are convex coefficients on the two groups such that

\[
y
=\sum_{i\in I_+}a_i\Phi(x_i)
=\sum_{j\in I_-}b_j\Phi(x_j),
\]

with

\[
a_i,b_j\ge0,
\qquad
\sum_i a_i=\sum_j b_j=1.
\]

The associated probability measures

\[
\mu=\sum_{i\in I_+}a_i\delta_{x_i},
\qquad
\nu=\sum_{j\in I_-}b_j\delta_{x_j}
\]

have disjoint supports and identical `\mathcal F`-moments.

For this application, Radon's theorem is equivalent to the affine-dependence proof above. Its value is conceptual: finite moment compression maps the probability simplex to the convex hull of the evaluation image, and nonunique convex representations are exactly same-destination measure fibers.

If `\Phi(X)` lies in an affine subspace of dimension `k<d`, the same argument needs only `k+2` source points. The effective fidelity dimension is therefore the affine dimension of the observable image, not the raw number of listed tests.

## Tverberg makes the fiber multiplicity unbounded

Radon's theorem provides two disjoint representing measures. Tverberg's 1966 theorem strengthens this substantially.

For `r\ge2`, Tverberg states that any

\[
(d+1)(r-1)+1
\]

points in `\mathbb R^d` can be partitioned into `r` nonempty blocks whose convex hulls have a common point.

Choose that many distinct source points `x_i` and apply the theorem to `\Phi(x_i)`. Let `I_1,\ldots,I_r` be the resulting disjoint blocks and let

\[
y\in\bigcap_{j=1}^r
\operatorname{conv}\{\Phi(x_i):i\in I_j\}.
\]

For each block choose barycentric coefficients representing `y` and form a probability measure `\mu_j` supported on that block. Then

\[
M_\mathcal F(\mu_j)=y
\qquad(1\le j\le r).
\]

Since the original blocks are disjoint, the resulting measures are pairwise mutually singular. Zero barycentric coefficients, if any, only shrink individual supports and do not destroy disjointness.

Thus a finite-dimensional moment fiber can contain arbitrarily many pairwise mutually singular positive normalized representatives whenever the source supplies enough points. In particular, if `X` is infinite, then for every `r` there is some fiber of `M_\mathcal F` containing `r` mutually singular finitely supported probability measures.

Again the effective affine dimension `k=\dim\operatorname{aff}\Phi(X)` can replace `d`, giving the sharper threshold

\[
(k+1)(r-1)+1.
\]

## Relation to truncated moment theory

This phenomenon belongs to classical truncated-moment and convex-geometry mathematics, not to a new Arithmetic Fidelity theory invented from scratch.

For a finite function family

\[
\mathsf A=\{a_1,\ldots,a_m\},
\]

the vector

\[
\left(\int a_1\,d\mu,\ldots,\int a_m\,d\mu\right)
\]

is precisely a truncated moment sequence, and the collection of all such vectors forms the moment cone. Modern treatments such as di Dio--Schmüdgen analyze this convex set and its atomic representing measures; Richter-type results show that finite moment data admit sparse atomic representatives.

AF-021 asks the complementary fidelity question: when is the representing measure unique for **every** possible moment vector? For unrestricted probability measures, the affine-independence criterion above answers exactly. Once more than `d+1` source states are admissible, the finite test map necessarily has nontrivial fibers, and Tverberg shows that those fibers can support many mutually singular representatives.

No novelty is claimed for Radon's theorem, Tverberg's theorem, affine dependence, or the general truncated-moment framework. The Arithmetic Fidelity contribution is the placement of these classical results as a complete no-go audit for finite linear test compression of unrestricted positive measures.

## Relation to AF-002 and AF-020

AF-002 treated a different finite-observable problem: a deterministic source point is observed through a fixed library of coordinates, and a target discriminator is recoverable exactly when the selected observables hit every unresolved conflict pair. That is rough-set discernibility / reduct theory.

Here the source object is itself a **probability measure** and the observables are integrated linearly. Convex mixing creates new collisions even when the pointwise evaluation map `\Phi` separates every individual source point. Pointwise injectivity therefore does not suffice. The needed condition for unrestricted measure recovery is the much stronger affine independence of the entire evaluation family.

AF-020, meanwhile, used the complete distributional test family `C_c^\infty(0,A)` and proved that it determines the whole prime-power measure below the arithmetic horizon `e^A`. AF-021 isolates what changes when that complete family is compressed to finitely many linear functionals:

\[
\boxed{
\text{full test family}
\quad\rightsquigarrow\quad
\text{measure on visible support}
}
\]

whereas

\[
\boxed{
\text{finite test family}
\quad\rightsquigarrow\quad
\text{a finite-dimensional moment vector with convex fibers}.
}
\]

The two losses are logically independent. Restricting support can erase distant mass even with an infinite separating family; restricting test dimension can merge different mass configurations entirely inside a fixed visible support.

This yields a two-parameter audit for test-function arguments:

\[
\text{scale coverage}
\quad+\quad
\text{within-scale resolution}.
\]

Neither parameter should be inferred from the other.

## Arithmetic boundary

For the Weil prime-power measure of AF-020,

\[
\omega_Q
=
\sum_j\sum_{m\ge1}
\ell_j e^{-m\ell_j/2}\delta_{m\ell_j},
\qquad \ell_j=\log q_j,
\]

the weights and locations are not free. They are tied together by one underlying generator multiset and all of its positive integer multiples.

Therefore the generic Tverberg witnesses above need not be realizable as two measures of the form `\omega_Q` and `\omega_R`. It would be invalid to conclude merely from AF-021 that any finite collection of explicit-formula tests admits a changed-prime-system control with exactly the same values.

The correct next question is an **identifiability problem on the constrained model class**:

\[
Q
\longmapsto
\bigl(W_Q(F_1),\ldots,W_Q(F_d)\bigr).
\]

Finite-dimensional tests are globally non-faithful on the ambient cone of positive measures, but a restricted nonlinear family can in principle remain injective. Classical sparse moment reconstruction already gives positive examples of finite measurements recovering sufficiently constrained atomic models under suitable assumptions.

Accordingly, a prime-specific no-go must establish a collision **inside** the admissible generalized-prime/control family at the same retained layer. Conversely, a claimed finite-test recovery theorem must state the structural restriction that defeats the ambient Tverberg obstruction rather than appealing to the precision of the measured real numbers.

## Prior art and novelty assessment

The core ingredients are classical.

- Johann Radon, **“Mengen konvexer Körper, die einen gemeinsamen Punkt enthalten,”** *Mathematische Annalen* 83 (1921), 113--115, DOI `10.1007/BF01464231`, is the original convex-partition theorem giving the two-block intersection result.
- Helge Tverberg, **“A Generalization of Radon's Theorem,”** *Journal of the London Mathematical Society* s1-41 (1966), 123--128, DOI `10.1112/jlms/s1-41.1.123`, gives the `r`-block generalization used to build arbitrarily large mutually singular same-moment families.
- Philipp J. di Dio and Konrad Schmüdgen, **“The multidimensional truncated moment problem: The moment cone,”** *Journal of Mathematical Analysis and Applications* 511(1) (2022), 126066, DOI `10.1016/j.jmaa.2022.126066`, provides a modern general finite-function-family moment-cone framework and places atomic representing measures and Carathéodory/Richter-type bounds in the established truncated-moment literature.

The pairwise collision proof could be presented without citing Radon because it is elementary affine dependence. Tverberg supplies the stronger multiplicity statement. No novelty is claimed for either theorem or for the truncated moment problem.

The reusable Arithmetic Fidelity result is the exact interpretation: **finite linear test compression of an unrestricted positive-measure source is faithful exactly on an affinely independent evaluation family, and otherwise its fibers contain disjoint positive witnesses; on infinite sources the same finite test map has fibers of unbounded mutually singular multiplicity.**

## Boundaries and failure modes

- The theorem concerns finitely supported **probability measures**. This is already enough to disprove injectivity on any larger measure class containing them.
- The observables are real-valued. A family of `d` complex-valued tests can be treated as at most `2d` real coordinates; sharper bounds use the real affine dimension of its evaluation image.
- Exact knowledge of total mass is built in by using probability measures. For arbitrary finite positive measures, include the constant observable `1` when mass is part of the retained data.
- The `d+2` and Tverberg thresholds are universal sufficient bounds, not claims that every smaller configuration is identifiable. The sharp local parameter is the affine dependence structure of the actual evaluation vectors.
- If `X` is finite with at most `d+1` points and their indexed evaluation vectors are affinely independent, the finite moment map is exactly injective. Thus finite-dimensional testing is not intrinsically lossy on every restricted source class.
- Pointwise injectivity of `\Phi` is insufficient once convex mixtures are admissible. Distinct source points may all be separated while their convex combinations collide.
- Tverberg witnesses are arbitrary atomic measures. They do not automatically satisfy prime-power multiplicative constraints, equal fixed weights, spectral admissibility, positivity-kernel constraints beyond ordinary measure positivity, or another nonlinear model restriction.
- Approximate/noisy recovery, stability, sample complexity, entropy, and numerical conditioning are separate questions. AF-021 is an exact zero-error fidelity statement.
- Nonlinear observables of the unknown measure can evade a theorem whose hypothesis is a finite family of linear test integrals. The actual destination map must be audited rather than relabeled as a moment vector.
- This result has no implication for RH or for the location of zeta zeros.

## Decisive audit test

For any argument that compresses a positive distribution, spectral measure, prime-power measure, or related object to finitely many test-function evaluations:

1. state the admissible source class and the exact linear tests;
2. compute the real affine dimension of the evaluation image rather than only counting test coordinates;
3. first test the ambient positive-measure class with the affine-independence / Radon / Tverberg obstruction;
4. if the intended source class is narrower, identify the exact nonlinear constraints that exclude those ambient same-moment witnesses;
5. either construct two admissible source objects with identical test vector or prove injectivity on the constrained image;
6. if support is also restricted, audit support horizon and finite-test resolution separately;
7. for an arithmetic claim, require the collision or recovery theorem inside a matched rational-prime/generalized-prime control class before drawing a prime-specific conclusion.

A generic ambient Tverberg collision is a decisive no-go for unrestricted measure recovery, but only a warning for a structured source class. The remaining burden is always identifiability of the actual admissible image.

## Consequence for the line

Add **moment-test dimension** as a fidelity axis distinct from support scale.

For measure-valued carriers, the audit should now distinguish:

\[
\text{source constraints}
\longrightarrow
\text{support window}
\longrightarrow
\text{test family}
\longrightarrow
\text{moment vector}.
\]

The full distributional test family can be faithful on a visible region, while every fixed finite-dimensional subfamily has large fibers on the ambient probability cone. Any finite-test recovery claim therefore lives or dies on the source constraints that cut across those convex fibers.

For the arithmetic program, the next nontrivial step is not another generic moment theorem. It is to determine whether natural finite families arising in explicit-formula, positivity, or trace arguments are injective or non-injective on the **structured prime-power/generalized-prime model class itself**.