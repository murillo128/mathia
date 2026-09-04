# ANF-021 — symplectic scale mixtures pass the local cusp gate but fail the Montgomery--Taylor band

**Status:** `EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION + NONDETERMINANTAL-FILTER`. `ANF-020` turns the remaining universal-affine scalar ceiling into an exact diffraction-realizability problem and rules out stationary translation-invariant determinantal witnesses below contraction factor one. The natural classical escape is the circular symplectic bulk process: the `beta=4` log gas is Pfaffian, not determinantal, and its long-wavelength structure-factor slope is only one half of the sine-process slope. That improvement is real: it passes the local atom/cusp gate at the Montgomery--Taylor contraction. Nevertheless the **whole support-one band** rules it out, and the failure survives arbitrary convex mixtures of spatial scales.

Let

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\qquad
a:=C_{\rm MT}^{-1}
=0.753296067856070\ldots .
\tag{1}
\]

In unit-density bulk normalization the circular `beta=4` structure factor is

\[
S_4(t)=
\begin{cases}
\displaystyle
\frac{|t|}{2}-\frac{|t|}{4}\log\bigl|1-|t|\bigr|,&0<|t|<2,\\[2mm]
1,&|t|\ge2,
\end{cases}
\tag{2}
\]

with the familiar logarithmic singularity at `|t|=1`. Dilation to intensity `rho>0` gives the per-particle diffraction candidate

\[
\mu_\rho
=\rho\,\delta_0+S_4(\alpha/\rho)\,d\alpha.
\tag{3}
\]

For any probability measure `pi` on positive scales define

\[
\overline\mu
:=\int\mu_\rho\,d\pi(\rho)
=\overline\rho\,\delta_0+\overline S(\alpha)\,d\alpha,
\]

\[
\overline\rho:=\int\rho\,d\pi,
\qquad
\overline S(h):=\int S_4(h/\rho)\,d\pi(\rho).
\tag{4}
\]

Then

\[
\boxed{
\overline\mu\not\le
 a\bigl(\delta_0+|\alpha|\,d\alpha\bigr)
\quad\text{on }(-1,1)
}
\tag{5}
\]

for every such scale mixture. More strongly, once the atom condition `\overline\rho\le a` holds, the diffuse density exceeds `a|h|` on an interval of positive length beginning at `h=1/5`.

## 1. Source normalization and the local cusp

Forrester and Shen identify the circular `beta=4` ensemble with the circular symplectic ensemble and hence a Pfaffian point process. Their exact finite-`N` spectral form factor and bulk expansion give (2). For `0<t<1`,

\[
S_4(t)
=\frac t2-\frac t4\log(1-t)
=\frac t2+
\sum_{m=2}^{\infty}\frac{t^m}{4(m-1)}.
\tag{6}
\]

The older log-gas analysis of Forrester--Jancovici--McAnally gives the general small-wave-number law; after converting to the present `e^{2\pi i\alpha x}` convention, its leading slope is `2/beta`, agreeing with the coefficient `1/2` in (6).

A spatial dilation taking unit intensity to intensity `rho` sends the dimensionless structure factor to `S_4(h/rho)`, while the forward per-particle diffraction atom becomes `rho delta_0`, giving (3). From (6),

\[
S_4(t)=\frac t2+\frac{t^2}{4}+O(t^3)
\qquad(t\downarrow0).
\tag{7}
\]

Fatou's lemma applied to the nonnegative quotients therefore yields

\[
\liminf_{h\downarrow0}\frac{\overline S(h)}h
\ge
\frac12\int\frac{d\pi(\rho)}{\rho}.
\tag{8}
\]

If a local target `\overline\rho\le a` and `\overline S(h)\le a|h|+o(|h|)` were possible, then

\[
\int\frac{d\pi(\rho)}{\rho}\le2a.
\]

Cauchy--Schwarz gives

\[
1
\le
\left(\int\rho\,d\pi\right)
\left(\int\frac{d\pi}{\rho}\right)
\le2a^2,
\tag{9}
\]

