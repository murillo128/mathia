# ANF-052 — central-notch two-pair five-point perturbation is cubic on bounded heights

**Status:** `EXACT-DERIVED + UNIFORM-BOUNDED-HEIGHT-PERTURBATION + CUBIC-NOTCH-SENSITIVITY + UNIFORM-FAMILY-COERCIVITY + STRUCTURAL-REDUCTION`. `ANF-034` constructs the explicit central-notch ray

\[
J_s=J_{\rm MT}-s\phi_\eta,
\qquad
\phi_\eta(\alpha)=b_\eta\left(1-\frac{|\alpha|}{\eta}\right)_+,
\qquad 0<b_\eta\le1,
\tag{1}
\]

while `ANF-046` shows that its pair-functional gain after paying the exact elementary normalization slack is order `s b_eta`, with slack only order `s b_eta eta`. The remaining cardinality-five issue is the two-conjugate-pair defect of `ANF-040`--`ANF-051`. A narrow central notch perturbs that defect on every bounded height range only at **cubic order in the notch width**. More precisely, for every fixed `Y>0`, uniformly over

\[
0<y_1,y_2\le Y,
\qquad t_1,t_2\in\mathbb R,
\]

one has an explicit bound

\[
\boxed{
\begin{aligned}
|H_{J_s}-H_{J_{\rm MT}}|
\le s b_\eta\Bigg[&
\frac56(2\pi Y)^2\cosh(2\pi\eta Y)\,\eta^3\\
&+\frac1{15}(2\pi Y)^4\cosh^2(2\pi\eta Y)\,\eta^5
\Bigg].
\end{aligned}
}
\tag{2}
\]

Consequently, as `eta->0` with `Y` fixed,

\[
\boxed{
\sup_{\substack{0<y_1,y_2\le Y\\t_1,t_2\in\mathbb R}}
|H_{J_s}-H_{J_{\rm MT}}|
\le
\frac{10}{3}\pi^2Y^2\,s b_\eta\eta^3
+O_Y(s b_\eta\eta^5).
}
\tag{3}
\]

The physical five-point energy difference is `4H_J`, so its perturbation is bounded by four times (2). No horizontal compactness, phase localization, or cancellation between frequencies is used.

There is also a family-level vertical consequence. A positive-frequency interval on which `J_MT` is bounded below lies outside every sufficiently narrow central notch. The coercivity proof of `ANF-043` can therefore be made uniform over the entire family (1): there are constants `eta_0>0` and `Y_infty<infinity`, depending only on `J_MT`, such that for every

\[
0<\eta<\eta_0,
\qquad 0\le s\le1,
\]

and every two-pair geometry with

\[
\max(y_1,y_2)\ge Y_\infty,
\]

one has

\[
\boxed{H_{J_s}(y_1,y_2;t_1,t_2)>0}
\tag{4}
\]

uniformly in the horizontal positions. Thus all possible negative two-pair defects of every sufficiently narrow notch lie below one **notch-independent height ceiling**, and throughout that entire relevant height range the perturbation from Montgomery--Taylor is controlled by the cubic estimate (2).

## 1. The exact two-pair integrand has a simple amplitude envelope

Retain the `ANF-042` notation for

\[
W=\{x_1\pm iy_1,x_2\pm iy_2,r\},
\qquad
t_j=x_j-r,
\qquad
d=t_1-t_2,
\]

and write

\[
E_F(W)-E_F(R(W))=4H_J
=4\int J(\alpha)h_\alpha\,d\alpha.
\tag{5}
\]

At a fixed frequency define

\[
a=\cosh(2\pi\alpha y_1)-1,
\qquad
b=\cosh(2\pi\alpha y_2)-1,
\]

\[
p=a+b,
\qquad q=a-b,
\qquad
C=\cos(\pi\alpha d),
\qquad S=\sin(\pi\alpha d).
\tag{6}
\]

With the common mean phase `m` and

\[
R=\sqrt{p^2C^2+q^2S^2},
\]

`ANF-042` gives the exact normal form

\[
h_\alpha
=R^2+4pC^2+pC\cos m-qS\sin m.
\tag{7}
\]

Since `a,b>=0`,

\[
|q|\le p,
\qquad
0\le R\le p.
\tag{8}
\]

The final two terms in (7) have absolute value at most `R`. Therefore every frequency, every pair of heights, and every horizontal geometry satisfy

\[
\boxed{
|h_\alpha|
\le R^2+4pC^2+R
\le p^2+5p.
}
\tag{9}
\]

This envelope is intentionally coarse. `ANF-051` gives the exact phase-dependent sign region, but (9) is better suited to perturbation theory because it is phase free and vanishes quadratically with frequency near the origin.

