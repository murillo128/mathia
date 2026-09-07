# PC-208 — zero-depth Hardy singularity is the primitive shell, not a discrete spectrum

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the singular zero-depth escape explicitly left open by PC-207, restricted to the canonical fixed-finite-valence Fourier-leg Hardy lift.

PC-207 classified every fixed finite collection of positive-depth character legs as a separated tensor product of bounded rational Hardy multipliers, but deliberately left the limit `x -> 0+` open because the poles move onto the unit circle and the bounded-operator argument breaks down. In the source-native zero-depth limit, that singularity can be classified exactly. For a primitive nonprincipal Dirichlet character, the limiting one-leg symbol is a rational Smirnov-class multiplier whose denominator is precisely the cyclotomic polynomial of the primitive shell. Its boundary poles carry only the classical finite Fourier transform/Gauss-sum phases of the character. The corresponding maximal Hardy multiplication operator is closed and densely defined, but its adjoint has a reproducing-kernel eigenvector for every point of an open subset of the complex plane, so its spectrum is intrinsically continuous and cannot have compact resolvent. The obvious bounded scalar renormalization collapses strongly to zero, while the first nontrivial quadratic boundary renormalization recovers only the primitive-root point measure.

Thus the singularity which appears when the damping is removed is real and geometrically exact, but in this canonical lift it is **the original primitive shell reappearing as a classical cyclotomic boundary pole set**, not a new discrete spectral carrier. Any surviving zero-depth mechanism must introduce a nonseparable renormalization/coupling, growing valence, shell-dependent transfer, or another source-forced operation before the separated multiplier reduction.

## 1. Zero depth cancels every nonprimitive root exactly

Let `chi` be a primitive nonprincipal Dirichlet character modulo `n`, extended by zero on nonunits. For `x>0`, PC-207 used

\[
B_{\chi,x}(z)
=
\sum_{k\ge1}\chi(k)e^{-xk}z^k
=
\frac{P_\chi(e^{-x}z)}{1-e^{-nx}z^n},
\qquad
P_\chi(w)=\sum_{a=1}^{n}\chi(a)w^a.
\tag{1}
\]

For every compact subset of the open unit disk, `B_{chi,x}` converges locally uniformly as `x -> 0+` to

\[
b_\chi(z)
:=
\sum_{k\ge1}\chi(k)z^k
=
\frac{P_\chi(z)}{1-z^n}.
\tag{2}
\]

Let `zeta_n=e^{2 pi i/n}` and define the usual Gauss sum

\[
\tau(\chi)=\sum_{a=1}^{n}\chi(a)\zeta_n^a.
\]

The classical finite Fourier transform of a primitive character gives, for every integer `r`,

\[
\boxed{
P_\chi(\zeta_n^r)
=
\overline{\chi(r)}\,\tau(\chi),
}
\tag{3}
\]

where the right-hand side is zero when `(r,n)>1`. Hence `P_chi` vanishes at every nonprimitive `n`-th root of unity, including `1`. Since all roots of `z^n-1` are simple,

\[
D_n(z):=\frac{z^n-1}{\Phi_n(z)}
\quad\text{divides}\quad
P_\chi(z).
\tag{4}
\]

Writing `P_chi=D_n R_chi` therefore gives the exact reduced form

\[
\boxed{
b_\chi(z)=-\frac{R_\chi(z)}{\Phi_n(z)},
\qquad
\deg R_\chi<\varphi(n).
}
\tag{5}
\]

This is a sharper description than merely saying that periodic coefficients give a rational function. **After all removable boundary singularities are cancelled, the denominator is exactly the cyclotomic polynomial whose zeros are the primitive/new-vertex shell.**

At a primitive root `omega=zeta_n^r`, equation (3) and the derivative of `1-z^n` give

\[
\boxed{
\operatorname*{Res}_{z=\omega} b_\chi(z)
=-\frac{\omega}{n}\,
\tau(\chi)\overline{\chi(r)}.
}
\tag{6}
\]

For primitive `chi`, `|tau(chi)|=sqrt(n)`. Thus every primitive-shell pole has the same residue magnitude `n^{-1/2}`; the only pointwise arithmetic decoration is the classical character/Gauss phase.

## 2. The canonical zero-depth operator is a classical unbounded analytic multiplier

Because `Phi_n` has no zeros in the open disk and all its zeros lie on the unit circle, it is an outer polynomial in `H^infinity`. Equation (5) places `b_chi` in the Smirnov class `N+`. Define the maximal multiplication operator

\[
M_{b_\chi}f=b_\chi f,
\qquad
\mathcal D(M_{b_\chi})
=
\{f\in H^2:\ b_\chi f\in H^2\}.
\tag{7}
\]

