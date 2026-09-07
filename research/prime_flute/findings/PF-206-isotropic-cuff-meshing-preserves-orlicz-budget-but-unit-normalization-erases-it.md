# PF-206 — isotropic cuff meshing preserves physical Orlicz budget but unit normalization erases it

**Status:** `EXACT-DERIVED + ENDPOINT-LOCALIZATION + NEGATIVE/ROUTE-BOUNDARY`. PF-205 puts the optional smooth distinguished-cuff comparison on the deterministic scale `w_n\asymp d_n\asymp p_n^{-1}` and proves two facts simultaneously: the smoothed pulled metrics are uniformly elliptic with uniform local `C^1` control, while the full seam coefficient has a prime-summable critical `L\log L` norm of order at most `a_nd_n^2\log(e+1/(a_nd_n))`. The remaining question was phrased as scale/aspect-ratio uniform critical localization on a cylinder of normal width `O(d_n)` and circumference `O(a_n)`. The **aspect ratio itself does not destroy the coefficient currency**: cutting the seam tangentially into `O(a_n/d_n)` physical cells of size `d_n\times d_n` still leaves the sum of the local physical Luxemburg norms at the summable scale

\[
O\!\left(a_nd_n^2\log\!\left(e+\frac1{d_n}\right)\right).
\]

However, a tempting next step is invalid as a budget-preserving argument: if every `d_n\times d_n` cell is first dilated to one fixed unit box and Ponge's fixed-domain critical estimate is then applied to the **unweighted normalized coefficient**, the physical area factor is lost. For a bounded coefficient on a cell of area `\asymp w^2`, the physical Luxemburg norm is `\asymp b w^2\log(e/w)`, whereas its unit-box dilation has Luxemburg norm `\asymp b`. There is therefore no scale-independent inequality that controls the normalized `L\log L` norm by the physical one. With only the PF-205 envelope, summing such normalized unit-box bounds gives an `O(a_n)` module bound rather than a prime-summable one. This does **not** prove that the seam operator fails to be weak trace class; it proves that naive fixed-box normalization discards exactly the small-support currency PF-205 worked to preserve. A successful smooth-route proof must keep physical scale inside the critical operator estimate, or recover the missing scale through a separately proved weighted square-function/Poincare mechanism. PF-204's unsmoothed native-resolvent route remains unaffected.

## Claim

Let `U_n` be PF-205's natural-width two-sided seam neighborhood around the distinguished decomposition cuff. In its signed Fermi-area coordinates,

\[
U_n=\{|x|<w_n\},
\qquad
w_n=\kappa d_n,
\qquad
d\mu=dx\,ds,
\tag{1}
\]

where the cuff circumference is

\[
L_n=2a_n.
\tag{2}
\]

Let `C_n=C_n^{\rm seam}` denote the matrix-valued cotangent coefficient of the smooth exact-area comparison. PF-205 gives, after a finite head,

\[
\|C_n\|_{\infty}\le B_n:=C d_n,
\qquad
\|C_n\|_1\le L_n^{(1)}:=C a_nd_n^2.
\tag{3}
\]

Fix one smooth one-dimensional partition template and cut the `s`-circle into intervals of length comparable to `w_n`, with fixed enlargement and overlap multiplicity `\nu`. Write

\[
C_n=\sum_{j=1}^{N_n}C_{n,j},
\qquad
C_{n,j}=\chi_{n,j}C_n,
\tag{4}
\]

where `0\le\chi_{n,j}\le1`. Then

\[
N_n\le C\left(1+\frac{a_n}{w_n}\right)
\le C\left(1+\frac{a_n}{d_n}\right),
\tag{5}
\]

and for `\Phi(t)=t\log(e+t)` the **physical** local coefficient budget satisfies

\[
\boxed{
\sum_{j=1}^{N_n}
\|C_{n,j}\|_{L_\Phi(U_n)}
\le
C a_nd_n^2
\log\!\left(e+\frac{C}{d_n^2}\right).
}
\tag{6}
\]

Consequently, for the exact prime/shift family,

\[
\boxed{
\sum_n\sum_j
\|C_{n,j}\|_{L_\Phi}<\infty.
}
\tag{7}
\]

Thus an isotropic physical mesh does not create a coefficient-level aspect-ratio loss.

By contrast, let `Q_w` be any Euclidean/Fermi cell of area `m_w\asymp w^2`, and let `D_w:Q\to Q_w` be the affine dilation from one fixed reference box `Q`. For a coefficient `u` on `Q_w`, define the normalized coefficient

