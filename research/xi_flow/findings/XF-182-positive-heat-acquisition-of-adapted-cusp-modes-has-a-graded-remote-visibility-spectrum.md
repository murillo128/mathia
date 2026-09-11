---
type: theorem
research_line: xi_flow
finding_id: XF-182
status: canonical
---

# XF-182 — Positive-heat acquisition of adapted cusp modes has a graded remote visibility spectrum

**Evidence classification:** `EXACT-DERIVED + SHARP-LINEARIZED + ACQUISITION-CONDITIONING`. XF-181 removes the monomial Vandermonde penalty once the first `m` cusp moments of a known `m`-atom packet are already available: in packet-adapted orthogonal coordinates the local atom-location inverse is infinitesimally isometric. The remaining acquisition caveat can now be quantified sharply. For a fixed-complexity packet of consecutive remote Xi atoms, the `k`th adapted cusp direction has raw positive-heat Jacobi visibility of order `N^{-(k+1)}`. Thus the `m` orthogonal cusp modes form a graded visibility ladder `N^{-1},N^{-2},...,N^{-m}`. The highest mode reproduces the `N^{-m}` moment-cancellation scale behind XF-178, while the full ladder shows where the remote-index penalty actually lives: **not in the algebraic inverse from exact cusp data, but in the forward map from atom motion to unrenormalized positive-heat data**.

## Statement

Fix an integer

\[
m\ge2.
\tag{1}
\]

For an integer `N>=m`, take the consecutive Xi squared radii

\[
\lambda_j=(N+j)^2,
\qquad 1\le j\le m,
\tag{2}
\]

and use the affine normalization of XF-180--XF-181,

\[
A=(N+1)^2,
\qquad
R=(N+m)^2-(N+1)^2,
\qquad
u_j=\frac{\lambda_j-A}{R}.
\tag{3}
\]

Then

\[
0=u_1<\cdots<u_m=1,
\qquad
u_j\longrightarrow\frac{j-1}{m-1}
\quad(N\to\infty).
\tag{4}
\]

Write

\[
a_N:=\frac AR
\sim\frac{N}{2(m-1)}.
\tag{5}
\]

Let `p_0,...,p_(m-1)` be the empirical orthonormal polynomials of XF-181,

\[
\frac1m\sum_{j=1}^m p_k(u_j)p_\ell(u_j)=\delta_{k\ell},
\tag{6}
\]

and define the unit vectors

\[
q_j^{(k)}:=\frac{p_k(u_j)}{\sqrt m},
\qquad
0\le k\le m-1.
\tag{7}
\]

The vectors `q^(0),...,q^(m-1)` form an orthonormal basis of `R^m`. Perturb the normalized squared radii in one adapted direction,

\[
v_j(\varepsilon)=u_j+\varepsilon q_j^{(k)},
\qquad
\mu_j(\varepsilon)=A+Rv_j(\varepsilon).
\tag{8}
\]

For sufficiently small `epsilon`, this preserves positivity and ordering. Let the direct heat defect of this packet be

\[
D_{N,k,\varepsilon}(x)
:=
2\sum_{j=1}^m
\left(
 e^{-\pi\mu_j(\varepsilon)x}
-e^{-\pi\lambda_jx}
\right),
\tag{9}
\]

and let its Jacobi residual be

\[
\mathcal J_{N,k,\varepsilon}(x)
:=
D_{N,k,\varepsilon}(x)
-x^{-1/2}D_{N,k,\varepsilon}(1/x).
\tag{10}
\]

Define the linearized positive-heat response

\[
G_{N,k}(x)
:=
\left.
\frac{\partial}{\partial\varepsilon}
\mathcal J_{N,k,\varepsilon}(x)
\right|_{\varepsilon=0}.
\tag{11}
\]

Then for every fixed `m` and `0<=k<=m-1` there are constants `0<c_(m,k)<=C_(m,k)<infinity` such that, for all sufficiently large `N`,

\[
\boxed{
 c_{m,k}\,a_N^{-(k+1)}
\le
\sup_{x>0}|G_{N,k}(x)|
\le
 C_{m,k}\,a_N^{-(k+1)}.
}
\tag{12}
\]

Equivalently, because of `(5)`,

\[
\boxed{
\sup_{x>0}|G_{N,k}(x)|
=\Theta_{m,k}(N^{-(k+1)}).
}
\tag{13}
\]

The asymptotic constant is explicit. If `gamma_(m,k)>0` is the limiting leading coefficient of `p_k` on the equispaced nodes `0,1/(m-1),...,1`, then

