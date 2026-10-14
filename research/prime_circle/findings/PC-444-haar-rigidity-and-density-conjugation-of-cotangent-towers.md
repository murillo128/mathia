# PC-444 — Haar rigidity and density-conjugation dichotomy for profinite cotangent towers

**Status:** EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. For the coherent, fixed-base, complete preimage-tube cotangent operator of PC-443, the unchanged cylinder action has a symmetric realization on $L^2(X,\nu)$ for a Borel probability $\nu$ **only** when $\nu$ is the canonical Haar probability. This includes measures without assumed full support or absolute continuity. In contrast, compensating an arbitrary equivalent measure by the canonical half-density unitary produces exactly the old self-adjoint spectrum; and bounded equivalent changes of measure leave even the **uncompensated** operator boundedly similar to the Haar operator, with a Riesz eigenbasis. These are elementary operator-theoretic principles applied to the intrinsic Prime-Circle refinement system, not a new RH mechanism.

## 1. Operator and three precisely different measure prescriptions

Fix $d>1$, $r=\varphi(d)$, and the PC-443 inverse system
\[
Y_m=\{y\in S^1:y^m\in P_d^*\},\qquad X=\varprojlim_mY_m,\qquad
\mathcal A_{\rm cyl}=\bigcup_m\mathbb C^{Y_m}.
\tag{1}
\]
The inclusions are the actual power-map pullbacks $P_{m,n}$ for $m\mid n$, and $\mu$ is the unique probability with uniform marginal on every $Y_m$. Write
\[
B_m=C_{d,m}/m,\qquad B_m^+=(C_{d,m}+J_m)/m.
\tag{2}
\]
PC-443 proves $B_n^{(+)}P_{m,n}=P_{m,n}B_m^{(+)}$, so each family gives a well-defined pointwise map $\mathcal B^{(+)}:\mathcal A_{\rm cyl}\to\mathcal A_{\rm cyl}$. Its bounded self-adjoint Haar realization on $\mathcal H_\mu=L^2(X,\mu)$ is $B_\mu^{(+)}$.

**Theorem (Haar rigidity).** Let $\nu$ be any Borel probability on $X$. Suppose the *unchanged* pointwise cylinder prescription $\mathcal B$ (or $\mathcal B^+$) descends to an operator on $L^2(X,\nu)$, its domain contains every cylinder-function class, and that operator admits a symmetric extension. Then
\[
\boxed{\nu=\mu.}
\tag{3}
\]
No full-support, non-atomicity, equivalence-of-measures, bounded-density, or bounded-operator hypothesis is needed. In particular no non-Haar probability can make the original cotangent prescription self-adjoint merely by changing the Hilbert-space measure.

**Theorem (two distinct reweightings).** For any probability $\nu=w\mu$ with $0<w<\infty$ $\mu$-almost everywhere, the multiplication map
\[
U_w:L^2(X,\nu)\longrightarrow L^2(X,\mu),\qquad U_w f=\sqrt w\,f
\tag{4}
\]
is unitary. The *compensated* operator
\[
B_{\nu}^{\rm hd,(\!+\!)}
=U_w^{-1}B_\mu^{(+)}U_w
\tag{5}
\]
is bounded self-adjoint and has precisely the same spectrum, essential spectrum and spectral multiplicities as $B_\mu^{(+)}$, **even if $w$ or $1/w$ is unbounded**. It is a changed operator, generally not the original cylinder prescription.

If additionally $0<c\le w\le C<\infty$ $\mu$-almost everywhere, the *uncompensated* cylinder prescription extends to a bounded operator $B_\nu^{\rm raw,(\!+\!)}$ on $L^2(X,\nu)$, and the bounded invertible identity map $I_{\nu\to\mu}$ intertwines it with $B_\mu^{(+)}$. Therefore
\[
\boxed{
\sigma(B_\nu^{\rm raw,(\!+\!)})=\sigma(B_\mu^{(+)}),\qquad
\sigma_{\rm ess}^{\rm Fredholm}(B_\nu^{\rm raw,(\!+\!)})
=\sigma_{\rm ess}^{\rm Fredholm}(B_\mu^{(+)}).
}
\tag{6}
\]
The Haar eigenvectors of PC-443 remain a Riesz basis of eigenvectors for the raw operator. When $w$ is nonconstant, the raw operator is not symmetric (and, since its spectrum is real, not normal). The spectral *type* of the nonnormal raw realization should not be confused with the spectral type of the self-adjoint compensated one.