\[
\widetilde u(y)=u(D_wy).
\tag{8}
\]

There is **no** constant `K` independent of `w\downarrow0` such that

\[
\|\widetilde u\|_{L_\Phi(Q)}
\le K\|u\|_{L_\Phi(Q_w)}
\tag{9}
\]

for all bounded `u`. Indeed, for `u_w=b\mathbf 1_{Q_w}` with fixed `b>0`,

\[
\|u_w\|_{L_\Phi(Q_w)}
=\frac{b}{\Phi^{-1}(1/m_w)}
\asymp b\,w^2\log\!\left(\frac e w\right),
\tag{10}
\]

whereas

\[
\|\widetilde u_w\|_{L_\Phi(Q)}
=\frac{b}{\Phi^{-1}(1/|Q|)}
\asymp_Q b.
\tag{11}
\]

Hence the ratio in (9) diverges at least like

\[
\frac{1}{w^2\log(e/w)}.
\tag{12}
\]

For the PF mesh, the same normalization can be quantified directly from local `L^1` masses. If

\[
\ell_{n,j}:=\|C_{n,j}\|_1,
\tag{13}
\]

then the unit-box dilation has

\[
\|\widetilde C_{n,j}\|_1\asymp w_n^{-2}\ell_{n,j},
\qquad
\|\widetilde C_{n,j}\|_\infty\le Cd_n.
\tag{14}
\]

Applying the elementary Luxemburg bound after dilation and summing by concavity gives only

\[
\boxed{
\sum_j\|\widetilde C_{n,j}\|_{L_\Phi(Q)}
\le C a_n
}
\tag{15}
\]

from the PF-205 information alone. Equation (15) is an **available proof bound**, not a lower bound for the actual normalized coefficient family and not an operator lower bound. Its importance is that the factor `d_n^2` in (6) has disappeared. Therefore the inference

\[
\text{physical PF-205 }\ell^1(L\log L)
\quad\Longrightarrow\quad
\text{summable fixed-unit-box Ponge bounds}
\tag{16}
\]

is invalid without an additional scale-carrying mechanism.

## 1. Physical square meshing costs only one concentration logarithm

PF-196 proves for bounded nonzero `u`

\[
\|u\|_{L_\Phi}
\le
\|u\|_1
\log\!\left(e+\frac{\|u\|_\infty}{\|u\|_1}\right).
\tag{17}
\]

Put

\[
\ell_j=\|C_{n,j}\|_1,
\qquad
\widetilde L_n=\sum_j\ell_j.
\tag{18}
\]

The fixed overlap gives

\[
\widetilde L_n\le\nu\|C_n\|_1\le C a_nd_n^2.
\tag{19}
\]

For fixed `B>0`, the function

\[
f_B(t)=t\log\!\left(e+\frac Bt\right)
\tag{20}
\]

is concave on `(0,\infty)` because

\[
f_B''(t)
=-\frac{B^2}{t(B+et)^2}<0.
\tag{21}
\]

It is also increasing. Therefore (17), Jensen, (3), (5), and (19) give

\[
\begin{aligned}
\sum_j\|C_{n,j}\|_{L_\Phi}
&\le\sum_jf_{B_n}(\ell_j)\\
&\le
\widetilde L_n
\log\!\left(e+\frac{B_nN_n}{\widetilde L_n}\right)\\
&\le
C a_nd_n^2
\log\!\left(e+\frac{C}{d_n^2}\right),
\end{aligned}
\tag{22}
\]

which proves (6).

This is the seam analogue of PF-198, but its geometry is different. PF-198 had `O(a_n)` **fixed-size** windows along a Lambert body. Here the normal direction itself has width `w_n\asymp d_n`, so an aspect-ratio-one mesh has

\[
N_n\asymp\frac{a_n}{d_n},
\tag{23}
\]

many more cells. Even this much larger count enters only inside the critical concentration logarithm when the norm is kept in the physical measure.

PF-107/PF-205 give

\[
d_n\asymp P_n^{-1},
\qquad
a_n=O(\log P_n).
\tag{24}
\]

Thus

\[
a_nd_n^2\log\!\left(e+\frac1{d_n^2}\right)
=O\!\left(\frac{(\log P_n)^2}{P_n^2}\right),
\tag{25}
\]

which is summable even over all integers. This proves (7).

The conclusion is exact and useful: **neither the long circumference nor the `O(a_n/d_n)` number of isotropic cells is a coefficient-space obstruction.** Any remaining aspect-ratio loss must enter through the operator normalization/factorization, not through physical `L\log L` fragmentation.

