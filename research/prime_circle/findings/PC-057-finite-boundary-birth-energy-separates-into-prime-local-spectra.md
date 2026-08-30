# PC-057 — finite boundary birth energy separates into explicit prime-local spectra

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the finite renormalized boundary term left open by PC-056. After subtracting the universal logarithmic collision divergence from the full-root Dirichlet Gram family and applying Möbius birth extraction, the resulting non-diagonal cross-level operator is exactly the tangent at exponent one of the classical power-GCD/Smith factorization. On every finite divisor box its shell-normalized matrix is a Kronecker sum of independent prime-power chains, and every prime-local chain has an elementary closed-form spectrum. Thus the most canonical finite correction to the intrinsic two-dimensional boundary metric contains no hidden zeta-zero spectrum: its finite-level spectral data are completely prime-separable and explicit.

This does **not** rule out nonlinear functionals of the finite and divergent terms taken jointly, non-divisor-closed truncations with a separately justified limit, genuinely nonseparable dynamics across refinement levels, or the global Fuchsian uniformization/accessory branch of PC-017. It rules out treating the finite renormalized Dirichlet birth Gram operator itself, or its ordinary finite divisor-box spectral determinants, as an unexplained Hilbert–Pólya mechanism.

## 1. The finite term left open by PC-056

For the full-root fields

\[
V_n(z)=\Log(1-z^n),
\]

PC-006 and PC-056 give the exact radial Dirichlet Gram matrix, with \(x=r^2\),

\[
G^{\rm full}_{m,n}(x)
=
-\gcd(m,n)\log\!\left(1-x^{\operatorname{lcm}(m,n)}\right).
\]

Writing

\[
\Lambda(x)=-\log(1-x),
\]

the boundary expansion is

\[
G^{\rm full}_{m,n}(x)
=
\gcd(m,n)\Lambda(x)
-\gcd(m,n)\log\operatorname{lcm}(m,n)
+o(1).
\]

PC-056 classified the leading coefficient

\[
K(m,n)=\gcd(m,n)
\]

as the classical Smith GCD form and showed that Möbius birth extraction orthogonalizes it exactly. The remaining canonical finite matrix is therefore

\[
\boxed{
R(m,n)
=
-\gcd(m,n)\log\operatorname{lcm}(m,n).
}
\]

This is already a genuinely non-diagonal, cross-level object forced by the two-dimensional harmonic energy. The question is whether its primitive-shell version retains a nontrivial collective spectrum after the leading Smith form has been removed.

## 2. The finite matrix is the tangent of a classical power-GCD family

Introduce

\[
H_t(m,n)
=
\gcd(m,n)\operatorname{lcm}(m,n)^{-t}.
\]

Since

\[
\operatorname{lcm}(m,n)=\frac{mn}{\gcd(m,n)},
\]

we have

\[
\boxed{
H_t(m,n)
=
m^{-t}n^{-t}\gcd(m,n)^{1+t},
}
\]

and hence

\[
\boxed{
R=H'_0.
}
\]

On a finite divisor-closed set let \(Z\) be the divisor-incidence matrix,

\[
Z(n,d)=\mathbf 1_{d\mid n},
\]

let \(M=Z^{-1}\) be its Möbius inverse, and let

\[
J_\alpha(n)
=
n^\alpha\prod_{p\mid n}(1-p^{-\alpha})
\]

be the generalized Jordan totient. The classical Smith/meet-matrix identity extends to the power-GCD family as

\[
\boxed{
\bigl[\gcd(m,n)^\alpha\bigr]
=
Z D_{J_\alpha} Z^{\mathsf T}.
}
\]

With \(D_t=\operatorname{diag}(n^{-t})\),

\[
\boxed{
H_t=D_t Z D_{J_{1+t}} Z^{\mathsf T}D_t.
}
\]

So the finite boundary correction is not an unrelated new matrix: it is the derivative at \(t=0\) of the same generalized Smith family whose value at \(t=0\) produced the leading GCD collision metric.

## 3. Möbius extraction turns the tangent into von Mangoldt incidence plus a diagonal term

Let

\[
L=\operatorname{diag}(\log n)
\]

