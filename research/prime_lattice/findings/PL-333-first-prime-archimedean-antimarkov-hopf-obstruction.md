# PL-333 — The archimedean remainder destroys the Dirichlet/Hopf sign at the first-prime threshold

**Evidence:** `LITERATURE+EXACT-DERIVED + DECISIVE-ROUTE-BOUNDARY + SOURCE-SELECTED-NONVANISHING-OPEN`

**Status:** `FULL-THRESHOLD-FORM-NOT-MARKOV + LOG-LAPLACIAN-HOPF-SIGN-REVERSED + C0-NONVANISHING-REQUIRES-FULL-OPERATOR-COMPARISON`

## Precise claim

`PL-329` and `PL-332` reduce the first rational-prime activation problem to two source-selected questions, one of which is the fixed-threshold nonvanishing of the canonical half-log boundary coefficient `C_0` at

\[
a_0=\frac12\log2.
\]

The sharp logarithmic-Laplacian Hopf theorem in source `97` is an obvious candidate for this fixed-aperture gate: a nontrivial nonnegative weak supersolution of the Dirichlet logarithmic Laplacian has a strictly positive `ell(dist)^{1/2}` boundary lower law. However, Suzuki's exact fixed-domain decomposition shows that this theorem cannot be applied directly to the completed-Weil threshold state. The obstruction is not merely that positivity of that state has not been proved at `a_0`. The bounded archimedean remainder has the **opposite Beurling--Deny sign** on the full threshold interval.

Let

\[
b=\log2,
\qquad a_0=b/2.
\]

At `a=a_0`, the `p=2` translation has scaled lag `b/a_0=2`, so its overlap in `(-1,1)` has measure zero. Thus Suzuki's formula (4.5) reduces exactly to

\[
\boxed{
q_{a_0}(w)
=c_0\|w\|_2^2+\mathcal L(w)+\langle K_0w,w\rangle,
}
\tag{PL333-1}
\]

where `c_0` is a scalar,

\[
\mathcal L(w)
=\frac14\int_{-1}^1\!\int_{-1}^1
\frac{|w(x)-w(y)|^2}{|x-y|}\,dx\,dy
-\frac12\int_{-1}^1 |w(x)|^2\log(1-x^2)\,dx,
\tag{PL333-2}
\]

and

\[
(K_0w)(x)
=-a_0\int_{-1}^1 r''(a_0(x-y))w(y)\,dy.
\tag{PL333-3}
\]

Suzuki's explicit archimedean remainder gives, for `t>0`,

\[
r''(t)
=-2\cosh(t/2)
+\frac{e^{-t/2}}{1-e^{-2t}}
-\frac1{2t}
=-2\cosh(t/2)
+\frac{e^{t/2}}{2\sinh t}
-\frac1{2t}.
\tag{PL333-4}
\]

On the entire threshold difference range `0<t<=b`, this is strictly negative. Indeed `b<1`, and

\[
e^{t/2}<1+t,
\qquad \sinh t>t,
\]

so

\[
\frac{e^{t/2}}{2\sinh t}-\frac1{2t}<\frac12.
\]

Consequently

\[
\boxed{r''(t)<-\frac32<0\qquad(0<t\le\log2),}
\tag{PL333-5}
\]

with the continuous limit `r''(0)=-7/4`. Hence the integral kernel

\[
k_0(x,y):=-a_0r''(a_0(x-y))
\tag{PL333-6}
\]

is strictly positive on the whole closed square `[-1,1]^2`.

This positive off-diagonal correction destroys the Markov property of the full threshold form. At the longest chord `|x-y|=2`, so that `t=a_0|x-y|=b`, (PL333-4) gives exactly

\[
r''(b)
=-\frac{5\sqrt2}{6}-\frac1{2b},
\]

and therefore

\[
\boxed{
-1-2b\,r''(b)
=\frac{5\sqrt2}{3}\,b>0.
}
\tag{PL333-7}
\]

By continuity the same strict inequality holds for all pairs `(x,y)` in sufficiently small opposite endpoint neighborhoods. Choose nonzero real `f,g>=0` with disjoint supports in those two neighborhoods and put `w=f-g`, so `|w|=f+g`. A direct cross-term calculation from (PL333-1)--(PL333-3) yields