\[
\boxed{
 a_N^{k+1}
 \sup_{x>0}|G_{N,k}(x)|
\longrightarrow
\frac{2\sqrt m}{k!\,\gamma_{m,k}}
\left(\frac{k+1}{e}\right)^{k+1}.
}
\tag{14}
\]

The maximizing heat scale is asymptotically

\[
\boxed{
 x_{N,k}\sim\frac{k+1}{\pi A}
\asymp_m N^{-2}.
}
\tag{15}
\]

Thus the natural remote-atom scale remains `x~N^(-2)`, but each additional adapted packet moment costs one extra factor `N^(-1)`.

There is a finite-sample version. Choose any distinct positive constants

\[
0<c_1<\cdots<c_m
\tag{16}
\]

and sample at

\[
x_\ell=\frac{c_\ell}{\pi A}.
\tag{17}
\]

Let `M_N` be the `m x m` linearized acquisition matrix whose `(ell,k)` entry is `G_(N,k)(x_ell)`, with columns indexed by `k=0,...,m-1`. Then

\[
\boxed{
\|M_N\|_2=\Theta_m(a_N^{-1}),
\qquad
\|M_N^{-1}\|_2=\Theta_m(a_N^m),
\qquad
\kappa_2(M_N)=\Theta_m(a_N^{m-1}).
}
\tag{18}
\]

Hence `m` well-chosen positive heat scales already attain the same worst-direction order as the full continuum of heat data. The absolute local inverse from unrenormalized heat residuals necessarily amplifies the hardest mode by order `N^m`, even though the subsequent cusp-coordinate inverse of XF-181 has condition number one.

## 1. Orthogonality forces exact cancellation of the first `k` heat moments

Because `p_k` is orthogonal to every polynomial of degree below `k`, `(7)` gives

\[
\boxed{
\sum_{j=1}^m q_j^{(k)}u_j^r=0
\qquad(0\le r<k).
}
\tag{19}
\]

At the first surviving degree,

\[
\beta_{N,k}
:=
\sum_{j=1}^m q_j^{(k)}u_j^k
>0.
\tag{20}
\]

Indeed, if `gamma_(N,k)>0` is the leading coefficient of `p_k`, then `t^k=gamma_(N,k)^(-1)p_k(t)` plus a polynomial of degree below `k`. Therefore

\[
\boxed{
\beta_{N,k}=\frac{\sqrt m}{\gamma_{N,k}}.
}
\tag{21}
\]

For fixed `m`, the node vectors in `(4)` stay in a compact uniformly separated family, so `gamma_(N,k)` converges to a finite positive limit and `beta_(N,k)` stays bounded above and below away from zero.

Differentiate `(9)` at `epsilon=0`. With

\[
y:=\pi Rx,
\qquad
a:=\frac AR,
\qquad
S_{N,k}(y):=
\sum_{j=1}^m q_j^{(k)}e^{-u_jy},
\tag{22}
\]

one obtains the exact direct response

\[
\boxed{
G^{\rm dir}_{N,k}(x)
=-2y e^{-ay}S_{N,k}(y).
}
\tag{23}
\]

Using `(19)` to subtract the Taylor polynomial of `e^(-u_j y)` through degree `k-1`, Taylor's remainder gives, for every `y>=0`,

\[
|S_{N,k}(y)|
\le
\frac{\sqrt m}{k!}y^k.
\tag{24}
\]

Consequently,

\[
|G^{\rm dir}_{N,k}(x)|
\le
\frac{2\sqrt m}{k!}
y^{k+1}e^{-ay}.
\tag{25}
\]

The right-hand side is maximized at `y=(k+1)/a`, proving the upper half of the power law in `(12)` for the direct term.

The cancellation is also exactly of order `k`, not higher. From `(20)`,

\[
S_{N,k}(y)
=
\frac{(-1)^k\beta_{N,k}}{k!}y^k
+O_m(y^{k+1})
\qquad(y\to0).
\tag{26}
\]

Take `y=(k+1)/a`. Since `a_N->infinity`, `(23)` and `(26)` give

\[
G^{\rm dir}_{N,k}
\left(\frac{k+1}{\pi A}\right)
=
-\frac{2(-1)^k\beta_{N,k}}{k!}
\left(\frac{k+1}{a}\right)^{k+1}
 e^{-(k+1)}
+O_m(a^{-(k+2)}).
\tag{27}
\]

This supplies the lower bound and the limiting constant in `(14)`.

The key structural point is that the directions which make the XF-181 cusp inverse orthogonal are **the same directions which successively cancel more terms of the finite-scale heat expansion**. Orthogonalization fixes the inverse geometry at the cusp, but it does not make the forward heat profiles equally visible.

## 2. The reciprocal Jacobi image is negligible at the resolving scale

Differentiating the reciprocal term in `(10)` gives

