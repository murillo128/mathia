# NB-017 — all-depth compressed enrichment has rough-core reciprocal blind modes

**Status:** `EXACT-DERIVED + ALL-DEPTH-QUOTIENT-GRAPH + RECIPROCAL-BLIND-MODES + ROUGH-CORE-DECOMPOSITION + NEGATIVE/METHOD-BOUNDARY`. `NB-016` identifies the compressed enrichment frame with a multiplication-table support operator when `2<=M<=N`. The restriction `M<=N` is not needed to expose the underlying finite geometry. At arbitrary depth `M>=2`, the quotient channel is the rooted incidence operator of a finite multiplicative graph. Its kernel is described exactly by connected components, and the corresponding invisible future residual pairings are reciprocal profiles `q_k=c/k` on those components.

This extends the source-independent obstruction to the full diagonal corridor used by `NB-015`. Taking `M>N` can connect many multiplication-table holes, but it cannot make the quotient frame coercive on the whole new section: multiplication by old indices preserves the part of an integer supported on primes larger than `N`, so distinct `N`-rough cores can never communicate. In particular the compressed frame is singular for every `N>=2` and `M>=2`.

Let

\[
V_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
r_N=e-P_Ne,
\qquad
W_{N,M}=V_{MN}\ominus V_N,
\tag{1}
\]

and retain

\[
F_{N,M}=\sum_{m=2}^M A_mP_NA_m^*,
\qquad
C_{N,M}=P_{W_{N,M}}F_{N,M}P_{W_{N,M}}.
\tag{2}
\]

For `N<k<=MN` put

\[
h_k=(I-P_N)g_k,
\qquad z_k=k h_k,
\tag{3}
\]

and use the convention `h_k=z_k=0` when `k<=N`. As in `NB-016`, the future vectors `h_(N+1),...,h_(MN)` form a basis of `W_(N,M)`.

Define a finite rooted multigraph `Gamma_(N,M)` with vertex set

\[
\{\ast\}\cup\{N+1,\ldots,MN\}.
\tag{4}
\]

For every `2<=m<=M` and `2<=j<=N` with `mj>N`, add an edge

\[
\begin{cases}
\ast\longleftrightarrow mj,&m\le N,\\
m\longleftrightarrow mj,&m>N.
\end{cases}
\tag{5}
\]

Parallel rooted edges are harmless. Let `c_(N,M)` denote the number of connected components of `Gamma_(N,M)` that do **not** contain the root.

Then

\[
\boxed{
\operatorname{rank}C_{N,M}=N(M-1)-c_{N,M},
\qquad
\dim\ker C_{N,M}=c_{N,M}.
}
\tag{6}
\]

There is an equally explicit target-aware form. For `2<=k<=MN` define

\[
q_k:=\langle r_N,g_k\rangle,
\qquad
s_k:=kq_k,
\tag{7}
\]

so the normal equations give `q_k=s_k=0` for `k<=N`. Then the visible defect of `NB-014`--`NB-015` satisfies

\[
\boxed{
\mathcal J_{N,M}=0
\iff
s\text{ is }0\text{ on the rooted component and constant on every unrooted component.}
}
\tag{8}
\]

Equivalently, the invisible future-pairing profiles are exactly

\[
\boxed{
q_k=\frac{a_{\mathcal C}}{k}
\quad(k\in\mathcal C)
}
\tag{9}
\]

with one free scalar `a_C` for each unrooted component `C`, and `q_k=0` on the root component. Thus the generic blind directions are not arbitrary after the all-depth channels are added: they are componentwise copies of the target semigroup character `k^{-1}`.

Finally define the `N`-rough core

\[
\mathfrak r_N(k):=
\prod_{p>N}p^{v_p(k)}.
\tag{10}
\]

It is constant along every edge of `Gamma_(N,M)`, while the root component has rough core `1`. Consequently

\[
\boxed{
c_{N,M}\ge
\#\{r:N<r\le MN,\ p\mid r\Rightarrow p>N\}
\ge \pi(MN)-\pi(N).
}
\tag{11}
\]

Bertrand's postulate gives `pi(MN)-pi(N)>=1` for every `N>=2`, `M>=2`; hence

\[
\boxed{\ker C_{N,M}\ne\{0\}\quad\text{for every }N>=2,\ M>=2.}
\tag{12}
\]

The live problem is therefore stricter than finding a depth where the compressed frame becomes source-independently coercive. No such depth exists. Any successful continuation of the `NB-015` visibility budget must show that the **actual Nyman residual pairings** have enough edgewise variation across this multiplicative graph, or enough mass in its nonzero generalized eigenspaces, to defeat the reciprocal blind profiles.

## 1. The all-depth quotient channel is a rooted incidence operator

The exact Bagchi-space dilation identity used in `NB-014` and `NB-016` is

