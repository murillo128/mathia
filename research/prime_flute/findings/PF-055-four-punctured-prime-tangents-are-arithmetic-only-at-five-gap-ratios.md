# PF-055 — four-punctured prime tangents are arithmetic only at five gap ratios

**Status:** `DECISIVE-NEGATIVE` for the branch that tries to explain the prime-sensitive tangent spectrum through modular/arithmetic Fuchsian structure; `EXACT-DERIVED` within the four-punctured tangent family.

PF-044 showed that the one-gap tangent is the universal thrice-punctured sphere and hence inherits modular/Riemann-zeta scattering for reasons completely unrelated to the gap. The next possible place where gap information survives is the four-punctured tangent coming from three prime offsets. This finding asks whether that first moduli-dependent tangent can still be arithmetic, so that its spectral/scattering data might reduce to modular or automorphic-L-function machinery.

The answer is extremely rigid.

## 1. Normalize the exact tangent by the gap ratio

Let

\[
H=\{\eta_1<\eta_2<\eta_3\},\qquad
 d_1=\eta_2-\eta_1,\quad d_2=\eta_3-\eta_2,
\]

and define the scale-free ratio

\[
r:=\frac{d_1}{d_2}>0.
\]

Translation and positive dilation are hyperbolic isometries of the upper-half-plane model, so we may normalize

\[
\eta_1=0,\qquad \eta_2=1,\qquad \eta_3=1+t,
\qquad t=\frac1r.
\]

PF-029 gives the three finite peripheral parabolics in the form

\[
Q(c,D)=
\begin{pmatrix}
1+cD&-c^2D\\
D&1-cD
\end{pmatrix}
\]

with

\[
(c_1,D_1)=(0,2),
\]

\[
(c_2,D_2)=\left(-1,2\left(1+\frac1t\right)\right),
\]

\[
(c_3,D_3)=\left(-(1+t),\frac2t\right).
\]

They generate the cofinite torsion-free four-cusp tangent group; the fourth peripheral element is the inverse of \(Q_1Q_2Q_3\).

## 2. The two basic hyperbolic traces are exact rational functions of the gap ratio

Direct multiplication gives

\[
\boxed{
\operatorname{tr}(Q_1Q_2)=-2(1+2r),
}
\]

and

\[
\boxed{
\operatorname{tr}(Q_2Q_3)=-2\left(1+\frac2r\right).
}
\]

The remaining pair trace is

\[
\operatorname{tr}(Q_1Q_3)
=-2\left(3+2r+\frac2r\right),
\]

while

\[
\operatorname{tr}(Q_1Q_2Q_3)=2.
\]

These are not arbitrary trace coordinates: PF-029 already identified the first two with the two complementary separating geodesics. For example

\[
\sinh^2\frac{L_{12}}4=r,
\]

so

\[
\frac{|\operatorname{tr}(Q_1Q_2)|}{2}
=1+2r
=\cosh\frac{L_{12}}2.
\]

Thus the arithmetic test below is directly a condition on the exact orthogonal-circle modulus.

## 3. Takeuchi arithmeticity collapses to an elementary integrality test

All generator matrices lie in \(\mathrm{PSL}_2(\mathbb Q)\) because \(r\in\mathbb Q_{>0}\) for integer prime gaps. Hence the invariant trace field is \(\mathbb Q\).

For a cofinite Fuchsian group with invariant trace field \(\mathbb Q\), Takeuchi's arithmeticity criterion reduces to trace integrality: there are no nontrivial embeddings of \(\mathbb Q\), so arithmeticity is equivalent to the relevant trace set being algebraic-integral, i.e. integral. Equivalently in the nonuniform case one may use the standard formulation that all trace squares are integers.

Necessity is immediate from the two pair traces. Arithmeticity forces

\[
-2(1+2r)\in\mathbb Z
\quad\text{and}\quad
-2\left(1+\frac2r\right)\in\mathbb Z,
\]

hence

\[
4r\in\mathbb Z,
\qquad
\frac4r\in\mathbb Z.
\]

Write \(r=a/b\) in lowest terms. Then

\[
b\mid4,\qquad a\mid4.
\]

Since \((a,b)=1\), the only possibilities are

\[
\boxed{
r\in\left\{\frac14,\frac12,1,2,4\right\}.}
\]

## 4. The five ratios are also sufficient

Assume

\[
4r\in\mathbb Z,
\qquad
4/r\in\mathbb Z.
\]

Then the traces of

\[
Q_1,Q_2,Q_3,
Q_1Q_2,Q_1Q_3,Q_2Q_3,
Q_1Q_2Q_3
\]

