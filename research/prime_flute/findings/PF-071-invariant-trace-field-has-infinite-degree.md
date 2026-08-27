# PF-071 — the prime-flute invariant trace field has infinite degree

**Status:** `DECISIVE-NEGATIVE` for arithmetic / semi-arithmetic / fixed-number-field spectral mechanisms; `EXACT-DERIVED`.

## Claim

Let \(\Gamma_{\rm prime}<\mathrm{PSL}_2(\mathbb R)\) be the exact zero-twist prime-flute group in the generator convention used in PF-018. Its cusp parabolics have fixed points

\[
c_n=-u_n=-\cot\frac{\pi}{p_n}.
\]

Then the invariant trace field

\[
k_{\Gamma}:=
\mathbb Q\bigl(\operatorname{tr}\gamma:\gamma\in\Gamma^{(2)}\bigr),
\qquad
\Gamma^{(2)}=\langle\gamma^2:\gamma\in\Gamma\rangle,
\]

has infinite degree over \(\mathbb Q\):

\[
\boxed{[k_\Gamma:\mathbb Q]=\infty.}
\]

Consequently no conjugate of \(\Gamma_{\rm prime}\) is contained in \(\mathrm{PSL}_2(K)\) for any number field \(K\). In particular it cannot be a subgroup of an arithmetic or semi-arithmetic Fuchsian lattice with finite-degree invariant trace field, and the prime-flute cannot obtain Hecke/congruence/arithmetic spectral structure by being an infinite-sheeted cover of such a finite-area orbifold.

This is an algebraic obstruction independent of the zero-systole obstruction of PF-070.

## 1. Cusp cross-ratios are already visible in invariant traces

Use trace-\(+2\) lifts of the primitive cusp parabolics in the standard form

\[
Q(c,D)=
\begin{pmatrix}
1+cD&-c^2D\\
D&1-cD
\end{pmatrix}.
\]

PF-018 gives exactly this parabolic geometry, with fixed point \(c_n=-u_n\) and a nonzero raw width parameter \(D_n\). For two such parabolics,

\[
\boxed{
\operatorname{tr}(Q_iQ_j)
=2-D_iD_j(c_i-c_j)^2.
}
\]

The Fricke trace identity with \(\operatorname{tr}Q_i=\operatorname{tr}Q_j=2\) gives

\[
\boxed{
\operatorname{tr}[Q_i,Q_j]-2
=D_i^2D_j^2(c_i-c_j)^4.
}
\]

The commutator belongs to \(\Gamma^{(2)}\): the quotient \(\Gamma/\Gamma^{(2)}\) has exponent two, hence is abelian, so the commutator subgroup is contained in \(\Gamma^{(2)}\). Therefore

\[
B_{ij}:=\operatorname{tr}[Q_i,Q_j]-2\in k_\Gamma.
\]

For four distinct cusps,

\[
\frac{B_{ij}B_{k\ell}}
     {B_{ik}B_{j\ell}}
=
\left(
\frac{(c_i-c_j)(c_k-c_\ell)}
     {(c_i-c_k)(c_j-c_\ell)}
\right)^4.
\]

Thus

\[
\boxed{
[c_i,c_j;c_k,c_\ell]^4\in k_\Gamma
}
\]

(up to the conventional permutation of the cross-ratio). All cusp-width factors cancel. This is intrinsic under independent cusp normalization and under global Möbius conjugacy.

## 2. Prime cusp coordinates have unbounded cyclotomic degree

For an odd prime \(p\), put

\[
t_p=\cot\frac{\pi}{p},
\qquad
\zeta_p=e^{2\pi i/p}.
\]

The elementary identities

\[
t_p=i\frac{\zeta_p+1}{\zeta_p-1},
\qquad
\zeta_p=\frac{t_p+i}{t_p-i}
\]

show

\[
\mathbb Q(t_p,i)=\mathbb Q(\zeta_p,i).
\]

Since \(t_p\) is real, adjoining \(i\) has degree two. For odd \(p\), the cyclotomic fields of conductors \(p\) and \(4\) have trivial intersection, so

\[
[\mathbb Q(\zeta_p,i):\mathbb Q]=2(p-1).
\]

Hence

\[
\boxed{
[\mathbb Q(t_p):\mathbb Q]=p-1.
}
\]

