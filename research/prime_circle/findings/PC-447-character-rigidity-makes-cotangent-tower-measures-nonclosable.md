# PC-447 — Character rigidity makes cotangent tower measures nonclosable

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. The unchanged complete cotangent tower has no closed extension on any full-support probability for which nontrivial fiber characters approach the constant function while their rational frequencies approach zero. Every full-support purely atomic probability has this property. An explicit full-support **nonatomic singular** probability also has it. This is an existence obstruction for an operator realization, not a statement about the spectrum of a nonexistent closure or a classification of all singular measures.

## 1. Fixed object and precise obstruction

Use the fixed finite base and complete power-preimage tower of PC-443 and PC-446:
\[
B=P_d^*,\quad r=\varphi(d),\quad
Y_m=\{y\in S^1:y^m\in B\},\quad
X=\varprojlim_mY_m.
\tag{1}
\]
Write the base points as \(\beta_a=e^{2\pi i\theta_a}\), with distinct \(\theta_a\in[0,1)\). The coherent lifts
\(e^{2\pi i(\theta_a+t)/m}\) identify \(X\) with \(B\times\widehat{\mathbb Z}\). In these coordinates let
\[
\chi_q(z)=e^{2\pi i j(z\bmod m)/m},\qquad q=j/m\in\mathbb Q/\mathbb Z.
\tag{2}
\]
This is independent of the representation of \(q\). Throughout, \(q\downarrow0\) refers to its **real representative**, not to convergence in the discrete Pontryagin dual.

On the cylinder domain \(\mathcal A_{\rm cyl}=\bigcup_m\mathbb C^{Y_m}\), retain either prescription
\[
\mathcal B|_{\mathbb C^{Y_m}}=C_{d,m}/m,
\qquad
\mathcal B^+|_{\mathbb C^{Y_m}}=(C_{d,m}+J_m)/m.
\tag{3}
\]
PC-446 proves these are well-defined on all cylinder classes in \(L^2(X,\nu)\) exactly when the Borel probability \(\nu\) has full support.

**Theorem.** Suppose \(\nu\) has full support and there are rational representatives \(q_k\in(0,1/2)\) such that
\[
q_k\longrightarrow0,
\qquad \|\chi_{q_k}-1\|_{L^2(\nu)}\longrightarrow0.
\tag{4}
\]
Then both operators in (3) are **nonclosable**. In fact there are explicit cylinder functions, using only the two nonzero sectors \(q_k,-q_k\), such that
\[
f_k\longrightarrow0,
\qquad \mathcal B f_k=\mathcal B^+ f_k\longrightarrow2\mathbf1
\quad\text{in }L^2(\nu).
\tag{5}
\]
Thus the obstruction also survives an arbitrary change to the zero-character block, restriction to the span of nonzero-character sectors, or addition of an operator bounded on \(L^2(\nu)\). In the restriction statement, the original action on all the nonzero sectors is retained.

This answers a question left explicitly open in PC-446: full support alone can give a valid dense cylinder prescription with **no closed realization at all**, not merely an undesirable spectral band if a realization exists.

## 2. The exact jump between opposite character sectors

Let \(H\) have diagonal zero and off-diagonal entries
\(H_{ac}=i\cot(\pi(\theta_a-\theta_c))\), and put
\[
A=H+J_r,\qquad D_q=\operatorname{diag}(e^{2\pi i q\theta_a}),\qquad U=D_1.
\tag{6}
\]
The finite Fourier formula of PC-053, compatible at every level by PC-443, gives for \(0<q<1\) and every \(v\in\mathbb C^r\)
\[
\mathcal B^{(+)}(\chi_qv)=\chi_qK(q)v,
\qquad K(q)=D_qAD_q^{-1}-2qI.
\tag{7}
\]
Here \((\chi_qv)(a,z)=\chi_q(z)v_a\). No orthogonality with respect to \(\nu\) is required for this pointwise identity.

The source kernel has the exact endpoint relation
\[
UAU^{-1}-2I=H-J_r.
\tag{8}
\]
Indeed, for \(a\ne c\),
\[
H_{ac}=\frac{\beta_c+\beta_a}{\beta_c-\beta_a},\qquad
A_{ac}=\frac{2\beta_c}{\beta_c-\beta_a},\qquad
(UAU^{-1})_{ac}=\frac{2\beta_a}{\beta_c-\beta_a}=H_{ac}-1.
\]
On the diagonal, \(1-2=-1\). Consequently
\[
\lim_{q\downarrow0}K(q)=H+J_r,
\qquad \lim_{q\downarrow0}K(1-q)=H-J_r.
\tag{9}
\]
The discontinuity is the nonzero rank-one matrix \(2J_r\), including when \(r=1\).