## 2. A notch supported near zero can only see quadratic hyperbolic amplitude

Fix `Y>0` and assume

\[
0<y_1,y_2\le Y,
\qquad
|\alpha|\le\eta.
\]

Put

\[
z:=2\pi\eta Y.
\]

For `0<=u<=z`, the integral identity

\[
\cosh u-1
=\int_0^u(u-v)\cosh v\,dv
\]

gives

\[
\boxed{
\cosh u-1
\le\frac{u^2}{2}\cosh z.
}
\tag{10}
\]

Applying (10) to both hyperbolic amplitudes in (6) yields

\[
\begin{aligned}
p
&\le
\frac{(2\pi|\alpha|)^2}{2}
(y_1^2+y_2^2)\cosh(2\pi\eta Y)\\
&\le
(2\pi Y)^2\cosh(2\pi\eta Y)\,\alpha^2.
\end{aligned}
\tag{11}
\]

Define

\[
A_{Y,\eta}
:=(2\pi Y)^2\cosh(2\pi\eta Y).
\tag{12}
\]

Then (9)--(12) imply the uniform pointwise estimate

\[
\boxed{
|h_\alpha|
\le
A_{Y,\eta}^2\alpha^4
+5A_{Y,\eta}\alpha^2
\qquad(|\alpha|\le\eta).
}
\tag{13}
\]

The forced `alpha^2` factor is the mechanism. A central spectral perturbation cannot couple at zeroth or first order to a genuine vertical split because every hyperbolic amplitude `cosh(2pi alpha y)-1` has a double zero at the central frequency.

## 3. Exact tent moments give the cubic perturbation law

Because the geometry-dependent integrand `h_alpha` is linear in the spectral weight,

\[
H_{J_s}-H_{J_{\rm MT}}
=-s\int\phi_\eta(\alpha)h_\alpha\,d\alpha.
\tag{14}
\]

The central tent has exact even moments

\[
\boxed{
\int\phi_\eta(\alpha)\alpha^2\,d\alpha
=\frac{b_\eta\eta^3}{6},
\qquad
\int\phi_\eta(\alpha)\alpha^4\,d\alpha
=\frac{b_\eta\eta^5}{15}.
}
\tag{15}
\]

Indeed, for `k=2,4`,

\[
2b_\eta\int_0^\eta
\left(1-\frac\alpha\eta\right)\alpha^k\,d\alpha
=
\frac{2b_\eta\eta^{k+1}}{(k+1)(k+2)}.
\]

Combining (13)--(15) proves exactly

\[
|H_{J_s}-H_{J_{\rm MT}}|
\le
s b_\eta
\left(
\frac{5A_{Y,\eta}}6\eta^3
+
\frac{A_{Y,\eta}^2}{15}\eta^5
\right),
\tag{16}
\]

which is (2). Expanding

\[
\cosh(2\pi\eta Y)=1+O_Y(\eta^2)
\]

then gives (3).

The estimate is uniform in `t_1,t_2` and also in `s in [0,1]`. It does not require the curvature condition `m_5(J_s)>=0`; that condition remains useful for proving positivity near the real axis, but the cubic perturbation law itself is a direct finite-height consequence of the exact `ANF-042` integrand.

## 4. The whole narrow-notch family shares one high-height safety ceiling

`ANF-043` proves height coercivity for each fixed nonzero positive spectrum by choosing a positive-frequency interval

\[
I=[\beta,\gamma]
\subset(0,1)
\]

on which the spectrum is bounded below, with `beta>1/2`. For the exact Montgomery--Taylor spectrum, `J_MT` is continuous and strictly positive on `(-1,1)`. Fix once and for all numbers

\[
\frac12<\beta<\gamma<1
\]

and put

\[
j_0:=\min_{\alpha\in I}J_{\rm MT}(\alpha)>0.
\tag{17}
\]

Choose

\[
\eta_0<\beta.
\tag{18}
\]

Then every notch (1) with `eta<eta_0` is supported away from `I`, so

\[
\boxed{
J_s(\alpha)=J_{\rm MT}(\alpha)
\qquad(\alpha\in I)
}
\tag{19}
\]

for all `0<=s<=1`. In particular the interval lower bound `j_0`, the interval mass, and the anti-phase leakage constant `c_I` used in `ANF-043` are identical for the entire family. The only global negative contribution in that proof is controlled by the universal pointwise floor `h_alpha>=-1/4` times the total spectral mass. But

\[
\int J_s
\le
\int J_{\rm MT}.
\tag{20}
\]

