# NB-255 — Signed scalar carriers pay a total-variation coherence tax

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + SIGNED-COMPLEX-MIXTURE + EULER-NORMALIZED + TOTAL-VARIATION-TAX + COHERENCE-WINDOW + MATCHED-CONTROL + NB-254-EXTENSION + METHOD-BOUNDARY + SOURCE-ONLY + FRESH-PRIOR-ART-AUDIT`.

`NB-254` shows that every **positive** scalar mixture whose carrier centers occupy a span `W` has an unavoidable coherence window of width `Theta(1/W)`. It deliberately leaves signed or complex coefficients open: cancellation can make the normalized Fourier factor small much closer to the origin than positivity allows.

There is nevertheless a quantitative obstruction. After normalizing by the actual Euler weight at

\[
\sigma_X=1+\frac rX,
\]

a signed or complex mixture with Euler-weighted coefficient total variation `V` remains order-one coherent throughout a disk of radius at least `c/(WV)`. Consequently, if

\[
J_*:=\frac{R}{WV}\to\infty,
\]

then a matched Ford packet with `Theta(J_*)` points still fits inside that compulsory coherent region and contributes order one. In the original Ford coordinate

\[
d=X(1-\beta)-\log J,
\qquad J=\frac RH,
\]

the replacement critical layer is

\[
\boxed{
d=-\log\!\big((W/H)V\big)+O(1).
}
\]

Thus signs do not remove the scalar obstruction for free. To evade this particular forced-coherence mechanism, the Euler-normalized coefficient variation must at least reach the scale `R/W`, so that `J_*` no longer grows.

This does **not** yet prove that such a large coefficient variation creates the same-size Nyman--Beurling or Hardy-space norm cost. Overlapping signed shells may cancel after convolution or projection. The result is therefore a source-side method boundary: it quantifies the conditioning price required to destroy the central scalar coherence window, and isolates the remaining question of whether the projected source can hide that price.

## 1. Signed scalar mixture and the correct Euler normalization

Retain the exact-Ford normalization of `NB-230`--`NB-254`:

\[
Q:=\log(10+|t_0|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
Y:=\frac XR\asymp1,
\qquad
J:=\frac RH\to\infty,
\tag{1}
\]

with the conservative matched-control restriction

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

and write

\[
F(z):=\int_0^1\phi(y)e^{iyz}\,dy,
\qquad F(0)>0.
\tag{4}
\]

Let `nu=nu_J` be an arbitrary finite signed or complex measure supported in

\[
[-W/2,W/2],
\tag{5}
\]

and define the scalar multi-shell source

\[
\boxed{
h_\nu(u)
:=
\int
\frac1H
\phi\!\left(\frac{u-X-\xi}{H}\right)
\,d\nu(\xi).
}
\tag{6}
\]

The exact carrier factor is

\[
L_\nu(v)
=
 e^{iXv}F(Hv)A_\nu(v),
\qquad
A_\nu(v):=\int e^{i\xi v}\,d\nu(\xi).
\tag{7}
\]

For positive mixtures `NB-254` normalized `nu` to have total mass one. With signs this is not the right invariant normalization, because the Euler source at `sigma_X` sees the component centered at `X+xi` with the extra factor `e^{-r xi/X}`. Define therefore

\[
Z_r(\nu)
:=
\int e^{-r\xi/X}\,d\nu(\xi).
\tag{8}
\]

A useful scalar source must have `Z_r(nu) != 0`. Rescale by this complex number and henceforth impose

\[
Z_r(\nu)=1.
\tag{9}
\]

Equivalently, introduce the Euler-weighted measure

\[
\boxed{
d\lambda(\xi):=e^{-r\xi/X}\,d\nu(\xi).
}
\tag{10}
\]

Then

\[
\lambda(\mathbb R)=1.
\tag{11}
\]

Its total variation

\[
\boxed{
V:=\|\lambda\|_{\mathrm{TV}}
}
\tag{12}
\]

satisfies `V>=1`. Since the regime below will imply `W/X -> 0`, fixed `r` also gives

\[
\|\nu\|_{\mathrm{TV}}
=(1+o(1))V.
\tag{13}
\]

This is the natural coefficient-conditioning parameter after the Euler return has been normalized to order one. Under the matched regime (28) below, `J_* -> infinity` implies eventually

\[
V<\frac RW\le J\le\log Q.
\]

Thus the uniform prime-number-theorem/Stieltjes error used in `NB-253` and `NB-254` remains `o(1)` after integration against the variation measure, and the same calculation gives

\[
\sum_{n\ge2}\Lambda(n)h_\nu(\log n)n^{-\sigma_X}
=
 e^{-r}\int_0^1\phi(y)e^{-rHy/X}\,dy+o(1)
\longrightarrow
 e^{-r}\int_0^1\phi(y)\,dy.
\tag{14}
\]

So increasing `V` is not being hidden by simultaneously increasing the normalized Euler return.

## 2. Generic lemma: total variation controls how fast normalized coherence can disappear

The key point is independent of zeta. Let `lambda` be any finite complex measure supported in `[-W/2,W/2]` with total mass one and total variation `V`. Set

\[
B_\lambda(z):=\int e^{i\xi z}\,d\lambda(\xi).
\tag{15}
\]

For every complex `z`,

\[
e^{i\xi z}-1
=
 i\xi z\int_0^1 e^{it\xi z}\,dt,
\tag{16}
\]

and therefore

\[
|e^{i\xi z}-1|
\le
|\xi|\,|z|e^{|\xi|\,|\Im z|}.
\tag{17}
\]

Integrating against the variation measure gives the elementary bound

\[
\boxed{
|B_\lambda(z)-1|
\le
\frac{WV}{2}|z|e^{W|\Im z|/2}.
}
\tag{18}
\]

In particular, because `V>=1`, if

\[
|z|\le\frac{1}{4WV},
\tag{19}
\]

then

\[
|B_\lambda(z)-1|
\le
\frac18 e^{1/8}<\frac14,
\tag{20}
\]

so

\[
\boxed{
\Re B_\lambda(z)\ge\frac34.
}
\tag{21}
\]

The constant is irrelevant; what matters is the guaranteed scale. A normalized signed or complex measure with support diameter `W` and total variation `V` has a compulsory order-one Fourier--Laplace coherence neighborhood containing the disk

\[
\boxed{
|z|\le \frac{c}{WV}
}
\tag{22}
\]

for an absolute `c>0`. This is a lower bound on the coherence radius, not a claim that every mixture loses coherence immediately outside that disk.

For `V=1`, equality in the triangle inequality forces positivity up to a common phase after normalization, and (22) recovers the `1/W` guaranteed scale of `NB-254`. Cancellation can make the guaranteed coherent disk smaller, but only in direct proportion to the coefficient variation spent on that cancellation.

## 3. Euler normalization removes the `r/X` shift exactly

For a zero `rho=beta+i gamma`, the Ford carrier is evaluated at

\[
v_\rho
=u_\rho+i(\sigma_X-\beta),
\qquad
u_\rho:=\gamma-t_0,
\tag{23}
\]

where the displayed `u_rho` is the real vertical displacement, not the measure `nu`. Using (10), the signed carrier factor satisfies the exact identity

\[
\begin{aligned}
A_\nu(v_\rho)
&=
\int e^{i\xi u_\rho}
 e^{-\xi(r/X+1-\beta)}\,d\nu(\xi)\\
&=
\int e^{i\xi u_\rho}e^{-\xi(1-\beta)}\,d\lambda(\xi).
\end{aligned}
\tag{24}
\]

Hence, with

\[
z_\rho:=u_\rho+i(1-\beta),
\tag{25}
\]

we have

\[
\boxed{
A_\nu(v_\rho)=B_\lambda(z_\rho).
}
\tag{26}
\]

This is why the weighted normalization is the clean one: the fixed Euler displacement `r/X` disappears exactly from the coherence problem. The only remaining imaginary displacement is the actual horizontal zero depth `1-beta`.

## 4. Effective Ford capacity for signed scalar carriers

Assume

\[
\boxed{
\frac WH\to\infty,
\qquad
J_*:=\frac{R}{WV}\to\infty.
}
\tag{27}
\]

Since `V>=1`, (27) implies `W/R -> 0`, hence `W/X -> 0`, justifying (13). It also gives

\[
J_*\le\frac RW\le\frac RH=J.
\tag{28}
\]

Fix an integer `q>=1` and a bounded real depth offset `d_*`. Let

\[
M_*:=\lfloor\delta J_*\rfloor,
\tag{29}
\]

where `delta>0` will be chosen sufficiently small depending only on `q` and a fixed compact range for `Y`.

Use the same matched-control ordinates as in `NB-231`, `NB-253`, and `NB-254`:

\[
\boxed{
\gamma_j-t_0
=
\frac{2\pi qj}{X},
\qquad
0\le j<M_*.
}
\tag{30}
\]

Then

\[
e^{iX(\gamma_j-t_0)}=1
\tag{31}
\]

for every point. Place all points at horizontal depth

\[
\boxed{
X(1-\beta_j)=\log J_*+d_*.
}
\tag{32}
\]

For the real displacement in (25),

\[
WV|u_j|
\le
\frac{2\pi qWV M_*}{X}
\le
\frac{2\pi q\delta}{Y}+o(1).
\tag{33}
\]

Choose `delta` so that this is at most `1/8` uniformly in the allowed range of `Y`. The imaginary displacement obeys

\[
WV(1-\beta_j)
=
\frac{\log J_*+d_*}{YJ_*}
\longrightarrow0.
\tag{34}
\]

Therefore, for all sufficiently large `J`,

\[
|z_j|\le\frac{1}{4WV}.
\tag{35}
\]

By (21),

\[
\Re A_\nu(v_j)
=
\Re B_\lambda(z_j)
\ge\frac34.
\tag{36}
\]

The original shell profile is simultaneously flat across the packet. Indeed,

\[
H|u_j|
\ll
\frac{H}{WV},
\tag{37}
\]

which tends to zero because `W/H -> infinity` and `V>=1`, while

\[
H(\sigma_X-\beta_j)
=
\frac{r+\log J_*+d_*}{YJ}
\longrightarrow0.
\tag{38}
\]

Thus

\[
F(Hv_j)=F(0)+o(1)
\tag{39}
\]

uniformly through the packet. Combining (36) and (39), after increasing the scale if necessary,

\[
\Re\!\left(F(Hv_j)A_\nu(v_j)\right)
\ge c_\phi>0
\tag{40}
\]

uniformly in `j`.

Finally,

\[
\begin{aligned}
e^{iXv_j}
&=
 e^{iX(\gamma_j-t_0)}e^{-X(\sigma_X-\beta_j)}\\
&=
 e^{-r}e^{-X(1-\beta_j)}\\
&=
\frac{e^{-r-d_*}}{J_*}.
\end{aligned}
\tag{41}
\]

Hence the matched packet contributes

\[
\begin{aligned}
\Re\sum_{j<M_*}L_\nu(v_j)
&\ge
\frac{e^{-r-d_*}}{J_*}
 c_\phi M_*\\
&\longrightarrow
\delta c_\phi e^{-r-d_*}>0.
\end{aligned}
\tag{42}
\]

We have therefore proved the control statement

\[
\boxed{
J_*\to\infty
\quad\Longrightarrow\quad
\text{the Euler-normalized signed scalar carrier still admits an order-one matched Ford packet.}
}
\tag{43}
\]

As in the earlier matched controls, this is a compatibility construction. It does not assert that the actual zeros of `zeta` realize these points.

## 5. The new critical coordinate includes the variation budget

From (32), the original Ford coordinate is

\[
\begin{aligned}
d
&:=X(1-\beta)-\log J\\
&=\log J_* -\log J+d_*\\
&=-\log\!\left(\frac{J}{J_*}\right)+d_*.
\end{aligned}
\tag{44}
\]

Since

\[
\frac{J}{J_*}
=
\frac{R/H}{R/(WV)}
=
\frac WH V,
\tag{45}
\]

we obtain

\[
\boxed{
d_{\mathrm{crit}}
=-\log\!\big((W/H)V\big)+O(1).
}
\tag{46}
\]

This interpolates the previous scalar obstructions:

\[
V=1
\quad\Longrightarrow\quad
 d_{\mathrm{crit}}=-\log(W/H)+O(1),
\tag{47}
\]

which is exactly the positive-mixture layer of `NB-254`. Allowing cancellation with variation `V` buys only the additional horizontal shift `-log V` in this guaranteed-coherence argument.

Equivalently, if

\[
V=o(R/W),
\tag{48}
\]

then `J_* -> infinity` and the matched obstruction survives. Therefore any signed/complex scalar design that hopes to escape **this particular forced-coherence argument** must enter the regime

\[
\boxed{
V\not=o(R/W),
}
\tag{49}
\]

and in a regular asymptotic design must pay variation on the scale

\[
V\gtrsim\frac RW
\tag{50}
\]

so that the guaranteed coherent capacity no longer diverges.

Equation (50) is a conditioning threshold, not yet a norm lower bound for the projected Nyman source.

## 6. Compatibility with the previously audited zeta inputs

The packet in section 4 is no larger or deeper than the positive packet already audited in `NB-254`. Indeed,

\[
M_*=\Theta(J_*)\le O(J)\le O(\log Q),
\tag{51}
\]

and its Ford/Bellotti depth is

\[
R(1-\beta)
=
\frac{\log J_*+O(1)}{Y}
=O(\log\log Q).
\tag{52}
\]

Its full vertical diameter is

\[
\operatorname{diam}_\gamma\mathcal P_*
\ll
\frac{J_*}{X}
=
\frac{1}{Y W V}
=o\!\left(\frac1H\right),
\tag{53}
\]

where the final relation follows from `W/H -> infinity` and `V>=1`. Thus the construction inherits the same compatibility audit with the zero-free input, the Bellotti growing-density allowance, local disk population, and ordinary zero count used for `NB-231` and `NB-254`.

No stronger statement is intended: those results do not construct such a packet, and this finding does not claim they do.

## 7. Adversarial review: what the variation tax does and does not prove

The main failure mode is to identify coefficient total variation with the actual analytic cost of the source. From (6) one has the easy upper bound

\[
\|h_\nu\|_{L^1}
\le
\|\phi\|_{L^1}\|\nu\|_{\mathrm{TV}},
\tag{54}
\]

but there is no matching lower bound in this argument. Nearby positive and negative shells may cancel strongly after convolution with `phi`; still more cancellation may occur after the Hardy projection used in the Nyman--Beurling route. Therefore (50) does **not** close the signed/complex escape.

The statement that survives adversarial review is narrower and exact:

> After normalizing the actual Euler return, a scalar carrier mixture of span `W` and Euler-weighted coefficient variation `V` necessarily retains order-one Fourier--Laplace coherence throughout a disk of radius `c/(WV)`. Whenever `R/(WV) -> infinity`, that disk is large enough to contain a growing matched Ford packet whose normalized contribution stays order one.

The genuinely open question is now whether a family with

\[
V\asymp R/W
\tag{55}
\]

or larger can suppress the scalar coherence peak **while keeping the convolved source and its Hardy projection admissibly conditioned**. Proving that the projected norm must inherit a comparable cost would close the signed-scalar route. Constructing a design where projection cancels the large coefficient variation without restoring a coherent Ford window would instead be a real escape.

The other qualitatively different route from `NB-254` remains untouched: keep multiple carrier channels as an `ell^2` family until after projection rather than collapsing them into one scalar source.

The local review also checks the normalization issue that is easy to miss with signs. Using raw mass `int dnu=1` would be incorrect at `sigma_X`; equations (8)--(26) show that the Euler-weighted measure is the invariant object, and with that normalization the `r/X` imaginary displacement cancels exactly.

**Adversarial-review verdict:** `pass`, with the explicit restriction that the theorem is a coefficient-conditioning/coherence statement and not a lower bound for the final Nyman--Beurling norm.

## 8. Representation and prior-art boundary

The lemma (18)--(22) is generic harmonic analysis: a compactly supported normalized Fourier--Stieltjes transform cannot move far from its value at the origin faster than its first absolute moment permits. The elementary proof above is sufficient; no external theorem is load-bearing.

The zeta/Nyman-specific content begins with the Euler-weighted normalization (8)--(14), the Ford scaling `X~R`, the matched population `R/(WV)`, the depth choice (32), and the conversion to the original critical coordinate (46). The finding is therefore classified as a **source-side method boundary with an abstract matched spectral control**, not as a new zero theorem or a quantitative Nyman--Beurling approximation theorem.

A fresh targeted prior-art search checked compactly supported signed/complex Fourier measures and Bernstein/Lipschitz-type transform bounds, together with signed/complex Nyman--Beurling and mollifier constructions. The generic variation estimate is classical in spirit, but no result found in that audit supplied this Ford-scaled `V`-dependent obstruction or the critical layer (46). Since the argument here is self-contained and uses no new external load-bearing theorem, `SOURCES.md` requires no update.

## Conclusion

`NB-254` left signs and complex phases as the most immediate scalar escape from positivity. `NB-255` quantifies what those signs must buy: after the Euler return is normalized, the carrier remains coherent throughout a guaranteed disk of radius `c/(WV)`, where `V` is the weighted coefficient total variation. The effective Ford capacity is therefore

\[
\boxed{
J_* = \frac{R}{WV},
}
\]

and the corresponding obstruction moves to

\[
\boxed{
d_{\mathrm{crit}}=-\log((W/H)V)+O(1).
}
\]

Hence every signed/complex scalar construction with `V=o(R/W)` remains inside the matched-packet obstruction. The only scalar regime not covered by this argument is precisely the high-variation regime `V` on the scale `R/W` or larger. The next useful source-side question is no longer whether signs can cancel the central peak—they can—but whether the amount of variation required to do so can be hidden by shell overlap and Hardy projection, or whether that conditioning necessarily reappears as a comparable analytic norm cost.