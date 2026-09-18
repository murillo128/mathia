# PC-347 — finite radial-flux Chen hierarchy symmetrizes to Mangoldt and is cyclotomic

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for fully symmetric finite-depth radial orderings, and `DECISIVE-BOUNDARY` for the genuinely ordered/noncommutative part.

PC-346 leaves products, commutators, and orderings performed **before** scalar Mellin integration as one of the natural ways in which a matrix-valued Prime-Circle construction could differ from a passive Hilbert-space amplification. The canonical first test does not require choosing a matrix representation at all: retain the complete radial order of the exact cyclotomic logarithmic one-forms and form their Chen iterated integrals.

This produces a genuine ordered hierarchy. It does not collapse coefficientwise to the endpoint data: its depth-two antisymmetric component is exactly the interior carrier already isolated by PC-180/PC-181, and higher depths retain further ordered information. But two exact constraints sharply delimit what this buys.

First, **complete symmetrization at every finite depth is pure common-vertex data**. If

\[
J_{n_1,\ldots,n_r}
:=\int_{0<z_1<\cdots<z_r<1}
\prod_{j=1}^r d\log\Phi_{n_j}(z_j),
\qquad n_j>1,
\tag{1}
\]

then

\[
\boxed{
\sum_{\pi\in S_r}
J_{n_{\pi(1)},\ldots,n_{\pi(r)}}
=
\prod_{j=1}^r\Lambda(n_j).
}
\tag{2}
\]

Consequently every constant fully symmetric rank-`r` shell tensor `C` satisfies

\[
\boxed{
\sum_{n_1,\ldots,n_r} C_{n_1\cdots n_r}J_{n_1,\ldots,n_r}
=
\frac1{r!}
\sum_{n_1,\ldots,n_r}
C_{n_1\cdots n_r}
\prod_{j=1}^r\Lambda(n_j).
}
\tag{3}
\]

Thus PC-180's quadratic symmetric collapse is not a depth-two accident: **every finite-depth fully symmetric scalarization of this source-native ordered radial hierarchy sees only the Mangoldt endpoint vector**.

Second, the unsymmetrized coefficients are not a new period class. If

\[
N=\operatorname{lcm}(n_1,\ldots,n_r),
\]

then each `J_{n_1,...,n_r}` is a finite sum of convergent hyperlogarithmic iterated integrals whose letters are roots of unity in `mu_N`. Hence

\[
\boxed{
J_{n_1,\ldots,n_r}
\in
\operatorname{span}_{\mathbb Q}
\{\text{cyclotomic hyperlogarithm values of level }N
\text{ and length }r\}.
}
\tag{4}
\]

Equivalently, every fixed finite homogeneous level of the formal radial path signature lies in the classical cyclotomic multiple-polylogarithm period algebra. Finite path ordering therefore preserves more information than scalar Mellinization, but it does not by itself manufacture a new zeta spectral variable, a functional equation, or a critical-line mechanism.

## 1. The radial one-forms are exactly cyclotomic logarithmic letters

For `n>1`, put

\[
X_n(z):=\log\Phi_n(z),
\qquad 0\le z\le1.
\tag{5}
\]

There is no branch ambiguity on this interval. The real polynomial `Phi_n` has no zero in `[0,1]` and `Phi_n(0)=1`, so it stays positive there. Its endpoint values are

\[
X_n(0)=0,
\qquad
X_n(1)=\log\Phi_n(1)=\Lambda(n).
\tag{6}
\]

The exact logarithmic one-form is

