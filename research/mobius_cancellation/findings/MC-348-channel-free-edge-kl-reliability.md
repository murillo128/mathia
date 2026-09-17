# MC-348 — Channel-free source-edge KL controls joint-transcript reliability

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-347` makes the reliability budget invariant under the fidelity of a **raw-coordinate query**, but it still assumes that every acquisition event selects one source coordinate and observes a channel depending only on that bit. A genuinely joint transcript can mix many source coordinates in one observation, so nominal query count and the raw-coordinate acquisition model are not intrinsic.

The intrinsic reliability currency is instead the collection of pairwise transcript divergences along the natural neighboring-state graph of the reciprocal source law.

Keep the reciprocal source vector

\[
X=(X_1,\ldots,X_R)
\]

from `MC-340`. For each admissible source state `x`, let `P_x` denote the law of the **complete admitted transcript** `Y`. No factorization, sequential query structure, coordinate selection rule, finite alphabet, or observation dimension is assumed. Let `\widehat X(Y)` be any estimator and write

\[
\bar p
:=\frac1R\mathbf E\,d_H(\widehat X,X).
\tag{1}
\]

For two source states `x,x'`, define the symmetrized transcript divergence

\[
b(x,x')
:=\frac12\left(
D(P_x\|P_{x'})+D(P_{x'}\|P_x)
\right),
\tag{2}
\]

with the convention that an infinite divergence makes the lower bounds below automatic.

Put

\[
\Lambda_k:=\frac{2^k-2}{2^k-1}.
\tag{3}
\]

### Even rank

For even `R`, the source vector is uniform on

\[
S=\{-1,+1\}^R\setminus\{\mathbf1\},
\qquad m=2^R-1.
\]

Let `E_1` be the surviving Hamming-cube edges in `S`, so an edge joins states differing in exactly one coordinate. Define the source-averaged edge reliability expenditure

\[
\mathfrak J_1
:=\frac{2}{m}\sum_{e\in E_1} b_e.
\tag{4}
\]

Then every transcript channel and every decoder satisfy

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R}{4}
\exp\!\left(
-\frac{\mathfrak J_1}{\Lambda_R R}
\right).
}
\tag{5}
\]

Equivalently,

\[
\boxed{
\mathfrak J_1
\ge
\Lambda_R R
\left[
\log\frac{\Lambda_R}{4\bar p}
\right]_+.
}
\tag{6}
\]

### Odd rank

For odd `R>=3`, condition on the event `E_0` that `X` is not the all-`+1` word. As in `MC-340` and `MC-347`,

\[
\mathbf P(E_0)=\Lambda_R,
\]

and conditioned on `E_0` the source is uniform on the even-parity cube with the all-`+1` vertex removed. Its size is

\[
M=2^{R-1}-1.
\]

Let `E_2` be the surviving graph whose edges join states differing in two coordinates. Define the unconditional-normalized pair-edge expenditure

\[
\mathfrak J_2
:=
\frac{2\Lambda_R}{M(R-1)}
\sum_{e\in E_2}b_e.
\tag{7}
\]

Then

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R\Lambda_{R-1}}{4}
\exp\!\left(
-\frac{2\mathfrak J_2}
{\Lambda_R\Lambda_{R-1}R}
\right),
}
\tag{8}
\]

and therefore

\[
\boxed{
\mathfrak J_2
\ge
\frac{\Lambda_R\Lambda_{R-1}R}{2}
\left[
\log\frac{\Lambda_R\Lambda_{R-1}}{4\bar p}
\right]_+.
}
\tag{9}
\]

Thus, in either parity,

\[
\boxed{
\bar p\to0
\quad\Longrightarrow\quad
\mathfrak J=\Omega\!\left(R\log\frac1{\bar p}\right),
}
\tag{10}
\]

where `\mathfrak J` is the appropriate source-edge divergence budget.

This removes the acquisition-model restriction left by `MC-347`: **a joint observation may encode many source coordinates at once, but vanishing reconstruction error still requires logarithmically growing discrimination along the source graph.** The theorem charges the complete transcript itself, not the number or syntax of observations used to produce it.

At the matched-filter endpoint of `MC-340`, coefficient energy `\mathcal E(W)\le1` and dephasing error `\delta(W)\le\varepsilon` admit a coordinatewise Bayes decoder with average Hamming error at most

\[
\alpha_\varepsilon
:=\varepsilon-\frac{\varepsilon^2}{2}.
\tag{11}
\]