are all integers. The classical Fricke/Takeuchi finite-generator trace theorem expresses every trace in the group as an integer polynomial in precisely these finite basic traces. Therefore every group trace is integral.

Since the group is a cofinite nonuniform Fuchsian lattice with trace field \(\mathbb Q\), Takeuchi's criterion now gives arithmeticity.

Consequently the classification within the exact prime-tangent one-parameter family is

\[
\boxed{
Y_{d_1,d_2}\text{ is arithmetic}
\iff
\frac{d_1}{d_2}
\in
\left\{\frac14,\frac12,1,2,4\right\}.
}
\]

Up to reversing the ordered tangent, \(r\leftrightarrow1/r\), this leaves only three marked ratio types: \(1\), \(2\), and \(4\).

## 5. Direct formulation in terms of the distinguished cuffs

For an occurrence of the bounded three-prime pattern near scale \(P\),

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1).
\]

Hence

\[
\boxed{
\frac{d_1}{d_2}
=
\lim_{P\to\infty}
\exp\left[-\frac{\ell_1(P)-\ell_2(P)}2\right].
}
\]

Therefore arithmeticity of the four-punctured tangent is equivalent to the asymptotic cuff contrast landing in the discrete five-point set

\[
\boxed{
\lim_{P\to\infty}
 e^{-(\ell_1-\ell_2)/2}
\in
\left\{\frac14,\frac12,1,2,4\right\}.
}
\]

This is an exact bridge between the prime-derived cuff contrast and arithmeticity of the first nontrivial tangent Fuchsian group.

## 6. Decisive consequence for the hierarchical spectral branch

PF-045--PF-054 deliberately force

\[
\frac{d_1}{d_2}\to0
\]

(and, in the stronger hierarchy, successive ratios tend to zero at separated scales) in order to generate prime-specific small-eigenvalue ladders.

Hence, once the hierarchy is strong enough that

\[
0<\frac{d_1}{d_2}<\frac14,
\]

the corresponding four-punctured tangent is automatically nonarithmetic.

Thus the regime in which the prime-gap contrasts generate the strongest genuinely moduli-dependent Laplace/scattering signal is **disjoint from the arithmetic locus** after finitely many steps:

\[
\boxed{
\text{hierarchical prime spectral ladder}
\Longrightarrow
\text{nonarithmetic four-punctured tangent}.
}
\]

This rules out a tempting explanation of PF-045--PF-054 in which the observed low-energy structure is secretly inherited from modular/congruence spectral theory, Hecke operators, or a standard arithmetic Selberg/L-function factorization.

The tangent still has an ordinary Selberg zeta and scattering matrix because it is finite-area; the point is that the **arithmetic-lattice mechanism** is absent in the prime-sensitive hierarchy.

## 7. Relation to the known classification of modular four-punctured spheres

The classical theory of torsion-free genus-zero index-12 subgroups of \(\mathrm{PSL}_2(\mathbb Z)\) gives a finite list of modular four-cusp surfaces. Sebbar proved that all torsion-free genus-zero index-12 subgroups are congruence and listed the six modular-conjugacy classes; after allowing broader real conjugacy some classes coincide. This is fully consistent with the discreteness found above: the arithmetic locus inside the real one-parameter symmetric four-punctured family must be finite.

No novelty is claimed for Takeuchi's criterion, Fricke trace generation, or the classification of modular four-punctured surfaces.

Directed searches did not locate the exact specialization

\[
\frac{d_1}{d_2}
\in\left\{\frac14,\frac12,1,2,4\right\}
\]

for the prime-flute ideal-quadrilateral tangent, but this may well be implicit in the older four-punctured-sphere classification literature. The substantive result for the present project is the **negative branch closure**: the moduli regime that carries the strongest prime-gap spectral ladders is provably nonarithmetic.

## 8. Research consequence

Do not pursue the PF-054 hierarchy by trying to identify its tangent scattering poles/eigenvalues with modular or Hecke spectra merely because PF-044 exhibited Riemann-zeta scattering in the universal one-gap tangent.

The remaining viable mechanism is genuinely geometric/nonarithmetic:

\[
\text{relative prime gaps}
\to
\text{orthogonal-circle moduli}
\to
\text{nonarithmetic finite tangent}
\to
\text{small Laplace/scattering spectrum}
\to
\text{essential/local spectral data of the infinite flute}.
\]

If a zeta-like object eventually emerges from this branch, it cannot be explained as a routine modular/congruence specialization of the tangents in the hierarchical regime.
