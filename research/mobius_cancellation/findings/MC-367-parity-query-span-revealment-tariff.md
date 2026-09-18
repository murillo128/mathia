# MC-367 — Parity-query transcripts pay an exact span-revealment tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-366` prices direct own-coordinate access for adaptive coordinate-query transcripts. Its main boundary explicitly leaves arbitrary parity/linear queries open: several joint queries can reveal a source phase even when no query is the corresponding coordinate itself.

For the even-rank reciprocal endpoint, the correct invariant is not whether a parity query **mentions** the target coordinate. It is whether the target coordinate character lies in the linear span of the parity queries accumulated by the transcript.

Let

\[
X=(X_1,\ldots,X_R)
\]

be uniform on

\[
\Omega_R:=\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\},
\qquad
m:=2^R-1.
\tag{1}
\]

Identify the full cube with `G=F_2^R` by `X_j=(-1)^{a_j}`. A parity query indexed by `q in G` returns

\[
\chi_q(X)=(-1)^{q\cdot a}
=\prod_{j=1}^R X_j^{q_j}.
\tag{2}
\]

Fix source cell `i`. Consider a randomized adaptive noiseless parity-query algorithm with source-independent randomness `U_i`. Define its **refined complete transcript**

\[
T_i=(U_i,\text{realized query vectors},\text{query answers}).
\tag{3}
\]

Including `U_i` is only a refinement device: if the coefficient actually sees a coarser observation `Y_i=\phi(T_i)`, conditional-expectation contraction can only reduce its target-phase predictability.

For a realized refined transcript `t`, write

\[
V_i(t):=\operatorname{span}_{\mathbf F_2}\{\text{query vectors on the path to }t\},
\qquad
r_i(t):=\dim V_i(t).
\tag{4}
\]

Define the **linear own-phase revealment event**

\[
L_i:=\{e_i\in V_i(T_i)\},
\qquad
p_i^{\rm lin}:=\mathbf P(L_i).
\tag{5}
\]

For each realization of `U_i`, feed the deleted all-plus point through the same adaptive rule hypothetically. Let `T_i^0(U_i)` be that refined transcript and put

\[
V_i^0(U_i):=V_i(T_i^0(U_i)),
\qquad
r_i^0(U_i):=\dim V_i^0(U_i).
\tag{6}
\]

Then the refined-transcript predictability has the exact identity

