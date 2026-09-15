# FD-146 — Anchor connectivity alone does not control normalized ancestry energy

- **Date:** 2026-09-15
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** main-track quantitative no-go theorem / anchored-energy obstruction
- **Depends on:** FD-135, FD-144, FD-145

## Claim

FD-145 shows that ancestry-defect observations cannot recover absolute Möbius orientation on a component disconnected from an anchor. Restoring connectivity removes that exact `Z_2` gauge, but connectivity by itself is still not a quantitative coercivity statement.

Let

\[
V_T=\{n\le T:\mu^2(n)=1\}
\tag{1}
\]

and let `E_T` be the full squarefree ancestry graph up to `T`: an oriented edge `n -> pn` belongs to `E_T` whenever `n,pn in V_T` and `p` is prime. The underlying graph is connected and every vertex is connected to the anchored vertex `1` by repeatedly deleting prime factors.

Fix `R_0>=1` and use the same one-wall source as FD-145,

\[
a_n=0\quad(\mu(n)=0),
\qquad
 a_n=\mu(n)b(n)\quad(\mu^2(n)=1),
\tag{2}
\]

where

\[
b(n)=
\begin{cases}
+1,&\omega(n)\le R_0,\\
-1,&\omega(n)>R_0.
\end{cases}
\tag{3}
\]

Then the full graph includes the anchor and **every** ancestry bridge; there is no disconnected observed component. Nevertheless, for every fixed `1<=q<infinity`, the uniformly normalized ancestry defect satisfies

\[
\boxed{
\left(
\frac1{|E_T|}
\sum_{(n,pn)\in E_T}|a_{pn}+a_n|^q
\right)^{1/q}
\ll_{R_0,q}
\left(
\frac{(\log\log T)^{R_0}}{\log T}
\right)^{1/q}
\longrightarrow0,
}
\tag{4}
\]

while the uniformly normalized coefficient error satisfies

\[
\boxed{
\left(
\frac1{|V_T|}
\sum_{n\in V_T}|a_n-\mu(n)|^q
\right)^{1/q}
\longrightarrow2.
}
\tag{5}
\]

Thus **small finite-`L^q` ancestry energy on a fully anchor-connected graph does not force coefficient proximity to Möbius**. The obstruction left after FD-145 is quantitative: the anchor can be connected through a boundary whose normalized edge exposure tends to zero.

Equivalently, any anchored Poincare-type inequality with uniform vertex and edge normalization,

\[
\left(
\frac1{|V_T|}\sum_{n\in V_T}|b(n)-1|^q
\right)^{1/q}
\le
C_q(T)
\left(
\frac1{|E_T|}\sum_{(n,pn)\in E_T}|b(pn)-b(n)|^q
\right)^{1/q},
\tag{6}
\]

must have

\[
\boxed{
C_q(T)
\gg_{R_0,q}
\left(
\frac{\log T}{(\log\log T)^{R_0}}
\right)^{1/q}.
}
\tag{7}
\]

The exact exponent in (7) is not asserted to be optimal. The point is that the coercivity constant necessarily diverges even though the observed ancestry graph is connected to the anchor and contains all local edges.

## 1. The full ancestry graph is anchored

Every `m in V_T`, `m>1`, can be written `m=pn` with `p|m` prime and `n=m/p`. Since `m` is squarefree, `p` does not divide `n`, and since `n<m<=T`, both endpoints belong to `V_T`. Repeating this operation reaches `1`.

Hence the underlying graph of `(V_T,E_T)` is connected. In particular, unlike FD-145's rank-truncated observation domain, no high-rank component is separated from the Möbius anchor.

The graph also has at least a linear number of edges. Choose one prime divisor `p(m)` for each `m in V_T\{1}` and assign to `m` the edge

\[
(m/p(m),m).
\tag{8}
\]

Different children `m` give different edges, so

\[
|E_T|\ge |V_T|-1.
\tag{9}
\]

The classical squarefree-counting asymptotic gives

\[
|V_T|\sim \frac{T}{\zeta(2)},
\tag{10}
\]