\[
A_mg_j=\sqrt m\,(g_{mj}-j^{-1}g_m).
\tag{13}
\]

For `2<=m<=M` set

\[
B_m:=P_{W_{N,M}}A_m|_{V_N}.
\tag{14}
\]

Compression of (13) gives, without assuming `m<=N`,

\[
B_mg_j
=\sqrt m\,(h_{mj}-j^{-1}h_m).
\tag{15}
\]

If `mj<=N`, then necessarily `m<=N` and both terms vanish. If `mj>N`, equation (3) turns (15) into

\[
\boxed{
B_mg_j
=\frac{\sqrt m}{mj}
\begin{cases}
z_{mj},&m\le N,\\
z_{mj}-z_m,&m>N.
\end{cases}}
\tag{16}
\]

These are precisely nonzero scalar multiples of the rooted edge-incidence vectors in (5), written in the basis `{z_k}` of the quotient. Moreover

\[
C_{N,M}=\sum_{m=2}^M B_mB_m^*.
\tag{17}
\]

For a finite family of operators, the range of the positive sum `sum B_mB_m^*` equals the sum of the ranges of the `B_m`. Therefore `Ran C_(N,M)` is exactly the span of all root-deleted incidence vectors of `Gamma_(N,M)`.

A rooted incidence matrix has one independent relation for each connected component not containing the root. More explicitly, a component containing `r` future vertices and the root contributes rank `r`; an unrooted component containing `r` future vertices contributes rank `r-1`. Since the graph has

\[
MN-N=N(M-1)
\tag{18}
\]

future vertices, summing componentwise proves (6).

When `M<=N`, every channel source `m` belongs to the old section, so every nonzero edge is rooted. Each future vertex that occurs as a product `mj` lies in the root component and every other future vertex is isolated. Thus (6) reduces exactly to the multiplication-support rank formula of `NB-016`. The graph formulation is therefore an extension of that result rather than a competing coordinate description.

## 2. The actual visible defect is a weighted multiplicative Dirichlet energy

The graph also controls the source-aware statistic, not only the rank of an abstract operator. Let `G_N` be the Gram matrix of `g_2,...,g_N`; it is positive definite because these generators are linearly independent. For each `m` define the old-indexed vector

\[
(v_m)_j:=q_{mj}-j^{-1}q_m
=\frac{s_{mj}-s_m}{mj},
\qquad 2\le j\le N,
\tag{19}
\]

where `q_m=s_m=0` when `m<=N`. The equality on the right uses `s_k=kq_k` and remains valid in both the rooted and unrooted cases.

Because `A_m` is an isometry, the family `A_mg_2,...,A_mg_N` has Gram matrix `G_N`. Equation (13) gives

\[
\langle r_N,A_mg_j\rangle
=\sqrt m\,(v_m)_j.
\tag{20}
\]

The projection formula therefore yields

\[
\|P_{A_mV_N}r_N\|^2
=m\,v_m^*G_N^{-1}v_m.
\tag{21}
\]

Since `P_Nr_N=0`, the scalar character term in `D_m=A_m^*-m^{-1/2}I` disappears after projection and

\[
\|P_ND_mr_N\|^2
=\|P_{A_mV_N}r_N\|^2.
\tag{22}
\]

Hence the visible defect has the exact all-depth factorization

\[
\boxed{
\mathcal J_{N,M}
=\sum_{m=2}^M
m\,v_m^*G_N^{-1}v_m.
}
\tag{23}
\]

This is a positive weighted Dirichlet energy on the multiplicative graph, with the within-channel metric supplied by `G_N^{-1}` rather than by a diagonal edge norm. Positivity of `G_N^{-1}` implies

\[
\mathcal J_{N,M}=0
\iff
v_m=0\text{ for every }m
\iff
s_{mj}=s_m\text{ on every unrooted edge and }s_{mj}=0\text{ on every rooted edge}.
\tag{24}
\]

That is exactly the component condition (8), and division by `k` gives (9).

There is no conflict with the quotient-kernel statement. If

\[
u_{N,M}=P_{MN}r_N=r_N-r_{MN}\in W_{N,M},
\tag{25}
\]

then `q_k=<u_(N,M),h_k>` for every future index. Since the Gram matrix of the `h_k` basis is invertible, future-pairing coordinates and quotient-vector coordinates are in bijection. Equations (6) and (8) are the same kernel seen respectively in primal quotient coordinates and target-residual pairing coordinates.

## 3. Rough cores prevent all-depth generic coercivity

The graph has a simple arithmetic invariant that is invisible in the `M<=N` multiplication-table picture. Multiplying an integer by `j<=N` cannot introduce a prime factor larger than `N`. Therefore, for every unrooted edge `m<->mj`,

\[
\mathfrak r_N(mj)=\mathfrak r_N(m).
\tag{26}
\]

