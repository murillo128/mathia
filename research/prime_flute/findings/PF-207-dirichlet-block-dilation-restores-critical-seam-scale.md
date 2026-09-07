# PF-207 — operator-level Dirichlet dilation restores the shrinking-cell critical scale

**Status:** `LITERATURE+DERIVED + EXACT-SCALING + POSITIVE/ROUTE-NARROWING`. PF-206 proves that a coefficient-only normalization of the PF-205 seam cells to a fixed unit box erases the physical `w_n^2` support factor: the summed normalized `L\log L` coefficient bound is only `O(a_n)`. That loss is **not intrinsic to a correctly rescaled critical operator block**. For a Dirichlet order-`-2` Birman--Schwinger block on a cell `Q_w=wQ`, unitary dilation contributes an exact factor `w^2` from the two order-`-1` sides. Frank--Laptev's domain-independent two-dimensional Orlicz bound, combined with the Birman--Schwinger principle, gives a uniform weak-trace estimate for the fixed Dirichlet block. Hence the PF-206 normalized coefficient estimate becomes `O(w_n^2 a_n)=O(a_n d_n^2)`, which is prime-summable. The remaining smooth-seam difficulty is therefore **not a local Dirichlet shrinking-box constant**; it is the comparison/reassembly step that must connect the true global gradient-resolvent seam term to such scale-correct local blocks without creating `w_n^{-1}` commutator, boundary, or transmission losses. This does not prove the global seam term is weak trace class and does not alter the independent true-short-collar splice gate.

## Claim

Let `Q\subset\mathbb R^2` be one fixed bounded open reference cell and `Q_w=wQ`. Let

\[
A_w=-\Delta^D_{Q_w},\qquad A=-\Delta^D_Q,
\tag{1}
\]

and let `U_w:L^2(Q_w)\to L^2(Q)` be the two-dimensional unitary dilation

\[
(U_wu)(y)=w\,u(wy).
\tag{2}
\]

For a bounded measurable scalar coefficient `f_w` on `Q_w`, write

\[
\widetilde f_w(y)=f_w(wy).
\tag{3}
\]

Then

\[
U_wA_wU_w^{-1}=w^{-2}A,
\tag{4}
\]

and therefore the massive critical block

\[
K_w=(1+A_w)^{-1/2}M_{f_w}(1+A_w)^{-1/2}
\tag{5}
\]

satisfies the exact identity

\[
\boxed{
U_wK_wU_w^{-1}
=w^2(w^2+A)^{-1/2}M_{\widetilde f_w}(w^2+A)^{-1/2}.
}
\tag{6}
\]

Put

\[
B_w=\left(\frac{A}{A+w^2}\right)^{1/2}.
\tag{7}
\]

Since the Dirichlet Laplacian on the bounded reference cell has positive first eigenvalue, `B_w` is a contraction and commutes with `A`. Thus

\[
(w^2+A)^{-1/2}=B_wA^{-1/2},
\tag{8}
\]

so for every symmetric ideal gauge `q` stable under bounded left/right multiplication,

\[
\boxed{
q(K_w)
\le w^2 q\!\left(A^{-1/2}M_{\widetilde f_w}A^{-1/2}\right).
}
\tag{9}
\]

For the logarithmic weak-trace gauge used in the current endpoint line,

\[
q(T)=\sup_{N\ge2}\frac1{\log N}\sum_{m=1}^Ns_m(T),
\tag{10}
\]

there is a constant `C_Q` such that

\[
q\!\left(A^{-1/2}M_fA^{-1/2}\right)
\le C_Q\|f\|_{L\log L(Q)}.
\tag{11}
\]

More precisely, the scalar estimate follows from Frank--Laptev with a constant that is in fact uniform over all finite-measure planar Dirichlet domains, up to the standard equivalence between their Orlicz norm and the `t\log(e+t)` normalization used here. Consequently

\[
\boxed{
q(K_w)\le C_Q w^2\|\widetilde f_w\|_{L\log L(Q)}.
}
\tag{12}
\]

The same conclusion holds, with only a fixed fibre-dimension constant, for a Hermitian matrix coefficient acting on a fixed finite-dimensional trivial bundle over `Q`: split it into positive and negative parts and dominate each by its scalar operator-norm envelope times the identity.

Apply (12) to the PF-205/PF-206 isotropic seam mesh, where

\[
w_n\asymp d_n,
\qquad
\sum_j\|\widetilde C_{n,j}\|_{L\log L(Q)}\le C a_n
\tag{13}
\]

is exactly the normalized bound isolated in PF-206. For the corresponding **Dirichlet critical model blocks**,

\[
\boxed{
\sum_j q(K_{n,j})
\le Cw_n^2\sum_j\|\widetilde C_{n,j}\|_{L\log L(Q)}
\le C a_nd_n^2.
}
\tag{14}
\]

PF-107/PF-205 give `d_n\asymp P_n^{-1}` and `a_n=O(\log P_n)`, so

