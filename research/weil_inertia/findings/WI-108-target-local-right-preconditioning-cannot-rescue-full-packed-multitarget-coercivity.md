# WI-108 — Target-local right preconditioning cannot rescue full-packed multitarget coercivity

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It closes an escape left explicitly open by WI-107: replacing each full-packed target block by an arbitrary target-local linear reweighting or internal right preconditioner cannot restore a uniform relative source coercivity. The obstruction is invariant under arbitrary block-diagonal right processing, including nonscalar diagonal weights, invertible changes of target basis, and singular target-side compressions.

More precisely, let

\[
A_j:H_j\to H,
\qquad
K_j=\ker A_j^*\subset H
\qquad(1\le j\le J),
\tag{1}
\]

and suppose unit vectors `x_j in K_j` are available. Write

\[
\delta_{ij}=\operatorname{dist}(x_i,K_j).
\tag{2}
\]

For completely arbitrary finite-dimensional linear maps

\[
C_j:E_j\to H_j,
\tag{3}
\]

form the target-locally processed blocks and their horizontal concatenation

\[
\widetilde A_j=A_jC_j,
\qquad
\widetilde B=[\,\widetilde A_1\;\cdots\;\widetilde A_J\,].
\tag{4}
\]

If `\widetilde B` is full row rank, choose `i_*` so that

\[
\|\widetilde A_{i_*}\|_2=\max_j\|\widetilde A_j\|_2.
\tag{5}
\]

Then

\[
\boxed{
\frac{\sigma_{\min}(\widetilde B)}
     {\sigma_{\max}(\widetilde B)}
\le
\left(\sum_{j\ne i_*}\delta_{i_*j}^2\right)^{1/2}.
}
\tag{6}
\]

If `\widetilde B` is not full row rank, its source coercivity already vanishes, so the corresponding condition number is infinite. Thus arbitrary target-local right processing can only leave the WI-107 near-kernel obstruction unchanged or make it worse; it cannot remove it.

Applied to the simultaneous positive-defect full-packing family of WI-107, with source prime `p`, target primes

\[
p<q_1<\cdots<q_J<\frac{4p}{3},
\qquad
\Delta=q_J-q_1=O(J\log p),
\tag{7}
\]

and cross Grams

\[
G_j=(U_p^{(N)})^*U_{q_j}^{(N)},
\tag{8}
\]

the same order-three quotient-character witnesses satisfy uniformly in `i,j`

\[
\delta_{ij}^2\le \frac{3\Delta}{2p}.
\tag{9}
\]

Consequently, for **every** collection of target-local linear maps `C_j`, either

\[
[\,G_1C_1\;\cdots\;G_JC_J\,]
\tag{10}
\]

is source-rank deficient, or

\[
\boxed{
\frac{\sigma_{\min}([G_1C_1\;\cdots\;G_JC_J])}
     {\sigma_{\max}([G_1C_1\;\cdots\;G_JC_J])}
\le
\sqrt{\frac{3(J-1)\Delta}{2p}}.
}
\tag{11}
\]

Hence whenever

\[
J=o\!\left(\sqrt{\frac{p}{\log p}}\right),
\tag{12}
\]

one has uniformly over all such block-diagonal right preprocessing rules

\[
\boxed{
\kappa_2([G_1C_1\;\cdots\;G_JC_J])
=\Omega\!\left(\frac1J\sqrt{\frac{p}{\log p}}\right)
\longrightarrow\infty
}
\tag{13}
\]

whenever the processed concatenation retains full source row rank. The `C_j` may depend arbitrarily on `p,q_1,\ldots,q_J,N` and may be rectangular or singular.

## 1. The left-kernel obstruction survives every target-local right map

The key identity is purely finite-dimensional. Since

\[
\widetilde A_j^*=C_j^*A_j^*,
\tag{14}
\]

every original left-kernel vector remains a left-kernel vector after target-local right processing:

\[
\boxed{
K_j=\ker A_j^*\subseteq\ker(C_j^*A_j^*)
=\ker\widetilde A_j^*.
}
\tag{15}
\]

Equivalently, `ran(A_jC_j) subseteq ran(A_j)`. No invertibility assumption on `C_j` is needed. Singular compression enlarges the left kernel rather than repairing it.

Take the unit witness `x=x_{i_*}` from (5). Equation (15) gives

\[
\widetilde A_{i_*}^*x=0.
\tag{16}
\]

For every `j ne i_*`, let `P_j` be the orthogonal projection onto the **original** kernel `K_j`. Because `P_jx in K_j subseteq ker \widetilde A_j^*`,

\[
\begin{aligned}
\|\widetilde A_j^*x\|
&=\|\widetilde A_j^*(x-P_jx)\|\\
&\le \|\widetilde A_j\|_2\,\|x-P_jx\|\\
&=\|\widetilde A_j\|_2\,\delta_{i_*j}.
\end{aligned}
\tag{17}
\]

Therefore

\[
\begin{aligned}
\|\widetilde B^*x\|^2
&=\sum_{j\ne i_*}\|\widetilde A_j^*x\|^2\\
&\le \|\widetilde A_{i_*}\|_2^2
\sum_{j\ne i_*}\delta_{i_*j}^2.
\end{aligned}
\tag{18}
\]

