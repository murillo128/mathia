# PC-202 — finite multi-output Haar fusion is colored rational-cone Dirichlet data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for using any fixed finite scalar same-angle Haar fusion of the source-native Prime-Circle Cauchy–Poisson packets, with any finite number of holomorphic and antiholomorphic legs, as a new RH/GRH carrier.

PC-201 classified every fixed finite Haar fusion with one antiholomorphic output: angular momentum conservation leaves an additive cone and the independent radial Mellin transform is exactly Mordell–Tornheim multiple `L`-data. Its explicit surviving boundary was to allow several antiholomorphic legs, where the selection law becomes a genuinely balanced relation rather than one output equaling the sum of all inputs.

That boundary can also be closed. For arbitrary fixed finite numbers `r,q >= 1` of holomorphic and antiholomorphic source-native packets, scalar Haar contraction imposes exactly

\[
k_1+\cdots+k_r=\ell_1+\cdots+\ell_q.
\]

After independent Mellin transforms, the surviving lattice is the positive integral part of one pointed rational polyhedral cone. Finite rational-cone subdivision then expresses the result as a finite combination of colored rational-cone multiple Dirichlet series: after a simplicial/unimodular subdivision, every denominator is a positive affine integral linear form in independent cone coordinates, while all Dirichlet-character or Ramanujan coefficients are finite periodic colors. Thus several output legs do preserve more multi-index information than PC-201, but a **fixed finite scalar Haar contraction still does not leave the classical cyclotomic/conical multiple-zeta/Dirichlet-series architecture**.

The first genuinely new case `r=q=2` can be decomposed explicitly into two three-dimensional chambers, so the classification does not rely only on abstract cone language. No source-derived Euler product, self-adjoint spectral problem, critical-line involution, or Weil-type positivity principle appears.

## 1. Arbitrary finite holomorphic/antiholomorphic packet fusion

For a primitive nonprincipal Dirichlet character `chi` modulo `n`, use the PC-197 angular packet

\[
\mathcal K_{n,\chi}(x,\theta)
=
2\tau(\overline\chi)
\sum_{k\ge1}\chi(k)e^{-kx}e^{ik\theta},
\qquad x>0.
\tag{1}
\]

Choose primitive nonprincipal characters

\[
\chi_i\pmod{n_i},\quad i=1,\ldots,r,
\qquad
\psi_j\pmod{m_j},\quad j=1,\ldots,q,
\]

and positive depths `x_i,y_j`. Define the scalar same-angle Haar invariant

\[
\boxed{
\mathcal T_{r,q}(\mathbf x;\mathbf y)
:=
\frac1{2\pi}\int_0^{2\pi}
\prod_{i=1}^{r}\mathcal K_{n_i,\chi_i}(x_i,\theta)
\prod_{j=1}^{q}\overline{\mathcal K_{m_j,\psi_j}(y_j,\theta)}
\,d\theta.
}
\tag{2}
\]

The conjugate packets are

\[
\overline{\mathcal K_{m_j,\psi_j}(y_j,\theta)}
=
2\overline{\tau(\overline\psi_j)}
\sum_{\ell_j\ge1}\overline{\psi_j(\ell_j)}e^{-\ell_jy_j}e^{-i\ell_j\theta}.
\tag{3}
\]

At positive depths all series converge absolutely, so multiplication and termwise Haar integration are justified.

## 2. Haar orthogonality leaves one rational-cone balance law

Substitution of (1) and (3) into (2) gives the angular factor

\[
\frac1{2\pi}\int_0^{2\pi}
\exp\!\left(i\theta\left[\sum_{i=1}^r k_i-\sum_{j=1}^q\ell_j\right]\right)d\theta
=
\mathbf 1_{\sum_i k_i=\sum_j\ell_j}.
\tag{4}
\]

Therefore

\[
\boxed{
\begin{aligned}
\mathcal T_{r,q}(\mathbf x;\mathbf y)
&=C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\
\sum_i k_i=\sum_j\ell_j}}
\left(\prod_{i=1}^r\chi_i(k_i)\right)
\left(\prod_{j=1}^q\overline{\psi_j(\ell_j)}\right)\\
&\qquad\times
\exp\!\left(-\sum_i k_ix_i-\sum_j\ell_jy_j\right),
\end{aligned}}
\tag{5}
\]

