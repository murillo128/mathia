# MC-349 — Destination quotient cuts determine the intrinsic reliability tariff

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-348` proves that reliable recovery of the **whole reciprocal source vector** forces an `R log(1/error)` source-edge KL expenditure. That is the correct admission test when the downstream construction genuinely needs coordinatewise source recovery. It can, however, overprice a future arithmetic destination that consumes only a quotient or aggregate of the source state.

The correct channel-free object is the cut that the actual destination induces on the source-neighbor graph.

Let `S` be a finite source support of size `m`, let `G=(S,E)` be a fixed source-natural neighboring-state graph, and let `X` be uniform on `S`. For each source state `x`, let `P_x` be the law of the complete admitted transcript `Y`. Define, as in `MC-348`,

\[
b_e=b(x,x')
:=\frac12\left(D(P_x\|P_{x'})+D(P_{x'}\|P_x)\right)
\qquad(e=\{x,x'\}).
\tag{1}
\]

Now let

\[
q:S\to\mathcal Q
\tag{2}
\]

be the **actual downstream discrete destination** that the transcript must determine; `q` need not be injective and `\mathcal Q` need not be binary. Let

\[
E_q:=\{\{x,x'\}\in E:q(x)\ne q(x')\}
\tag{3}
\]

be its source-edge boundary, and write

\[
d_q(x):=|\{e\in E_q:x\in e\}|,
\qquad
\Delta_q:=\max_{x\in S}d_q(x).
\tag{4}
\]

Assume `E_q` is nonempty and define its average cut degree and transcript divergence expenditure by

\[
\kappa_q:=\frac{2|E_q|}{m},
\qquad
\mathfrak J_q:=\frac{2}{m}\sum_{e\in E_q}b_e.
\tag{5}
\]

For an arbitrary estimator `\widehat q(Y)`, let

\[
p_q:=\mathbf P\{\widehat q(Y)\ne q(X)\}.
\tag{6}
\]

Then

\[
\boxed{
p_q
\ge
\frac{\kappa_q}{4\Delta_q}
\exp\!\left(-\frac{\mathfrak J_q}{\kappa_q}\right).
}
\tag{7}
\]

Equivalently,

\[
\boxed{
\mathfrak J_q
\ge
\kappa_q
\left[
\log\frac{\kappa_q}{4\Delta_q p_q}
\right]_+.
}
\tag{8}
\]

Thus the reliability tariff is controlled not by output entropy or the number of destination labels alone, but by the **source-edge sensitivity of the destination**. A one-bit destination may still require an extensive divergence budget when changing many independent source directions changes that bit, while a coarse quotient with a sparse source boundary can evade the full-vector tariff.

For the even-rank reciprocal source law of `MC-340` and `MC-348`,

\[
S=\{-1,+1\}^R\setminus\{\mathbf1\},
\qquad
m=2^R-1,
\qquad
\Lambda_R=\frac{2^R-2}{2^R-1},
\tag{9}
\]

with the surviving Hamming-one graph. For any nonempty coordinate set `T\subseteq\{1,\ldots,R\}` of size `k`, consider the one-bit parity destination

\[
q_T(x):=\prod_{i\in T}x_i.
\tag{10}
\]

Exactly the edges flipping a coordinate in `T` cross the destination cut. Hence

\[
|E_{q_T}|=k(2^{R-1}-1),
\qquad
\kappa_{q_T}=\Lambda_R k,
\qquad
\Delta_{q_T}=k.
\tag{11}
\]

If

\[
\mathfrak J_T
:=\frac2m\sum_{e\in E_{q_T}}b_e,
\tag{12}
\]

then `(7)` becomes

\[
\boxed{
p_T
\ge
\frac{\Lambda_R}{4}
\exp\!\left(-\frac{\mathfrak J_T}{\Lambda_R k}\right),
}
\tag{13}
\]

and therefore

\[
\boxed{
\mathfrak J_T
\ge
\Lambda_R k
\left[
\log\frac{\Lambda_R}{4p_T}
\right]_+.
}
\tag{14}
\]

This gives an exact interpolation between two qualitatively different one-bit targets. A single coordinate (`k=1`) requires only an `O(log(1/p))` boundary-divergence tariff. Full parity (`k=R`) is also just one bit, but reliable recovery costs

\[
\Omega\!\left(R\log\frac1p\right)
\tag{15}
\]

in the source-edge currency because **every** source direction changes the answer.

Moreover, if `q_i(x)=x_i` and `\mathfrak J_i` is its cut expenditure, then the Hamming-one edges partition by their flipped coordinate, so

\[
\sum_{i=1}^R\mathfrak J_i=\mathfrak J_1^{\rm MC\text{-}348}.
\tag{16}
\]

Applying `(13)` with `k=1` to each coordinate and using Jensen gives

\[
\frac1R\sum_i p_i
\ge
\frac{\Lambda_R}{4}
\exp\!\left(
-\frac{\mathfrak J_1^{\rm MC\text{-}348}}
{\Lambda_RR}
\right),
\tag{17}
\]

which is exactly the even-rank reliability inequality of `MC-348`. The new statement therefore does not weaken or replace the full-recovery theorem; it identifies the destination-relative structure that theorem was implicitly summing over.

No estimate for `M(x)` follows. The result is a finite-source guardrail: before importing a full-vector information or reliability obstruction into a Möbius-derived endpoint, one must prove that the downstream arithmetic quantity actually separates the corresponding source directions.

## 1. Every destination-cut edge is a binary testing problem

For each source state define its conditional destination error

\[
e(x):=P_x\{\widehat q(Y)\ne q(x)\}.
\tag{18}
\]

Take a cut edge `e={x,x'}` with `q(x)\ne q(x')`. Let

\[
A_x:=\{\widehat q(Y)=q(x)\}.
\]

Under source state `x`, `P_x(A_x^c)=e(x)`. Under `x'`, the event `A_x` is necessarily an error, so