\[
\omega_n(z)
:=dX_n(z)
=\frac{\Phi_n'(z)}{\Phi_n(z)}\,dz.
\tag{7}
\]

Writing `P_n^*` for the primitive `n`-th roots of unity gives the elementary partial fraction identity

\[
\boxed{
\omega_n(z)
=
\sum_{\alpha\in P_n^*}
\frac{dz}{z-\alpha}.
}
\tag{8}
\]

Because `1` is not primitive of order `n>1`, every letter in (8) stays off the integration path. Thus all iterated integrals in (1) are ordinary absolutely convergent Chen integrals; no endpoint regularization is required.

The relation with the signed radial flux of PC-179 is exact. With `z=e^{-x}` and

\[
F_n(x)=\log\Phi_n(e^{-x}),
\qquad
\rho_n(x)=-F_n'(x),
\tag{9}
\]

one has `dF_n=omega_n` after the change of variable and `rho_n(x)dx=-dF_n(x)`. Reversing the radial orientation from `x:0->infinity` to the intrinsic inward path `z:0->1` therefore produces precisely the one-form (7). The hierarchy (1) is not an externally inserted kernel; it is the ordered integral hierarchy of the same exact signed radial field already used in PC-179--PC-183.

## 2. Depth one is exactly the common-vertex Mangoldt selector

At depth one,

\[
J_n
=\int_0^1\omega_n
=X_n(1)-X_n(0)
=\Lambda(n).
\tag{10}
\]

Thus the degree-one part of the ordered hierarchy is exactly the existing common-anchor identity, not a new selector. In particular it vanishes on every non-prime-power shell and equals `log p` on `p^a`.

This matters for interpreting higher degrees. Any arithmetic support inherited simply by projecting the hierarchy back onto degree one is the original Mangoldt endpoint data. A new mechanism would have to use the genuinely ordered components in a way that survives the line's matched controls.

## 3. The shuffle identity upgrades PC-180 to every finite depth

Chen iterated integrals satisfy the shuffle product. Applying it to the product of the `r` one-letter integrals gives

\[
\left(\int_0^1\omega_{n_1}\right)\cdots
\left(\int_0^1\omega_{n_r}\right)
=
\sum_{\pi\in S_r}
J_{n_{\pi(1)},\ldots,n_{\pi(r)}}.
\tag{11}
\]

Repeated shell labels cause no exception: permutations are permutations of the labeled positions, so repeated words occur with their natural multiplicity. Substituting (10) proves (2).

For a finite shell set `S`, let `C` be a completely symmetric rank-`r` tensor. Define the most general radial-coordinate-independent symmetric contraction of the ordered level `r` by

\[
Q_C
:=
\sum_{n_1,\ldots,n_r\in S}
C_{n_1\cdots n_r}J_{n_1,\ldots,n_r}.
\tag{12}
\]

Symmetry of `C` makes `Q_C` invariant under every permutation of the indices. Averaging (12) over `S_r` and using (2) gives (3). Therefore no completely symmetric finite-degree polynomial readout of the Chen hierarchy can recover radial interior information that was absent from the endpoint vector.

At `r=2`, the statement is exactly PC-180. Indeed its ordered matrix

\[
A_{mn}=\int_0^\infty\rho_m(x)F_n(x)\,dx
\tag{13}
\]

satisfies, after the orientation change above,

\[
\boxed{A_{mn}=J_{n,m}.}
\tag{14}
\]

Then (11) becomes

\[
A_{mn}+A_{nm}=\Lambda(m)\Lambda(n),
\tag{15}
\]

which is PC-180's rank-one symmetric boundary identity. PC-181's nonzero `{2,6}` skew block is therefore the first nontrivial Lie/shuffle component of this same hierarchy, not a separate phenomenon.

## 4. Every fixed ordered coefficient is a cyclotomic hyperlogarithmic period

Insert (8) into (1). Since each root set is finite and all letters avoid `[0,1]`, expansion and integration commute directly:

\[
\boxed{
J_{n_1,\ldots,n_r}
=
\sum_{\alpha_j\in P_{n_j}^*}
\int_{0<z_1<\cdots<z_r<1}
\prod_{j=1}^r\frac{dz_j}{z_j-\alpha_j}.
}
\tag{16}
\]

If `N=lcm(n_1,...,n_r)`, every `alpha_j` belongs to `mu_N`. The summands in (16) are precisely ordinary hyperlogarithmic iterated integrals on

\[
\mathbb P^1\setminus(\{0,\infty\}\cup\mu_N),
\tag{17}
\]

with endpoint `1`, using only letters away from that endpoint. Up to the conventional reversal used in recursive `G(a_1,...,a_r;1)` notation, they are the standard multiple-polylogarithm values at roots of unity studied in cyclotomic multiple-polylogarithm theory. This proves (4).

The classification is coefficientwise and exact. No Mellin transform, analytic continuation, asymptotic approximation, or numerical recognition is involved. Shell arithmetic enters only through the finite choice of primitive root letters; path ordering raises the iterated-integral depth inside a classical cyclotomic period algebra.

This does **not** imply that the ordered coefficients are determined by `Lambda`. PC-181 already supplies the contrary control: on `{2,6}`, `Lambda(6)=0` while the off-diagonal ordered coefficient is nonzero. The point is different. Ordered information survives, but at every fixed depth its transcendental carrier is a classical cyclotomic hyperlogarithm rather than a newly forced zeta-zero object.

## 5. Formal noncommutativity is real, but bounded depth still classicalizes

Let `e_n` be noncommuting formal symbols and form the universal connection along the radial path

\[
\Omega_S(z)
:=\sum_{n\in S} e_n\,\omega_n(z)
\tag{18}
\]

for a finite shell set `S`. Its formal path-ordered exponential has the Chen expansion

\[
\mathcal U_S
=1+
\sum_{r\ge1}
\sum_{n_1,\ldots,n_r\in S}
J_{n_1,\ldots,n_r}\,
 e_{n_1}\cdots e_{n_r},
\tag{19}
\]

up to the harmless word-order convention chosen for left versus right ordered evolution.

Equation (19) makes precise the simplest noncommutative continuation left open by PC-346. The noncommutativity is active **before** any final scalar readout: word order distinguishes `J_{m,n}` from `J_{n,m}`, and commutators isolate the nonsymmetric interior components.

Nevertheless, every truncation through degree `R` has coefficients in the finite span of level-`N` cyclotomic hyperlogarithms of length at most `R`. More generally, if the symbols are represented by matrices or operators whose generated algebra is nilpotent of step `R`, the Dyson/Chen series terminates and the exact endpoint holonomy is a finite matrix whose entries lie in that same classical period span.

Therefore simply replacing the passive matrices of PC-346 by a **bounded-depth** product, commutator, Magnus term, or nilpotent path ordering does not escape to a new analytic class. It can preserve ordered shell information, but it remains a finite cyclotomic iterated-integral construction.

## 6. What is actually still open

The theorem deliberately stops before an infinite-depth, nonnilpotent resummation. For fixed nonnilpotent matrices `M_n`, the exact endpoint of

\[
U'(z)=U(z)\sum_{n\in S}M_n\frac{\Phi_n'(z)}{\Phi_n(z)}
\tag{20}
\]

