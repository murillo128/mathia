---
type: theorem
research_line: xi_flow
finding_id: XF-183
status: canonical
---

# XF-183 — Packet-relative heat acquisition removes remote mode loss but exposes an exponential normalization barrier

**Evidence classification:** `EXACT-RELATIVE-ACQUISITION + UNIFORM-LINEAR-INVERSE + NORMALIZATION-BARRIER`. XF-182 shows that, for a fixed `m`-atom consecutive Xi packet at remote index `N`, the packet-adapted cusp directions have raw positive-heat visibility `N^-1,N^-2,...,N^-m`. That ladder is not an intrinsic loss of the finite packet geometry. If the heat response is divided by the heat mass of the same reference packet and sampled at the packet-width scale `x~R^-1~N^-1`, the complete `m`-dimensional linearized location map has condition number bounded independently of `N`. The remote factor cancels exactly. The cost is equally sharp: the reference packet itself has size `exp(-Theta_m(N))` at those scales, so extracting the relative observable from an additive absolute heat estimate requires exponentially small absolute error. Thus relative normalization can remove the polynomial mode ladder only by changing the acquisition topology; a useful Xi source theorem must supply a genuinely relative or modular tail identity, not merely divide an absolute error bound by an exponentially small known reference.

## Statement

Fix an integer

\[
m\ge2.
\tag{1}
\]

For `N>=m`, take the consecutive Xi squared radii

\[
\lambda_j=(N+j)^2,
\qquad 1\le j\le m,
\tag{2}
\]

and retain the affine packet normalization of XF-180--XF-182,

\[
A=(N+1)^2,
\qquad
R=(N+m)^2-(N+1)^2,
\qquad
u_j=\frac{\lambda_j-A}{R},
\tag{3}
\]

so that

\[
0=u_1<\cdots<u_m=1,
\qquad
u_j\longrightarrow\frac{j-1}{m-1},
\tag{4}
\]

and

\[
a_N:=\frac AR
=\frac{(N+1)^2}{(m-1)(2N+m+1)}
=\frac{N}{2(m-1)}+O_m(1).
\tag{5}
\]

Let `q^(0),...,q^(m-1)` be the orthonormal packet-adapted location directions of XF-181--XF-182. Thus, with

\[
S_{N,k}(y):=\sum_{j=1}^m q_j^{(k)}e^{-u_jy},
\qquad
B_N(y):=\sum_{j=1}^m e^{-u_jy},
\tag{6}
\]

XF-182 gives the direct linearized Jacobi response

\[
G^{\rm dir}_{N,k}(x)
=-2y e^{-a_Ny}S_{N,k}(y),
\qquad
y=\pi Rx.
\tag{7}
\]

Define the positive reference heat mass of the same packet by

\[
P_N(x):=2\sum_{j=1}^m e^{-\pi\lambda_jx}.
\tag{8}
\]

At the packet-width parametrization

\[
x=\frac{y}{\pi R},
\tag{9}
\]

one has the exact factorization

\[
\boxed{
P_N\!\left(\frac{y}{\pi R}\right)
=2e^{-a_Ny}B_N(y).
}
\tag{10}
\]

Let `G_(N,k)` denote the full linearized Jacobi residual of XF-182, including the reciprocal image, and define the packet-relative response

\[
\mathscr R_{N,k}(y)
:=
\frac{G_{N,k}(y/(\pi R))}
{P_N(y/(\pi R))}.
\tag{11}
\]

For every fixed compact interval `0<y_-<=y<=y_+<infinity`,

\[
\boxed{
\mathscr R_{N,k}(y)
=-y\frac{S_{N,k}(y)}{B_N(y)}
+O_{m,y_-,y_+}(e^{-c_mN^3}).
}
\tag{12}
\]

The direct part of `(12)` is exact: the common remote factor `e^(-a_N y)` cancels. The error comes only from the reciprocal Jacobi image.

There is a full finite-sample version. Choose any fixed distinct positive numbers

\[
0<y_1<\cdots<y_m<\infty.
\tag{13}
\]

Let `\mathscr M_N` be the `m x m` matrix with

\[
(\mathscr M_N)_{\ell k}
=
\mathscr R_{N,k}(y_\ell),
\qquad
1\le\ell\le m,
\quad
0\le k\le m-1.
\tag{14}
\]

Then there are constants

\[
0<c_m\le C_m<\infty,
\tag{15}
\]

which may depend on the chosen sample points but not on `N`, such that for all sufficiently large `N`,

