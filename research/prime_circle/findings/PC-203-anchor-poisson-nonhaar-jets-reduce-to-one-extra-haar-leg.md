# PC-203 — anchored Poisson non-Haar jets reduce to one extra Haar leg

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for using the source-native common-anchor Poisson semigroup, or any fixed finite radial/angular jet of that semigroup, as a scalar non-Haar fusion of finitely many Prime-Circle Cauchy–Poisson packets to obtain a new RH/GRH carrier.

PC-202 closed every fixed finite **Haar** scalar fusion of holomorphic and antiholomorphic source-native character packets: angular conservation leaves a rational cone, and independent Mellin transforms give finite colored rational-cone Dirichlet data. Its explicit surviving boundary included source-forced non-Haar angular couplings. The common anchored vertex `1` supplies a particularly canonical such coupling: weight the angular product by the Poisson kernel centered at the anchor rather than by Haar measure alone.

That repair retains Fourier mismatch rather than imposing exact equality, but it still does not escape the finite packet algebra. After removing the Haar zero mode, the anchored Poisson kernel weights a mismatch `Delta` by `e^{-|Delta|u}`. Mellinizing the intrinsic anchor depth `u` turns that factor into `Gamma(w)|Delta|^{-w}`. Splitting into `Delta>0` and `Delta<0` shows something stronger than a generic cone reduction: each chamber is **exactly a PC-202 balanced Haar cone with one additional conductor-one anchor frequency**. Finite Dirichlet-to-Neumann/radial/angular derivatives only multiply that extra frequency by a fixed power and therefore shift its Mellin exponent.

Thus the most canonical non-Haar scalar kernel forced by the common anchor is not a second analytic carrier. It is an extra trivial-frequency leg inside the already-classified finite rational-cone packet algebra.

## 1. Source-native packets and the anchored Poisson kernel

For primitive nonprincipal characters `chi_i (mod n_i)` and `psi_j (mod m_j)`, use the angular Cauchy–Poisson packets of PC-197/PC-202,

\[
\mathcal K_{n_i,\chi_i}(x_i,\theta)
=
2\tau(\overline\chi_i)
\sum_{k_i\ge1}\chi_i(k_i)e^{-k_ix_i}e^{ik_i\theta},
\tag{1}
\]

and similarly for the conjugate packets. For fixed finite `r,q>=1`, write

\[
F(\theta)
:=
\prod_{i=1}^{r}\mathcal K_{n_i,\chi_i}(x_i,\theta)
\prod_{j=1}^{q}\overline{\mathcal K_{m_j,\psi_j}(y_j,\theta)}.
\tag{2}
\]

The common vertex is the angle `theta=0`. For anchor depth `u>0`, let

\[
P_u(\theta)
:=
\frac{1-e^{-2u}}
{1-2e^{-u}\cos\theta+e^{-2u}}
=
\sum_{h\in\mathbb Z}e^{-|h|u}e^{ih\theta}
\tag{3}
\]

be the disk Poisson kernel centered on the radial ray to `1`. Its centered version

\[
P_u^\circ(\theta):=P_u(\theta)-1
=\sum_{h\ne0}e^{-|h|u}e^{ih\theta}
\tag{4}
\]

removes the Haar mode already classified by PC-202.

Define the anchored non-Haar scalar fusion

\[
\boxed{
\mathcal A_u
:=
\frac1{2\pi}\int_0^{2\pi}
P_u^\circ(\theta)F(\theta)\,d\theta.
}
\tag{5}
\]

This weighting is not chosen to manufacture a Dirichlet exponent: it is the ordinary harmonic Poisson evaluation attached to the distinguished source vertex. At positive packet depths all Fourier series are absolutely convergent.

## 2. Exact mismatch formula

Expanding (2), put

\[
\Delta(\mathbf k,\boldsymbol\ell)
:=
\sum_{i=1}^{r}k_i-
\sum_{j=1}^{q}\ell_j.
\tag{6}
\]

The angular integral in (5) pairs the Fourier mode `Delta` with the coefficient of `P_u^circ` at `-Delta`. Therefore

\[
\boxed{
\begin{aligned}
\mathcal A_u
&=C_{\boldsymbol\chi,\boldsymbol\psi}
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\
\Delta\ne0}}
\left(\prod_i\chi_i(k_i)\right)
\left(\prod_j\overline{\psi_j(\ell_j)}\right)\\
&\qquad\times
\exp\!\left(-\sum_i k_ix_i-\sum_j\ell_jy_j\right)
 e^{-|\Delta|u},
\end{aligned}}
\tag{7}
\]

where

\[
C_{\boldsymbol\chi,\boldsymbol\psi}
=2^{r+q}
\prod_i\tau(\overline\chi_i)
\prod_j\overline{\tau(\overline\psi_j)}.
\tag{8}
\]