\[
G^{\rm rec}_{N,k}(x)
=
2\pi R x^{-3/2}
 e^{-\pi A/x}
 S_{N,k}(\pi R/x).
\tag{28}
\]

Since `||q^(k)||_2=1`,

\[
|S_{N,k}(t)|\le\sum_j|q_j^{(k)}|\le\sqrt m
\qquad(t\ge0).
\tag{29}
\]

For `0<x<=1` and `N` large,

\[
|G^{\rm rec}_{N,k}(x)|
\le
2\pi R\sqrt m\,x^{-3/2}e^{-\pi A/x}
\le
2\pi R\sqrt m\,e^{-\pi A},
\tag{30}
\]

because `x^(-3/2)e^(-pi A/x)` is increasing on `(0,1]` once `pi A>3/2`. This is smaller than every power of `N`.

Moreover the Jacobi residual obeys

\[
\mathcal J(1/x)=-x^{1/2}\mathcal J(x),
\tag{31}
\]

and the same identity holds after linearization. Therefore values with `x>=1` are controlled by values with `x<=1`. Equations `(25)` and `(30)` prove the global upper bound in `(12)`.

At the resolving scale `(15)`, the reciprocal exponent is of order `-A^2`, so `(28)` is super-polynomially smaller than the direct contribution `(27)`. The lower bound is therefore unaffected. This also shows why the remote visibility law is a genuine forward-heat effect rather than a cancellation between the direct and reciprocal Jacobi images.

## 3. The full adapted basis has visibility ladder `N^-1,...,N^-m`

XF-181 defines the normalized adapted cusp map `Z=m^(-1/2)Y`. Its Jacobian rows are exactly the vectors `(7)`. Hence

\[
D_hZ(0)q^{(k)}=e_k.
\tag{32}
\]

A unit displacement in direction `q^(k)` is therefore, to first order, a **unit change in exactly one adapted cusp coordinate**. Equation `(13)` says that the raw heat data carrying that unit coordinate have size only `N^{-(k+1)}`.

The hierarchy is thus

\[
\boxed{
q^{(0)}:\ N^{-1},
\quad
q^{(1)}:\ N^{-2},
\quad\cdots\quad,
q^{(m-1)}:\ N^{-m}.
}
\tag{33}
\]

The last direction is the linearized counterpart of the high-order packet cancellation in XF-178. XF-178 already showed that a finite nontrivial packet matching the first `m-1` offset moments can have total Jacobi signal `O(N^(-m))`. The new point is not another fixed-topology no-go. It is the **complete first-order acquisition spectrum** after the inverse has been optimally preconditioned: every complexity level appears as one orthogonal mode, and each extra level costs exactly one additional factor `N^(-1)`.

This also explains the relevant heat scale. Sampling at the packet-width scale `x~R^(-1)` would make the common carrier

\[
e^{-\pi Ax}=e^{-\Theta(A/R)}=e^{-\Theta(N)}
\tag{34}
\]

exponentially small. To keep the remote Gaussian visible one must instead use `x~A^(-1)~N^(-2)`. But on that scale the normalized packet width is

\[
\pi Rx=\Theta(R/A)=\Theta(N^{-1}),
\tag{35}
\]

so the `k` cancelled moments impose exactly the factor `N^(-k)` on top of the base `N^(-1)` location response. The polynomial visibility ladder is the optimum balance between common-carrier suppression and packet-moment cancellation.

## 4. `m` positive scales attain the optimal linearized acquisition order

At the sample scales `(17)`, one has

\[
y_\ell=\pi R x_\ell=\frac{c_\ell}{a}.
\tag{36}
\]

Using `(26)` in `(23)` gives, uniformly for fixed `ell` and `k`,

\[
G_{N,k}(x_\ell)
=
-2\frac{(-1)^k\beta_{N,k}}{k!}
 e^{-c_\ell}c_\ell^{k+1}
 a^{-(k+1)}
+O_m(a^{-(k+2)}),
\tag{37}
\]

with the reciprocal term negligible. Thus

\[
M_N
=
\bigl(B+o(1)\bigr)
\operatorname{diag}(a^{-1},a^{-2},\ldots,a^{-m}),
\tag{38}
\]

where, up to nonzero column constants,

\[
B_{\ell k}=e^{-c_\ell}c_\ell^{k+1}.
\tag{39}
\]

Because the `c_ell` are distinct and nonzero, `(39)` is a row-scaled Vandermonde matrix and is invertible. Therefore

\[
\|M_N\|_2\asymp_m a^{-1},
\qquad
\|M_N^{-1}\|_2\asymp_m a^m,
\tag{40}
\]

which proves `(18)`.

