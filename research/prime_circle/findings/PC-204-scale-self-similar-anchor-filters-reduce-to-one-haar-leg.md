# PC-204 — scale-self-similar anchor filters reduce to one extra Haar leg

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for obtaining a new Prime-Circle/RH carrier by replacing the common-anchor Poisson kernel of PC-203 with any fixed scalar rotation-invariant anchor filter whose nonzero Fourier multiplier is self-similar in one homogeneous angular scale.

PC-203 proved that the canonical common-anchor Poisson kernel and every fixed finite Poisson/Dirichlet-to-Neumann jet do not escape the finite scalar packet algebra: after Mellinizing the anchor depth, each nonzero angular mismatch becomes one additional conductor-one Haar frequency. A natural repair is to change the anchor propagation law itself. The ordinary circle heat kernel uses `exp(-u h^2)` rather than `exp(-u |h|)`, while fractional spectral semigroups use `exp(-u |h|^alpha)`. More generally, a source-compatible scalar scale filter may have Fourier coefficient `kappa(u |h|^alpha)` for one fixed profile `kappa`.

The entire class collapses for the same structural reason, but the exact statement is stronger than the semigroup examples: **after Mellinization, the profile `kappa` disappears except for its scalar Mellin transform, and the mismatch contributes only the power `|Delta|^{-alpha w}`.** Splitting the sign of the mismatch again converts the construction into the PC-202 balanced Haar cone with one extra trivial conductor-one leg. Thus heat, fractional heat, homogeneous resolvent-type filters, and any other fixed Mellin-admissible self-similar scalar anchor profile do not provide a second arithmetic carrier.

## 1. General homogeneous anchor filter

Use the same finite source-native Cauchy–Poisson packets as PC-197/PC-202/PC-203. For primitive nonprincipal characters `chi_i (mod n_i)` and `psi_j (mod m_j)`, at positive packet depths,

\[
\mathcal K_{n_i,\chi_i}(x_i,\theta)
=
2\tau(\overline\chi_i)
\sum_{k_i\ge1}\chi_i(k_i)e^{-k_i x_i}e^{ik_i\theta},
\tag{1}
\]

and similarly for the conjugate packets. Write

\[
F(\theta)
=
\prod_{i=1}^{r}\mathcal K_{n_i,\chi_i}(x_i,\theta)
\prod_{j=1}^{q}\overline{\mathcal K_{m_j,\psi_j}(y_j,\theta)}.
\tag{2}
\]

Fix `alpha>0`. Let `kappa:(0,infinity)->C` be a profile such that the Fourier series and integrals below are absolutely convergent at the chosen positive packet depths and such that

\[
M_\kappa(w)
:=
\int_0^\infty v^{w-1}\kappa(v)\,dv
\tag{3}
\]

exists in a nonempty vertical strip. Consider the centered rotation-invariant anchor filter

\[
W_u^{(\alpha,\kappa)}(\theta)
=
\sum_{h\in\mathbb Z\setminus\{0\}}
\kappa(u|h|^\alpha)e^{ih\theta},
\qquad u>0.
\tag{4}
\]

The zero mode is omitted because it is exactly the Haar scalar fusion already classified in PC-202. Define

\[
\mathcal A_u^{(\alpha,\kappa)}
=
\frac1{2\pi}\int_0^{2\pi}
W_u^{(\alpha,\kappa)}(\theta)F(\theta)\,d\theta.
\tag{5}
\]

This class includes the ordinary centered heat kernel on the circle (`alpha=2`, `kappa(v)=e^{-v}`), the Poisson kernel of PC-203 (`alpha=1`, `kappa(v)=e^{-v}`), and the fractional spectral semigroups `exp(-u|D|^alpha)` for arbitrary positive `alpha`. No semigroup property is needed for the reduction.

## 2. Exact mismatch formula

As in PC-203, define

\[
\Delta(\mathbf k,\boldsymbol\ell)
=
\sum_{i=1}^{r}k_i-
\sum_{j=1}^{q}\ell_j.
\tag{6}
\]

The angular integral selects the coefficient of the anchor filter at `-Delta`, so

\[
\boxed{
\begin{aligned}
\mathcal A_u^{(\alpha,\kappa)}
&=C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\\Delta\ne0}}
\left(\prod_i\chi_i(k_i)\right)
\left(\prod_j\overline{\psi_j(\ell_j)}\right)\\
&\quad\times
\exp\!\left(-\sum_i k_i x_i-\sum_j\ell_j y_j\right)
\kappa\!\left(u|\Delta|^\alpha\right),
\end{aligned}}
\tag{7}
\]

