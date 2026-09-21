# PC-395 — Jacobsthal gap control closes all summable Kron outlier windows

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the remaining longer-window unscaled-outlier route left open by PC-394 in the positive inverse-power chord/Kron branch.

PC-394 proved that, for the simultaneous-deletion correction `Delta_T` at a primorial refinement step, summable inverse-power chord tails force `||Delta_T||_op -> 0` on the polynomial window `H=p^u` whenever `alpha>1/2` and `2<u<=1+2 alpha`. Its bound used the total internal deleted-layer conductance, hence carried a factor proportional to the number of deleted points and became inconclusive on longer windows.

That window restriction is not intrinsic. The deleted layer is `q`-separated, while every deleted point lies within a Jacobsthal gap of the surviving `q`-rough set. Combining those two local facts controls the Euclidean synthesis norm of the normalized incidence matrix independently of the total number of deletions. If `J(q)` denotes the maximal gap between integers having no prime factor `<=q`, then

\[
\boxed{
\|\Delta_T\|_{\rm op}
\ll_{\alpha,\tau}
\left(1+\frac{J(q)}q\right)q^{-2\alpha}.
}
\tag{1}
\]

Iwaniec's classical linear-sieve bound `J(q)\ll q^2` therefore gives

\[
\boxed{
\|\Delta_T\|_{\rm op}
\ll_{\alpha,\tau} q^{1-2\alpha}\longrightarrow0
\qquad(\alpha>1/2).
}
\tag{2}
\]

The estimate contains no deletion-count or window-length factor. Consequently, throughout the local-arc regime `H=o(M)` of the normalized chord kernel, and in particular on **every fixed polynomial window** `H=p^u`, the irreducible simultaneous-deletion correction cannot create a persistent unscaled spectral outlier for any `alpha>1/2`. For the canonical inverse-square interaction `alpha=1`, PC-394's former boundary `u<=3` disappears entirely.

## 1. Exact Schur factorization inherited from PC-391/PC-394

At the successive primorial step `P_p -> qP_p`, let

\[
S=R_q(H),
\qquad
T=qR_p(H/q)=\{t_1,\ldots,t_k\}
\tag{3}
\]

be the surviving and simultaneously deleted sets. Write

\[
B=(b_{ai})_{a\in S,\,i\le k},
\qquad
d_i:=\sum_{a\in S}b_{ai},
\qquad
D:=\operatorname{diag}(d_i),
\tag{4}
\]

for the survivor-to-deleted conductances and let `K` be the weighted Laplacian of the graph induced on `T`.

PC-394 rewrote the exact higher-boundary correction as

\[
\Delta_T=PQP^\top,
\qquad
P:=BD^{-1},
\qquad
Q:=D-D(D+K)^{-1}D,
\tag{5}
\]

with

\[
\boxed{0\preceq Q\preceq K.}
\tag{6}
\]

Every column `p_i` of `P` is a probability vector on `S`:

\[
p_{ai}=\frac{b_{ai}}{d_i}\ge0,
\qquad
\sum_{a\in S}p_{ai}=1.
\tag{7}
\]

Thus `||P||_1=1`. PC-394 bounded `||Delta_T||` by `tr K`; the improvement below is to control the **row overlap** of these normalized incidence profiles before applying the much smaller operator norm of `K`.

## 2. Jacobsthal covering bounds every normalized incidence profile

Let `J(q)` be the maximal gap in the set of integers with no prime factor `<=q`, equivalently the Jacobsthal gap for the primorial through `q`. Every interval of length `J(q)` contains a `q`-rough integer.

For every deleted point `t_i in T`, there is therefore a survivor `s_i in S` satisfying

\[
|s_i-t_i|\le J(q).
\tag{8}
\]

Indeed, if `t_i>J(q)`, apply the defining covering property to the interval immediately to the left of `t_i`; the resulting `q`-rough integer is positive and at most `t_i<=H`, hence lies in `S`. If `t_i<=J(q)`, the anchor `1 in S` already gives (8).

For the normalized regularized inverse-power chord kernel of PC-390--PC-394,

\[
\kappa_M(d)
=M^{-2\alpha}
\left[2\left(\cosh\frac{\tau}{M}-\cos\frac{2\pi d}{M}\right)\right]^{-\alpha},
\tag{9}
\]

uniform local-arc asymptotics give, whenever `H=o(M)`,

\[
c_{\alpha,\tau}d^{-2\alpha}
\le \kappa_M(d)
\le C_{\alpha,\tau}d^{-2\alpha}
\qquad(1\le d\le H)
\tag{10}
\]

for all sufficiently large conductors. From (8)--(10),

