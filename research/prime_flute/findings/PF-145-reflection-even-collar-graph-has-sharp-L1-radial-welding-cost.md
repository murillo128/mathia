# PF-145 — reflection-even collar graph has sharp `L^1` radial welding cost

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-144 identifies the sharp local Güneysu--Thalmaier wave-weight currency of the reflection-odd angular trace on a pinching collar as its unweighted `L^1` amplitude. The independent transverse/radial interface-shape gate has the same endpoint currency. On a fixed interior cross-section of every sufficiently short standard collar, a small reflection-even radial graph `rho(theta)` can be straightened to the standard cross-section by a reflection-equivariant bi-Lipschitz map with inverse-unit-ball weighted cost `O(||rho||_1)`, uniformly in the collapsing core length; every small radial-only straightening pays at least `c||rho||_1`. A simultaneous small radial-plus-angular trace has a sufficient cost `O(||rho||_1+||psi||_1)`. Thus collar collapse gives no discount to radial shape error and no stronger derivative norm is intrinsically forced. This does **not** estimate the actual prime/shift-clone traces and does not complete the global wave-operator comparison.

## Claim

Let

\[
C_L^+=[0,w(L)]\times\mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

be a standard hyperbolic half-collar with

\[
g_L=dr^2+L^2\cosh^2(r)\,d\theta^2,
\qquad \theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Put inward distance from the outer collar boundary

\[
y=w(L)-r.
\tag{3}
\]

For all sufficiently small `L`, use the fixed interior interface `y=1` and its inward welding slab `1<=y<=2`. Let `rho in C^1(S^1)` satisfy the reflection parity

\[
\boxed{\rho(-\theta)=\rho(\theta)}
\tag{4}
\]

and

\[
\varepsilon:=\max\{\|\rho\|_\infty,\|\rho'\|_\infty\}<\varepsilon_0.
\tag{5}
\]

There are absolute constants `L_0, epsilon_0, c, C>0` such that, for `0<L<L_0`, there is a reflection-equivariant bi-Lipschitz radial straightening

\[
F_\rho(y,\theta)=(y+v(y,\theta),\theta)
\tag{6}
\]

supported in `1<=y<=2`, with interface trace

\[
F_\rho(1,\theta)=(1+\rho(\theta),\theta),
\tag{7}
\]

and

\[
\boxed{\operatorname{Bilip}(F_\rho)\le1+C\varepsilon.}
\tag{8}
\]

For the local weighted metric-deviation functional

\[
\mathcal W_{L,[1,2]}(F)
:=
\int_{\{1\le y\le2\}}
\mu_{g_L}(B_{g_L}(z,1))^{-1}
\delta_{g_L,F^*g_L}(z)\,d\mu_{g_L}(z),
\tag{9}
\]

one has

\[
\boxed{
\mathcal W_{L,[1,2]}(F_\rho)
\le C\|\rho\|_{L^1(\mathbb S^1)}.
}
\tag{10}
\]

Conversely, within the small radial-only near-isometric class with the same trace (7),

\[
\boxed{
\mathcal W_{L,[1,2]}(F)
\ge c\|\rho\|_{L^1(\mathbb S^1)}.
}
\tag{11}
\]

The constants in (8)--(11) are independent of `L`. Hence the sharp local radial-only welding scale is

\[
\boxed{
\inf_{F\in\mathcal R(\rho)}\mathcal W_{L,[1,2]}(F)
\asymp\|\rho\|_1,
}
\tag{12}
\]

with no factor depending on the pinching core length.

Moreover, if a normalized interface trace has the full reflection-equivariant Fermi-coordinate form

\[
\Gamma(\theta)=\bigl(1+\rho(\theta),\theta+\psi(\theta)\bigr),
\qquad
\rho(-\theta)=\rho(\theta),
\quad
\psi(-\theta)=-\psi(\theta),
\tag{13}
\]

and both components are sufficiently `C^1`-small, then a simultaneous local correction exists with

\[
\boxed{
\mathcal W_{L,[1,2]}(F_{\rho,\psi})
\le C\left(\|\rho\|_1+\|\psi\|_1\right).
}
\tag{14}
\]

Equation (14) is only a sufficient upper bound. PF-145 does **not** assert a matching two-sided estimate for arbitrary coupled radial/angular maps; the sharp lower bounds are established separately for the pure angular sector in PF-143/PF-144 and for the pure radial sector in (11).

## 1. A fixed interior collar slab is uniformly noncollapsing

In the `y` coordinate the metric is

\[
g_L=dy^2+a_L(y)^2d\theta^2,
\tag{15}
\]

where

\[
\begin{aligned}
a_L(y)
&=L\cosh(w(L)-y)\\
&=L\coth(L/2)\cosh y
 -L\operatorname{csch}(L/2)\sinh y.
\end{aligned}
\tag{16}
\]

Therefore, uniformly on every fixed compact `y` interval,

\[
\boxed{a_L(y)\longrightarrow2e^{-y}}
\qquad(L\to0).
\tag{17}
\]

In particular, on the slightly enlarged slab `1/2<=y<=5/2`,

\[
0<c_0\le a_L(y)\le C_0<\infty,
\tag{18}
\]

and

\[
\boxed{
0<c_1
\le\left|\partial_y\log a_L(y)\right|
=\tanh(w(L)-y)
\le1
}
\tag{19}
\]

for all sufficiently small `L`. The local curvature is constantly `-1`; (18), together with the fixed-width embedded slab, gives uniform upper and lower bounds for unit-ball area there. Consequently

\[
\boxed{
\mu_{g_L}(B_{g_L}(z,1))^{-1}d\mu_{g_L}(z)
\asymp dy\,d\theta
}
\tag{20}
\]

uniformly on `1<=y<=2` as `L->0`.

This is the key calibration. The core circumference tends to zero far deeper in the collar, but a fixed-distance cross-section measured from the **outer** boundary stays at order-one circumference. Any interface correction performed there is therefore charged at an order-one weighted density.

## 2. Adaptive radial depth realizes the `L^1` amplitude

Write `x=y-1 in [0,1]`. For `rho` not identically zero define

\[
\boxed{
v(x,\theta)
=\operatorname{sgn}(\rho(\theta))
\bigl(|\rho(\theta)|-\varepsilon x\bigr)_+,
}
\tag{21}
\]

and take `v=0` when `rho=0`. Since `epsilon>=||rho||_infty`, (21) vanishes before `x=1`, while

\[
v(0,\theta)=\rho(\theta).
\tag{22}
\]

Away from the measure-zero free boundary,

\[
|v_x|
=\varepsilon\mathbf 1_{\{|\rho|>\varepsilon x\}},
\qquad
|v_\theta|
\le|\rho'|\mathbf 1_{\{|\rho|>\varepsilon x\}}.
\tag{23}
\]

Fubini gives the exact or one-sided endpoint estimates

\[
\int_0^1|v_x|\,dx=|\rho|,
\tag{24}
\]

\[
\int_0^1|v_\theta|\,dx
\le\frac{|\rho'||\rho|}{\varepsilon}
\le|\rho|,
\tag{25}
\]

and

\[
\int_0^1|v|\,dx
=\frac{|\rho|^2}{2\varepsilon}
\le\frac12|\rho|.
\tag{26}
\]

Thus

\[
\boxed{
\int_0^1\int_{\mathbb S^1}
\left(|v|+|v_x|+|v_\theta|\right)d\theta dx
\le C\|\rho\|_1.
}
\tag{27}
\]

Because soft thresholding preserves evenness, (4) implies `v(x,-theta)=v(x,theta)`, so the standard zero-twist collar reflection is preserved.

## 3. Hyperbolic metric deviation has the same local scale

For

\[
F(y,\theta)=(y+v(y,\theta),\theta),
\tag{28}
\]

the differential in source and target orthonormal frames is

\[
M=
\begin{pmatrix}
1+v_y & v_\theta/a_L(y)\\
0 & a_L(y+v)/a_L(y)
\end{pmatrix}.
\tag{29}
\]

Equations (18)--(19) and smallness of `epsilon` imply

\[
\left|
\frac{a_L(y+v)}{a_L(y)}-1
\right|
\le C|v|
\tag{30}
\]

and hence

\[
\|M^TM-I\|
\le C\left(|v|+|v_y|+|v_\theta|\right).
\tag{31}
\]

This proves (8), and the same finite-dimensional comparison for the Güneysu--Thalmaier metric-deviation scalar gives

\[
\delta_{g_L,F^*g_L}
\le C\left(|v|+|v_y|+|v_\theta|\right).
\tag{32}
\]

Combining (20), (27), and (32) proves (10).

The construction is Lipschitz and piecewise smooth. As in PF-144, its free boundary can be rounded inside the same fixed slab with arbitrarily small multiplicative loss in the displayed budget if a later global scattering argument requires a smooth comparison. PF-145 itself does not invoke the global wave-operator theorem.

## 4. Collapse cannot lower the radial-only cost

Now let a small radial-only map (28) have trace (7), remain inside the enlarged fixed slab, and be tail-near-isometric. In that regime the matrix (29) and the metric deviation determine each of its small strain components uniformly. In particular,

\[
|v_y|
\le C\delta_{g_L,F^*g_L},
\tag{33}
\]

while the second diagonal component and the lower bound in (19) give

\[
|v|
\le C\left|
\log\frac{a_L(y+v)}{a_L(y)}
\right|
\le C\delta_{g_L,F^*g_L}.
\tag{34}
\]

For every fixed `theta`, the one-dimensional trace inequality on `0<=x<=1` gives

\[
|\rho(\theta)|
=|v(0,\theta)|
\le
\int_0^1\left(|v|+|v_x|\right)dx.
\tag{35}
\]

Integrating (35) in `theta`, then using (20), (33), and (34), yields (11).

Thus the radial graph mode has exactly the same qualitative feature as PF-144's angular mode: **the local optimal cost is its `L^1` trace amplitude, not that amplitude multiplied by the shrinking core length**.

## 5. Radial and angular traces can be corrected together at additive `L^1` cost

Let `(rho,psi)` satisfy (13), and choose a common small

\[
\varepsilon
\ge
\max\{
\|\rho\|_\infty,\|\rho'\|_\infty,
\|\psi\|_\infty,\|\psi'\|_\infty
\}.
\tag{36}
\]

Apply the same soft-threshold profile to each component,

\[
v(x,\theta)=S_{\varepsilon x}(\rho(\theta)),
\qquad
u(x,\theta)=S_{\varepsilon x}(\psi(\theta)),
\tag{37}
\]

and set

\[
F_{\rho,\psi}(y,\theta)
=(y+v(y,\theta),\theta+u(y,\theta)).
\tag{38}
\]

The derivative matrix now contains the radial terms from (29), the angular terms of PF-144, and products that are quadratic in the common `C^1` size. Uniform geometry on the fixed slab and the same Fubini calculation give

\[
\mathcal W_{L,[1,2]}(F_{\rho,\psi})
\le
C\left(\|\rho\|_1+\|\psi\|_1\right),
\tag{39}
\]

which proves (14). Even/odd parity makes (38) reflection-equivariant and preserves the PF-142 angular anchors.

No general coupled lower bound is claimed. In particular, one should not smuggle an `L^1` Korn inequality into the argument: coupled radial/angular strains can interact, and such an endpoint coercivity statement would require its own proof. For the current watch, the one-sided combined bound is enough to identify a sufficient global summability target.

## 6. Consequence for the accepted shift-clone wave clue

PF-144 left two local questions at every PF-138 short separator: the actual reflection-odd angular trace and the transverse/radial shape mismatch between the body comparison and PF-128's optimized standard-collar map. PF-145 removes the **local norm-selection ambiguity** in the second question.

If a globally coherent body map induces on a fixed interior interface of the `eta`th short collar a small reflection-equivariant trace

\[
\Gamma_\eta(\theta)
=\bigl(1+\rho_\eta(\theta),
\theta+\psi_\eta(\theta)\bigr),
\tag{40}
\]

with `C^1` size tending to zero and

\[
\boxed{
\sum_\eta
\left(
\|\rho_\eta\|_1+\|\psi_\eta\|_1
\right)<\infty,
}
\tag{41}
\]

then the complete family of local short-collar interface weldings has finite total inverse-unit-ball weighted metric-deviation cost. PF-144 already supplies the angular part; PF-145 supplies the radial part and shows they can be inserted simultaneously at additive cost.

What remains is no longer a generic extension-theory question. One must prove that the **actual** PF-139/PF-140 prime/shift body comparison reaches a chosen fixed interior collar cross-section as a small graph, compute or bound the resulting `rho_eta` and `psi_eta`, and establish (41). Only after those estimates and the global smoothing/quasi-isometry/completeness checks can the Güneysu--Thalmaier criterion be invoked.

A failure of (41) for the actual canonical traces could still be a substantive negative result. What PF-145 rules out is a different failure mode: radial interface shape does not intrinsically demand a `W^{1,1}`-type global derivative ledger, nor is it automatically cheap because the underlying geodesic is short.

## 7. Prior-art and novelty audit

The scattering target remains the Güneysu--Thalmaier theorem recorded as `S16` in `research/prime_flute/SOURCES.md`: it supplies a sufficient inverse-unit-ball weighted metric-deviation criterion for complete wave operators under quasi-isometric metric perturbations without a global injectivity-radius lower bound. PF-145 does not strengthen that theorem.

The soft-threshold extension and the one-dimensional trace lower bound above are elementary local constructions. They are consistent with the classical endpoint fact that `W^{1,1}` trace theory naturally has `L^1` boundary data and that nonlinear right inverses can avoid charging an artificial full derivative norm. The project-specific content here is narrower: after putting a collapsing hyperbolic collar in the exact fixed-interior coordinates (15)--(20), the Güneysu--Thalmaier weight remains uniformly order one, so the radial graph component has the sharp `L^1` cost (12) with **no core-length factor**, and it composes with PF-144's marked angular sector as in (14).

The prior-art audit found general Sobolev trace/extension theory, bilipschitz extension theory, hyperbolic collar lemmas, and metric-scattering perturbation criteria, but no theorem that already states this prime-flute-specific fixed-collar weighted calibration. Accordingly PF-145 is classified as an exact derived boundary lemma for the present comparison problem, **not** as a claimed new general theorem.

## Evidence boundary

PF-145 proves only a local statement for a prescribed small interface graph inside a standard collar. It does not prove:

- that the actual prime/shift-clone body trace is a `C^1`-small graph on the chosen interface;
- that the actual amplitudes satisfy (41);
- that all local corrections assemble into one smooth complete global quasi-isometry;
- existence or completeness of the relative wave operators;
- equality of scattering matrices, resonances, discrete spectra, determinants, Selberg/Ruelle objects, or any RH statement.

It also does not repair the first-resolvent trace-class failure of PF-112 or promote the above-`S_1` Schatten information of PF-126/PF-127 to trace class. Its durable conclusion is only the sharp local radial welding currency and the additive sufficient vector-trace budget (41).