where the Gauss-sum constant is the same as in PC-203. The filter genuinely retains every nonzero mismatch before scalarization. The issue is whether the new scale law makes that mismatch into a new analytic carrier.

A direct numerical control with quadratic characters modulo `3` and `5`, positive depths `(x,y,u)=(0.7,0.9,0.4)`, `alpha=2`, and `kappa(v)=e^{-v}` gives agreement to machine precision between the angular quadrature of (5) and the truncated double mismatch sum (7). The theorem below is exact and does not depend on that check.

## 3. Mellinization removes the filter profile

For every nonzero integer mismatch, the change of variable `v=u|Delta|^alpha` gives

\[
\boxed{
\int_0^\infty
u^{w-1}\kappa\!\left(u|\Delta|^\alpha\right)\,du
=
M_\kappa(w)|\Delta|^{-\alpha w}.
}
\tag{8}
\]

Thus after Mellinizing the packet depths independently, in any common absolute-convergence region,

\[
\boxed{
\begin{aligned}
\mathcal M\mathcal A
&=C_{\boldsymbol\chi,\boldsymbol\psi}
M_\kappa(w)
\prod_i\Gamma(s_i)
\prod_j\Gamma(t_j)\\
&\quad\times
Z^{(\alpha)}_{r,q}(\mathbf s;\mathbf t;w),
\end{aligned}}
\tag{9}
\]

with

\[
\boxed{
Z^{(\alpha)}_{r,q}
=
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\\Delta\ne0}}
\frac{
\prod_i\chi_i(k_i)
\prod_j\overline{\psi_j(\ell_j)}
}
{
\prod_i k_i^{s_i}
\prod_j\ell_j^{t_j}
|\Delta|^{\alpha w}
}.
}
\tag{10}
\]

The dependence on the complete anchor profile `kappa` is now the scalar factor `M_kappa(w)`. All arithmetic dependence of the filter is carried by the single homogeneous linear form `|Delta|` with exponent `alpha w`.

This is the decisive rigidity statement. Changing from Poisson to heat or to another self-similar profile changes an exponent rescaling and a scalar Mellin factor; it does not create another conductor, coefficient system, angular state, or shell relation.

## 4. The two sign chambers are again one-extra-leg Haar cones

If `Delta>0`, set `h=Delta`. Then

\[
\sum_i k_i
=
\sum_j\ell_j+h.
\tag{11}
\]

If `Delta<0`, set `h=-Delta`, giving

\[
\sum_i k_i+h
=
\sum_j\ell_j.
\tag{12}
\]

Therefore

\[
\boxed{
Z^{(\alpha)}_{r,q}
=
Z^{(+)}_{r,q+1}(\mathbf s;\mathbf t;\alpha w)
+
Z^{(-)}_{r+1,q}(\mathbf s;\mathbf t;\alpha w),
}
\tag{13}
\]

where both terms are exactly the fixed finite balanced rational-cone Dirichlet series of PC-202, with one additional conductor-one frequency carrying the trivial coefficient sequence `1,1,1,...`. Relative to PC-203, the only structural change is that the extra-leg Mellin exponent is `alpha w` rather than `w`.

The one-packet control makes the collapse especially transparent. With one holomorphic packet and no conjugate packet, the mismatch is just `Delta=k`, so after Mellinizing both positive scales the arithmetic factor is

\[
\sum_{k\ge1}\frac{\chi(k)}{k^{s+\alpha w}}
=
L(s+\alpha w,\chi).
\tag{14}
\]

For several packets the same operation produces the finite colored cone series (13), not a new Euler product.

## 5. Heat, fractional heat, and other homogeneous filters do not repair the RH mechanism

For the ordinary circle heat kernel,

\[
\kappa(v)=e^{-v},
\qquad \alpha=2,
\qquad M_\kappa(w)=\Gamma(w),
\tag{15}
\]

so the extra leg has exponent `2w`. For the Poisson semigroup `alpha=1`, this reproduces PC-203. Fractional powers of the circle Laplacian or `|D|` simply replace `2w` by the corresponding homogeneous exponent. A constant scale `c>0` in `kappa(cu|h|^alpha)` contributes only the scalar `c^{-w}`.

