# PC-126 — global Möbius shell resultants factor into collision hyperplanes

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`.

PC-125 classified the one-complex-parameter deformation obtained by multiplying one primitive shell by a scalar before taking its resultant with another shell. Its divisor is finite cyclotomic torsion. The most natural nonuniform geometric response is to let one complete shell move by a circle/projective automorphism instead: a single Möbius map moves different vertices by different Euclidean amounts while preserving the projective geometry of the circle.

That enlargement does not produce a new spectral divisor. For two finite primitive shells, the entire relative Möbius resultant is a classical binary-form resultant which factors, over the cyclotomic splitting field, into one linear collision hyperplane for every ordered vertex pair. Restricting to any one-parameter projective subgroup yields only finitely many elementary zero lattices (semisimple case) or finitely many points (unipotent case). In particular its zero count is `O(T)`, not the `T log T` density of the Riemann zeros.

## 1. Homogeneous primitive-shell forms

For `m>1`, write

\[
r_m:=\varphi(m),
\qquad
F_m(X,Y):=Y^{r_m}\Phi_m(X/Y)
=\prod_{\alpha\in P_m^*}(X-\alpha Y).
\]

Let

\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in GL_2(\mathbb C)
\]

act projectively by

\[
g(z)=\frac{az+b}{cz+d}.
\]

Moving the `m`-shell by `g` while leaving the `n`-shell fixed gives the cleared-denominator polynomial

\[
H_{n,g}(x)
:=(cx+d)^{r_n}
\Phi_n\!\left(\frac{ax+b}{cx+d}\right).
\]

Because

\[
\Phi_n(y)=\prod_{\beta\in P_n^*}(y-\beta),
\]

we have the exact factorization

\[
\boxed{
H_{n,g}(x)
=
\prod_{\beta\in P_n^*}
\bigl((a-c\beta)x+(b-d\beta)\bigr).
}
\]

Define the relative projective shell resultant

\[
\mathcal R_{m,n}(g)
:=
\operatorname{Res}_x\bigl(\Phi_m(x),H_{n,g}(x)\bigr).
\]

Since `Phi_m` is monic,

\[
\boxed{
\mathcal R_{m,n}(g)
=
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}
\Bigl((a-c\beta)\alpha+(b-d\beta)\Bigr).
}
\]

Equivalently, using homogeneous representatives `v_alpha=(alpha,1)^T` and `v_beta=(beta,1)^T`, each factor is the wedge

\[
\det(gv_\alpha,v_\beta)
\]

up to the fixed sign convention. Thus the zero set is exactly

\[
\boxed{
\mathcal R_{m,n}(g)=0
\iff
\exists\,\alpha\in P_m^*,\beta\in P_n^*
\text{ with }g(\alpha)=\beta.
}
\]

There is no hidden many-body divisor: over `Q(mu_lcm(m,n))` it is literally a finite hyperplane arrangement in the four matrix entries.

## 2. The factorization is generic, not specifically arithmetic

Nothing in the preceding factorization uses primality or even roots of unity until the coefficients `alpha,beta` are specified. For arbitrary finite point sets `A,B subset P^1(C)`, the corresponding binary-form resultant under relative `PGL_2` motion is the product of the pairwise brackets

\[
\prod_{\alpha\in A,\beta\in B}\det(gv_\alpha,v_\beta).
\]

Thus the projective deformation has not uncovered a new arithmetic interaction. The only prime-circle specialization is that the hyperplane normals lie in a cyclotomic field and satisfy the finite Galois symmetries of the primitive shells.

This is the appropriate matched control: the same geometric mechanism exists for every pair of finite point clouds on `P^1`. Any claimed RH content would therefore have to come from an additional cross-level or limiting organization, not from the finite Möbius resultant itself.

## 3. Actual circle automorphisms do not supply a holomorphic spectral divisor

The intrinsic automorphism group of the unit disk/circle is `PSU(1,1)`. Its parameters form a real Lie group. In the common formula

\[
z\longmapsto e^{i\theta}\frac{z-u}{1-\overline u z},
\qquad |u|<1,
\]

the coefficient `\overline u` is forced by circle preservation.

Consequently, if one varies the full disk-automorphism parameter `u`, the collision condition

\[
g_u(\alpha)=\beta
\]

is a real codimension-one condition in the real parameter manifold, not the zero divisor of a naturally supplied holomorphic one-complex-variable function. Treating `u` and `\overline u` as independent complex variables already complexifies beyond the intrinsic circle geometry.

This matters for the intended spectral interpretation: the genuine geometric deformation supplies a real group action, while a complex spectral parameter appears only after choosing and complexifying a one-parameter subgroup.

## 4. Every one-parameter subgroup has only elementary zero sets

The complexified one-parameter subgroups of `PGL_2(C)` have the standard semisimple/unipotent dichotomy. Conjugation does not change the following zero-set classification because each collision factor remains linear in the matrix entries.

### Semisimple case

After conjugation one may write

\[
g(t)=h
\begin{pmatrix}
 e^{\lambda t}&0\\
 0&e^{-\lambda t}
\end{pmatrix}
h^{-1},
\qquad \lambda\ne0.
\]

For every fixed pair `(alpha,beta)`, the corresponding collision factor therefore has the form

\[
L_{\alpha,\beta}(t)
=A_{\alpha,\beta}e^{\lambda t}
+B_{\alpha,\beta}e^{-\lambda t}.
\]

If both coefficients are nonzero, its zeros satisfy

\[
\boxed{
e^{2\lambda t}=-\frac{B_{\alpha,\beta}}{A_{\alpha,\beta}},
}
\]

hence form one arithmetic logarithmic lattice

\[
\boxed{
t=
\frac{\Log(-B_{\alpha,\beta}/A_{\alpha,\beta})+2\pi i k}
{2\lambda},
\qquad k\in\mathbb Z.
}
\]

If one coefficient vanishes, the factor has no finite zeros unless it vanishes identically because the chosen subgroup preserves that collision.

### Unipotent case

After conjugation,

\[
g(t)=h
\begin{pmatrix}1&t\\0&1\end{pmatrix}
h^{-1}.
\]

Each collision factor is affine,

\[
L_{\alpha,\beta}(t)=A_{\alpha,\beta}+B_{\alpha,\beta}t,
\]

so it has at most one zero unless it is identically zero.

Therefore a fixed pair of primitive shells and a fixed nondegenerate projective one-parameter motion have a divisor which is a union of at most `r_m r_n` arithmetic lattices in the semisimple case, or at most `r_m r_n` isolated points in the unipotent case.

The scalar deformation of PC-125 is precisely the diagonal semisimple special case. PC-126 shows that allowing the whole shell to move nonuniformly by a global Möbius transformation does not change the analytic type of the divisor.

## 5. Zero-density mismatch with zeta

Let `N_{m,n,g}(T)` count zeros of `mathcal R_{m,n}(g(t))`, with multiplicity, in any fixed-width vertical strip and `|Im t|<=T`, excluding an identically-zero collision factor. The preceding factorization gives

\[
\boxed{
N_{m,n,g}(T)=O_{m,n,g}(T).
}
\]

By contrast the Riemann-von Mangoldt formula gives

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log T).
\]

Thus no fixed finite pair of shells under a global projective one-parameter deformation can reproduce even the zero-counting law of `zeta`, before asking for the functional equation or the critical line. Reparametrizing `t` nonlinearly to force a `T log T` density would add external analytic structure rather than derive it from the circle action.

For an actual real `PSU(1,1)` subgroup the obstruction is stronger: real collision times are ordinary vertex coincidences. The infinite complex replicas appear only after analytic continuation of the group parameter and remain exact arithmetic translates imposed by the exponential parametrization.

## 6. Relation to PC-026 and PC-125

PC-026 classifies finite projective invariants of a fixed prime polygon: its cross-ratios are cyclotomic units and their logarithms lie in the classical `L(1,chi)` package. The present result addresses a different proposed escape: **move one whole shell relative to another before taking the resultant**. The finite relative-moduli divisor is not a new projective spectrum; it is the classical bracket product detecting pairwise collisions.

PC-125 treated the scalar subgroup `z -> t z` and obtained a cyclotomic torsion divisor in `t`. PC-126 closes the much larger family in which the same global Möbius transformation acts on every vertex of one shell. Although such a transformation is nonuniform in Euclidean coordinates, its resultant remains a finite binary-form covariant and every one-parameter spectralization remains elementary.

PC-013 and PC-018 are complementary. They rule out projective moving-frame/path-order holonomies that telescope or form exact cocycles. PC-126 instead rules out a finite relative-projective **collision determinant** even before any transport is composed.

## 7. Prior art and novelty audit

The algebraic mechanism is classical invariant theory, not a new resultant theorem.

- J. P. S. Kung and G.-C. Rota, **The invariant theory of binary forms**, *Bulletin of the American Mathematical Society* 10:1 (1984), 27–85, DOI `10.1090/S0273-0979-1984-15188-7`, gives a modern account of binary forms, homogenized roots, brackets, covariants, and linear changes of variables. In classical invariant theory the resultant of two binary forms is a simultaneous invariant, and its root description is a product of pairwise brackets.
- PC-125 already records Apostol's 1975 scaled cyclotomic resultant as the direct prior art for the diagonal subgroup.
- The Riemann-von Mangoldt zero-counting asymptotic is classical; the `O(T)` versus `T log T` comparison here is only a falsification test for this finite projective candidate.

Directed searches for Möbius/fractional-linear cyclotomic resultants did not expose an additional prime-circle mechanism beyond this standard binary-form covariance. No theorem-level novelty is claimed. The durable contribution is the scope classification: **global projective nonuniformity is still too finite and too algebraic to escape the finite collision-resultant class**.

## 8. Boundary of the obstruction

PC-126 rules out resultant spectralizations in which one finite primitive shell is moved relative to another by a single global projective transformation, including every intrinsic anchor-fixing/circle-preserving subgroup and every one-parameter complexification of such a motion.

It does **not** rule out:

- genuinely vertex-dependent coupled deformations not induced by one `PGL_2` element;
- matrix-valued or noncommutative cross-level transport that is not a scalar collision resultant;
- infinite cross-level limits whose convergence or renormalization creates new analytic structure rather than a finite product of collision factors;
- the nonlinear Fuchsian uniformization/monodromy sector of PC-017, where the projective connection is solved globally rather than obtained by applying one finite-dimensional Möbius map to a shell.

The surviving part of the PC-125 "nonuniform deformation" boundary is therefore narrower: a viable deformation must be genuinely **non-projective-global**. Merely replacing a common scaling by a common Möbius transformation does not create the analytic or spectral complexity required for RH.
