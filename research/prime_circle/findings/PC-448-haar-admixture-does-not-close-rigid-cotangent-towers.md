# PC-448 — Haar admixture does not close rigid cotangent towers

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. A nonzero character-rigid singular component makes the unchanged complete cotangent tower nonclosable even after adding an arbitrary absolutely continuous component. In particular, nonclosable probabilities occur arbitrarily close to Haar in total variation and can dominate a positive multiple of Haar. Bounded positive cylinder-density approximations to a Haar-plus-atom example retain the Haar spectrum, but their raw operator norms diverge at least as the square root of the refinement level. These are existence and stability boundaries for one fixed operator prescription, not a classification of all singular measures or an RH result.

## 1. Fixed prescription and mixed-measure theorem

Use PC-443's complete power-preimage tower over a fixed finite base
\[
B=P_d^*,\quad r=\varphi(d),\quad
Y_m=\{y:y^m\in B\},\qquad
X=\varprojlim_mY_m\simeq B\times\widehat{\mathbb Z}.
\tag{1}
\]
The coordinates are the coherent lifts
\(e^{2\pi i(\theta_a+t)/m}\), where
\(\beta_a=e^{2\pi i\theta_a}\in B\) and \(0\le\theta_a<1\).
Let \(\mu\) be base-uniform times fiber-Haar probability and
\(\chi_{j/m}(z)=e^{2\pi i j(z\bmod m)/m}\). On the full cylinder algebra retain
\[
\mathcal B|_{\mathbb C^{Y_m}}=C_{d,m}/m,
\qquad
\mathcal B^+|_{\mathbb C^{Y_m}}=(C_{d,m}+J_m)/m.
\tag{2}
\]
Here \(J_m\) is the all-ones matrix. Both prescriptions are pointwise refinement-compatible; on \(L^2(\mu)\) they are bounded self-adjoint operators.

**Theorem.** Let \(\nu=\eta+\sigma\) be a full-support Borel probability on \(X\), where \(\eta=w\mu\), \(w\ge0\) is integrable, and \(\sigma\ne0\) is a positive measure singular to \(\mu\). Suppose distinct rational representatives \(q_k\in(0,1/2)\) satisfy
\[
q_k\longrightarrow0,
\qquad \|\chi_{q_k}-1\|_{L^2(\sigma)}\longrightarrow0.
\tag{3}
\]
For a Borel set \(S\) carrying \(\sigma\) with \(\mu(S)=0\), there are cylinder functions \(f_N\) such that
\[
f_N\longrightarrow0,
\qquad
\mathcal B f_N=\mathcal B^+f_N\longrightarrow2\mathbf1_S
\quad\text{in }L^2(\nu).
\tag{4}
\]
Thus neither prescription admits a closed extension. The same conclusion holds after adding any operator bounded on \(L^2(\nu)\), and the witness uses no zero-character input.

Full support ensures that (2) is a well-defined dense-domain prescription, by PC-446. No lower or upper bound on \(w\) is required. The condition \(q_k\to0\) refers to real representatives, not convergence in the discrete Pontryagin dual.

This is not a direct application of PC-447 to \(\nu\): if \(\eta(X)>0\), Fourier vanishing for \(w\mu\) gives
\[
\liminf_k\|\chi_{q_k}-1\|_{L^2(\nu)}^2
\ge 2\eta(X)>0.
\tag{5}
\]
The individual opposite-character witnesses from that finding do not tend to zero in the mixed norm either: the same Fourier vanishing gives their squared norm on the absolutely continuous component the limit \(2\eta(X)/r^2\). Averaging resolves precisely this obstruction.

## 2. Averaging separates the absolutely continuous and rigid parts

Set
\[
H_{aa}=0,\quad H_{ac}=i\cot\bigl(\pi(\theta_a-\theta_c)\bigr),
\quad A=H+J_r,\quad D_q=\operatorname{diag}(e^{2\pi iq\theta_a}).
\]
The exact nonzero-sector formula from PC-053 and PC-443 is
\[
\mathcal B^{(+)}(\chi_qv)=\chi_qK(q)v,
\qquad K(q)=D_qAD_q^{-1}-2qI\quad(0<q<1).
\tag{6}
\]
It is a pointwise formula, independent of the Hilbert-space measure.
For \(U=D_1\), the identity \(UAU^{-1}-2I=H-J_r\) follows on off-diagonal entries from
\[
A_{ac}=\frac{2\beta_c}{\beta_c-\beta_a},\qquad
(UAU^{-1})_{ac}=\frac{2\beta_a}{\beta_c-\beta_a}=H_{ac}-1;
\]
the diagonal entries on both sides are \(-1\). Consequently
\[
K(q)\longrightarrow H+J_r,
\qquad K(1-q)\longrightarrow H-J_r
\quad(q\downarrow0).
\tag{7}
\]

