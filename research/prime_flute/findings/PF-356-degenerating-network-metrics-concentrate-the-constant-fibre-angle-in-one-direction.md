# PF-356 — degenerating network metrics concentrate the constant-fibre angle in one direction

**Status:** EXACT-DERIVED + CLASSICAL-SCHUR-PERTURBATION-METHOD + MODEL-MULTIPLICITY-COUNTERCONTROL + ACTUAL-PANT-ANGLE-OPEN.

PF-355's retained-constant angle can approach norm one while **every singular value except the first tends to zero**, even with an increasing number of modules and complete unequal Fourier transition bands. Thus its norm/determinant obstruction cannot supply a uniform multiplicity theorem from positivity of the network matrix alone.

The control uses `K_tau = vv^T + tau I`, with every `v_i != 0` and `tau>0`. For two modules, `v=(1,-1)` is a grounded difference network. For more modules this is generally a dense coupling, **not the nearest-neighbor flute network**. The result concerns constants against a finite bounded high-frequency strip; it neither bounds the enlarged full low/high angle from above nor settles the actual pant/seam operator.

## 1. Exact finite statement

Fix `d>=2`, a positive node `a`, and the complete retained fibre

\[
F_a=\{(i,a):1\le i\le d\}.
\]

Let `T` be any finite transition-label set and `Y={(i_j,b_j):1<=j<=r}` a retained high-label set, with `r>=2`. Require that **all scalar nodes in `T union Y` are mutually distinct and different from `a`**, including nodes on different modules. Set

\[
K_\tau=vv^{\mathsf T}+\tau I_d,\qquad v_i\ne0,\quad\tau>0,
\qquad
(M_\tau)_{(i,x),(j,y)}=\frac{(K_\tau)_{ij}}{x+y}.
\tag{1}
\]

All nodes are positive. Short exactly the whole set `T`, and write

\[
S_\tau=M_\tau^{/T}
=\begin{pmatrix}A_\tau&C_\tau\\C_\tau^{\mathsf T}&B_\tau\end{pmatrix},
\qquad
Z_\tau=A_\tau^{-1/2}C_\tau B_\tau^{-1/2}.
\tag{2}
\]

The blocks are indexed by `F_a` and `Y`. For every `tau>0` the full coefficient form is strictly positive, by the exponential Gram representation in PF-355. Put

\[
p=\min(d,r),\qquad
P_Y=\prod_{j=1}^r\left(\frac{b_j-a}{b_j+a}\right)^2\in(0,1).
\]

For these **fixed finite data**, as `tau` decreases to zero,

\[
\boxed{
\sigma_k(Z_\tau)=O(\sqrt\tau)\quad(2\le k\le p),
\qquad
\sigma_1(Z_\tau)^2=1-P_Y-O(\tau).
}
\tag{3}
\]

The last error is nonnegative: `sigma_1^2 <= 1-P_Y` for every positive `tau`. Constants in the asymptotic bounds may depend on every finite node, `v`, and the number of labels. No estimate uniform over growing lattices or near-colliding nodes is asserted.

## 2. Why normalization does not restore the other directions

Use scalar vectors `k_x(t)=exp(-xt)` in `L^2(0,infinity)`, so their Gram kernel is `C(x,y)=1/(x+y)`. At `tau=0`, (1) is the Gram matrix of the vectors `v_i k_x`. The transition vectors are independent because their nodes are distinct and `v_i` is nonzero. Thus the transition block remains invertible at zero, even though the **whole** matrix has the `d-1` constant-fibre degeneracy.

Let `Pi_T` be scalar orthogonal projection onto `span{k_t:t in T}`, ignoring the nonzero scalar weights, and define

\[
r_T(x,y)=\langle(I-\Pi_T)k_x,(I-\Pi_T)k_y\rangle.
\]

Then

\[
A_0=r_T(a,a)vv^{\mathsf T},\qquad
(C_0)_{ij}=v_i v_{i_j}r_T(a,b_j),
\qquad
(B_0)_{jk}=v_{i_j}v_{i_k}r_T(b_j,b_k).
\tag{4}
\]

In particular `rank C_0<=1`. The residual high block `B_0` is strictly positive: the scalar nodes in `T union Y` are all distinct, so their full scalar Cauchy Gram matrix and its transition Schur complement are strictly positive. Write `beta=lambda_min(B_0)>0`.

The transition inverse is analytic near zero. Therefore

\[
C_\tau=C_0+O(\tau),\qquad B_\tau\ge B_0>0.
\tag{5}
\]

