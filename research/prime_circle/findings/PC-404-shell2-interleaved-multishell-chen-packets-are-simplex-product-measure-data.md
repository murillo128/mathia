# PC-404 — shell-2-interleaved multishell Chen packets are simplex product-measure data

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the entire finite-target Chen family obtained by fixing an ordered list of non-reference shells and distributing arbitrary shell-2 letters through the gaps, and for the canonical multivariate moment pencil built from that family. This does not classify cross-level/refinement couplings, a source-forced interaction that changes the product law between shell profiles, or nonlinear operations that introduce genuinely new data beyond the separately recovered profiles.

PC-403 leaves words with two or more genuinely independent non-reference shell insertions as the immediate unresolved continuation of the shell-2 Chen program. Those words do retain relative order information, but the whole family can be classified exactly. Once shell 2 is used as the monotone coordinate, an ordered word with fixed target shells is simply a multivariate moment of the **restricted product measure** of their already-known one-shell flux measures on an ordered simplex. Distributing shell-2 letters among all gaps gives the ordinary Bernstein basis on that simplex.

Consequently, for any fixed finite ordered target list, the complete shell-2-interleaved packet contains no independent cross-shell carrier beyond the individual measures reconstructed by PC-399 and the universal order relation `t_1<...<t_r`. At two targets the irreducible antisymmetric coefficient is a matrix element of one universal skew Volterra operator whose spectrum can be written explicitly and is independent of the cyclotomic source. The most canonical multivariate generalized-moment spectralization likewise reduces to multiplication by the separable density `prod_a w_{n_a}(t_a)` on the simplex, so its spectrum is only the range of that already-known product profile.

## 1. Exact ordered-simplex formula for arbitrary finite target depth

Use the shell-2 coordinate and measures from PC-399--PC-403:

\[
X_n(z)=\log\Phi_n(z),\qquad
t=X_2(z)=\log(1+z),\qquad
L=\log2,
\]

and

\[
\mu_n:=(X_2)_*(dX_n)
\quad\text{on }[0,L].
\tag{1}
\]

Fix an ordered list of target shells

\[
\mathbf n=(n_1,\ldots,n_r),\qquad r\ge1,
\]

and nonnegative integers `k_0,...,k_r`. As in PC-403, `2^{k_j}` denotes `k_j` repeated shell-2 letters, not an integer power. Consider the Chen word

\[
W(\mathbf k,\mathbf n)
=
2^{k_0},n_1,2^{k_1},n_2,\ldots,n_r,2^{k_r}.
\tag{2}
\]

Condition on the target insertion positions and write their shell-2 coordinates as

\[
0<t_1<\cdots<t_r<L.
\]

The repeated shell-2 blocks in the `r+1` gaps contribute ordinary simplex volumes. Therefore

\[
\boxed{
\left(\prod_{j=0}^{r}k_j!\right)
J_{W(\mathbf k,\mathbf n)}
=
\int_{0<t_1<\cdots<t_r<L}
 t_1^{k_0}
 \prod_{a=1}^{r-1}(t_{a+1}-t_a)^{k_a}
 (L-t_r)^{k_r}
 \prod_{a=1}^{r}d\mu_{n_a}(t_a).
}
\tag{3}
\]

No approximation or asymptotic limit enters. Equation (3) is the direct higher-dimensional analogue of PC-403 equation (1).

Define the ordered simplex

\[
\Delta_r(L):=\{(t_1,\ldots,t_r):0<t_1<\cdots<t_r<L\}
\tag{4}
\]

and the finite signed measure

\[
\boxed{
\nu_{\mathbf n}
:=
\mathbf 1_{\Delta_r(L)}
\,\mu_{n_1}\otimes\cdots\otimes\mu_{n_r}.
}
\tag{5}
\]

Then every coefficient in (3) is a polynomial moment of this one fixed measure. The apparent multishell interaction is therefore not an independently generated coupling measure: it is the ordinary product of the one-shell measures, restricted by the universal Chen ordering cone.

## 2. Shell-2 placements are exactly the Bernstein basis on the simplex

Introduce normalized gap coordinates

