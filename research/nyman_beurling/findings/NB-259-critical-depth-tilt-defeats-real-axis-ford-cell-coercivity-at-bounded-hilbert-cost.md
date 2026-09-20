# NB-259 — Critical-depth tilt defeats real-axis Ford-cell coercivity at bounded Hilbert cost

> **Representation:** _Nyman–Beurling / Hardy-projected vantage._ The line-specific data are the positive Mellin shell scale `H`, Ford scale `R`, capacity `J=R/H`, exact Euler normalization, the `H`-resolved signed carrier dictionary of `NB-257`--`NB-258`, and the legal zero evaluation identified in `NB-249`/`NB-255`. The generic engine is minimum-norm two-point interpolation for a short exponential sum. This is a route correction: it shows that the real-axis full-cell coercivity of `NB-258` cannot be transferred directly to the legally projected critical-zero line, because that line sits at imaginary Ford distance `Theta(log J)`.

**Date:** 2026-09-21  
**Status:** `EXACT-DERIVED + HARDY-PROJECTED-ZERO-EVALUATION + H-SEPARATED-SIGNED-CARRIER + CRITICAL-DEPTH-TILT + MINIMUM-L2-INTERPOLATION + LOGARITHMIC-IMAGINARY-SEPARATION + NB-258-ROUTE-CORRECTION + DESTINATION-INTERFACE + METHOD-BOUNDARY + FRESH-PRIOR-ART-AUDIT`.

`NB-258` proves a genuine source-side obstruction: for bounded shell-Hilbert cost and any fixed exponent gap `K <= J^(1-delta)`, the Ford-rescaled carrier

\[
C_J(x):=B_\lambda(x/R),\qquad C_J(0)=1,
\]

has a positive `L^2` floor on every fixed real Ford interval. The open question is whether this real-axis floor survives the legal Hardy/Nyman destination map.

It does not survive by a direct coercive transfer. The reason is geometric and specific to the exact zero mark. After the Euler normalization of `NB-255`, a zero `rho=beta+i gamma` samples the signed carrier at

\[
z_\rho=(\gamma-t_0)+i(1-\beta).
\]

In the critical Ford layer

\[
d_\rho=X(1-\beta)-\log J=O(1),
\]

its Ford-rescaled imaginary coordinate is not bounded:

\[
\boxed{
R(1-\beta)=\frac{\log J+d_\rho}{Y}=\Theta(\log J),
\qquad Y:=X/R\asymp1.
}
\]

That logarithmic vertical displacement changes the interpolation price. On the same disjoint `H`-grid used in `NB-257`--`NB-258`, an exact notch at the center of the critical-depth line has minimum coefficient `ell^2` cost

\[
\boxed{
\|c\|_2\asymp \frac{J}{(\log J)K^{3/2}}.
}
\]

Consequently the notch already has bounded physical shell-Hilbert cost at

\[
\boxed{
K\asymp\left(\frac{J}{\log J}\right)^{2/3},
}
\]

strictly below the real Ford-scale one-notch crossover `J^(2/3)` of `NB-257`.

More importantly, at that crossover the carrier derivative in Ford coordinates is only `O(1/log J)`. Hence one exact critical-depth notch suppresses not merely one point but every fixed complex Ford cell around it:

\[
\boxed{
\sup_{|x|\le A,\ |d|\le D}
\left|
B_\lambda\!\left(
\frac{x}{R}+i\frac{\log J+d}{YR}
\right)
\right|
\ll_{A,D}\frac1{\log J}.
}
\]

At the same time `C_J(0)=1`, and `NB-258` still forces order-one energy on fixed **real** Ford intervals. Thus the two statements coexist:

\[
\int_I|C_J(x)|^2dx\gg_I1,
\qquad
\int_I|C_J(x+i\log J/Y)|^2dx\ll_I(\log J)^{-2}.
\]

The source real-axis floor therefore does not by itself control the legally projected critical-zero samples. A successful destination-side lower bound must use more than `NB-258`'s real-axis carrier energy; it must control analytic continuation through the logarithmic Ford-depth displacement, or use a genuinely Hardy/Nyman quantity that is coercive on the sampled complex line.

This does **not** suppress the full hard Ford window. A fixed Ford cell has `R(\gamma-t_0)=O(1)`, while the hard `1/H` ordinate window has `R(\gamma-t_0)=O(J)`. Nor does the construction eliminate the shallower replacement layers isolated in `NB-255`. It only closes the naive route “real source-band floor => projected critical-cell floor”.

## 1. Exact destination evaluation is vertically displaced by `log J`

Retain the normalization from `NB-249`, `NB-255`, and `NB-258`:

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

Fix

\[
0<a<b<1,
\qquad
0\le\phi\in C_c^\infty((a,b)),
\qquad
\phi\not\equiv0,
\tag{2}
\]

