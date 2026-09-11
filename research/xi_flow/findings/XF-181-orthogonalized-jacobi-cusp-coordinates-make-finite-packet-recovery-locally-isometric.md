---
type: theorem
research_line: xi_flow
finding_id: XF-181
status: canonical
---

# XF-181 — Orthogonalized Jacobi cusp coordinates make finite-packet recovery locally isometric

**Evidence classification:** `CLASSICAL-PRECONDITIONING + EXACT-DERIVED + LOCAL-ISOMETRY`. XF-180 shows that affine recentering removes the remote index from the finite-packet moment inversion, but its monomial coordinates still have an inverse norm growing at least exponentially in packet complexity. That exponential lower bound is not intrinsic to the local algebraic inverse problem. For any known `m`-atom reference packet, one can orthogonalize polynomials against the empirical reference nodes and integrate that basis once. The resulting `m` observables are exact linear combinations of the same first `m` centered Jacobi cusp derivatives used in XF-180, so they consume no additional jet depth. Their location Jacobian is, after one scalar normalization, exactly orthogonal. For every fixed `m`, consecutive remote Xi packets therefore admit a neighborhood with bi-Lipschitz constants independent of the remote index. Complexity remains in the required depth, in the nonlinear neighborhood size, and potentially in the cost of extracting the adapted cusp observables from finite positive heat scales.

## Statement

Retain the notation of XF-180. Let

\[
0\le u_1<\cdots<u_m\le1,
\qquad
v_j=u_j+h_j,
\tag{1}
\]

be the normalized reference and moved squared radii, and let

\[
\mathcal C_\ell
=
\sum_{j=1}^m v_j^\ell-
\sum_{j=1}^m u_j^\ell,
\qquad 1\le\ell\le m,
\tag{2}
\]

be the centered normalized Jacobi cusp data supplied exactly by XF-180.

Put the empirical inner product

\[
\langle f,g\rangle_u
:=
\frac1m\sum_{j=1}^m f(u_j)g(u_j).
\tag{3}
\]

Because the nodes are distinct, there is a unique real orthonormal polynomial family

\[
p_0,p_1,\ldots,p_{m-1},
\qquad
\deg p_k=k,
\tag{4}
\]

with positive leading coefficients, satisfying

\[
\frac1m\sum_{j=1}^m p_k(u_j)p_\ell(u_j)=\delta_{k\ell}.
\tag{5}
\]

Define the antiderivatives

\[
Q_k(t):=\int_0^t p_k(s)\,ds,
\qquad 0\le k\le m-1,
\tag{6}
\]

and the adapted cusp coordinates

\[
\boxed{
Y_k(v;u)
:=
\sum_{j=1}^m
\bigl(Q_k(v_j)-Q_k(u_j)\bigr).
}
\tag{7}
\]

Then the following hold.

First, `(7)` uses exactly the same cusp depth as XF-179--XF-180. If

\[
Q_k(t)=\sum_{\ell=1}^{k+1}a_{k\ell}t^\ell,
\tag{8}
\]

then

\[
\boxed{
Y_k=\sum_{\ell=1}^{k+1}a_{k\ell}\mathcal C_\ell.
}
\tag{9}
\]

The coefficient matrix in `(9)` is lower triangular with nonzero diagonal, because `Q_k` has degree `k+1`. Hence the vector `(Y_0,...,Y_{m-1})` contains exactly the same algebraic information as `(mathcal C_1,...,mathcal C_m)`. In particular,

\[
Y_0=\cdots=Y_{m-1}=0
\quad\Longleftrightarrow\quad
\mathcal C_1=\cdots=\mathcal C_m=0,
\tag{10}
\]

so XF-179's exact `m`-versus-`m-1` identification threshold is unchanged.

Second, let

\[
P_{kj}:=p_k(u_j),
\qquad 0\le k\le m-1,
\quad 1\le j\le m.
\tag{11}
\]

The derivative of the adapted map at the reference packet is

\[
\boxed{
D_hY(0)=P.
}
\tag{12}
\]

