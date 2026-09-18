# MC-367 — Parity-query transcripts pay an exact span-revealment tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-366` prices direct own-coordinate access for adaptive coordinate-query transcripts. Its main boundary explicitly leaves arbitrary parity/linear queries open: several joint queries can reveal a source phase even when no query is the corresponding coordinate itself.

For the even-rank reciprocal endpoint, the correct invariant is not whether a parity query **mentions** the target coordinate. It is whether the target coordinate character lies in the linear span of the parity queries accumulated by the transcript.

Let

\[
X=(X_1,\ldots,X_R)
\]

be uniform on the punctured source cube

\[
\Omega_R:=\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\qquad
m:=|\Omega_R|=2^R-1.
\tag{1}
\]

Identify the full cube with `G=F_2^R` by `X_j=(-1)^{a_j}`. A parity query indexed by `q in G` returns

\[
\chi_q(X)=(-1)^{q\cdot a}
=\prod_{j=1}^R X_j^{q_j}.
\tag{2}
\]

Fix a source cell `i`. Let `Y_i` be the complete transcript of a randomized adaptive noiseless parity-query algorithm with source-independent internal randomness `U_i`. The transcript records the realized query vectors and their answers. For a realized transcript `y`, write

\[
V_i(y):=\operatorname{span}_{\mathbf F_2}\{\text{query vectors on the path to }y\},
\qquad
r_i(y):=\dim V_i(y).
\tag{3}
\]

Define the **linear own-phase revealment event**

\[
L_i:=\{e_i\in V_i(Y_i)\},
\qquad
p_i^{\rm lin}:=\mathbf P(L_i).
\tag{4}
\]

For each realization of `U_i`, also feed the deleted all-plus point through the same adaptive query rule hypothetically. Let `Y_i^0(U_i)` denote that hypothetical transcript, and put

\[
V_i^0(U_i):=V_i(Y_i^0(U_i)),
\qquad
r_i^0(U_i):=\dim V_i^0(U_i).
\tag{5}
\]

Then the exact `L^2` predictability entering `MC-338`,

\[
\rho_i^2
:=\mathbf E\left|
\mathbf E[X_i\mid Y_i]
\right|^2,
\tag{6}
\]

satisfies the identity

\[
\boxed{
\rho_i^2
=
p_i^{\rm lin}
+
\frac1m\,
\mathbf E_{U_i}
\left[
\frac{\mathbf1_{\{e_i\notin V_i^0(U_i)\}}}
{2^{R-r_i^0(U_i)}-1}
\right].
}
\tag{7}
\]

The fraction in `(7)` is used only on `e_i notin V_i^0`; there `r_i^0<=R-1`, so its denominator is positive. Thus every parity transcript has exactly two sources of own-phase predictability:

1. the accumulated parity queries linearly reveal `X_i`, meaning `e_i` lies in their span; or
2. the transcript lands on the unique affine fiber containing the deleted all-plus point, and the single missing atom leaves a precisely quantified residual bias.

In particular, if every nonrevealing deleted-point path leaves at least `k_i>=1` hidden linear dimensions,

\[
R-r_i^0(U_i)\ge k_i
\quad\text{whenever }e_i\notin V_i^0(U_i),
\tag{8}
\]

then

\[
\boxed{
\rho_i^2
\le
p_i^{\rm lin}
+
\frac1{m(2^{k_i}-1)}.
}
\tag{9}
\]

This strictly extends the provenance tariff of `MC-366`: for ordinary coordinate queries the path span contains `e_i` exactly when coordinate `i` was queried, while the worst nonrevealing deleted-point path can have hidden dimension one. Equation `(9)` therefore reduces to

\[
\rho_i^2\le p_i+\frac1m,
\]

which is `MC-366` equation (3).

No estimate for `M(x)` follows. The result closes the parity-query gap in the finite reciprocal endpoint: arbitrary adaptive linear observations do not create a third route to target-phase predictability beyond **span revealment plus the one-point puncture correction**.

## 1. Every adaptive parity transcript is an affine fiber

Condition first on the source-independent randomness `U_i=u`. A deterministic adaptive parity tree remains. Along any realized root-to-leaf path, the query answers impose a consistent affine system

\[
q_1\cdot a=b_1,\ldots,q_t\cdot a=b_t
\qquad(\bmod 2).
\tag{10}
\]

If the path-query span is `V` of rank `r`, the set of full-cube inputs that produce that transcript is an affine subspace

\[
A=a_0+V^\perp,
\qquad
|A|=2^{R-r}.
\tag{11}
\]

Adaptivity does not alter this leaf geometry: it changes which query is selected after a previous answer, but once a transcript is fixed, the path still records a finite consistent linear system.

For the target coordinate character `X_i(a)=(-1)^{e_i\cdot a}`, standard character orthogonality on the affine subspace gives

\[
\mathbf E_{a\in A}X_i(a)
\in\{-1,0,+1\},
\tag{12}
\]

with magnitude one exactly when

\[
e_i\in V.
\tag{13}
\]

