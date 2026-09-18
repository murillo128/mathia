# PC-349 — inversion-closed radial signature has trivial abelianization and a rank-two first Lie level

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `NUMERICAL-SANITY` + `DECISIVE-NEGATIVE` for commutative/determinant and degree-two inversion readouts; `DECISIVE-BOUNDARY` for higher noncommutative depth.

PC-003 gives the exact interior/exterior reciprocity of the cyclotomic potentials, PC-029 shows that linearly spectralizing that spatial inversion produces only elementary Ramanujan data, and PC-347/PC-348 show that radial path ordering retains genuinely noncommutative information. A natural remaining possibility is therefore to combine the two exact structures: close the radial cyclotomic path by its reciprocity-forced asymptotic ray and inspect the resulting noncommutative signature as the analogue of an inversion/scattering defect.

The resulting object is canonical and source-native, but its first two structural tests are strongly negative. Its **entire abelianization is trivial**, so every commutative character and determinant sees nothing. More sharply, its first nonzero Lie level is an antisymmetric shell matrix of rank at most two, with an exact coefficient depending only on `phi(n)`, `rad(n)`, `mu(rad(n))`, and `zeta(2)`. The rank-two collapse is kinematic for any reciprocal path; the cyclotomic input merely makes the one remaining moment vector elementary.

Thus spatial inversion does produce a genuine noncommutative defect, but neither its abelian channel nor its first Lie correction supplies a zeta functional equation, a critical-line selector, or a high-rank arithmetic coupling. Any surviving inversion-based mechanism must use higher/unbounded noncommutative depth in an essential way.

## 1. The reciprocity-forced inversion loop

Fix a finite shell set `S` and write

\[
X_n(r):=\log\Phi_n(r),\qquad r\ge 0,\quad n\in S,
\tag{1}
\]

with `X_n(0)=0`. For `n>1`, cyclotomic reciprocity is

\[
\boxed{
X_n(r)=\varphi(n)\log r+X_n(r^{-1})
}
\qquad(r>0).
\tag{2}
\]

Let

\[
\boldsymbol\varphi=(\varphi(n))_{n\in S}
\tag{3}
\]

and, for `R>1`, form the path `Gamma_R` in shell-coordinate space by first following

\[
r\longmapsto X_S(r):=(X_n(r))_{n\in S},\qquad 0\le r\le R,
\tag{4}
\]

and then appending the straight segment of displacement

\[
-(\log R)\boldsymbol\varphi.
\tag{5}
\]

This closure is not chosen freely. By (2), the endpoint is exactly

\[
X_S(R)-(\log R)\boldsymbol\varphi=X_S(R^{-1})\longrightarrow0.
\tag{6}
\]

Thus `Gamma_R` tends to a closed path after removing precisely the exterior growth forced by reciprocity.

Let `e_n` be noncommuting shell letters and let `Sig(Gamma_R)` be the tensor signature. Equivalently, if

\[
\Omega=\sum_{n\in S}e_n\,dX_n,
\qquad
H=\sum_{n\in S}\varphi(n)e_n,
\tag{7}
\]

then, with the standard chronological product convention,

\[
\mathcal D_R
=
\mathcal P\exp\!\left(\int_0^R\Omega\right)
\exp[-(\log R)H].
\tag{8}
\]

The degreewise limit

\[
\boxed{
\mathcal D_S:=\lim_{R\to\infty}\mathcal D_R
}
\tag{9}
\]

exists in the completed tensor algebra. Under `t=1/r`, the exterior connection is

\[
\Omega(t)-H\,\frac{dt}{t},
\tag{10}
\]

namely a logarithmic connection with residue `-H` at the tangential endpoint `t=0` plus a regular cyclotomic remainder. Equation (9) is therefore the standard degreewise regularized holonomy of a logarithmic Fuchsian connection. No arbitrary matrix representation has been inserted.

## 2. The complete abelian channel cancels exactly

The abelianization of the signature of any path is the exponential of its total displacement. Hence (6) gives, for every finite `R`,

\[
\operatorname{ab}(\mathcal D_R)
=
\exp\!\left(
\sum_{n\in S}X_n(R^{-1})e_n
\right).
\tag{11}
\]

Taking `R -> infinity`,

\[
\boxed{
\operatorname{ab}(\mathcal D_S)=1.
}
\tag{12}
\]

Consequently

\[
\boxed{
\log\mathcal D_S
\in
[\widehat{\mathfrak f}_S,\widehat{\mathfrak f}_S],
}
\tag{13}
\]

where `f_S` is the free Lie algebra on the shell letters. The inversion defect has no degree-one component at all.

This is stronger than the endpoint collapse in PC-348. There the full interior signature abelianizes to `exp(sum Lambda(n)e_n)`; after adjoining the reciprocity-forced exterior and asymptotic closure, even that endpoint vector cancels. Every algebra homomorphism from (9) to a commutative algebra therefore sends the defect to the identity.