so the **local** symplectic atom/cusp threshold is only

\[
\boxed{a\ge\frac1{\sqrt2}=0.70710678\ldots .}
\tag{10}
\]

This is strictly weaker than the DPP threshold `a>=1` from `ANF-020`, and `a_MT=0.753296...` lies on the allowed side. For one fixed scale the same calculation says the local constraints permit

\[
\frac1{2a}\le\rho\le a,
\tag{11}
\]

which is nonempty exactly when `a>=1/sqrt(2)`. Thus the Pfaffian candidate genuinely escapes the *local* DPP obstruction; it must be killed by finite-frequency information.

## 2. A global affine minorant at moderate frequency

Fix any `h>0` satisfying

\[
\frac ha\le\frac13,
\tag{12}
\]

and define

\[
f_h(\rho):=S_4(h/\rho).
\]

For `rho>h`, equation (6) gives

\[
f_h(\rho)
=\frac{h}{2\rho}
+\sum_{m=2}^{\infty}
\frac{h^m}{4(m-1)\rho^m}.
\tag{13}
\]

Every term `rho^{-m}` is decreasing and convex, so `f_h` is strictly decreasing and convex on `(h,\infty)`. Let `L_h` be its tangent line at `rho=a`:

\[
L_h(\rho)
=f_h(a)+f_h'(a)(\rho-a).
\tag{14}
\]

Then `f_h(rho)>=L_h(rho)` for `rho>h`.

For `rho<=h`, put `t=h/rho>=1`. Formula (2) obeys

\[
S_4(t)\ge1
\qquad(t\ge1).
\tag{15}
\]

Indeed, for `1<t<2`, writing `u=t-1` and using

\[
-\log u\ge\frac{2(1-u)}{1+u}
\qquad(0<u<1)
\tag{16}
\]

gives (15), while for `t>=2` equality holds.

It remains to compare the tangent with this unit floor. Put `t_h=h/a<=1/3`. Since `f_h'(a)<0`, the maximum of `L_h` on `0<rho<=h` occurs at `rho=0`, where

\[
L_h(0)=S_4(t_h)+t_hS_4'(t_h).
\tag{17}
\]

For `0<t<=1/3`,

\[
-\log(1-t)\le\frac{t}{1-t}\le\frac12,
\]

hence

\[
S_4(t)\le\frac5{24},
\qquad
S_4'(t)\le\frac34,
\]

and therefore

\[
L_h(0)\le\frac5{24}+\frac14
=\frac{11}{24}<1.
\tag{18}
\]

Combining the two scale regimes gives the **global affine minorant**

\[
\boxed{
S_4(h/\rho)\ge L_h(\rho)
\qquad(\rho>0,\ 0<h\le a/3).
}
\tag{19}
\]

Averaging (19) against `pi`, and using `\overline rho<=a` together with `f_h'(a)<0`, gives

\[
\boxed{
\overline S(h)
\ge S_4(h/a)
\qquad(0<h\le a/3).
}
\tag{20}
\]

Thus under the atom budget the single scale `rho=a` furnishes a universal lower envelope for the entire scale-mixture family over this initial portion of the Fourier band.

## 3. The lower envelope crosses the Montgomery--Taylor budget on a positive-measure interval

Write `t=h/a`. For `0<t<1`,

\[
S_4(t)>a h
\quad\Longleftrightarrow\quad
\frac12-\frac14\log(1-t)>a^2.
\tag{21}
\]

The left side is strictly increasing in `t`. It therefore suffices to verify (21) at

\[
h_0:=\frac15,
\qquad
t_0:=\frac1{5a}.
\tag{22}
\]

The exact expression (1) gives the safe enclosure

\[
0.75329<a<0.75330.
\tag{23}
\]

Using

\[
-\log(1-t)>t+\frac{t^2}{2}
\qquad(0<t<1),
\tag{24}
\]

we have

\[
t_0>\frac1{5(0.75330)}>0.26549
\]

and hence