Take \(v=r^{-1}\mathbf1_r\), so \(J_rv=\mathbf1_r\), and set
\[
f_k=\chi_{q_k}v-\chi_{-q_k}v.
\tag{10}
\]
Because \(\chi_{-q_k}=\overline{\chi_{q_k}}\), (4) implies \(f_k\to0\). Equations (7)--(9) give
\[
\mathcal B^{(+)}f_k
=\chi_{q_k}K(q_k)v-\chi_{-q_k}K(1-q_k)v
\longrightarrow2J_rv=2\mathbf1.
\tag{11}
\]
To justify convergence even for correlated base/fiber measures, the finite vectors \(K(q_k)v\) and \(K(1-q_k)v\) converge in the maximum norm, while multiplication of \(\chi_{\pm q_k}-1\) by a uniformly bounded vector has \(L^2(\nu)\) norm tending to zero. No equivalence to Haar or weighted Fourier-basis bound enters.

A closed extension would contain the limit graph point \((0,2\mathbf1)\), impossible for a linear operator. The same sequence proves nonclosability after adding any bounded operator, since its value on \(f_k\) tends to zero. It never uses the zero-character action. Moreover, the span of nonzero sectors is itself dense under (4): each base vector \(v\) is the \(L^2(\nu)\) limit of \(\chi_{q_k}v\), and adjoining base vectors gives the full cylinder algebra.

## 3. Every purely atomic full-support probability meets the criterion

Let
\[
\nu=\sum_{i\ge1}w_i\delta_{(a_i,z_i)},\qquad w_i>0,\quad\sum_iw_i=1,
\tag{12}
\]
with full support. No hypothesis that the \(z_i\) are ordinary integers is made.

For each integer \(k\ge3\), choose an integer \(m_k>k^{k+1}\), and put
\(\alpha_i=(z_i\bmod m_k)/m_k\) for \(1\le i\le k\).
Partition \([0,1)^k\) into \(k^k\) boxes of side \(1/k\), and place the \(k^k+1\) points
\(\ell(\alpha_1,\ldots,\alpha_k)\bmod1\), \(0\le\ell\le k^k\), into them. Two share a box. Their index difference \(j_k\) satisfies
\[
1\le j_k\le k^k<m_k/k,
\qquad \|j_k\alpha_i\|_{\mathbb R/\mathbb Z}<1/k\quad(i\le k).
\tag{13}
\]
Thus \(q_k=j_k/m_k\in(0,1/k)\) is nonzero and
\[
\|\chi_{q_k}-1\|_{L^2(\nu)}^2
\le \frac{4\pi^2}{k^2}+4\sum_{i>k}w_i\longrightarrow0.
\tag{14}
\]
This is the classical simultaneous Dirichlet pigeonhole argument, with the large denominator chosen *before* approximating the finitely many profinite residues. It applies in particular to every dense countable-support probability considered as a possible singular realization in PC-446. Those prescriptions are well-defined but never closable.

## 4. Nonatomicity does not repair the failure

Fix any prime \(p\), and use
\[
\widehat{\mathbb Z}=\mathbb Z_p\times G^{(p)},\qquad
G^{(p)}=\prod_{\ell\ne p}\mathbb Z_\ell.
\]
Let \(h^{(p)}\) be Haar probability on \(G^{(p)}\), and define
\[
\eta=\left(\sum_{n=0}^\infty2^{-n-1}\delta_n^{\mathbb Z_p}\right)
\otimes h^{(p)},\qquad
\nu=\frac1r\sum_{a\in B}\delta_a\otimes\eta.
\tag{15}
\]
Every nonempty finite congruence cylinder has positive mass: the nonnegative integers meet every residue class modulo a power of \(p\), and the other prime coordinates have Haar marginals. Hence \(\nu\) has full support. It is nonatomic because \(h^{(p)}\) is nonatomic. It is singular to the canonical tower probability \(\mu\), since its \(p\)-coordinate belongs to the Haar-null countable set of nonnegative integers.