Choose \(v=r^{-1}\mathbf1_r\), so \(J_rv=\mathbf1_r\), and define
\[
g_N^\pm=\frac1N\sum_{k=1}^N\chi_{\pm q_k},
\qquad f_N=(g_N^+-g_N^-)v.
\tag{8}
\]
Each finite sum is a cylinder function at the least common multiple of its character denominators. On the singular component, (3) and the triangle inequality for Cesàro means give \(g_N^\pm\to1\) in \(L^2(\sigma)\). Equations (6)--(7), convergence of finite-dimensional vectors and \(|\chi_q|=1\) then give
\[
f_N\to0,\qquad
\mathcal B^{(+)}f_N
=\frac1N\sum_{k=1}^N
\left(\chi_{q_k}K(q_k)v-\chi_{-q_k}K(1-q_k)v\right)
\longrightarrow2\mathbf1
\quad\text{in }L^2(\sigma).
\tag{9}
\]

On Haar space all \(2N\) characters in (8) are distinct and orthogonal, since \(0<q_k<1/2\). Thus
\[
\|f_N\|_{L^2(\mu)}^2=\frac{2}{r^2N},
\qquad
\|\mathcal B^{(+)}f_N\|_{L^2(\mu)}\longrightarrow0.
\tag{10}
\]
The second assertion uses the bounded Haar realization. Both \(f_N\) and \(\mathcal B^{(+)}f_N\) are also uniformly bounded in the pointwise maximum norm: (8) bounds the first, and the finite-dimensional matrix family \(K(q)\), \(0<q<1\), bounds the second through (9).

If \(h_N\) is either of these uniformly bounded sequences, say \(|h_N|\le M\), then for every \(R>0\)
\[
\int|h_N|^2w\,d\mu
\le R\|h_N\|_{L^2(\mu)}^2
+M^2\int_{\{w>R\}}w\,d\mu.
\tag{11}
\]
First let \(N\to\infty\), then \(R\to\infty\). This proves convergence to zero in \(L^2(\eta)\), even for unbounded \(w\). Together with (9) and mutual singularity, it proves (4). The limiting output has norm \(2\sqrt{\sigma(X)}>0\), so the graph closure contains a nonzero vertical vector. A closed linear operator cannot contain it. A bounded added operator sends \(f_N\) to zero and cannot remove the defect.

## 3. Arbitrarily small singular contamination

For any singular probability \(\tau\) satisfying (3),
\[
\nu_\varepsilon=(1-\varepsilon)\mu+\varepsilon\tau,
\qquad 0<\varepsilon<1,
\tag{12}
\]
has full support and dominates \((1-\varepsilon)\mu\), but both raw prescriptions are nonclosable. With the convention
\(d_{\rm TV}(\alpha,\beta)=\sup_E|\alpha(E)-\beta(E)|\),
\[
d_{\rm TV}(\nu_\varepsilon,\mu)=\varepsilon.
\tag{13}
\]
Hence there is no total-variation neighborhood of Haar in which the unchanged cylinder action is always closable. Domination of Haar is insufficient; it supplies only one direction of norm comparison.

This covers every purely atomic \(\tau\), without requiring it to have full support: the simultaneous Dirichlet argument in PC-447, §3, uses only its countable support and summable masses. In particular one atom suffices. It also covers the nonatomic singular probability in PC-447, §4: an atomic distribution on one \(p\)-adic coordinate times Haar on the other prime coordinates has \(\chi_{p^{-k}}\to1\). Thus the mixed obstruction is not confined to atomic measures. It does not assert (3) for every singular measure.

## 4. Positive cylinder approximations keep the spectrum but lose uniform bounds

Take the one-point base \(B=P_2^*=\{-1\}\), identify \(X\) with \(\widehat{\mathbb Z}\), and choose \(\tau=\delta_0\). Here \(H=0\), and the unaugmented Haar multiplier is
\[
b(0)=0,\qquad b(q)=1-2q\quad(0<q<1),
\qquad \|B_\mu\|=1,\quad\sigma(B_\mu)=[-1,1].
\tag{14}
\]
For \(m\) in a cofinal divisibility sequence, for example factorials, let
\[
E_m=\{z:z\equiv0\pmod m\},\qquad
w_{\varepsilon,m}=1-\varepsilon+\varepsilon m\mathbf1_{E_m},
\qquad \nu_{\varepsilon,m}=w_{\varepsilon,m}\mu.
\tag{15}
\]
Every density is bounded above and bounded below by \(c=1-\varepsilon>0\). PC-444 therefore gives a bounded raw tower operator \(T_{\varepsilon,m}\), similar to \(B_\mu\), with the exact same spectrum \([-1,1]\). The measures converge weakly to \(\nu_\varepsilon\) in (12), since \(m\mathbf1_{E_m}\mu\) converges to \(\delta_0\). They also satisfy
\(d_{\rm TV}(\nu_{\varepsilon,m},\mu)=\varepsilon(1-1/m)\).
They do **not** converge in total variation to the measure with an atom.

