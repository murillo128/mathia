# PC-446 — Raw cotangent tower measures cannot remove the inherited spectral bands

**Status:** EXACT-DERIVED + CLASSICAL-STRUCTURE + NEGATIVE/OBSTRUCTION + CONTROL-BLIND. For the fixed-base complete cotangent tower of PC-443, changing the Hilbert-space probability cannot produce a compact-resolvent realization while retaining the exact action on every cylinder function. This holds for arbitrary Borel probabilities, including singular measures and equivalent measures with unbounded or vanishing densities. The precise conclusions are a full-support criterion for the cylinder prescription and spectral **inclusion** for every closed extension; no boundedness, closability, spectral equality, or spectral-type assertion is made for arbitrary measures.

## 1. The measure-only question and exact statement

Fix \(d>1\), \(r=\varphi(d)\), and
\[
Y_m=\{y\in S^1:y^m\in P_d^*\},\qquad
X=\varprojlim_mY_m,\qquad
\mathcal A_{\rm cyl}=\bigcup_m\mathbb C^{Y_m}.
\tag{1}
\]
The maps in the inverse system are the power maps of PC-443. Its exact refinement identity gives two pointwise cylinder prescriptions
\[
\mathcal B|_{\mathbb C^{Y_m}}=B_m=C_{d,m}/m,\qquad
\mathcal B^+|_{\mathbb C^{Y_m}}=B_m^+=(C_{d,m}+J_m)/m.
\tag{2}
\]
Let \(H_d=C_{d,1}\), \(A_d=H_d+J_1\), and let \(\lambda_1,\ldots,\lambda_r\) be the eigenvalues of \(A_d\). Put
\[
\mathscr B_d=\bigcup_{\alpha=1}^r[\lambda_\alpha-2,\lambda_\alpha].
\tag{3}
\]
Here \(J_m\) is the all-ones matrix on \(Y_m\); in particular \(J_1\) has size \(r\).

**Theorem.** For any Borel probability \(\nu\) on \(X\):

1. Either prescription in (2) defines a well-defined linear operator on all cylinder-function classes in \(L^2(X,\nu)\) **if and only if** \(\nu\) has full topological support, equivalently every nonempty cylinder has positive mass.
2. If a closed operator \(T\) on \(L^2(X,\nu)\) extends that prescription, then
\[
\lambda_\alpha-2q\in\sigma_p(T)
\quad(1\le\alpha\le r,\ q\in\mathbb Q\cap(0,1)),\qquad
\mathscr B_d\subseteq\sigma(T).
\tag{4}
\]
For the unaugmented prescription, also \(\sigma(H_d)\subseteq\sigma_p(T)\); for the augmented one, \(\sigma(A_d)\subseteq\sigma_p(T)\).
3. No such closed extension has compact resolvent. This conclusion does not assume symmetry or boundedness.

PC-444 gives exact spectral equality by bounded similarity when the density and its inverse are bounded, and Haar uniqueness when the unchanged action must be symmetric. The new boundary is that dropping **both** requirements cannot delete the inherited bands or give compact resolvent. The general closed realization might fail to exist or have additional spectrum.

## 2. Null classes force full support before symmetry enters

Write \(p_m(x)=\nu(\pi_m^{-1}\{x\})\) and let \(e_x\) be the indicator of this cylinder. If \(p_m(x)=0\), then \([e_x]=0\). Well-definedness alone requires
\[
[\mathcal B e_x]=0,\qquad
(B_m)_{yx}=0\quad\text{whenever }p_m(y)>0.
\tag{5}
\]
There is no cancellation here: \(\mathcal B e_x\) has the constant value \((B_m)_{yx}\) on the \(y\)-cylinder.

For \(x=e^{2\pi i\theta_x}\ne y=e^{2\pi i\theta_y}\),
\[
(B_m)_{yx}=\frac{i}{m}\cot\!\bigl(\pi(\theta_y-\theta_x)\bigr).
\tag{6}
\]
This is zero exactly for antipodal pairs. On a finite set of at least three circle points, the undirected nonzero-entry graph is connected: two non-antipodal points have an edge, and an antipodal pair has a common neighbor at every third point. Since the support set \(S_m=\{y:p_m(y)>0\}\) is nonempty, (5) forbids an edge from \(S_m\) to its complement. Connectivity forces \(S_m=Y_m\) whenever \(|Y_m|\ge3\).

For any exceptional smaller level, pass to level \(3m\). It has at least three points, all its cylinder masses are positive, and the mass of each level-\(m\) cylinder is the sum of the masses of its three preimages. Thus every level has strictly positive masses. For \(B_m^+\), the off-diagonal entry is
\[
\frac{1+i\cot(\pi(\theta_y-\theta_x))}{m},
\tag{7}
\]
which is never zero, so the same argument applies directly to every nontrivial level.

The single-coordinate cylinders form a clopen basis for \(X\): any finite collection of levels is dominated by their least common multiple. Hence positivity of every cylinder mass is equivalent to full support. Conversely, under full support a cylinder function that vanishes \(\nu\)-almost everywhere is identically zero. Thus (2) respects equivalence classes and has bounded cylinder outputs in \(L^2(\nu)\). Cylinder functions are dense in \(C(X)\) and then in \(L^2(\nu)\), so this is a densely defined operator. This proves **well-definedness**, not closability.