\[
\boxed{
\widetilde\rho_i^2
:=\mathbf E\left|\mathbf E[X_i\mid T_i]\right|^2
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

On the event in the numerator, `r_i^0<=R-1`, so the denominator is positive. If the actual admissible observation is any coarsening `Y_i=\phi(T_i)`, the `MC-338` leakage obeys

\[
\boxed{
\rho_i^2
:=\mathbf E\left|\mathbf E[X_i\mid Y_i]\right|^2
\le\widetilde\rho_i^2.
}
\tag{8}
\]

Thus parity-query predictability has only two sources: the accumulated query span reveals `X_i`, or the unique affine fiber containing the deleted all-plus point acquires a precisely quantified one-atom bias.

If every nonrevealing deleted-point path leaves at least `k_i>=1` hidden linear dimensions,

\[
R-r_i^0(U_i)\ge k_i
\quad\text{whenever }e_i\notin V_i^0(U_i),
\tag{9}
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
\tag{10}
\]

For ordinary coordinate queries, the query span contains `e_i` exactly when coordinate `i` was queried. The worst nonrevealing deleted-point path can leave one hidden dimension, so `(10)` recovers the `MC-366` bound

\[
\rho_i^2\le p_i+\frac1m.
\tag{11}
\]

No estimate for `M(x)` follows. This is an exact finite endpoint admission theorem: adaptive linear observations create no third route to target-phase predictability beyond **span revealment plus the puncture correction**.

## 1. Adaptive parity leaves are affine fibers

Condition on `U_i=u`. The algorithm becomes a deterministic adaptive parity tree. Along a realized root-to-leaf path the answers impose

\[
q_1\cdot a=b_1,\ldots,q_t\cdot a=b_t
\qquad(\bmod 2).
\tag{12}
\]

If the path-query span is `V` of rank `r`, the full-cube inputs reaching that transcript form an affine subspace

\[
A=a_0+V^\perp,
\qquad
|A|=2^{R-r}.
\tag{13}
\]

Adaptivity changes which equations are asked, but once a transcript is fixed its fiber is still exactly an affine solution space.

For the target coordinate character `X_i(a)=(-1)^{e_i\cdot a}`, character orthogonality gives

\[
\mathbf E_{a\in A}X_i(a)
\in\{-1,0,+1\},
\tag{14}
\]

with magnitude one exactly when

\[
e_i\in V.
\tag{15}
\]

If `e_i in V=(V^perp)^perp`, the character is constant on the fiber. Otherwise its restriction to `V^perp` is nontrivial and its fiber sum is zero. Hence on the unpunctured cube there is no intermediate target-coordinate correlation at a parity-tree leaf.

## 2. The deleted point gives one exact residual term

The reciprocal source deletes only the origin `a=0`, corresponding to the all-plus source word. Every full-cube leaf not containing `0` is unchanged by this puncture.

For each fixed `u`, there is exactly one hypothetical leaf `A_0(u)` containing `0`: the leaf reached by feeding the deleted point through the deterministic tree. Let its query span have rank `r_0`.

If `e_i in V_0`, the target phase is already fixed and that source mass is included in `p_i^lin`. Suppose instead `e_i notin V_0`. The full-fiber target-character sum is zero, while `X_i(0)=+1`; after deleting `0`,

\[
\sum_{a\in A_0\setminus\{0\}}X_i(a)=-1.
\tag{16}
\]

Since

\[
|A_0\setminus\{0\}|=2^{R-r_0}-1,
\tag{17}
\]

the posterior mean on this one exceptional refined transcript is

\[
-\frac1{2^{R-r_0}-1}.
\tag{18}
\]

The same transcript has punctured-source probability

\[
\frac{2^{R-r_0}-1}{m}.
\tag{19}
\]

Its contribution to the squared posterior mean is therefore exactly

\[
\frac1{m(2^{R-r_0}-1)}.
\tag{20}
\]

All other nonrevealing leaves contribute zero. Averaging `(20)` over `U_i` proves `(7)`. Equation `(8)` is the `L^2` contraction of conditional expectation from the refined sigma-algebra `sigma(T_i)` to the coarser `sigma(Y_i)`.

This also shows why merely **touching** coordinate `i` is not the correct resource. One query `e_i+e_j` has `e_i` outside its one-dimensional span and gives zero full-cube prediction of `X_i`. If a later query supplies `e_j`, the accumulated span contains `e_i=(e_i+e_j)+e_j`, and `X_i` becomes exactly reconstructible.

## 3. A common low-rank parity sketch cannot serve all source cells cheaply

A stronger corollary holds when every source cell receives one **common refined parity transcript** `T`, or any common coarsening of it. For a realized transcript write

\[
V(T)=\text{query span},
\qquad
r(T)=\dim V(T),
\]

and define

\[
N(V):=|\{i:e_i\in V\}|.
\tag{21}
\]

Distinct standard basis vectors are linearly independent, so

\[
N(V)\le\dim V.
\tag{22}
\]

Therefore

\[
\bar p^{\rm lin}
:=\frac1R\sum_i\mathbf P(e_i\in V(T))
=
\frac1R\mathbf E N(V(T))
\le
\frac1R\mathbf E r(T).
\tag{23}
\]

Assume every path has rank at most `q<R`. The puncture correction in `(7)` is at most

\[
\kappa_{R,q}
:=\frac1{(2^R-1)(2^{R-q}-1)}.
\tag{24}
\]

Hence for the actual common observation available to the coefficients,

\[
\boxed{
\rho^2
:=\frac1R\sum_i\rho_i^2
\le
\frac qR+\kappa_{R,q}.
}
\tag{25}
\]

Combining `(25)` with the exact information-energy inequality of `MC-338`, every admissible endpoint coefficient family with normalized energy `E(W)<=C` satisfies

\[
\boxed{
\delta(W)
\ge
\left(
1-\sqrt C
\sqrt{\frac qR+\frac1{(2^R-1)(2^{R-q}-1)}}
\right)_+.
}
\tag{26}
\]

Thus a common parity sketch with `q=o(R)` and bounded normalized energy has

\[
\delta(W)\to1.
\tag{27}
\]

If `delta(W)<=1-eta`, then

\[
\frac qR
\ge
\frac{\eta^2}{C}
-
\frac1{(2^R-1)(2^{R-q}-1)}.
\tag{28}
\]

At matched-filter energy `C=1`, exact all-source dephasing is impossible for `q<R`, because for every `q<=R-1`,

\[
\frac qR+\kappa_{R,q}<1.
\tag{29}
\]

So a **single shared parity sketch needs full rank** before unit-energy coefficients can recover all endpoint source phases exactly.

This rank statement does **not** apply to separately targeted source-cell transcripts. Cell `i` could use the rank-one query `e_i`, giving full own-phase revealment at rank one. For source-specific transcripts the correct currency is the per-cell span-revealment probability in `(7)`–`(10)`.

## 4. Relation to MC-366 and the generic-channel boundary

For coordinate decision trees every query vector is a standard basis vector. Before coordinate `i` is queried, the span of the other queried basis vectors cannot contain `e_i`. Thus the linear revealment event reduces exactly to the direct-query event of `MC-366`.

The parity theorem is genuinely broader because joint queries can reconstruct a target direction without ever issuing the singleton query. Conversely, a query that includes the target coordinate need not reveal it. Query-span membership is the invariant distinction.

The coordinatewise BSC family from `MC-365` remains outside this noiseless linear-query class because it exposes each target coordinate and then corrupts it. It already spends full own-source access before noise is applied. `MC-367` instead closes the exact-linear side-channel escape left open by `MC-366`.

## Prior art and novelty boundary

Parity/linear decision trees and their affine-leaf geometry are classical. Kushilevitz and Mansour, *Learning Decision Trees Using the Fourier Spectrum*, SIAM Journal on Computing **22** (1993), 1331–1348, DOI `10.1137/0222080`, study decision trees that query linear functions over `F_2`.

Girish, Tal and Wu, *Fourier Growth of Parity Decision Trees*, 36th Computational Complexity Conference (CCC 2021), LIPIcs **200**, article 39, DOI `10.4230/LIPIcs.CCC.2021.39`, make the exact leaf fact used here explicit: inputs reaching a node form an affine subspace, the fully correlated Fourier characters are the orthogonal subspace, and this orthogonal subspace is the span of the parity queries on the path. Their Fact 19 records the resulting `{-1,0,+1}` character-expectation trichotomy.

No novelty is claimed for parity decision trees, affine fibers, Walsh-character orthogonality, or query-span reconstruction. A targeted search on 18 September 2026 for parity-decision-tree results on a one-atom-punctured cube did not locate a theorem needed beyond those classical facts. The proof of `(7)` is elementary once the reciprocal endpoint source law is fixed.

The durable line-specific delta is the composition with the exact source model and `MC-338`: deleting the principal source word creates one computable residual term, while every other parity-tree contribution is classified exactly by query-span revealment. The common-sketch corollary `(26)` then turns ordinary linear rank into a dephasing-energy admission barrier. The external literature is background rather than a load-bearing theorem, so no new `SOURCES.md` anchor is required.

## Boundaries and falsification tests

- **Even rank is load-bearing.** The punctured independent-source-cube law is the even-rank reciprocal endpoint from `MC-340`; the odd-rank source has the global parity relation already analyzed in `MC-337` and `MC-338`.
- **Queries are noiseless `F_2` parities.** General nonlinear measurements, other finite groups, arbitrary real sketches, and noisy joint channels are not covered.
- **Randomness is source-independent.** Equation `(7)` is exact for the refined transcript that includes the random seed. If the seed is hidden from the coefficient, `(8)` gives the correct inequality by coarsening.
- **The complete path is charged.** Query vectors and answers are included. Under adaptivity the chosen vectors encode previous answers but no source information beyond the path itself.
- **Rank alone is not a per-cell tariff.** The rank corollary requires one common transcript; separately targeted sketches are governed by span revealment.
- **Touching is not revealing.** A nonzero `i`th query coefficient is insufficient; the decisive event is `e_i` entering the accumulated span.
- **The puncture term is necessary.** Even with no span revealment, the deleted all-plus point creates one biased hypothetical leaf, quantified exactly by `(20)`.
- **No arithmetic cancellation estimate is proved.** A future Möbius application must show that a concrete arithmetic transcript admits this parity-sketch provenance with small span revealment or small common rank, then connect the endpoint obstruction to a global cancellation mechanism.

## Consequence for the research line

`MC-366` left parity queries, group characters and linear side channels as the first explicit escape from coordinate revealment. `MC-367` closes the `F_2` parity-query part of that escape without reverting to a generic divergence tariff.

For parity transcripts, own-phase access is query-span membership up to one exact puncture correction. A common bounded-rank linear sketch cannot supply bounded-energy all-source dephasing, while separate parity sketches must pay whenever their accumulated query span reveals the target direction.

The remaining provenance frontier is now genuinely nonlinear/dependent source information, nonbinary group measurements, noisy joint channels, or a concrete Möbius-derived transcript that fails to admit a parity-sketch representation. The productive next step is to audit such a concrete arithmetic transcript against this span criterion rather than invent another generic channel currency.