\[
\boxed{
q_{a_0}(|w|)-q_{a_0}(w)
=2\int\!\!\int
\frac{f(x)g(y)}{|x-y|}
\Bigl[-1-2t\,r''(t)\Bigr]\,dx\,dy>0,
\qquad t=a_0|x-y|.
}
\tag{PL333-8}
\]

(The double integral is over the two chosen opposite endpoint supports.) The scalar term and the killing term in `mathcal L` cancel in this comparison. Therefore

\[
\boxed{q_{a_0}(|w|)>q_{a_0}(w)}
\tag{PL333-9}
\]

for an explicit class of test functions. The first Beurling--Deny contraction inequality fails, so the full completed-Weil threshold form is **not** a Dirichlet form and its semigroup is not positivity preserving. Suzuki's positivity-improving argument in Section 5.2 applies to the limiting principal form `\overline{\mathcal L}` used in the `a->0` analysis, not to `q_{a_0}`.

There is a second, sharper obstruction to importing source `97`. Suppose, even more favorably, that a threshold eigenstate `u` were known independently to be nonnegative, nontrivial, continuous up to the boundary, and zero outside `(-1,1)`. Source `96` and `PL-289` identify the operator associated with `mathcal L` as

\[
T_{\mathcal L}=\frac12L_\Delta+\gamma I.
\tag{PL333-10}
\]

Thus the eigen-equation for (PL333-1) gives

\[
\boxed{
L_\Delta u
=2(\lambda-c_0-\gamma)u-2K_0u.
}
\tag{PL333-11}
\]

Because `k_0(x,y)>0` everywhere and `u>=0` is nonzero,

\[
(K_0u)(x)>0
\]

throughout the interval and extends continuously with a strictly positive one-sided value at each endpoint. Since `u(x)->0` there, (PL333-11) implies

\[
\boxed{
\lim_{x\uparrow1}L_\Delta u(x)
=-2(K_0u)(1)<0,
}
\tag{PL333-12}
\]

and analogously at `-1`. In the source-trace formulation used in `PL-319`, the same statement is a one-sided boundary forcing law. Therefore a hypothetical nonnegative threshold ground state is, near the boundary, a **strict logarithmic-Laplacian subsolution**, not the supersolution required by the Hopf theorem of source `97`.

The direct route

\[
\text{positive threshold state}
\ +\
\text{standard }L_\Delta\text{ Hopf lemma}
\Longrightarrow
C_0\ne0
\]

is consequently blocked even if positivity of the state were granted for free.

## 1. Why the prime term really vanishes at the threshold

Suzuki's scaled Rayleigh quotient contains the prime-power contribution

\[
-\sum_{n\le e^{2a}}\frac{\Lambda(n)}{\sqrt n}
\left(
\int_{-1}^{1-\log n/a}w(x+\log n/a)\overline{w(x)}\,dx
+
\int_{-1+\log n/a}^{1}w(x-\log n/a)\overline{w(x)}\,dx
\right).
\tag{PL333-13}
\]

At `a_0=b/2`, the only possible rational prime power is `n=2`, and

\[
\frac{\log2}{a_0}=2.
\]

Both integration intervals in (PL333-13) collapse to a single endpoint. Hence their Lebesgue integrals are zero. This is the exact threshold counterpart of the first-prime activation analyzed in `PL-325`--`PL-332`: just above `a_0` a shrinking `p=2` edge channel appears, while exactly at `a_0` the rational-prime operator contributes nothing on `L^2(-1,1)`.

Therefore the failure in (PL333-9) is already present **before** the first rational-prime overlap has positive measure. It is caused by the archimedean remainder of the completed explicit formula.

## 2. Exact sign of the archimedean kernel

Suzuki decomposes

\[
r(t)=r_0(t)+r_1(t),
\qquad
r_0(t)=-4(e^{t/2}+e^{-t/2}-2),
\]

and obtains

\[
r_1''(t)
=\frac{e^{-|t|/2}}{1-e^{-2|t|}}-\frac1{2|t|}.
\]

For `0<t<=b`, rewrite the latter as

\[
r_1''(t)
=\frac{e^{t/2}}{2\sinh t}-\frac1{2t}.
\]

The elementary bound in (PL333-5) is deliberately stronger than needed. To verify it, define

\[
h(t)=1+t-e^{t/2}.
\]

For `0<t<=b`,

\[
h'(t)=1-\frac12e^{t/2}
\ge1-\frac1{\sqrt2}>0,
\]