The inequality follows from variational monotonicity of shorting, since `M_tau>=M_0`; it does not require the singular full matrix `M_0` to have an inverse.

There is also a sufficient quantitative floor for the singular low normalization. Let `D` be the Gram matrix obtained by replacing `K_tau` with `I_d` in (1). It is positive and separates by module. Since `M_tau=M_0+tau D>=tau D`, shorting gives

\[
A_\tau\ge\tau A_D>0,
\qquad
(A_D)_{ii}=\frac1{2a}
\prod_{(i,t)\in T}\left(\frac{a-t}{a+t}\right)^2.
\tag{6}
\]

The empty product is one. Formula (6) is the scalar Cauchy Schur identity; it also follows by eliminating one node at a time. Here other retained high coordinates are fixed to zero when taking the low principal block. Thus `alpha=lambda_min(A_D)>0` for the fixed data, however small it is.

Approximate the normalized mixed block by the rank-at-most-one matrix

\[
R_\tau=A_\tau^{-1/2}C_0B_\tau^{-1/2}.
\]

Equations (5)--(6) give

\[
\|Z_\tau-R_\tau\|
\le (\tau\alpha)^{-1/2}\,\|C_\tau-C_0\|\,\beta^{-1/2}
=O(\sqrt\tau).
\tag{7}
\]

The singular-value approximation principle proves the first assertion of (3). This calculation is necessary: the low normalization is unbounded as `tau -> 0`, so simply substituting a rank-one matrix before normalization would not prove the result.

Finally PF-355's complete-fibre elimination identity gives, at every `tau>0`,

\[
\prod_{k=1}^{p}(1-\sigma_k(Z_\tau)^2)=P_Y.
\tag{8}
\]

For clarity, eliminate `F_a` first: its block is `K_tau/(2a)`, and every remaining entry is multiplied by `(x-a)/(x+a)` on the left and the corresponding factor on the right. Shorting `T` cancels its nonzero diagonal factors. Reversing the elimination order proves
`B_tau-C_tau^T A_tau^(-1) C_tau=F B_tau F`, where `F_jj=(b_j-a)/(b_j+a)`, and determinants give (8).

By (7), the product of the factors in (8) with `k>=2` is `1-O(tau)`. Hence

\[
1-\sigma_1(Z_\tau)^2
=\frac{P_Y}{\prod_{k=2}^{p}(1-\sigma_k(Z_\tau)^2)}
=P_Y+O(\tau),
\]

with a nonnegative error. This proves all of (3), without an inverse or pseudoinverse of `A_0`.

## 3. Complete unequal physical bands and arbitrarily many modules

Use the cosine realization of PF-355,

\[
x=\cosh(\pi\xi),\qquad \xi=2\pi k/L_i,\qquad a=1.
\]

Take any finite collection of periods whose pairwise ratios are irrational. Eliminate **every** positive cosine lattice frequency in a fixed interval `(kappa_-,kappa_+)`, and retain as `Y` every such mode in `[kappa_+,Omega]`, where `0<kappa_-<kappa_+<Omega`. These sets are finite and their nonzero nodes are globally distinct. PF-354 proves this nonintersection property for the actual distinct prime-cuff periods. Thus (3) applies when sampling those periods, but with the **freely chosen** matrix (1), not the actual geometric coupling.

Sine transition modes decouple in the even-weight cosine model and do not alter the result. Positive physical Fourier normalizations are diagonal congruences and leave canonical correlations unchanged.

For a sequence of finite models, allow both the module count `d_n` and the minimum period to tend to infinity. The number `r_n` of retained high modes tends to infinity. With

\[
q=\frac{\cosh(\pi\Omega)-1}{\cosh(\pi\Omega)+1}<1,
\qquad P_{Y_n}\le q^{2r_n},
\]

choose `tau_n>0` **after fixing all data of the nth finite model**, small enough that (3) implies

\[
\sigma_2(Z_{\tau_n})\le 1/n,
\qquad
\sigma_1(Z_{\tau_n})^2\ge1-q^{2r_n}-1/n.
\tag{9}
\]

Then `||Z_tau_n|| -> 1`, while for every fixed threshold `0<epsilon<1` the number of singular values above `epsilon` is exactly one eventually. All matrices used in this sequence are strictly positive. No uniform relation between `tau_n`, the periods, or corridor conductances is obtained; the choice can be arbitrarily small and depends on conditioning of the whole finite section.