## 2. Proof of rigidity, including zero-mass cylinders

Let $p_m(x)=\nu(\{z:\pi_m(z)=x\})$ for $x\in Y_m$. The indicator $e_x$ of that cylinder belongs to $\mathcal A_{\rm cyl}$. Since $B_m$ is Hermitian in the **pointwise** basis, symmetry on the classes of $e_x,e_y$ requires
\[
\bigl(p_m(x)-p_m(y)\bigr)(B_m)_{xy}=0
\qquad(x\ne y).
\tag{7}
\]
This calculation does not divide by any $p_m(x)$, so it remains valid when cylinder masses vanish. It is also a necessary condition when the map fails to descend on null classes; in that case a symmetric realization is already impossible.

Write $x=e^{2\pi i\theta_x}$ for distinct points of $Y_m$. For the unchanged cotangent kernel,
\[
(B_m)_{xy}=\frac{i}{m}\cot\bigl(\pi(\theta_x-\theta_y)\bigr)
\quad(x\ne y).
\tag{8}
\]
Its off-diagonal zero occurs **only** when $x$ and $y$ are antipodal. Every circle point has at most one antipode, so on any set with at least three distinct points the graph whose edges have $(B_m)_{xy}\ne0$ is connected. Equation (7) therefore forces all $p_m(x)$ to agree when $|Y_m|\ge3$. The sum of the masses is one, so
\[
p_m(x)=\frac1{m\varphi(d)}\quad\text{for every }m\ge3.
\tag{9}
\]
The low-level exceptional graphs do not create alternative measures: for an arbitrary $m=1,2$, project from level $3m$, whose masses are already uniform. Every point of $Y_m$ has three preimages, giving (9) at those levels as well. The cylinder sets at all levels generate the Borel sigma-algebra of the profinite inverse limit, so (9) uniquely identifies $\nu=\mu$.

For the augmented family, the off-diagonal entries are $(1+i\cot(\pi(\theta_x-\theta_y)))/m$, which are **never zero** for distinct circle points. The same conclusion follows, including the exceptional two-point antipodal level. This proves (3) for either family.

## 3. Proof of spectral invariance and its sharp boundary

For every $0<w<\infty$ almost everywhere, (4) is unitary because $\|U_wf\|_\mu^2=\int|f|^2w\,d\mu=\|f\|_\nu^2$; surjectivity follows by applying $1/\sqrt w$ to an arbitrary $L^2(\mu)$ function. Formula (5) is therefore a unitary transport of the PC-443 self-adjoint operator, with no norm bounds required on $w$. Its exact spectral law remains the direct sum of the rational-character blocks (PC-443, equations (8)--(11)). Compensation changes the pointwise formula whenever $w$ is not constant.

Under $0<c\le w\le C$, the two Hilbert norms on cylinder functions satisfy
\[
c\|f\|_\mu^2\le\|f\|_\nu^2\le C\|f\|_\mu^2.
\tag{10}
\]
The identity from $L^2(\nu)$ to $L^2(\mu)$ and its inverse are bounded with norm product at most $\sqrt{C/c}$. Compatibility (2) identifies the same cylinder action on both sides, hence $I_{\nu\to\mu}B_\nu^{\rm raw}=B_\mu I_{\nu\to\mu}$ and likewise with augmentation. Invertible bounded similarity gives (6), including Fredholm essential spectra, and for $z$ outside the Haar spectrum gives the quantitative bound
\[
\left\|(B_\nu^{\rm raw,(\!+\!)}-z)^{-1}\right\|_{\nu}
\le
\frac{\sqrt{C/c}}{\operatorname{dist}(z,\sigma(B_\mu^{(+)}))}.
\tag{11}
\]
If $(\psi_j)$ is the orthonormal eigenbasis assembled from PC-443's finite rational-character blocks, it remains a complete raw eigenvector family, with
\[
c\sum_j|a_j|^2\le
\left\|\sum_j a_j\psi_j\right\|_\nu^2
\le C\sum_j|a_j|^2
\tag{12}
\]
for finite coefficient families. This is exactly the Riesz-basis estimate.

