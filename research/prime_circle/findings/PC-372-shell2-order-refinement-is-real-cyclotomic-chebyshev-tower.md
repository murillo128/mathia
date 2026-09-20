# PC-372 — shell-2 order refinement is the real cyclotomic Chebyshev tower

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-IDENTITY` + `DECISIVE-NEGATIVE` for the most direct cross-shell/order repair left by PC-371. The shell-2 centered order cone is not merely representable by a finite Hausdorff moment measure: its complete polynomial is exactly an affine reciprocal form of the maximal-real cyclotomic polynomial. The source-native power/refinement map descends to the corresponding Chebyshev map, and the exact parent/child relation is precisely the maximal-real quotient of ordinary cyclotomic refinement. It can exclude generic irrational unit-circle controls, but only by detecting torsion/root-of-unity dynamics already contained in the cyclotomic/Bost--Connes tower.

This does **not** classify every cross-shell nonlinear or nonlocal operation on the PC-371 order measures. It closes the canonical operation obtained by coupling that order structure to the geometry's own power maps, including the full preimage polynomial relation, normalized measure transport, and finite moment intertwiners. Derivative-weighted transfer operators, source-forced interactions between different prime directions not reducible to these Chebyshev pullbacks, and other genuinely nonlocal cross-shell constructions remain outside the theorem.

## 1. The PC-371 cone is an affine reciprocal real-cyclotomic polynomial

For `n>2`, set

\[
q_n:=\frac{\varphi(n)}2
\]

and choose one representative from each conjugate pair of primitive `n`-th roots,

\[
zeta_{n,a}=e^{2\pi i a/n},
\qquad a\in (\mathbb Z/n\mathbb Z)^*/\{\pm1\}.
\]

PC-371 attaches to that pair the shell-2 order coordinate

\[
\lambda_{n,a}
:=\cos^2\!\frac{\pi a}{n}
=\frac{2+\zeta_{n,a}+\zeta_{n,a}^{-1}}4
\in(0,1).
\tag{1}
\]

Let

\[
\Lambda_n:=\{\lambda_{n,a}:a\in(\mathbb Z/n\mathbb Z)^*/\{\pm1\}\}
\]

and define its monic root polynomial

\[
R_n(\lambda):=\prod_{\alpha\in\Lambda_n}(\lambda-\alpha).
\tag{2}
\]

Let `Psi_n(X)` be the monic minimal polynomial of

\[
\zeta_n+\zeta_n^{-1}=2\cos\frac{2\pi}{n}.
\]

Its roots are exactly the conjugates

\[
2\cos\frac{2\pi a}{n},
\qquad a\in(\mathbb Z/n\mathbb Z)^*/\{\pm1\},
\]

so the affine change `X=4 lambda-2` gives the exact identity

\[
\boxed{
R_n(\lambda)=4^{-q_n}\Psi_n(4\lambda-2).
}
\tag{3}
\]

Thus `R_n` is simply the defining polynomial of the maximal real cyclotomic orbit, written in the PC-371 shell-2 coordinate.

Now recall the PC-371 variable

\[
y(r)=\frac{4r}{(1+r)^2}\in(0,1]
\]

and its exact factorization

\[
\exp W_n(r)=\prod_{\alpha\in\Lambda_n}(1-\alpha y(r)).
\tag{4}
\]

Equations (2)--(4) give

\[
\boxed{
\exp W_n(r)
=y(r)^{q_n}R_n\!\left(\frac1{y(r)}\right)
=\left(\frac{y(r)}4\right)^{q_n}
\Psi_n\!\left(\frac4{y(r)}-2\right).
}
\tag{5}
\]

So the complete centered order cone is not an independent new polynomial invariant sitting beside cyclotomy. It is a reciprocal affine presentation of the real cyclotomic polynomial itself. The moment sequence of PC-371 is its Newton data, and the finite atomic measure is its root measure.

The classical identity behind this is the usual maximal-real cyclotomic relation

\[
\Psi_n(z+z^{-1})=z^{-q_n}\Phi_n(z),
\tag{6}
\]

up to the conventional normalization of `Psi_n`. Equation (5) is the same relation after the shell-2 affine coordinate and reciprocal evaluation forced by the centered radial factorization.

## 2. Source refinement descends exactly to a Chebyshev map

The circle power map `z -> z^p` has a canonical action on (1). Define

\[
\boxed{
C_p(\lambda)
:=\frac{1+T_p(2\lambda-1)}2,
}
\tag{7}
\]

where `T_p` is the Chebyshev polynomial of the first kind. Since

\[
2\lambda(z)-1=\frac{z+z^{-1}}2=\cos\theta
\]

for `z=e^{i\theta}`, the defining identity `T_p(cos theta)=cos(p theta)` gives

\[
\boxed{
C_p(\lambda(z))=\lambda(z^p).
}
\tag{8}
\]

The polynomial `C_p` has degree `p` and leading coefficient `4^{p-1}`.

The exact root-order classification of a `p`-th preimage is elementary. If `u^p` has exact order `n`, then

\[
\operatorname{ord}(u)=
\begin{cases}
n\text{ or }pn,&p\nmid n,\\
pn,&p\mid n.
\end{cases}
\tag{9}
\]

After quotienting conjugate pairs, (9) becomes

\[
\boxed{
C_p^{-1}(\Lambda_n)=
\begin{cases}
\Lambda_n\sqcup\Lambda_{pn},&p\nmid n,\\
\Lambda_{pn},&p\mid n.
\end{cases}}
\tag{10}
\]

The union in the first line is disjoint. Comparing roots, degrees, and leading coefficients therefore gives the exact polynomial refinement law

\[
\boxed{
R_n(C_p(\lambda))
=4^{q_n(p-1)}R_{pn}(\lambda)
\begin{cases}
R_n(\lambda),&p\nmid n,\\
1,&p\mid n.
\end{cases}}
\tag{11}
\]

This is the maximal-real/Chebyshev form of the ordinary cyclotomic prime-child recursion. No new incidence tensor has appeared: the same power map has simply been pushed through the quotient

\[
z\sim z^{-1},
\qquad
\lambda=\frac{2+z+z^{-1}}4.
\tag{12}
\]

Equation (11) was checked symbolically for all `3 <= n <= 14` and `p in {2,3,5}` by independently constructing the minimal polynomial of `2 cos(2 pi/n)` and comparing both sides coefficient by coefficient. The identity itself follows exactly from (9), so the computation is only a falsification control.

## 3. The atomic order measures have only the inherited power-map transport

Let

\[
\nu_n:=\sum_{\alpha\in\Lambda_n}\delta_\alpha
\tag{13}
\]

be the PC-371 atomic order measure. The map from primitive `pn`-th roots to primitive `n`-th roots under `z -> z^p` is uniform. Its fiber size is

\[
\kappa_p(n):=\frac{\varphi(pn)}{\varphi(n)}
=
\begin{cases}
p-1,&p\nmid n,\\
p,&p\mid n.
\end{cases}
\tag{14}
\]

and quotienting by conjugation does not change that multiplicity. Therefore

\[
\boxed{
(C_p)_*\nu_{pn}=\kappa_p(n)\nu_n.
}
\tag{15}
\]

For the normalized probability measures

\[
\widehat\nu_n:=\frac{2}{\varphi(n)}\nu_n,
\]

this becomes simply

\[
\boxed{(C_p)_*\widehat\nu_{pn}=\widehat\nu_n.}
\tag{16}
\]

Consequently every polynomial moment intertwines through the same Chebyshev map:

\[
\boxed{
\int C_p(\lambda)^m\,d\nu_{pn}(\lambda)
=\kappa_p(n)M_m(n),
}
\tag{17}
\]

where `M_m(n)` is the Ramanujan/binomial moment of PC-371. Because `C_p(lambda)^m` is a finite polynomial in `lambda`, (17) is only a finite linear relation among the existing PC-371 moments. It supplies no new continuous spectral parameter or independent analytic carrier.

Equations (10), (11), and (15) retain more information than the scalar prime-child identity of PC-370: they act on the complete positive order measure and its full root polynomial. Nevertheless they remain the conjugation quotient of the same cyclotomic power-map dynamics.

## 4. Why this beats the generic one-shell control but still does not create new arithmetic

PC-371 showed that at one shell an arbitrary finite conjugation-stable set on the unit circle can reproduce the entire positivity/absolute-monotonicity cone: choose arbitrary angles and use their values `lambda=cos^2(theta/2)`. The immediate surviving proposal was therefore to combine that order structure with a **source-forced cross-shell operation** that a generic configuration cannot reproduce.

The exact old-branch relation in (10) does indeed reject a generic irrational configuration. Suppose a finite set `A subset [0,1]` satisfies the source-like old-set condition

\[
A\subseteq C_p^{-1}(A),
\qquad\text{equivalently }C_p(A)\subseteq A.
\tag{18}
\]

For every `lambda in A`, finiteness forces two iterates to agree,

\[
C_p^r(\lambda)=C_p^s(\lambda),
\qquad r>s\ge0.
\]

Lift `lambda=(1+cos theta)/2`. Then

\[
\cos(p^r\theta)=\cos(p^s\theta),
\]

so

\[
(p^r-p^s)\theta\in2\pi\mathbb Z
\quad\text{or}\quad
(p^r+p^s)\theta\in2\pi\mathbb Z.
\tag{19}
\]

Hence `theta/(2 pi)` is rational and the lift is a root of unity. Thus the cross-shell condition distinguishes the source from the generic PC-371 control **exactly by forcing torsion/preperiodic power-map dynamics**.

That is a genuine matched-control improvement, but not a new RH-relevant structure. Finite Chebyshev-preperiodic sets on this quotient are just the images of finite root-of-unity power orbits. Once the exact-order shell labels and all positive-integer power maps are restored, this is the same cyclotomic tower already classified in PC-010, with complex conjugation/inversion quotiented out. Arbitrary torsion unions provide matched non-prime-shell controls for the dynamical property itself; selecting precisely the primitive `n`-orbit is ordinary cyclotomic exact-order data.

So the route

\[
\text{PC-371 positive order cone}
\longrightarrow
\text{source power-map refinement}
\longrightarrow
\text{generic-control discriminator}
\]

works only up to the statement "these points are torsion and organized by exact order." That statement is classical cyclotomy, not a new spectral mechanism.

## 5. Relation to the Bost--Connes boundary and to zeta

PC-010 already proves that retaining roots of unity, their exact birth/order labels, divisibility inclusions, and the power maps `z -> z^k` gives the classical cyclotomic/Bost--Connes tower. The new observation here is that the seemingly more geometric PC-371 order carrier does not evade that boundary when coupled to its canonical refinement: both its complete polynomial (5) and its dynamics (8)--(16) factor through the inversion-fixed/maximal-real quotient of the same tower.

In algebraic terms, the order coordinate is already the inversion-invariant element

\[
\lambda(z)=\frac{2+z+z^{-1}}4
\tag{20}
\]

of the cyclotomic group algebra, and `C_p` is simply the image of the semigroup action `z -> z^p` on that invariant coordinate. The field generated by one primitive shell is the maximal real cyclotomic subfield

\[
\mathbb Q(\zeta_n+\zeta_n^{-1}).
\tag{21}
\]

Therefore a determinant, resultant, finite transfer matrix, or normalized measure transport built only from `R_n`, `C_p`, and the exact maps (10)--(17) can at most repackage this real cyclotomic quotient. The known Bost--Connes appearance of `zeta` as a partition function, or the `1/zeta` shell Dirichlet carrier already visible in PC-371, is inherited arithmetic. It does not by itself produce a new functional equation, gamma factor, critical-line selector, or Hilbert--Polya operator.

This conclusion is intentionally scoped. A derivative-weighted Perron--Frobenius operator, a coupling between several prime directions with additional geometry-dependent weights, or a nonlocal cross-shell kernel can contain more than the unweighted quotient dynamics proved here. Such an operator would need its weights and domain to be forced independently by Prime-Circle geometry and then pass a fresh matched-control and prior-art audit.

## 6. Prior-art and novelty audit

The key algebraic ingredients are classical. The relation between `Phi_n(z)` and the minimal polynomial of `zeta_n+zeta_n^{-1}` is standard maximal-real cyclotomic theory; Washington's *Introduction to Cyclotomic Fields*, already anchored in `SOURCES.md`, provides the general cyclotomic-field setting. D. H. Lehmer's 1933 note *A Note on Trigonometric Algebraic Numbers*, *American Mathematical Monthly* 40:3, 165--166, gives the classical trigonometric/cyclotomic relation (DOI `10.2307/2301023`). Modern literature on minimal polynomials of `cos(2 pi/n)` and Chebyshev factorization, for example Y. Z. Gurtas, *Chebyshev Polynomials and the Minimal Polynomial of cos(2 pi/n)*, *American Mathematical Monthly* 124:1 (2017), 74--78, DOI `10.4169/amer.math.monthly.124.1.74`, explicitly places these cosine polynomials inside standard Chebyshev/cyclotomic algebra. Yamagishi's work on Chebyshev resultants and modified cyclotomic polynomials supplies a nearby resultant-level boundary.

No theorem-level historical novelty is claimed for (3), (7), or the root-order decomposition behind (10). The durable project-local contribution is the exact **boundary classification after PC-371**: the first canonical way to combine its genuinely positive order cone with cross-shell source refinement does break the arbitrary irrational one-shell control, but only because the order cone is the real cyclotomic polynomial and its refinement is the Chebyshev image of the classical power-map tower. Thus this natural repair lands directly back on the prior-art surface that the research mandate requires us to exclude as progress by itself.

The directed prior-art check also searched for a distinct RH mechanism attached specifically to these maximal-real shell polynomials and their Chebyshev refinement. The nearby literature concerns cyclotomic/minimal-polynomial factorizations, Chebyshev resultants, and the already-established cyclotomic/Bost--Connes dynamics. Nothing found turns the exact relation above into an independent critical-line mechanism. More importantly, the negative conclusion does not rest on absence of literature: equations (3), (8), and (11) explicitly factor the candidate through classical cyclotomic data.

## 7. Falsification tests and surviving frontier

The classification has direct tests.

1. Construct `Psi_n` independently as the minimal polynomial of `2 cos(2 pi/n)` and verify (3) and (5) against the PC-371 root product.
2. Verify `C_p(lambda(z))=lambda(z^p)` from the Chebyshev identity and check that its leading coefficient is `4^(p-1)`.
3. Enumerate exact root orders in a `p`-th preimage and verify (10), including the parity-sensitive control `p=2`, odd `n`, where the two branches are `Lambda_n` and `Lambda_{2n}` rather than a duplicated shell.
4. Compare both sides of (11) coefficient by coefficient. Symbolic checks for `3<=n<=14` and `p=2,3,5` pass exactly.
5. Push the uniform primitive-pair measure through `C_p` and verify the multiplicities (14)--(16).
6. For an arbitrary irrational finite angle set, the one-shell cone still satisfies PC-371 positivity, but the old-branch invariance (18) must fail. Conversely, any finite set satisfying (18) must lift to torsion by (19).

A falsifier would be a non-torsion finite support satisfying the exact source old-branch Chebyshev invariance, a failure of the polynomial factorization (11), or a source-native refinement observable built from the PC-371 order data that provably does not factor through the power-map/conjugation quotient described above.

The surviving frontier is therefore sharper. **Order/positivity plus canonical power refinement is not enough.** A viable next step must add a cross-shell or nonlocal datum that is not determined by the real cyclotomic polynomial and its Chebyshev semigroup action: for example geometry-forced weights coupling several preimage branches, an interaction that compares distinct prime directions before they collapse to the common power semigroup, or a genuinely two-dimensional operator whose matrix elements retain information absent from the maximal-real quotient. Such a candidate must still beat matched torsion controls and the Bost--Connes/cyclotomic prior-art boundary before it can count as RH-relevant progress.