\[
P_{x'}(A_x)\le e(x').
\tag{19}
\]

The Bretagnolle--Huber testing inequality in each orientation therefore gives

\[
e(x)+e(x')
\ge
\frac12 e^{-D(P_x\|P_{x'})},
\qquad
 e(x)+e(x')
\ge
\frac12 e^{-D(P_{x'}\|P_x)}.
\tag{20}
\]

Since the smaller directional KL divergence is no larger than their average,

\[
\boxed{
e(x)+e(x')\ge\frac12e^{-b_e}.
}
\tag{21}
\]

This is valid for an arbitrary destination alphabet. The proof only uses the fact that the two neighboring source states require different correct outputs.

## 2. Cut geometry converts the edge tests into a destination risk bound

Summing `(21)` over the destination boundary gives

\[
\sum_{x\in S}d_q(x)e(x)
\ge
\frac12\sum_{e\in E_q}e^{-b_e}.
\tag{22}
\]

The left-hand side is bounded above by

\[
\Delta_q\sum_x e(x)
=\Delta_q m p_q.
\tag{23}
\]

On the right, Jensen yields

\[
\sum_{e\in E_q}e^{-b_e}
\ge
|E_q|
\exp\!\left(
-\frac1{|E_q|}\sum_{e\in E_q}b_e
\right).
\tag{24}
\]

Using `(5)`,

\[
\frac{|E_q|}{2m\Delta_q}
=\frac{\kappa_q}{4\Delta_q},
\qquad
\frac1{|E_q|}\sum_{e\in E_q}b_e
=\frac{\mathfrak J_q}{\kappa_q}.
\tag{25}
\]

Substitution of `(24)`--`(25)` into `(22)`--`(23)` proves `(7)`, and inversion proves `(8)`.

The two geometric quantities have distinct roles. `\kappa_q` is the **average number of source-neighbor directions that change the destination**; on a full Boolean cube this is the standard total edge influence. `\Delta_q` is the maximum local boundary degree and accounts for the fact that destination errors could concentrate on source states where many cut edges meet.

## 3. The reciprocal puncture preserves the parity sensitivity scale

For even `R`, each coordinate direction contributes `2^{R-1}` edges in the full cube. Removing the all-`+1` state deletes exactly one edge in each direction. Therefore, for a parity on `k` coordinates,

\[
|E_{q_T}|
=k(2^{R-1}-1).
\tag{26}
\]

Every source vertex has at most `k` incident `T`-edges, and a surviving vertex with all `k` such neighbors exists, so `\Delta_{q_T}=k`. Equations `(11)`--`(14)` follow exactly.

The key point is conceptual rather than the small puncture correction. The destination has only two values for every `k`, but its source-edge sensitivity grows linearly with `k`. Consequently a transcript that reliably reports the parity of all `R` reciprocal source bits must discriminate across essentially every local source perturbation even though it emits only one semantic bit.

Conversely, the theorem explicitly leaves room for quotient destinations whose edge boundary is sparse. That is not a defect of the lower bound: it is the correct warning that **full source reconstruction is not automatically necessary for every downstream arithmetic statistic**.

## 4. Odd rank uses the same theorem on the parity-preserving source graph

For odd `R`, `MC-340` shows that after conditioning away the exceptional all-`+1` image, the reciprocal source is uniform on a punctured even-parity cube. `MC-348` uses the natural graph of Hamming-two pair flips because single-bit flips leave that support.

The theorem above applies verbatim to that conditional support with `G` equal to the surviving pair-flip graph. For any destination `q`, one must count only pair-flip edges on which `q` changes and use the corresponding conditional `\kappa_q`, `\Delta_q`, and edge-KL budget. The unconditional error is at least the conditioning probability `\Lambda_R` times the resulting conditional error.

No generic `R log(1/error)` conclusion is valid before that destination cut is computed. The full-coordinate result of `MC-348` obtains the extensive scale because each coordinate error is charged across all relevant pair-flip directions; a coarser quotient may have a genuinely different boundary geometry.

## Prior art and novelty boundary

The statistical mechanism is classical and **no novelty is claimed** for the general lower-bound method.

Patrice Assouad, *Deux remarques sur l'estimation*, C. R. Acad. Sci. Paris Sér. I Math. **296** (1983), 1021--1024, introduced the neighboring-hypothesis hypercube reduction. Jean Bretagnolle and Catherine Huber, *Estimation des densités : risque minimax*, Séminaire de Probabilités XII (1978), 342--363, provide the two-point testing inequality used in `(20)`--`(21)`. Bin Yu, *Assouad, Fano, and Le Cam*, in *Festschrift for Lucien Le Cam* (Springer, 1997), pp. 423--435, and Alexandre Tsybakov, *Introduction to Nonparametric Estimation* (Springer, 2009), Chapter 2, give standard modern treatments of these minimax reductions.

The interpretation of `\kappa_q` as an edge-sensitivity quantity is also standard Boolean-function language. Ryan O'Donnell, *Analysis of Boolean Functions* (Cambridge University Press, 2014; corrected arXiv edition `2105.10386`), treats coordinate influence, total influence, edge boundaries, parity, and threshold examples on the Boolean cube.

The durable Mathia delta is narrower. `MC-348` had already identified the exact reciprocal source graph and its channel-free edge-KL currency, but its destination was full coordinate recovery. Equations `(7)`--`(8)` expose the **destination-relative quotient cut** inside that same fixed source geometry, and `(13)`--`(17)` show exactly when the existing extensive reliability tariff survives or collapses. The result is retained as a guardrail against applying a full-reconstruction lower bound to a downstream arithmetic quantity that may require less source discrimination.

## Boundaries and falsification tests

- **This is not an arithmetic estimate.** It does not bound `M(x)`, prove a zero-free region, or show that a natural Möbius transcript has small source-edge KL.
- **The destination must be real.** One may not choose a convenient quotient `q` after the fact. A candidate arithmetic mechanism must derive the actual finite-source destination consumed by its downstream theorem or approximation.
- **The neighboring graph remains source-natural.** The cut is taken inside the reciprocal source graph already justified by the construction. Arbitrary distant pairs cannot be inserted merely to enlarge `\kappa_q`.
- **A sparse cut is a genuine escape from full reconstruction.** If `\kappa_q` is small or `\kappa_q/\Delta_q` degenerates, `(7)` may be weak. That means the current edge test does not certify a large reliability cost for that quotient; it must not be upgraded to the `MC-348` tariff by analogy.
- **A one-bit output need not be cheap.** Subset parity `(10)` is an exact counterexample to any argument that prices a destination only by `H(q(X))` or by alphabet size. Its edge sensitivity, not its semantic output length, drives `(14)`.
- **Large or infinite edge KL remains an escape.** As in `MC-348`, a concrete arithmetic architecture still needs an independent theorem upper-bounding the destination-cut divergence budget by coefficient energy, precision, harmonic bandwidth, regularity, or another genuine resource.
- **The maximum cut degree may not be sharp.** Equation `(23)` deliberately uses only `\Delta_q`. A destination with highly inhomogeneous boundary degree may admit a stronger weighted or measure-sensitive inequality, but no such sharpening is assumed here.
- **Odd-rank conditioning is load-bearing.** Single-bit cut counts cannot be transplanted into the parity-constrained odd-rank source support; the pair-flip graph must be used.
- **Prior-art status is explicit.** The two-point/Assouad mechanism and Boolean influence vocabulary are classical. No novelty is claimed for the abstract statistical theorem.

## Consequence for the research line

The finite-source reliability program now has a necessary destination-selection gate.

`MC-340` and `MC-348` remain decisive whenever bounded-energy dephasing or another endpoint theorem actually forces near-coordinatewise source recovery. But future Möbius-derived transcripts may feed a downstream statistic that is insensitive to some reciprocal source directions. In that case the correct invariant object is not the whole source cube and not transcript entropy alone; it is the cut of the **actual destination quotient** inside the source graph.

This creates a concrete next arithmetic test. For any proposed bridge from reciprocal source data toward a Mertens or zero-location statement, first derive the finite-source destination `q` that the analytic step truly consumes. Then compute or bound its source-edge sensitivity `\kappa_q` and local concentration `\Delta_q`, and only afterward ask whether the analytic architecture can supply the required cut-edge divergence `\mathfrak J_q`. Parity-like destinations preserve an extensive tariff even with a one-bit output; low-boundary quotients expose a real loophole that must be closed by arithmetic structure rather than by full-reconstruction language.