Its domain is dense: equation (5) implies

\[
\Phi_n H^2\subset \mathcal D(M_{b_\chi}),
\tag{8}
\]

and multiplication by the outer function `Phi_n` has dense range in `H^2`.

The operator is closed without any extra regularization. If `f_j -> f` and `b_chi f_j -> g` in `H^2`, bounded point evaluation inside the disk gives

\[
g(w)=b_\chi(w)f(w)
\qquad(w\in\mathbb D),
\]

so `f` belongs to the maximal domain and `g=M_{b_chi}f`.

This is exactly the classical unbounded analytic Toeplitz/Smirnov setting studied systematically by Donald Sarason, **Unbounded Toeplitz operators**, *Integral Equations and Operator Theory* 61 (2008), 281--298, DOI `10.1007/s00020-008-1588-3`. No new operator class is created by moving the periodic Hardy poles onto the boundary.

## 3. Reproducing kernels force a spectral continuum

Let

\[
k_w(z)=\frac{1}{1-\overline w z}
\]

be the Hardy reproducing kernel. For every `w in D` and every `f` in the maximal domain,

\[
\langle M_{b_\chi}f,k_w\rangle
=b_\chi(w)f(w).
\]

Therefore `k_w` lies in the domain of the adjoint and

\[
\boxed{
M_{b_\chi}^*k_w
=
\overline{b_\chi(w)}k_w.
}
\tag{9}
\]

Consequently

\[
\boxed{
b_\chi(\mathbb D)
\subset
\operatorname{Spec}(M_{b_\chi}).
}
\tag{10}
\]

Indeed, if `lambda=b_chi(w)`, then `M_{b_chi}-lambda I` has nondense range because its adjoint has the nonzero kernel vector `k_w`. Since `b_chi` is nonconstant, the open mapping theorem makes `b_chi(D)` a nonempty open subset of `C`. The spectrum of the canonical zero-depth operator therefore has interior; it is not a discrete divisor. In particular this operator cannot have compact resolvent. If its resolvent set is nonempty, compact resolvent would force a discrete spectrum of finite-multiplicity eigenvalues with no finite accumulation; if the resolvent set were empty, the compact-resolvent requirement already fails.

This rules out a Hilbert--Polya interpretation of the **canonical separated zero-depth multiplication operator** itself. The boundary poles are arithmetically placed, but the interior Hardy state immediately fills an open spectral continuum.

## 4. The natural bounded scalar renormalization converges strongly to zero

One might try to retain only the boundary blow-up by multiplying the positive-depth bounded operators by the pole distance `x`. This does not produce a nonzero bounded operator limit.

For `|z|<=1`, the defining series gives the uniform estimate

\[
|xB_{\chi,x}(z)|
\le
x\sum_{k\ge1}e^{-xk}
=
\frac{x}{e^x-1}
\le1.
\tag{11}
\]

For almost every boundary point `e^{i theta}` -- all except the finite set of `n`-th roots -- equation (1) has a finite zero-depth boundary limit, hence

\[
xB_{\chi,x}(e^{i\theta})\to0.
\]

Dominated convergence on boundary values then yields, for every `f in H^2`,

\[
\boxed{
xM_{B_{\chi,x}}f\longrightarrow0
\quad\text{in }H^2.
}
\tag{12}
\]

Thus the simplest normalization that keeps the diverging bounded multipliers uniformly controlled converges **strongly to the zero operator**. It does not expose a hidden finite spectral operator.

## 5. Quadratic boundary scaling recovers exactly the primitive-shell measure

Although the linear bounded normalization vanishes strongly, the concentrated boundary energy has a nonzero distributional limit. Near a primitive root `omega=zeta_n^r`, write `e^{i theta}=omega e^{it}`. Equations (1) and (3) give

\[
1-e^{-nx}e^{int}
=n(x-it)+O(x^2+t^2),
\]

and

\[
P_\chi(e^{-x}\omega e^{it})
=\tau(\chi)\overline{\chi(r)}+O(x+|t|).
\]

Using `|tau(chi)|^2=n`, the local profile is

\[
|B_{\chi,x}(\omega e^{it})|^2
=\frac{1}{n(x^2+t^2)}+O\!\left(\frac{1}{x+|t|}\right)
\]

at the scale responsible for the mass. Therefore, for normalized Haar measure `dm(theta)=dtheta/(2 pi)`,

\[
\boxed{
x|B_{\chi,x}(e^{i\theta})|^2dm(\theta)
\overset{*}{\longrightarrow}
\frac{1}{2n}
\sum_{\substack{r\bmod n\\(r,n)=1}}
\delta_{2\pi r/n}.
}
\tag{13}
\]