\[
d_i
=\sum_{a\in S}\kappa_M(|a-t_i|)
\ge c_{\alpha,\tau}J(q)^{-2\alpha}.
\tag{11}
\]

On the other hand `d_i>=b_{ai}` for every individual survivor `a`. Hence, putting `r=|a-t_i|>=1`,

\[
\boxed{
p_{ai}
\le
\min\!\left\{1,
C_{\alpha,\tau}\left(\frac{J(q)}r\right)^{2\alpha}
\right\}.}
\tag{12}
\]

This is the local fact absent from the deletion-count estimate of PC-394: a normalized deleted-star profile can be broad only when the corresponding deleted point sits in a long `q`-rough gap, and the worst such width is controlled by the Jacobsthal function.

## 3. `q`-separation turns Jacobsthal width into a Bessel bound

Distinct deleted points are multiples of `q`, so

\[
|t_i-t_j|=q|r_i-r_j|\ge q
\qquad(i\ne j).
\tag{13}
\]

Fix a survivor `a`. For any `q`-separated subset of the line and any `J>0`, elementary packing gives, when `2 alpha>1`,

\[
\sum_i
\min\!\left\{1,
C\left(\frac{J}{|a-t_i|}\right)^{2\alpha}
\right\}
\ll_{\alpha,C}1+\frac Jq.
\tag{14}
\]

To see this, there are only `O(1+J/q)` centers within distance `J`. Outside that interval, grouping centers into `q`-sized distance shells gives a tail bounded by

\[
\left(\frac Jq\right)^{2\alpha}
\sum_{m\ge J/q}m^{-2\alpha}
=O_\alpha\!\left(1+\frac Jq\right),
\tag{15}
\]

where summability is exactly the condition `alpha>1/2`.

Applying (14) to (12) yields

\[
\boxed{
\|P\|_\infty
=
\max_{a\in S}\sum_i p_{ai}
\ll_{\alpha,\tau}1+\frac{J(q)}q.
}
\tag{16}
\]

Since `||P||_1=1`, the standard induced-norm inequality gives

\[
\boxed{
\|P\|_2^2
\le \|P\|_1\|P\|_\infty
\ll_{\alpha,\tau}1+\frac{J(q)}q.
}
\tag{17}
\]

Thus the many normalized star profiles cannot synthesize coherently with norm proportional to their cardinality. Their possible overlap is controlled instead by the **largest local survivor gap**.

## 4. The internal deleted Laplacian is uniformly small in operator norm

The same `q`-separation gives an operator rather than trace bound for `K`. For each deleted vertex,

\[
\sum_{j\ne i}c_{ij}
\le
C_{\alpha,\tau}q^{-2\alpha}
\sum_{h\ge1}2h^{-2\alpha}
\ll_{\alpha,\tau}q^{-2\alpha},
\tag{18}
\]

again because `alpha>1/2`. A weighted graph Laplacian has spectral norm at most twice its maximum weighted degree, so

\[
\boxed{
\|K\|_{\rm op}
\ll_{\alpha,\tau}q^{-2\alpha}.
}
\tag{19}
\]

Combining (5)--(6), (17), and (19),

\[
\begin{aligned}
\|\Delta_T\|_{\rm op}
&\le \|P\|_2^2\,\|Q\|_{\rm op}\\
&\le \|P\|_2^2\,\|K\|_{\rm op}\\
&\ll_{\alpha,\tau}
\left(1+\frac{J(q)}q\right)q^{-2\alpha},
\end{aligned}
\tag{20}
\]

which is (1). Notice that neither `k=|T|` nor `H` occurs in the final estimate.

## 5. Iwaniec's Jacobsthal bound removes the long-window loophole

Iwaniec proved by the linear sieve that the maximal Jacobsthal gap satisfies

\[
\boxed{J(w)\ll w^2.}
\tag{21}
\]

Banks, Ford, and Tao explicitly restate this bound in their 2023 treatment of interval sieves and large prime gaps. Substituting (21) into (20) gives

\[
\boxed{
\|\Delta_T\|_{\rm op}
\ll_{\alpha,\tau}
q^{1-2\alpha}
\to0
\qquad(\alpha>1/2).
}
\tag{22}
\]

This is uniform in the number of simultaneous deletions and in the window length as long as the chord kernel remains in its local-arc regime `H=o(M)`. In the fixed-polynomial setting `H=p^u`, that condition is automatic because the primorial conductor grows faster than every fixed power of `p`.

For `1<u<=2`, the successive primorial step already has only one deleted rough point eventually, so `Delta_T=0` exactly as in PC-390/PC-391. For every fixed `u>2`, (22) now supplies the missing conclusion. Hence