with the nonzero Gauss normalization

\[
C_{\boldsymbol\chi,\boldsymbol\psi}
=2^{r+q}
\prod_{i=1}^r\tau(\overline\chi_i)
\prod_{j=1}^q\overline{\tau(\overline\psi_j)}.
\tag{6}
\]

The support is the positive integral lattice of

\[
\boxed{
C_{r,q}
=
\left\{(\mathbf k,\boldsymbol\ell)\in\mathbb R_{>0}^{r+q}:
\sum_i k_i=\sum_j\ell_j\right\}.
}
\tag{7}
\]

Its closure is a pointed rational polyhedral cone of dimension `r+q-1`. Thus multiple outputs genuinely enlarge the PC-201 support: for `q>1` no distinguished frequency is forced to equal the sum of all remaining ones. But the enlargement is still finite-dimensional, rational, and completely source-forced by one linear Haar conservation law.

## 3. Independent radial Mellin transforms give a colored cone Dirichlet series

Mellin-transform every depth independently. In the safe region

\[
\Re s_i>1,\qquad \Re t_j>1,
\]

absolute convergence is immediate by bounding the constrained sum by the unconstrained product. Termwise integration gives

\[
\int_0^\infty x_i^{s_i-1}e^{-k_ix_i}\,dx_i
=\Gamma(s_i)k_i^{-s_i},
\qquad
\int_0^\infty y_j^{t_j-1}e^{-\ell_jy_j}\,dy_j
=\Gamma(t_j)\ell_j^{-t_j}.
\tag{8}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal M\mathcal T_{r,q}(\mathbf s;\mathbf t)
&=C_{\boldsymbol\chi,\boldsymbol\psi}
\prod_i\Gamma(s_i)\prod_j\Gamma(t_j)\\
&\quad\times
Z_{r,q}(\mathbf s;\mathbf t;
\boldsymbol\chi,\boldsymbol\psi),
\end{aligned}}
\tag{9}
\]

where

\[
\boxed{
Z_{r,q}
:=
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\
\sum_i k_i=\sum_j\ell_j}}
\frac{
\prod_i\chi_i(k_i)
\prod_j\overline{\psi_j(\ell_j)}
}
{
\prod_i k_i^{s_i}
\prod_j\ell_j^{t_j}
}.
}
\tag{10}
\]

Equation (10) is the complete scalar analytic datum produced by the finite multi-output fusion. The remaining question is whether the balanced support makes (10) a new analytic species. It does not.

## 4. Rational-cone subdivision classicalizes every fixed finite `r,q`

Because the closure of `C_{r,q}` is a pointed rational polyhedral cone, it has a finite rational simplicial subdivision; a rational simplicial cone can in turn be subdivided into smooth/unimodular cones. Boundary faces can be assigned by a half-open convention or handled by finite inclusion-exclusion. This is standard rational-cone geometry and is exactly the subdivision setting used in the conical-zeta literature.

On one resulting smooth cone choose independent semigroup coordinates `u_1,...,u_d >= 0`, with `d <= r+q-1`, together with the finite translation data required to account for the positive lattice and any fundamental parallelepiped. Every original coordinate then has the form

\[
k_i=L_i(\mathbf u)+a_i,
\qquad
\ell_j=M_j(\mathbf u)+b_j,
\tag{11}
\]

with nonnegative integral linear forms `L_i,M_j` and fixed rational/integral shifts after clearing a finite common denominator. On the relevant relative interior these affine forms are positive.

The coefficient

\[
\prod_i\chi_i(L_i(\mathbf u)+a_i)
\prod_j\overline{\psi_j(M_j(\mathbf u)+b_j)}
\tag{12}
\]

is periodic in the finitely many integer variables `u_a`. Any such periodic function has a finite discrete Fourier expansion into products of roots-of-unity colors. Consequently each cone piece of (10) is a finite linear combination of series of the form