\[
x_0=\frac{t_1}{L},\qquad
x_a=\frac{t_{a+1}-t_a}{L}\ (1\le a<r),\qquad
x_r=\frac{L-t_r}{L}.
\tag{6}
\]

They satisfy

\[
x_j>0,\qquad \sum_{j=0}^{r}x_j=1,
\tag{7}
\]

so they are the barycentric coordinates of the standard `r`-simplex. Let `\eta_{\mathbf n}` be the pushforward of `\nu_{\mathbf n}` under (6), and fix total shell-2 depth

\[
K=k_0+\cdots+k_r.
\]

Multiplying (3) by `K!/L^K` gives

\[
\boxed{
\frac{K!}{L^K}J_{W(\mathbf k,\mathbf n)}
=
\int
\frac{K!}{k_0!\cdots k_r!}
\prod_{j=0}^{r}x_j^{k_j}
\,d\eta_{\mathbf n}(x).
}
\tag{8}
\]

The integrand is precisely the degree-`K` simplicial Bernstein polynomial indexed by `\mathbf k`. As `\mathbf k` ranges over all weak compositions of `K` into `r+1` parts, these polynomials form a basis of all polynomials of total degree at most `K` on the `r`-simplex. The number of placements,

\[
\binom{K+r}{r},
\]

is exactly the dimension of that polynomial space.

Hence the full fixed-`K` placement packet is an invertible linear re-encoding of the degree-`<=K` moment functional of `\eta_{\mathbf n}`. Taking all `K` gives every polynomial moment of the compact signed measure. By polynomial density on a compact simplex, those moments determine `\eta_{\mathbf n}` and therefore `\nu_{\mathbf n}` uniquely.

For `r=1`, this reduces exactly to PC-403: the two gap coordinates are `t/L` and `(L-t)/L`, and target placement is the ordinary one-dimensional Bernstein basis. For `r=2`, the previously open words

\[
J_{2^i,m,2^j,n,2^k}
\]

are the triangular Bernstein moments of

\[
\mathbf 1_{t<u}\,d\mu_m(t)d\mu_n(u).
\]

Thus adding a second independent target shell really raises the moment domain from an interval to a triangle, but it does **not** create a new coupling law on that triangle.

## 3. The full packet is already determined by the separate one-shell decoders

PC-399 proves that the one-sided shell-2 ladder

\[
\bigl(J_{2^k,n}\bigr)_{k\ge0}
\]

reconstructs `\mu_n` completely. Therefore, for a fixed target list `\mathbf n`, the separate ladders reconstruct every factor in

\[
\mu_{n_1}\otimes\cdots\otimes\mu_{n_r}.
\]

The ordering region `\Delta_r(L)` is universal and known. Equation (5) then reconstructs `\nu_{\mathbf n}` without using a single multishell Chen coefficient, and equation (3) computes every shell-2-interleaved multishell coefficient from it.

Consequently

\[
\boxed{
\{\text{all one-shell shell-2 ladders}\}
\Longrightarrow
\{\text{all shell-2-interleaved finite-target Chen packets}\}.
}
\tag{9}
\]

This implication is exact at infinite moment depth. It does **not** say that a finite multishell packet is a linear function of finite one-shell moment prefixes of comparable degree; the order indicator is not polynomial. The point is the durable information boundary: once the canonical one-shell decoder has recovered the radial profiles, the entire class (2) is a deterministic universal functional of those profiles and adds no independent source datum.

This sharpens PC-348/PC-399. Full signature information can of course encode interactions between coordinates, but in this particular time-augmented subfamily the shell-2 letter acts only as a common monotone clock. Interleaving that clock among finitely many target letters probes the product path measure through an ordered simplex; it does not generate a new arithmetic interaction between the targets.

## 4. At two targets the antisymmetric carrier is a universal skew Volterra operator

The first genuinely ordered case is `r=2` with no intervening shell-2 letters:

\[
J_{m,n}
=\int_{0<t<u<L}d\mu_m(t)d\mu_n(u).
\tag{10}
\]

The measures `\mu_n` are absolutely continuous with analytic real densities

\[
d\mu_n(t)=w_n(t)dt,
\qquad
w_n(t)=e^tX_n'(e^t-1),
\tag{11}
\]

so the diagonal has zero product measure. Partitioning the square gives the familiar shuffle identity