The finite level-\(m\) restriction is \(B_m=C_{2,m}/m\). In ordinary Euclidean coordinates its weighted realization is
\(W_m^{1/2}B_mW_m^{-1/2}\), where
\(W_m=\operatorname{diag}(c+\varepsilon m,c,\ldots,c)\).
Its distinguished row has squared unweighted norm
\[
\sum_{j=1}^{m-1}\frac1{m^2}\cot^2\frac{\pi j}{m}
=\frac{(m-1)(m-2)}{3m^2}.
\tag{16}
\]
One can derive (16) without a trigonometric summation theorem: circulant symmetry makes each diagonal entry of \(B_m^2\) equal to \(m^{-1}\operatorname{Tr}(B_m^2)\); inserting the eigenvalues \(0,1-2j/m\), \(1\le j<m\), and summing squares gives the right side.

The norm of a matrix dominates the Euclidean norm of each row. This restriction is an invariant cylinder subspace, so (16), followed by the full-space bounded-similarity estimate, gives
\[
\boxed{
\sqrt{\frac{c+\varepsilon m}{c}}
\sqrt{\frac{(m-1)(m-2)}{3m^2}}
\ \le\ \|T_{\varepsilon,m}\|
\ \le\ \sqrt{\frac{c+\varepsilon m}{c}}.
}
\tag{17}
\]
For each fixed \(\varepsilon>0\), the norms are therefore \(\Theta_\varepsilon(\sqrt m)\). Equal spectra and valid bounded operators at every regularized stage do not supply a uniformly bounded unchanged-action limit. The endpoint's nonclosability follows from (4), not merely from this norm divergence. No operator-convergence statement between the changing Hilbert spaces is being inferred.

## 5. Prior art, audit and research boundary

The ingredients are classical: Haar character orthogonality, Cesàro averaging, truncation of an integrable density and the graph criterion for closability. The last is Lemma 4.13 in E. Kowalski, *Spectral theory in Hilbert spaces*, ETH Zürich notes (2009), [author's text](https://people.math.ethz.ch/~kowalski/spectral-theory.pdf). The neighboring circle-measure rigidity literature includes C. Badea and S. Grivaux, *Kazhdan constants, continuous probability measures with large Fourier coefficients and rigidity sequences*, Comment. Math. Helv. 95 (2020), 99–127, [DOI 10.4171/CMH/482](https://doi.org/10.4171/CMH/482). It does not provide the profinite cotangent conclusion. The finite identity (16) is explicitly classical, also recorded as equation (3) in J. Franke, *Dirichlet series with trigonometric coefficients*, Integers 21 (2021), A23, [journal text](https://math.colgate.edu/~integers/v23/v23.pdf).

The bounded prior-art check covered Fourier rigidity, closability under singular measure changes, and finite cotangent power sums. No novelty is claimed for these general methods or identities. The line-local increment over PC-447 is the averaged graph witness on a **mixed** measure, where global character rigidity is impossible, together with an explicit positive-density regularization showing why finite boundedness and spectral equality cannot repair it.

**Validation.** The proof is exact. As a separate finite diagnostic, direct level-64 cotangent multiplication of (8) with \(N=8\), \(q_j=j/64\), agreed with (6) to maximum residual \(2.9\times10^{-15}\) in standard double precision. For \(\varepsilon=0.1\), the distinguished-row formula (16) was checked at \(m=3,8,31,128\), with maximum norm residual \(1.0\times10^{-15}\); applying each weighted matrix to its normalized conjugate distinguished row respected both bounds in (17). In the explicit atom witness with \(q_j=j/N^2\), \(1\le j\le N\), \(N\ge3\), the exact input norm is \(\sqrt{2(1-\varepsilon)/N}\), while the squared output error from \(2\mathbf1_{\{0\}}\) is
\[
\frac{2(1-\varepsilon)}{N^2}
\sum_{j=1}^N(1-2j/N^2)^2
+\varepsilon\left(\frac{2(N+1)}{N^2}\right)^2.
\tag{18}
\]
These formulas independently expose the nonzero limiting output; numerical evaluations are diagnostics rather than a replacement for (8)--(11).

The theorem and its proof hold for any finite set of distinct circle points with the same cotangent kernel and complete preimages. In (14)--(18), any singleton base at an irrational angle gives identical matrices. Thus the obstruction is not a prime discriminator. The decisive audit points are the opposite-sector jump, distinctness of the averaged characters, the uniform pointwise bound needed for (11), and the singular support of the output in (4). The boundary includes both raw prescriptions, but the quantitative example (14)--(18) is for the unaugmented one.

PC-446 already excludes compact resolvent whenever an unchanged-action closed realization exists. This result addresses the different issue of whether regularizing the **measure** can restore such an operator: Haar admixture fails on the stated class, and bounded cylinder approximations hide diverging norms. Purely absolutely continuous unbounded weights, singular measures without (3), changed kernels, domains omitting the witnesses, incomplete fibers and growing-base limits remain unclassified here. No new RH implication follows.