\[
\boxed{
\sum_n\sum_j q(K_{n,j})<\infty.
}
\tag{15}
\]

Thus PF-206's loss of the `d_n^2` factor occurs only if one normalizes the coefficient and then forgets the simultaneous scaling of the critical operator factors. A correctly dilated Dirichlet block restores exactly the missing area scale.

## 1. Frank--Laptev gives the required fixed-domain weak endpoint

Frank and Laptev prove that there is an absolute constant `C` such that for every finite-measure open set `\Omega\subset\mathbb R^2` and every real potential in their critical Orlicz class,

\[
N(-\Delta^D_\Omega+V)
\le C\|V_-\|_{\mathcal B,\Omega}.
\tag{16}
\]

Their Young function is equivalent at infinity to `t\log(1+t)`, hence to the `L\log L` normalization used in PF-196--PF-206; on the fixed reference cell the standard Luxemburg/dual Orlicz norms are equivalent up to an irrelevant absolute/domain constant.

For `f\ge0`, apply (16) to `V=-\alpha f`. The Birman--Schwinger principle identifies the negative-eigenvalue count with the counting function of

\[
H_f=A^{-1/2}M_fA^{-1/2}
\tag{17}
\]

at threshold `\alpha^{-1}`. Therefore, for every `t>0`,

\[
n_+(t,H_f)
\le Ct^{-1}\|f\|_{L\log L(Q)}.
\tag{18}
\]

Equivalently,

\[
s_m(H_f)\le \frac{C}{m}\|f\|_{L\log L(Q)}.
\tag{19}
\]

Since `\sum_{m\le N}m^{-1}\le1+\log N`, (19) implies (11). A real signed scalar coefficient follows by positive/negative decomposition and the Ky Fan triangle inequality.

For a Hermitian `r\times r` coefficient `F`, write `F=F_+-F_-` and `0\le F_\pm\le\|F\|_{\mathrm{op}}I_r`. The positive Birman--Schwinger blocks are then form-dominated by the direct sum of `r` copies of the scalar block with potential `\|F\|_{\mathrm{op}}`; the eigenvalue-counting bound gains only the fixed factor `r`. This is enough for the two-dimensional cotangent fibre in the seam model. No new matrix-valued Cwikel theorem is claimed here.

## 2. Exact dilation returns the scale that coefficient normalization removed

PF-206 considered the tempting inference

\[
\text{physical }L\log L\text{ budget}
\longrightarrow
\text{unit-box coefficient norm}
\longrightarrow
\text{fixed-box critical bound}.
\tag{20}
\]

The first arrow alone is lossy: on one `w\times w` cell, the unit-box coefficient norm forgets the cell area. Equation (6) shows what is missing from that bookkeeping. Dilation of the **whole critical block**, rather than only `f`, gives one factor `w` from each order-`-1` side and hence the prefactor `w^2`.

The mass term `1` does not spoil the conclusion. After dilation it becomes the spectral parameter `w^2` in `(A+w^2)^{-1/2}`, and the contraction factorization (7)--(9) bounds it by the homogeneous Dirichlet block uniformly as `w\downarrow0`.

For the PF mesh, PF-206 already proves the only coefficient estimate needed after normalization:

\[
\sum_j\|\widetilde C_{n,j}\|_{L\log L(Q)}=O(a_n).
\tag{21}
\]

Multiplying by the operator-level `w_n^2\asymp d_n^2` immediately yields (14). In particular, no concentration logarithm is required for summability at this stage:

\[
a_nd_n^2=O\!\left(\frac{\log P_n}{P_n^2}\right).
\tag{22}
\]

This is stronger than merely saying that a scale-aware theorem might exist. The scale-aware endpoint is already available for the canonical **Dirichlet Birman--Schwinger model** of each shrinking cell.

## 3. What remains open is the global-to-Dirichlet bridge

The true PF seam operator is not the orthogonal direct sum of (5). In the preferred unsmoothed architecture PF-204 gives

\[
(dR_g)^*M_{C_0}P_{F_0}dR_+,
\tag{23}
\]

with two native global hyperbolic resolvents and the piecewise cotangent transport `P_{F_0}`. In the optional PF-205 smooth architecture the local factors are still restrictions of global gradient resolvents, not independently imposed Dirichlet half-resolvents on each mesh cell.

Therefore (15) does **not** license replacing the global operator by a Dirichlet direct sum. Such a replacement has to account for at least:

- localization/IMS or resolvent-commutator terms generated by the cell partition;
- boundary and transmission terms across artificial Dirichlet cell boundaries;
- comparison between the two varying but uniformly `C^1` seam metrics and the reference Dirichlet block;
- finite-overlap reassembly back into the global two-resolvent factorization;
- the piecewise cotangent transport in the PF-204 branch if the unsmoothed architecture is used.