\[
\boxed{
c_m\|z\|_2
\le
\|\mathscr M_N z\|_2
\le
C_m\|z\|_2
\qquad(z\in\mathbb R^m).
}
\tag{16}
\]

In particular,

\[
\boxed{
\|\mathscr M_N\|_2=O_m(1),
\qquad
\|\mathscr M_N^{-1}\|_2=O_m(1),
\qquad
\kappa_2(\mathscr M_N)=O_m(1).
}
\tag{17}
\]

Thus the entire graded `N^-1,...,N^-m` visibility ladder of XF-182 disappears from the **relative** packet acquisition map.

The normalization cost is explicit. Since `0<=u_j<=1`,

\[
me^{-y}\le B_N(y)\le m,
\tag{18}
\]

and therefore for every fixed `y>0`,

\[
\boxed{
P_N\!\left(\frac{y}{\pi R}\right)
=
\exp\!\left(
-\frac{y}{2(m-1)}N+O_{m,y}(1)
\right).
}
\tag{19}
\]

Consequently an additive acquisition error `eta_N` in the numerator of `(11)` produces relative error of order

\[
\boxed{
|\eta_N|
\exp\!\left(
\frac{y}{2(m-1)}N+O_{m,y}(1)
\right).
}
\tag{20}
\]

Any argument entering `(11)` only through an absolute additive heat estimate therefore needs exponentially small absolute precision at fixed packet-width scale. The uniform relative inverse `(17)` is useful only if the source supplies relative information before that division, or supplies an exact structural operation that isolates the remote packet/tail without paying the subtraction error in `(20)`.

## 1. Relative normalization cancels the remote carrier exactly

Equation `(7)` and the factorization `(10)` immediately give

\[
\frac{G^{\rm dir}_{N,k}(y/(\pi R))}
{P_N(y/(\pi R))}
=
-y\frac{S_{N,k}(y)}{B_N(y)}.
\tag{21}
\]

No asymptotic estimate is used in this cancellation. The quantity on the right depends on the normalized packet geometry `u_1,...,u_m` and on the selected adapted direction, but it contains no factor `a_N=A/R`. For fixed `m`, the node vector remains in a compact uniformly separated family and converges to the equispaced configuration in `(4)`.

The reciprocal Jacobi image does not spoil this relative limit. XF-182 gives

\[
G^{\rm rec}_{N,k}(x)
=
2\pi R x^{-3/2}e^{-\pi A/x}
S_{N,k}(\pi R/x).
\tag{22}
\]

At `x=y/(pi R)`, use `|S_(N,k)|<=sqrt(m)` and `(18)` to obtain

\[
\left|
\frac{G^{\rm rec}_{N,k}(y/(\pi R))}
{P_N(y/(\pi R))}
\right|
\le
C_{m,y_-,y_+}R^{5/2}
\exp\!\left(
-\frac{\pi^2AR}{y}+a_Ny
\right).
\tag{23}
\]

For fixed `m`, `A~N^2`, `R~2(m-1)N`, and `a_N~N/[2(m-1)]`. The exponent in `(23)` is `-Theta_m(N^3)`, uniformly on every fixed compact positive `y` interval. This proves `(12)`. At the relative resolving scale the reciprocal image is far smaller than the already exponentially small direct packet carrier.

## 2. A fixed `m`-sample relative bank is uniformly invertible in the remote index

It is clearer first to use the normalized atom-displacement coordinates themselves. For a perturbation vector `h=(h_1,...,h_m)`, the direct derivative of the relative response at sample `y` is

\[
\mathcal A_N(y)h
=
-y\,
\frac{\sum_{j=1}^m h_j e^{-u_jy}}
{B_N(y)}.
\tag{24}
\]

At the sample points `(13)`, the corresponding matrix is

\[
C_N
=
-\operatorname{diag}\!\left(
\frac{y_1}{B_N(y_1)},\ldots,
\frac{y_m}{B_N(y_m)}
\right)E_N,
\tag{25}
\]

where

\[
(E_N)_{\ell j}=e^{-u_jy_\ell}.
\tag{26}
\]

The matrix `E_N` is nonsingular whenever the `u_j` and the `y_ell` are distinct. This can be proved without importing a reconstruction theorem. If a nontrivial linear combination of `m` exponentials

\[
f(y)=\sum_{j=1}^m c_je^{-u_jy}
\tag{27}
\]

had `m` distinct positive zeros, multiply by `e^(u_1 y)` and apply Rolle's theorem. Its derivative is a nontrivial combination of only `m-1` exponentials and would have at least `m-1` distinct zeros. Induction from `m=1` gives a contradiction. Hence evaluation at `m` distinct points has trivial kernel.