\[
J_{m,n}+J_{n,m}=\Lambda(m)\Lambda(n).
\tag{12}
\]

The antisymmetric part is

\[
\boxed{
J_{m,n}-J_{n,m}
=
\int_0^L\!\int_0^L
\operatorname{sgn}(u-t)
 w_m(t)w_n(u)\,du\,dt.
}
\tag{13}
\]

Thus the depth-two Lie carrier of PC-347/PC-180 is a matrix element of the single source-independent operator

\[
(Sf)(t)
:=
\int_0^L\operatorname{sgn}(u-t)f(u)\,du.
\tag{14}
\]

This operator is compact and skew-adjoint on `L^2([0,L])`. Its nonzero eigenpairs are elementary:

\[
\boxed{
S\,e^{i(2k+1)\pi t/L}
=
\frac{2iL}{(2k+1)\pi}
 e^{i(2k+1)\pi t/L},
\qquad k\in\mathbb Z.
}
\tag{15}
\]

Indeed `(Sf)'=-2f`, and the eigenvalue equation forces the anti-periodic boundary condition `f(L)=-f(0)`. Therefore

\[
\sigma(S)
=
\{0\}\cup
\left\{\frac{2iL}{(2k+1)\pi}:k\in\mathbb Z\right\}.
\tag{16}
\]

The nonlocal ordering kernel is real and useful, but its entire operator spectrum is universal. Cyclotomic arithmetic enters only through the vectors `w_n` used in the matrix elements (13). Spectralizing the order kernel itself therefore cannot produce a zeta-zero spectrum; a genuinely source-dependent operator would need additional coupling beyond the universal Chen order relation.

## 5. The canonical multivariate moment pencil is again only multiplication

The same collapse persists for the most direct spectralization of the complete `r`-target moment packet. Relative to Lebesgue measure on `\Delta_r(L)`, equation (11) gives

\[
d\nu_{\mathbf n}(\mathbf t)
=
W_{\mathbf n}(\mathbf t)d\mathbf t,
\qquad
\boxed{
W_{\mathbf n}(t_1,\ldots,t_r)
=\prod_{a=1}^{r}w_{n_a}(t_a).
}
\tag{17}
\]

The all-shell-2 reference is simply `d\mathbf t`. Define on polynomials

\[
B_{\mathbf n}(p,q)
=
\int_{\Delta_r(L)}p(\mathbf t)q(\mathbf t)
W_{\mathbf n}(\mathbf t)d\mathbf t,
\]

and

\[
B_{\mathbf 2}(p,q)
=
\int_{\Delta_r(L)}p(\mathbf t)q(\mathbf t)d\mathbf t.
\tag{18}
\]

Because the Bernstein packets (8) recover polynomial moments of every degree, their finite matrices provide these forms by fixed polynomial basis conversion. Completing in the positive reference norm gives

\[
L^2(\Delta_r(L),d\mathbf t),
\]

and the relative Riesz operator is exactly

\[
\boxed{
A_{\mathbf n}=M_{W_{\mathbf n}}.
}
\tag{19}
\]

Since `W_{\mathbf n}` is real and continuous and the closed ordered simplex is connected,

\[
\boxed{
\sigma(A_{\mathbf n})
=
W_{\mathbf n}(\overline{\Delta_r(L)})
=
[\min W_{\mathbf n},\max W_{\mathbf n}].
}
\tag{20}
\]

Finite polynomial moment pencils are ordinary Galerkin/Ritz compressions of this multiplication operator, exactly as in PC-402 but now on a simplex. Increasing the multivariate moment depth can approximate the extrema of the separable product density; it does not expose a hidden discrete arithmetic spectrum.

This does not rule out every nonlinear use of several shell profiles. It rules out interpreting the raw ordered multishell packet, its simplex moment matrices, or the canonical relative generalized spectrum as an independent cross-shell interaction. Their source content is already contained in the one-shell densities `w_n`.

## 6. Matched control and prior-art audit

Nothing in Sections 1--5 uses roots of unity beyond the choice of the smooth densities `w_n`. Replace the cyclotomic profiles by arbitrary smooth real profiles `Y_n` on `[0,1]`, keep the same monotone coordinate

