# NB-262 — Minimum-Hilbert boundary notch exports the Ford obstruction into a packet-scale side-lobe

> **Representation:** _Nyman–Beurling / resolved scalar-carrier destination interface._ The line-specific inputs are the Euler-normalized `H`-separated carrier dictionary and shell-Hilbert/`ell^2` identification of `NB-255`--`NB-261`, together with the legal complex Ford zero coordinate used in `NB-259` and the shrinking boundary scale isolated in `NB-261`. The generic engine is a two-functional minimum-`ell^2` interpolation problem and its continuum Fourier profile. The result is a route correction for the signed/complex escape left open by `NB-261`: a single shallow-depth boundary notch can indeed be imposed at vanishing shell-Hilbert cost, so Hilbert cost alone does not preserve the positive boundary trace. But the minimum-Hilbert notch necessarily carries total variation `Theta(m/u)` and turns that conditioning into a horizontal side-lobe of the same size on the natural Ford scale `x~m`. At the matched depth `u=log m+O(1)`, a Bellotti-compatible carrier-locked subpacket can therefore recover order-one residue mass away from the notched center. This does **not** rule out more elaborate signed/complex designs with additional horizontal constraints.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-CARRIER + EULER-NORMALIZED + H-SEPARATED-DICTIONARY + MINIMUM-HILBERT-INTERPOLANT + VANISHING-HILBERT-COST + TOTAL-VARIATION-TAX + PACKET-SCALE-SIDE-LOBE + SHRINKING-BOUNDARY-LAYER + MATCHED-CONTROL + NB-261-REFINEMENT + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-261` leaves one scalar route genuinely open. For positive near-full carriers with

\[
K\sim \frac{J}{m},
\qquad
1\ll m\ll A_J\asymp\log J,
\]

the fixed-depth Ford rectangle can be suppressed, but positivity forces a surviving shallow layer and a matched packet at

\[
u:=X(1-\beta)=\log m+O(1).
\]

A signed or complex carrier can cancel at that shallow depth, so the positive argument no longer applies. The first non-circular test is therefore the cheapest possible signed repair: impose the Euler anchor at `w=0`, impose one exact zero at the shallow boundary point `w=i u/Y`, and minimize the resolved shell-Hilbert cost.

That optimization can be solved exactly. Write

\[
C_J(w)=\sum_{j=0}^{K-1}c_j e^{ijw/J},
\qquad
C_J(0)=1,
\]

and put

\[
q:=e^{-u/(YJ)},
\qquad
\lambda:=\frac{Ku}{YJ}.
\]

The notch condition is

\[
C_J\!\left(i\frac uY\right)
=\sum_{j=0}^{K-1}c_jq^j
=0.
\]

If

\[
S_1:=\sum_{j=0}^{K-1}q^j,
\qquad
S_2:=\sum_{j=0}^{K-1}q^{2j},
\qquad
\Delta:=KS_2-S_1^2,
\]

then the unique minimum-`ell^2` coefficient vector is

\[
\boxed{
c_j=\frac{S_2-S_1q^j}{\Delta}
}
\]

and

\[
\boxed{
\|c\|_2^2=\frac{S_2}{\Delta}.
}
\]

In the near-full regime `K~J/m`, and at any shallow depth `u=o(m)`, one has

\[
\lambda\sim\frac{u}{Ym}\longrightarrow0.
\]

Provided `K lambda^2 -> infinity`—automatic at the `NB-261` depth `u=log m+O(1)` under `m=o(log J)`—the Riemann-sum asymptotics give

\[
\boxed{
\|c\|_2^2
\sim
\frac{12}{K\lambda^2}
\sim
\frac{12Y^2m^3}{Ju^2}.
}
\]

Consequently, at

\[
u=\log m+d_*,
\]

with fixed `d_*`,

\[
\boxed{
\|c\|_2
\sim
\frac{\sqrt{12}\,Y m^{3/2}}{\sqrt J\,u}
\longrightarrow0.
}
\]

The exact physical Euler tilt changes all resolved coefficients only by `1+o(1)` because the full carrier span is `W~KH~R/m=o(R)` and hence `W/X=O(1/m)`. Since the translated shells are disjoint, the normalized physical shell-Hilbert cost is asymptotic to a fixed multiple of `||c||_2`. Thus a signed carrier can erase the **center** of the shallow positive boundary layer at vanishing Hilbert cost. Any attempt to close the signed route by saying that such a notch must itself be Hilbert-expensive is false.

The same optimizer, however, reveals where the cost went. Every coefficient vector satisfying the two constraints obeys

\[
1
=\left|\sum_jc_j(1-q^j)\right|
\le
\|c\|_1\,(1-q^{K-1}),
\]

so

\[
\boxed{
\|c\|_1\ge\frac{1+o(1)}{\lambda}
\sim\frac{Ym}{u}.
}
\]

The minimum-Hilbert vector actually has this scale sharply. Define

\[
A_1(\lambda):=\frac{1-e^{-\lambda}}{\lambda},
\qquad
A_2(\lambda):=\frac{1-e^{-2\lambda}}{2\lambda},
\qquad
D(\lambda):=A_2(\lambda)-A_1(\lambda)^2.
\]

Then

\[
D(\lambda)=\frac{\lambda^2}{12}+O(\lambda^3)
\]

and the coefficient profile satisfies

\[
c_j
=\frac1Kf_\lambda(j/K)+o\!\left(\frac1{K\lambda}\right),
\qquad
f_\lambda(t)
:=\frac{A_2(\lambda)-A_1(\lambda)e^{-\lambda t}}{D(\lambda)}.
\]

Uniformly for `0<=t<=1`,

\[
\boxed{
\lambda f_\lambda(t)
=6(2t-1)+O(\lambda).
}
\]

Therefore

\[
\boxed{
\|c\|_1
\sim
\int_0^1|f_\lambda(t)|\,dt
\sim
\frac3\lambda
\sim
\frac{3Ym}{u}.
}
\]

So the cheap Hilbert notch is highly conditioned in exactly the total-variation currency isolated abstractly by `NB-255`.

The new point is that, for the minimum-Hilbert interpolant, this large variation cannot remain hidden in coefficient space. It reappears as a horizontal Ford side-lobe on the natural inverse-span scale. Put

\[
w_y:=\frac JK y+i\frac uY.
\]

Because `q=e^{-lambda/K}`, the exact carrier becomes

\[
C_J(w_y)
=\sum_{j=0}^{K-1}c_j
\exp\!\left(\frac{(iy-\lambda)j}{K}\right).
\]

For every bounded real `y`, the profile above yields the locally uniform limit

\[
\boxed{
\lambda C_J(w_y)
\longrightarrow
H(y):=6\int_0^1(2t-1)e^{iyt}\,dt.
}
\]

Here

\[
H(0)=0,
\qquad
H'(0)=i,
\]

and hence

\[
H(y)=iy-\frac{y^2}{2}+O(y^3).
\]

Choose any sufficiently small fixed `y_0>0`. Then `H(y_0) != 0`, and in a fixed neighborhood of `y_0` the values of `H` stay inside one complex cone. It follows that

\[
\boxed{
\left|C_J\!\left(\frac JK y+i\frac uY\right)\right|
\asymp
\frac1\lambda
\asymp
\frac{Ym}{u}
}
\]

for `y` in a small fixed interval around `y_0`. The center notch is therefore not a broad suppression of the shallow boundary layer. It is accompanied by an amplified lobe at horizontal Ford distance

\[
x\asymp\frac JK\asymp m.
\]

At the `NB-261` matched depth `u=log m+d_*`, this lobe has size

\[
\asymp\frac{m}{\log m}.
\]

That is much larger than the order-one positive carrier it was designed to cancel.

The side-lobe can be converted back into a matched compatibility control. Choose a fixed small `y_0>0` as above and let `n_0` be a carrier-locked index for which

\[
x_{n_0}:=\frac{2\pi q n_0}{Y}
\]

satisfies

\[
\frac KJx_{n_0}=y_0+o(1).
\]

Such an index exists because `J/K~m->infinity`. Take

\[
M:=\lfloor\delta u\rfloor
\]

consecutive carrier-locked ordinates

\[
\gamma_n=t_0+\frac{2\pi qn}{X},
\qquad
n_0\le n<n_0+M,
\]

with fixed sufficiently small `delta>0`, all at depth

\[
X(1-\beta)=u=\log m+d_*.
\]

Across this short packet,

\[
\frac KJ(x_n-x_{n_0})
=O\!\left(\frac{u}{m}\right)
=o(1),
\]

so all minimum-Hilbert carrier values remain in the same fixed cone and satisfy

\[
\left|C_J\!\left(x_n+i\frac uY\right)\right|
\asymp\frac{m}{u}.
\]

The main carrier is exactly locked,

\[
e^{iX(\gamma_n-t_0)}=1,
\]

while the original smooth shell coordinate obeys

\[
H[(\gamma_n-t_0)+i(1-\beta)]
=\frac1J\left(x_n+i\frac uY\right)
=o(1),
\]

because `x_n=Theta(m)` and `m=o(J)`. Thus the smooth envelope is `F(0)+o(1)` uniformly on the packet. Finally,

\[
e^{-X(1-\beta)}
=e^{-d_*}m^{-1}.
\]

Each side-lobe pole therefore contributes magnitude

\[
\asymp
\frac1m\frac{m}{u}
=\frac1u,
\]

with common phase up to a fixed cone. Since `M~delta u`, the complete matched contribution stays of order one:

\[
\boxed{
\liminf_{J\to\infty}
|\mathcal R_{\mathrm{side\ packet}}|
>0.
}
\]

This packet is strictly sparser than the `Theta(m)` positive control already audited in `NB-261`. It occupies a horizontal Ford interval of width only `Theta(u)=Theta(log m)`, centered at distance `Theta(m)` from `t_0`, and uses the same carrier spacing and the same depth `log m+O(1)`. The zero-free, Bellotti local-count and aggregate density ledger inherited from `NB-261` therefore remains permissive. As before, this is a **matched compatibility control**, not a claim that the actual zeta zeros realize such a packet.

## 1. Exact minimum-Hilbert interpolation

Retain the resolved notation of `NB-257`--`NB-261`,

\[
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR,
\qquad
J:=\frac RH\to\infty,
\]

with `Y` in a fixed compact subset of `(0,infinity)`. Let

\[
1\ll m\ll A_J:=\frac{\log J}{Y},
\qquad
K:=\left\lfloor\frac Jm\right\rfloor.
\]

Use the same one-sided `H`-separated offsets `xi_j=jH`, `0<=j<K`, but now allow signed or complex Euler-normalized masses `c_j`:

\[
\lambda_J:=\sum_{j=0}^{K-1}c_j\delta_{jH},
\qquad
\sum_jc_j=1.
\]

The physical coefficient measure is

\[
d\nu_J(\xi)=e^{r\xi/X}d\lambda_J(\xi),
\]

so the exact Euler normalization remains

\[
\int e^{-r\xi/X}d\nu_J(\xi)=1.
\]

Since

\[
W=(K-1)H\sim\frac Rm,
\qquad
\frac WX=O(m^{-1}),
\]

the physical tilt `e^{rjH/X}` is uniformly `1+o(1)`. The disjoint-shell identity therefore gives

\[
H^{1/2}\|h_{\nu_J}\|_2
=(1+o(1))\|\phi\|_2\|c\|_2.
\]

Thus minimizing coefficient `ell^2` is asymptotically the same as minimizing the actual resolved shell-Hilbert cost.

Fix a shallow physical Ford depth `u=u_J` with

\[
1\ll u=o(m)
\]

and impose the exact boundary notch

\[
C_J\!\left(i\frac uY\right)=0.
\]

Set

\[
q=e^{-u/(YJ)},
\qquad
a=(1,\ldots,1),
\qquad
b=(1,q,\ldots,q^{K-1}).
\]

The constraints are

\[
a\cdot c=1,
\qquad
b\cdot c=0.
\]

Although complex coefficients are allowed, the constraint vectors and target data are real, so the unique minimum-`ell^2` solution is real. Its Gram matrix is

\[
G=
\begin{pmatrix}
K&S_1\\
S_1&S_2
\end{pmatrix},
\]

with determinant `Delta=KS_2-S_1^2>0`. Projecting the origin onto the affine constraint plane gives

\[
c=A^T(AA^T)^{-1}
\binom10,
\]

which is exactly

\[
c_j=\frac{S_2-S_1q^j}{\Delta}.
\]

The minimum norm is

\[
\|c\|_2^2
=\left(G^{-1}\right)_{11}
=\frac{S_2}{\Delta}.
\]

No asymptotic input enters these formulas.

## 2. The shallow notch is Hilbert-cheap but variation-expensive

Define the dimensionless depth-span product

\[
\lambda:=\frac{Ku}{YJ}.
\]

Then

\[
q=e^{-\lambda/K}.
\]

For `K->infinity`, the normalized sums are Riemann sums for

\[
A_1(\lambda)=\int_0^1e^{-\lambda t}dt,
\qquad
A_2(\lambda)=\int_0^1e^{-2\lambda t}dt.
\]

If `lambda->0` and `K lambda^2->infinity`, then

\[
\frac{S_1}{K}=A_1(\lambda)+o(\lambda^2),
\qquad
\frac{S_2}{K}=A_2(\lambda)+o(\lambda^2),
\]

and therefore

\[
\frac\Delta{K^2}
=D(\lambda)+o(\lambda^2).
\]

The elementary expansions

\[
A_1(\lambda)
=1-\frac\lambda2+\frac{\lambda^2}{6}+O(\lambda^3),
\]

\[
A_2(\lambda)
=1-\lambda+\frac{2\lambda^2}{3}+O(\lambda^3)
\]

give

\[
D(\lambda)
=\frac{\lambda^2}{12}+O(\lambda^3).
\]

Hence

\[
\|c\|_2^2
\sim\frac{12}{K\lambda^2}.
\]

At the live `NB-261` boundary depth

\[
u=\log m+d_*,
\]

we have

\[
\lambda
=\frac{Ku}{YJ}
\sim\frac{u}{Ym}
\to0
\]

and

\[
K\lambda^2
\asymp
\frac{Ju^2}{m^3}
\to\infty
\]

because `m=o(log J)`. Therefore

\[
H^{1/2}\|h_{\nu_J}\|_2
\asymp
\frac{m^{3/2}}{\sqrt J\,\log m}
\to0.
\]

This is the first correction supplied by the finding: **the positive boundary trace of `NB-261` is not protected by resolved Hilbert cost once signs are allowed.**

Total variation behaves in the opposite way. The two interpolation constraints imply

\[
1
=\left|\sum_jc_j(1-q^j)\right|
\le\sum_j|c_j|(1-q^j)
\le\|c\|_1(1-q^{K-1}).
\]

Since

\[
1-q^{K-1}
=(1-e^{-\lambda})(1+o(1))
\sim\lambda,
\]

every notch satisfies

\[
\|c\|_1\gtrsim\lambda^{-1}.
\]

For the minimum-Hilbert vector, the continuum profile gives the stronger asymptotic

\[
\|c\|_1\sim\frac3\lambda.
\]

Thus the exact operation that is cheap in `ell^2` is expensive in the total-variation currency already identified by `NB-255`.

## 3. The minimum-Hilbert vector turns its variation into a Ford side-lobe

The coefficient profile can be read directly from the exact optimizer. Under the same regime,

\[
c_j
=\frac1Kf_\lambda(j/K)+o\!\left(\frac1{K\lambda}\right)
\]

uniformly in `j`, where

\[
f_\lambda(t)
=\frac{A_2(\lambda)-A_1(\lambda)e^{-\lambda t}}
{A_2(\lambda)-A_1(\lambda)^2}.
\]

A direct Taylor expansion yields

\[
\lambda f_\lambda(t)
=6(2t-1)+O(\lambda)
\]

uniformly on `[0,1]`. The minimum-Hilbert coefficients therefore look, after scaling, like a signed linear ramp. The large positive and negative masses cancel at both prescribed evaluation functionals, but they remain individually of total size `Theta(1/lambda)`.

Now inspect the carrier one natural horizontal coherence length away from the notch. For fixed real `y`, put

\[
w_y=\frac JK y+i\frac uY.
\]

Then

\[
C_J(w_y)
=\sum_jc_j e^{(iy-\lambda)j/K}.
\]

Riemann-sum convergence and the profile asymptotic give

\[
\lambda C_J(w_y)
\to
6\int_0^1(2t-1)e^{iyt}dt
=:H(y)
\]

locally uniformly in `y`. The exact notch appears as `H(0)=0`. But

\[
H'(0)
=6i\int_0^1t(2t-1)dt
=i,
\]

so the limiting profile leaves zero linearly:

\[
H(y)=iy-\frac{y^2}{2}+O(y^3).
\]

Therefore there are fixed constants `0<eta_1<eta_2` and `c>0` such that, for all sufficiently large `J`,

\[
\left|C_J\!\left(\frac JK y+i\frac uY\right)\right|
\ge\frac{c}{\lambda}
\]

for `eta_1<=y<=eta_2`; after one fixed phase rotation the same values have positive real part `>=c/lambda`. Since `J/K~m`, this is a horizontal Ford strip

\[
x\asymp m
\]

with amplitude

\[
\asymp\frac{m}{u}.
\]

This is not a generic theorem that every signed notch must have this exact lobe. It is an exact asymptotic description of the **minimum-Hilbert** notch, the most favorable one-notch design if shell `ell^2` cost is the optimization objective.

## 4. A short carrier-locked subpacket recovers order-one residue mass

Set

\[
u=\log m+d_*
\]

with fixed `d_*`, and choose a point `y_0` in the side-lobe interval above. Carrier-locked Ford ordinates have coordinates

\[
x_n=\frac{2\pi qn}{Y},
\]

so their `y`-mesh is

\[
\frac KJ(x_{n+1}-x_n)
=\frac{2\pi qK}{YJ}
\asymp\frac1m.
\]

Hence there is an index `n_0=Theta(m)` with

\[
\frac KJx_{n_0}=y_0+o(1).
\]

Take only

\[
M=\lfloor\delta u\rfloor
\]

consecutive points from there. Since `u=o(m)`, the whole packet remains in an `o(1)` `y`-neighborhood of `y_0`. The carrier values are consequently cone-aligned with magnitude `Theta(m/u)`.

At the same time,

\[
e^{iYx_n}=1
\]

for every carrier-locked point, and

\[
\frac1J\left(x_n+i\frac uY\right)
=O\!\left(\frac mJ\right)+o(1)
=o(1),
\]

so the fixed smooth shell envelope is `F(0)+o(1)`. The Ford damping is

\[
e^{-u}=e^{-d_*}m^{-1}.
\]

Each pole therefore carries `Theta(1/u)` after the signed side-lobe amplification, and `Theta(u)` aligned poles give an order-one residue contribution.

This control is easier on the zero-count ledger than the positive packet in `NB-261`: the depth is identical, the horizontal location is still only `Theta(m/R)=o(1/H)` from `t_0`, and the population has fallen from `Theta(m)` to `Theta(log m)`. No new zeta input is being asserted. The construction only shows that the currently audited zero-free and density information does not exclude the side-lobe packet that defeats this particular signed repair.

## 5. What changes after `NB-261`

`NB-261` ended with the signed/complex near-full carrier as the main scalar escape because positivity no longer forces an order-one boundary value near `s=0`. The present calculation confirms the first half of that intuition: **signs really can kill the positive boundary trace at negligible resolved Hilbert cost.** The minimum-cost center notch at `u=log m+O(1)` has shell-Hilbert norm tending to zero.

But it also shows why a single signed notch is not enough. The interpolation problem is badly conditioned in `ell^1`: its total variation is `Theta(m/u)`. For the minimum-Hilbert solution that conditioning appears physically as a side-lobe at exactly the horizontal Ford scale `x~m` left by the carrier span `W~R/m`. The old positive packet at the center is removed, but a much shorter `Theta(u)` matched packet at horizontal offset `Theta(m)` can restore order-one residue mass.

The right next target is therefore not another center-depth interpolation condition. A potentially successful signed design has to control a **two-dimensional shallow boundary strip**: it must suppress enough of the horizontal interval `x=Theta(m)` at depth `u~log m` to prevent carrier-locked subpackets, while keeping shell-Hilbert norm, total variation and rank under control. Extra horizontal constraints may flatten the minimum-Hilbert side-lobe, so the present result does not close that route; it identifies the additional quantity such a design must pay for.

A useful equivalent formulation is to ask for the minimum resolved Hilbert cost under

\[
C_J(0)=1
\]

and simultaneous shallow-depth conditions at a mesh of points

\[
C_J(x_\ell+i u/Y)\approx0,
\qquad
x_\ell\asymp m.
\]

The number and spacing of these constraints should be matched to carrier-locked Ford spacing, not chosen as an arbitrary interpolation grid. This is genuinely different from the fixed-depth ladder of `NB-260`: the depth is now shrinking, while the live complexity is horizontal.

## 6. Prior art and representation audit

The finite-dimensional optimization is generic. Minimum-energy interpolation of band-limited functions and the associated growth of dynamic range are classical themes in the superoscillation literature; Ferreira and Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Transactions on Signal Processing 54 (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, is a close conceptual boundary. That work studies minimum-energy band-limited interpolation and the energy/dynamic-range price of superoscillatory constraints. It does not supply the Ford-scaled complex-depth statement above.

A fresh search across Nyman--Beurling/Hardy literature and minimum-energy interpolation did not locate the specific combination here: exact Euler normalization, a near-full resolved Mellin carrier, a notch at the shrinking legal depth `X(1-beta)=log(J/K)+O(1)`, vanishing shell-Hilbert cost, and the resulting packet-scale horizontal amplification. No external theorem is load-bearing in the proof, so `SOURCES.md` needs no new durable dependency.

The representation split is explicit. The two-constraint Gram solve, the `ell^1` lower bound and the continuum side-lobe profile are generic Fourier/interpolation facts. The Nyman--Beurling-specific content is the Euler normalization, the shell-Hilbert/`ell^2` identification, the legal complex zero coordinate, the Ford scaling `J=R/H`, the depth damping `e^{-X(1-beta)}`, and the conversion of the side-lobe into a matched zeta-compatible residue packet. The final packet remains a compatibility test against imported zeta bounds, not a theorem about actual zeta-zero geometry.

## 7. Adversarial audit

The strongest invalid conclusion would be that signed/complex near-full scalar carriers are impossible. This finding proves no such theorem. It analyzes the unique minimum-Hilbert solution to **one** shallow boundary notch and shows that this optimizer has a large natural-scale horizontal side-lobe. A different coefficient vector with extra interpolation constraints can deliberately trade more Hilbert cost or rank for side-lobe suppression.

A second overclaim would be that the total-variation lower bound alone forces the specific side-lobe. It does not. The universal statement is only

\[
\|c\|_1\gtrsim\frac{m}{u}.
\]

The explicit side-lobe theorem uses the exact minimum-`ell^2` optimizer and its continuum ramp profile. The two statements are kept separate.

A third possible failure is the finite-`K` passage to the continuum profile. The required scale separation is

\[
K\lambda^2\to\infty.
\]

At the live boundary depth `u=log m+O(1)` and under the `NB-261` regime `m=o(log J)`,

\[
K\lambda^2
\asymp\frac{J(\log m)^2}{m^3}
\to\infty,
\]

so discretization errors are negligible compared with the `lambda^2` Gram determinant. No claim is made outside regimes where this condition holds.

A fourth overclaim would be to identify coefficient `ell^2` exactly with the final Nyman distance. The identification here is only with the resolved disjoint-shell source Hilbert cost, up to the `1+o(1)` Euler tilt. Hardy projection and the rest of the Nyman approximant remain separate. The point is narrower: the cheapest resolved signed notch is not blocked by source Hilbert norm, yet it is also not a successful Ford suppression because its own carrier regenerates an admissible matched residue packet.

Finally, the control packet is not evidence that zeta actually contains zeros at those points. It reuses a shallower and sparser subset of the admissible geometry already audited in `NB-261`. Its role is only to prevent the present source design from claiming deterministic success under the currently imported zero information.

## 8. Surviving frontier

The positive route of `NB-261` failed because coherence was forced near the Euler boundary. The one-notch signed repair studied here can remove that central coherence with vanishing Hilbert cost, but only by producing a conditioned carrier whose minimum-Hilbert profile has amplitude `Theta(m/log m)` one natural horizontal scale away.

The next non-circular problem is therefore:

> What is the minimum resolved Hilbert/variation cost of suppressing a carrier-locked **horizontal shallow strip** at `X(1-beta)~log(J/K)`, rather than a single vertical center point, when `K=J^{1-o(1)}`?

If that multi-point cost becomes coercive before `K=Theta(J)`, the signed scalar escape closes. If it remains bounded while side-lobes can be flattened on the entire Ford packet scale, then signed near-full carriers would provide the first genuine escape from the `NB-252`--`NB-262` obstruction chain and would have to be tested through the exact Hardy projection.