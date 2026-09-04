# ANF-020 — the Montgomery--Taylor scalar ceiling dualizes to diffraction realizability

**Status:** `EXACT-DERIVED + CONVEX-DUALITY-REDUCTION + NEGATIVE/OBSTRUCTION + PRIOR-ART-REDIRECT`. The free-density stability problem of `ANF-018`--`ANF-019` has an exact dual formulation that removes the remaining profile-by-profile quantifier. Let

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2}
=1.327499296320588\ldots,
\qquad
a_{\rm MT}:=C_{\rm MT}^{-1}
=0.753296067856070\ldots .
\]

For every finite set of distinct real points `X`, define its normalized band diffraction measure on `(-1,1)` by

\[
\mu_X(d\alpha)
:=\frac1{|X|}
\left|\sum_{x\in X}e^{-2\pi i\alpha x}\right|^2d\alpha.
\]

Let `K` be the weak-* closed convex hull of these even positive measures in the dual of the even space `C_0((-1,1))`, and define the Montgomery--Taylor budget measure

\[
\nu_{\rm MT}
:=a_{\rm MT}\,\delta_0
+a_{\rm MT}|\alpha|\,d\alpha.
\]

Then the remaining universal scalar ceiling

\[
q_{\rm real}(J)\le\frac{C(J)}{C_{\rm MT}}
\qquad
\text{for every continuous even }J\ge0
\text{ supported in }[-1,1]
\]

is **equivalent** to the single measure-realizability statement

\[
\boxed{
K\cap\{\mu:0\le\mu\le\nu_{\rm MT}\}\ne\varnothing .
}
\]

Thus one does not need a different low-energy configuration for each spectrum `J` at the conceptual level: the whole theorem is equivalent to the existence of one `J`-independent averaged/asymptotic diffraction witness dominated by the Montgomery--Taylor budget. Conversely, failure of this realizability statement automatically produces one nonnegative compact-band spectrum that separates **all** finite real configurations from the desired ceiling.

The target is strongly hyperuniform in the point-process interpretation. Its diffuse mass in `(-epsilon,epsilon)` is at most `a_MT epsilon^2`, and the unit-density sine/free-fermion process supplies the exact uncontracted comparison `delta_0+|alpha|dalpha` on `|alpha|<=1`. However, this natural determinantal route is sharply blocked: **no stationary translation-invariant determinantal point process can realize even the band domination**

\[
\rho\delta_0+S(\alpha)d\alpha
\le a\delta_0+a|\alpha|d\alpha
\qquad(|\alpha|<1)
\]

for any `a<1`. The sine process saturates the endpoint `a=1`. Hence the desired contraction `a=a_MT<1` cannot come from the entire stationary translation-invariant DPP/free-fermion class.

## 1. Finite configurations are positive diffraction measures

Retain the notation of `ANF-018`. For continuous even `J>=0` supported in `[-1,1]`, let

\[
F(t)=\widehat J(t)
=\int_{-1}^{1}J(\alpha)e^{-2\pi i\alpha t}\,d\alpha.
\]

For a finite set `X`, Fourier expansion gives

\[
\begin{aligned}
e_J(X)
&=\frac1{|X|}\sum_{x,y\in X}F(x-y)\\
&=\int_{-1}^{1}J(\alpha)
\frac1{|X|}\left|\sum_{x\in X}e^{-2\pi i\alpha x}\right|^2d\alpha\\
&=\int J\,d\mu_X.
\end{aligned}
\tag{1}
\]

Therefore

\[
\boxed{
q_{\rm real}(J)=\inf_X\int J\,d\mu_X.
}
\tag{2}
\]

Passing from the set of `mu_X` to its convex hull does not change the infimum of a linear functional, and passing to the weak-* closure does not change it for `J in C_0((-1,1))`. Hence

\[
q_{\rm real}(J)=\inf_{\mu\in K}\int J\,d\mu.
\tag{3}
\]

On the analytic side,

\[
C(J)=J(0)+\int_{-1}^{1}|\alpha|J(\alpha)\,d\alpha,
\]

so

