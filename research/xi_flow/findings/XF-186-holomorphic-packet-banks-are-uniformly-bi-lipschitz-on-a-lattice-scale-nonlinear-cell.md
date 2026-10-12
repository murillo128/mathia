---
type: theorem
research_line: xi_flow
finding_id: XF-186
status: canonical
---

# XF-186 — Holomorphic packet banks are uniformly bi-Lipschitz on a lattice-scale nonlinear cell

**Evidence classification:** `CLASSICAL-FEJER/FOURIER-SEPARATION + EXACT-XI/JACOBI-GEOMETRY + UNIFORM-NONLINEAR-PACKET-COERCIVITY`. XF-185 shows that a known consecutive Xi packet with `2<=m<=N` is uniformly observable after linearization by a Fejer-overcomplete bank of complex Jacobi samples. The remaining local question is whether nonlinear inversion reintroduces a condition-number loss when all `m` atom locations move simultaneously. It does not on the natural lattice cell. For every fixed right-half-plane parameter `alpha>0`, the same bank is uniformly bi-Lipschitz on a normalized cube of radius `kappa_alpha/m`, with constants independent of both the remote index `N` and packet complexity `m`. In physical lattice coordinates that cube contains displacements of fixed size independent of `N,m`. Thus the XF-185 linear frame is not merely infinitesimally well conditioned: it gives a genuine nonlinear coordinate chart for constant-size local perturbations of every atom in a known packet. Lower visibility for the unnormalized raw samples is also uniform, but requires a separate zero-row erasure argument; the full symmetric diagonal normalizer is not uniformly bounded.

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

Let \(J_{\rm raw}(h)=(\mathcal J_{N,h}(x_\ell))_{|\ell|<L}\), and let \(P_*\) delete the \(\ell=0\) coordinate, leaving the remaining original sample points and weights untouched. On the same cube, with the constants and onset specified below,
\[
\boxed{\quad
\|P_*(J_{\rm raw}(h)-J_{\rm raw}(g))\|_2
\ge\frac{\pi e^{-4\alpha}}{5\sqrt2}
\sqrt L\,\|h-g\|_2.\quad}
\]
This also lower-bounds the full raw norm, since \(P_*\) is an orthogonal projection. It does not rely on the unbounded full symmetric row normalizer.

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

## A fixed reference along nonlinear chords

A pointwise lower singular-value bound for a moving Jacobian does not in general imply a lower Lipschitz bound: the tangent images could cancel when integrated. Set \(d=h-g\), \(z_t=g+t(h-g)\), and use the **same** retained reference vector \(P_*V(0)D_0d\) for every \(t\). The direct chord is
\[
\mathfrak B^{\rm dir}(h)-\mathfrak B^{\rm dir}(g)
=\int_0^1J^{\rm dir}(z_t)d\,dt.
\]
It suffices to prove uniform positive real pairing against that fixed vector.

## Exact quadratic separation and erased mixed Fejer Gram

Choose
\[
0<\kappa_\alpha\le\min\{1/96,\log(33/32)/(3\alpha)\}.
\]
For the **actual quadratic nodes** rather than an equispaced surrogate, the consecutive circular gaps (including wrap-around) satisfy
\[
y_{j+1}-y_j=\frac{2N+2j+1}{m(2N+m+1)}
\ge\delta_{N,m},\qquad
1-(y_m-y_1)=\frac1m\ge\delta_{N,m}.
\]
Furthermore \(2/3<m\delta_{N,m}\le1\), so
\[
2m\le L\le3m,\qquad L\delta_{N,m}\ge2.
\]
At circular neighbor rank \(q=\min(|j-k|,m-|j-k|)\), unshifted nodes are separated by at least \(q\delta_{N,m}\). On the cube, \(|\beta z_j|\le\delta_{N,m}/64\), so mixed unshifted/shifted nodes and pairs of shifted nodes are separated by at least \((q-1/32)\delta_{N,m}\), including the wrap-around.

For \(F_L(t)=L^{-1}(\sin(\pi Lt)/\sin(\pi t))^2\), the usual Fejer bound \(F_L(t)\le[4L\operatorname{dist}_{\mathbb T}(t,0)^2]^{-1}\) yields both the mixed **row and column** off-diagonal estimates
\[
\frac1L\sum_{k\ne j}F_L(y_k+\beta z_k-y_j)
\le\frac1{2L^2\delta_{N,m}^2}
\sum_{q\ge1}(q-1/32)^{-2}
\le\frac{\pi^2}{48}\left(\frac{32}{31}\right)^2
<\frac{11}{50}.
\]
Each circular rank contributes at most two entries. Since \(L|\beta z_j|\le1/32\) and \(\sin t\ge t-t^3/6\),
\[
\frac{F_L(\beta z_j)}L
\ge\left(1-\frac{\pi^2}{6\cdot32^2}\right)^2
>\frac{99}{100}.
\]

