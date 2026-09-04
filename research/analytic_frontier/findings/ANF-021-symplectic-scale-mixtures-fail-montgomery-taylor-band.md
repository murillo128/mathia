# ANF-021 — symplectic scale mixtures pass the local cusp gate but fail the Montgomery--Taylor band

**Status:** `EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE/OBSTRUCTION + NONDETERMINANTAL-FILTER`. `ANF-020` turns the remaining universal-affine scalar ceiling into an exact diffraction-realizability problem and shows that no stationary translation-invariant determinantal process can supply the required contracted sine-process envelope. The most natural classical escape from that DPP obstruction is the circular symplectic bulk process: the `beta=4` log gas is Pfaffian rather than determinantal, and its long-wavelength structure-factor slope is only one half of the sine-process slope. This genuinely passes the local atom/cusp obstruction at the Montgomery--Taylor contraction. Nevertheless the full support-one band kills it, and the failure survives **arbitrary convex mixtures of spatial scales**.

Let

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\qquad
a:=a_{\rm MT}=C_{\rm MT}^{-1}
=0.753296067856070\ldots .
\]

In unit-density bulk normalization, the `beta=4` circular symplectic ensemble has limiting structure factor

\[
S_4(t)=
\begin{cases}
\displaystyle
\frac{|t|}{2}-\frac{|t|}{4}\log\bigl|1-|t|\bigr|,&0<|t|<2,\\[2mm]
1,&|t|\ge2,
\end{cases}
\tag{1}
\]

with the logarithmic singularity at `|t|=1`. After dilation to intensity `rho>0`, its per-particle diffraction candidate is

\[
\mu_\rho
=\rho\,\delta_0+S_4(\alpha/\rho)\,d\alpha.
\tag{2}
\]

For any probability measure `pi` on positive scales, put

\[
\overline\mu
:=\int\mu_\rho\,d\pi(\rho)
=\overline\rho\,\delta_0+\overline S(\alpha)\,d\alpha,
\quad
\overline\rho:=\int\rho\,d\pi,
\quad
\overline S(h):=\int S_4(h/\rho)\,d\pi.
\tag{3}
\]

Then

\[
\boxed{
\overline\mu\not\le
 a\bigl(\delta_0+|\alpha|\,d\alpha\bigr)
\quad\text{on }(-1,1)
}
\tag{4}
\]

for every such scale mixture. In fact, if the atom constraint `\overline\rho\le a` holds, the diffuse domination already fails at the fixed interior frequency

\[
h_0=\frac15.
\]

Thus convexifying scales does not repair the classical symplectic candidate. The important structural point is that this failure is **not visible from the slope at zero**: the local cusp test for `beta=4` has threshold only `a\ge1/\sqrt2`, and Montgomery--Taylor lies above that threshold. The obstruction has moved from local hyperuniformity to the finite-frequency shape of the whole band.

## 1. Primary-source structure factor

Forrester and Shen identify the circular `beta=4` ensemble with the circular symplectic ensemble and hence with a Pfaffian point process. Their exact finite-`N` spectral form factor and its bulk expansion give, in the unit-density scaling used here, the leading function (1). In particular, for `0<t<1`,

\[
S_4(t)
=\frac t2-\frac t4\log(1-t)
=\frac t2+\sum_{m=2}^{\infty}\frac{t^m}{4(m-1)}.
\tag{5}
\]

The older log-gas structure-function analysis of Forrester--Jancovici--McAnally gives the general small-wave-number law; after converting their Fourier variable to the present `e^{2\pi i\alpha x}` normalization, the leading slope is `2/beta`, so `beta=4` gives the `1/2` in (5).

If a stationary unit-density process is dilated so that its intensity becomes `rho`, the dimensionless structure factor rescales as

\[
S_{4,\rho}(h)=S_4(h/\rho),
\tag{6}
\]

while the forward diffraction atom becomes `rho delta_0`. This gives (2).

## 2. The Pfaffian process escapes the DPP local obstruction

Equation (5) gives

\[
S_4(t)=\frac t2+\frac{t^2}{4}+O(t^3)
\qquad(t\downarrow0).
\tag{7}
\]

For a scale mixture, Fatou's lemma applied to the nonnegative quotients yields