\[
\boxed{
\frac{C(J)}{C_{\rm MT}}
=\int J\,d\nu_{\rm MT}.
}
\tag{4}
\]

Equations (3)--(4) put the two sides of the scalar frontier in the same ordered cone of positive Radon measures.

## 2. An infinite-dimensional Farkas alternative removes the `for every J` quantifier

Let

\[
D_{\rm MT}
:=\{\eta:\ 0\le\eta\le\nu_{\rm MT}\}.
\tag{5}
\]

Within the even finite Radon measures on `(-1,1)`, `D_MT` is convex and weak-* compact. The following two statements are equivalent:

\[
\text{(A)}\qquad
\inf_{\mu\in K}\int J\,d\mu
\le\int J\,d\nu_{\rm MT}
\quad\text{for every even }J\in C_0,\ J\ge0;
\tag{6}
\]

\[
\text{(B)}\qquad
K\cap D_{\rm MT}\ne\varnothing.
\tag{7}
\]

The implication `(B) => (A)` is immediate. If `mu_* in K` and `mu_*<=nu_MT`, then for every nonnegative `J`,

\[
\inf_{\mu\in K}\int J\,d\mu
\le\int J\,d\mu_*
\le\int J\,d\nu_{\rm MT}.
\tag{8}
\]

For the converse, suppose `K` and `D_MT` are disjoint. A closed convex set and a disjoint compact convex set in this locally convex weak-* space can be strictly separated, so there is an even real `f in C_0((-1,1))` such that

\[
\inf_{\mu\in K}\int f\,d\mu
>
\sup_{\eta\in D_{\rm MT}}\int f\,d\eta.
\tag{9}
\]

All measures in `K` are positive. Replacing `f` by its positive part `f_+=max(f,0)` can therefore only increase the left side. On the right side, domination by `nu_MT` gives the exact support function

\[
\sup_{0\le\eta\le\nu_{\rm MT}}\int f\,d\eta
=\int f_+\,d\nu_{\rm MT}.
\tag{10}
\]

Hence

\[
\inf_{\mu\in K}\int f_+\,d\mu
>
\int f_+\,d\nu_{\rm MT},
\tag{11}
\]

which contradicts (A) because `f_+` is again continuous, even, nonnegative and vanishes at the endpoints. This proves the equivalence.

Combining with (2)--(4) gives the exact reformulation

\[
\boxed{
\forall J\ge0:\quad
q_{\rm real}(J)\le\frac{C(J)}{C_{\rm MT}}
\quad\Longleftrightarrow\quad
K\cap D_{\rm MT}\ne\varnothing.
}
\tag{12}
\]

This is the same sharp scalar question as `ANF-018`, not a relaxation. Convexification corresponds only to averaging finite diffraction measures after the energy has become linear.

## 3. What a universal witness must look like near zero

If `mu_* in K` satisfies `mu_*<=nu_MT`, then its mass near the origin obeys

\[
\mu_*\bigl((-\varepsilon,\varepsilon)\setminus\{0\}\bigr)
\le
a_{\rm MT}\int_{-\varepsilon}^{\varepsilon}|\alpha|\,d\alpha
=a_{\rm MT}\varepsilon^2.
\tag{13}
\]

Its atom at zero is at most `a_MT`. Thus any stationary point-process realization of such a witness would have intensity at most `a_MT` and a diffuse structure factor bounded by

\[
S(\alpha)\le a_{\rm MT}|\alpha|
\qquad(|\alpha|<1).
\tag{14}
\]

In the standard hyperuniform language, (14) is class-II-or-stronger suppression at long wavelengths. More importantly for the present problem, the coefficient is load-bearing: it is not enough that `S(0)=0`; the linear cusp must lie below a slope strictly smaller than one.

There is a canonical endpoint comparison. The unit-density sine process has translation-invariant kernel

\[
K_{\rm sine}(x-y)
=\frac{\sin\pi(x-y)}{\pi(x-y)}.
\]

Its pair correlation is

\[
g_2(r)=1-|K_{\rm sine}(r)|^2,
\]

and Fourier transforming the squared sinc gives