and therefore `|E_T| >> T`.

## 2. All defect energy sits on one finite-rank wall

For a squarefree parent `n` and `p\nmid n`, FD-145's exact identity is

\[
a_{pn}+a_n
=\mu(n)\bigl(b(n)-b(pn)\bigr).
\tag{11}
\]

Multiplication by `p` raises `omega` by one. Hence

\[
|a_{pn}+a_n|
=
\begin{cases}
2,&\omega(n)=R_0,\\
0,&\omega(n)\ne R_0.
\end{cases}
\tag{12}
\]

Let

\[
Q_k(T)=\#\{m\le T:\mu^2(m)=1,\ \omega(m)=k\}.
\tag{13}
\]

Every crossing edge has a child `m` with `omega(m)=R_0+1`. Conversely, each such child has exactly `R_0+1` prime divisors, and deleting any one of them gives a distinct parent of rank `R_0`. Therefore the number `B_T` of nonzero-defect edges is exactly

\[
B_T=(R_0+1)Q_{R_0+1}(T).
\tag{14}
\]

For fixed `k`, Landau's fixed-rank almost-prime estimate in its squarefree form gives

\[
Q_k(T)
\asymp_k
\frac{T(\log\log T)^{k-1}}{\log T},
\tag{15}
\]

and only the corresponding upper bound is needed here. Thus

\[
B_T
\ll_{R_0}
\frac{T(\log\log T)^{R_0}}{\log T}.
\tag{16}
\]

Combining (9), (10), and (16),

\[
\boxed{
\frac{B_T}{|E_T|}
\ll_{R_0}
\frac{(\log\log T)^{R_0}}{\log T}
\longrightarrow0.
}
\tag{17}
\]

So the anchor bridge is present, but its share of the full local ancestry energy vanishes.

## 3. Vanishing edge energy coexists with macroscopic coefficient error

By (12), every nonzero edge defect has magnitude exactly `2`. Therefore for every fixed finite `q>=1`,

\[
\begin{aligned}
\frac1{|E_T|}
\sum_{(n,pn)\in E_T}|a_{pn}+a_n|^q
&=2^q\frac{B_T}{|E_T|},
\end{aligned}
\tag{18}
\]

which together with (17) proves (4).

The coefficient side behaves oppositely. The source differs from Möbius exactly on the high-rank set

\[
H_T=\{n\in V_T:\omega(n)>R_0\}.
\tag{19}
\]

For fixed `R_0`, Landau's estimate gives

\[
|V_T\setminus H_T|
\le
1+\sum_{k=1}^{R_0}Q_k(T)
=o(T).
\tag{20}
\]

Together with (10), this implies

\[
\frac{|H_T|}{|V_T|}\longrightarrow1.
\tag{21}
\]

On `H_T`, `a_n=-mu(n)` and hence `|a_n-mu(n)|=2`; off `H_T` the difference is zero. Consequently

\[
\frac1{|V_T|}\sum_{n\in V_T}|a_n-\mu(n)|^q
=2^q\frac{|H_T|}{|V_T|}
\longrightarrow2^q,
\tag{22}
\]

which proves (5).

Substituting the same `b` into (6) proves the lower bound (7) for any possible uniform anchored coercivity constant.

## 4. What FD-146 adds beyond FD-145

FD-145 is an **exact connectivity obstruction**. If the visible graph starts above the rank wall, every observed raw defect is exactly zero and the high-rank component has a free global orientation.

FD-146 deliberately restores everything that obstruction asked for: the vertex `1` is present, every coefficient is connected to it, every local ancestry edge is retained, and the rank-wall bridges themselves are observed. The exact gauge is therefore gone. A pointwise observer can detect the source immediately by looking at any wall edge.

What fails is the stronger inference

\[
\text{small normalized local ancestry energy}
\quad\Longrightarrow\quad
\text{small normalized coefficient error}.
\tag{23}
\]

The wall has full pointwise amplitude but asymptotically negligible mass. Connectivity is a qualitative property; stability needs a quantitative lower bound on how much normalized observation weight every macroscopic orientation change must cross.