Therefore every constant in the two large-height cases of `ANF-043` can be chosen using only `J_MT`, the fixed interval `I`, and one fixed height-disparity split parameter. The resulting threshold `Y_infty` is independent of `s` and `eta<eta_0`. This proves (4).

This family-level statement is stronger than applying `ANF-043` separately after choosing a notch. It removes a possible nonuniformity: the obstruction box does not drift to arbitrarily large height as the notch narrows.

## 5. The notch has a three-scale hierarchy

`ANF-046` gives the exact elementary normalization slack

\[
\boxed{\delta_s=s b_\eta\eta}
\tag{21}
\]

and the exact post-slack pair-functional improvement

\[
\boxed{
m_{\rm MT}-\bigl(M(F_s)+\delta_s\bigr)
=s b_\eta
\left(1-2\eta+\frac{\eta^2}{3}\right).
}
\tag{22}
\]

For narrow `eta`, this is order `s b_eta`. On any bounded height range the new estimate gives instead

\[
\boxed{
|H_{J_s}-H_{J_{\rm MT}}|
=O_Y(s b_\eta\eta^3).
}
\tag{23}
\]

Hence the central-notch construction has the scale separation

\[
\boxed{
\text{objective gain }\asymp s b_\eta,
\qquad
\text{normalization slack }\asymp s b_\eta\eta,
\qquad
\text{bounded-height two-pair response }=O_Y(s b_\eta\eta^3).
}
\tag{24}
\]

The complex five-point layer is therefore **two powers of notch width smaller than the already-subleading normalization cost**, and three powers smaller than the leading objective gain. This does not prove that `J_s` passes the two-pair gate: `H_{J_MT}` may itself approach or attain zero on the residual shape domain, so even a cubic perturbation could decide the sign there. What (24) proves is that finite-height complex sensitivity cannot generically consume the leading notch advantage at order `s b_eta` or `s b_eta eta`.

The curvature estimate of `ANF-038` fits the same hierarchy: its bound

\[
m_5(J_s)
\ge
m_5(J_{\rm MT})-rac56s b_\eta\eta^3
\tag{25}
\]

is another manifestation of the same double central zero. The present result extends that cubic sensitivity from the infinitesimal curvature gate to the **entire two-pair defect on every bounded height range**.

## 6. Prior art, falsification, and evidence boundary

No new external theorem is load-bearing. The positive Fourier--Laplace framework for complex strip kernels is already anchored in `SOURCES.md` through Buescu--Paixão--Symeonides, and the Montgomery--Taylor extremizer is already anchored through Carneiro--Chandee--Littmann--Milinovich. The new argument is the elementary amplitude envelope (9), the hyperbolic Taylor bound (10), and the exact tent moments (15). A targeted check of the neighboring positive-definite strip and bandlimited pair-correlation literature found the expected general frameworks but no theorem needed for (2)--(4). No publication-level novelty claim is made, and no `SOURCES.md` update is required.

The main falsification checks are finite. Expanding (7) must reproduce the exact `ANF-042` normal form. The inequality `R<=p` follows from `|q|<=p`, so (9) holds without assuming a favorable phase. Equation (10) follows directly from the integral remainder and is uniform on `0<=u<=2pi eta Y`. The tent moments in (15) are exact. Finally, the common high-height ceiling uses only a fixed outer interval untouched by the notch and the fact that removing nonnegative spectral mass cannot worsen the `F(0)/4` term in the `ANF-043` lower bounds.

This finding does **not** prove a positive lower bound for `H_{J_MT}` on the complete finite-height two-pair domain, does not prove `H_{J_s}>=0` for every five-point configuration, and does not establish the full universal affine counting inequality of `ANF-005`. It also does not control configurations of cardinality greater than five. The estimate is perturbative in spectral width, not a sign theorem.

## 7. Consequence for the next gate

For the central-notch branch the remaining five-point question can now be organized around the Montgomery--Taylor base profile rather than around the notch itself. Choose a fixed outer interval and the common high-height ceiling `Y_infty` from Section 4. On

\[
0<y_1,y_2\le Y_\infty,
\]

every sufficiently narrow notch differs from `H_{J_MT}` by at most the explicit cubic quantity in (2), uniformly over all horizontal placements.

Thus the decisive next task is to understand the **zero/margin structure of the Montgomery--Taylor two-pair defect** on the already-localized finite-height domain from `ANF-044`--`ANF-051`. A certified positive margin `mu` on a residual region would immediately transfer to every notch whose right side in (2) is `<mu`. Where the Montgomery--Taylor margin vanishes or becomes too small, one should instead characterize that zero set and compare the sign of the explicit notch correction there. Either route is now quantitatively sharper than treating the full notched four-variable coherence problem from scratch.