may involve the entire Chen series rather than a finite period combination. Nothing here proves that such a holonomy collapses to a finite list of cyclotomic multiple polylogarithms.

But (20) also exposes the source-selection problem. Prime Circle intrinsically supplies the scalar forms `omega_n`; it does **not** automatically supply arbitrary noncommuting matrices `M_n`, a preferred representation, or a preferred spectral scalarization of the resulting holonomy. Choosing those freely would be an arbitrary spectral wrapper, excluded by the research mandate. A surviving noncommutative mechanism must therefore derive its representation or multiplication law from the roots/refinement/cross-level geometry itself and then prove that the resulting infinite-depth or nonperturbative observable has a zeta-relevant property not already inherited from cyclotomic period theory.

Similarly, the theorem does not cover a genuinely cross-level operation in which refinement changes the state space between radial insertions, a shell-dependent matrix symbol forced by old/new geometry, or an infinite-level limit whose normalization couples depth to conductor. Those alter a hypothesis rather than merely increasing the finite Chen depth.

## 7. Prior-art and novelty audit

The ambient mathematics is classical. Chen iterated integrals and their shuffle algebra are standard. A. B. Goncharov, **Multiple polylogarithms, cyclotomy and modular complexes**, *Mathematical Research Letters* 5 (1998), 497--516, DOI `10.4310/MRL.1998.v5.n4.a7`, treats multiple-polylogarithm values at roots of unity and is already the line's principal period-class anchor for cyclotomic hyperlogarithms in PC-100/PC-102/PC-104. The same source class therefore contains (16).