## 2. Fixed-unit dilation removes the small-support factor from the Luxemburg norm

Equation (10) is PF-196's exact characteristic-function formula specialized to a shrinking cell. Since the Luxemburg norm is homogeneous in amplitude but not invariant under changing the underlying measure, dilating `Q_w` to a fixed box changes the norm by far more than a harmless coordinate constant.

The same bookkeeping can be seen without a test function. Under the two-dimensional dilation (8),

\[
\|\widetilde C_{n,j}\|_1
=w_n^{-2}\ell_{n,j}
\tag{26}
\]

up to the fixed chart-shape Jacobian, while the pointwise bound stays `O(d_n)`. Applying (17) on the fixed box gives

\[
\|\widetilde C_{n,j}\|_{L_\Phi}
\le
C\frac{\ell_{n,j}}{w_n^2}
\log\!\left(
 e+C\frac{d_nw_n^2}{\ell_{n,j}}
\right).
\tag{27}
\]

Summing exactly as in Section 1,

\[
\sum_j\|\widetilde C_{n,j}\|_{L_\Phi}
\le
C\frac{\widetilde L_n}{w_n^2}
\log\!\left(
 e+C\frac{d_nN_nw_n^2}{\widetilde L_n}
\right).
\tag{28}
\]

With `w_n\asymp d_n`, `N_n\lesssim a_n/d_n`, and `\widetilde L_n\lesssim a_nd_n^2`, the logarithm is bounded by an absolute constant and the prefactor is only `O(a_n)`. This proves (15).

The fixed-torus theorem used in PF-197/PF-200 is homogeneous in the **fixed-domain** Luxemburg norm. Consequently, if one simply maps every shrinking square to the same torus chart, applies

\[
q\!\left(
\Lambda^{-1}M_{\widetilde C_{n,j}}\Lambda^{-1}
\right)
\le C\|\widetilde C_{n,j}\|_{L\log L},
\tag{29}
\]

and then direct-sums the blocks, equations (15) and (29) no longer expose the prime-summable factor from (6). This is the exact point at which the naive normalization loses the PF-205 currency.

Nothing in this argument says that the true localized seam operator has size `\asymp a_n`. It says only that **Ponge-on-unit-boxes plus unweighted direct-sum counting cannot derive the desired summability from the current physical coefficient estimates**. Additional structure may restore the missing scale.

## 3. The missing scale cannot be moved between factors for free

PF-201's regular-body architecture factors the global principal term as

\[
T=A_h^*DA_g,
\tag{30}
\]

with a bounded global-to-local square-function map and a block-diagonal critical middle operator. On fixed-size windows this is ideal because the coefficient's physical and chart measures differ only by uniform constants.

On `w_n`-cells, after unit normalization, one might try to restore the missing `w_n^2` by replacing each middle block `D_{n,j}` by `w_n^2D_{n,j}`. Algebraically, however, preserving (30) then requires multiplying both adjacent local factors by `w_n^{-1}`. In other words, the desired redistribution asks for a weighted square-function estimate of the schematic form

\[
\sum_{n,j}
 w_n^{-2}
\|A_{k,n,j}f\|_2^2
\le C\|f\|_2^2.
\tag{31}
\]

Ordinary bounded overlap supplies only the same estimate **without** `w_n^{-2}`. PF-200/PF-201 therefore do not contain (31) implicitly.

This does not prove that (31), or a weaker substitute sufficient for the endpoint, is false for gradient resolvents. It identifies the extra analytic statement that would be needed if the scale is to be recovered through the outer factors rather than through the middle critical theorem. A Poincare cancellation, derivative structure, homogeneous/conformal critical estimate, or another two-space factorization might provide it; none is currently established by the persisted seam results.

Thus the smooth-route gate can be sharpened from the vague phrase “scale-uniform Cwikel constant” to the following dichotomy:

\[
\boxed{
\begin{array}{l}
\text{either keep the physical }w_n^2\text{ measure inside the critical middle estimate,}\\
\text{or prove a weighted local resolvent/square-function mechanism that returns it.}
\end{array}}
\tag{32}
\]

A fixed-unit coefficient normalization followed by the unmodified PF-201 factorization does neither.

## 4. Prior-art and novelty audit

The Luxemburg characteristic-function formula, the concavity estimate (20)--(22), ordinary partitions of unity, affine dilation, and direct-sum weak-Schatten bookkeeping are standard. PF-196 and PF-198 already use the same Orlicz accounting principles in nonshrinking PF geometries. No novelty is claimed for those analytic facts.