This also separates FD-146 from FD-144. FD-144 limits how many arbitrary source-independent tests can be coercive in high rank. Here there is no sparse test family at all: we average over the **entire** squarefree ancestry graph. The failure comes from the normalization of a bottleneck, not from an insufficient number of sampled relations.

## 5. Matched controls and limits

The theorem does not say that full ancestry data are information-theoretically insufficient. They are sufficient: because the graph is connected and the anchor is fixed, exact knowledge of every raw edge defect exposes the wall. In particular,

\[
\max_{(n,pn)\in E_T}|a_{pn}+a_n|=2.
\tag{24}
\]

Thus the finite-`L^q` restriction in (4) is essential. The `L^infinity` observable does not decay.

Likewise, a source-independent weighting that deliberately assigns nonvanishing total mass to the rank-`R_0` wall defeats this particular construction. More generally, for any nonnegative edge weights, the same source is invisible in normalized finite-`L^q` energy exactly to the extent that the total normalized weight of the wall tends to zero. FD-146 therefore identifies the quantity that must be audited rather than claiming that every possible weighting fails.

Direct coefficient samples also defeat the source, and a genuinely nonlocal Farey/Fourier functional may couple the two orientations without reducing to normalized local edge energy. No no-go claim is made for such destination-side observables.

Finally, the construction is one fixed infinite source. If a finite squarefree seed is prescribed, choose `R_0` larger than the maximum `omega(n)` in that seed. Then (2)--(3) agree with Möbius on the entire seed while all conclusions above remain unchanged.

## 6. Prior-art and source audit

The abstract lesson that connectivity alone does not provide a uniform Poincare or spectral coercivity constant is standard graph analysis; no novelty is claimed there. The Mathia-specific content is the explicit arithmetic realization inside the **full squarefree Möbius ancestry graph**: one fixed finite-rank orientation wall has boundary

\[
O_{R_0}\!\left(
\frac{T(\log\log T)^{R_0}}{\log T}
\right)
\tag{25}
\]

while separating a coefficient set of asymptotic squarefree density one from the anchor.

The only asymptotic inputs are already anchored in `SOURCES.md`: the squarefree counting law and Wright's version of Landau's fixed-`k` almost-prime theorem. No new external theorem is load-bearing, so no source update is required.

## 7. Falsifiable next test

The immediate coefficient-side question should strengthen **anchor connectivity** to a quantitative exposure condition. For an ancestry/Farey functional proposed as coercive, identify the induced vertex and edge normalizations and ask whether every set carrying macroscopic coefficient mass but excluding the anchor must have a boundary carrying nonvanishing observation mass.

A concrete positive target is an anchored inequality of the form

\[
\|b-1\|_{L^q(V_T,\nu_T)}
\le C
\|\nabla b\|_{L^q(E_T,\eta_T)}
\tag{26}
\]

with `C` independent of `T` for the **source-native weights** `(nu_T,eta_T)` actually produced by the Farey/Franel skeleton. FD-146 shows that the naive uniform normalization cannot have such a constant.

A concrete falsifier of the present obstruction would be to derive from the physical Farey/Fourier energy a source-independent edge weighting for which every fixed rank wall receives a nonvanishing fraction of total coercive mass, while the weighting still controls the desired discrepancy norm. Such a result would explain how the arithmetic observable transports the anchor quantitatively rather than merely graph-theoretically.

## Conclusion

FD-145 established that an unanchored ancestry component has an exact orientation gauge. FD-146 shows that removing that gauge is only the first step. On the complete squarefree ancestry graph, every vertex is connected to the Möbius anchor and every bridge is visible, yet one fixed seed-compatible source satisfies

\[
\boxed{
\text{normalized finite-}L^q\text{ ancestry defect}\to0,
\qquad
\text{normalized coefficient error}\to2.
}
\tag{27}
\]

The next coercive resource is therefore not connectivity alone but **quantitative anchor exposure under the source-native normalization**. Only after that survives the rank-wall control does the observation-budget question of FD-144 become the relevant next bottleneck.