\[
\liminf_{h\downarrow0}\frac{\overline S(h)}h
\ge
\frac12\int\frac{d\pi(\rho)}{\rho}.
\tag{8}
\]

Hence domination by the Montgomery--Taylor-type local envelope

\[
\overline\rho\le a,
\qquad
\overline S(h)\le a|h|+o(|h|)
\tag{9}
\]

forces

\[
\int\frac{d\pi(\rho)}{\rho}\le2a.
\tag{10}
\]

Cauchy--Schwarz gives

\[
1
\le
\left(\int\rho\,d\pi\right)
\left(\int\frac{d\pi}{\rho}\right)
\le2a^2.
\tag{11}
\]

Therefore the **local** atom/cusp obstruction for symplectic scale mixtures is only

\[
\boxed{a\ge\frac1{\sqrt2}=0.70710678\ldots .}
\tag{12}
\]

This is strictly weaker than the determinantal threshold `a>=1` proved in `ANF-020`, and

\[
a_{\rm MT}=0.753296\ldots>\frac1{\sqrt2}.
\tag{13}
\]

For a single scale this is already visible directly: the local constraints permit

\[
\frac1{2a}\le\rho\le a,
\tag{14}
\]

which is a nonempty interval exactly when `a>=1/sqrt(2)`. Thus the `beta=4` Pfaffian class is a genuine test that escapes the **local** DPP no-go. Any argument that looked only at intensity plus the coefficient of the linear hyperuniform cusp would incorrectly leave it alive at the Montgomery--Taylor constant.

## 3. A fixed interior frequency kills every convex scale mixture

Set

\[
h_0:=\frac15,
\qquad
f(\rho):=S_4(h_0/\rho).
\tag{15}
\]

For `rho>h_0`, equation (5) applies with `t=h_0/rho<1` and gives

\[
f(\rho)
=\frac{h_0}{2\rho}
+\sum_{m=2}^{\infty}
\frac{h_0^m}{4(m-1)\rho^m}.
\tag{16}
\]

Every term `rho^{-m}` is decreasing and convex. Hence

\[
\boxed{f\text{ is strictly decreasing and convex on }(h_0,\infty).}
\tag{17}
\]

Let `L` be the tangent line to `f` at `rho=a`:

\[
L(\rho)=f(a)+f'(a)(\rho-a).
\tag{18}
\]

Convexity gives `f(rho)>=L(rho)` whenever `rho>h_0`.

For `rho<=h_0`, put `t=h_0/rho>=1`. Formula (1) satisfies

\[
S_4(t)\ge1
\qquad(t\ge1).
\tag{19}
\]

For `1<t<2`, write `u=t-1 in (0,1)` and use the elementary inequality

\[
-\log u\ge\frac{2(1-u)}{1+u};
\tag{20}
\]

substitution into (1) gives (19), while for `t>=2` it is equality by definition.

It remains only to check that the tangent line lies below this unit floor on the small-scale side. Put

\[
t_0:=\frac{h_0}{a}.
\]

The exact Montgomery--Taylor expression gives `0.75329<a<0.75330`, hence `t_0<1/3`. Since `f'(a)<0`, the maximum of `L` on `0<rho<=h_0` occurs at `rho=0`, and

\[
L(0)=S_4(t_0)+t_0S_4'(t_0).
\tag{21}
\]

For `0<t<=1/3`, the elementary upper bound `-log(1-t)<=t/(1-t)<=1/2` gives

\[
S_4(t)\le\frac5{24},
\qquad
S_4'(t)\le\frac34,
\]

so

\[
L(0)\le\frac5{24}+\frac14=\frac{11}{24}<1.
\tag{22}
\]

Combining (17)--(22) proves the global affine minorant

\[
\boxed{S_4(h_0/\rho)\ge L(\rho)\qquad(\rho>0).}
\tag{23}
\]

Average (23) against an arbitrary scale law `pi`. If the target atom bound holds, `\overline\rho<=a`, and because `f'(a)<0`,

\[
\begin{aligned}
\overline S(h_0)
&\ge
f(a)+f'(a)(\overline\rho-a)\\
&\ge f(a).
\end{aligned}
\tag{24}
\]

Thus the best possible scale mixture under the atom budget is already bounded below by the single scale `rho=a` at this frequency.

## 4. The tangent lower bound crosses the Montgomery--Taylor envelope

