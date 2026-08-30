# PC-056 — boundary Dirichlet GCD completion is exact Smith factorization

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most canonical non-diagonal scale-index Hilbert completion left open by PC-055: the completion obtained from the leading boundary singularity of the genuinely two-dimensional Dirichlet correlations of the full-root fields. PC-006 already derived the underlying finite-radius GCD Gram kernel and identified its normalized critical GCD form. The new point here is the infinite **basis-completion** question reopened by PC-055: in the correlation-induced metric, Möbius birth extraction is exactly the classical Smith/Le Paige orthogonalization, and the physical birth-to-full coefficient transform extends to a unitary map. The diagonal-completion anomaly of PC-055 therefore disappears rather than becoming a critical-line operator.

This does **not** rule out every non-diagonal completion, the finite renormalized part of the boundary energy, nonlinear/cross-level operators, or the global uniformization branch of PC-017. It rules out attributing an RH mechanism to the leading collision metric canonically forced by the all-mode Dirichlet energy itself.

## 1. Starting point already established in PC-006: exact full-root GCD Gram data

Retain the normalized full-root fields used in PC-006/PC-027,

\[
V_n(z)=\Log(1-z^n),
\qquad
V_{n,r}(z)=V_n(rz),
\qquad 0<r<1,
\]

with the analytic Dirichlet inner product

\[
\langle f,g\rangle_{\mathcal D}
=\frac1\pi\int_{\mathbb D}f'(z)\overline{g'(z)}\,dA(z).
\]

Put `x=r^2`. PC-006 already derives, by matching common Fourier modes,

\[
\boxed{
G^{\rm full}_{m,n}(x)
:=\langle V_{m,r},V_{n,r}\rangle_{\mathcal D}
=-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right).
}
\]

For completeness, if `L=lcm(m,n)`, the common indices are `Lt` and the Dirichlet coefficient sum is

\[
\sum_{t\ge1}\frac{mn}{Lt}x^{Lt}
=-\frac{mn}{L}\log(1-x^L),
\]

with `mn/L=gcd(m,n)`.

Let

\[
\Lambda(x):=-\log(1-x).
\]

Since for every fixed positive integer `L`,

\[
-\log(1-x^L)=\Lambda(x)-\log L+o(1),
\qquad x\to1^-,
\]

PC-006's full-root Gram family has the exact leading boundary form

\[
\boxed{
\lim_{x\to1^-}
\frac{G^{\rm full}_{m,n}(x)}{\Lambda(x)}
=K(m,n):=\gcd(m,n).
}
\]

Geometrically this coefficient counts shared logarithmic boundary charges, because

\[
\mu_m\cap\mu_n=\mu_{\gcd(m,n)}.
\]

PC-006 used the normalized kernel `gcd(m,n)/sqrt(mn)` to identify the classical critical GCD/Poisson structure. PC-055 later left open a different question: whether a **non-diagonal Hilbert completion forced by the two-dimensional correlations themselves** could make the infinite Möbius birth/full-root change of basis anomalous. The remaining sections answer that question for this canonical leading boundary form.

## 2. Möbius birth extraction is exactly Smith/Le Paige orthogonalization

For the primitive/birth fields,

\[
F_n=\sum_{d\mid n}\mu(n/d)V_d,
\]

let

\[
M(n,d)=\mu(n/d)\mathbf 1_{d\mid n}
\]

be the Möbius incidence matrix and

\[
Z(n,d)=\mathbf1_{d\mid n}
\]

the divisor-zeta incidence matrix. On every finite factor-closed set,

\[
M=Z^{-1}.
\]

The elementary identity

\[
\boxed{
\gcd(m,n)=\sum_{d\mid m,\,d\mid n}\varphi(d)
}
\]

gives

\[
\boxed{
K=ZD_\varphi Z^{\mathsf T},
\qquad
D_\varphi=\operatorname{diag}(\varphi(n)).
}
\]

and therefore

\[
\boxed{
MKM^{\mathsf T}=D_\varphi.
}
\]

Equivalently,

\[
\boxed{
\sum_{d\mid m}\sum_{e\mid n}
\mu(m/d)\mu(n/e)\gcd(d,e)
=\delta_{m,n}\varphi(n).
}
\]

Thus primitive-shell extraction **orthogonalizes the leading boundary collision form exactly**. Distinct birth shells have zero leading collision covariance, and shell `n` has self-weight `phi(n)`, exactly the number of primitive logarithmic singularities.