with `diam(supp phi)<1`. For odd `K`, use the resolved offsets

\[
\xi_j=jH,
\qquad
-m\le j\le m,
\qquad
K=2m+1,
\tag{3}
\]

and the Euler-normalized coefficient measure

\[
\lambda=\sum_{j=-m}^m c_j\delta_{\xi_j},
\qquad
\sum_jc_j=1.
\tag{4}
\]

As in `NB-257`, the physical shell coefficients are obtained from

\[
d\nu(\xi)=e^{r\xi/X}\,d\lambda(\xi),
\tag{5}
\]

so the normalized Euler return is exact. Because the translated shell supports are disjoint,

\[
H\|h_\nu\|_2^2
=\|\phi\|_2^2
\sum_j e^{2r\xi_j/X}|c_j|^2.
\tag{6}
\]

Whenever `K=o(J)`, the span is `W\asymp KH=o(R)\asymp o(X)` and therefore

\[
H^{1/2}\|h_\nu\|_2
=(1+o(1))\|\phi\|_2\|c\|_2.
\tag{7}
\]

Define

\[
B_\lambda(z):=\sum_jc_j e^{i\xi_jz},
\qquad
C_J(w):=B_\lambda(w/R)
=\sum_jc_j e^{ijw/J}.
\tag{8}
\]

The exact Euler normalization gives

\[
C_J(0)=1.
\tag{9}
\]

`NB-255` proves that the additional signed carrier factor at a zero is not evaluated on the real axis. With

\[
z_\rho:=(\gamma-t_0)+i(1-\beta),
\tag{10}
\]

the full source transform contributes exactly `B_lambda(z_rho)` after the fixed `r/X` displacement has cancelled against the Euler weighting. Linearity of the positive-frequency Hardy projection in `NB-249` preserves this factor in the finite zero mark.

If

\[
d_\rho:=X(1-\beta)-\log J,
\tag{11}
\]

then

\[
Rz_\rho
=R(\gamma-t_0)
+i\frac{\log J+d_\rho}{Y}.
\tag{12}
\]

Thus a bounded critical-depth box `|d_rho|<=D` is sampled on a horizontal strip centered at imaginary Ford height

\[
\boxed{
A_J:=\frac{\log J}{Y}\to\infty.
}
\tag{13}
\]

This is precisely the direction absent from the real-axis coercivity statement of `NB-258`.

## 2. A critical-depth notch costs `J/(A_J K^(3/2))`

Consider the exact two-point interpolation problem

\[
C_J(0)=1,
\qquad
C_J(iA_J)=0.
\tag{14}
\]

Put

\[
\varepsilon_J:=\frac{A_J}{J},
\qquad
e:=(1)_{j=-m}^m,
\qquad
v:=(e^{-j\varepsilon_J})_{j=-m}^m.
\tag{15}
\]

Then (14) is

\[
c\cdot e=1,
\qquad
c\cdot v=0.
\tag{16}
\]

Assume temporarily

\[
K\varepsilon_J=\frac{KA_J}{J}=o(1).
\tag{17}
\]

Let `P_(v^perp)` denote Euclidean orthogonal projection. The minimum-`ell^2` solution of (16) is

\[
c_*=\frac{P_{v^\perp}e}{\|P_{v^\perp}e\|_2^2},
\qquad
\|c_*\|_2
=\frac1{\|P_{v^\perp}e\|_2}.
\tag{18}
\]

Because the grid is symmetric,

\[
\sum_jj=0,
\qquad
\sum_jj^2=\frac{K(K^2-1)}{12}.
\tag{19}
\]

Uniformly under (17),

\[
v=e-\varepsilon_J(j)_j+O(\varepsilon_J^2j^2),
\tag{20}
\]

and the first-order perturbation is orthogonal to `e`. Hence

\[
\|P_{v^\perp}e\|_2
=(1+o(1))\varepsilon_J
\left(\sum_jj^2\right)^{1/2}
=(1+o(1))\frac{A_JK^{3/2}}{\sqrt{12}J}.
\tag{21}
\]

Therefore

\[
\boxed{
\min\{\|c\|_2:(16)\}
=(1+o(1))\frac{\sqrt{12}J}{A_JK^{3/2}}.
}
\tag{22}
\]

The same scaling also follows as a lower bound directly from Cauchy--Schwarz:

\[
1
=\left|\sum_jc_j(1-e^{-j\varepsilon_J})\right|
\le
\|c\|_2
\left(\sum_j|1-e^{-j\varepsilon_J}|^2\right)^{1/2},
\tag{23}
\]

and the second factor is `(1+o(1))A_J K^(3/2)/(sqrt(12)J)`. Thus (22) is a genuine sharp crossover, not merely one explicit construction.

Take now