The algebraic complexity of the exact prime cusp positions therefore tends to infinity with \(p\).

## 3. Contradiction with a finite-degree invariant trace field

Fix three distinct cusp points \(c_a,c_b,c_c\), and let \(K_0=\mathbb Q(c_a,c_b,c_c)\). For every other prime cusp define the cross-ratio

\[
x_p=
\frac{(c_p-c_a)(c_b-c_c)}
     {(c_p-c_c)(c_b-c_a)}.
\]

This is a nonconstant Möbius transform of \(c_p\) with coefficients in \(K_0\), so

\[
K_0(x_p)=K_0(c_p).
\]

Section 1 gives

\[
x_p^4\in k_\Gamma.
\]

Suppose for contradiction that \([k_\Gamma:\mathbb Q]<\infty\). Since \(x_p\) satisfies \(X^4-x_p^4=0\) over \(k_\Gamma\),

\[
[K_0k_\Gamma(x_p):K_0k_\Gamma]\le4.
\]

As \(c_p\in K_0(x_p)\), this yields the uniform bound

\[
[\mathbb Q(c_p):\mathbb Q]
\le
4[K_0k_\Gamma:\mathbb Q],
\]

independent of \(p\). But \(c_p=-t_p\) and Section 2 gives

\[
[\mathbb Q(c_p):\mathbb Q]=p-1\to\infty.
\]

Contradiction. Therefore

\[
\boxed{[k_\Gamma:\mathbb Q]=\infty.}
\]

## 4. Spectral consequence

Translation lengths and traces are linked by

\[
2\cosh\frac{\ell(\gamma)}2=|\operatorname{tr}\gamma|.
\]

Thus the exact prime-flute holonomy/length system cannot live over a fixed number field in the way arithmetic and semi-arithmetic Fuchsian spectral theories do.

This rules out the branch

\[
\boxed{
\text{prime-flute holonomy / cuffs}
\to
\text{fixed arithmetic trace field}
\to
\text{Hecke/congruence or arithmetic-thin spectral mechanism}.
}
\]

It is stronger algebraically than merely observing that the surface has infinite area or zero systole: even if one drops cofinite generation and asks only for a conjugation of the whole prime group into \(\mathrm{PSL}_2(K)\) for a number field \(K\), it is impossible.

It also complements PF-055. PF-055 showed that the gap-dependent four-punctured tangents are arithmetic only at five exceptional ratios. PF-071 says that the **global infinite group itself** has no finite-degree invariant trace field at all.

This does **not** rule out the ordinary Selberg/scattering theory of each finite tangent \(Y_H\), nor does it say that individual finite subgroups cannot lie in number fields. The obstruction is global and comes from the unbounded sequence of prime cyclotomic degrees.

## 5. Interior/exterior and exact-geometry compatibility

The proof uses only cusp fixed points and fourth powers of cross-ratios. Hence it is invariant under global Möbius conjugacy. The ambient interior/exterior involution merely conjugates/permutates these real cross-ratios and does not remove the degree growth. No choice of raw cusp width is involved; all \(D_i\) cancel exactly.

## Literature / novelty check

Known ingredients:

- invariant trace fields and Takeuchi's arithmeticity criterion are classical;
- arithmetic Fuchsian groups have finite-degree number-field invariant trace fields;
- cusp cross-ratios and fields of definition are classical objects in Fuchsian/Kleinian arithmetic;
- the Fricke commutator identity is classical;
- \([\mathbb Q(\cot(\pi/p)):\mathbb Q]=p-1\) is an elementary cyclotomic consequence.

Directed searches for prime/cyclotomic cotangent cusp sets combined with invariant trace fields did not locate this prime-flute specialization. Novelty is claimed conservatively: the mathematical value is primarily the exact obstruction for this construction, not any of the general trace-field theory.

## Lean / symbolic candidates

The finite algebraic core is well suited to formalization:

1. verify \(\operatorname{tr}(Q_iQ_j)=2-D_iD_j(c_i-c_j)^2\);
2. derive \(\operatorname{tr}[Q_i,Q_j]-2=D_i^2D_j^2(c_i-c_j)^4\);
3. prove cancellation to the fourth power of the cross-ratio;
4. keep the cyclotomic degree argument and arithmetic consequences as separate number-theoretic lemmas.