For fixed `m`, the possible Xi node vectors `u(N)` together with their `N=infinity` limit form a compact subset of the distinct-node region. The diagonal factors in `(25)` are also bounded above and below away from zero by `(18)`. Singular values depend continuously on the matrix entries, so compactness gives

\[
0<c_m
\le
s_{\min}(C_N)
\le
s_{\max}(C_N)
\le C_m<\infty
\tag{28}
\]

uniformly in `N`.

Passing from atom coordinates to the XF-181 adapted coordinates multiplies on the right by the orthogonal matrix whose columns are `q^(0),...,q^(m-1)`. This preserves all singular values. Finally `(23)` perturbs the matrix by `e^(-Theta_m(N^3))`, so `(28)` survives for the full Jacobi response and proves `(16)--(17)`.

This is stronger than showing that each mode can be detected somewhere. A **single fixed bank of `m` packet-width heat scales** recovers every linearized adapted mode with remote-index-uniform conditioning. The condition may still deteriorate with `m`; the theorem does not remove the sharp complexity-depth requirement of XF-179 or the unbounded-complexity obstruction of XF-178.

## 3. The raw and relative observations sit on opposite sides of an exact scale tradeoff

XF-182's polynomial ladder is recovered by asking that the common remote Gaussian remain only polynomially small. The adapted direction `q^(k)` satisfies

\[
S_{N,k}(y)
=
\frac{(-1)^k\beta_{N,k}}{k!}y^k
+O_m(y^{k+1}),
\qquad
0<c_{m,k}\le\beta_{N,k}\le C_{m,k}.
\tag{29}
\]

Together with `(7)`, for any fixed `theta>0` and

\[
y=a_N^{-\theta},
\tag{30}
\]

one obtains

\[
|G^{\rm dir}_{N,k}|
=
\Theta_{m,k}\!\left(
 a_N^{-\theta(k+1)}
 e^{-a_N^{1-\theta}}
\right)
\tag{31}
\]

whenever `N` is large. Three regimes are immediate.

At `theta=1`, the common carrier is `e^(-1)` and `(31)` is `Theta(a_N^(-(k+1)))`, exactly the optimal raw visibility scale of XF-182, corresponding to `x~A^-1~N^-2`. If `0<theta<1`, the packet begins to resolve more of its internal geometry, but the common carrier contributes `exp(-a_N^(1-theta))`, smaller than every inverse power. If `theta>1`, the carrier ceases to be a problem, but the packet is sampled at an even smaller normalized width and the moment cancellation produces the worse power `a_N^(-theta(k+1))`.

To keep the internal packet scale noncollapsed, one needs `y=Theta(1)`, equivalently

\[
x=\Theta(R^{-1})=\Theta_m(N^{-1}).
\tag{32}
\]

Then the normalized matrix is uniformly conditioned by `(17)`, while the absolute packet mass is `exp(-Theta_m(N))` by `(19)`. Thus there is no unnormalized positive-heat scale in this packet model that simultaneously gives order-one internal geometric resolution and retains a merely polynomial absolute carrier. The raw `N^(-(k+1))` ladder and the relative exponential normalization are two sides of the same Gaussian scale tradeoff, not two independent defects.

## 4. Exact theta-tail peeling would bypass the algebraic ladder, but approximate peeling inherits the exponential barrier

The preceding normalization is packet-adapted and assumes the relevant remote reference packet is already identified. It is useful to state what happens if one tries to realize it from the actual theta source by removing a lower prefix.

Let

\[
T_N(x)
:=2\sum_{r\ge1}e^{-\pi(N+r)^2x}
\tag{33}
\]

be the positive theta tail starting with the first atom of the packet. At `x=y/(pi R)`, factor the same remote carrier:

\[
\frac12e^{a_Ny}T_N\!\left(\frac{y}{\pi R}\right)
=
\sum_{r\ge1}
\exp\!\left(
-y\frac{(N+r)^2-(N+1)^2}{R}
\right).
\tag{34}
\]

For each fixed `r`,

\[
\frac{(N+r)^2-(N+1)^2}{R}
\longrightarrow
\frac{r-1}{m-1},
\tag{35}
\]

and the summands admit a geometric majorant depending only on fixed `m` and `y>0`. Hence dominated convergence gives

\[
\boxed{
\frac12e^{a_Ny}T_N\!\left(\frac{y}{\pi R}\right)
\longrightarrow
\frac{1}{1-e^{-y/(m-1)}}.
}
\tag{36}
\]