\[
\boxed{
K\asymp\left(\frac{J}{A_J}\right)^{2/3}
\asymp
\left(\frac{J}{\log J}\right)^{2/3}.
}
\tag{24}
\]

Then (17) holds because

\[
\frac{KA_J}{J}
\asymp
\left(\frac{A_J}{J}\right)^{1/3}	o0,
\tag{25}
\]

and (22) gives

\[
\|c_*\|_2=O(1).
\tag{26}
\]

By (7), the actual disjoint-shell source has bounded shell-Hilbert cost. Also

\[
\|c_*\|_1\le\sqrt K\|c_*\|_2
=O\!\left((J/\log J)^{1/3}\right),
\tag{27}
\]

so under the standing conservative restriction `J<=log Q` the same PNT/Stieltjes error ledger used in `NB-255`--`NB-257` remains harmless. The normalized Euler return is not being bought by an exploding arithmetic error.

Equation (24) is smaller than the real Ford one-notch scale `J^(2/3)` by the factor `(log J)^(-2/3)`. The gain is exactly the logarithmic imaginary separation of the destination sample.

## 3. One exact notch suppresses a whole fixed critical Ford cell

Let `c=c_*` from (18), so

\[
C_J(iA_J)=0.
\tag{28}
\]

For complex `w`, differentiation of (8) gives

\[
C_J'(w)
=\sum_jc_j\frac{ij}{J}e^{ijw/J}.
\tag{29}
\]

Fix constants `A,D>0`, and let `Y` remain in a fixed compact subinterval of `(0,infinity)`. On the complex patch

\[
\mathcal P_{A,D,J}
:=\left\{
 w=x+i\left(A_J+\frac dY\right):
 |x|\le A,\ |d|\le D
\right\},
\tag{30}
\]

the exponential weights in (29) are uniformly `1+o(1)` in modulus because `KA_J/J=o(1)`. Cauchy--Schwarz, (19), and (26) therefore give

\[
\sup_{w\in\mathcal P_{A,D,J}}
|C_J'(w)|
\ll
\|c\|_2\frac{K^{3/2}}J
\ll
\frac1{A_J}.
\tag{31}
\]

Every point of (30) lies a bounded Euclidean distance from `iA_J`. Integrating (31) along the straight segment from `iA_J` and using (28) yields

\[
\boxed{
\sup_{w\in\mathcal P_{A,D,J}}
|C_J(w)|
\ll_{A,D,Y_-,Y_+}
\frac1{A_J}
\asymp
\frac1{\log J}.
}
\tag{32}
\]

Returning to the zero variable through (12), (32) is exactly

\[
\boxed{
\sup_{\substack{|R(\gamma-t_0)|\le A\\ |d_\rho|\le D}}
|B_\lambda(z_\rho)|
\ll_{A,D}
(\log J)^{-1}.
}
\tag{33}
\]

Thus the critical-depth tilt converts one two-point interpolation constraint into uniform suppression on every fixed complex Ford cell around the selected height.

The geometry is also visible from the affine limit. At the crossover (24),

\[
\|C_J''\|_\infty
\ll
\frac{K^{5/2}}{J^2}
\asymp
J^{-1/3}A_J^{-5/3},
\tag{34}
\]

and even after multiplication by `A_J^2` the right side tends to zero. Hence on the rectangle joining the origin to the critical-depth cell,

\[
C_J(w)=1+\frac{iw}{A_J}+o(1),
\tag{35}
\]

uniformly on bounded horizontal translates of `0<=Im w<=A_J`. The real-axis profile is therefore almost constant, while its vertical translate through `iA_J` is almost zero:

\[
C_J(x)=1+O(A_J^{-1}),
\qquad
C_J(x+iA_J)=\frac{ix}{A_J}+o(1)
\tag{36}
\]

for every fixed bounded real `x`.

This is fully consistent with `NB-258`, not a contradiction to it.

## 4. The legal Hardy-projected mark inherits the suppression factor

For the smooth shell, the single-channel zero coefficient reconstructed by the positive-frequency Hardy projection in `NB-249` is

\[
\frac{e^{-r-d_\rho}}J
m(\rho)\chi(d_\rho)
 e^{iX(\gamma-t_0)}
F(\tau_\rho+i\eta_\rho).
\tag{37}
\]

For the signed resolved mixture, linearity and the exact Euler identity of `NB-255` multiply (37) by

\[
B_\lambda(z_\rho).
\tag{38}
\]

Therefore every zero in a fixed critical Ford cell (33) gains the deterministic factor

\[
O((\log J)^{-1}).
\tag{39}
\]

This is the precise destination-interface statement. The real-axis carrier floor of `NB-258` does not survive as a pointwise lower bound after the legal zero evaluation, even though the actual source Hilbert norm remains bounded and the Euler return remains normalized.