So the non-Haar kernel really does retain information killed by Haar projection: all nonzero angular mismatches survive. The question is whether this retained index produces a new analytic species after using the intrinsic depth variable. It does not.

As a numerical sanity check, for the quadratic characters modulo `3` and `5`, positive depths `(x,y,u)=(0.7,0.9,0.5)`, a Fourier quadrature of (5) and the truncated double sum (7) agree to machine precision. The exact result, however, is the Fourier identity above and does not depend on numerics.

## 3. Mellinizing the anchor depth creates only one extra positive linear form

Mellin-transform all radial depths independently. In the safe region

\[
\Re s_i>1,
\qquad
\Re t_j>1,
\qquad
\Re w>0,
\tag{9}
\]

absolute convergence permits termwise integration. Besides the usual factors

\[
\int_0^\infty x^{s-1}e^{-kx}\,dx
=\Gamma(s)k^{-s},
\]

one has for every nonzero mismatch

\[
\int_0^\infty u^{w-1}e^{-|\Delta|u}\,du
=\Gamma(w)|\Delta|^{-w}.
\tag{10}
\]

Hence

\[
\boxed{
\begin{aligned}
\mathcal M\mathcal A
&=C_{\boldsymbol\chi,\boldsymbol\psi}
\Gamma(w)
\prod_i\Gamma(s_i)
\prod_j\Gamma(t_j)\\
&\quad\times
Z^{\rm anch}_{r,q}(\mathbf s;\mathbf t;w),
\end{aligned}}
\tag{11}
\]

with

\[
\boxed{
Z^{\rm anch}_{r,q}
=
\sum_{\substack{\mathbf k,\boldsymbol\ell\ge1\\
\Delta\ne0}}
\frac{
\prod_i\chi_i(k_i)
\prod_j\overline{\psi_j(\ell_j)}
}
{
\prod_i k_i^{s_i}
\prod_j\ell_j^{t_j}
|\Delta|^w
}.
}
\tag{12}
\]

The additional intrinsic Mellin variable is genuine, but its only arithmetic action is to attach a power to the one integer linear form `|Delta|`.

## 4. Each sign chamber is literally one extra Haar packet leg

Split (12) according to the sign of `Delta`.

If `Delta>0`, put

\[
h=\Delta\ge1.
\]

Then

\[
\sum_i k_i
=
\sum_j\ell_j+h.
\tag{13}
\]

This is exactly the PC-202 Haar balance law after adding one **antiholomorphic conductor-one anchor leg** of positive frequency `h`, trivial periodic coefficient `1`, and Mellin exponent `w`.

If `Delta<0`, put

\[
h=-\Delta\ge1.
\]

Then

\[
\sum_i k_i+h
=
\sum_j\ell_j,
\tag{14}
\]

which is the same PC-202 balance law with one additional **holomorphic conductor-one anchor leg**.

Therefore

\[
\boxed{
Z^{\rm anch}_{r,q}
=
Z^{(+)}_{r,q+1}
+
Z^{(-)}_{r+1,q},
}
\tag{15}
\]

where both terms are fixed finite balanced rational-cone Dirichlet series of precisely the class already classified in PC-202. The common anchor does not supply a new conductor or a new coefficient system; it supplies the trivial coefficient sequence `1,1,1,...` on the extra leg.

This reduction is stronger than merely saying that (12) can be subdivided into cones. The non-Haar operation itself can be re-expressed as ordinary Haar angular conservation after adjoining one source-native anchor frequency.

## 5. The first two-packet case is a colored Tornheim/Shintani cone

For `r=q=1`, write the Mellin exponents as `s,t,w`. Equation (12) splits exactly into

\[
\boxed{
\begin{aligned}
Z^{\rm anch}_{1,1}
&=
\sum_{h,\ell\ge1}
\frac{\chi(h+\ell)\overline\psi(\ell)}
{(h+\ell)^s\ell^t h^w}\\
&\quad+
\sum_{k,h\ge1}
\frac{\chi(k)\overline\psi(k+h)}
{k^s(k+h)^t h^w}.
\end{aligned}}
\tag{16}
\]

The coefficients are periodic in the two cone coordinates, hence finite Fourier sums of roots-of-unity colors. The denominator uses only the three positive integral linear forms `h`, `ell`, `h+ell` (or `k`, `h`, `k+h`). Thus the simplest genuinely non-Haar anchored fusion already lands directly in the colored Tornheim/Shintani/conical-zeta architecture used in PC-189, PC-201 and PC-202.

This also gives a transparent endpoint check. As `u->0+` at fixed positive packet depths, Poisson convergence gives

\[
\mathcal A_u
\longrightarrow
F(0)-\frac1{2\pi}\int_0^{2\pi}F(\theta)\,d\theta.
\tag{17}
\]