A directed check against cyclotomic multiple polylogarithms, iterated logarithmic integrals at roots of unity, Chen/path signatures, and noncommutative holonomy found the expected classical iterated-integral and cyclotomic-polylogarithm frameworks. In particular, the fact that a connection with logarithmic poles at roots of unity generates root-of-unity iterated integrals is standard structure, not a Prime-Circle novelty claim.

The line-local mathematical delta is narrower and exact: the **particular signed radial-flux hierarchy forced by the Prime-Circle cyclotomic shells** has PC-180 as its degree-two shuffle identity; its complete symmetric component collapses to the Mangoldt endpoint tensor at every finite degree; and all remaining fixed-degree ordered components lie in the classical cyclotomic hyperlogarithm algebra. This is distinct from PC-104, which classifies ordinary traces of finite Hardy-operator shell words, and from PC-189, which classifies Mellin transforms of finite local polynomial jet products as colored Tornheim/conical functions. Here the operation is radial **depth ordering before scalarization**, precisely the simple noncommutative continuation left open by PC-346.

No historical novelty is claimed for Chen theory, shuffle identities, hyperlogarithms, or cyclotomic multiple-polylogarithm values. The contribution is the exact boundary they impose on this specific Prime-Circle escape route.

## 8. Consequence for the Prime-Circle frontier

The finite-depth radial-ordering branch is now separated into two parts.

The completely symmetric part is closed: at every degree it is exactly a finite tensor form in `Lambda`, so it cannot provide a new positivity/coercivity mechanism beyond the common-anchor prime-power selector. The genuinely ordered part survives and really does retain composite-shell interior information, but each fixed homogeneous degree is a classical cyclotomic period. Merely taking more finite commutators or more finite Chen levels therefore increases iterated-integral depth without creating the missing zeta functional equation or critical-line structure.

The remaining noncommutative question is correspondingly sharper. It is not whether path ordering can remember information -- it can. It is whether the original Prime-Circle geometry forces a **specific nonnilpotent/infinite-depth or cross-level representation and a specific final invariant** whose analytic structure does something unavailable to the classical cyclotomic iterated-integral package. Without that additional source-forced structure, the formal signature is an information-rich encoding rather than an RH mechanism.

## Audit / falsification tests

This finding fails if any of the following occurs:

1. for some `n>1`, `Phi_n` has a zero on `[0,1]`, invalidating the ordinary logarithmic path or the convergence assertion;
2. the exact one-form decomposition (8) fails, or a root letter outside `mu_N` appears in a word with conductor lcm `N`;
3. the shuffle product of the one-letter integrals does not give (2), or a completely symmetric contraction retains a component not present in `Lambda^{\otimes r}`;
4. the change of variables between the radial flux coupling and (14) has the wrong orientation/sign, so that PC-180 is not recovered at depth two;
5. a bounded-depth/nilpotent path-ordered construction from only the forms (7) produces a coefficient outside the cyclotomic hyperlogarithm period algebra.

All five checkpoints are exact consequences of cyclotomic factorization, endpoint evaluation, Chen shuffle, and finite expansion. The theorem makes no claim about source-forced infinite-depth nonnilpotent holonomy or genuinely changing cross-level state spaces.