For the same family, `NB-258` still applies on every fixed real interval `I` because (24) lies well inside a fixed-power regime, for example `K<=J^(3/4)` for large `J`. Thus

\[
\liminf_{J\to\infty}
\int_I|C_J(x)|^2dx>0,
\tag{40}
\]

while (32) gives

\[
\boxed{
\int_I|C_J(x+iA_J)|^2dx
\ll_I A_J^{-2}	o0.
}
\tag{41}
\]

Equations (40)--(41) are the clean separation: **real source-cell coercivity is not stable under the logarithmic imaginary translation imposed by the critical Ford depth.**

## 5. What this closes, and what it does not

The result closes one tempting continuation of `NB-258`. It is not enough to prove a lower bound for `B_lambda(x/R)` on real fixed Ford intervals and then appeal to the Hardy projection as if it sampled the same geometry. The legal zero mark samples a complex line whose distance from the real axis grows like `log J`; bounded source `L^2` does not make evaluation across that displacement coercive.

The result is deliberately **cell-local**. A hard selected-height Ford window has

\[
|\gamma-t_0|=O(1/H),
\qquad
|R(\gamma-t_0)|=O(J),
\tag{42}
\]

whereas (33) controls only `|R(gamma-t_0)|=O(1)`. The `Theta(J)`-cell matched packet of `NB-231` can therefore still survive away from the notched cell. No claim is made that (24) suppresses the full hard-box current or the complete carrier-band form factor of `NB-250`.

Nor does the notch eliminate the shallower replacement layer predicted by `NB-255`. The construction spends coefficient variation to destroy coherence at the original critical depth `X(1-beta)~log J`; an adversarial packet may move toward smaller horizontal depth. The next source/destination calculation should therefore keep the **whole depth ladder** and the hard `O(J)` Ford ordinate range simultaneously, rather than adding more isolated notches without tracking where the obstruction relocates.

Finally, the construction is allowed to depend on the selected local parameters `(J,Y,t_0)`. Turning such local sources into one global Nyman approximant would require a separate assembly argument and is not asserted here.

## 6. Prior-art and novelty boundary

The generic interpolation mechanism is classical. Minimum-energy interpolation of band-limited signals and the associated cost of superoscillation are well established; Ferreira and Kempf, *Superoscillations: Faster Than the Nyquist Rate*, IEEE Trans. Signal Processing 54 (2006), 3732--3740, DOI `10.1109/TSP.2006.877642`, is a representative reference. The present proof does not depend on a theorem from that paper: the two-constraint minimum norm and its asymptotics are derived directly in (18)--(23).

A fresh targeted search also checked Nyman--Beurling Hardy/Mellin formulations and did not locate this particular coupling of the Euler-normalized resolved shell, the exact Hardy-projected zero evaluation, and the logarithmic imaginary Ford displacement. This is only a prior-art boundary, not a uniqueness claim. No new external theorem is load-bearing, so `SOURCES.md` does not need a new durable dependency.

The line-specific content is the conjunction of four already established facts: the legal one-copy Hardy projection of `NB-249`, the exact Euler-weighted carrier evaluation of `NB-255`, the disjoint-shell Hilbert geometry of `NB-257`, and the real-axis fixed-power coercivity of `NB-258`. Together they expose a destination geometry that none of the four facts alone identifies.

## 7. Adversarial audit

The strongest possible misreading would be to call (33) a solution of the Ford current. It is not. The hard window contains `Theta(J)` Ford cells, while (33) covers only `O(1)` cells. A packet can re-lock outside the notched cell, and the source has not acquired the super-`H` independent averaging needed to control all of them.

A second misreading would be that `NB-258` is false. It remains exactly true: our carrier is almost one on bounded real Ford intervals, so its real-axis energy is maximally non-small. The new point is that the destination samples a line vertically translated by `Theta(log J)`, where that same affine carrier is almost zero.

A third concern is hidden coefficient cancellation. There is none at the physical source level: the shells are `H`-separated with disjoint supports, and (6)--(7) make the coefficient `ell^2` cost equal to the shell-Hilbert cost up to the fixed profile factor. The bounded cost in (26) is therefore genuine.

A fourth concern is the imaginary exponential weight for negative `j`. It is harmless in the claimed cell because `KA_J/J=o(1)`, so all factors `exp(-j Im(w)/J)` remain uniformly `1+o(1)` there. This same small parameter is what makes the asymptotic projection calculation (21) and derivative bound (31) uniform.

The remaining theorem must therefore be genuinely two-dimensional in Ford coordinates: it must decide whether one can suppress, at bounded Nyman cost, the full `O(J)` horizontal cell range while following the critical and shallower depth layers, or whether the Hardy/Nyman geometry restores a lower bound only after that global coupling is retained.
