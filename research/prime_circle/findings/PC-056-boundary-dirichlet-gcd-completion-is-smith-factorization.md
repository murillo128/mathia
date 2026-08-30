# PC-056 — boundary Dirichlet GCD completion is exact Smith factorization

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most canonical non-diagonal scale-index Hilbert completion left open by PC-055: the completion obtained from the leading boundary singularity of the genuinely two-dimensional Dirichlet correlations of the full-root fields. That correlation kernel is exactly `gcd(m,n)`. Möbius birth extraction diagonalizes it exactly to `diag(phi(n))`, so the induced infinite birth-to-full coefficient transform is an isometry after completion. The apparent infinite-dimensional anomaly disappears rather than producing a critical-line operator.

This does **not** rule out every non-diagonal completion, the finite renormalized part of the boundary energy, nonlinear/cross-level operators, or the global uniformization branch of PC-017. It rules out attributing an RH mechanism to the leading collision metric canonically forced by the all-mode Dirichlet energy itself.

## 1. The full-root fields have an exact GCD Dirichlet Gram kernel

Retain the normalized full-root fields from PC-027,

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

Put `x=r^2`. Since

\[
V_m(rz)=-\sum_{j\ge1}\frac{x^{mj/2}}{j}z^{mj},
\]

two modes can pair only when their Fourier index is a common multiple of `m` and `n`. Writing

\[
L=\operatorname{lcm}(m,n),
\]

a direct coefficient calculation gives

\[
\begin{aligned}
\langle V_{m,r},V_{n,r}\rangle_{\mathcal D}
&=\sum_{t\ge1}\frac{mn}{Lt}x^{Lt}\\
&=-\frac{mn}{L}\log(1-x^L).
\end{aligned}
\]

Since `mn/L=gcd(m,n)`, the exact finite-radius full-root Gram entry is

\[
\boxed{
G^{\rm full}_{m,n}(x)
=-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right).
}
\]

This is the full-root counterpart of the finite divisor formula for the birth-field Gram matrix in PC-027. It is already genuinely non-diagonal in the polygon-level index and came from the two-dimensional Dirichlet integral, not from an externally chosen sequence norm.

Small controls fix the normalization. For `m=n=1`, the formula is the familiar

\[
\|\Log(1-rz)\|_{\mathcal D}^2=-\log(1-x).
\]

For `(m,n)=(2,4)` it gives

\[
\langle V_{2,r},V_{4,r}\rangle_{\mathcal D}
=-2\log(1-x^4),
\]

matching the direct common-mode sum.

## 2. The leading boundary collision form is exactly the GCD matrix

Let

\[
\Lambda(x):=-\log(1-x).
\]

For every fixed positive integer `L`,

\[
-\log(1-x^L)
=\Lambda(x)-\log L+o(1)
\qquad(x\to1^-).
\]

Therefore

\[
\boxed{
\lim_{x\to1^-}
\frac{G^{\rm full}_{m,n}(x)}{\Lambda(x)}
=\gcd(m,n).
}
\]

So the most direct boundary-renormalized covariance on the scale labels is

\[
\boxed{K(m,n)=\gcd(m,n).}
\]

The geometry of this coefficient is transparent. `V_m` has logarithmic boundary singularities at all `m`-th roots and `V_n` at all `n`-th roots. Their shared collision set is

\[
\mu_m\cap\mu_n=\mu_{\gcd(m,n)},
\]

which has exactly `gcd(m,n)` points. The leading Dirichlet divergence counts those common logarithmic boundary charges one-for-one.

This is precisely the sort of non-diagonal metric PC-055 deliberately left outside its diagonal weighted-`l^2` analysis. Here it is not guessed: it is forced by the leading singular part of the same two-dimensional harmonic fields used throughout PC-027.

## 3. Möbius birth extraction diagonalizes the collision form exactly

For the primitive/birth fields,

\[
F_n=\sum_{d\mid n}\mu(n/d)V_d,
\]

let

\[
M(n,d)=\mu(n/d)\mathbf 1_{d\mid n}
\]

be the Möbius incidence matrix and let

\[
Z(n,d)=\mathbf1_{d\mid n}
\]

be the divisor-zeta incidence matrix. On every finite factor-closed set, `M=Z^{-1}`.

The elementary identity

\[
\boxed{
\gcd(m,n)=\sum_{d\mid m,\,d\mid n}\varphi(d)
}
\]

gives the matrix factorization

