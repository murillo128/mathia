# WI-128 — extensive Lamzouri screening forces a macroscopic Vandermonde near-null sector

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-INTERFACE`. WI-127 proves that any one fixed-period, distinct-node exceptional cell pays a positive Lamzouri horizontal-transversality cost, but its argument uses only the smallest singular value of the fiber Vandermonde and therefore leaves open the possibility that the constant collapses as the period grows. The exact strengthening below identifies the correct growing-period invariant: if a positive density of bounded-depth off-line pairs makes Lamzouri's horizontal remainder subextensive, then not merely one but a **positive-density sector of the normalized reciprocal-node Vandermonde spectrum must collapse to zero**.

More precisely, for a period-`P` density-one cell with `k` non-real conjugate pairs, reciprocal-node Vandermonde `\widetilde{\mathcal V}_P=P^{-1/2}\mathcal V_P`, and normalized horizontal depths bounded by `B`, the periodic Lamzouri remainder obeys

\[
\boxed{
\frac{R_H}{PM}
\ge
f_{\min}e^{-2\pi B}\,
\frac1P\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2,
}
\tag{A}
\]

where singular values are ordered decreasingly and

\[
f_{\min}
=\frac{\cos(1/\sqrt2)}{\sqrt2\sin(1/\sqrt2)}
=0.8274992963\ldots.
\]

Thus, if `k/P >= rho > 0` while `R_H/(PM) -> 0`, the mean squared singular value across the bottom `k` directions tends to zero. For every fixed `epsilon>0`, all but `o(P)` of those `k` singular values then satisfy `sigma^2 < epsilon`. A surviving bounded-depth periodic screen therefore requires a macroscopic near-null sector, not just a bad condition number caused by one exceptional direction.

This is a structural constraint on the uncertified complement, not a new unconditional percentage for zeta. It refines WI-127 and supports the WI-126 defect-to-zero program by replacing a non-uniform `sigma_min` target with a positive-density spectral-tail target.

## 1. Interface from WI-126 and WI-127

Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*, arXiv:2609.02882v1 (2 September 2026), introduces

\[
f_z(u)=\eta(u)e^{-2\pi iuz},\qquad
 g_z=\frac{f_z+f_{\bar z}}2,\qquad
 h_z=\frac{f_z-f_{\bar z}}{2i}.
\]

WI-126 reconstructs the nonnegative slack discarded by the adapted Gram--Schmidt/Bessel argument and isolates the exact horizontal term

\[
R_H\ge4\sum_{z\in Z_+}m_z\operatorname{dist}(h_z,V)^2.
\tag{1}
\]

WI-127 then considers a simple, conjugation-invariant density-one cell of `P` labels modulo real translation by `P`, with exactly `k` non-real conjugate pairs and pairwise distinct reciprocal nodes

\[
\omega_j=e^{-2\pi i\zeta_j/P}.
\tag{2}
\]

On the fiber interval

\[
J=(-1/2,-1/2+1/P),
\]

the full raw `f` family has the factorization

\[
F(t)=D_\eta(t)\,\mathcal V_P\,D_t,
\qquad
(\mathcal V_P)_{rj}=\omega_j^r,
\quad 0\le r<P,
\tag{3}
\]

where

\[
D_\eta(t)=\operatorname{diag}(\eta(t+r/P))_{r=0}^{P-1},
\qquad
D_t=\operatorname{diag}(e^{-2\pi i\zeta_jt})_{j=1}^{P}.
\]

Replacing each raw conjugate pair by its `g/h` pair gives a square fiber matrix

\[
W(t)=[V(t)\ H(t)]=F(t)C,
\tag{4}
\]

where `V(t)` contains the `P-k` retained real-`f` and `g` columns and `H(t)` contains the `k` omitted anti-invariant `h` columns. Each pairwise change-of-columns block has smallest singular value `1/sqrt(2)`, hence

\[
s_{\min}(C)=\frac1{\sqrt2}.
\tag{5}
\]

The range inclusion established in WI-127 gives, after summing over the `k` base anti-invariant directions,

\[
\sum_{j=1}^{k}\operatorname{dist}(h_j,V_\infty)^2
\ge
\int_J
\|(I-P_{V(t)})H(t)\|_F^2\,dt.
\tag{6}
\]

The point of the present finding is to keep the full rank-`k` residual in (6) instead of lowering every individual distance by the single number `sigma_min(W(t))`.

Primary source: https://arxiv.org/abs/2609.02882.

## 2. Eckart--Young converts horizontal screening into a bottom spectral tail

At a fixed fiber `t`, define

\[
S(t)=H(t)^*(I-P_{V(t)})H(t).
\]

Then

\[
\operatorname{tr}S(t)
=\|(I-P_{V(t)})H(t)\|_F^2.
\tag{7}
\]

Construct

\[
A(t)=[V(t),\ P_{V(t)}H(t)].
\]

Every column of `A(t)` lies in `col(V(t))`, so `rank A(t) <= P-k`, while

\[
W(t)-A(t)=[0,(I-P_{V(t)})H(t)].
\]

The Eckart--Young--Mirsky theorem therefore gives the exact lower bound

\[
\boxed{
\operatorname{tr}S(t)
\ge
\sum_{\ell=P-k+1}^{P}\sigma_\ell(W(t))^2.
}
\tag{8}
\]

This is the key strengthening over the fixed-period argument. A single collapsing singular value can destroy a determinant or `sigma_min` bound, but screening `k` omitted directions in Frobenius energy requires collapse of the whole bottom `k` singular-value tail.

## 3. Uniform transfer to the reciprocal-node Vandermonde

Use Lamzouri's optimizing profile

\[
f_0(x)=\frac{\cos(\sqrt2x)}{\sqrt2\sin(1/\sqrt2)},
\qquad |x|<1/2,
\]

with the smoothed normalized family from WI-127,

\[
\eta_\delta(x)=\frac{\psi_\delta(x)\sqrt{f_0(x)}}{\sqrt{A_\delta}},
\qquad A_\delta\le1.
\]

Choose `delta <= 1/(4P)` and restrict the fiber variable to

\[
E_P=
\left[-\frac12+\frac1{4P},
      -\frac12+\frac3{4P}\right],
\qquad |E_P|=\frac1{2P}.
\tag{9}
\]

For every `t in E_P` and every `0<=r<P`, the point `t+r/P` lies in the flat core of the cutoff. Since `f_0` is positive and minimized at the endpoints of `(-1/2,1/2)`,

\[
s_{\min}(D_\eta(t))
\ge\sqrt{f_{\min}},
\qquad
f_{\min}:=f_0(1/2)
=\frac{\cos(1/\sqrt2)}{\sqrt2\sin(1/\sqrt2)}.
\tag{10}
\]

Assume the normalized horizontal depths in the cell satisfy

\[
|\operatorname{Im}\zeta_j|\le B.
\tag{11}
\]

Because `|t|<=1/2`,

\[
s_{\min}(D_t)\ge e^{-\pi B}.
\tag{12}
\]

For singular values ordered as `sigma_1 >= ... >= sigma_P`, the standard product inequality

\[
\sigma_\ell(AXB)
\ge s_{\min}(A)s_{\min}(B)\sigma_\ell(X)
\]

applied to (3)--(5) yields, for every `ell`,

\[
\boxed{
\sigma_\ell(P^{-1/2}W(t))^2
\ge
\frac{f_{\min}e^{-2\pi B}}2
\sigma_\ell(\widetilde{\mathcal V}_P)^2,
}
\tag{13}
\]

where

\[
\widetilde{\mathcal V}_P=P^{-1/2}\mathcal V_P.
\]

Combining (6), (8), and (13), then integrating only over `E_P`, gives

\[
\begin{aligned}
\sum_{j=1}^{k}\operatorname{dist}(h_j,V_\infty)^2
&\ge
|E_P|\,P\,
\frac{f_{\min}e^{-2\pi B}}2
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2\\
&=
\boxed{
\frac{f_{\min}e^{-2\pi B}}4
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2.
}
\end{aligned}
\tag{14}
\]

The constant in (14) is independent of `P`; all period dependence has been moved into the normalized Vandermonde spectral tail itself.

## 4. Repeated cells and the macroscopic near-null condition

Repeat the cell through `M` consecutive periods. As in WI-127, the finite Lamzouri span satisfies `V_M subset V_infty`, and translation by one period preserves `V_infty`. Therefore every repeated copy pays the same lower bound (14). Inserting this into (1) gives

\[
R_H
\ge
M f_{\min}e^{-2\pi B}
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2,
\]

or equivalently the advertised normalized estimate

\[
\boxed{
\frac{R_H}{PM}
\ge
f_{\min}e^{-2\pi B}
\frac1P
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2.
}
\tag{15}
\]

Now let the period grow along a sequence with

\[
\frac{k}{P}\ge\rho>0,
\qquad
|\operatorname{Im}\zeta_j|\le B,
\qquad
\frac{R_H}{PM}\longrightarrow0.
\tag{16}
\]

Equation (15) forces

\[
\frac1P
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2
\longrightarrow0.
\tag{17}
\]

Since `k/P>=rho`, also

\[
\boxed{
\frac1k
\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2
\longrightarrow0.
}
\tag{18}
\]

Consequently, for every fixed `epsilon>0`, Markov's inequality shows that only `o(k)=o(P)` members of this bottom sector can have `sigma_ell^2 >= epsilon`. Equivalently, the empirical singular-value distribution of `\widetilde{\mathcal V}_P` must place asymptotic mass at least `rho` in every fixed neighborhood of zero.

This is substantially more rigid than `sigma_min(\widetilde{\mathcal V}_P)->0`. One or finitely many nearly dependent modes are insufficient: a positive-density off-line sector can horizontally screen only if the reciprocal-node system develops a **macroscopic low-energy subspace**.

If the non-real depths also obey `|Im zeta_j|>=b_0>0`, then within each mirror pair

\[
P|\omega_+-\omega_-|
=2P\sinh\left(\frac{2\pi|\operatorname{Im}\zeta|}{P}\right)
\ge4\pi b_0.
\tag{19}
\]

Thus the extensive collapse in (18) cannot then be attributed merely to each conjugate pair coalescing onto the critical line. It must come from collective/inter-pair reciprocal-node geometry or from a source-incompatible density distortion.

## 5. A growing-period all-off-line lattice does not screen

The condition above is non-vacuous even when `P->infinity`. Take `P=2M` and an all-off-line cell

\[
\zeta_{j,\pm}=2j\pm ib,
\qquad j=0,\ldots,M-1,
\qquad b>0.
\tag{20}
\]

Its reciprocal nodes are

\[
r u_j,\quad r^{-1}u_j,
\qquad
u_j=e^{-2\pi ij/M},
\qquad
r=e^{\pi b/M}.
\]

A unitary discrete Fourier transform across the `M` centers block-diagonalizes `\widetilde{\mathcal V}_{2M}` into `M` two-by-two blocks

\[
B_q=\frac1{\sqrt2}
\begin{pmatrix}
r^q&r^{-q}\\
r^{q+M}&r^{-(q+M)}
\end{pmatrix},
\qquad q=0,\ldots,M-1.
\tag{21}
\]

Each block has

\[
|\det B_q|=\sinh(\pi b)
\tag{22}
\]

and

\[
\|B_q\|_F^2
=\cosh\left(\frac{2\pi bq}{M}\right)
 +\cosh\left(\frac{2\pi b(q+M)}{M}\right)
\le
\cosh(2\pi b)+\cosh(4\pi b).
\tag{23}
\]

For a two-by-two matrix, `sigma_min^2 >= |det|^2/||B||_F^2`; hence every block obeys

\[
\sigma_{\min}(B_q)^2
\ge
c_b:=
\frac{\sinh^2(\pi b)}
{\cosh(2\pi b)+\cosh(4\pi b)}
>0.
\tag{24}
\]

Therefore every singular value of the block diagonal matrix is at least `sqrt(c_b)`, and in particular its bottom `M=P/2` squared singular values satisfy

\[
\boxed{
\frac1P
\sum_{\ell=M+1}^{2M}
\sigma_\ell(\widetilde{\mathcal V}_{2M})^2
\ge\frac{c_b}{2}>0.
}
\tag{25}
\]

Equation (15) then gives a period-uniform positive Lamzouri horizontal charge. Merely increasing the period, even with every label off the line, is therefore not enough to manufacture screening. A successful countermodel must engineer genuinely collective spectral collapse.

## 6. Why determinant-only refinements are too weak

A natural first route was to combine the Schur-complement identity

\[
\det S=\frac{|\det W|^2}{\det(V^*V)}
\]

with WI-127's explicit Vandermonde discriminant. That route is insufficient for the present objective. A determinant is a geometric-mean observable: one extremely small residual singular direction can make it tiny while the other `k-1` anti-invariant directions remain macroscopically transverse. It therefore cannot certify or falsify screening of a positive-density off-line population.

Equation (8) is the robust replacement. The horizontal remainder is a Frobenius-energy quantity, so its correct spectral counterpart is the **sum of the bottom `k` squared singular values**, not their product and not only the minimum. This closes the determinant-only route as a useful bootstrap invariant unless additional information controls the entire singular spectrum.

## 7. Prior-art audit and provenance

The low-rank approximation step is the classical Eckart--Young--Mirsky theorem; the singular-value product inequalities are standard matrix analysis. No novelty is claimed for either.

The relevant Vandermonde-conditioning literature is extensive. Céline Aubel and Helmut Bölcskei, *Vandermonde Matrices with Nodes in the Unit Disk and the Large Sieve*, Applied and Computational Harmonic Analysis 47 (2019), 53--86, derive extremal singular-value and condition-number bounds for nodes in the unit disk using large-sieve methods (preprint arXiv:1701.02538). Ankur Moitra, *Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices*, STOC 2015, arXiv:1408.1681, identifies sharp separation/conditioning phenomena for unit-circle Vandermonde systems. Stefan Kunis, Dominik Nagel and Anna Strotmann, *Multivariate Vandermonde matrices with separated nodes on the unit circle are stable*, Applied and Computational Harmonic Analysis 58 (2022), 50--59, give explicit lower singular-value bounds under quantitative separation. Dmitry Batenkov, Benedikt Diederichs, Gil Goldman and Yosef Yomdin, *The spectral properties of Vandermonde matrices with clustered nodes*, Linear Algebra and Its Applications 609 (2021), 37--72, analyze all singular values in clustered unit-circle regimes.

These results materially redirect what a next proof should try to control, but none directly settles (17) for the present reciprocal-node geometry. Here conjugate pairs naturally produce reciprocal nodes on opposite sides of the unit circle, the matrix is square at critical density, and arbitrary growing-period cells may have clustering at the `1/P` scale or worse. No unconditional zeta input currently audited in this line supplies the separation or bounded-cluster hypotheses needed to invoke the cited stability theorems uniformly.

A targeted search around Lamzouri's September 2026 preprint, Vandermonde spectral tails, large-sieve conditioning, super-resolution, clustered nodes, and periodic exponential systems found the standard ingredients above but no statement combining Lamzouri's `g/h` horizontal remainder with a positive-density bottom singular-value tail. Absence from that search is not evidence of priority, and no priority claim is made. The durable line-specific deduction is the exact combination of WI-126's horizontal slack, WI-127's fiberization, and classical low-rank approximation leading to (15)--(18).

References:

- Lamzouri: https://arxiv.org/abs/2609.02882
- Aubel--Bölcskei: https://arxiv.org/abs/1701.02538
- Moitra: https://arxiv.org/abs/1408.1681
- Kunis--Nagel--Strotmann: https://doi.org/10.1016/j.acha.2022.01.001
- Batenkov--Diederichs--Goldman--Yomdin: https://arxiv.org/abs/1909.01927

## 8. Scope, barriers, and falsification tests

The result remains a periodic-model statement. It does not prove that the actual zeta exceptional set has a cell structure, nor does it solve the external-reservoir problem: adding arbitrary vectors outside the repeated block enlarges Lamzouri's `V` and can reduce selected distances. A zeta application also needs a legitimate diagonal passage between period size, block length, smoothing, and height.

The bounded-depth assumption (11) is load-bearing for a period-uniform comparison with the raw reciprocal-node Vandermonde. If normalized horizontal depths grow with `P` or with zeta height, the factor `e^{-2 pi B}` degenerates. Critical-line multiplicity remains a separate population: when a mirror pair approaches the line, reciprocal nodes coalesce and the spectral collapse is compatible with WI-126's fact that a real double can have zero horizontal cost.

Nor does Fujii number variance from WI-121 by itself prove the needed spectral-tail lower bound. It rules out positive-density long/macroscopic count islands, but microscopic reciprocal-node clustering can be spectrally destructive without creating the same count discrepancy. Higher correlations, local multiplicity/zero-density control, or a direct nonharmonic-Fourier/Riesz lower-tail theorem compatible with actual zeta statistics would be genuinely new input.

The most useful next tests are therefore sharp and falsifiable. On the positive side, seek a theorem of the form

\[
\liminf_{P\to\infty}
\frac1P\sum_{\ell=P-k+1}^{P}
\sigma_\ell(\widetilde{\mathcal V}_P)^2>0
\]

under source-compatible zeta constraints with `k/P>=rho` and non-vanishing horizontal depth. On the adversarial side, construct a growing-period or aperiodic, density-one conjugation-symmetric cell satisfying the known count/correlation constraints while making this tail `o(P)`. Either outcome materially advances the defect-to-zero program.

A direct algebraic falsifier of the present finding would be a cell satisfying the hypotheses of (11) for which the pointwise rank-`k` residual in (8) is smaller than the bottom-`k` singular-value tail, or a repeated-cell family violating (15). Both are excluded by Eckart--Young--Mirsky plus the exact WI-127 fiber factorization; the remaining uncertainty is entirely in whether zeta-source constraints can prevent the spectral collapse demanded by (18).

## 9. Evidence anchors and relation to the line

- `research/weil_inertia/findings/WI-126-lamzouri-hilbert-slack-separates-offline-transversality.md` — exact horizontal remainder (1) and the separation between off-line pairs and real doubles.
- `research/weil_inertia/findings/WI-127-fixed-period-cells-have-extensive-lamzouri-transversality.md` — periodic fiberization, reciprocal-node Vandermonde factorization, smoothing-uniform common fiber region, and repeated-cell interface.
- Youness Lamzouri, arXiv:2609.02882v1 — primary source for the finite Hilbert-space inequality and `f/g/h` decomposition.
- Classical matrix approximation plus the audited Vandermonde-conditioning literature above — literature-backed spectral context; no theorem from that literature is silently imported beyond its stated hypotheses.

**Research implication.** WI-127 left growing-period conditioning as a scalar `sigma_min` loophole. The correct loophole is much narrower: with bounded horizontal depth and positive off-line pair density, subextensive Lamzouri horizontal slack requires an extensive near-null sector of the normalized reciprocal-node Vandermonde. This gives the next bootstrap a quantitative target that is simultaneously strong enough to match the population being screened and weak enough not to demand uniform invertibility of every spectral direction.