\[
t=\log(1+z),
\]

and push `dY_n` forward to arbitrary smooth signed densities `v_n(t)dt`. Equations (3), (5), (8), (13), and (17)--(20) survive verbatim with `w_n` replaced by `v_n`. Hence the entire product-simplex/Bernstein/multiplication architecture is reproduced by non-arithmetic controls. Cyclotomic input selects special profiles; it does not make the ordering mechanism arithmetic.

The ambient mathematics is classical Chen-signature and polynomial-moment theory. PC-347 already anchors Chen iterated integrals and cyclotomic hyperlogarithms; PC-399 anchors signature inversion and compact moment determinacy. A particularly close current prior-art result is Arthur Bourdon, Benjamin Jourdain and Hervé Andrès, **Linear independence properties of the signature components of time-augmented stochastic processes**, arXiv:2601.10545v3 (17 July 2026). They emphasize that adding time as a signature component creates universal linear dependencies: at truncation order `N`, length-`N` time-augmented signature components span all components of length at most `N`, and they identify smaller spanning subfamilies. Prime Circle's shell `2` becomes exactly such a time coordinate after the reparametrization `t=X_2(z)`.

The simplicial Bernstein basis in (8), compact multivariate moment determinacy, the Volterra/order kernel in (14), and multiplication-operator spectral theory are likewise standard. No novelty is claimed for those ingredients. The line-local delta is the exact classification of the specific Prime-Circle continuation left open by PC-403: **any finite ordered list of target shells with arbitrary shell-2 blocks between them is only the Bernstein moment system of a universally ordered product of already-decoded shell measures.**

This is stronger than the fixed-depth cyclotomic-period classification in PC-347 and different from the one-target Bernstein gauge in PC-403. It identifies the data carrier itself for arbitrarily many fixed target insertions and shows that even the natural higher-dimensional moment spectralization adds no independent coupling.

## 7. Consequence for the surviving Prime-Circle frontier

The immediate route

\[
\text{several target shells + arbitrary shell-2 placements}
\longrightarrow
\text{ordered multivariate moment packet}
\longrightarrow
\text{new off-diagonal/nonlocal spectral carrier}
\]

is closed in this form. Shell-2 placement creates barycentric coordinates on an ordered simplex; the target measures remain factorized; and the canonical relative operator is multiplication by their product density.

A surviving multishell mechanism must therefore alter at least one of those facts. It could use a cross-level/refinement operation that changes the state space between insertions, a root-derived kernel that is not the universal order indicator, a source-forced interaction measure that does not factor into the individual `\mu_n`, or a nonlinear operation whose essential datum is not already determined by separately reconstructed shell profiles. Such constructions remain subject to the README's matched-control, prior-art, and no-arbitrary-wrapper gates.

The result also clarifies what does **not** qualify as an escape: merely increasing the number of target insertions, increasing the number of shell-2 letters, passing from interval moments to simplex moments, antisymmetrizing the first two target letters, or forming the canonical generalized moment pencil. All of those operations stay inside the product-measure/time-augmentation envelope classified above.

## Audit / falsification tests

This finding must be revised or withdrawn if any of the following fails:

1. conditioning the Chen word (2) on the `r` target insertion positions does not give the `r+1` simplex-volume factors in (3);
2. the common shell-2 change of variable fails to push the target differentials independently to the product measure in (5);
3. the gap monomials at fixed total degree `K` are not the simplicial Bernstein basis and do not span all polynomials of degree at most `K`;
4. polynomial moments fail to determine a finite signed measure on the compact simplex;
5. PC-399's one-shell ladders do not determine the individual `\mu_n`, invalidating implication (9);
6. the two-target antisymmetric identity (13) or the explicit universal spectrum (15)--(16) is incorrect;
7. the relative form (18) has an operator other than multiplication by `W_{\mathbf n}`;
8. a smooth non-arithmetic matched family cannot reproduce the same ordered-product/Bernstein construction.

Items 1--8 are exact consequences of simplex conditioning, the shell-2 homeomorphic coordinate, compact polynomial density, and standard integral-operator theory. The finding makes no no-go claim for genuinely new cross-level data or a source-derived non-factorizing multishell interaction.