For \(q_k=p^{-k}\), the character depends only on the \(p\)-coordinate, and on the component indexed by \(n\) it equals \(e^{2\pi i n/p^k}\). In particular
\[
\int_X\chi_{q_k}\,d\nu
=\sum_{n\ge0}2^{-n-1}e^{2\pi i n/p^k}
=\frac1{2-e^{2\pi i/p^k}}\longrightarrow1,
\tag{16}
\]
which proves (4). Quantitatively, \(\sum_{n\ge0}2^{-n-1}n^2=3\) gives
\[
\|\chi_{q_k}-1\|_{L^2(\nu)}^2\le 12\pi^2p^{-2k}.
\tag{17}
\]
Both raw cotangent prescriptions are therefore nonclosable on this full-support nonatomic singular probability too.

For comparison, under Haar every nonzero character satisfies \(\|\chi_q-1\|_\mu^2=2\). More generally (4) forces \(\nu\) to be purely singular to \(\mu\): if \(w\mu\) is its absolutely continuous part, Fourier vanishing at infinity gives
\[
\int |\chi_{q_k}-1|^2w\,d\mu\longrightarrow2\int w\,d\mu.
\tag{18}
\]
Here \(q_k\to0\) through nonzero rational representatives leaves every finite subset of \(\mathbb Q/\mathbb Z\). The needed Fourier vanishing can also be proved by approximating \(w\) in \(L^1(\mu)\) by cylinder functions: the integral of a sufficiently high-denominator character against a fixed cylinder function is zero. The left side of (18) is bounded by the squared norm in (4), so \(w=0\). **The converse is not asserted:** general singular measures, mixed measures and arbitrary unbounded densities are not classified here.

## 5. Controls, prior art, validation and research boundary

Equations (6)--(11) hold for every finite set of distinct circle points, with the same actual cotangent kernel and complete power preimages. Thus the theorem and both classes of examples hold on geometrically matched bases containing irrational angles. The obstruction is a character-limit/symbol-jump incompatibility, not prime-birth information. The prime \(p\) in (15) merely selects a profinite coordinate for an explicit control measure.

The ingredients are classical. E. Kowalski, *Spectral theory in Hilbert spaces*, ETH Zürich lecture notes (2009), §4.2, Lemma 4.13, gives the graph-closure criterion used in (11) ([author's notes](https://people.math.ethz.ch/~kowalski/spectral-theory.pdf)). Simultaneous approximation in (13) is proved here by the usual Dirichlet box argument. Fourier recurrence of continuous measures is established harmonic-analysis territory; see C. Badea and S. Grivaux, *Kazhdan constants, continuous probability measures with large Fourier coefficients and rigidity sequences*, Comment. Math. Helv. **95** (2020), 99–127, DOI [10.4171/CMH/482](https://doi.org/10.4171/CMH/482), [arXiv:1804.01369](https://arxiv.org/abs/1804.01369). That paper is neighboring circle-measure prior art, not a theorem about this profinite cotangent prescription. Our explicit measure and recurrence are established by (15)--(17).

No novelty is claimed for closability, simultaneous approximation or Fourier rigidity. The line-local result is their exact combination with the **two-sided rank-one cotangent jump**, showing that an entire class of full-support singular realizations fails to exist even after discarding the constant sector. This differs from PC-178's semibounded Toeplitz-form criterion and PC-377's coefficient-summability obstruction; neither applies the present operator to a changed probability on the same cylinder-function space.

**Validation.** The proofs above are exact. Separate floating-point diagnostics checked the endpoint identity (8) for bases \(d=2,3,4,5\) and the irrational-angle base \(\{\sqrt2,\sqrt3,\sqrt5\}\bmod1\), with maximum entry residual \(8.1\times10^{-16}\). Direct complete-tube matrices at \(m=3,5,8\), at both characters \(j=1,m-1\), agreed with (7) to maximum absolute residual \(5.9\times10^{-14}\). For the one-point base and (15) with \(p=2\), exact geometric-series moment formulas give, at \(k=10\), \(\|f_k\|\approx0.021252\) and \(\|\mathcal B f_k-2\|\approx0.004031\). These are diagnostics, not evidence for the infinite limit in place of the proof. The decisive audit points are the sign in (8), the nonzero opposite-sector inputs (10), the simultaneous approximation quantifiers (13), and full support versus nonatomicity in (15).

PC-446 excludes compact resolvent for every closed realization retaining all cylinder eigenvectors. The present result settles an earlier existence gate for the measures in (4): there is no closed realization to spectralize. It does not strengthen that conditional spectral inclusion to an equality, and says nothing about the spectra of nonclosable prescriptions. Changed kernels, domains that omit the witness sequences, incomplete fibers, half-density-compensated operators and growing-base limits remain outside the theorem. No RH implication or complete singular-measure classification follows.