Indeed, if `e_i in V=(V^perp)^perp`, the character is constant on the affine fiber. Otherwise its restriction to `V^perp` is nontrivial and its full-fiber sum vanishes.

Thus on the **unpunctured** cube there is no intermediate linear predictability at a parity-tree leaf: the target coordinate is either fixed by the query span or has conditional mean zero.

## 2. Deleting one point creates one exact exceptional contribution

The reciprocal source is not the full cube: the origin `a=0`, corresponding to the all-plus phase word, is deleted.

If a full-cube leaf `A` does not contain `0`, puncturing changes nothing. Therefore `(12)` remains exact on that leaf.

There is exactly one hypothetical leaf for the deleted point for each fixed `u`, namely the leaf `A_0(u)` reached by feeding `a=0` through the deterministic tree. Let its query span have rank `r_0`.

If `e_i in V_0`, the target phase is already fixed by the linear transcript, so this leaf is included in the revealment term `p_i^lin`.

Suppose instead that `e_i notin V_0`. The full affine fiber has zero target-character sum, but it contains `0`, where `X_i(0)=+1`. Removing that one point leaves

\[
\sum_{a\in A_0\setminus\{0\}}X_i(a)=-1.
\tag{14}
\]

Since

\[
|A_0\setminus\{0\}|=2^{R-r_0}-1,
\tag{15}
\]

the posterior mean on the punctured exceptional leaf is exactly

\[
\mathbf E[X_i\mid Y_i=Y_i^0(u)]
=-\frac1{2^{R-r_0}-1}.
\tag{16}
\]

That leaf has probability

\[
\frac{2^{R-r_0}-1}{m}
\tag{17}
\]

under the punctured uniform law. Its contribution to the squared posterior mean is therefore

\[
\frac{2^{R-r_0}-1}{m}
\frac1{(2^{R-r_0}-1)^2}
=
\frac1{m(2^{R-r_0}-1)}.
\tag{18}
\]

Every other nonrevealing leaf contributes zero. Averaging `(18)` over the source-independent randomness proves `(7)`, and `(9)` follows immediately from `(8)`.

The formula also explains why **querying a parity that contains coordinate `i` is not itself own-phase revealment**. For example, one query `e_i+e_j` leaves `e_i` outside the one-dimensional query span and does not predict `X_i` on the full cube. If a later query supplies `e_j`, however, the span contains `e_i=(e_i+e_j)+e_j`, and the target phase becomes exactly reconstructible. Span membership, rather than syntactic coordinate incidence, is the invariant resource.

## 3. A common low-rank parity sketch cannot dephase all source cells cheaply

There is a stronger consequence when every source cell receives the **same** parity transcript `Y`, as happens for a common global linear sketch rather than `R` separately targeted algorithms.

For a realized transcript let `V(Y)` be its query span and `r(Y)=dim V(Y)`. Define

\[
N(V):=|\{i:e_i\in V\}|.
\tag{19}
\]

Distinct standard basis vectors are linearly independent, so every `r`-dimensional subspace satisfies

\[
N(V)\le r.
\tag{20}
\]

Consequently the average linear revealment obeys

\[
\bar p^{\rm lin}
:=\frac1R\sum_i\mathbf P(e_i\in V(Y))
=
\frac1R\mathbf E N(V(Y))
\le
\frac1R\mathbf E r(Y).
\tag{21}
\]

Assume every positive-probability path has rank at most `q<R`. Then the deleted-point correction in `(7)` is at most

\[
\kappa_{R,q}
:=
\frac1{m(2^{R-q}-1)}.
\tag{22}
\]

Averaging over source cells gives

\[
\boxed{
\rho^2
:=\frac1R\sum_i\rho_i^2
\le
\frac qR+\kappa_{R,q}.
}
\tag{23}
\]

Insert `(23)` into the exact information-energy obstruction of `MC-338`. Every coefficient family measurable with respect to that common transcript, with normalized coefficient energy `E(W)<=C`, satisfies

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt C
\sqrt{\frac qR+\frac1{(2^R-1)(2^{R-q}-1)}}
\right)_+.
}
\tag{24}
\]

Hence a common parity sketch with `q=o(R)` and bounded normalized energy has

\[
\delta(W)\to1.
\tag{25}
\]

More generally, if `delta(W)<=1-eta`, then `(24)` forces

\[
\frac qR
\ge
\frac{\eta^2}{C}
-
\frac1{(2^R-1)(2^{R-q}-1)}.
\tag{26}
\]

At matched-filter energy `C=1`, exact all-source dephasing cannot occur with `q<R`: for `q<=R-1`,

\[
\frac qR+\kappa_{R,q}<1.
\tag{27}
\]

Thus a **single shared parity transcript needs full rank** before unit-energy coefficients can recover every endpoint source phase exactly. This is stronger than a raw query-count statement because dependent/repeated parity queries do not increase `r(Y)`.