The total mass check is exact from coefficients:

\[
\lim_{x\downarrow0}
 x\|B_{\chi,x}\|_{H^2}^2
=
\lim_{x\downarrow0}
 x\sum_{k\ge1}|\chi(k)|^2e^{-2xk}
=
\frac{\varphi(n)}{2n},
\tag{14}
\]

matching the total mass on the right of (13).

So the first natural nonlinear boundary observable does survive, but it recovers **only the uniform point measure on the primitive/new-vertex shell**. The character phases disappear after taking modulus squared. Cross-character quadratic forms retain the corresponding finite Gauss/character phases, again classical finite Fourier data rather than a new zeta-zero carrier.

## 6. Fixed finite valence remains separated at zero depth

For finitely many primitive character legs, the zero-depth PC-207 symbol is

\[
F(z_1,\ldots,z_d)
=C\prod_{a=1}^{d}b_{\chi_a}(z_a)
=(-1)^d C
\prod_{a=1}^{d}
\frac{R_{\chi_a}(z_a)}{\Phi_{n_a}(z_a)}.
\tag{15}
\]

Its polar divisor is the union of the coordinate primitive-shell divisors `Phi_{n_a}(z_a)=0`. There is no mixed denominator and no source-forced cross-coordinate residue. The maximal multiplication operator on `H^2(D^d)` is densely defined because its domain contains

\[
\left(\prod_a\Phi_{n_a}(z_a)\right)H^2(\mathbb D^d),
\]

whose range is dense by the tensor product of the one-variable outer ranges. Reproducing kernels again satisfy

\[
M_F^*k_w=\overline{F(w)}k_w,
\]

and fixing all but one nonzero coordinate factor shows that the spectrum contains a nonempty open continuum. Distinct coordinate multipliers still commute on their natural common core.

Hence taking the source-native singular limit **before** the bounded multiplier reduction changes boundedness and domain theory but not the separability that was the decisive obstruction in PC-207.

## 7. Prior-art and novelty audit

Every abstract ingredient is classical.

The periodic generating function (2) is elementary. Equation (3) is the standard finite Fourier transform/Gauss-sum identity for a primitive Dirichlet character; it is the same classical Gauss-sum package that enters the functional equation of Dirichlet `L`-functions. The cancellation (4)--(5) is then a direct cyclotomic consequence, not a new theorem about character sums. The local `SOURCES.md` already anchors the character/Gauss-sum and cyclotomic frameworks used throughout PC-025, PC-035, and neighboring findings.

On the operator side, Sarason's 2008 paper is explicit prior art for unbounded analytic Toeplitz operators and Smirnov-class symbols on `H^2`. PC-207 already anchored the ordinary finite-polydisc Toeplitz/Hardy setting through Guo--Yan and its finite-variable Brown--Halmos neighbors. Reproducing-kernel adjoint eigenvectors, outer-function dense ranges, and the compact-resolvent spectral discreteness criterion are standard Hardy/operator theory.

No novelty is claimed for any of those components. The durable Prime-Circle contribution is the **exact closure of PC-207's canonical zero-depth boundary**: after removing all removable roots, the singular Hardy symbol is literally a reciprocal cyclotomic denominator supported on the primitive shell; its natural unbounded operator has a spectral continuum, its bounded `x`-renormalization vanishes strongly, and its quadratic boundary layer returns only the primitive-shell measure.

A directed novelty search did not reveal a separate RH mechanism attached to this particular zero-depth repackaging. More importantly, the exact reductions above show why absence of such a mechanism is structural rather than a failure to find the right terminology: all singular support and residues are already determined by `Phi_n` and the finite Gauss transform.

## 8. Boundary and research consequence

This finding is deliberately narrower than an all-purpose no-go for singular limits. It does **not** classify a renormalization that mixes two or more legs before the limit, a shell/refinement-dependent transfer operator, a valence growing with arithmetic complexity, a coupled distributional limit across levels, or a global uniformization/monodromy construction. Those can change the state space before equations (15) and the reproducing-kernel continuum argument apply.

It does close the source-native fixed-finite-valence option left explicitly open in PC-207:

\[
\boxed{
\text{positive Fourier legs at }x\downarrow0
\longrightarrow
\text{reciprocal cyclotomic Smirnov multipliers}
\longrightarrow
\text{primitive-shell boundary poles + continuous Hardy spectrum}.
}
\tag{16}
\]

The zero-depth singularity is therefore not by itself the missing nonseparable carrier. A viable continuation must create coupling **before** the separated rational/Smirnov multiplier stage, or move to a genuinely growing/global state where fixed finite tensor factorization no longer controls the operator.