Equation `(5)` gives

\[
PP^T=mI_m.
\tag{13}
\]

Since `P` is square, also `P^TP=mI_m`. Therefore, after defining

\[
Z:=m^{-1/2}Y,
\tag{14}
\]

one has

\[
\boxed{
D_hZ(0)=m^{-1/2}P\in O(m),
}
\tag{15}
\]

and hence

\[
\boxed{
\|D_hZ(0)h\|_2=\|h\|_2,
\qquad
\kappa_2(D_hZ(0))=1.
}
\tag{16}
\]

Thus the exponential inverse lower bound in XF-180 is a property of the monomial power-moment coordinates, not an unavoidable infinitesimal conditioning law for a known finite packet.

There is also a quantitative nonlinear neighborhood. For `rho>0` define

\[
B_{u,\rho}
:=
\sup_{\substack{1\le j\le m\\|t-u_j|\le\rho}}
\left(
\frac1m\sum_{k=0}^{m-1}|p_k'(t)|^2
\right)^{1/2}.
\tag{17}
\]

Whenever `||h||_infinity<=rho`, Taylor's theorem in integral form gives

\[
\boxed{
\|Z(u+h;u)-m^{-1/2}Ph\|_2
\le
\frac{B_{u,\rho}}2\|h\|_2^2.
}
\tag{18}
\]

Consequently,

\[
\boxed{
\left(1-\frac{B_{u,\rho}}2\|h\|_2\right)\|h\|_2
\le
\|Z(u+h;u)\|_2
\le
\left(1+\frac{B_{u,\rho}}2\|h\|_2\right)\|h\|_2.
}
\tag{19}
\]

For example, if `B_(u,rho)||h||_2<=1`, the adapted defect lies between one half and three halves of the normalized displacement. This is genuine local coercivity, not merely nonsingularity of a Jacobian.

For the consecutive Xi packet

\[
\lambda_j=(N+j)^2,
\qquad 1\le j\le m,
\tag{20}
\]

with the affine normalization of XF-180,

\[
A=(N+1)^2,
\qquad
R=(N+m)^2-(N+1)^2,
\qquad
u_j=\frac{\lambda_j-A}{R},
\tag{21}
\]

fix `m>=2` and allow `N>=m`. XF-180 proves

\[
\min_{j\ne k}|u_j-u_k|\ge\frac1{2(m-1)}.
\tag{22}
\]

The family of node vectors `(u_1,...,u_m)` obtained from `N>=m`, together with its `N=infinity` limit, is compact and remains in the distinct-node region. The orthonormal polynomial coefficients and the derivative envelope `(17)` depend continuously on those nodes. Hence there are constants `rho_m>0` and `B_m<infinity`, depending only on `m`, such that `(18)--(19)` hold with `B_(u,rho_m)<=B_m` for every `N>=m`. The local adapted inverse can therefore be chosen uniformly in the remote index.

## 1. The adapted coordinates are exact Jacobi cusp observables

Equation `(9)` is not a new source assumption. XF-180 gives, for every `ell>=1`,

\[
\mathcal C_\ell(A,R)
=
\frac{1}{2(-\pi R)^\ell}
\left[(\partial_x+\pi A)^\ell\mathcal J_\rho(x)\right]_{x=0}.
\tag{23}
\]

Introduce the dimensionless centered cusp operator

\[
\mathcal T_{A,R}
:=-\frac{\partial_x+\pi A}{\pi R}.
\tag{24}
\]

Since `Q_k(0)=0`, `(8)--(9)` can be written directly as

\[
\boxed{
Y_k
=
\frac12
\left[Q_k(\mathcal T_{A,R})\mathcal J_\rho\right]_{x=0}.
}
\tag{25}
\]

Thus every orthogonalized coordinate is one polynomial differential observable of order at most `k+1`. The reciprocal Jacobi image is flat at the cusp, exactly as in XF-179--XF-180, so no hidden reciprocal term enters `(25)`.

