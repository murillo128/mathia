# NB-253 — Positive multi-shell comb recreates the Ford obstruction at shallower depth

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + MULTI-CARRIER-AUDIT + SOURCE-NORMALIZED + DIRICHLET-KERNEL + MATCHED-CONTROL + NB-252-REFINEMENT + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-251` leaves a genuine source-side opening: at fixed Ford localization scale `H` and fixed population parameter `J=R/H`, a carrier span `W` with `W/H -> infinity` defeats the standard matched packet if that extra span is available as independent carrier averaging. `NB-252` shows that simply replacing one shell of width `H` by one shell of width `B_J H` does not realize that premise, because the legal Ford problem renormalizes to `J_B=J/B_J` and a replacement critical layer restores the obstruction.

The next canonical construction is a sparse multi-shell source: keep every component shell at width `H`, keep the original `H` and `J`, but average `K=K_J` translated copies whose centers span `Theta(KH)`. This really does have super-`H` source support while each component retains the old local width.

For the natural positive equal-weight comb, however, the gain is again illusory. Its Mellin carrier factors exactly as

\[
\boxed{
L_K(v)=e^{iXv}F(Hv)P_K(CHv),
\qquad
P_K(z)=\frac1K\sum_{k=0}^{K-1}e^{ikz}.
}
\]

The normalized Dirichlet factor `P_K` develops a coherence peak of vertical width `Theta(1/(KH))`. Consequently the number of carrier cells participating coherently near that peak is not `J` but

\[
\boxed{
J_K:=\frac{R}{KH}=\frac JK.
}
\]

A matched packet with `Theta(J_K)` points placed at the shallower horizontal depth

\[
\boxed{
X(1-\beta)=\log J_K+O(1)
}
\]

still contributes order one. Equivalently, in the old depth coordinate

\[
d=X(1-\beta)-\log J,
\]

the replacement layer is

\[
\boxed{
d=-\log K+O(1).}
\]

Thus the simplest genuinely multi-carrier architecture is also scale-covariant, but by a different mechanism from `NB-252`: **the component width does not change, yet coherent recombination of the carriers narrows the selected-height kernel and dynamically replaces `J` by `J/K`.** Merely having a convex carrier span `W/H -> infinity` is therefore not enough to realize the fixed-window averaging premise of `NB-251`.

This does not close every multi-carrier escape. Signed or complex coefficients, an `ell^2` family kept separate until after projection, or another architecture that produces super-`H` carrier energy without a unit-height coherence peak of width `1/W` remains open. The result closes the canonical positive normalized comb and identifies the extra property a successful construction must defeat.

## 1. Build a legal positive multi-shell source at fixed component width

Retain the exact-Ford notation stabilized in `NB-230`--`NB-252`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty.
\tag{1}
\]

As in the conservative matched-control regime, assume

\[
J\le \log Q.
\tag{2}
\]

Fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\tag{3}
\]

and choose a fixed spacing constant

\[
C>1.
\tag{4}
\]

Let `K=K_J` be an integer sequence satisfying

\[
\boxed{
K\to\infty,
\qquad
\frac JK\to\infty,
\qquad
\frac{K\log J}{J}\to0.
}
\tag{5}
\]

For example `K=floor(sqrt(J))` is admissible. Define the positive equal-weight comb

\[
\boxed{
h_K(u)
:=
\frac1K\sum_{k=0}^{K-1}
\frac1H
\phi\!\left(
\frac{u-X-kCH}{H}
\right).
}
\tag{6}
\]

Every component has the original width `H`; no literal replacement `H -> KH` has been made. Since `C>1` and `supp phi subset (0,1)`, the components may be taken disjoint. Their convex support span is

\[
W_K=CKH+O(H),
\tag{7}
\]

so

\[
\boxed{
\frac{W_K}{H}\asymp K\to\infty,
\qquad
\frac{W_K}{X}
\asymp
\frac{K}{YJ}	o0.
}
\tag{8}
\]

This is exactly the mesoscopic geometry left open by `NB-251`--`NB-252`: super-`H`, but still `o(X)`.

The source normalization remains order one. Exactly,

\[
\int_\mathbb R h_K(u)\,du
=
\int_0^1\phi(y)\,dy.
\tag{9}
\]

For the positive Euler source on

\[
\sigma_X=1+\frac rX,
\tag{10}
\]

the same prime-number-theorem/Stieltjes argument used in `NB-224` gives

\[
\begin{aligned}
S_K(0)
&=
\sum_{n\ge2}\Lambda(n)h_K(\log n)n^{-\sigma_X}\\
&=
\frac1K\sum_{k=0}^{K-1}
\int_0^1
\phi(y)
\exp\!\left[-r\left(
1+\frac{(kC+y)H}{X}
\right)\right]dy
+o(1).
\end{aligned}
\tag{11}
\]

Because

\[
\frac{KH}{X}=\frac{K}{YJ}=o(1),
\tag{12}
\]

the convergence in (11) is uniform in `k<K`, and hence

\[
\boxed{
S_K(0)
\longrightarrow
 e^{-r}\int_0^1\phi(y)\,dy
>0.
}
\tag{13}
\]

Thus the carrier span is not being bought by letting the positive source mass grow or vanish.

All Mellin frequencies in (6) remain positive for large `X`, so the positive-frequency Hardy projection of `NB-249` continues to apply linearly, before any squaring.

## 2. The carrier is a narrow shell envelope times a Dirichlet coherence factor

Write

\[
F(z)=\int_0^1\phi(y)e^{iyz}\,dy.
\tag{14}
\]

The Fourier/Mellin carrier of (6) is exactly

\[
\begin{aligned}
L_K(v)
&:=\int_\mathbb R h_K(u)e^{iuv}\,du\\
&=
\frac1K\sum_{k=0}^{K-1}
 e^{i(X+kCH)v}F(Hv).
\end{aligned}
\tag{15}
\]

Therefore

\[
\boxed{
L_K(v)=e^{iXv}F(Hv)P_K(CHv),
}
\tag{16}
\]

where

\[
\boxed{
P_K(z)=\frac1K\sum_{k=0}^{K-1}e^{ikz}
=
\frac{1-e^{iKz}}{K(1-e^{iz})}
}
\tag{17}
\]

away from removable singularities.

Equation (16) is the decisive representation audit. The source really has `K` separated `H`-scale carrier pieces, but after they are recombined into one normalized source they do not behave like `K` independent observations. They produce one coherent trigonometric factor.

On the real axis `P_K(0)=1`, while the central coherence peak has width `Theta(1/K)` in the scaled variable `Hv`; equivalently its physical vertical width is

\[
\boxed{
|v|\lesssim\frac1{KH}.
}
\tag{18}
\]

The corresponding Bellotti carrier capacity is therefore

\[
\boxed{
J_K:=\frac{R}{KH}=\frac JK.
}
\tag{19}
\]

The assumption `J/K -> infinity` ensures that this new capacity still grows. Notice that `J_K` has emerged from the exact carrier factor (16); it was not introduced by relabeling the component shell width.

The same phenomenon is visible from the usual Dirichlet-kernel asymptotic. For `|z|<=c/K`,

\[
P_K(z)=1+O(K|z|),
\tag{20}
\]

whereas away from the coherence lattice

\[
|P_K(z)|
\le
\min\!\left(1,\frac{2}{K|1-e^{iz}|}\right).
\tag{21}
\]

Thus averaging more positive carrier pieces suppresses the old broad `1/H` response, but only by concentrating it into narrower coherence peaks.

## 3. A replacement matched packet survives in the central coherence peak

Fix an integer `q>=1` and a bounded target depth `d_*`. Define

\[
\boxed{
J_K:=\frac JK,
\qquad
M_K:=\lfloor\delta J_K\rfloor,
}
\tag{22}
\]

where `delta>0` will be chosen sufficiently small, independently of `J`.

Take an abstract matched packet of zeros with ordinates

\[
\boxed{
\gamma_j-t_0
=
\frac{2\pi qj}{X},
\qquad
0\le j<M_K,
}
\tag{23}
\]

and common horizontal depth

\[
\boxed{
X(1-\beta_j)
=
\log J_K+d_*.
}
\tag{24}
\]

As in `NB-231`, this is a compatibility control, not a claim that actual zeta zeros realize the packet.

Put

\[
a_K:=\sigma_X-\beta_j
=
\frac{r+\log J_K+d_*}{X}
\tag{25}
\]

and

\[
v_j=(\gamma_j-t_0)+ia_K.
\tag{26}
\]

The large carrier phases are exactly aligned:

\[
e^{iX(\gamma_j-t_0)}=1.
\tag{27}
\]

Moreover the original shell envelope is essentially constant on the packet. Indeed,

\[
|H(\gamma_j-t_0)|
\le
\frac{2\pi q\delta}{YK}
=o(1),
\tag{28}
\]

while

\[
Ha_K
=
\frac{r+\log J_K+d_*}{YJ}
=o(1).
\tag{29}
\]

Hence

\[
\boxed{
F(Hv_j)=F(0)+o(1)
}
\tag{30}
\]

uniformly for `j<M_K`, with

\[
F(0)=\int_0^1\phi(y)\,dy>0.
\tag{31}
\]

It remains to check that the multi-carrier factor is also coherent. For every `0<=k<K` and `0<=j<M_K`,

\[
\begin{aligned}
|kCH(\gamma_j-t_0)|
&\le
KCH\frac{2\pi q\delta J_K}{X}\\
&=
\frac{2\pi qC\delta}{Y}+o(1).
\end{aligned}
\tag{32}
\]

Choose `delta` so small that the right side is below a fixed small angle, say `pi/6`, uniformly once `Y` lies in a fixed compact subset of `(0,infinity)`. The imaginary displacement across the full comb obeys

\[
\begin{aligned}
KCHa_K
&=
\frac{CK}{YJ}
\bigl(r+\log J_K+d_*\bigr)\\
&=o(1)
\end{aligned}
\tag{33}
\]

by (5). Therefore every summand in `P_K(CHv_j)` lies in one fixed positive angular sector and has modulus `1+o(1)`. Consequently there is a constant `c_0>0` such that

\[
\boxed{
\Re P_K(CHv_j)\ge c_0
}
\tag{34}
\]

uniformly for all packet points and all sufficiently large `J`.

Finally,

\[
\begin{aligned}
e^{iXv_j}
&=
 e^{-Xa_K}e^{iX(\gamma_j-t_0)}\\
&=
 e^{-r}e^{-X(1-\beta_j)}\\
&=
\boxed{
\frac{e^{-r-d_*}}{J_K}.
}
\end{aligned}
\tag{35}
\]

Combining (16), (30), (34), and (35), after shrinking `delta` if necessary,

\[
\Re L_K(v_j)
\ge
\frac{c_1}{J_K}
\tag{36}
\]

for a fixed `c_1>0`. Summing the `M_K=Theta(J_K)` packet points yields

\[
\boxed{
\liminf_{J\to\infty}
\Re\sum_{j=0}^{M_K-1}L_K(v_j)
\ge
c_1\delta
>0.
}
\tag{37}
\]

Thus the positive comb has not removed the order-one matched obstruction. It has only changed the packet size from `Theta(J)` to `Theta(J/K)` and moved the dangerous horizontal layer accordingly.

## 4. The critical layer shifts by exactly `log K`

Let the old Ford coordinate be

\[
d:=X(1-\beta)-\log J.
\tag{38}
\]

The coherence-peak capacity (19) suggests the natural replacement coordinate

\[
d_K:=X(1-\beta)-\log J_K.
\tag{39}
\]

Since `J_K=J/K`,

\[
\boxed{
d_K=d+\log K.}
\tag{40}
\]

Therefore the packet (24), which has `d_K=d_*`, lies at

\[
\boxed{
d=-\log K+d_*.}
\tag{41}
\]

This is the same horizontal compensation mechanism found for literal dilation in `NB-252`, but it has a different source origin. There,

\[
H\mapsto KH
\]

forced `J -> J/K` definitionally. Here every source component still has width `H`; instead the normalized carrier polynomial itself creates a `1/(KH)` coherence window and hence an **effective** capacity `J/K`.

The old critical layer `d=O(1)` is genuinely weakened by the comb. Each point there still carries size `Theta(1/J)`, while only `Theta(J/K)` carrier cells fit coherently inside the central Dirichlet peak, so its coherent mass falls to `Theta(1/K)`. But (41) supplies the replacement layer: there each point carries

\[
 e^{-X(1-\beta)}
\asymp
\frac1{J_K}
=
\frac KJ,
\tag{42}
\]

and `Theta(J_K)` coherent cells again sum to order one.

This distinction matters for the `NB-251` bandwidth audit. `NB-251` holds the old `J`, old depth mark and old selected-height window fixed while hypothetically averaging the same marked zero current across a super-`H` carrier band. The comb (6) does not provide that operation. Its carrier pieces are recombined **before** the zero current is squared or averaged, and the recombination changes the vertical coherence geometry itself.

## 5. The replacement packet remains compatible with the audited zeta constraints

The packet uses

\[
M_K\asymp\frac JK
\tag{43}
\]

points and occupies vertical diameter

\[
\operatorname{diam}_\gamma\mathcal P_K
\asymp
\frac{J_K}{X}
=
\frac1{YKH},
\tag{44}
\]

which is exactly the central coherence width (18).

Its Bellotti horizontal depth is

\[
D_K^{(R)}
:=
R(1-\beta_j)
=
\frac{\log J_K+d_*}{Y}.
\tag{45}
\]

Because `J_K -> infinity` but `J_K<=J<=log Q`,

\[
D_K^{(R)}
=O(\log\log Q)
=o(\log Q),
\tag{46}
\]

so the packet remains inside the shallow range where the local Bellotti disk control used in `NB-224` and `NB-230` is available.

At ordinate spacing `Theta(1/X)=Theta(1/R)`, a Bellotti disk of radius `D/R` meets only `O(D)` consecutive packet points, matching the same local-population geometry used to validate `NB-231`. The total population `Theta(J/K)` is below the old `Theta(J)` carrier budget. No already-audited absolute population input excludes it.

The zero-free region does not exclude the replacement layer either. Its physical horizontal displacement satisfies

\[
X(1-\beta_j)
=
\log J_K+O(1)
\longrightarrow\infty,
\tag{47}
\]

whereas the Ford zero-free boundary corresponds to a fixed positive normalized displacement at `X asymp R`. Thus the packet lies safely to the left of that forbidden boundary.

The condition `K log J/J ->0` is also essential to the present control. It guarantees that the rightmost shell in the comb sees essentially the same horizontal damping as the leftmost one. If `K` approaches `J/log J`, the imaginary factor in (33) is no longer negligible and a fresh audit is required.

## 6. Representation audit, prior art, and the remaining escape

The generic harmonic-analysis ingredient in this finding is elementary: a normalized equally spaced carrier comb has a Dirichlet-kernel Fourier factor with coherence scale inverse to its span. The line-specific content is the interaction of that exact factor with the Ford quantities already fixed by the source representation:

\[
J=R/H,
\qquad
 e^{-X(1-\beta)},
\qquad
\gamma-t_0\asymp X^{-1},
\tag{48}
\]

which produces the replacement coordinate (40) and the order-one packet (37).

A fresh prior-art scan found only the expected classical separated-frequency/large-sieve framework of Montgomery--Vaughan and the recent short-interval zeta pair-correlation theorem of Biao Wang (arXiv:2609.07918, submitted 7 September 2026). The former concerns mean-square control of trigonometric sums and the latter derives pair-correlation information in short intervals; neither supplies or analyzes this source-side positive multi-shell normalization at the Ford critical layer. No external theorem is load-bearing in (16), (34), or (40), so `SOURCES.md` needs no new durable entry.

The conclusion is deliberately narrower than “multi-carrier averaging cannot work.” The argument uses a **single positive equal-weight source** in which all carrier pieces are linearly recombined before the residual is tested. Architectures not covered include:

- signed or complex carrier coefficients whose Fourier polynomial does not behave like a positive normalized coherence kernel;
- several carrier observables retained as an `ell^2` family until after the Hardy projection rather than collapsed into one scalar source;
- nonuniform carrier geometries designed to suppress every order-one coherence peak while keeping source normalization controlled.

Any such escape must now audit a sharper requirement. It is not enough to show that the convex hull of source frequencies has width `W>>H`. One must show that the resulting operation supplies **independent carrier energy at that width while the effective selected-height capacity and the Ford depth normalization remain at the old `J` scale**. If the operation creates a coherence peak of width `1/W`, the dangerous layer simply slides to the population capacity supported by that peak.

## 7. Claim boundary

`NB-253` is source-side. It does not prove that zeta zeros realize the replacement packet, does not prove a new zero-density theorem, and does not close the Nyman--Beurling distance bridge. Its matched packet is an adversarial compatibility control showing that the already-audited zero-free, local-population and carrier constraints do not force the positive comb residual to decay.

The source mass calculation uses positivity and equal weights. Signed/complex coefficients can have substantially different normalization and coherence behavior and are intentionally left open. Likewise, `K=o(J/log J)` is a mesoscopic regime in which all carrier centers stay at `X+o(X)` and their Ford damping is asymptotically common; no claim is made at `K` comparable with `J`.

The durable delta over `NB-252` is therefore:

\[
\boxed{
\text{fixed-}H\text{ positive }K\text{-shell comb}
\quad\Longrightarrow\quad
\text{Dirichlet peak width }(KH)^{-1},
\quad
J_{\rm eff}=J/K,
\quad
d_{\rm crit}=-\log K+O(1).
}
\tag{49}
\]

So the first canonical multi-carrier realization of `W/H -> infinity` does **not** realize the fixed-window hypothesis of `NB-251`; it exports the apparent bandwidth gain into a narrower vertical coherence window and a shallower Ford critical layer.