\[
\boxed{
\sum_{\mathbf u\in\mathbb Z_{\ge0}^{d}}
\frac{\omega_1^{u_1}\cdots\omega_d^{u_d}}
{
\prod_i(L_i(\mathbf u)+a_i)^{s_i}
\prod_j(M_j(\mathbf u)+b_j)^{t_j}
},
}
\tag{13}
\]

where all `omega_a` are roots of unity forced by the conductors.

Thus for arbitrary complex Mellin exponents in an absolute-convergence region, the exact output is a **finite colored rational-cone multiple Dirichlet/Lerch-type series with products of affine linear forms**. At convergent positive-integer exponents this specializes to the cyclotomic conical-zeta-value framework. No claim is needed that every complex-variable member of (13) is literally one named special function; the decisive point is that finite Haar fusion has reduced the Prime-Circle geometry to the established finite rational-cone/periodic-coefficient apparatus rather than generating a new source-specific spectral object.

## 5. The first new case `r=q=2` is already two explicit classical chambers

The balanced law is

\[
k_1+k_2=\ell_1+\ell_2.
\tag{14}
\]

It admits a direct disjoint chamber decomposition.

If `ell_1 <= k_1`, put

\[
a=\ell_1\ge1,
\qquad b=k_1-\ell_1\ge0,
\qquad c=k_2\ge1.
\]

Then

\[
k_1=a+b,
\qquad k_2=c,
\qquad \ell_1=a,
\qquad \ell_2=b+c,
\]

and the denominator is

\[
(a+b)^{s_1}c^{s_2}a^{t_1}(b+c)^{t_2}.
\tag{15}
\]

If `ell_1 > k_1`, put

\[
a=k_1\ge1,
\qquad b=\ell_1-k_1\ge1,
\qquad c=\ell_2\ge1.
\]

Then

\[
k_1=a,
\qquad k_2=b+c,
\qquad \ell_1=a+b,
\qquad \ell_2=c,
\]

and the denominator is

\[
a^{s_1}(b+c)^{s_2}(a+b)^{t_1}c^{t_2}.
\tag{16}
\]

The corresponding character numerators are periodic functions of `(a,b,c)` and therefore finite Fourier sums of root-of-unity colors. So the first case left open by PC-201 is already a finite sum of three-variable colored product-of-linear-form Dirichlet series. The `b=0` face in the first chamber is simply a lower-dimensional cone contribution, not a new analytic sector.

Two limiting checks recover earlier findings exactly. For `q=1`, eliminating the unique output frequency gives PC-201's Mordell–Tornheim hierarchy. For `r=q=1`, (10) becomes

\[
\sum_{k\ge1}
\frac{\chi_1(k)\overline{\psi_1(k)}}{k^{s_1+t_1}},
\tag{17}
\]

namely the one product-character Dirichlet packet already isolated by PC-199.

## 6. Principal modes and composite-conductor controls

Centered principal packets do not escape the cone class. PC-197 writes their positive Fourier coefficients as Ramanujan sums `c_n(k)`. Since every Ramanujan sum is periodic, replacing any character coefficient in (10) by `c_n` only replaces (12) by another finite periodic function on the cone lattice. Its discrete Fourier expansion again yields finitely many roots-of-unity colors in (13).

Primality is likewise unused in the derivation. Primitive characters of composite conductors obey the same Gauss expansion (1), the same Haar balance (4), and the same cone decomposition. The analytic species therefore survives unchanged under matched composite-conductor controls. Prime levels merely make all nonprincipal multiplicative characters primitive.

These controls matter for the mandate: the balanced cone is a real geometric consequence of scalar angular fusion, but it is not a discriminator of rational-prime birth layers.

## 7. Prior-art and novelty audit

The cone mechanism itself is classical. Tomohide Terasoma, **Rational convex cones and cyclotomic multiple zeta values**, arXiv `math/0410306` (2004), develops zeta values attached to rational convex cones with finite-order/cyclotomic data and relates them to cyclotomic multiple zeta values. Li Guo, Sylvie Paycha and Bin Zhang, **Conical zeta values and their double subdivision relations**, *Advances in Mathematics* 252 (2014), 343–381, DOI `10.1016/j.aim.2013.10.022`, explicitly develops rational-cone subdivisions and conical zeta values. Both references are already anchored in `research/prime_circle/SOURCES.md`.