The depth budget is optimal in the same sense as before. The collection `Q_0,...,Q_(m-1)` spans the polynomials with zero constant term and degree at most `m`, because its degrees are `1,...,m` with nonzero leading coefficients. Hence `(25)` is merely an invertible complexity-matched change of coordinates inside the sharp `m`-dimensional cusp information already identified by XF-179. It does not evade the exact `m-1` cancellation obstruction by adding extra data.

## 2. Orthogonality diagonalizes the location Jacobian

Differentiate `(7)` in the displacement vector. Since `Q_k'=p_k`,

\[
\frac{\partial Y_k}{\partial h_j}(0)
=p_k(u_j),
\tag{26}
\]

which proves `(12)`. Equation `(5)` says precisely that the rows of `P/sqrt(m)` are orthonormal. Because there are `m` rows and `m` columns, they form an orthonormal basis of `R^m`, proving `(15)--(16)`.

This construction should be compared with XF-180's normalized monomial data

\[
s_k=\sum_j u_j^k h_j+O(\|h\|^2).
\tag{27}
\]

Those coordinates use the evaluation matrix of the monomials `1,t,...,t^(m-1)`, whose inverse is Vandermonde and can be exponentially ill-conditioned. The present coordinates replace that basis by its orthonormalization **with respect to the actual reference nodes**, then integrate once so that the derivative of the nonlinear atom-location map evaluates the orthonormal basis itself. In Euclidean norm the linearized inverse is therefore exactly isometric.

The fact that an orthogonal polynomial basis can dramatically improve conditioning relative to raw moments is classical modified-moment numerical analysis. In particular, Walter Gautschi's *On the Construction of Gaussian Quadrature Rules from Modified Moments*, Mathematics of Computation 24 (1970), 245--260, DOI `10.1090/S0025-5718-1970-0285117-6`, explicitly contrasts progressively ill-conditioned power moments with much better conditioned orthogonal-polynomial modified moments. Later work of Gautschi and others develops the sensitivity theory further. No novelty is claimed here for modified moments, Gram--Schmidt orthogonalization, or polynomial preconditioning.

The Xi-flow-specific point is `(25)`: the affine-recentered Jacobi cusp bridge makes the **integrated discrete orthogonal basis itself** available as exact source observables of the moved squared theta atoms, with no depth increase beyond the sharp `m` derivatives.

## 3. The nonlinear error is quadratic in displacement

For each `j`, write the contribution of the `j`th atom to `(7)` as

\[
Q_k(u_j+h_j)-Q_k(u_j)
=
p_k(u_j)h_j
+
\int_0^{h_j}
\bigl(p_k(u_j+s)-p_k(u_j)\bigr)\,ds.
\tag{28}
\]

Divide the vector in `k` by `sqrt(m)`. For `|h_j|<=rho`, the Euclidean norm of the second term contributed by this atom is bounded by