This realizes, inside PF-355's exact matrix class and with complete transition bands, its warning that determinant deficit can concentrate in one singular direction. It rules out any growing lower bound on this **constant-fibre/high-strip** singular count based only on `K>0`, unequal lattices, and the number of sampled modes.

## 4. Controls and the surviving geometric question

- **Shared nonzero nodes change the limit.** If `Y` instead contains one complete common high fibre `F_b`, then `B_0` is singular. Estimate (7) no longer applies, and PF-353 gives all `d` correlations exactly `2 sqrt(ab)/(a+b)` at every positive `tau`. Exact lattice nonintersection is load-bearing, not cosmetic.
- **Nearest-neighbor locality is not preserved in growing dimension.** For `d=2`, `v=(1,-1)` gives `E_tau=||f_1-f_2||^2+tau(||f_1||^2+||f_2||^2)`, the two-module difference model. For `d>2`, all off-diagonal entries `v_i v_j` are nonzero, so (1) is not the flute's tridiagonal network. A growing-multiplicity theorem exploiting that locality remains possible.
- **The enlarged low space is a different question.** Constants are only a subspace of the retained physical low sector. Adding other low modes or the unbounded high sector can increase singular values. The upper bound on `sigma_2` here does not transfer through that enlargement. The norm lower bound still does, as in PF-355.
- **No singular metric is normalized.** Zero is used only to analyze blocks with invertible transition and high restrictions. Every canonical correlation in (2), (8), and (9) uses strictly positive `tau`.
- **No actual-surface or infinite-operator conclusion.** The free matrix, its degenerating scale, the pant/seam remainder, compatible infinite-section limits, and localized witnesses remain separate obligations. This control proves neither compactness nor noncompactness, no Schatten endpoint, no scattering statement, and no zeta-zero or RH consequence. Nonprime unequal periods work equally well.

The remaining multiplicity route must use information beyond the constant-fibre determinant and positivity alone, such as the actual local coupling or additional retained low structure. PF-355's norm obstruction remains intact.

## 5. Prior art and verification

Schur residual correlations are classical; see Forrester and Zhang, [*Parametrising correlation matrices*](https://arxiv.org/abs/1812.07685), equations (2.6)--(2.7), already S23. Canonical correlations in a positive matrix metric and their perturbation theory are also classical: Knyazev and Argentati, [*Principal Angles between Subspaces in an A-Based Scalar Product: Algorithms and Perturbation Estimates*](https://doi.org/10.1137/S1064827500377332), SIAM Journal on Scientific Computing 23 (2002), 2008--2040. The latter is context, not an imported uniform estimate for a metric becoming singular. The finite bound (7) and its hypotheses are proved here.

Structure-directed searches covered Cauchy Schur complements, canonical correlations under degenerating metrics, rank-one couplings, and Gram/Stein formulations. No historical novelty is claimed for these elementary matrix methods. The derived addition is the explicit **rank-concentration control in the same unequal-lattice family as PF-355**, including the normalized rate, exact surviving correlation, and growing-section quantifier (9). It sharpens an evidence boundary; it is not a new general theory of canonical correlation.

Supplementary Python/mpmath 1.4.1 checks at 160 decimal digits used `d=2,3,4`, `a=1`, `v_i=(-1)^i` with zero-based indices, either no transitions or one node `2+i/7` per module, and high nodes `5+i/11` on each module plus node `7` on module 0. For `tau=10^(-16),10^(-32),10^(-48),10^(-64)`, all 24 cases had positive Cholesky factors and satisfied (8) with absolute residual below `1e-95`. At the smallest `tau`, every second correlation was below `2.1e-24`, and the squared first correlation differed from `1-P_Y` by less than `1e-25`. The observed `sigma_2/sqrt(tau)` stabilized at data-dependent values ranging from about `677` to `2.07e8`, illustrating why a uniform rate cannot be inferred from the fixed-data proof.

A shared-high control with `d=3`, high node `5` on every module, the same mismatched transitions, and `tau=1e-32` retained all three correlations `sqrt(20)/6`, agreeing within `1e-95`. A complete-lattice check used periods `30 sqrt(2),30 sqrt(3),30 sqrt(5)`, transition interval `(1,1.2)`, high strip `[1.2,2]`, and `tau=1e-100`: its 5 transition modes and 21 high modes gave correlations approximately `0.875968378712`, `1.43e-37`, and `1.17e-38`. These computations check the finite formulas only; (3) and (9) follow from the exact argument, not from the numerical examples. No Lean verification or independent adversarial approval is claimed.