Ponge's matrix-valued critical `Q u P` theorem is prior art recorded as S20 in `research/prime_flute/SOURCES.md`; PF-197/PF-200 explain its fixed-torus localization and the dependence on the fixed-domain `L\log L` norm. A fresh structure-directed audit also located F. Sukochev and D. Zanin, *Cwikel-Solomyak estimates on tori and Euclidean spaces*, arXiv:2008.04494; published as *Solomyak-type eigenvalue estimates for the Birman-Schwinger operator*, Sbornik Mathematics **213** (2022), 1250--1289, DOI `10.4213/sm9732e`. Their Euclidean symmetrized critical theory is explicitly motivated by conformal invariance. That is relevant evidence that scale-aware critical formulations exist in flat space, but PF-206 does **not** import it as a theorem for the curved two-metric prime-flute seam and does not claim that it directly supplies (32).

The project-specific deduction is the combination of PF-205's exact width/amplitude/area scales with the critical Luxemburg localization formula: **physical isotropic meshing remains prime-summable, while fixed-unit normalization can erase precisely the `d_n^2` support gain needed for that conclusion.** This isolates a concrete proof-architecture trap and a precise scale-carrying obligation for the next endpoint step. A literature search did not identify a theorem that automatically transfers the Euclidean scale-aware estimate to PF-205's varying hyperbolic source/target gradient-resolvent form with the required uniform constants; search absence is not treated as novelty evidence.

## 5. Falsification and boundary checks

A later adversary can audit PF-206 by:

1. checking PF-205's physical seam data `w_n\asymp d_n`, circumference `2a_n`, `\|C_n\|_\infty=O(d_n)`, and `\|C_n\|_1=O(a_nd_n^2)`;
2. constructing the fixed-overlap tangential partition with `N_n=O(1+a_n/d_n)` and verifying that no derivative of the partition enters the coefficient-only statement;
3. differentiating (20) to check concavity/increase and reproducing (22) without replacing every cell by the global worst-case norm;
4. inserting `d_n\asymp P_n^{-1}` and `a_n=O(\log P_n)` to verify the summable majorant (25);
5. checking the exact Luxemburg norm of `b\mathbf1_E` and the Jacobian under two-dimensional dilation to obtain (10)--(12) and (26)--(28);
6. keeping (15) in its correct logical role: it is the bound available from PF-205 after unit normalization, not a lower bound for the actual PF coefficient or operator;
7. refusing to infer failure of weak `S_1` from the normalization counterexample;
8. refusing to claim that the Euclidean/conformal Sukochev--Zanin theorem already applies to the varying hyperbolic two-metric seam;
9. if a future proof inserts a factor `w_n^2` into the normalized critical block, checking explicitly where the compensating `w_n^{-1}` factors are controlled rather than hiding them in “scale invariance”;
10. keeping PF-204's unsmoothed piecewise cotangent-transport route and PF-183's true-short-collar splice logically separate.

PF-206 would need narrowing if the PF-205 seam coefficient cannot be partitioned with the stated physical `L^1`/`L^\infty` controls, if the Fermi area coordinate does not give the asserted `w_n^2` cell Jacobian, or if the Luxemburg characteristic-function scaling is used with a different normalization of the underlying measure. None of those checks depends on the still-open operator estimate.

## Consequences for the research line

The optional smooth decomposition-cuff branch is now more sharply normalized. PF-205 already showed that one can choose `w_n\asymp d_n` without sacrificing `C^1` geometry or critical coefficient summability. PF-206 adds that **breaking the long thin cuff into aspect-ratio-one physical cells is also harmless at the coefficient level**. The raw number `a_n/d_n` of cells is not the problem.

The remaining issue is exactly where critical scale lives in the operator theorem. A proof should not say merely “rescale each cell to unit size and apply Ponge”: that step changes the homogeneous Luxemburg currency and can erase the support factor. The next useful target is a scale-aware critical estimate that remains linear in the **physical** seam `L\log L` budget, or a weighted global-to-local factorization proving the missing scale through the gradient-resolvent factors. The flat Euclidean/conformal Cwikel literature is a natural audit surface for that target, but the curved two-metric bridge still has to be derived.

PF-204 remains the preferred alternative if the smooth-route scaling becomes artificial: its native two-Hilbert-space identity avoids seam smoothing altogether and asks instead for a critical theorem that retains the explicit piecewise cotangent transport. Neither route changes the independent PF-183 true-short-collar endpoint obligation, and no wave/scattering/determinant/RH consequence is asserted here.