Because `t_0=h_0/a<1`,

\[
\frac{f(a)}{t_0}
=\frac12-\frac14\log(1-t_0).
\tag{25}
\]

The target value `a h_0` is `a^2 t_0`, so `f(a)>a h_0` is equivalent to

\[
\frac12-\frac14\log(1-t_0)>a^2.
\tag{26}
\]

This inequality has a comfortable elementary margin. Using

\[
-\log(1-t)>t+\frac{t^2}{2}
\qquad(0<t<1)
\tag{27}
\]

and the same enclosure `0.75329<a<0.75330`,

\[
t_0>\frac1{5(0.75330)}>0.26549,
\]

so the left side of (26) is larger than

\[
\frac12+\frac{t_0}{4}+\frac{t_0^2}{8}
>0.57518,
\tag{28}
\]

whereas

\[
a^2<(0.75330)^2=0.56746089.
\tag{29}
\]

Therefore (26) follows without a delicate numerical comparison. For calibration, the actual values are

\[
f(a)=0.153230926741\ldots,
\qquad
a h_0=0.150659213571\ldots .
\tag{30}
\]

Equations (24) and (30) give

\[
\boxed{
\overline S(1/5)
>\frac a5
}
\tag{31}
\]

for every convex scale mixture satisfying the atom condition `\overline rho<=a`. This contradicts the diffuse part of the desired domination and proves (4).

## 5. Why this is stronger than pointing at the CSE logarithmic singularity

For a single intensity `rho<=a<1`, the logarithmic singularity of `S_4(h/rho)` occurs at `|h|=rho` inside the support-one band and already kills domination. But that observation is not stable under convexification: a non-atomic distribution of scales can smear the individual logarithmic singularities into a finite averaged profile.

The tangent argument above is deliberately stronger. It uses only the exact sub-singular branch `0<h/rho<1` plus the unit lower floor on the other branch, and it proves failure at the **same regular frequency `h_0=1/5` for every probability mixture of scales**. Thus the obstruction survives precisely the convexification that is natural after `ANF-020` replaced individual configurations by the convex diffraction body `K`.

This is also why the local computation matters. The scale-mixture class is not being rejected for the same reason as DPPs. It genuinely improves the local cusp/atom tradeoff from `a>=1` to `a>=1/sqrt(2)`; the loss appears only when one asks for control over a nonzero fraction of the entire Fourier band.

## 6. Prior-art boundary

The random-matrix/log-gas ingredients are classical or explicitly available in current literature. Forrester--Jancovici--McAnally derive the small-wave-number structure-function expansion and the `beta <-> 4/beta` duality for the one-dimensional log gas. Forrester--Shen give the explicit circular `beta=4` spectral form factor in the bulk normalization used here and identify the `beta=4` state as Pfaffian.

A targeted search across circular/sine `beta` structure factors, hyperuniformity, Pfaffian processes, scale mixtures and Montgomery--Taylor pair-correlation bounds did not locate the specific convex-scale obstruction (23)--(31) or its application to the contracted Montgomery--Taylor diffraction target. No publication-level novelty claim is made. The new content here is the exact matching of the known symplectic structure factor to `ANF-020`'s budget, the local threshold (12), and the global tangent certificate at `h_0=1/5`.

## 7. Evidence boundary and next filter

This finding does **not** prove that the order interval in `ANF-020` is disjoint from `K`, and therefore it does not close the universal-affine scalar branch. It excludes one large and natural non-determinantal construction class: arbitrary convex mixtures of spatially rescaled unit-density `beta=4` CSE bulk diffraction profiles.

The argument also does not assert that every stationary CSE diffraction measure, or its arbitrary scale mixture, is automatically an element of the finite-configuration convex body `K`. That realizability passage is unnecessary for the negative result: even granting these point-process profiles as admissible candidate witnesses, they violate the required envelope.

General `beta` log gases, non-scale mixtures of different correlation mechanisms, nonstationary limits, direct finite-cluster convexifications and separating-spectrum arguments remain open. In particular, a lower long-wavelength slope is not enough. A useful future candidate must be tested against the **whole support-one band**, and `h=1/5` is now a cheap exact falsification point for the entire symplectic scale-mixture family.

The configuration-level branch of `ANF-006` remains outside this scalar diffraction duality and is unaffected.