\[
\boxed{
K=Z D_\varphi Z^{\mathsf T},
\qquad
D_\varphi=\operatorname{diag}(\varphi(n)).
}
\]

Consequently

\[
\boxed{
MKM^{\mathsf T}=D_\varphi.
}
\]

Equivalently, entrywise,

\[
\boxed{
\sum_{d\mid m}\sum_{e\mid n}
\mu(m/d)\mu(n/e)\gcd(d,e)
=\delta_{m,n}\varphi(n).
}
\]

Thus primitive-shell extraction does not merely make the boundary collision form simpler: it **orthogonalizes it exactly**. Distinct birth shells have zero leading collision covariance, while the self-weight of shell `n` is exactly the number `phi(n)` of primitive boundary singularities.

The same statement follows directly from PC-027's birth Gram formula. For `m != n`, the boundary Dirichlet pairing has a finite resultant limit, so division by `Lambda(x)` sends it to zero. On the diagonal, the divergent coefficient is `phi(n)`. The incidence factorization explains why those local boundary facts and the full-root GCD kernel are the same theorem in two bases.

## 4. The induced infinite non-diagonal completion makes coefficient transport unitary

The finite identity has a clean infinite completion without introducing a Dirichlet weight parameter.

On finitely supported sequences `a=(a_n)`, define the full-root collision norm

\[
\boxed{
\|a\|_{\gcd}^2
:=\sum_{m,n\ge1}a_m\overline{a_n}\gcd(m,n).
}
\]

Using `K=Z D_phi Z^T`, this is

\[
\boxed{
\|a\|_{\gcd}^2
=\sum_{d\ge1}\varphi(d)
\left|
\sum_{n:\,d\mid n}a_n
\right|^2.
}
\]

Define on finite support

\[
(Z^{\mathsf T}a)_d
:=\sum_{n:\,d\mid n}a_n.
\]

Then

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

On finitely supported sequences, `Z^T` is bijective with inverse `M^T`, because

\[
Z^{\mathsf T}M^{\mathsf T}
=(MZ)^{\mathsf T}=I,
\qquad
M^{\mathsf T}Z^{\mathsf T}
=(ZM)^{\mathsf T}=I.
\]

Let `H_gcd` be the Hilbert completion of finite support in the collision norm. The preceding isometry therefore extends uniquely to a unitary equivalence

\[
\boxed{
Z^{\mathsf T}:\mathscr H_{\gcd}
\overset{\sim}{\longrightarrow}
\ell^2(\varphi),
\qquad
(Z^{\mathsf T})^{-1}=M^{\mathsf T}.
}
\]

This transpose is the correct operator for **basis coefficients**. If `b` is a finite coefficient vector in the birth basis, then

\[
\sum_n b_nF_n
=\sum_d (M^{\mathsf T}b)_dV_d.
\]

Hence the actual birth-to-full coefficient transport is exactly

\[
\boxed{
M^{\mathsf T}:\ell^2(\varphi)
\overset{\sim}{\longrightarrow}
\mathscr H_{\gcd}.
}
\]

It is unitary in the Hilbert geometries supplied by the boundary collision form itself.

This distinction prevents a false contradiction with PC-055. PC-055 studied the row convolution operator `T_mu` on a preselected **diagonal** coefficient norm `sum |x_n|^2 n^{-2sigma}` and found its `1/2` membership threshold and `1` multiplier threshold. The present construction instead lets the two-dimensional correlations choose a **non-diagonal** full-root metric. In that metric the coefficient basis-change is the transpose incidence operator, and the classical GCD factorization makes it an exact isometry. There is no boundedness threshold to turn into RH.

## 5. The arithmetic factorization is classical Smith/Le Paige GCD-matrix theory

The factorization

\[
G_N=L_N\Phi_NL_N^{\mathsf T},
\]

where `(G_N)_{ij}=gcd(i,j)`, `L_N(i,j)=1_{j|i}`, and `Phi_N=diag(phi(1),...,phi(N))`, is classical GCD-matrix theory. Henry J. Stephen Smith computed the determinant

\[
\det G_N=\prod_{k=1}^N\varphi(k)
\]

in **On the Value of a Certain Arithmetical Determinant**, *Proceedings of the London Mathematical Society* s1-7 (1875), 208–213, DOI `10.1112/plms/s1-7.1.208`. The explicit incidence/LDU factorization is commonly associated with Le Paige and is given in modern form by Warren P. Johnson, **An LDU Factorization in Elementary Number Theory**, *Mathematics Magazine* 76:5 (2003), 392–394, DOI `10.1080/0025570X.2003.11953215`.