\[
S_{\rm sine}(\alpha)=|\alpha|
\qquad(|\alpha|\le1).
\tag{15}
\]

Thus its per-particle diffraction on the relevant band is exactly

\[
\delta_0+|\alpha|d\alpha.
\tag{16}
\]

The Montgomery--Taylor witness asks, in this language, for a uniform contraction of both the forward atom and the diffuse sine-process cusp by the factor

\[
a_{\rm MT}=0.7532960678\ldots<1.
\tag{17}
\]

## 4. Stationary translation-invariant determinantal witnesses have a sharp `a>=1` obstruction

Consider any stationary translation-invariant determinantal point process on `R` with kernel

\[
K(x-y)=\int_{\mathbb R}e^{2\pi i\xi(x-y)}\varphi(\xi)\,d\xi,
\]

where the standard DPP existence condition is

\[
0\le\varphi\le1,
\qquad
\rho:=K(0)=\int\varphi(\xi)d\xi<\infty.
\tag{18}
\]

Its diffuse structure factor is

\[
\boxed{
S(h)=1-\frac1\rho(\varphi*\widetilde\varphi)(h),
\qquad
\widetilde\varphi(\xi)=\varphi(-\xi).
}
\tag{19}
\]

The per-particle diffraction is `rho delta_0+S(h)dh`. Suppose, for some `0<a<1`, it were dominated on `(-1,1)` by

\[
\nu_a:=a\delta_0+a|h|dh.
\tag{20}
\]

Atom domination first gives

\[
\rho\le a.
\tag{21}
\]

The convolution in (19) is continuous because `varphi in L^1 cap L^2`, so the a.e. diffuse domination extends continuously to the origin. Since `S(h)<=a|h|`,

\[
S(0)=0.
\tag{22}
\]

But

\[
S(0)=1-\frac1\rho\int\varphi(\xi)^2d\xi.
\tag{23}
\]

As `0<=varphi<=1`, equality in `int varphi^2 <= int varphi=rho` forces

\[
\varphi=\mathbf 1_E
\quad\text{a.e.}
\tag{24}
\]

for some measurable set `E` of finite measure `|E|=rho`. Therefore any such hyperuniform determinantal candidate must already be a projection/free-fermion process.

For a projection process, (19) becomes

\[
S(h)
=1-\frac{|E\cap(E+h)|}{\rho}
=\frac{|E\triangle(E+h)|}{2\rho}.
\tag{25}
\]

The assumed linear domination now says, for all sufficiently small `h`,

\[
\|\mathbf1_E(\cdot+h)-\mathbf1_E\|_{L^1}
\le2\rho a|h|.
\tag{26}
\]

The standard translation characterization of bounded variation, which also follows directly by testing difference quotients against compactly supported `C^1` functions, gives

\[
P(E)=|D\mathbf1_E|(\mathbb R)\le2\rho a.
\tag{27}
\]

Any nonempty finite-measure finite-perimeter set in one dimension has perimeter at least `2`: up to null sets it is a union of intervals and must have at least one entering and one leaving boundary. Hence

\[
2\le P(E)\le2\rho a,
\qquad\text{so}\qquad
1\le\rho a.
\tag{28}
\]

Combining with `rho<=a` yields

\[
1\le\rho a\le a^2<1,
\tag{29}
\]

a contradiction. Therefore

\[
\boxed{
\text{no stationary translation-invariant DPP can satisfy (20) for any }a<1.
}
\tag{30}
\]

At `a=1`, equality is attainable: take `E` to be one interval of length one. Then `rho=1` and (25) gives `S(h)=|h|` for `|h|<=1`, exactly the sine process. The determinantal obstruction is therefore sharp at the same endpoint that calibrates the Montgomery--Taylor target.

## 5. Relation to ANF-018 and ANF-019

The diffraction reformulation and the stability formulation are two dual views of the same finite-configuration quantity. `ANF-018` writes

\[
q_{\rm real}(J)=F(0)-2B_{\rm stab}(F),
\]

while (3) writes it as the lower support function of the convex diffraction set `K`. The desired sharp lower bound on the best stability constant is therefore equivalent to asking whether `K` reaches the order interval below `nu_MT`.

