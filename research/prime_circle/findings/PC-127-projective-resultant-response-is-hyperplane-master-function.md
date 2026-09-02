# PC-127 — projective resultant response is a hyperplane master function

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` + `PRIOR-ART-REDIRECTION`.

PC-126 showed that the relative Möbius resultant of two finite primitive shells factors into pairwise collision hyperplanes. A natural attempted repair is not to use the resultant divisor itself, but to differentiate its logarithm and treat the resulting force, Hessian, curvature-like tensors, or finite response matrices as a richer nonlocal observable. That repair still does not escape the finite projective branch.

The reason is exact: the logarithm of the shell resultant is a unit-weight hyperplane-arrangement master function. Every finite differential response tensor is therefore a sum of independent collision-hyperplane tensors. Along every complexified one-parameter projective subgroup, all finite algebraic differential invariants are rational functions of one exponential variable in the semisimple case, or rational functions of the group parameter in the unipotent case. Their zero/pole counts remain at most linear in height and cannot reproduce the `T log T` Riemann-zero density.

## 1. Exact master-function form

Retain the notation of PC-126. For primitive shells `P_m^*` and `P_n^*`, write a projective matrix as

\[
g=\begin{pmatrix}a&b\\c&d\end{pmatrix}
\]

and define, for every ordered pair `(alpha,beta)`,

\[
L_{\alpha,\beta}(g)
:=
(a-c\beta)\alpha+(b-d\beta)
=
\alpha a+b-\alpha\beta c-\beta d.
\]

Then PC-126 gives

\[
\mathcal R_{m,n}(g)
=
\prod_{\alpha\in P_m^*}
\prod_{\beta\in P_n^*}
L_{\alpha,\beta}(g).
\]

On the complement of the collision arrangement choose any local branch

\[
\mathcal S_{m,n}(g):=\log\mathcal R_{m,n}(g).
\]

This is exactly the logarithm of a hyperplane-arrangement master function with all weights equal to one. Its logarithmic one-form is

\[
\boxed{
 d\mathcal S_{m,n}
 =
 \sum_{\alpha,\beta}
 \frac{dL_{\alpha,\beta}}{L_{\alpha,\beta}}.
}
\]

Because every `L_{alpha,beta}` is linear in `(a,b,c,d)`, all higher derivatives are explicit. For every `k>=1`,

\[
\boxed{
D^k\mathcal S_{m,n}
=
(-1)^{k-1}(k-1)!
\sum_{\alpha,\beta}
\frac{(dL_{\alpha,\beta})^{\otimes k}}
     {L_{\alpha,\beta}^{\,k}}.
}
\]

In particular the affine Hessian is

\[
\boxed{
D^2\mathcal S_{m,n}
=-
\sum_{\alpha,\beta}
\frac{dL_{\alpha,\beta}\otimes dL_{\alpha,\beta}}
     {L_{\alpha,\beta}^{\,2}}.
}
\]

Thus differentiating does not create pair-pair interactions: each response tensor is still an additive superposition of rank-one tensors attached to the original pairwise collision hyperplanes. The primitive-shell arithmetic enters only through the cyclotomic normals

\[
(\alpha,1,-\alpha\beta,-\beta).
\]

The common scalar rescaling of `g` is the expected projective gauge. Passing to any affine chart of `PGL_2` turns the same factors into affine-linear forms, so the master-function classification survives removal of that gauge.

## 2. Hessian, critical-set, and Gaudin language is classical arrangement theory

The preceding object sits directly inside classical hyperplane-arrangement master-function theory. Varchenko's work on critical points of products of powers of linear functions and the Schechtman-Varchenko/Aomoto framework treat precisely functions of the form

\[
\Phi=\prod_j f_j^{\lambda_j},
\qquad
 d\log\Phi=\sum_j\lambda_j\,d\log f_j.
\]

Modern arrangement literature studies the critical scheme of this logarithmic one-form, its Hessian, resonance, and the associated Gaudin/Bethe algebra. In particular:

- A. Varchenko, *Critical points of the product of powers of linear functions and families of bases of singular vectors*, Compositio Math. 97 (1995), 385–401, develops the critical-point/Hessian setting for products of powers of linear functions.
- A. Varchenko, *Bethe Ansatz for Arrangements of Hyperplanes and the Gaudin Model*, Moscow Math. J. 6 (2006), 195–210, arXiv:math/0408001, relates the Hessian of the logarithm of an arrangement master function to the Gaudin/Bethe construction.
- D. Cohen, G. Denham, M. Falk and A. Varchenko, *Vanishing products of one-forms and critical points of master functions*, arXiv:1010.3743, explicitly takes `Phi=prod f_i^{lambda_i}` and `omega=d log Phi` as the basic arrangement objects and studies their critical loci.

Therefore rebranding the PC-126 collision product as a Hessian, logarithmic force, critical-point system, or finite Gaudin-style master function does not by itself constitute a new prime-circle spectral mechanism. Any arithmetic significance would have to come from a further structure not already present in this finite weighted arrangement.

## 3. Semisimple one-parameter motions remain rational in one exponential

Let a nondegenerate complexified semisimple projective flow be conjugated to

\[
g(t)=h
\begin{pmatrix}e^{\lambda t}&0\\0&e^{-\lambda t}\end{pmatrix}
h^{-1},
\qquad \lambda\ne0.
\]

For each collision hyperplane PC-126 gives

\[
L_{\alpha,\beta}(g(t))
=A_{\alpha,\beta}e^{\lambda t}
+B_{\alpha,\beta}e^{-\lambda t}.
\]

Set

\[
y=e^{2\lambda t}.
\]

Then, with `N=varphi(m)varphi(n)`,

\[
\mathcal R_{m,n}(g(t))
=e^{-N\lambda t}P(y)
\]

for a polynomial `P` of degree at most `N`. Hence

\[
\frac{d}{dt}\log\mathcal R
=-N\lambda+2\lambda y\frac{P'(y)}{P(y)},
\]

and every derivative of order at least two is a rational function of `y`. More generally, any finite matrix assembled algebraically from finitely many such response tensors and their inverses where defined has entries rational in `y`; its determinants, traces, characteristic coefficients, finite curvature expressions, and similar algebraic differential invariants are again rational in `y`.

Consequently every non-identically-zero scalar invariant in this class has only finitely many zero or pole values `y_1,...,y_r`. Pulling them back to `t` gives finitely many logarithmic lattices

\[
\boxed{
 t=
 \frac{\Log y_j+2\pi i k}{2\lambda},
 \qquad k\in\mathbb Z.
}
\]

Thus in any fixed-width vertical strip,

\[
\boxed{N_I(T)=O(T).}
\]

Differentiation, Hessian formation, finite matrix inversion, and finite algebraic contraction can change the finite set of base values `y_j`, but cannot change the analytic type from a finite union of exponential pullbacks.

## 4. Unipotent motions are even more finite

For a complexified unipotent subgroup,

\[
g(t)=h
\begin{pmatrix}1&t\\0&1\end{pmatrix}
h^{-1},
\]

each collision factor is affine in `t`. Therefore the resultant is a finite polynomial in `t`, every logarithmic derivative is rational in `t`, and every finite algebraic differential invariant of the same class is rational in `t`.

Except for an identically zero invariant, it therefore has only finitely many finite zeros and poles. No repeated vertical zero lattice is present at all.

## 5. Zero-density obstruction for finite differential spectralization

The Riemann-von Mangoldt law is

\[
N_\zeta(T)
=
\frac{T}{2\pi}\log\frac{T}{2\pi}
-
\frac{T}{2\pi}
+O(\log T).
\]

The differential/projective response class above has at most `O(T)` zeros along a semisimple complexified flow and only finitely many along a unipotent flow. Therefore a finite response construction cannot acquire the Riemann zero density merely by passing from the collision determinant to its gradient, Hessian, critical equations, finite response matrices, or finite differential-geometric contractions.

This is stronger than PC-126's statement about the original resultant divisor. PC-126 left open the possibility that differentiation of the logarithm might expose a richer collective interaction even though the determinant itself was a simple product. The exact derivative formula shows that no such finite collective tensor is generated: all orders remain sums of powers of the original logarithmic hyperplane forms, and their one-parameter analytic continuation remains rational in one elementary group variable.

## 6. Falsification controls and boundary

The result is deliberately limited to **finite differential extraction from the PC-126 global-projective resultant**. It does not rule out:

- vertex-dependent deformations not induced by a single `PGL_2` element;
- an infinite cross-level limit whose convergence or renormalization creates a genuinely new analytic function;
- a noncommutative transport not algebraically generated from finitely many derivatives of `log R`;
- the nonlinear Fuchsian uniformization/monodromy branch of PC-017;
- an independently forced spectral parameter whose origin is not a reparameterization of the projective group variable.

It also does not claim that the cyclotomic collision arrangement has no interesting arrangement combinatorics. The point is narrower: **the standard differential enrichments of its finite master function remain classical finite-arrangement data and retain the same elementary one-parameter analytic complexity**.

Matched nonarithmetic finite point clouds obey the identical derivative formulas, with only the hyperplane normals changed. Thus primality does not enter the differential mechanism itself.

## 7. Research consequence

The global-projective resultant branch is now closed not only at the level of its divisor but under finite logarithmic differential response:

\[
\boxed{
\text{finite primitive shells}
\to
\text{global }PGL_2\text{ motion}
\to
\text{resultant/master function}
\to
\text{finite differential response}
\not\to
\text{new RH spectral divisor}.
}
\]

A viable continuation of the resultant/deformation idea must cross one of the explicit boundaries above. In particular, merely replacing the resultant by its Hessian, a force matrix, a finite master-function critical scheme, or a Gaudin-style wrapper is a prior-art redirection rather than progress toward the target RH mechanism.