\[
\frac12-\frac14\log(1-t_0)
>
\frac12+\frac{t_0}{4}+\frac{t_0^2}{8}
>0.57518,
\tag{25}
\]

whereas

\[
a^2<(0.75330)^2=0.56746089.
\tag{26}
\]

Thus (21) holds at `h_0`, and because its left side increases with `h`, it holds for every

\[
\boxed{
\frac15\le h\le\frac a3.
}
\tag{27}
\]

This interval has positive length because `a/3>0.25109`. Combining (20) and (27),

\[
\boxed{
\overline S(h)>a h
\qquad
\left(\frac15\le h\le\frac a3\right).
}
\tag{28}
\]

The contradiction is therefore genuinely **measure-level**, not a pointwise-density artifact: the absolutely continuous part of `\overline mu` exceeds the Montgomery--Taylor budget on a set of positive Lebesgue measure. For calibration only,

\[
S_4\!\left(\frac1{5a}\right)
=0.153230926741\ldots,
\qquad
\frac a5
=0.150659213571\ldots .
\tag{29}
\]

Equations (28)--(29) prove (5).

## 4. Why the logarithmic CSE singularity is not the real proof

For one intensity `rho<=a<1`, the logarithmic singularity of `S_4(h/rho)` occurs at `|h|=rho` inside the support-one band and already rules out domination. That observation is not stable under convexification: a non-atomic distribution of scales can smear individual logarithmic singularities into a finite averaged profile.

The affine-minorant argument is stronger. It uses only the regular branch `0<h/rho<1` plus the unit lower floor on the opposite side, and it forces excess over the target throughout the fixed interval (27) for **every** probability mixture of scales. This is precisely the kind of convexification allowed by the diffraction viewpoint of `ANF-020`.

The comparison with `ANF-020` is therefore structural. DPPs fail already because intensity and the infinitesimal cusp force `a>=1`. Symplectic Pfaffian statistics improve that local threshold to `1/sqrt(2)` and therefore survive the Montgomery--Taylor local test. They fail only when a nonzero fraction of the complete support-one band is enforced. Hyperuniform slope alone is not the right invariant for the remaining scalar problem.

## 5. Prior-art boundary

The random-matrix ingredients are classical or explicitly available in current literature. Forrester--Jancovici--McAnally derive the small-wave-number structure function and `beta <-> 4/beta` duality for the one-dimensional log gas. Forrester--Shen give the explicit circular `beta=4` spectral form factor in the bulk normalization used here and identify the `beta=4` state as Pfaffian.

A targeted search across circular/sine `beta` structure factors, hyperuniformity, Pfaffian processes, scale mixtures and Montgomery--Taylor pair-correlation bounds did not locate the specific convex-scale obstruction (19)--(28) or its application to the contracted Montgomery--Taylor diffraction target. No publication-level novelty claim is made. The derived content here is the exact matching of the known symplectic profile to `ANF-020`'s budget, the local threshold (10), and the positive-measure finite-frequency certificate (28).

## 6. Evidence boundary and next filter

This finding does **not** prove that the order interval in `ANF-020` is disjoint from the full convex diffraction body `K`, so it does not close the universal-affine scalar branch. It excludes one large and natural non-determinantal construction class: arbitrary convex mixtures of spatially rescaled unit-density `beta=4` CSE bulk diffraction profiles.

Nor is it necessary here to prove that every stationary CSE expected diffraction measure, or every scale mixture of them, belongs to `K`. The conclusion is negative: even granting those point-process profiles as candidate admissible witnesses, they violate the required envelope.

General `beta` log gases, mixtures of genuinely different correlation mechanisms, nonstationary limits, direct finite-cluster convexifications and separating-spectrum arguments remain open. The immediate falsification lesson is sharper than in `ANF-020`: a candidate can pass the atom and `|h|` cusp tests and still fail badly at moderate frequency. Future diffraction constructions should therefore be tested against a **band profile**, not only the hyperuniform exponent or its leading coefficient.

The configuration-level branch of `ANF-006` remains outside this scalar diffraction duality and is unaffected.