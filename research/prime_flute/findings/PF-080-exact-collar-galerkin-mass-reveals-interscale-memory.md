# PF-080 — exact collar Galerkin mass reveals a candidate interscale-memory term

**Status:** `EXACT-DERIVED` for the harmonic-collar Ritz operator and its finite-matrix multiscale expansion; `CANDIDATE-NEW-SECOND-ORDER-MECHANISM` for the corresponding second-order term of the true surface spectrum/scattering. No RH claim.

PF-079 showed that, in a strongly hierarchical prime-derived degeneration, the leading physical-scattering profile at each neck scale is universal: the arithmetic information is primarily in the scale at which the profile appears. This finding asks the next natural question: **what is the first correction that can remember more than the current scale?**

The answer is already nontrivial at the canonical variational level. If one retains not only the exact collar conductance but also its exact \(L^2\) mass, the tangent has a completely explicit generalized graph eigenproblem. In a hierarchy of necks, the first finite-matrix correction contains an effective-resistance term involving *all stronger upstream necks*. This is a genuine interscale memory mechanism. What remains open is to prove that the true Laplace eigenvalues or scattering poles inherit that coefficient rather than only its scale.

## 1. Exact maximal-collar coordinates

For a separating geodesic of length \(L\), the standard maximal collar is

\[
C_L=\{(r,\theta):|r|<w(L),\ \theta\in\mathbb R/\mathbb Z\},
\]

with

\[
ds^2=dr^2+L^2\cosh^2r\,d\theta^2,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}.
\]

Set

\[
A(L):=\arctan\!\bigl(\operatorname{csch}(L/2)\bigr)
=2\arctan(e^{-L/2})
\]

and introduce the conformal coordinate

\[
t=\frac1L\arctan(\sinh r).
\]

Then

\[
t\in[-T,T],\qquad T=\frac{A(L)}L,
\]

and

\[
\boxed{
ds^2=L^2\sec^2(Lt)(dt^2+d\theta^2).
}
\]

The reflection \(r\mapsto-r\), which is the intrinsic zero-twist symmetry of the collar, becomes \(t\mapsto-t\). Thus the construction respects the exact interior/exterior pairing of the two collar sides.

## 2. Exact stiffness: the collar capacity

For endpoint values \(c_-\) and \(c_+\), the \(\theta\)-independent harmonic interpolant is linear in \(t\):

\[
u(t)=\frac{c_-+c_+}{2}+\frac{c_+-c_-}{2T}t.
\]

Dirichlet energy is conformally invariant in dimension two, so

\[
E_{C_L}(u)
=\frac{|c_+-c_-|^2}{2T}.
\]

Hence the exact conductance/capacity of the collar is

\[
\boxed{
\kappa(L)=\frac1{2T}
=\frac{L}{2A(L)}
=\frac{L}{4\arctan(e^{-L/2})}.
}
\]

This is the exact quantity already isolated in PF-056. For \(L\to0\),

\[
\boxed{
\kappa(L)=\frac L\pi+\frac{L^2}{\pi^2}+O(L^3).
}
\]

## 3. Exact \(L^2\) mass of the harmonic collar element

The previous graph reductions retained the stiffness but effectively lumped the \(L^2\) mass into the adjacent pairs of pants. The conformal coordinate lets us integrate the mass exactly.

Let

\[
N_\pm(t)=\frac{1\pm t/T}{2}
\]

be the two harmonic endpoint basis functions. Write

\[
a(L):=L\sinh w(L)=L\,\operatorname{csch}(L/2),
\]

so that \(a(L)\) is the area of a half-collar and the full collar has area \(2a(L)\).

The off-diagonal mass is

\[
\boxed{
m(L)
=\frac L4
\int_{-A}^{A}
\sec^2y\left(1-\frac{y^2}{A^2}\right)dy.
}
\]

Equivalently,

\[
\boxed{
m(L)=L\left[
-\frac{\log(\cos A)}A
+\frac1{A^2}\int_0^A\log(\cos y)\,dy
\right],
}
\]

where \(A=A(L)\) and \(\cos A=\tanh(L/2)\).

By symmetry and the identity \(N_-+N_+=1\), the exact two-endpoint collar mass matrix is

\[
\boxed{
M_e(L)=
\begin{pmatrix}
a(L)-m(L)&m(L)\\
m(L)&a(L)-m(L)
\end{pmatrix}.
}
\]

As \(L\to0\),

\[
\boxed{
m(L)=\frac{2L}{\pi}\log\frac1L+O(L).
}
\]

The logarithm is important: the mass correction is parametrically larger than an ordinary analytic \(L^2\) correction.