The variational characterization of the smallest singular value and the trivial block lower bound for the largest singular value give

\[
\sigma_{\min}(\widetilde B)
\le\|\widetilde B^*x\|,
\qquad
\sigma_{\max}(\widetilde B)
\ge\|\widetilde A_{i_*}\|_2.
\tag{19}
\]

Combining (18)--(19) proves (6). This is the WI-107 common-near-kernel lemma with its only scalar-specific assumption removed.

## 2. Exact specialization to the WI-107 arithmetic family

WI-107 constructs infinitely many source primes `p`, clustered target primes `q_j`, and one common observation length `N` for which all pairwise interactions are genuinely positive-defect and exactly full packed. In common source coordinates the kernels contain normalized order-three quotient-character vectors `x_j` whose supports are nested exterior intervals. WI-107 proves exactly

\[
|\langle x_i,x_j\rangle|^2
=\frac{\min(t_i,t_j)}{\max(t_i,t_j)},
\qquad
t_j=2p-q_j,
\tag{20}
\]

and hence

\[
\operatorname{dist}(x_i,K_j)^2
\le \frac{|q_i-q_j|}{\max(t_i,t_j)}
\le \frac{3\Delta}{2p}.
\tag{21}
\]

The proof of WI-107 then used only one scalar weight per block. Equations (15)--(19) show that this restriction was unnecessary: after replacing `G_j` by **any** `G_jC_j`, the same `x_j` remain exact left-kernel witnesses and the same distance estimate (21) remains available. Substitution into (6) gives (11), and the clustered-prime estimate `Delta=O(J log p)` gives (13).

This also handles singular internal processing cleanly. Such a `C_j` may destroy source rank, in which case there is nothing left to prove; if the total concatenation nevertheless remains full row rank, (11) applies unchanged.

## 3. What this closes and what it does not

WI-107 explicitly left nonscalar diagonal weights and internal target preconditioners outside its scalar theorem. Those operations are now closed whenever they act separately inside each target block on the **right**. In particular, no choice of column-dependent weights, target-local change of basis, local whitening, local pseudoinverse/truncation, or other linear map `C_j` can manufacture a fixed relative source singular gap from the full-packed clustered family below the square-root target-count scale.

The boundary is equally important. A source-side left transformation changes the source geometry in which the kernels and their principal angles are measured, so it is not covered. Nor is a genuinely cross-target right transformation with off-diagonal blocks that mixes columns from different `G_j` before the coercivity test; such a map need not preserve any individual `K_j`. Unrestricted source whitening of an already full-row-rank concatenation can of course normalize its row Gram, so excluding those operations is not merely technical. Any analytic use of such a rescue must therefore justify why that source- or cross-target coupling is actually available from the Weil/Yang arithmetic rather than being an arbitrary post hoc preconditioner.

The result is also a uniform-algebraic obstruction, not an assertion that the specially synchronized CRT windows occur with positive zeta density. As in WI-105--WI-107, its role is to falsify coercivity theorems that claim to follow from the full-packed interface alone.

## 4. Prior art and novelty boundary

The inclusion `ran(AC) subseteq ran(A)` and its orthogonal-complement form `ker A^* subseteq ker(AC)^*` are elementary linear algebra. The connection between small angles of prescribed subspaces and unavoidable conditioning is classical; WI-106 already anchors J. W. Demmel, **The Condition Number of Equivalence Transformations That Block Diagonalize Matrix Pencils**, *SIAM Journal on Numerical Analysis* 20:3 (1983), 599--610, DOI `10.1137/0720040`.

Fusion-frame theory is also relevant prior art for separating global subspace geometry from the choice of local spanning frames. P. G. Casazza, G. Kutyniok and S. Li, **Fusion frames and distributed processing**, *Applied and Computational Harmonic Analysis* 25:1 (2008), 114--132, DOI `10.1016/j.acha.2007.10.001`, develops fusion-frame systems in which each fixed subspace carries its own local frame. That framework is structural prior art for the distinction used here between target-local representation changes and the geometry of the underlying source defect subspaces.

A targeted search around right/block-diagonal preconditioning, left nullspaces, principal angles, fusion-frame local systems, and block conditioning found the classical ingredients above but no source applying this invariance to the finite-window Ramanujan full-packing family or deriving (11)--(13). This negative search is **not** a priority claim. The durable contribution is the exact specialization: the arithmetic near-kernel family of WI-107 survives arbitrary target-local right processing, not merely scalar block weights.

## 5. Program consequence

This removes one of the main loopholes explicitly left after WI-107. Within the exact full-packing algebraic interface, moving from one scalar per target to arbitrarily sophisticated **within-target** linear weights does not change the asymptotic obstruction. Below `J ~ sqrt(p/log p)`, any uniform relative coercivity theorem still fails on the same clustered modulus-three family.

The remaining escapes now require information that genuinely changes or couples the source defect geometry: source-side structure with an analytically fixed normalization, cross-target mixing that is not block diagonal, positive-slack layers away from exact full packing, or a target count at or above the first scale not excluded by WI-107/WI-108. This is a sharper falsification rule than WI-107's scalar-only version: a proposed covariance gain based on target-local diagonal or internal operator weights must be tested on the WI-107 family **after** those weights are inserted. Equation (11) shows that no such target-local preprocessing can supply a fixed relative singular gap.