So an **exactly isolated theta tail** naturally carries order-one relative information on the packet-width scale. This is the positive side of the result: a modular or arithmetic identity that provides such a tail relatively could in principle cross the XF-182 acquisition ladder without asking for `N^-m` mode-by-mode absolute precision.

But ordinary additive prefix subtraction does not supply that interface stably. The full positive theta mass at `x~N^-1` is `Theta_m(sqrt(N))` by the Jacobi theta transformation, while `(19)` and `(36)` give

\[
T_N\!\left(\frac{y}{\pi R}\right)
=
\exp(-\Theta_m(N)).
\tag{37}
\]

Therefore

\[
\boxed{
\frac{T_N(y/(\pi R))}
{2\sum_{n\ge1}e^{-\pi n^2y/(\pi R)}}
=
\Theta_{m,y}\!\left(
N^{-1/2}e^{-a_Ny}
\right).
}
\tag{38}
\]

If the lower prefix is known only through an additive approximation to the full theta heat, isolating the tail requires relative accuracy at the exponentially small scale `(38)`. Exact symbolic subtraction is mathematically legitimate, but an inequality with only polynomial or power-saving additive control loses the tail. This is precisely the distinction the live source problem must respect: **relative tail structure can help; post hoc division of an absolute estimate cannot.**

## Stress tests and boundaries

The result is deliberately local and complexity-matched. The packet size `m` is fixed, the packet location and consecutive reference support are known, and the theorem concerns the linearized location map. Uniformity is in the remote index `N`, not in `m`. It does not discover an unknown support window, prove a global nonlinear inverse for arbitrary finite atom surgery, or control an infinite deformation.

There is no contradiction with XF-178. That finding lets packet complexity grow to cancel every fixed bank of power-weighted Jacobi observables. Here the number of relative samples grows with the fixed packet complexity and the sampling/normalization is packet-adapted. Nor is there a contradiction with XF-182: `(31)` recovers its raw optimum and explains why moving to the geometrically resolving scale necessarily makes the absolute carrier exponentially small.

The normalization barrier is an acquisition statement, not an information-theoretic impossibility theorem. Exact arithmetic or modular identities may expose a remote tail **relatively**, in which case dividing by its natural scale is legitimate. What is ruled out is treating a relative normalization as free when the only admitted source input is an additive absolute error larger than the packet mass. A future Xi theorem must specify which of those two information models it actually has.

Nothing here yields an upper bound on the de Bruijn--Newman constant, real-rootedness at `t=0`, or RH. The transition-sensitive step remains downstream: even a stable source reconstruction must still be connected to a quantity that a hypothetical positive-`Lambda` transition is forced to disturb.

## Prior-art and novelty audit

Exponential-sum reconstruction, Chebyshev systems of exponentials, total positivity of exponential kernels, and severe ill-posedness of inverse Laplace transformation are classical. A focused literature audit found the expected general inverse-Laplace and exponential-reconstruction conditioning literature. None is load-bearing: the uniform inverse `(16)--(17)` follows from the elementary zero-count argument for `(27)` plus compactness, while the normalization law `(19)`, scale tradeoff `(31)`, and theta-tail comparison `(36)--(38)` follow directly from the Xi square packet and Jacobi theta scaling already present in this line.

The line-specific contribution is the exact placement of the XF-182 graded visibility law inside this tradeoff. The same packet has a remote-index-uniform relative acquisition map at `x~N^-1`, but its denominator is `exp(-Theta(N))`; the raw polynomial optimum at `x~N^-2` is therefore not a bad choice of coordinates but the best regime that avoids exponential common-carrier suppression. No new external source is required in `SOURCES.md` for this specialization.

## Consequence for the Xi-flow frontier

The source-side gate after XF-182 can now be stated more sharply. Further preconditioning of the finite packet inverse is unnecessary, and merely defining a location-dependent relative norm is also insufficient. The next useful source theorem must provide one of two genuinely new inputs: an arithmetic/modular mechanism that isolates remote theta tails or packet modes **relatively before additive error is introduced**, or a structural restriction that prevents high-complexity remote packet motion from being an admissible Xi-source defect.

A theorem giving only polynomially small additive error for the full positive heat trace cannot exploit the uniformly conditioned relative bank `(17)`, because the relevant packet denominator is exponentially smaller. Conversely, a true relative tail identity would evade the `N^-m` absolute ladder rather than merely renaming it. This separates the remaining source question from both finite-dimensional inverse conditioning and generic inverse-Laplace ill-posedness.