The nearby critical normalized GCD kernels are also already part of the modern GCD-sum literature anchored in `SOURCES.md` through Aistleitner–Berkes–Seip.

No novelty is claimed for the GCD identity, Smith determinant, incidence factorization, or Hilbert completion of an exact finite isometry. The prime-circle-specific research value is the **provenance and closure statement**:

\[
\boxed{
\text{leading 2D Dirichlet boundary correlation}
\longrightarrow
\text{classical GCD kernel}
\longrightarrow
\text{exact Möbius/Smith orthogonalization}.
}
\]

Thus the most canonical non-diagonal completion suggested by the geometry does not repair the diagonal anomaly of PC-055 into a deeper critical-line phenomenon; it removes the anomaly completely.

## 6. Why no zeta-zero or critical-line condition remains

There is no free complex parameter anywhere in the construction. The boundary normalization is fixed by the universal logarithmic collision divergence, and the resulting Hilbert geometry is exactly equivalent to weighted diagonal birth coordinates with weights `phi(n)`.

In particular:

- the number `1/2` from PC-055 does not survive as a threshold;
- no reciprocal zeta multiplier is needed to define the completed coefficient transport;
- no gamma completion or `s <-> 1-s` involution appears;
- no determinant zero appears, because every finite factor-closed GCD matrix is positive definite with determinant `prod phi(n)>0`;
- the infinite completion is obtained by completing an exact isometry, not by analytically continuing a singular multiplier.

One can of course take Dirichlet transforms of `phi(n)` or of the GCD kernel afterward, but that returns the classical zeta ratios already classified elsewhere in the prime-circle corpus. Such a transform would add the spectral parameter externally rather than derive it from this boundary geometry.

Therefore the route

\[
\boxed{
\text{2D harmonic correlations}
\to
\text{non-diagonal scale Hilbert space}
\to
\text{Möbius basis anomaly}
\to
\text{RH}
}
\]

fails for the canonical leading boundary correlation form.

## 7. Boundary of the obstruction

The result is deliberately limited to the **leading logarithmically divergent boundary form** of the Dirichlet Gram matrix. It does not eliminate all information in the next term. Indeed,

\[
-\gcd(m,n)\log(1-x^{\operatorname{lcm}(m,n)})
=
\gcd(m,n)\Lambda(x)
-\gcd(m,n)\log\operatorname{lcm}(m,n)
+o(1),
\]

and after Möbius extraction the corresponding finite parts are the resultant/discriminant energies already classified in PC-006/PC-027. Those are classical arithmetic data, but they are not part of the unitary leading-form theorem.

The finding also does not rule out:

- a different non-diagonal inner product derived from some other intrinsic two-dimensional operator rather than the leading Dirichlet collision form;
- nonlinear functionals that combine the finite and divergent pieces before taking a limit;
- genuinely nonseparable cross-level dynamics;
- an operator whose complex parameter is forced by geometry rather than appended by a Dirichlet/Mellin transform;
- the composite primitive-only Fuchsian uniformization/accessory defect of PC-017.

Any claimed escape through a boundary Hilbert completion should therefore state explicitly what geometric datum it retains beyond the classical collision-count GCD kernel.

## 8. Exact audit and falsification tests

Every main statement is finite and directly falsifiable before completion:

1. expand `V_m(rz)` and `V_n(rz)` in Fourier modes and verify
   \[
   \langle V_{m,r},V_{n,r}\rangle
   =-\gcd(m,n)\log(1-x^{\operatorname{lcm}(m,n)});
   \]
2. divide by `-log(1-x)` and take `x->1-` to recover `gcd(m,n)`;
3. on any finite factor-closed set, form `Z`, `M`, and `D_phi` and check
   \[
   K=ZD_\varphi Z^T,
   \qquad MZ=ZM=I,
   \qquad MKM^T=D_\varphi;
   \]
4. compare the diagonal birth weights with the `phi(n)` boundary divergence already derived in PC-027;
5. for finite coefficient support, verify
   \[
   \|a\|_{\gcd}^2
   =\sum_d\varphi(d)|(Z^Ta)_d|^2
   \]
   and the inverse relation with `M^T`;
6. verify that none of these steps invokes a zeta zero, analytic continuation, or an assumed zero-free half-plane.

A failure of the exact full-root Gram formula, the boundary GCD limit, or the incidence factorization would invalidate the finding. A different completion evades it only by proving that its non-diagonal metric is forced by additional prime-circle geometry not present in this leading collision form.