For a finite-dimensional substitution `e_n -> M_n`, the same statement implies formally, and analytically whenever the regularized matrix holonomy exists,

\[
\boxed{\det \mathcal D_S(M)=1.}
\tag{14}
\]

Indeed at finite `R`, Liouville's determinant formula gives

\[
\det\mathcal D_R(M)
=
\exp\!\left(
\sum_n X_n(R^{-1})\operatorname{tr}M_n
\right)
\longrightarrow1.
\tag{15}
\]

Thus the product of holonomy eigenvalues cannot carry the hoped-for inversion arithmetic.

## 3. The first surviving Lie coefficient is an exact radial area

Because the limiting displacement vanishes, the degree-two part of `log D_S` is the Levy-area bivector. For shells `m,n`, put

\[
A_{mn}
:=
\frac12\int_{\Gamma_\infty}
(X_m\,dX_n-X_n\,dX_m).
\tag{16}
\]

The appended straight segment contributes

\[
-\frac{\log R}{2}
\bigl(X_m(R)\varphi(n)-X_n(R)\varphi(m)\bigr)
\tag{17}
\]

at cutoff `R`. Reciprocity replaces `X_k(R)` by `varphi(k) log R+X_k(1/R)`; the quadratic logarithmic term cancels and (17) tends to zero because `X_k(t)=O(t)` as `t->0`. Therefore

\[
A_{mn}
=
\frac12\int_0^\infty
(X_m\,dX_n-X_n\,dX_m).
\tag{18}
\]

Now invert only the exterior half. Set

\[
I_n:=\int_0^1 X_n(t)\,\frac{dt}{t}.
\tag{19}
\]

Using

\[
X_n(1/t)=X_n(t)-\varphi(n)\log t
\tag{20}
\]

and integrating the `log t dX_n` terms by parts gives the exact cancellation

\[
\boxed{
A_{mn}=\varphi(n)I_m-\varphi(m)I_n.
}
\tag{21}
\]

Thus the first noncommutative inversion correction is already decomposable: it is the wedge of the totient vector with one scalar moment vector.

## 4. The remaining moment is elementary Ramanujan data

For `0<=t<1`, the classical cyclotomic/Ramanujan expansion is

\[
X_n(t)
=-\sum_{k\ge1}\frac{c_n(k)}{k}t^k.
\tag{22}
\]

Termwise integration in (19) yields

\[
I_n=-\sum_{k\ge1}\frac{c_n(k)}{k^2}.
\tag{23}
\]

Using

\[
c_n(k)=\sum_{d\mid(n,k)}d\,\mu(n/d)
\tag{24}
\]

one obtains

\[
\sum_{k\ge1}\frac{c_n(k)}{k^2}
=
\zeta(2)\sum_{d\mid n}\frac{\mu(n/d)}d
=
\frac{\zeta(2)}n\prod_{p\mid n}(1-p).
\tag{25}
\]

Equivalently, with `rad(n)` the squarefree radical,

\[
\boxed{
I_n
=-\zeta(2)\,\mu(\operatorname{rad}n)
\frac{\varphi(n)\operatorname{rad}(n)}{n^2}.
}
\tag{26}
\]

Define

\[
g_n:=\mu(\operatorname{rad}n)\frac{\operatorname{rad}(n)}{n^2}.
\tag{27}
\]

Substitution into (21) gives

\[
\boxed{
A_{mn}
=
\zeta(2)\varphi(m)\varphi(n)(g_n-g_m).
}
\tag{28}
\]

If `u_n=varphi(n)` and `v_n=varphi(n)g_n`, then

\[
\boxed{
A=\zeta(2)(u v^T-v u^T),
\qquad \operatorname{rank}A\le2.
}
\tag{29}
\]

This rank bound is independent of the number of shells. For squarefree `n`, `g_n=mu(n)/n`, so even on a growing squarefree family the entire first Lie level is only the wedge of two elementary arithmetic vectors.

As a numerical sanity check, for the pair `{2,3}` formula (28) gives

\[
A_{2,3}=\frac{\zeta(2)}3=\frac{\pi^2}{18}
=0.548311355616075\ldots,
\tag{30}
\]

matching direct quadrature of (18).

## 5. The rank-two collapse is kinematic, not arithmetic

The decomposability in (21) is not special to cyclotomic polynomials. Let `Y(t)` be any sufficiently regular vector path on `(0,1]` with `Y(t)=O(t^alpha)` for some `alpha>0`, and construct an exterior path by the same reciprocal law

\[
Y^{\mathrm{ext}}(r)
=\boldsymbol a\log r+Y(1/r),
\qquad r\ge1,
\tag{31}
\]

then close by the asymptotic ray `-(log R) a`. Repeating the derivation gives