This is also the leading-order form of PC-027's birth Gram asymptotics: for `m != n` the pairing has a finite resultant limit and hence vanishes after division by `Lambda(x)`, while the diagonal divergence coefficient is `phi(n)`. The matrix factorization identifies those geometric facts with a classical incidence algebra identity.

## 3. The induced non-diagonal infinite completion makes coefficient transport unitary

On finitely supported full-root coefficient sequences `a=(a_n)`, define the collision norm

\[
\boxed{
\|a\|_{\gcd}^2
:=\sum_{m,n\ge1}a_m\overline{a_n}\gcd(m,n).
}
\]

The Smith factorization gives

\[
\boxed{
\|a\|_{\gcd}^2
=\sum_{d\ge1}\varphi(d)
\left|
\sum_{n:\,d\mid n}a_n
\right|^2.
}
\]

Define

\[
(Z^{\mathsf T}a)_d
:=\sum_{n:\,d\mid n}a_n.
\]

Then on finite support

\[
\boxed{
\|a\|_{\gcd}
=\|Z^{\mathsf T}a\|_{\ell^2(\varphi)},
}
\]

where

\[
\|b\|_{\ell^2(\varphi)}^2
=\sum_{n\ge1}\varphi(n)|b_n|^2.
\]

Both `Z^T` and `M^T` preserve finite support, and

\[
Z^{\mathsf T}M^{\mathsf T}
=(MZ)^{\mathsf T}=I,
\qquad
M^{\mathsf T}Z^{\mathsf T}
=(ZM)^{\mathsf T}=I.
\]

Let `H_gcd` be the Hilbert completion of finite support in the collision norm. The exact finite-support isometry extends uniquely to

\[
\boxed{
Z^{\mathsf T}:\mathscr H_{\gcd}
\overset{\sim}{\longrightarrow}
\ell^2(\varphi),
\qquad
(Z^{\mathsf T})^{-1}=M^{\mathsf T}.
}
\]

The transpose is essential because the research question is about **basis coefficients**. If `b` is a finite coefficient vector in the birth basis, then

\[
\sum_n b_nF_n
=\sum_d(M^{\mathsf T}b)_dV_d.
\]

Hence the physical birth-to-full coefficient transport is exactly

\[
\boxed{
M^{\mathsf T}:\ell^2(\varphi)
\overset{\sim}{\longrightarrow}
\mathscr H_{\gcd}.
}
\]

So the correlation-induced completion does not make the infinite change of basis singular: it makes it **unitary by construction from the exact geometric Gram form**.

## 4. Why this does not contradict PC-055

PC-055 studies the row Möbius convolution operator

\[
(T_\mu x)(n)=\sum_{d\mid n}\mu(n/d)x(d)
\]

on the preselected diagonal family

\[
\|x\|_\sigma^2
=\sum_n|x_n|^2n^{-2\sigma}.
\]

There, `T_mu e_1` first belongs to the space only for `sigma>1/2`, and bounded invertibility occurs only for `sigma>1`, because under the Hardy-Dirichlet model the operator is multiplication by shifted reciprocal zeta.

The present metric is a different object for a precise reason: it is not chosen diagonally in the full-root basis. It is the leading boundary covariance of the two-dimensional Dirichlet fields themselves. Once that covariance is used, the full-root coefficient space is `H_gcd`, the birth coefficient space is `l^2(phi)`, and the **coefficient** transport is `M^T`, not the same-space row multiplier studied in PC-055.

Thus the two results fit together:

\[
\boxed{
\begin{array}{c}
\text{external diagonal scale metric}\\
\downarrow\\
\text{Möbius multiplier thresholds at }1/2\text{ and }1
\end{array}
\qquad
\begin{array}{c}
\text{intrinsic leading Dirichlet collision metric}\\
\downarrow\\
\text{exact Smith isometry, no threshold}
\end{array}}
\]

The natural non-diagonal repair therefore does not upgrade the `1/2` anomaly into RH evidence; it removes that anomaly completely.

## 5. Prior-art and novelty audit

The arithmetic factorization is classical GCD-matrix theory. For

\[
(G_N)_{ij}=\gcd(i,j),
\]

Henry J. Stephen Smith computed

\[
\det G_N=\prod_{k=1}^N\varphi(k)
\]

in **On the Value of a Certain Arithmetical Determinant**, *Proceedings of the London Mathematical Society* s1-7 (1875), 208–213, DOI `10.1112/plms/s1-7.1.208`. The incidence factorization