The dangerous point is exactly the one PF-206 exposed: derivatives of a `w_n`-scale partition cost `w_n^{-1}`. A valid bridge must show that the two order-`-1` operator factors, cancellation, Poincaré structure, or a boundary-resolvent identity absorb those costs without consuming the restored `w_n^2` budget. Merely imposing Dirichlet boundary conditions by fiat would hide the unresolved step.

Thus the smooth-route frontier sharpens to

\[
\boxed{
\text{scale-correct local Dirichlet endpoint: closed}
\quad\Longrightarrow\quad
\text{global/local comparison and reassembly: open}.
}
\tag{24}
\]

This is complementary to PF-204: the unsmoothed route may still avoid artificial seam-cell boundaries entirely if a two-manifold/branchwise critical estimate can handle `P_{F_0}` directly.

## 4. Prior-art and novelty audit

The dilation law for the Dirichlet Laplacian, ideal stability under bounded multiplication, the Birman--Schwinger principle, and harmonic-sum conversion from an `s_m=O(m^{-1})` bound to the logarithmic Ky Fan gauge are classical.

The main imported endpoint theorem is:

**R. L. Frank, A. Laptev**, *Bound on the number of negative eigenvalues of two-dimensional Schrödinger operators on domains*, Algebra i Analiz **30** (2018), no. 3, 250--272; English translation St. Petersburg Mathematical Journal **30** (2019), no. 3, 573--589. DOI `10.1090/spmj/1559`; arXiv:1712.03167. Their Theorem 1.1 gives the critical Orlicz negative-eigenvalue bound with a constant independent of the finite-measure Dirichlet domain.

This sits next to the already audited critical literature in S20/PF-197 and PF-206: Ponge proves matrix-valued `Q u P` weak-trace estimates on fixed smooth critical pseudodifferential backgrounds, while Sukochev--Zanin emphasize conformally natural critical Cwikel--Solomyak formulations in flat space. None of those sources is claimed to prove the PF global seam comparison.

No novelty is claimed for the local Dirichlet estimate itself. The project-specific deduction is the conjunction of Frank--Laptev/Birman--Schwinger with PF-206's exact normalized seam budget: **the `d_n^2` factor lost by coefficient-only normalization is restored automatically when the whole Dirichlet critical block is dilated.** Therefore a shrinking local Dirichlet constant is not the remaining PF obstruction; the mathematical burden moves to an explicit global-to-local boundary/commutator comparison. A structure-directed literature search found the domain-uniform Dirichlet theorem above but no theorem that identifies PF-204/PF-205's two-metric global gradient-resolvent seam term with the required direct sum while preserving the same prime-summable endpoint currency. Search absence is not used as evidence of novelty.

## 5. Falsification and boundary checks

A later adversary can audit PF-207 by:

1. verifying the two-dimensional unitary dilation (2) and the spectral scaling (4);
2. deriving (6) directly by functional calculus and checking the exact `w^2` prefactor;
3. verifying `0\le B_w\le1` and the ideal inequality (9);
4. checking Frank--Laptev Theorem 1.1 and the equivalence of its critical Orlicz normalization with `L\log L` on the fixed reference cell;
5. applying Birman--Schwinger at coupling `\alpha=t^{-1}` to obtain the counting estimate (18), then (19) and (11);
6. checking the finite-fibre domination argument separately rather than attributing a matrix theorem to Frank--Laptev;
7. inserting PF-206's already-persisted normalized bound (13) and `w_n\asymp d_n` to reproduce (14)--(15);
8. refusing to replace the actual global gradient-resolvent seam term by independent Dirichlet blocks without an explicit resolvent/localization identity;
9. tracking every derivative of a `w_n`-scale cutoff, where a factor `w_n^{-1}` can consume the restored scale;
10. keeping the PF-183 true-short-collar splice and all wave/scattering/determinant/RH consequences outside this finding.

PF-207 would need narrowing if Frank--Laptev's counting theorem cannot be converted by Birman--Schwinger to the stated fixed-domain weak singular-value estimate, if the PF-206 normalized sum is incompatible with the chosen equivalent Orlicz norm, or if the dilation is applied to only the coefficient rather than the entire critical block. None of those checks assumes the still-open global/local comparison.

## Consequences for the research line

PF-206's dichotomy is now asymmetric. The first branch -- **keep physical scale in the critical local operator** -- has a concrete successful Dirichlet realization. For the PF-205 natural-width seam mesh, local Dirichlet critical blocks have a total logarithmic weak-trace budget `O(a_nd_n^2)` and therefore sum absolutely over the prime/shift family.

The useful next question is no longer whether a two-dimensional shrinking box can support a scale-correct critical theorem. It can. The next question is whether the actual PF seam term admits a localization/comparison to those blocks whose artificial-boundary and cutoff errors are also prime-summable, or whether the PF-204 unsmoothed native-resolvent route avoids that bridge more efficiently. In either case the endpoint work has moved from **local critical scale** to **global/local operator architecture**.

This remains analytic control shared by the prime flute and its all-composite shift clone. It supplies no prime/clone separator and no RH mechanism by itself.