---
type: theorem
research_line: xi_flow
finding_id: XF-186
status: canonical
---

# XF-186 — Holomorphic packet banks are uniformly bi-Lipschitz on a lattice-scale nonlinear cell

**Evidence classification:** `CLASSICAL-FEJER/FOURIER-SEPARATION + EXACT-XI/JACOBI-GEOMETRY + UNIFORM-NONLINEAR-PACKET-COERCIVITY`. XF-185 shows that a known consecutive Xi packet with `2<=m<=N` is uniformly observable after linearization by a Fejer-overcomplete bank of complex Jacobi samples. The remaining local question is whether nonlinear inversion reintroduces a condition-number loss when all `m` atom locations move simultaneously. It does not on the natural lattice cell. For every fixed right-half-plane parameter `alpha>0`, the same bank is uniformly bi-Lipschitz on a normalized cube of radius `kappa_alpha/m`, with constants independent of both the remote index `N` and packet complexity `m`. In physical lattice coordinates that cube contains displacements of fixed size independent of `N,m`. Thus the XF-185 linear frame is not merely infinitesimally well conditioned: it gives a genuine nonlinear coordinate chart for constant-size local perturbations of every atom in a known packet.

## Statement

Retain the notation and sampling bank of XF-185. Thus

\[
\lambda_j=(N+j)^2,\qquad 1\le j\le m,\qquad 2\le m\le N,
\]

\[
A=(N+1)^2,\qquad
R=(N+m)^2-(N+1)^2=(m-1)(2N+m+1),
\]

\[
u_j=\frac{\lambda_j-A}{R},\qquad a=\frac AR.
\]

For a real normalized displacement vector `h=(h_1,...,h_m)`, put

\[
\mu_j(h)=A+R(u_j+h_j)
\]

and

\[
D_{N,h}(x)=2\sum_{j=1}^m\left(e^{-\pi\mu_j(h)x}-e^{-\pi\lambda_jx}\right),
\]

\[
\mathcal J_{N,h}(x)=D_{N,h}(x)-x^{-1/2}D_{N,h}(1/x),\qquad \Re x>0,
\]

using the principal square-root branch.

Let

\[
\delta_{N,m}=\frac{2N+3}{m(2N+m+1)},\qquad
L=\left\lceil\frac{2}{\delta_{N,m}}\right\rceil,
\]

so XF-185 gives `L<=3m` and `L delta_{N,m}>=2`. For `|ell|<=L-1`, set

\[
w_\ell=1-\frac{|\ell|}{L},\qquad
\omega_m=2\pi\frac{m-1}{m},
\]

\[
s_\ell=\frac{\alpha}{a}+i\ell\omega_m,
\qquad
x_\ell=\frac{s_\ell}{\pi R}.
\]

Define the normalized nonlinear Jacobi packet map by

\[
\bigl(\mathfrak B_{N,m}(h)\bigr)_\ell
:=-\sqrt{w_\ell}\,\frac{e^{a s_\ell}}{2s_\ell}\,
\mathcal J_{N,h}(x_\ell),
\qquad |\ell|\le L-1.
\]

Then for every fixed `alpha>0` there are constants

\[
\kappa_\alpha>0,\qquad
c_\alpha>0,\qquad
C_\alpha<\infty,
\]

and `N_alpha`, depending only on `alpha`, such that whenever `N>=N_alpha`, `2<=m<=N`, and

\[
\|h\|_\infty,\ \|g\|_\infty\le\frac{\kappa_\alpha}{m},
\]

one has

\[
\boxed{
 c_\alpha\sqrt L\,\|h-g\|_2
 \le
 \|\mathfrak B_{N,m}(h)-\mathfrak B_{N,m}(g)\|_2
 \le
 C_\alpha\sqrt L\,\|h-g\|_2 .
}
\]

The constants are uniform in both `N` and `m`. In particular, the packet map is injective and quantitatively bi-Lipschitz on the entire cube, not merely at the reference comb.

## Exact direct map and its moving Fourier frame

At the XF-185 sample points, the direct Gaussian part simplifies before any approximation. Since

\[
\pi\mu_j(h)x_\ell=(a+u_j+h_j)s_\ell,
\]

the direct contribution to the normalized map is

\[
\bigl(\mathfrak B^{\rm dir}_{N,m}(h)\bigr)_\ell
=
\sqrt{w_\ell}\sum_{j=1}^m
 e^{-u_js_\ell}\,
 \frac{1-e^{-h_js_\ell}}{s_\ell}.
\]

Hence, at an arbitrary point `z`, its differential in direction `d` is exactly

\[
\bigl(J^{\rm dir}(z)d\bigr)_\ell
=
\sqrt{w_\ell}\sum_{j=1}^m
 d_j e^{-(u_j+z_j)s_\ell}.
\]