This prior art is sufficient for the structural novelty decision: the finite polyhedral subdivision and cyclotomic coloring used in Section 4 are not new mathematical mechanisms. PC-201 already anchored the more special Mordell–Tornheim `L`-function literature reached when `q=1`. A directed search for balanced multi-index multiple Dirichlet series also reaches broader conical/root-system/Weyl-group multiple-series literatures rather than identifying a Prime-Circle-specific analytic family. The latter comparison is only a novelty warning: Weyl-group multiple Dirichlet series have additional arithmetic coefficients and functional-equation symmetries that are **not** produced by (10), so they are not being claimed as an exact identification here.

No theorem-level novelty is claimed for rational-cone subdivision, conical zeta values, cyclotomic colors, or their analytic continuations. The durable Mathia-specific result is the exact closure statement: **the several-output scalar Haar boundary left open by PC-201 still remains inside finite classical cone-series algebra.**

## 8. RH and critical-line audit

The balanced constraint in (10) is genuinely nonlocal in the Fourier indices and retains `r+q-1` independent directions. That is more information than any scalar evaluation or one-ray collapse. But after scalar contraction its analytic content is still a finite cone series with periodic coefficients.

Nothing in (4), (7), or (13) forces an Euler product over rational primes, a source-native self-adjoint operator whose spectral determinant has the zeta zeros, a functional equation matching the completed Riemann zeta function, or an involution selecting `Re(s)=1/2`. Cone subdivision creates algebraic relations among equivalent presentations; it does not supply a zero-confinement principle. Any special values or functional relations inherited from known conical/multiple-zeta theory therefore cannot be counted as a new RH mechanism merely because the cone arose from roots-of-unity packets.

This also prevents an arbitrary spectral wrapper: one could package (10) into matrices or determinants after the fact, but unless the matrix indices are retained by a source-forced operator **before** scalar Haar contraction, such packaging adds structure rather than deriving it.

## 9. Boundary of the result

The exact closed route is

\[
\boxed{
\text{fixed finite PC-197 packet legs}
\xrightarrow{\text{scalar same-angle Haar}}
C_{r,q}\cap\mathbb Z_{>0}^{r+q}
\xrightarrow{\text{independent radial Mellin}}
\text{finite colored rational-cone Dirichlet data}.
}
\tag{18}
\]

PC-202 therefore closes the finite multi-output scalar extension explicitly left open by PC-201. Together they show that increasing finite scalar valence on either side of the Haar contraction can enlarge the surviving Fourier cone without escaping established finite conical packet algebra.

The result **does not** classify matrix/operator-valued couplings that retain the cone indices as degrees of freedom before contraction, shell-dependent non-Haar kernels forced by old/new chord geometry, source-forced infinite refinement limits, non-scalar positivity constructions, nonlinear cocycles that are not reducible to a fixed finite periodic cone sum, or the global uniformization/monodromy branch. Those remain structurally distinct and are the relevant surviving directions.

## Audit / falsification tests

The finding has five direct failure points.

1. Expanding (2) at positive depths must impose exactly the balance law (4), with no additional hidden Fourier constraint.
2. Independent Mellin transformation must give exactly (10) after removing the nonzero Gauss and gamma factors.
3. The `r=q=2` balanced lattice must be exhausted without overlap by the two chambers in Section 5, apart from their explicitly assigned boundary.
4. A finite rational simplicial/smooth subdivision of `C_{r,q}` must convert every original coordinate and periodic coefficient into the affine-linear/finite-color form (13). A genuinely nonperiodic residual coefficient would invalidate the classicalization.
5. Replacing prime conductors by composite conductors supporting primitive characters must leave the balance law and cone species unchanged. A prime-only residual term would expose missing arithmetic structure.

All five tests are independent of RH or GRH.