## 4. Exact canonical Ritz problem for a prime tangent

Suppose the multi-gap separating geodesics split a finite tangent \(Y_H\) into \(N\) pairs of pants arranged in a path. Each pair of pants has area exactly \(2\pi\). For edge \(e=(i,i+1)\), put

\[
B_e=(e_i-e_{i+1})(e_i-e_{i+1})^T.
\]

Use the canonical finite-dimensional trial space consisting of functions that are constant on each pants core and harmonically interpolated across every maximal collar.

The stiffness matrix is exactly

\[
\boxed{
K_H=\sum_e\kappa(L_e)B_e.
}
\]

When the core areas and exact collar masses are assembled, all half-collar area terms cancel and the consistent \(L^2\) mass matrix simplifies to

\[
\boxed{
M_H=2\pi I-\sum_e m(L_e)B_e.
}
\]

In particular,

\[
\boxed{M_H\mathbf1=2\pi\mathbf1.}
\]

Thus the geometry itself produces the generalized eigenproblem

\[
\boxed{
K_Hc=\nu M_Hc.
}
\]

No graph weights or vertex masses have been chosen externally. Both are exact integrals of the hyperbolic metric on the orthogonal-circle collars.

By Rayleigh-Ritz/min-max, its generalized eigenvalues give rigorous upper bounds for the corresponding Laplace eigenvalues in the finite-dimensional variational range. Consequently, any \(\nu_j<1/4\) is a non-asymptotic certificate for small spectrum of the tangent, improving the mass-lumped bound of PF-056.

## 5. Four-punctured tangent: an exact Ritz formula

For \(S_{0,4}\), there is one separating neck \(L\). On the antisymmetric vector \((1,-1)\),

\[
K=\kappa(L)B,
\qquad
M=2\pi I-m(L)B,
\]

so the unique nonzero generalized eigenvalue is exactly

\[
\boxed{
\nu_{\rm Ritz}(L)=\frac{\kappa(L)}{\pi-m(L)}.
}
\]

As \(L\to0\),

\[
\boxed{
\nu_{\rm Ritz}(L)
=\frac{L}{\pi^2}
+\frac{2}{\pi^4}L^2\log\frac1L
+O(L^2).
}
\]

The first term is Burger's graph scale. The next term appears automatically from the exact collar mass and has the same \(L^2|\log L|\) scale that occurs in sharp one-collar degeneration estimates. This agreement of scales is encouraging, but **the coefficient above is a Ritz coefficient, not yet a theorem about the true \(\lambda_1\)**.

## 6. Hierarchical necks: the graph already remembers stronger scales

Now take a strongly ordered path of neck weights

\[
w_1\gg w_2\gg\cdots\gg w_{N-1}>0,
\]

with \(w_j\) denoting the current weak edge. At leading order, PF-054/PF-079 give the universal eigenvalue

\[
\mu_j^{(0)}=\frac{j+1}{j}w_j.
\]

Let \(L_C\) be the weighted Laplacian of the already-contracted cluster of the first \(j\) vertices, using the stronger weights \(w_1,\ldots,w_{j-1}\). A Schur/Feshbach expansion of the finite graph gives an upstream correction governed by

\[
R_C=e_j^TL_C^+e_j.
\]

For a path this quantity is explicit. Solving

\[
L_Cx=e_j-\frac1j\mathbf1
\]

shows that edge \(m<j\) carries current \(m/j\), hence

\[
\boxed{
R_C=\frac1{j^2}
\sum_{m=1}^{j-1}\frac{m^2}{w_m}.
}
\]

Including the first weaker downstream edge \(w_{j+1}\), the graph eigenvalue has the expansion

\[
\boxed{
\mu_j
=
\frac{j+1}{j}w_j
+\frac{j}{j+1}w_{j+1}
-\frac{j+1}{j^3}w_j^2
\sum_{m<j}\frac{m^2}{w_m}
+\text{higher-order terms}.
}
\]

Thus the first finite-dimensional correction splits into three geometrically distinct mechanisms once the exact collar mass is restored:

1. **upstream memory:** a negative effective-resistance term involving every stronger neck;
2. **downstream leakage:** a positive term from the next weaker neck;
3. **local collar mass:** a universal \(w_j^2\log(1/w_j)\) correction.

After the Burger normalization by \(2\pi^2\), the upstream term is

\[
-\frac{j+1}{2\pi^2j^3}
\,w_j^2
\sum_{m<j}\frac{m^2}{w_m}.
\]

This is the first mechanism in the current program in which a single spectral scale can remember an **ordered collection of earlier cuff contrasts**, rather than only the current adjacent ratio.