and differentiate the previous identity at \(t=0\). Since \(D'_0=-L\) and \(J_1=\varphi\),

\[
R=-LK-KL+Z D_{J'_1}Z^{\mathsf T},
\qquad
K=Z D_\varphi Z^{\mathsf T}.
\]

Apply primitive-shell extraction on both sides:

\[
B:=MRM^{\mathsf T}.
\]

Then

\[
\boxed{
B
=
D_{J'_1}
-
A D_\varphi
-
D_\varphi A^{\mathsf T},
\qquad
A:=MLZ.
}
\]

The matrix \(A\) has an exact arithmetic description. If \(d\mid n\),

\[
A_{n,d}
=
\sum_{\substack{k\mid n\\ d\mid k}}
\mu(n/k)\log k.
\]

Writing \(q=n/d\) and \(k=dr\), Möbius inversion of \(\log\) gives

\[
\boxed{
A_{n,d}
=
\begin{cases}
\log n,&n=d,\\[1mm]
\Lambda(n/d),&d\mid n,\ d<n,\\[1mm]
0,&d\nmid n.
\end{cases}
}
\]

Thus the exact common-vertex von Mangoldt arithmetic reappears here not through an externally chosen Dirichlet transform, but as the incidence derivative of the generalized Smith family.

Also,

\[
J'_1(n)
=
\varphi(n)
\left(
\log n+\sum_{p\mid n}\frac{\log p}{p-1}
\right).
\]

Consequently the entries of the finite primitive-shell Gram matrix are

\[
\boxed{
B_{n,n}
=
\varphi(n)
\left(
-\log n+\sum_{p\mid n}\frac{\log p}{p-1}
\right)
=
-\log|\operatorname{Disc}\Phi_n|,
}
\]

and, for \(d<n\),

\[
\boxed{
B_{n,d}
=
\begin{cases}
-\varphi(d)\log p,&n/d=p^k,\\
0,&\text{otherwise},
\end{cases}
}
\]

with symmetry \(B_{d,n}=B_{n,d}\). This recovers exactly the resultant/discriminant finite parts of PC-002/PC-006, but now as one differentiated incidence operator.

## 4. Shell normalization makes every divisor box an exact Kronecker sum

Normalize by primitive-shell populations,

\[
\boxed{
C=D_\varphi^{-1/2} B D_\varphi^{-1/2}.
}
\]

Let

\[
N=\prod_{p\mid N}p^{A_p}
\]

and restrict \(C\) to the full divisor box

\[
\mathcal D(N)=\{d:d\mid N\}.
\]

Identify each divisor with its valuation tuple

\[
d\longleftrightarrow(a_p)_{p\mid N},
\qquad
0\le a_p\le A_p.
\]

The diagonal entry separates additively:

\[
C_{d,d}
=
\sum_{p\mid N}
(\log p)
\left[
-a_p+\frac{\mathbf 1_{a_p>0}}{p-1}
\right].
\]

An off-diagonal entry is nonzero only when the two tuples differ in exactly one prime coordinate, because the ratio must be a prime power. Moreover the shell normalization cancels every unchanged prime factor. Therefore

\[
\boxed{
C_{\mathcal D(N)}
=
\bigoplus_{p\mid N}^{\rm Kron}
H_{p,A_p}
:=
\sum_{p\mid N}
I\otimes\cdots\otimes H_{p,A_p}\otimes\cdots\otimes I.
}
\]

This is an exact Kronecker **sum**, not an approximation or an asymptotic statement.

For one prime put

\[
q=p^{-1/2},
\qquad
s=\sqrt{1-q^2},
\qquad
c=\frac1{p-1}=\frac{q^2}{1-q^2},
\]

and write

\[
H_{p,A}=(\log p)\,h_{p,A}
\]

on exponents \(a=0,\ldots,A\). Then

\[
\boxed{
(h_{p,A})_{00}=0,
}
\]

\[
\boxed{
(h_{p,A})_{0b}=(h_{p,A})_{b0}
=
-\frac{q^b}{s},
\qquad b\ge1,
}
\]

while for \(a,b\ge1\),

\[
\boxed{
(h_{p,A})_{ab}
=
\begin{cases}
-a+c,&a=b,\\
-q^{|a-b|},&a\ne b.
\end{cases}
}
\]

The positive-exponent off-diagonal part is the familiar geometric/Kac–Murdock–Szegő kernel, but the distinguished exponent-zero row and the linear diagonal come from the primitive-shell boundary renormalization.

## 5. Every prime-local spectrum is elementary

The local matrix above diagonalizes exactly.

First, the vector

\[
u^{(*)}
=
\left(
\frac{q^A}{s},
q^{A-1},
q^{A-2},
\ldots,
q,
1
\right)^{\mathsf T}
\]

satisfies

\[
\boxed{
h_{p,A}u^{(*)}=-A\,u^{(*)}.
}
\]

For every \(j=0,\ldots,A-1\), define \(u^{(j)}\) with support only on coordinates \(0,\ldots,j+1\) by

\[
u^{(j)}_0=-q^{j-1}s,
\]

\[
u^{(j)}_a=(q^2-1)q^{j-1-a},
\qquad
1\le a\le j,
\]

\[
u^{(j)}_{j+1}=1,
\qquad
u^{(j)}_a=0\quad(a>j+1).
\]

A direct geometric-series substitution gives

\[
\boxed{
h_{p,A}u^{(j)}
=
(c-j)u^{(j)}.
}
\]

The \(A+1\) eigenvalues are distinct: \(c-j>-A\) for \(0\le j<A\). Hence these vectors form a complete eigenbasis and

\[
\boxed{
\operatorname{Spec}(H_{p,A})
=
(\log p)
\left(
\{-A\}
\cup
\left\{
\frac1{p-1}-j:
j=0,\ldots,A-1
\right\}
\right).
}
\]

Equivalently,

\[
\boxed{
\det(\lambda I-h_{p,A})
=
(\lambda+A)
\prod_{j=0}^{A-1}
\left(\lambda-\frac1{p-1}+j\right).
}
\]

No numerical diagonalization or limiting argument is used.

## 6. The full divisor-box spectrum is therefore explicit and additive

The Kronecker-sum identity immediately gives

\[
\boxed{
\operatorname{Spec} C_{\mathcal D(N)}
=
\left\{
\sum_{p\mid N}(\log p)\,\xi_p:
\;
\xi_p\in
\left(
\{-A_p\}
\cup
\left\{
\frac1{p-1}-j:
0\le j<A_p
\right\}
\right)
\right\}.
}
\]

Thus all finite spectral data of the normalized renormalized boundary operator on a divisor box are obtained by taking independent sums of elementary one-prime levels.

For example, if \(N\) is squarefree then every local block has only two eigenvalues,

\[
-\log p,
\qquad
\frac{\log p}{p-1},
\]

so the entire \(2^{\omega(N)}\)-dimensional spectrum consists of the corresponding subset sums.

This is the decisive collapse. The operator is intrinsically two-dimensional in origin, non-diagonal in shell index, cross-level, and uses both resultants and discriminants. Nevertheless, after the canonical birth normalization its spectral problem does not couple distinct primes.

## 7. Why this does not produce a new RH mechanism

The finite renormalized term was one of the strongest natural escape routes left by PC-056 because it survives after the leading GCD collision metric has been divided out. The exact factorization above shows that its ordinary spectral content is still completely arithmetic and separable:

\[
\boxed{
\text{finite boundary energy}
\to
\text{power-GCD tangent}
\to
\text{von Mangoldt divisor incidence}
\to
\text{independent prime-local chains}.
}
\]

There is no intrinsic complex parameter, no functional-equation involution, no gamma factor, and no unexplained spectral locus. On every divisor box the zeros of a characteristic polynomial are the explicit real sums displayed above.

One can of course attach a Dirichlet/Mellin parameter afterward, sum the local data over primes, or form an Euler product from them. But that would reintroduce the already-classified von Mangoldt/zeta machinery externally. The finite boundary Gram operator itself does not create the zero side of the explicit formula.

Accordingly the route

\[
\boxed{
\text{finite renormalized 2D Dirichlet boundary term}
\to
\text{primitive-shell spectral determinant}
\to
\text{new critical-line mechanism}
}
\]

fails for the canonical divisor-box exhaustion.

## 8. Prior-art and novelty audit

The broad matrix technology is classical. Smith's 1875 GCD determinant and the Le Paige/Johnson incidence factorization already anchor PC-056. Power-GCD matrices and their Smith-type generalizations are also established literature; for example S. Hong, X. Zhou and J. Zhao, **Power GCD Matrices for a UFD**, *Algebra Colloquium* **16**:1 (2009), 71–78, DOI `10.1142/S100538670900008X`, studies power-GCD matrices, their structure and determinants on factor-closed settings. General meet-matrix theory likewise contains the incidence-factorization viewpoint.

The geometric off-diagonal kernel \(q^{|a-b|}\) is the classical Kac–Murdock–Szegő Toeplitz kernel. That neighboring literature does not by itself supply the bordered, linearly shifted matrix above, but it makes clear that geometric Toeplitz structure is not novel.

Directed searches did **not** locate a source stating the exact prime-circle chain spectrum

\[
\{-A\}\cup\{(p-1)^{-1}-j:0\le j<A\}
\]

for this boundary-renormalized birth matrix, nor the exact prime-circle Kronecker-sum formulation. No historical novelty is claimed from that absence. The durable contribution is instead the negative classification: the canonical finite term left open by PC-056 is explicitly solvable and prime-separable once the classical power-GCD factorization is differentiated and the primitive basis is used.

## 9. Boundary and falsification tests

The claim is deliberately finite and exact. It can be falsified by any failure of the following checks:

1. differentiate
   \[
   H_t(m,n)=m^{-t}n^{-t}\gcd(m,n)^{1+t}
   \]
   at \(t=0\) and recover \(-\gcd(m,n)\log\operatorname{lcm}(m,n)\);
2. verify the generalized Smith factorization with \(J_\alpha\) on arbitrary finite divisor-closed sets;
3. compute \(A=MLZ\) and check that its strict divisor entries are \(\Lambda(n/d)\);
4. compare \(B=MRM^T\) with the exact resultant/discriminant finite parts from PC-006;
5. on arbitrary \(N\), permute the normalized divisor matrix into valuation-tuple order and verify the Kronecker-sum decomposition;
6. substitute the displayed local eigenvectors and recover all \(A+1\) eigenvalues.

The result does **not** exclude an operator that mixes the leading and finite boundary pieces nonlinearly before taking the limit, a non-factor-closed exhaustion with a geometry-derived reason for that choice, or the global uniformization/monodromy sector. Any such escape must identify a coupling that is absent from the exact differentiated Smith structure above.