\[
\int_0^{|h_j|}
|s|
\sup_{|t-u_j|\le\rho}
\left(\frac1m\sum_{k=0}^{m-1}|p_k'(t)|^2\right)^{1/2}ds
\le
\frac{B_{u,\rho}}2h_j^2.
\tag{29}
\]

Summing over `j` and using `sum_j h_j^2=||h||_2^2` proves `(18)`. Combining `(18)` with the exact isometry `(16)` gives `(19)`.

This estimate also identifies where packet complexity can return. The derivative envelope `B_(u,rho)` can grow with `m`, and the radius on which the quadratic remainder is dominated can shrink accordingly. XF-181 therefore does **not** claim a complexity-uniform nonlinear inverse as `m->infinity`. It shows something narrower but decisive for the interpretation of XF-180: exponential monomial Vandermonde conditioning is not already forced at first order, and for every fixed packet complexity the local reconstruction constants can be made uniform in the remote Xi index.

## 4. Consecutive remote Xi packets have a uniform fixed-complexity neighborhood

For `(20)--(21)`, XF-180 gives `u_1=0`, `u_m=1`, the separation bound `(22)`, and

\[
u_j\longrightarrow\frac{j-1}{m-1}
\qquad(N\to\infty).
\tag{30}
\]

For fixed `m`, the set of all these node vectors is therefore contained in a compact subset of the ordered, uniformly separated configuration space. The discrete Gram matrix of `1,t,...,t^(m-1)` is positive definite there, so its Gram--Schmidt/Cholesky orthonormalization varies continuously. The coefficients of the `p_k` and their derivatives on any fixed small neighborhood of `[0,1]` are consequently uniformly bounded over `N>=m`.

Choose, for example, any `rho_m` strictly below one quarter of the separation lower bound in `(22)`. Compactness then gives a finite `B_m` dominating `(17)` for all remote indices. Equations `(18)--(19)` show that sufficiently small normalized atom displacement is detected with constants depending on `m` alone.

The simplest sanity check is `m=2`. The normalized reference nodes are exactly `{0,1}` for every `N`. One may take

\[
p_0(t)=1,
\qquad
p_1(t)=2t-1,
\tag{31}
\]

so

\[
Q_0(t)=t,
\qquad
Q_1(t)=t^2-t.
\tag{32}
\]

Hence

\[
Y_0=\mathcal C_1,
\qquad
Y_1=\mathcal C_2-\mathcal C_1,
\tag{33}
\]

and the normalized Jacobian is

\[
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
-1&1
\end{pmatrix},
\tag{34}
\]

which is exactly orthogonal. The remote lattice index never appears.

## 5. Stress tests, prior-art boundary, and remaining gate

The basis is **template-adapted**. The reference nodes must be known in order to construct the empirical orthogonal polynomials. This is appropriate for finite surgery relative to the known Xi square lattice, but it does not solve model selection for an unknown support window or an infinite deformation.

The conditioning improvement is also tied to the adapted measurement coordinates. If one first measures the raw monomial cusp derivatives with independent absolute errors and only afterwards forms `(9)`, the coefficient transform can amplify those errors. Likewise, estimating the high-order differential polynomial `(25)` from values of `mathcal J_rho(x)` at positive `x` may be severely ill-conditioned. Orthogonalizing the algebraic inverse does not make differentiation at the modular cusp a bounded operation.

This is consistent with the classical modified-moment literature: the choice of basis can improve one stage of a moment problem while the generation of accurate modified moments remains a separate numerical question. The prior-art search found no need for a new load-bearing theorem beyond this classical conditioning principle; all identities `(7)--(19)` are elementary consequences of the exact Jacobi-to-moment bridge already established in XF-180.

Node collision remains another genuine boundary. As distinct reference nodes approach one another, the empirical polynomial coefficients and the derivative envelope in `(17)` can deteriorate even though `(15)` remains formally orthogonal after renormalizing the basis. The cost is then hidden in constructing or observing the adapted coordinates. Consecutive Xi packets avoid this particular degeneration at fixed `m` because of `(22)`.

Finally, nothing here produces an upper bound on the de Bruijn--Newman constant or a zero-transition theorem. It is a source-side finite-packet conditioning result. The exact `m`-depth requirement from XF-179 still grows with packet complexity, and an infinite atomwise deformation still outruns every fixed depth.

## Consequence for the Xi-flow frontier

The branch left open explicitly by XF-180 can now be separated more cleanly. Better-conditioned complexity-matched coordinates **do exist**: after orthogonalizing against the known reference packet and integrating once, the centered Jacobi cusp map has condition number one at the reference configuration and a fixed-complexity neighborhood whose constants are uniform in remote index.

Therefore the exponential lower bound in XF-180 should not be treated as an intrinsic local complexity barrier of finite atom recovery. What remains load-bearing is one of the following stronger difficulties: control how the nonlinear radius and derivative envelope grow with `m`; estimate the adapted polynomial cusp observables from finite positive heat scales without losing the gain in coefficient/differentiation amplification; or derive an Xi-specific law that bounds the effective packet complexity that must be resolved. Those are now sharper targets than further optimization of the monomial Vandermonde inverse.