\[
\boxed{
\text{for every fixed }u>1\text{ and every }\alpha>1/2,
\quad
\|\Delta_T\|_{\rm op}\to0.
}
\tag{23}
\]

For inverse-square chords (`alpha=1`) the rate supplied by the unconditional Jacobsthal bound is `O(q^{-1})`. The former PC-394 proof boundary at `u=3` was therefore an artifact of replacing the operator norm of the deleted-layer Laplacian by its trace.

By Weyl's inequality, every ordered eigenvalue of the true Kron response and the independent-star baseline differs by `o(1)`. Thus **no fixed polynomial window, however long, can resurrect an order-one unscaled outlier from the irreducible mutual coupling of the simultaneously deleted layer in the summable positive inverse-power phase**.

## 6. Prior-art and novelty audit

All abstract ingredients are classical. Kron reduction is Schur complementation of graph Laplacians; Dörfler and Bullo are already the line's general source anchor. The estimate `||K||<=2 d_max`, the induced-matrix inequality `||P||_2^2<=||P||_1||P||_infinity`, and the packing estimate for an integrable one-dimensional tail are standard linear-algebra/analysis facts.

The arithmetic input is also classical rather than a new prime-gap theorem. Henryk Iwaniec, *On the problem of Jacobsthal*, Demonstratio Mathematica 11:1 (1978), 225--232, DOI `10.1515/dema-1978-0121`, obtains the linear-sieve Jacobsthal bound underlying (21). William Banks, Kevin Ford, and Terence Tao, *Large prime gaps and probabilistic models*, Inventiones Mathematicae 233 (2023), 1471--1518, DOI `10.1007/s00222-023-01199-0`, Section 2.3, define `J(w)` as the maximal gap between integers with no prime factor `<=w` and explicitly record Iwaniec's `J(w)\ll w^2` bound.

I found no indication that the particular Jacobsthal-gap/Kron-incidence combination (12)--(22) is an established graph-spectral theorem, but no general novelty is claimed for its components. The project-specific mathematical delta is precise: **the one remaining longer-window loophole in PC-394 disappears because local rough-number covering bounds the normalized incidence overlap, while `q`-spacing bounds the deleted-layer Laplacian itself**. This is a Prime-Circle boundary/no-go result, not a new theorem about Jacobsthal's function or Kron reduction.

The appearance of Jacobsthal/interval-sieve theory also does not itself provide a zeta mechanism. Banks--Ford--Tao discuss deep links between interval sieves and exceptional Dirichlet zeros, but (22) uses only the unconditional coarse upper bound (21); importing sharper zero-sensitive gap information would merely improve an already vanishing upper bound in this positive summable branch.

## 7. Boundaries and falsification tests

The argument requires positivity of the survivor/deleted conductances, the exact Schur factorization (5), and a kernel with a summable one-dimensional tail `d^{-2 alpha}`. It therefore does not cover `alpha<=1/2`, signed or indefinite interactions, nonlinear elimination, or a state space not exhausted by the graph-Laplacian Schur response.

The conclusion is about **unscaled** operator norm. Multiplying `Delta_T` by a diverging source-justified factor can retain a nonzero limit, and the orientation/evolution of the thin contrast subspace across refinement levels is not addressed. Nor does (22) say that the full response `L_red-L_S` vanishes: the independent one-vertex star baseline can remain full rank and order one.

The finite-dimensional part is directly falsifiable. For any refinement step construct `S,T,B,D,K`, form `P=BD^{-1}` and `Q=D-D(D+K)^{-1}D`, and verify (5)--(6). Separately compute the maximal `q`-rough gap covering the deleted locations and check the row-overlap estimate (16). A counterexample with a positive inverse-power kernel for which the normalized incidence row sum grows faster than `1+J(q)/q`, or for which the `q`-separated deleted Laplacian violates (19), would invalidate the new step. The asymptotic conclusion would fail if the classical bound `J(q)\ll q^2` were unavailable or if the geometry left the local-arc regime.

## Consequence for the research line

PC-394's remaining positive summable-tail escape `u>1+2 alpha` is now closed for unscaled exceptional eigenvalues. Longer fixed polynomial windows do not change the answer: the irreducible simultaneous-deletion Kron correction tends to zero in operator norm for every `alpha>1/2`.

Accordingly, this branch should no longer spend effort extending the positive summable linear-Kron model merely by increasing the primorial window. Surviving directions must change an actual hypothesis or observable: nonsummable tails (`alpha<=1/2`), a source-forced renormalized exceptional observable, cross-level orientation/transport of the contrast subspaces, signed/indefinite structure, nonlinear response, or geometric/state information not captured by positive Schur elimination. Nothing in this result supplies a zeta zero, functional-equation symmetry, critical-line selector, or Hilbert--Polya operator.