so `h(t)>0`. Together with `sinh t>t`, this gives

\[
\frac{e^{t/2}}{\sinh t}
<\frac{1+t}{t}
=\frac1t+1,
\]

hence `r_1''(t)<1/2`. Since `r_0''(t)=-2cosh(t/2)<=-2`, (PL333-5) follows.

At `t=b`, use `e^{b/2}=sqrt2` and `e^{-2b}=1/4`:

\[
r_1''(b)=\frac{4}{3\sqrt2}-\frac1{2b}
=\frac{2\sqrt2}{3}-\frac1{2b},
\]

while

\[
r_0''(b)=-2\cosh(b/2)=-\frac3{\sqrt2}.
\]

Their sum is the exact value used in (PL333-7).

## 3. The Beurling--Deny failure is quantitative

For disjoint nonnegative `f,g`, only cross terms change when `w=f-g` is replaced by `|w|=f+g`. The jump part of `mathcal L` contributes

\[
-2\int\!\!\int \frac{f(x)g(y)}{|x-y|}\,dx\,dy,
\tag{PL333-14}
\]

whereas the archimedean integral operator contributes

\[
-4a_0\int\!\!\int r''(a_0(x-y))f(x)g(y)\,dx\,dy.
\tag{PL333-15}
\]

Combining them gives (PL333-8). Because the bracket in (PL333-8) has the strictly positive endpoint value (PL333-7), one may choose the supports sufficiently close to `-1` and `+1` so that the whole integrand is positive.

This matters because it rules out a tempting inference from Suzuki's small-`a` argument. The principal form `mathcal L` is an irreducible Dirichlet form and its semigroup is positivity improving. But the exact finite-`a` form is `mathcal L` plus bounded arithmetic/archimedean perturbations. At the first-prime threshold, the arithmetic translation has not yet appeared and nevertheless the archimedean perturbation already reverses the normal-contraction inequality on long chords. Positivity improving is therefore **not stable in the particular direction needed here**.

No assertion is made that the lowest eigenfunction of `q_{a_0}` must change sign. Failure of semigroup positivity preservation does not imply that. The precise conclusion is narrower: ground-state positivity and boundary nonvanishing cannot be imported from the Beurling--Deny structure of `mathcal L`.

## 4. Why the standard logarithmic Hopf theorem has the wrong forcing sign

Source `97` proves a sharp Hopf-type statement for nontrivial nonnegative weak supersolutions of the zero-exterior logarithmic Laplacian. In the notation of that paper, the load-bearing hypothesis is

\[
\mathcal E_L(v,\phi)\ge0
\qquad
\text{for every nonnegative compactly supported }\phi,
\tag{PL333-16}
\]

which is the weak `L_\Delta v>=0` condition. Under the interior-sphere hypothesis it forces a strictly positive `ell(dist)^{1/2}` boundary lower law.

For the completed-Weil threshold state, the full eigen-equation contains `K_0` with a strictly positive kernel. If `u` is nonnegative, that term enters (PL333-11) with a minus sign when the principal logarithmic Laplacian is isolated. The scalar multiple of `u` vanishes at the endpoint, whereas `K_0u` retains a positive boundary value. Hence the forcing is strictly negative near the endpoint and (PL333-16) fails there.

This is stronger than saying that the hypotheses of source `97` have not yet been checked. Their decisive sign is **provably reversed** by the actual archimedean completion term at `a_0`.

A Hopf theorem for an operator of the form

\[
L_\Delta+2K_0+V
\]

could in principle behave differently, but it would be a theorem for the **full completed-Weil threshold operator**, not an application of the existing logarithmic-Laplacian supersolution lemma. Any such theorem would have to accommodate a strictly positive nonlocal kernel on the left-hand side and prove a boundary lower law despite the negative `L_\Delta` source trace exposed above.

## 5. Prior-art and novelty audit

The ingredients are established prior art. Source `56` gives Suzuki's exact decomposition of the localized Weil form, the formulas for `r_0` and `r_1''`, and the irreducible Dirichlet-form argument for the limiting principal form `mathcal L`. Source `96` identifies the Dirichlet logarithmic Laplacian and its Fourier normalization. Source `97` supplies the sharp `ell(dist)^{1/2}` Hopf lower law for nonnegative logarithmic-Laplacian supersolutions. Standard Beurling--Deny theory supplies the equivalence between normal contractions and positivity-preserving symmetric semigroups.

