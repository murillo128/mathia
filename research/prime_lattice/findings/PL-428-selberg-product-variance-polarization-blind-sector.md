# PL-428 — Ordinary L-product variance polarization misses three mod-5 coherence directions

**Evidence/status:** EXACT-DERIVED + LITERATURE-CALIBRATED + DECISIVE-REPRESENTATION-OBSTRUCTION  
**Parents:** PL-415, PL-421, PL-424, PL-425, PL-427

## Claim

A natural continuation of the mod-5 matrix route is to apply a scalar short-interval variance theorem to many ordinary finite products of the four Dirichlet-
L channels and then polarize those scalar variances. This cannot recover the full unsymmetrized character covariance needed by the local image-cone criterion of PL-421.

For a real residue signal on \((\mathbb Z/5\mathbb Z)^\times\), its Hermitian covariance in the character/Fourier basis has ten real degrees of freedom. Scalar variances of **every real linear combination** of the four character channels determine only its real part, which has seven real degrees of freedom. The three missing directions are the imaginary coherences

\[
\Im K_{01},\qquad \Im K_{21},\qquad \Im K_{13}.
\]

Ordinary products \(\prod_j L(s,\chi_j)^{m_j}\) have integer multiplicities \(m_j\), so their logarithmic derivatives probe only this real-coefficient quadratic form. There are exact positive-semidefinite residue covariances with identical scalar variance for **every** such product but opposite PL-421 image-cone verdicts. Thus no family of scalar variance theorems indexed only by ordinary L-products can by itself prove the required matrix admission condition.

This is an information/representation obstruction, not an RH consequence and not a claim about the size of the three blind coherences for the actual prime source.

## 1. Ordinary products probe only real coefficient vectors

Order the nonzero residue classes by powers of the generator \(2\) modulo \(5\),

\[
(1,2,4,3),
\]

and use the normalized \(C_4\) Fourier matrix

\[
F_{rj}=\frac12 e^{-2\pi i rj/4}=\frac12(-i)^{rj}.
\]

Let \(R(y)\in\mathbb R^4\) be a centered residue-channel signal and put

\[
A(y)=F^*R(y),\qquad
S=\int R(y)R(y)^T\,dy,\qquad
K=\int A(y)A(y)^*\,dy=F^*SF.
\]

Here \(S\) is real symmetric positive semidefinite and \(K\) is Hermitian positive semidefinite.

For an ordinary product with multiplicity vector \(m=(m_0,m_1,m_2,m_3)\in\mathbb N_0^4\),

\[
H_m(s)=\prod_{j=0}^3 L(s,\chi_j)^{m_j},
\]

logarithmic differentiation gives