Equation (3) simultaneously shows that the *raw* operator is symmetric only for $w=1$ almost everywhere (since $\nu$ is a probability). A bounded operator with real spectrum that is normal would be self-adjoint, so a nonconstant bounded reweighting is also nonnormal. The similarity claims **do not** cover the uncompensated operator for unbounded or vanishing densities; norm equivalence and even a well-defined bounded raw realization may then fail. The *compensated* construction covers arbitrary equivalent probabilities but is unitarily the old model, not a spectral escape. Singular measures or genuinely modified cotangent kernels lie outside the compensated transport (4)--(5).

## 4. Matched controls, prior art and consequence

Repeat the entire construction with any finite set of $r$ **distinct non-root-of-unity** base points and their complete power-map preimages, preserving the oriented cotangent kernel and normalized refinement maps as in PC-443's equation (20). Off-diagonal cotangent entries still vanish only for antipodal pairs, so the connectivity argument, Haar uniqueness, half-density conjugation, and bounded-similarity/Riesz conclusions hold word for word. Exact base-band endpoints may change with the chosen points; the measure-rigidity mechanism and invariance under reweighting do not detect primality or cyclotomic birth data.

**Prior art and novelty:** The equation $WB=BW$ for a Hermitian matrix and a diagonal weight matrix, connectivity of its nonzero-entry graph, the uniqueness of projectively consistent finite uniform marginals, unitary change of measure and bounded-similarity spectral invariance are standard finite matrix, measure and operator theory. The Haar/Pontryagin framework is anchored by G. B. Folland, *A Course in Abstract Harmonic Analysis*, 2nd ed. (2016), already listed in this line's SOURCES.md; the Riesz-basis background is anchored there by O. Christensen, *An Introduction to Frames and Riesz Bases*, 2nd ed. (2016), DOI 10.1007/978-3-319-25613-9. The cotangent specialization uses the exact matrices of PC-053 and compatible limit of PC-443. No originality is claimed for the abstract measure/similarity lemmas. The line-local increment is their **simultaneous all-refinement rigidity statement without a measure-support assumption**, together with the explicit distinction between unchanged, half-density-compensated and boundedly similar spectral realizations.

**RH boundary:** Changing the Hilbert-space probability alone cannot create a different self-adjoint realization of the *unchanged* complete-tube cotangent action. Unitary half-density transport cannot change its spectrum, and bounded equivalent reweighting cannot change even the spectrum of the nonnormal raw action. This closes precisely these measure-only modifications of the fixed-$d$ PC-443 tower; it does not rule out an independently source-forced change of operator, singular limits that change domains, incomplete fibers, or a simultaneous growing-$d$ regime. Nothing here supplies a new implication toward RH.

**Decisive audit:** Verify (7) for arbitrary nonnegative cylinder masses, not only strictly positive ones; check the cotangent zero graph and its antipodal exceptions at $(d,m)=(2,2),(4,1)$, followed by connectivity at $(2,3)$ and a generic larger level. Verify that uniform pushforward from $3m$ fixes every exceptional lower marginal. Test the compensated unitary on an unbounded but positive density as well as a bounded nonconstant weight, and check (10)--(12) directly. Any admissible non-Haar measure supporting a symmetric unchanged cylinder action, or any difference in the spectra under the stated unitary or bounded similarity, would falsify the corresponding theorem.