For a rooted edge, both `m<=N` and `j<=N`, so every prime factor of `mj` is at most `N` and

\[
\mathfrak r_N(mj)=1.
\tag{27}
\]

Thus `mathfrak r_N` is constant on graph components if the root is assigned core `1`. Every integer `r` in `(N,MN]` all of whose prime factors exceed `N` is itself an `N`-rough core. Distinct such integers cannot lie in the same component, and none can lie in the root component. This proves the first inequality in (11). Primes in `(N,MN]` are a subset of those rough integers, proving the second.

The consequence is qualitative but exact. Increasing `M` beyond `N` creates non-root edges and can merge some of the isolated holes from `NB-016`, yet it never merges different rough-core sectors. Bertrand supplies a prime in `(N,2N)`; because `2N<=MN`, at least one unrooted sector survives at every allowed depth, proving (12).

The dimension lower bound (11) is deliberately not converted here into an asymptotic rank-density statement for general `M=M(N)`. Depending on the growth corridor, counting `N`-rough integers is a separate sieve problem, and kernel dimension alone still does not control the top frame eigenvalue or the actual residual's alignment. The exact invariant is the durable point needed by the Nyman visibility question.

## 4. Consequence for the scale-coupled visibility budget

`NB-015` shows that under a hypothetical nonzero limiting residual, every admissible nested path must satisfy

\[
\sum_k
\frac{\rho_{N_k,M_k}\log M_k}
{\beta_{N_k,M_k}}<\infty,
\qquad
\beta_{N,M}=\|C_{N,M}\|.
\tag{28}
\]

`NB-016` already ruled out a generic lower-frame argument at `M=N` by showing asymptotic multiplication-table rank sparsity. Equations (6)--(12) close the obvious escape of moving to `M>N`: **there is no finite depth at which `C_(N,M)` becomes positive definite on the full quotient**.

This does not imply that `rho_(N,M)` is small for the actual residual. The source could force its quotient component away from the kernel even when the kernel is large. What changes is the theorem that would be needed. A source-specific visibility estimate can now be formulated as a quantitative failure of the residual field

\[
s_k=k\langle r_N,g_k\rangle
\tag{29}
\]

to become approximately constant on the unrooted multiplicative components while vanishing approximately on the rooted component. The normal equations anchor the old section at zero; the new arithmetic work is to show that the future target-residual field cannot shadow the reciprocal blind profiles too efficiently along a controlled growth path.

This is genuinely different from adding more positive normal-equation channels. `NB-012`--`NB-013` already saturate that amplification architecture. Here the remaining quantity is an edge variation of future target-aware pairings after the old projection has been removed.

## 5. Prior-art boundary and falsification controls

The analytic inputs are the same canonical ones already anchored in this line: Bagchi's dilation-semigroup model and the finite Nyman projection geometry developed in `NB-014`--`NB-016`. The incidence-rank statement itself is elementary finite graph linear algebra, and Bertrand's postulate is classical. No new specialized external theorem is load-bearing, so `SOURCES.md` does not change.

A targeted prior-art check searched Nyman--Beurling finite sections, dilation-semigroup formulations, multiplicative graph/incidence formulations, Dirichlet-energy descriptions, generalized Nyman approximation, and recent multiscale Gram work. The located literature includes Bagchi's semigroup formulation, generalized polynomial approximation results, numerical finite-section studies, and recent Gram-decay/block-compressibility work, but no located source identified the compressed Nyman enrichment operator with the rooted graph (5) or its componentwise reciprocal blind profiles (9). Search absence is not a novelty proof; the evidence label here is `EXACT-DERIVED`, not a claim of literature priority.

Several boundaries are load-bearing:

- `C_(N,M)` being singular does **not** imply `beta_(N,M)=||C_(N,M)||` is small. Kernel, rank and top eigenvalue are distinct.
- The reciprocal profiles (9) characterize the zero-visible-defect subspace in future-pairing coordinates. They do not assert that the actual residual realizes a nonzero blind profile.
- Rough-core separation gives a lower bound on kernel dimension, not an upper bound on the source-visible fraction `rho_(N,M)`.
- Approximate blindness requires quantitative control in the `G_N^{-1}` channel metric of (23), not merely small pointwise differences of `s_k`.
- No closure, approximation-rate improvement, Möbius estimate, or zero-free statement follows from (6)--(12) alone.

The result is falsified by any counterexample to the all-depth compression formula (16), any graph component whose incidence span disagrees with `Ran C_(N,M)`, or any edge violating rough-core invariance. A positive continuation must instead exploit the actual source field (29): prove a quantitative anchored Poincaré/expansion estimate that remains valid for that field despite the exact reciprocal kernel, or derive another source-specific mechanism giving a divergent `NB-015` visibility budget.