The \(\ell=0\) row of \(V(z)\) is exactly \(\mathbf1_m^*\) for every \(z\). Thus deleting only this row gives the exact rank-one identity
\[
C_*(z):=V(0)^*P_*^*P_*V(z)
=V(0)^*V(z)-\mathbf1_m\mathbf1_m^*.
\]
The real diagonal is at least \(99L/100-1\); each absolute off-diagonal row and column sum is at most \(11L/50+(m-1)\). A row/column quadratic-form estimate, which does not assume the mixed Gram is Hermitian, gives
\[
\boxed{\quad
\operatorname{Re}\langle q,C_*(z)q\rangle
\ge[(99/100-11/50)L-m]\|q\|_2^2
\ge\frac{27}{100}L\|q\|_2^2.\quad}
\]
The same separation estimate on an individual shifted or reference frame also yields
\[
\|P_*V(0)\|,\ \|P_*V(z)\|,\ \|V(z)\|\le\sqrt{2L},
\qquad\|C_*(z)\|\le2L.
\]
This accounts for both positive and negative retained frequencies, and applies at \(m=2\) and \(m=N\).

The right-hand damping in \(J^{\rm dir}(z)=V(z)D_0E(z)\) obeys, since \(1/a=R/A<3\),
\[
\|E(z)-I\|\le e^{3\alpha\kappa_\alpha/m}-1\le1/32,
\qquad e^{-3\alpha}I\preceq D_0\preceq I.
\]
For \(q=D_0d\), uniformly all along the chord,
\[
\begin{aligned}
\operatorname{Re}\langle P_*V(0)q,P_*J^{\rm dir}(z_t)d\rangle
&=\operatorname{Re}\langle q,C_*(z_t)E(z_t)q\rangle\\
&\ge(27/100-2/32)L\|q\|_2^2
>\frac L5\|q\|_2^2.
\end{aligned}
\]
Integrating with the fixed reference before applying Cauchy--Schwarz yields
\[
\boxed{\quad
\|P_*(\mathfrak B^{\rm dir}(h)-\mathfrak B^{\rm dir}(g))\|_2
\ge\frac{e^{-3\alpha}}{5\sqrt2}\sqrt L\,\|h-g\|_2.\quad}
\]
The full direct-map upper chord estimate follows instead from \(\|V(z)\|\le\sqrt{2L}\) and \(\|E(z)\|\le33/32\).

## Reciprocal Jacobi control and the complete chart

Differentiating the **actual** reciprocal contribution of the symmetric normalized bank gives exactly
\[
\boxed{\quad
\partial_{h_j}(\mathfrak B^{\rm rec})_\ell(z)
=-\sqrt{w_\ell}\,e^{as_\ell}x_\ell^{-5/2}
\exp\left(-\frac{\pi\mu_j(z)}{x_\ell}\right).\quad}
\]
This uses \(s_\ell=\pi Rx_\ell\) and the principal square-root branch; it is a bound between moving configurations, not just at the base comb. The cube ensures \(\mu_j(z)\ge A/2\), so
\[
\|P_*J^{\rm rec}(z)\|^2
\le e^{2\alpha}\sum_{\ell\ne0}w_\ell|x_\ell|^{-5}
\sum_{j=1}^m
\exp[-2\pi\mu_j(z)\operatorname{Re}(1/x_\ell)].
\]
For the retained rows, \(|x_\ell|\le C_\alpha/N\), \(|x_\ell|^{-1}\le R<3N^2\), and \(\operatorname{Re}x_\ell=\alpha/(\pi A)\). Hence
\[
\operatorname{Re}\frac{\pi\mu_j(z)}{x_\ell}
=\frac{\alpha\mu_j(z)}{A|x_\ell|^2}
\ge c_\alpha N^2.
\]
There are fewer than \(6N\) retained rows and at most \(N\) columns. The Frobenius estimate therefore implies
\[
\sup_z\|P_*J^{\rm rec}(z)\|
\le C_\alpha N^6e^{-c_\alpha N^2}.
\]
The zero row of the *full* reciprocal derivative is likewise negligible: \(x_0=\alpha/(\pi A)>0\) has reciprocal magnitude \(O_\alpha(N^2)\) and its exponent is at least \(c_\alpha N^4\). Choose \(N_\alpha\) so the retained derivative norm is at most \(e^{-3\alpha}\sqrt L/(10\sqrt2)\). Integrating along the same chord and subtracting the reciprocal contribution gives
\[
\boxed{\quad
\|P_*(\mathfrak B(h)-\mathfrak B(g))\|_2
\ge\frac{e^{-3\alpha}}{10\sqrt2}\sqrt L\,\|h-g\|_2.\quad}
\]
Because \(P_*\) is contractive, the full normalized chart has the same lower bound. The direct and reciprocal full derivative estimates give its asserted uniform upper bound.