This is useful in both directions. The hardest adapted direction has `L^infinity` heat signal only `O(a^(-m))`, so **no inverse measured in unweighted absolute heat error can have a better worst-direction order than `a^m`**. Conversely, the explicit `m`-scale system achieves that order. There is no additional hidden fixed-`m` loss beyond the visibility ladder.

In particular, the remote-index dependence removed by XF-180--XF-181 was genuinely removed from the **cusp inverse**, not from the end-to-end map. The end-to-end factorization is now explicit:

\[
\text{atom displacement}
\xrightarrow{\text{positive heat acquisition}}
\text{adapted cusp information}
\xrightarrow{\text{XF-181 inverse}}
\text{atom displacement},
\tag{41}
\]

and only the first arrow carries the powers of `N`.

## 5. Stress tests and boundary conditions

The simplest check is `m=2`. The normalized nodes are `{0,1}` for every `N`, and XF-181 gives

\[
q^{(0)}=\frac1{\sqrt2}(1,1),
\qquad
q^{(1)}=\frac1{\sqrt2}(-1,1).
\tag{42}
\]

For the antisymmetric direction,

\[
S_{N,1}(y)
=
\frac{e^{-y}-1}{\sqrt2}
=-\frac{y}{\sqrt2}+O(y^2),
\tag{43}
\]

so the direct heat response is

\[
G^{\rm dir}_{N,1}(x)
=
\sqrt2\,y^2e^{-ay}+O(y^3e^{-ay}).
\tag{44}
\]

It is maximized at `y~2/a`, giving `Theta(a^(-2))=Theta(N^(-2))`, exactly as `(13)` predicts and exactly matching the centered two-atom suppression already visible in XF-178.

The perturbation is not artificially small in physical atom coordinates. Since `mu_j=A+R(u_j+epsilon q_j)`,

\[
\left.
\frac{d}{d\varepsilon}\sqrt{\mu_j(\varepsilon)}
\right|_{0}
=
\frac{Rq_j^{(k)}}{2(N+j)}.
\tag{45}
\]

For fixed `m`, `R~2(m-1)N`, so a unit normalized direction corresponds to an `O_m(1)` radial atom displacement as `N->infinity`. The decay in `(13)` is therefore true remote invisibility, not a consequence of shrinking the physical perturbation.

The theorem is **linearized and packet-adapted**. It does not claim a global nonlinear inverse for arbitrary finite displacement, nor does it discover an unknown support window. XF-178 supplies a separate finite-displacement obstruction, while XF-181 controls a local nonlinear neighborhood after exact adapted cusp data are known. The present result isolates the missing forward stage between them.

The norm matters. Multiplying the `k`th mode by `a^(k+1)`, or equivalently using a complexity- and location-dependent source norm, removes the power loss at the formal linear level. That is not a contradiction: it changes the acquisition topology. Any useful quantitative Xi theorem based on such a renormalization must explain why the source supplies the correspondingly shrinking absolute precision rather than merely hiding the `N^(k+1)` amplification in the definition of the observable.

## Prior-art and novelty audit

Severe ill-posedness of inverse Laplace transformation and conditioning issues for exponential-sum/Prony recovery are classical. A focused audit found the expected general literature, including analyses of inverse Laplace instability and Prony-type exponential reconstruction. None of those results is load-bearing here: `(12)--(18)` follow directly from the exact finite Xi packet, the XF-181 orthogonal basis, and elementary Taylor/Vandermonde estimates. `SOURCES.md` therefore does not require a new dependency.

No novelty claim is made for orthogonal polynomials, moment cancellation, inverse Laplace ill-posedness, or Vandermonde sampling. The line-specific result is the exact **graded remote visibility law** for the adapted Jacobi cusp coordinates of consecutive Xi theta atoms, together with the order-sharp `m`-scale acquisition matrix.

## Consequence for `xi_flow`

XF-179--XF-181 separate information depth from coordinate conditioning. XF-182 now separates coordinate conditioning from **observable acquisition** quantitatively. For fixed packet complexity, the cusp inverse can be made index-uniform and condition-one, yet the raw heat acquisition map still presents its complexity modes at powers `N^(-1),...,N^(-m)`. The highest power is not a basis artifact; it is the forward manifestation of moment cancellation already exposed globally by XF-178.

The next source-side target should therefore not be another preconditioner for the exact cusp moments. It should be a relative or multiscale acquisition mechanism that compensates the known Gaussian/packet geometry **before** absolute errors are compared, while remaining source-faithful and compatible with zero-sensitive transition estimates. An alternative is an arithmetic/modular theorem that bounds the effective packet complexity which can actually occur. Without one of those two ingredients, exact adapted cusp recovery remains quantitatively disconnected from finite positive-heat control.