\[
G_N=L_N\Phi_NL_N^{\mathsf T}
\]

is commonly associated with Le Paige and is given in modern form by Warren P. Johnson, **An LDU Factorization in Elementary Number Theory**, *Mathematics Magazine* 76:5 (2003), 392–394, DOI `10.1080/0025570X.2003.11953215`.

PC-006 already supplies the direct internal prior-art boundary: it derived the same full-root finite-radius Dirichlet Gram formula and redirected its normalized leading kernel to the Aistleitner-Berkes-Seip theory of critical GCD sums and Poisson integrals. Therefore **neither the GCD kernel nor its prime-circle derivation is new in PC-056**.

No historical novelty is claimed for the Smith determinant, Le Paige/Johnson factorization, Möbius inversion, or completion of an exact finite-support isometry. The durable research contribution is narrower: PC-055 left a concrete non-diagonal-completion escape route open, and the most canonical version of that route is now classified exactly. Its geometry-induced Gram form is the classical GCD matrix, and the birth/full-root coefficient transform is its classical incidence orthogonalization.

## 6. Why no zeta-zero or critical-line condition remains

There is no free complex parameter in this completion. The boundary normalization is fixed by the universal logarithmic collision divergence, and the resulting Hilbert geometry is exactly equivalent to weighted diagonal birth coordinates with weights `phi(n)`.

In particular:

- the number `1/2` from PC-055 does not survive as a threshold;
- no reciprocal-zeta multiplier is needed to define the completed coefficient transport;
- no gamma completion or `s <-> 1-s` involution appears;
- every finite factor-closed GCD matrix is positive definite, with determinant `prod phi(n)>0`;
- the infinite map is obtained by completing an exact isometry, not by analytically continuing a singular multiplier.

Taking a Dirichlet transform of `phi(n)` or of the GCD kernel afterward only re-enters the classical zeta-ratio identities already classified elsewhere in the corpus. Such a transform introduces the spectral parameter externally.

Therefore the route

\[
\boxed{
\text{2D harmonic correlations}
\to
\text{canonical non-diagonal scale Hilbert space}
\to
\text{Möbius basis anomaly}
\to
\text{RH}
}
\]

fails for the leading boundary collision form.

## 7. Boundary of the obstruction

The result is limited to the **leading logarithmically divergent boundary form**. The next term is not zero:

\[
-\gcd(m,n)\log(1-x^{\operatorname{lcm}(m,n)})
=
\gcd(m,n)\Lambda(x)
-\gcd(m,n)\log\operatorname{lcm}(m,n)
+o(1).
\]

After Möbius extraction, the finite parts are the resultant/discriminant energies already classified in PC-006/PC-027. They are classical arithmetic data, but they are not part of the unitary leading-form theorem.

The finding also does not rule out:

- another non-diagonal inner product derived from a different intrinsic two-dimensional operator rather than the leading Dirichlet collision form;
- nonlinear functionals combining finite and divergent pieces before the limit;
- genuinely nonseparable cross-level dynamics;
- an operator whose complex parameter is forced by geometry rather than appended by a Dirichlet/Mellin transform;
- the composite primitive-only Fuchsian uniformization/accessory defect of PC-017.

Any claimed boundary-Hilbert escape must therefore identify what geometric datum it retains beyond the classical collision-count GCD kernel and the Smith incidence factorization.

## 8. Exact audit and falsification tests

The new completion claim can be checked entirely on finite support:

1. reuse PC-006's exact full-root Gram identity and divide by `-log(1-x)` to recover `K(m,n)=gcd(m,n)`;
2. on any finite factor-closed set, form `Z`, `M`, and `D_phi` and verify
   \[
   K=ZD_\varphi Z^T,
   \qquad MZ=ZM=I,
   \qquad MKM^T=D_\varphi;
   \]
3. compare the diagonal birth weights with the `phi(n)` boundary divergence of PC-027;
4. for arbitrary finite coefficient support, verify
   \[
   \|a\|_{\gcd}^2
   =\sum_d\varphi(d)|(Z^Ta)_d|^2;
   \]
5. verify directly that `M^T` and `Z^T` are inverse on finite support, then complete the isometry;
6. check that no step invokes a zeta zero, analytic continuation, or a zero-free half-plane.

A failure of the incidence factorization or finite-support inverse/isometry would invalidate the new claim. A different completion evades it only by proving that its non-diagonal metric is forced by additional prime-circle geometry not present in this leading collision form.