No novelty is claimed for those general facts, for the observation that bounded perturbations can destroy a Markov property, or for Hopf lemmas themselves. The durable line-specific delta is the **exact threshold sign computation**: Suzuki's explicit archimedean remainder makes the completed-Weil form anti-Markov on opposite endpoint packets already at `a_0`, and the same positive kernel forces a hypothetical positive threshold eigenstate to have negative logarithmic-Laplacian boundary source. A targeted audit around Suzuki's 2026 paper, logarithmic-Laplacian Hopf/maximum principles, and nonlocal perturbations did not locate this first-prime-threshold calculation. Search absence is not used as evidence of broad novelty.

The currently indexed arXiv text of source `56` exposes the formulas used above; the source registry tracks the revised August 2026 version. The claim depends only on the explicit local expansion and scaled form decomposition, not on the later conjectural large-aperture material.

## 6. Adversarial controls and limits

**This does not prove `C_0=0`.** The result blocks a particular positivity/Hopf route to `C_0!=0`. The actual source-selected threshold state may still have a nonzero half-log coefficient for another reason.

**This does not prove that the threshold ground state changes sign.** Equation (PL333-9) proves failure of the Markov/absolute-value contraction for the full form. A particular lowest eigenfunction could nevertheless happen to be one-signed by a more specific mechanism.

**The Hopf-sign statement is conditional only on one-signedness, not on RH.** If a nonnegative nontrivial threshold eigenstate exists, the positivity of `K_0` forces the negative boundary source in (PL333-12) unconditionally from the finite-aperture operator identity.

**The first rational-prime term is not being discarded asymptotically.** It is exactly zero at `a_0` because its overlap has measure zero. The result therefore isolates an archimedean obstruction rather than mixing it with the newly active `p=2` reflection studied in `PL-325`--`PL-332`.

**The sign estimate uses the entire required kernel range.** Formula (PL333-5) proves `r''<0` for every `|t|<=log2`, so positivity of `K_0` is not inferred from a single endpoint sample. The endpoint sample is used only to prove the stronger quantitative failure of the Markov contraction.

**No statement about later prime activations follows.** Once `a>a_0`, the negative prime-translation quadratic term enters and the sign structure changes again. The present result concerns the fixed threshold state singled out by `PL-332`.

## Consequence for the research line

`PL-332` made the fixed coefficient `C_0` the natural remaining noncollapse question after uniform source control. The standard sharp Hopf theorem for `L_\Delta` does not close it. At the exact first-prime threshold, the completed-Weil operator already contains a positive archimedean integral kernel which both destroys the Dirichlet-form contraction and gives the wrong sign when the principal logarithmic Laplacian is isolated.

The next viable fixed-threshold route must therefore use structure of the **full operator** rather than the principal logarithmic Laplacian alone. Concrete possibilities include a boundary comparison theorem tailored to `L_\Delta+2K_0+V`, a source-selected integral identity that forces the half-log coefficient directly, or an independent nonvanishing argument for the threshold state. Re-proving positivity improving for `mathcal L` or invoking the existing `L_\Delta` Hopf lemma cannot settle the gate.

## Sources

- Source `56` in `research/prime_lattice/SOURCES.md`: Masatoshi Suzuki, *Weil's quadratic form via the screw function*; formulas (2.2), (4.4), and (4.5), and the limiting Dirichlet-form/positivity-improving argument.
- Source `96`: Huyuan Chen and Tobias Weth, *The Dirichlet problem for the logarithmic Laplacian*; singular-integral/Fourier normalization of `L_\Delta`.
- Source `97`: Víctor Hernández-Santamaría, Luis Fernando López Ríos, Alberto Saldaña, *Optimal boundary regularity and a Hopf-type lemma for Dirichlet problems involving the logarithmic Laplacian*; sharp half-log boundary law and nonnegative-supersolution Hopf theorem.
- `PL-289`: identification of Suzuki's principal fixed-domain operator with `(1/2)L_\Delta+\gamma I`.
- `PL-319`: endpoint source-trace formulation for completed-Weil eigenstates.
- `PL-329`: sharp source-selected first-prime amplitude/coefficient gate.
- `PL-330`--`PL-332`: norm-resolvent branch transport, moving-layer obstruction, and continuity of the source-selected half-log coefficient under uniform residual control.