Set

\[
\beta=\frac{m-1}{m},\qquad y_j=\beta u_j,
\]

and let

\[
V(z)_{\ell j}
=
\sqrt{w_\ell}
 e^{-2\pi i\ell(y_j+\beta z_j)}.
\]

Also put

\[
D_0=\operatorname{diag}\left(e^{-\alpha u_j/a}\right),
\qquad
E(z)=\operatorname{diag}\left(e^{-\alpha z_j/a}\right).
\]

Then

\[
J^{\rm dir}(z)=V(z)D_0E(z).
\]

This is the same separated Fejer frame as XF-185, but with every phase node displaced by `beta z_j` and every column multiplied by a small positive damping perturbation.

## Why a uniform Jacobian bound alone is not enough

A lower singular-value bound for `J(z)` at every point would not by itself prove a global lower Lipschitz bound: vectors `J(z_t)(h-g)` may rotate and cancel when integrated along a chord. The needed statement is stronger. Fix

\[
d=h-g,\qquad z_t=g+t(h-g),\qquad 0\le t\le1,
\]

and test every moving differential against the **same reference vector** `V(0)D_0d`.

The direct chord is

\[
\mathfrak B^{\rm dir}(h)-\mathfrak B^{\rm dir}(g)
=
\int_0^1J^{\rm dir}(z_t)d\,dt.
\]

Thus it suffices to show a uniform positive real-part estimate

\[
\operatorname{Re}
\left\langle V(0)D_0d,\,J^{\rm dir}(z)d\right\rangle
\ge
\eta_\alpha L\,\|D_0d\|_2^2
\]

throughout the cube. The mixed Fejer Gram makes this possible.

## Mixed Fejer coercivity on the whole cube

Let

\[
C(z)=V(0)^*V(z).
\]

Because the sample indices are symmetric and Fejer weighted, its entries are Fejer kernels at the phase differences. For the diagonal,

\[
C_{jj}(z)=F_L(\beta z_j),
\qquad
F_L(t)=\frac1L\left(\frac{\sin(\pi Lt)}{\sin(\pi t)}\right)^2.
\]

Choose `kappa_alpha` first small enough that `L|beta z_j|<=1/32` throughout the cube. Then the elementary sine bounds give, very conservatively,

\[
\frac{C_{jj}(z)}{L}\ge\frac4{\pi^2}.
\]

For `j!=k`, the unperturbed nodes are separated on the circle by integer multiples of `delta_{N,m}`. Since `delta_{N,m}^{-1}<3m/2`, shrinking `kappa_alpha` if necessary gives

\[
\operatorname{dist}\bigl(y_k+\beta z_k-y_j,\mathbb Z\bigr)
\ge
(q-1/32)\delta_{N,m}
\]

for the `q`-th neighbor. The standard Fejer bound

\[
F_L(t)\le\frac{1}{4L\,\operatorname{dist}(t,\mathbb Z)^2}
\]

therefore yields the normalized off-diagonal row/column estimate

\[
\rho_*
\le
\frac{1}{2L^2\delta_{N,m}^2}
\sum_{q\ge1}\frac{1}{(q-1/32)^2}.
\]

Using `L delta_{N,m}>=2`,

\[
\rho_*
\le
\frac{\pi^2}{48}\left(\frac{32}{31}\right)^2
<0.22
<\frac4{\pi^2}.
\]

Thus the mixed Gram has a dimension-free positive real-part margin. The damping perturbation does not consume that margin: since `m<=N`,

\[
\frac1a=\frac RA<3,
\]

and therefore

\[
\|E(z)-I\|
\le
 e^{3\alpha\kappa_\alpha/m}-1.
\]

Taking `kappa_alpha` smaller by a constant depending only on `alpha` makes this perturbation less than a fixed fraction of the Fejer margin. Consequently there is `eta_alpha>0`, independent of `N,m`, for which

\[
\operatorname{Re}
\left\langle V(0)D_0d,\,J^{\rm dir}(z)d\right\rangle
\ge
\eta_\alpha L\,\|D_0d\|_2^2.
\]

Integrating along the chord and applying Cauchy--Schwarz gives

\[
\|\mathfrak B^{\rm dir}(h)-\mathfrak B^{\rm dir}(g)\|_2
\ge
c_\alpha\sqrt L\,\|h-g\|_2,
\]

because `e^{-3alpha}<=D_0<=1`. The corresponding upper bound follows from the same separation estimate applied to the shifted frames `V(z)`, whose node spacing remains a fixed fraction of `delta_{N,m}` throughout the cube.

## The reciprocal Jacobi image remains negligible nonlinearly