The same closure extends beyond exponential semigroups. For example, whenever its Mellin strip is nonempty, a resolvent-type profile `kappa(v)=(1+v)^{-nu}` contributes a beta-function scalar in (8) while leaving exactly the same `|Delta|^{-alpha w}` cone coordinate. Angular differentiation or fixed powers of the homogeneous generator multiply the extra frequency by a fixed power and therefore only shift the extra-leg exponent.

This directly closes the idea that the Poisson result was special to the first-order Dirichlet-to-Neumann generator. The second-order heat operator and its fractional/nonlocal homogeneous relatives are no richer after the source-native finite scalar packet contraction.

## 6. Theta-function and functional-equation audit

The `alpha=2` case sits next to a famous classical mechanism: the complete circle/lattice heat trace is a Jacobi theta series, and Poisson summation plus the modular inversion of theta yields Mellin representations and functional equations for zeta-type functions. That nearby fact does not supply a Prime-Circle mechanism here.

The object in (7) is not the free heat trace. Its Gaussian frequency is the **packet mismatch** `Delta`, while the remaining packet indices carry cyclotomic/Dirichlet coefficients and positive radial depths. After the exact chamber substitution, the Gaussian coordinate is one positive cone leg constrained by (11) or (12). Mellinization gives (13) before any spectral interpretation. A special boundary specialization may recover ordinary character theta series or their classical Dirichlet-`L` functional equations, but that is established theta/Dirichlet theory rather than a new relation forced by primitive-shell geometry.

Accordingly, the appearance of a heat kernel does not by itself provide the missing `s <-> 1-s` involution or select `Re(s)=1/2`. Any modular identity available only after a special endpoint, completion, or additional lattice symmetrization must be audited as extra structure rather than attributed to the finite anchored packet fusion.

## 7. Prior-art and novelty audit

The analytic ingredients are classical. Heat and fractional-Laplacian semigroups on the circle/torus are standard spectral functional calculus; Mellin scaling in (8) is the elementary homogeneity rule for the Mellin transform. Directed searches across torus fractional Laplacians, heat/Poisson semigroups, theta Mellin transforms, and multiple/conical Dirichlet series found the expected classical frameworks rather than a Prime-Circle-specific carrier.

For the arithmetic output, the relevant durable prior-art boundary is already recorded in `SOURCES.md`: Terasoma's rational-cone/cyclotomic multiple-zeta framework and Guo–Paycha–Zhang's conical-zeta subdivision theory contain the fixed finite rational-cone architecture reached in (13). PC-201--PC-203 already record the colored Mordell–Tornheim/conical specializations needed for the packet coefficients. No external theorem is load-bearing for the new implication (8)--(13), so no additional bibliography entry is needed merely to name the standard heat or fractional semigroup.

No historical novelty is claimed for self-similar kernels, Mellin scaling, heat kernels, fractional Laplacians, theta modularity, or conical zeta functions. The durable Mathia-specific result is the **closure theorem**: once a finite anchored scalar filter depends on the mismatch only through one homogeneous combination `u|Delta|^alpha`, independent Mellinization erases its profile and returns it to the one-extra-leg Haar cone class.

## 8. Scope and surviving frontier

The assumptions carrying the no-go are explicit: the angular filter is scalar and rotation-invariant around the fixed anchor; its nonzero Fourier coefficient uses one common scale through `kappa(u|h|^alpha)`; the number of source packets is fixed and finite; and the final observable contracts the angular mismatch to a scalar before or during Mellinization.

The theorem does **not** classify a shell-dependent multiplier `kappa_{m,n}(u,h)` derived from old/new incidence, a genuinely nonhomogeneous frequency-scale law not reducible to one product `u|h|^alpha`, matrix/operator-valued couplings that retain `h` as a state, filters whose number of interacting legs grows with refinement, indefinite non-scalar positivity constructions, or the global uniformization/monodromy sector. Those remain outside (8).

The practical gate after PC-203 is therefore sharper. Merely replacing the common-anchor Poisson propagation by heat, fractional heat, a homogeneous resolvent, or any other fixed Mellin-admissible self-similar scalar smoothing law cannot produce a new RH carrier. A surviving anchor-based non-Haar construction must make the mismatch interact with **additional source-derived relational data** before scalar Mellin collapse, rather than change only the homogeneous response assigned to that mismatch.