Full support is weaker than equivalence to Haar. The inverse system is countable, so \(X\) is compact metrizable. Take a countable dense set \(\{x_j\}_{j\ge1}\subset X\) and \(\nu=\sum_{j\ge1}2^{-j}\delta_{x_j}\). This probability has full support and is singular to the nonatomic Haar probability. The cylinder prescription is well-defined for it; the theorem does not assert that this example admits a closed extension.

## 3. Cylinder eigenvectors survive every admissible measure

PC-053 and PC-443 give the exact finite fiber-Fourier blocks. At \(q=j/m\in(0,1)\), the normalized block is
\[
\mathcal K_q=D_qA_dD_q^{-1}-2qI,\qquad
D_q(a,a)=e^{2\pi iqa/d}.
\tag{8}
\]
The zero-character block is \(H_d\), or \(A_d\) for the augmented prescription. Every eigenvector of (8) gives a nonzero cylinder function \(f_{\alpha,q}\) satisfying the **pointwise** identity
\[
\mathcal B^{(+)}f_{\alpha,q}
=(\lambda_\alpha-2q)f_{\alpha,q}.
\tag{9}
\]
Refinement compatibility makes this identity independent of the finite level representing \(q\).

By full support, \(0<\|f_{\alpha,q}\|_{L^2(\nu)}<\infty\). Every extension whose domain contains all cylinder classes must therefore retain (9) as an actual eigenvector equation. This proves the point-spectrum statements, without transporting a Haar basis or comparing Hilbert norms. Rational \(q\) are dense in \((0,1)\), and the spectrum of a closed operator is closed, giving (4). Equivalently, normalizing these eigenvectors and letting \(q\to q_0\in[0,1]\) gives approximate eigenvectors at every band point.

If \(z\in\rho(T)\) and \((T-z)^{-1}\) were compact, fix \(\alpha\) and choose distinct rational \(q_j\to q_0\in(0,1)\). Equation (9) supplies the distinct eigenvalues
\[
\frac{1}{\lambda_\alpha-2q_j-z}
\longrightarrow
\frac{1}{\lambda_\alpha-2q_0-z}\ne0
\tag{10}
\]
of that compact operator. This contradicts the classical compact-operator spectral theorem. If \(\rho(T)=\varnothing\), \(T\) already fails the definition of compact resolvent. No orthogonality assumption on the surviving eigenvectors is used.

## 4. Controls, prior art, and exact limits of the conclusion

Replace \(P_d^*\) by any nonempty finite set of distinct circle points, including irrational angles, and retain complete power preimages, the oriented cotangent rule, and the \(1/m\) normalization. PC-443 gives (8) with that base's \(H_B+J\). The same antipodal zero graph and finite cylinder eigenvectors prove the entire theorem. Numerical band endpoints may change; the support criterion and inability to remove the bands are source-blind. No prime-specific mechanism is established.

The abstract ingredients are classical: invariance of the null-function subspace under a finite matrix, connectivity of its nonzero-entry graph, persistence of eigenvectors under an extension, and the Riesz–Schauder theorem. For the last step see Wolfgang Arendt, *Heat Kernels*, ISEM 2005/06, §1.3, Proposition 1.3.2, [author's lecture notes](https://www.math.tecnico.ulisboa.pt/~czaja/ISEM/09internetseminar200506.pdf). The exact tube blocks and inverse-limit realization are established in PC-053 and PC-443; PC-444 covers symmetry and equivalent bounded norms. No novelty is claimed for the general operator theory. The line-local increment is the **arbitrary-measure null-class gate and the resulting no-compact-resolvent boundary even outside bounded similarity**.

The conclusions require the unchanged pointwise action on **all** cylinder functions and fixed finite base. They do not cover a changed kernel, half-density-compensated action, a restriction that discards cylinder eigenvectors, incomplete fibers, or a growing-base limit. The compensated construction is separately classified in PC-444. Full support is not a boundedness or closability criterion. Beyond bounded similarity, neither equality of spectra nor preservation of spectral type, basis bounds, or Fredholm essential spectra is inferred. Dense eigenvalues alone do not justify those stronger claims for a nonnormal operator.

**Validation.** The proof is exact. As separate finite diagnostics, the nonzero-edge rule (6) was checked by integer antipode tests on \((d,m)=(2,2),(2,3),(3,2),(3,3),(4,1),(4,3),(5,2),(5,3)\). All 4,492 nonempty proper support subsets at levels with at least three vertices had a crossing edge; the two-point cases were retained as genuine finite-level exceptions. Direct complex Fourier block sums agreed with (8) on all eight levels to maximum absolute error \(4.6\times10^{-16}\) in ordinary floating-point arithmetic. These finite checks do not establish the infinite theorem. Its decisive audit points are the null-class implication (5), refinement of exceptional levels, nonvanishing eigenvector classes under full support, and the nonzero accumulation in (10).

**Consequence.** A measure-only proposal for a discrete spectral model must change the cylinder action or domain, rather than merely use an unbounded or singular weight. This is a bounded obstruction for the complete cotangent tower, not an RH result and not a classification of arbitrary weighted closed realizations.