## 7. Prime-cuff interpretation

For the hierarchical prime tangents,

\[
w_m=L_{m+1}
\sim4\sqrt{\frac{d_m}{d_{m+1}}}
\sim4\exp\left[-\frac{\ell_m-\ell_{m+1}}4\right].
\]

Therefore the upstream memory contains the multi-cuff combination

\[
\boxed{
w_j^2\sum_{m<j}\frac{m^2}{w_m},}
\]

which is not a function of the current contrast \(\ell_j-\ell_{j+1}\) alone.

For the very strong hierarchies obtainable in PF-054, one may arrange roughly

\[
w_j\asymp w_{j-1}^2,
\qquad
w_{j+1}\asymp w_j^2.
\]

Then the scales are

\[
\text{upstream memory}\asymp\frac{w_j^2}{w_{j-1}}
\asymp w_{j-1}^3,
\]

whereas

\[
\text{local collar mass}\asymp w_j^2\log(1/w_j)
\asymp w_{j-1}^4\log(1/w_{j-1}),
\]

and

\[
\text{downstream leakage}\asymp w_{j+1}\asymp w_{j-1}^4.
\]

So in this regime the **nonlocal upstream memory is parametrically larger than the universal local second-order correction**.

This is exactly the kind of information that PF-079 said must live beyond the universal leading tropical profile.

## 8. What is proved and what is not

### Proved here

- the exact conformal collar coordinate;
- the exact collar capacity \(\kappa(L)\);
- the exact consistent collar mass \(m(L)\) and mass block;
- the exact global harmonic-collar Ritz matrices
  \[
  K_H=\sum\kappa_eB_e,
  \qquad
  M_H=2\pi I-\sum m_eB_e;
  \]
- the exact \(S_{0,4}\) Ritz eigenvalue;
- the finite weighted-path effective-resistance correction above.

### Not yet proved

It is **not** yet proved that the true surface eigenvalue or physical-scattering pole has the same second-order upstream coefficient.

The existing surface-to-graph results establish the leading graph reduction. Sharp one-neck results control the next scale very precisely, but the available multi-neck literature found in the novelty audit establishes first-order dependence on the collapsing disconnecting lengths rather than the specific multiscale coefficient above.

Therefore the substantive conjectural statement is:

> In a sufficiently separated multi-neck degeneration, after the universal leading tropical term is removed, the first prime-sensitive correction of the true small spectrum/scattering contains the same effective-resistance memory of the stronger-side neck hierarchy as the canonical harmonic-collar Ritz operator.

A proof needs a second-order multiscale Feshbach estimate for the *surface* Laplacian, not another graph calculation.

## 9. Literature / novelty audit

Known ingredients include:

- Burger's first-order reduction of small eigenvalues of degenerating hyperbolic surfaces to weighted graph Laplacians;
- sharp one-disconnecting-collar estimates and polyhomogeneous information of Große-Rupflin;
- Chaudhary's extension of first-order small-eigenvalue dependence to multiple collapsing geodesics;
- standard capacity/effective-resistance and Schur/Feshbach theory;
- standard consistent-mass Galerkin ideas in numerical spectral approximation.

Directed searches for combinations of *hyperbolic collar + exact mass matrix*, *degenerating hyperbolic surface + Galerkin + effective resistance*, and *multi-collar second-order small eigenvalue + effective resistance* did not locate the exact matrices or the upstream-memory formula above.

No novelty is claimed for any abstract method. The potentially new narrow object is the **exact hyperbolic harmonic-collar consistent-mass reduction, specialized to the prime-derived multiscale tangent, and its resulting effective-resistance memory term**.

## 10. Falsification / next mathematical test

The intuition fails as a statement about the true spectrum if, for a two- or three-scale degeneration,

\[
\lambda_j^{\rm true}-\nu_j^{\rm Ritz}
\]

is of order \(w_j^2/w_{j-1}\) with an unrelated leading coefficient, or larger.

The decisive next theorem is therefore a uniform multiscale estimate of the form

\[
\boxed{
\lambda_j^{\rm true}
=\nu_j^{\rm Ritz}
+o\left(\frac{w_j^2}{w_{j-1}}\right)
}
\]

in a separated hierarchy. A weaker but still informative target is to show that the true coefficient of \(w_j^2/w_{j-1}\) equals the effective-resistance coefficient after projecting to the almost-constant pants modes.

If this holds, the first subleading spectral/scattering correction would contain genuinely nonlocal information about several prime-cuff contrasts even though the PF-079 leading profile is universal.