The common-transcript hypothesis is load-bearing. If every source cell is allowed its own targeted rank-one transcript, cell `i` may simply query `e_i`; then `p_i^lin=1` for every `i` despite rank one per transcript. For source-specific transcripts the correct currency remains the span-revealment probability in `(7)`, not rank alone.

## 4. Relation to MC-366 and the BSC boundary

For a coordinate decision tree, every query vector is a standard basis vector. On a path that has not queried coordinate `i`, the span of the other queried basis vectors cannot contain `e_i`. Hence

\[
L_i=Q_i
\tag{28}
\]

in the notation of `MC-366`. The parity theorem therefore contains the coordinate-query theorem as the special case in which linear revealment can happen only by direct self-query.

The new content appears when observations are joint. Queries such as `e_i+e_j` may touch the own phase without revealing it; conversely, several joint queries may reconstruct `e_i` without ever issuing the singleton query `e_i`. Equation `(7)` prices exactly that distinction.

The coordinatewise BSC family from `MC-365` remains outside this noiseless parity-tree theorem because it exposes each target coordinate and then corrupts it. It already sits on the full-own-source-access side of the provenance boundary. The present result instead classifies what can be extracted from exact linear combinations of the source phases before arbitrary nonlinear side channels are admitted.

## Prior art and novelty boundary

Parity/linear decision trees and their affine-leaf geometry are classical. Kushilevitz and Mansour, *Learning Decision Trees Using the Fourier Spectrum*, SIAM Journal on Computing **22** (1993), 1331–1348, DOI `10.1137/0222080`, study decision trees that query linear functions over `F_2`.

Girish, Tal and Wu, *Fourier Growth of Parity Decision Trees*, 36th Computational Complexity Conference (CCC 2021), LIPIcs **200**, article 39, DOI `10.4230/LIPIcs.CCC.2021.39`, make the exact leaf fact used above explicit: inputs reaching a node form an affine subspace, the fully correlated Fourier characters are the orthogonal subspace, and this orthogonal subspace is the span of the parity queries on the path. Their Fact 19 records the resulting `{-1,0,+1}` character expectation trichotomy.

No novelty is claimed for parity decision trees, affine fibers, Walsh-character orthogonality, or query-span reconstruction. A targeted search on 18 September 2026 for parity-decision-tree results on a one-atom-punctured cube did not locate a theorem needed beyond those classical facts. The proof of `(7)` is elementary once the reciprocal endpoint source law is fixed.

The durable line-specific delta is the composition with the exact source model and `MC-338`: deleting the principal source word creates one computable residual term, while every other parity-tree contribution is exactly classified by query-span revealment. The common-sketch corollary `(24)` then turns ordinary linear rank into a dephasing-energy admission barrier. Because the external literature is background rather than a load-bearing theorem, no new `SOURCES.md` anchor is required.

## Boundaries and falsification tests

- **Even rank is load-bearing.** The punctured independent-source-cube law used here is the even-rank reciprocal endpoint from `MC-340`. The odd-rank source has the global parity relation already analyzed in `MC-337` and `MC-338`.
- **Queries are noiseless `F_2` parities.** General nonlinear measurements, modular queries over other groups, arbitrary real sketches, and noisy joint channels are not covered.
- **Randomness must be source-independent.** If the algorithm receives source-dependent side information before querying, that information must be included in the observation and can invalidate the affine-fiber model.
- **The complete transcript matters.** Query vectors as well as answers are part of `Y_i`; under adaptivity the chosen vectors themselves encode previous answers but no extra source information beyond the tree path.
- **Rank is not enough for separately targeted sketches.** The rank bound `(23)` applies only to one common transcript shared across source cells. Source-specific parity trees are governed by the per-cell span-revealment probabilities in `(7)`.
- **Touching is not revealing.** A query with nonzero `i`th coefficient need not reveal `X_i`; the decisive event is `e_i` entering the total query span.
- **The puncture term is necessary.** Even when `e_i` never enters the span, the deleted all-plus point leaves a nonzero posterior on its unique hypothetical leaf. Equation `(18)` gives that contribution exactly.
- **No arithmetic cancellation estimate is proved.** A future Möbius application must show that its actual coefficient provenance is representable by a parity transcript with small span revealment or small common rank, and then connect the finite endpoint obstruction to a global cancellation mechanism.

## Consequence for the research line

`MC-366` left parity queries, group characters and linear side channels as the first explicit escape from coordinate revealment. `MC-367` closes that escape at the reciprocal endpoint without reverting to a generic information divergence.

For parity transcripts, **own-phase access is exactly query-span membership**, up to the single deleted-point correction. A common bounded-rank linear sketch cannot supply bounded-energy all-source dephasing, and separate parity sketches must pay explicitly whenever their accumulated queries span the target coordinate.

The next live provenance question is therefore narrower: an arithmetic transcript can evade this theorem only by using genuinely nonlinear/dependent source information, by carrying substantial target-direction span revealment, or by failing to admit a parity-sketch representation at all. The useful next step is not another generic channel tariff, but an audit of a concrete Möbius-derived transcript against this span criterion.