Therefore `(6)` or `(9)` applies with `\bar p\le\alpha_\varepsilon`. In particular, any arbitrary joint transcript that drives `\varepsilon_R\to0` must pay

\[
\mathfrak J=\Omega\!\left(R\log\frac1{\varepsilon_R}\right).
\tag{12}
\]

No estimate for `M(x)` follows. The result is an intrinsic finite-source admission theorem for the reciprocal endpoint.

## 1. One neighboring-source test already prices one bit of reliability

For a coordinate `i`, write

\[
e_i(x):=P_x(\widehat X_i\ne x_i).
\]

Suppose `x,x'` are admissible neighboring source states and differ in coordinate `i`. Applying the Bretagnolle--Huber testing inequality to the decision event for coordinate `i` gives

\[
e_i(x)+e_i(x')
\ge
\frac12 e^{-D(P_x\|P_{x'})}.
\tag{13}
\]

The reversed pair gives the same left-hand side with `D(P_{x'}\|P_x)`. Since the smaller directional divergence is no larger than their average,

\[
\boxed{
e_i(x)+e_i(x')
\ge
\frac12 e^{-b(x,x')}.
}
\tag{14}
\]

Nothing in this step knows how the transcript was generated. `Y` may be scalar, vector-valued, continuous, adaptive, interactive, or a one-shot joint statistic of the entire source vector.

Equation `(14)` is the only statistical ingredient needed below; the rest is exact source-graph counting.

## 2. Even rank: the punctured cube yields the exact edge budget

The full `R`-cube has `R2^{R-1}` undirected edges. Removing the all-`+1` source state deletes exactly `R` of them, hence

\[
|E_1|
=R(2^{R-1}-1)
=\frac{mR\Lambda_R}{2}.
\tag{15}
\]

Summing `(14)` over all surviving edges gives

\[
mR\bar p
\ge
\frac12\sum_{e\in E_1}e^{-b_e}.
\tag{16}
\]

The inequality rather than equality on the left is deliberate: coordinate errors corresponding to the deleted neighbor are still counted in `mR\bar p` but do not belong to a surviving edge.

By Jensen,

\[
\sum_{e\in E_1}e^{-b_e}
\ge
|E_1|
\exp\!\left(
-\frac1{|E_1|}\sum_{e\in E_1}b_e
\right).
\tag{17}
\]

From `(4)` and `(15)`,

\[
\frac1{|E_1|}\sum_{e\in E_1}b_e
=
\frac{\mathfrak J_1}{\Lambda_RR}.
\tag{18}
\]

Substitution in `(16)` proves `(5)`, and rearrangement proves `(6)`.

The logarithmic tariff is therefore a graph-level fact. A channel can concentrate all of its discrimination on some edges, but convexity makes poor discrimination on the remaining edges visible in average Hamming risk.

## 3. Odd rank: parity-preserving pair flips give the same scale

Condition on `E_0`. The even-parity cube has `2^{R-1}` vertices and degree `\binom R2` under pair flips. Removing the all-`+1` vertex gives

\[
|E_2|
=
\frac{M\Lambda_{R-1}}2\binom R2.
\tag{19}
\]

If a pair edge differs in coordinates `i,j`, applying `(14)` once to `i` and once to `j` yields

\[
e_i(x)+e_i(x')+e_j(x)+e_j(x')
\ge e^{-b_e}.
\tag{20}
\]

Each coordinate error can occur in at most `R-1` pair-flip edges. If `\bar p_0` is the conditional average Hamming risk, then

\[
(R-1)MR\bar p_0
\ge
\sum_{e\in E_2}e^{-b_e}.
\tag{21}
\]

Jensen, `(19)`, and the definition `(7)` give

\[
\bar p_0
\ge
\frac{\Lambda_{R-1}}4
\exp\!\left(
-\frac{2\mathfrak J_2}
{\Lambda_R\Lambda_{R-1}R}
\right).
\tag{22}
\]

Since the unconditional risk obeys `\bar p\ge\Lambda_R\bar p_0`, equation `(8)` follows, and `(9)` is its inversion.

As in `MC-347`, the odd-rank constants are not claimed sharp. Pair flips are chosen because they preserve the exact parity relation of the source law. The durable statement is the `R log(1/error)` reliability scale under a source-intrinsic neighboring-state graph.

## 4. MC-347 becomes an acquisition-specific corollary

The raw-query model of `MC-347` assigns each acquisition event to one source coordinate and defines its accumulated directional discrimination divergence

\[
\mathfrak D
=
\mathbf E\sum_{t\le\tau}
D\!\left(
K_t(\cdot\mid X_{J_t})
\middle\|
K_t(\cdot\mid -X_{J_t})
\right).
\]

Its adaptive change-of-measure calculation proves, for even rank,

\[
\sum_{e\in E_1}b_e
\le\frac m2\mathfrak D,
\]

hence

\[
\mathfrak J_1\le\mathfrak D.
\tag{23}
\]

For odd rank, writing `\mathfrak D_0` for the conditional expenditure on `E_0`, the same calculation gives

\[
\sum_{e\in E_2}b_e
\le\frac{M(R-1)}2\mathfrak D_0,
\]

so

\[
\mathfrak J_2
\le\Lambda_R\mathfrak D_0
\le\mathfrak D.
\tag{24}
\]

Substituting `(23)` or `(24)` into the channel-free lower bounds recovers exactly the reliability inequalities of `MC-347`.

This changes the interpretation of the frontier. Raw access, adaptive access, block access, and a one-shot joint transcript do not require separate lower-bound principles. They require different **upper bounds on the same intrinsic source-edge divergence budget**. The acquisition model matters only when converting its own resources into `\mathfrak J`.

## 5. Joint Gaussian encodings pay in source-edge Dirichlet energy

The channel-free formulation gives a concrete joint-observation corollary that is different from the total-variance capacity bound of `MC-343`.

Let

\[
T=F(X)\in\mathbf R^d,
\qquad
Z=T+N,
\qquad
N\sim\mathcal N(0,\sigma^2I_d),
\tag{25}
\]

and let the complete admitted transcript be any downstream processing of `Z`. For two source states `x,x'`, data processing and the equal-covariance Gaussian KL formula give

\[
b(x,x')
\le
\frac{\|F(x)-F(x')\|_2^2}{2\sigma^2}.
\tag{26}
\]

For even rank define the oriented single-flip source energy

\[
\mathcal D_1(F)
:=
\frac1m
\sum_{x\in S}
\sum_{i:\,x^{(i)}\in S}
\|F(x)-F(x^{(i)})\|_2^2.
\tag{27}
\]

Every undirected edge is counted twice, so `(4)` and `(26)` imply

\[
\mathfrak J_1
\le
\frac{\mathcal D_1(F)}{2\sigma^2}.
\tag{28}
\]

Consequently

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R}{4}
\exp\!\left(
-\frac{\mathcal D_1(F)}
{2\sigma^2\Lambda_RR}
\right),
}
\tag{29}
\]

and vanishing risk requires

\[
\boxed{
\mathcal D_1(F)
\ge
2\sigma^2\Lambda_RR
\left[
\log\frac{\Lambda_R}{4\bar p}
\right]_+.
}
\tag{30}
\]

For odd rank, on the conditional support `S_0`, define the oriented pair-flip energy

\[
\mathcal D_2(F)
:=
\frac1M
\sum_{x\in S_0}
\sum_{i<j:\,x^{(ij)}\in S_0}
\|F(x)-F(x^{(ij)})\|_2^2.
\tag{31}
\]

Then `(7)` and `(26)` give

\[
\mathfrak J_2
\le
\frac{\Lambda_R}{2(R-1)\sigma^2}\mathcal D_2(F),
\tag{32}
\]

hence

\[
\boxed{
\bar p
\ge
\frac{\Lambda_R\Lambda_{R-1}}4
\exp\!\left(
-\frac{\mathcal D_2(F)}
{\sigma^2\Lambda_{R-1}R(R-1)}
\right).
}
\tag{33}
\]

The distinction from `MC-343` is load-bearing. `MC-343` controls **how much total source information** a noisy Euclidean transcript can carry from its global variance or diameter; this is enough to rule out bounded-resource constant-factor dephasing. Equations `(29)`--`(33)` instead control **reliable recovery** through the local geometry of neighboring source states. Approaching exact source alignment requires increasing source-edge energy even if all coordinates are encoded jointly in one observation.

The relevant resource is therefore not the dimension of `F`, nor its syntax, nor the number of observations. It is the transcript's discrimination geometry on source perturbations that the destination must distinguish.

## Prior art and novelty boundary

The statistical mechanism is classical and **no novelty is claimed** for it.

Patrice Assouad, *Deux remarques sur l'estimation*, C. R. Acad. Sci. Paris Sér. I Math. **296** (1983), 1021--1024, introduced the hypercube reduction now generally called Assouad's lemma. The present proof uses the same neighboring-hypothesis principle specialized to the punctured reciprocal-source graph.

Jean Bretagnolle and Catherine Huber, *Estimation des densités : risque minimax*, Séminaire de Probabilités XII (1978), 342--363, provide the classical testing inequality used in `(13)`--`(14)`; the paper is available through Numdam/EuDML.

Bin Yu, *Assouad, Fano, and Le Cam*, in *Festschrift for Lucien Le Cam* (Springer, 1997), pp. 423--435, DOI `10.1007/978-1-4612-1880-7_29`, compares the standard minimax lower-bound reductions and their relationships. Alexandre Tsybakov, *Introduction to Nonparametric Estimation* (Springer, 2009), Chapter 2, DOI `10.1007/b13794`, gives a modern systematic treatment of minimax lower bounds including Assouad-type arguments.

The equal-covariance Gaussian KL formula and KL data processing used in `(26)` are standard information theory.

The durable Mathia delta is narrower: the exact reciprocal source law is not the full independent hypercube. It is a punctured cube in even rank and a nonuniform parity image that becomes a punctured even-parity cube after conditioning in odd rank. Equations `(5)`--`(10)` compute the corresponding normalized edge budget and show that the `R log(1/error)` reliability tariff survives **without any raw-coordinate acquisition assumption**. Equations `(29)`--`(33)` identify source-edge Dirichlet energy as one concrete resource that controls this budget for arbitrary joint Gaussian encodings.

## Boundaries and falsification tests

- **This is a reliability theorem, not an arithmetic estimate.** It does not bound `M(x)`, exclude a zeta zero, or construct a Möbius transcript with small or large `\mathfrak J`.
- **Large edge KL is allowed.** The theorem prices reliable source recovery; it does not say a natural arithmetic construction cannot supply the required discrimination.
- **The source graph is part of the statement.** Re-encoding the source labels does not invalidate the theorem if the neighboring hypotheses represent the same coordinate or parity perturbations, but an unrelated graph cannot be substituted merely to manufacture a stronger lower bound.
- **The complete admitted transcript must be charged.** Hidden selector information, side channels, shared randomness revealed to the decoder, or auxiliary observations belong inside `Y`. Omitting them can only create a false obstruction.
- **Symmetrized KL is not itself a physical cost.** A concrete arithmetic or analytic architecture still needs a theorem upper-bounding `\mathfrak J` by its genuine resource: coefficient energy, precision, sample complexity, regularity, harmonic bandwidth, or another source-natural quantity.
- **Infinite KL is an escape, not a contradiction.** Deterministically distinct noiseless transcript values can have singular laws and therefore infinite edge KL. This is the same perfect-precision loophole already isolated by `MC-341`--`MC-343`; a useful application must price the metric/noise/precision that makes those distinctions operational.
- **The odd-rank constant is not claimed optimal.** The pair-flip graph is a parity-preserving control that preserves the correct asymptotic reliability scale.
- **The Gaussian corollary requires a common nondegenerate noise covariance.** Anisotropic or state-dependent noise should be charged by the corresponding pairwise KL geometry rather than forced into `(26)`.
- **Prior-art status is explicit.** The lower-bound method is a classical Assouad/Bretagnolle--Huber mechanism. The finding is retained because it removes a live acquisition-model restriction in the current reciprocal endpoint analysis, not because the statistical theorem is new.

## Consequence for the research line

The reliability chain after `MC-340` is now acquisition-invariant at the finite source level.

`MC-340` says that near matched-filter dephasing requires near-complete source information. `MC-347` showed that raw-coordinate experiments must pay `R log(1/error)` accumulated discrimination. The present result removes the word **raw**: arbitrary joint transcripts must pay the same order in source-edge KL, and any particular observation architecture is responsible only for proving how its own resources upper-bound that edge budget.

This sharply narrows the next arithmetic question. A candidate Möbius-derived transcript should no longer be assessed by nominal access count, scalar/vector syntax, or whether it observes sources separately or jointly. The decisive task is to derive a source-natural upper bound on the neighboring-state transcript divergences at the resolution actually consumed downstream. For noisy Euclidean encodings this becomes the edge-energy problem `(30)` or `(33)`; for harmonic, operator, or arithmetic transcripts the analogous discrimination geometry must be derived rather than assumed.