It remains to check that the `x^{-1/2}D(1/x)` term does not destroy the direct coercivity away from `h=0`. On the cube `|z_j|<=kappa_alpha/m`, all deformed squared radii remain comparable to `A`; in particular, after reducing `kappa_alpha` once more if necessary,

\[
\mu_j(z)\ge cA.
\]

At the XF-185 sampling geometry, uniformly for `|ell|<=L-1`,

\[
\operatorname{Re}\frac{\pi\mu_j(z)}{x_\ell}
\ge c_\alpha N^2.
\]

Differentiating the reciprocal image introduces only polynomial factors in `N,m` and the sample coordinates. Hence

\[
\sup_{\|z\|_\infty\le\kappa_\alpha/m}
\|J^{\rm rec}(z)\|
\le
\operatorname{poly}_\alpha(N)e^{-c_\alpha N^2}
=o(\sqrt L).
\]

The reciprocal chord is therefore an exponentially small perturbation of the direct chord, so the same two-sided estimate holds for the full Jacobi map `mathfrak B_{N,m}` once `N>=N_alpha`.

XF-185 additionally shows that the diagonal row normalization used to define the Fejer bank has uniformly bounded operator norm in the direction needed to transfer a normalized lower bound back to the unnormalized complex Jacobi samples. The nonlinear argument uses the same fixed bank. Hence this result does not hide its coercivity behind division by an exponentially small packet reference: the corresponding raw holomorphic samples retain a uniform lower visibility as well.

## The normalized `1/m` cell is a constant physical lattice cell

The apparent shrinking radius `kappa_alpha/m` is exactly the natural normalization of a packet whose squared-radius width is `R=Theta(mN)` when `m<=N`. Write a physical displacement as

\[
N+j\longmapsto N+j+\varepsilon_j.
\]

Then

\[
h_j
=
\frac{2(N+j)\varepsilon_j+\varepsilon_j^2}{R}.
\]

For `N>=m>=2` and `|varepsilon_j|<=1`, a direct estimate gives

\[
 m|h_j|\le3|\varepsilon_j|.
\]

Therefore, with

\[
\varepsilon_\alpha
=
\min\left(\frac14,\frac{\kappa_\alpha}{3}\right),
\]

all simultaneous perturbations satisfying

\[
|\varepsilon_j|\le\varepsilon_\alpha
\]

lie inside the nonlinear bi-Lipschitz chart. The physical radius is independent of both the remote location `N` and the number `m` of packet atoms, even at the maximal regime `m=N`.

Some `varepsilon_j` may equal zero. Thus, once the ambient consecutive window is known, the theorem does **not** require prior knowledge of which atoms inside that window are actually displaced: the nonlinear coordinate vector can recover zero and nonzero displacements together. The remaining support/localization problem is the global one of locating and recentering the relevant packet window(s) inside the full theta comb.

## Stress test and scope

The theorem closes a specific gap and no more. It upgrades XF-185 from infinitesimal conditioning to finite nonlinear stability on an actual lattice-scale neighborhood. It does not locate an unknown packet in the full comb, treat several separated or multiscale packets simultaneously, cover the regime `m>>N`, allow unknown atom weights, or transfer source-side Jacobi coercivity to a zero-sensitive observable capable of controlling the de Bruijn--Newman flow or `Lambda`.

The superresolution literature already contains nonlinear Lipschitz-stability principles for separated sparse measures, so the abstract message "separated Fourier spikes can be nonlinearly stable" is not Xi-specific. The point here is narrower: the exact quadratic theta geometry, the XF-185 anisotropic complex sampling scale, the Fejer mixed-Gram estimate, and the exponentially suppressed reciprocal Jacobi image combine to give constants uniform in both the remote index and a packet complexity growing all the way to `m=N`. The proof above is self-contained and uses the external literature only to delimit that prior-art boundary.

## Frontier consequence

The sequence XF-183--XF-186 now separates four effects that were previously entangled. Relative real-heat normalization can remove remote mode loss but pays an exponential absolute-signal price; holomorphic sampling avoids that price; Fejer oversampling removes the growing **linear** packet-conditioning loss; and the present result removes the corresponding **local nonlinear** inversion loss on constant physical lattice cells.

Accordingly, local inversion inside a known packet is no longer a plausible source-side obstruction in the regime `m<=N`. The live frontier moves outward: locate/recenter unknown packet windows without an oracle, understand interactions between multiple windows and the `m>>N` regime, incorporate weight perturbations if they are genuinely source-admissible, and most importantly transport this holomorphic source coercivity to a quantity whose control constrains Xi zeros or the de Bruijn--Newman parameter rather than merely reconstructing the theta-side deformation.