\[
-\frac{H_m'}{H_m}(s)
 =\sum_{j=0}^3 m_j\left(-\frac{L'}{L}(s,\chi_j)\right).
\]

Thus the associated centered scalar statistic is a real-coefficient combination of the four character channels. Its quadratic variance is

\[
Q_K(m)=m^*Km=m^TKm=m^T\Re(K)m,
\]

because for Hermitian \(K\), \(\Im K\) is a real skew-symmetric matrix and hence \(m^T\Im(K)m=0\) for every real \(m\).

Knowing \(Q_K(m)\) for every integer \(m\) therefore determines exactly \(\Re K\): for example,

\[
2\Re K_{jk}=Q_K(e_j+e_k)-Q_K(e_j)-Q_K(e_k).
\]

Allowing all real coefficient vectors would not add information. Hermitian polarization needs genuinely complex coefficients in order to recover the imaginary cross terms.

## 2. Mod-5 Fourier reality leaves exactly three invisible coherences

Because \(R(y)\) is real, its Fourier coordinates obey

\[
A_0,A_2\in\mathbb R,\qquad A_3=\overline{A_1}.
\]

The corresponding admissible Hermitian covariance \(K\) has ten real degrees of freedom: three diagonal parameters \(K_{00},K_{22},K_{11}=K_{33}\); the real parameter \(K_{02}\); and the three complex parameters \(K_{01},K_{21},K_{13}\). Its real part carries only seven of them. The invisible sector is therefore exactly three-dimensional, represented by

\[
\Im K_{01},\qquad \Im K_{21},\qquad \Im K_{13}.
\]

Equivalently, consider

\[
\mathcal P:\operatorname{Sym}_4(\mathbb R)\longrightarrow
\operatorname{Sym}_4(\mathbb R),\qquad
\mathcal P(S)=\Re(F^*SF).
\]

A direct calculation gives \(\operatorname{rank}\mathcal P=7\), hence \(\dim\ker\mathcal P=3\). One exact real-symmetric kernel basis is

\[
A_1=\begin{pmatrix}
0&-1&0&1\\
-1&0&0&0\\
0&0&0&0\\
1&0&0&0
\end{pmatrix},\quad
A_2=\begin{pmatrix}
0&0&0&0\\
0&0&-1&0\\
0&-1&0&1\\
0&0&1&0
\end{pmatrix},\quad
A_3=\operatorname{diag}(0,-1,0,1).
\]

For the first direction,

\[
F^*A_1F=
\begin{pmatrix}
0&i/2&0&-i/2\\
-i/2&0&-i/2&-i\\
0&i/2&0&-i/2\\
i/2&i&i/2&0
\end{pmatrix},
\]

which is purely imaginary Hermitian. Hence it is invisible to every real quadratic probe \(m^TKm\).

## 3. Exact matched controls flip the local cone verdict

Take the one-parameter covariance family

\[
S_t=I_4+tA_1.
\]

The eigenvalues of \(A_1\) are \(\sqrt2,-\sqrt2,0,0\), so

\[
\operatorname{spec}(S_t)=
\{1+\sqrt2t,\,1-\sqrt2t,\,1,\,1\}.
\]

Therefore \(S_t\succeq0\) for \(0\le t\le1/\sqrt2\). Its diagonal is identically \((1,1,1,1)\), so at \(p=5\) the normalized correlation matrix appearing in PL-421 is simply \(S_t\). The PL-421 image-cone condition becomes

\[
\lambda_{\min}(S_t)=1-\sqrt2t\ge\frac14,
\]

or equivalently

\[
t\le\frac{3}{4\sqrt2}.
\]

Thus \(S_0=I_4\) passes the cone test, while

\[
S_{3/5}=I_4+\frac35A_1
\]

is still positive semidefinite because \(3/5<1/\sqrt2\), but

\[
\lambda_{\min}(S_{3/5})=1-\frac{3\sqrt2}{5}<\frac14,
\]

so it fails the cone test.

Nevertheless, since \(\Re(F^*A_1F)=0\), for every real \(m\in\mathbb R^4\),

\[
m^T(F^*S_tF)m=\|m\|_2^2,
\]

independently of \(t\). In particular \(S_0\) and \(S_{3/5}\) give exactly the same scalar variance for every ordinary L-product multiplicity vector \(m\in\mathbb N_0^4\), while they have opposite PL-421 image-cone verdicts.

This strengthens the matched-control obstruction of PL-424: the controls now agree not merely on the four marginals and the \(C_4\) twirl, but on the scalar variance of **every real linear combination** of character channels.

## 4. Relation to the current line

PL-424 showed that character marginals plus cyclic twirling do not determine local image-cone admission. The present result identifies the exact residual blind sector that survives even if one enriches the scalar data to all ordinary product channels.

PL-427 is not contradicted. Its key proof-level extension allows an arbitrary complex coefficient vector \(c\), and complex Hermitian polarization does recover the full mixed matrix. That is exactly the extra information missing here. PL-427 remains unusable as an RH input because its GRH hypothesis already contains the principal-channel RH statement; the distinction is between **representation completeness** and **hypothesis strength**.

PL-425 likewise remains relevant as a possible arithmetic suppression mechanism: its model suggests substantial character diagonalization. But model diagonalization is not a theorem that the actual source has zero or sufficiently small components in the three blind directions.

## 5. Prior-art and novelty audit

Bui, Keating and Smith study scalar short-interval variances and pair-correlation quantities for an individual primitive Selberg-class function, using the coefficients of its logarithmic derivative. This is the appropriate literature calibration for the proposed scalar-variance route:

- J. Bui, J. P. Keating, D. J. Smith, *On the variance of sums of arithmetic functions over primes in short intervals and pair correlation for L-functions in the Selberg class*, J. London Math. Soc. 94 (2016), 161–185, DOI: 10.1112/jlms/jdw030, arXiv:1506.03741.

The algebra used here is classical: logarithmic derivatives of products add, real quadratic forms recover only the real symmetric part of a Hermitian form, and complex polarization is needed for the full form. Targeted searches did not locate a source stating the line-specific mod-5 conclusion above—namely the exact three-dimensional blind sector together with positive-semidefinite matched controls that preserve every real/product-channel scalar variance while flipping the PL-421 cone verdict. No claim of novelty is made for the generic polarization facts themselves.

There is also a prior-art limitation on the proposed strategy before the present obstruction is even reached: the Bui–Keating–Smith theorem is stated for a primitive Selberg-class function, whereas an arbitrary product of Dirichlet L-functions is generally nonprimitive and changes degree. The finding therefore does **not** assert that their theorem can simply be applied to every \(H_m\); it says that even an ideal scalar variance theorem for all such products would still leave this three-dimensional information deficit.

## 6. Adversarial audit and failure modes

1. The matrices \(S_t\) above are abstract admissible covariance matrices. They are not claimed to be realized by the actual prime-residue source. Their purpose is to prove non-identifiability from the proposed scalar observables.
2. The principal character modulo \(5\) is imprimitive: \(L(s,\chi_0)=\zeta(s)(1-5^{-s})\). The finite \(p=5\) correction is already isolated in PL-415 and does not alter the real-versus-complex coefficient-space obstruction.
3. Ordinary product multiplicities are real integers. Multiplying an L-function by a constant phase does not help because logarithmic differentiation removes it. Formal complex powers such as \(L(s,\chi)^i\) are not ordinary global L-functions and introduce branch issues at zeros, so they are not a legitimate way to smuggle complex coefficients into a scalar product theorem.
4. Genuine complex mixed observables such as \(A_j+iA_k\), direct cross-covariances \(\int A_j\overline{A_k}\), or an equivalent oriented/non-self-conjugate statistic can see the blind sector. The result rules out only the ordinary real-product scalarization route.
5. Arithmetic structure could in principle force the three imaginary coherences to vanish or be small enough that \(\Re K\) suffices. That would require an independent theorem for the actual source; the matrix counterexample does not decide it.
6. No implication for RH follows from this finite-dimensional obstruction by itself.

## Consequence

The matrix route should not spend further effort trying to reconstruct the PL-421 source-covariance admission test by applying scalar short-interval variance theorems to a larger collection of ordinary products and then using real polarization. Even complete knowledge of those scalar variances leaves a three-real-dimensional coherence sector unresolved, and that sector can already change local admission at \(p=5\).

A viable continuation needs either genuinely complex/oriented mixed statistics that recover those coherences, or a weaker-than-RH arithmetic theorem showing that the actual source suppresses the blind sector with enough quantitative margin to make the PL-421 cone test follow.