\[
\boxed{
A^{Y}_{ij}
=a_j\int_0^1Y_i(t)\frac{dt}{t}
-a_i\int_0^1Y_j(t)\frac{dt}{t},
}
\tag{32}
\]

so `rank A^Y <= 2` for every such reciprocal control.

Therefore the low-rank first Lie defect is a universal consequence of **one reciprocal interior path plus one asymptotic direction**. Prime Circle does not obtain extra arithmetic selectivity from that mechanism. Its special contribution is only that the moment in (32) evaluates explicitly to the radical/totient expression (26).

This is an important matched control: observing a nonzero inversion area or rank-two commutator sector is not evidence for a zeta-specific structure.

## 6. Higher levels remain cyclotomic regularized holonomy

Let

\[
N=\operatorname{lcm}(S).
\tag{33}
\]

After inversion, (10) has logarithmic letters at `0` and at roots of unity in `mu_N`. Every fixed homogeneous coefficient of the regularized defect (9) is therefore a finite linear combination of regularized iterated integrals on

\[
\mathbb P^1\setminus(\{0,\infty\}\cup\mu_N).
\tag{34}
\]

Thus it lies in the same classical cyclotomic multiple-polylogarithm/regularized-holonomy setting that bounds PC-347 and PC-348. Goncharov's root-of-unity multiple-polylogarithm framework is the relevant period-class anchor. Enriquez's cyclotomic associators provide a stronger neighboring warning: noncommutative logarithmic holonomies with root-of-unity singularities and distribution structure are already an established subject. Regularized holonomy between tangential base points is likewise standard in KZ/associator theory; for example Alekseev, Naef and Ren, *Generalized Pentagon Equations*, Annales Henri Poincare 26 (2025), 877--894, DOI `10.1007/s00023-024-01523-1`, explicitly treats regularized KZ holonomies with tangential endpoints.

No historical novelty is claimed for cyclotomic reciprocity, Ramanujan sums, Chen signatures, Levy area, tangential-basepoint regularization, or cyclotomic associators. The line-local delta is the exact application to the reciprocity-closed Prime-Circle radial path, especially the closed formulas (12), (21), and (28)--(29).

## 7. Consequence for the RH-facing frontier

The most direct attempt to turn Prime Circle's spatial inversion into a noncommutative analogue of the zeta functional equation now has a sharp first boundary.

At all depths, every commutative readout of the canonical inversion defect is identically trivial. At the first genuinely noncommutative depth, the defect is only a rank-two bivector built from `phi(n)` and elementary radical/Mobius data times `zeta(2)`. Neither channel supplies a spectral variable, a Gamma factor, an `s <-> 1-s` reflection, or a zero-selecting condition. The degree-two structure also survives unchanged in form for non-arithmetic reciprocal controls.

PC-347 already says that every **fixed** higher Chen degree remains in the classical cyclotomic hyperlogarithm algebra. Therefore merely advancing to degree three, four, or any other fixed depth is not a new RH mechanism. What remains genuinely unclassified is an invariant that uses **unbounded Lie depth or conductor-coupled growing depth** while discarding enough of the faithful full signature of PC-348 to become selective, and whose choice is forced by the original roots/refinement geometry rather than inserted as an arbitrary spectral wrapper.

This finding does not rule out that all-depth noncommutative branch. It rules out the natural abelian/determinant channel and shows that the first nonabelian inversion correction is maximally low-rank and classical.

## Audit / falsification tests

This finding must be revised if any of the following fails:

1. cyclotomic reciprocity (2) fails for a shell `n>1`, or `Phi_n(r)` changes sign on the positive radial path so that the real logarithm is not globally defined;
2. the asymptotic closure (5) does not leave endpoint `X_S(1/R)` as in (6);
3. abelianization of the path signature does not equal the exponential of total displacement, invalidating (11)--(13);
4. the straight closing segment has a nonzero limiting contribution to the degree-two area;
5. inversion and integration by parts do not give (21);
6. the Ramanujan expansion (22) or divisor identity (24) does not imply (25)--(26);
7. a shell family produces a degree-two matrix of rank greater than two, contradicting the explicit wedge factorization (29);
8. the regularized higher coefficients require letters outside `0` and `mu_N`, invalidating the cyclotomic prior-art classification.

## Bottom line

The exact interior/exterior symmetry does have a canonical noncommutative completion: close the radial cyclotomic path by the reciprocity-forced totient ray and take its signature. But **the resulting inversion defect has trivial abelianization, determinant one, and a first Lie level of rank at most two with the explicit elementary formula (28)**. Spatial inversion therefore does not acquire a zeta functional equation merely by adding the first layer of path ordering. A surviving Prime-Circle mechanism must live genuinely at unbounded noncommutative depth or in a source-forced conductor-dependent quotient of it.