The first term is the direct product of the individual one-shell packets at the anchor, while the second is exactly the Haar fusion. Thus even the singular anchor endpoint reduces to already-classified packet data.

## 6. Finite Poisson/Dirichlet-to-Neumann jets do not escape

The Poisson semigroup is generated by the circle Dirichlet-to-Neumann multiplier. For integers `a,b>=0`, differentiate the centered kernel:

\[
W_{a,b}(u,\theta)
:=(-\partial_u)^a\partial_\theta^bP_u^\circ(\theta).
\tag{18}
\]

Its nonzero Fourier coefficients are

\[
\widehat W_{a,b}(h)
=|h|^a(ih)^b e^{-|h|u},
\qquad h\ne0.
\tag{19}
\]

Replacing `P_u^circ` by `W_{a,b}` therefore multiplies the summand in (7) by

\[
|\Delta|^a(-i\Delta)^b.
\tag{20}
\]

On the two sign chambers this is only a fixed phase times `h^{a+b}`. After the `u`-Mellin transform, the new factor is

\[
\Gamma(w)h^{a+b-w},
\tag{21}
\]

so the extra anchor-leg exponent in (13)--(15) is merely shifted from `w` to `w-a-b`. Any fixed finite linear combination of radial/angular Poisson jets stays in the same finite cone span. The harmonic-conjugate kernel only inserts the usual sign phase between positive and negative frequencies and changes nothing structurally.

Thus finite source-native DtN/Poisson differentiation does not turn the anchor into a second independent carrier. It changes parameters inside the same rational-cone family.

## 7. Composite controls and novelty audit

Primality is unused in (3)--(21). Primitive characters of composite conductors satisfy the same packet expansion, and principal/Ramanujan modes are still periodic coefficients. The same anchored Poisson reduction therefore survives conductor-matched composite controls unchanged. Prime levels merely make the nonprincipal multiplicative character basis especially complete.

The external ingredients are classical. The disk Poisson kernel, its Fourier semigroup, and the Dirichlet-to-Neumann generator are standard harmonic analysis. Tomohide Terasoma, *Rational convex cones and cyclotomic multiple zeta values* (arXiv `math/0410306`), and Li Guo, Sylvie Paycha and Bin Zhang, *Conical zeta values and their double subdivision relations*, *Advances in Mathematics* 252 (2014), 343–381, already provide the rational-cone/cyclotomic subdivision setting used by PC-202 and are recorded in `SOURCES.md`. The depth-two specialization (16) also lies in the colored Tornheim terrain already recorded there through Jianqiang Zhao.

Directed prior-art checks around Poisson/Dirichlet-to-Neumann semigroups and rational-cone multiple Dirichlet series returned the expected classical harmonic-semigroup and conical/Shintani frameworks rather than a Prime-Circle-specific analytic family. No historical novelty is claimed for any of those ingredients. The durable result here is the Prime-Circle closure statement (15): **the canonical common-anchor non-Haar Poisson coupling is exactly two already-classified Haar cone sectors with one extra trivial anchor leg**.

## 8. RH and critical-line audit

The construction improves on Haar projection in one real sense: it retains the full nonzero angular mismatch `Delta` before scalarization, and its Mellin variable `w` is dual to an intrinsic harmonic depth rather than inserted by hand. But after the exact chamber reduction, there is no source-derived Euler product, no new self-adjoint spectral problem, no completed-zeta functional equation, and no involution selecting `Re(s)=1/2`.

Any zero or functional relation inherited from the cone series is therefore a property of the established multiple-Dirichlet/conical analytic class, not a new zero-confinement mechanism forced by prime-circle geometry. Packaging (12) into a determinant after scalarization would be an arbitrary spectral wrapper and is outside the mandate.

## 9. Research consequence and boundary

This closes the most canonical source-forced **anchor-based non-Haar scalar** repair left by PC-202. Replacing Haar measure by the common-anchor Poisson kernel, its harmonic conjugate, or any fixed finite radial/angular/DtN jet does not escape the finite scalar packet closure; after Mellinization it is equivalent to adjoining one trivial anchor-frequency leg.

The finding does **not** classify shell-dependent non-Haar kernels whose Fourier multiplier is itself derived from old/new geometry, matrix/operator-valued couplings that retain the mismatch index as a state rather than summing it, infinite-refinement limits in which the number of coupled legs grows, non-scalar positivity constructions, or global uniformization/monodromy data. Those remain structurally outside (15).

The practical gate is therefore sharper than PC-202's generic `non-Haar` escape: a surviving finite scalar angular kernel must contain shell-dependent relational information that cannot be represented by finitely many source-native anchor Poisson/DtN legs. Merely breaking Haar orthogonality with the canonical common-anchor harmonic semigroup is not enough.