`ANF-019` explains why weak-* convexification is not artificial. A finite low-energy cluster can be copied far apart without losing its specific energy, and arbitrary convex mixtures can be approximated at the level of linear spectral tests by combining widely separated cluster phases. The present finding packages that free-density phase flexibility into the closed convex diffraction body. It does not require a single periodic or fixed-density ground state.

The new formulation changes the cheapest possible proof strategy. To prove the scalar ceiling it is enough to construct one dominated element of `K`; to refute it, one can instead produce a separating nonnegative spectrum. This is an exact infinite-dimensional primal/dual alternative, rather than another search over special finite clusters.

## 6. Prior-art boundary

The ingredients of the new language are classical. Hahn--Banach separation and support functions of positive-measure order intervals are standard convex analysis. Hyperuniformity and the structure-factor criterion `S(k)->0` are classical in the point-pattern literature; Torquato--Stillinger is a primary anchor. Zhang--Torquato studies the distinct but closely related realizability problem of constructing point configurations with prescribed target structure factors and emphasizes that the usual elementary positivity conditions are not sufficient for realizability.

Translation-invariant determinantal point processes and their spectral multipliers are classical; Soshnikov gives the standard framework and existence criterion. Torquato--Scardicchio--Zachary explicitly connect the one-dimensional free-fermion/sine process, random matrices, number theory and hyperuniform structure factor with a linear cusp at the origin.

What is derived here is the specialization of those frameworks to the exact Montgomery--Taylor scalar budget: the equivalence (12), the interpretation of its target as the contracted sine-band measure (16)--(17), and the sharp contradiction (21)--(30) excluding every stationary translation-invariant DPP when the contraction factor is below one. A targeted search did not locate this particular Montgomery--Taylor domination problem or the factor-one DPP obstruction. No publication-level novelty claim is made.

## 7. Audit and evidence boundary

Equation (12) is exact for the scalar finite-real problem under the existing hypotheses `J continuous, even, nonnegative, supp(J) subset [-1,1]`. Working in `C_0((-1,1))` merely encodes the endpoint condition `J(+-1)=0` forced by continuity and compact support. The strict-separation step uses the weak-* closed convex hull by definition, so no unproved compactness of the raw finite-configuration family is being assumed.

The measure `mu_* in K` furnished by (12), if it exists, is **not automatically the diffraction of one stationary point process**. `K` is a weak-* closed convex hull of finite diffraction measures. Hyperuniform point-process realizability is therefore a construction strategy and structural interpretation, not an additional equivalence established here. In particular, the DPP obstruction does not disprove (12): it only kills a large, natural candidate class for realizing the witness.

Likewise, (30) concerns stationary translation-invariant DPPs. It does not rule out non-determinantal stationary processes, nonstationary asymptotic constructions, correlated mixtures whose limiting diffraction lies in `K`, or a direct convex-analytic construction with no point-process representation. The argument also needs domination of the diffuse part in a neighborhood of zero, but no information outside the support-one band.

The perimeter step is one-dimensional and is exactly where the sharp factor one enters. In higher dimension the analogous isoperimetric scaling has a different form and is not asserted here.

## 8. Consequence for the scalar frontier

The live universal-affine scalar question can now be attacked without choosing a candidate spectrum first:

\[
\boxed{
\text{construct }\mu_*\in K\text{ with }
\mu_*\le a_{\rm MT}(\delta_0+|\alpha|d\alpha),
\quad\text{or separate this order interval from }K.
}
\tag{31}
\]

This reframes the many-particle stability inequality as a **band-limited diffraction realizability problem with an exact target envelope**. The unit sine/free-fermion process identifies the nearest canonical boundary object, but the determinantal calculation proves that simply diluting, reshaping or otherwise changing the spectral projection inside the stationary DPP class cannot supply the required `0.753296...` contraction.

A productive next route therefore needs genuinely non-determinantal correlations, a direct construction in the convex closure of finite cluster diffractions, or a separating-spectrum argument showing that even this enlarged diffraction body misses the target order interval. The configuration-level branch of `ANF-006` remains outside this scalar duality and is unaffected.