## Raw samples and unrestricted additive noise

Write \(\mathfrak B(h)=QJ_{\rm raw}(h)\), where
\[
Q_{\ell\ell}=-\sqrt{w_\ell}\frac{e^{as_\ell}}{2s_\ell}.
\]
The zero row has \(|Q_{00}|=e^\alpha a/(2\alpha)\), and in fact this equals \(\|Q\|\). With \(m=2\), \(a=(N+1)^2/(2N+3)\sim N/2\); **the full symmetric normalizer is unbounded**. XF-185 used a different one-sided bank excluding this row, so its full-normalizer argument does not transfer here.

On the **retained** rows alone,
\[
P_*\mathfrak B(h)=Q_*P_*J_{\rm raw}(h),\qquad
\|Q_*\|\le\frac{e^\alpha}{2\omega_m}
\le\frac{e^\alpha}{2\pi},
\]
because \(|\ell|\ge1\), \(|s_\ell|\ge\omega_m=2\pi(m-1)/m\ge\pi\). Combining this with the retained nonlinear lower bound gives
\[
\boxed{\quad
\|P_*(J_{\rm raw}(h)-J_{\rm raw}(g))\|_2
\ge\frac{\pi e^{-4\alpha}}{5\sqrt2}
\sqrt L\,\|h-g\|_2.\quad}
\]
No restricted noise range is assumed; a raw additive error of norm at most \(\sigma\) has retained norm at most \(\sigma\). If any feasible estimate \(\widehat h\) in the same cube fits the retained raw data with residual at most \(\sigma\), the triangle inequality implies
\[
\boxed{\quad
\|\widehat h-h\|_2
\le\frac{10\sqrt2 e^{4\alpha}}{\pi\sqrt L}\,\sigma.\quad}
\]
The problematic zero row is ignored, not reweighted. This is a deterministic bound for any feasible estimate, not an assertion about an efficient optimizer or an oracle-free packet search.

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

The inverse physical coordinate derivative is
\[
\frac{d\varepsilon_j}{dh_j}=\frac{R}{2(N+j+\varepsilon_j)}
\le\frac{3m}{2}\qquad(|\varepsilon_j|\le1/4).
\]
Thus \(\|\widehat\varepsilon-\varepsilon\|_2\le(3m/2)\|\widehat h-h\|_2\) in the physical cell. A constant physical *radius* does not supply a dimension-independent physical noise modulus.

## Stress test and scope

The theorem closes a specific gap and no more. It upgrades XF-185 from infinitesimal conditioning to finite nonlinear stability on an actual lattice-scale neighborhood and obtains raw lower visibility using retained rows rather than a false full-normalizer bound. It does not locate an unknown packet in the full comb, treat several separated or multiscale packets simultaneously, cover the regime `m>>N`, allow unknown atom weights, or transfer source-side Jacobi coercivity to a zero-sensitive observable capable of controlling the de Bruijn--Newman flow or `Lambda`.

The superresolution literature already contains nonlinear Lipschitz-stability principles for separated sparse measures, so the abstract message "separated Fourier spikes can be nonlinearly stable" is not Xi-specific. The point here is narrower: the exact quadratic theta geometry, the XF-185 anisotropic complex sampling scale, the Fejer mixed-Gram estimate, and the exponentially suppressed reciprocal Jacobi image combine to give constants uniform in both the remote index and a packet complexity growing all the way to `m=N`. The proof above is self-contained and uses the external literature only to delimit that prior-art boundary.

## Frontier consequence

The sequence XF-183--XF-186 now separates four effects that were previously entangled. Relative real-heat normalization can remove remote mode loss but pays an exponential absolute-signal price; holomorphic sampling avoids that price; Fejer oversampling removes the growing **linear** packet-conditioning loss; and the present result removes the corresponding **local nonlinear** inversion loss on constant physical lattice cells.

Accordingly, local inversion inside a known packet is no longer a plausible source-side obstruction in the regime `m<=N`. The live frontier moves outward: locate/recenter unknown packet windows without an oracle, understand interactions between multiple windows and the `m>>N` regime, incorporate weight perturbations if they are genuinely source-admissible, and most importantly transport this holomorphic source coercivity to a quantity whose control constrains Xi zeros or the de Bruijn--Newman parameter rather than merely reconstructing the theta-side deformation.