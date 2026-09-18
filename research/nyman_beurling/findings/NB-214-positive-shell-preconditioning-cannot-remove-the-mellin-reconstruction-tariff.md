# NB-214 — Positive shell preconditioning cannot remove the Mellin reconstruction tariff

**Date:** 2026-09-18  
**Status:** `DERIVED + METHOD-BOUNDARY + REPRESENTATION-AUDIT + SOURCE-ACQUISITION + POSITIVE-EULER + NB-213-REFINEMENT`.

`NB-213` shows that replacing `-zeta'/zeta` by the primitive `log zeta` and then estimating absolutely does not improve the current Vinogradov--Korobov growth class: differentiating the Mellin carrier costs `X=log x`. One escape left explicitly open there was to change the source-faithful observable itself, perhaps with an `X`-dependent shell profile that inserts a compensating reciprocal carrier factor before reconstruction.

For **nonnegative observables supported on a fixed multiplicative shell**, that escape is not available. The obstruction is uniform over the profile and does not require the profile to be fixed as `X -> infinity`.

Write the shell in logarithmic coordinates

\[
n=x e^y,\qquad 0\le y\le \Delta,\qquad X:=\log x,
\tag{1}
\]

with fixed `Delta>0`. Let `h_X` be any nonzero nonnegative integrable source profile on `[0,Delta]`, possibly depending arbitrarily on `X`, and put

\[
m_X:=\int_0^\Delta h_X(y)\,dy>0,
\qquad
A_X(v):=\int_0^\Delta h_X(y)e^{ivy}\,dy.
\tag{2}
\]

After one ordinary Mellin primitive transfer, the reconstruction kernel is, up to an irrelevant unit complex factor and the same bounded shell weights already present in `NB-212`--`NB-213`,

\[
K_X(v)
:=
\left(\frac d{dv}+iX\right)A_X(v)
=
i\int_0^\Delta (X+y)h_X(y)e^{ivy}\,dy.
\tag{3}
\]

There is a constant `c_Delta>0`, independent of `X` and of the choice of `h_X`, such that for every sufficiently large `X`,

\[
\boxed{
\int_I |K_X(v)|\,dv
\ge
c_\Delta X m_X
}
\tag{4}
\]

on every contour segment `I` containing one fixed neighbourhood of `v=0`. Consequently the normalized reconstruction functional

\[
L\longmapsto
\frac1{m_X}\int_I K_X(v)L(v)\,dv
\tag{5}
\]

has `L^infinity(I) -> C` operator norm at least `c_Delta X`. Thus **no nonnegative `X`-dependent shell profile can precondition the primitive reconstruction down to a sublinear-in-`X` operator norm while remaining source-normalized**.

On the coupled Vinogradov--Korobov diagonal of `NB-212`,

\[
X=Q^{2/3+o(1)},
\tag{6}
\]

so an argument whose only post-transfer arithmetic input is a uniform envelope for `log zeta` still carries a positive-power tariff `Q^{2/3+o(1)}` at the operator-norm level. In particular, positive source-window engineering by itself cannot move the `NB-212` contour method from the polynomial-prefactor class into the polylogarithmic or bounded-prefactor classes.

The conclusion is a **method boundary**, not a lower bound for the true contour remainder. It leaves open precisely the mechanisms that use the actual analytic/oscillatory structure of `log zeta` before absolute values, or that leave the positive-observable class.

## 1. A profile-uniform lower bound for the reconstruction kernel

Define

\[
\widetilde K_X(v)
:=
\frac{K_X(v)}{i}
=
\int_0^\Delta (X+y)h_X(y)e^{ivy}\,dy.
\tag{7}
\]

Choose once and for all

\[
\nu_\Delta:=\frac{\pi}{3\Delta}.
\tag{8}
\]

For `|v|<=nu_Delta` and `0<=y<=Delta`,

\[
|vy|\le \frac\pi3,
\qquad
\cos(vy)\ge\frac12.
\tag{9}
\]

Since the measure `(X+y)h_X(y)dy` is nonnegative,

\[
\begin{aligned}
|K_X(v)|
&=|\widetilde K_X(v)|\\
&\ge \Re\widetilde K_X(v)\\
&=\int_0^\Delta (X+y)h_X(y)\cos(vy)\,dy\\
&\ge \frac12 X m_X.
\end{aligned}
\tag{10}
\]

Therefore every interval `I` containing `[-nu_Delta,nu_Delta]` satisfies

\[
\boxed{
\|K_X\|_{L^1(I)}
\ge
\nu_\Delta X m_X.
}
\tag{11}
\]

This proves (4) with `c_Delta=nu_Delta`. Nothing in the argument requires a fixed shape, differentiability, a lower bound on the support width, or a lower bound on `m_X`. Bounded support and positivity are enough.

The same proof works for any uniformly bounded logarithmic shell `|y|<=Delta_0`. The factor `X+y` can then be replaced by any positive reconstruction multiplier `lambda_X(y)=X+O_Delta(1)`; for large `X` it remains comparable with `X`, and the Fourier transform of the resulting positive measure stays large on a fixed neighbourhood of the origin.

## 2. Source normalization makes trivial amplitude rescaling useless

A superficial way to make (3) smaller is to scale the profile by `1/X`. That does reduce `K_X` by `1/X`, but it also reduces the mass of the source observable by the same factor. Equation (11) is homogeneous:

\[
h_X\mapsto c_X h_X
\quad\Longrightarrow\quad
m_X\mapsto c_Xm_X,
\qquad
K_X\mapsto c_XK_X.
\tag{12}
\]

After dividing by `m_X`, as any positive-return witness must do if it is to retain a nondegenerate barycentric signal, the factor cancels and the lower bound remains

\[
\boxed{
\frac{\|K_X\|_{L^1(I)}}{m_X}
\ge c_\Delta X.
}
\tag{13}
\]

Thus neither shrinking the profile amplitude nor concentrating its mass into a thinner sub-shell creates a reciprocal `X` gain. Concentration actually makes the local Fourier transform more coherent; positivity prevents the cancellation that would be needed to suppress the central lobe.

For profile families with the usual uniform smoothness/Wiener control, the converse scale is also immediate. If

\[
\|A_X\|_1+\|A_X'\|_1\le C m_X
\tag{14}
\]

uniformly, then

\[
\|K_X\|_1
\le
\|A_X'\|_1+X\|A_X\|_1
\ll X m_X.
\tag{15}
\]

Hence the normalized reconstruction tariff is actually `Theta(X)` for the standard smooth positive shell profiles. The lower bound (13), however, is the part needed here and requires no Wiener upper hypothesis.

## 3. Why this is exactly the `log zeta -> zeta'/zeta` source-reconstruction cost

For `Re(s)>1`,

\[
\log\zeta(s)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\log n}\frac1{n^s},
\qquad
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{n^s}.
\tag{16}
\]

On the shell (1),

\[
\log n=X+y,
\qquad 0\le y\le\Delta.
\tag{17}
\]

Therefore converting the primitive coefficient `Lambda(n)/log n` back into the desired source coefficient `Lambda(n)` multiplies each physical shell component by exactly `X+y`. Equation (3) is simply the Mellin/Fourier representation of this coefficient reconstruction.

This also clarifies why an artificial factor `e^{-iXv}` is not a free fix. Multiplying a Mellin amplitude by a carrier that cancels `e^{iXv}` translates its inverse Fourier profile by distance `X` in logarithmic coordinate. For `X -> infinity`, that translated profile no longer lives in the fixed shell `y=O(1)` corresponding to `n asymp x`. An exact carrier cancellation therefore changes the physical observable rather than preconditioning the same source shell.

The positivity estimate (10) is the quantitative version of that support statement. A nonnegative profile whose physical support remains within bounded logarithmic distance of the shell centre necessarily has a reconstruction multiplier of size `X` and a central Fourier lobe of the same normalized size.

## 4. Exact operator-norm meaning of the tariff

Let `I` be the safe truncated contour segment used after the Vinogradov--Korobov shift, and suppose it contains `[-nu_Delta,nu_Delta]`; any standard truncation used for the fixed smooth shell inversion does so once the truncation height is large enough. Define

\[
T_X[L]
:=
\int_I K_X(v)L(v)\,dv.
\tag{18}
\]

As a functional on `L^infinity(I)`,

\[
\|T_X\|_{(L^\infty)^*}
=
\|K_X\|_{L^1(I)}.
\tag{19}
\]

The equality follows by taking the measurable phase of `K_X`; no arithmetic input is involved. Hence (13) says that the **best possible bound obtainable from a bare uniform envelope**

\[
|L(v)|\le B(Q)
\tag{20}
\]

has normalized worst-case cost at least

\[
c_\Delta X B(Q).
\tag{21}
\]

When `L(v)=log zeta(sigma+i(t+v))`, this does **not** assert that the actual zeta integral attains the operator norm. The analytic function `log zeta` occupies a tiny structured subset of the `L^infinity` unit ball. Equation (21) says only that a proof which discards that structure and retains solely the envelope (20) cannot certify a better reconstruction norm.

This distinction is essential. The live improvement route is not a smaller pointwise bound followed by the same absolute-value closure; it must exploit correlation between `log zeta`, the carrier, and the shell amplitude before passing to an absolute norm.

## 5. Coupled Vinogradov--Korobov consequence

`NB-212`--`NB-213` use

\[
Q:=\log(10+|t|),
\qquad
R(Q)=Q^{2/3}(\log Q)^{1/3},
\tag{22}
\]

with the zero-free displacement providing

\[
\exp\!\left[-c\frac{X}{R(Q)}\right].
\tag{23}
\]

Along the moving diagonal

\[
Q
=\kappa\frac{X^{3/2}}{(\log X)^\gamma},
\tag{24}
\]

one has

\[
X=Q^{2/3+o(1)}.
\tag{25}
\]

Even if the primitive itself enjoyed the optimistic uniform envelope

\[
|\log\zeta|=Q^{o(1)},
\tag{26}
\]

any positive shell reconstruction closed through its `L^infinity` norm has normalized operator tariff at least

\[
\boxed{
Q^{2/3+o(1)}.
}
\tag{27}
\]

That remains in the positive-power prefactor class isolated by `NB-212`. Therefore allowing the nonnegative shell window to depend on `X` does not, by itself, move the method into the polylogarithmic or bounded-prefactor regimes. The log-squared corridor remains the natural ceiling of this **positive profile + primitive + uniform-envelope** architecture.

## 6. Adversarial checks and boundaries

**Positivity is load-bearing.** If `h_X` is signed or complex, the measure in (7) can have vanishing low moments and the central-lobe lower bound can fail. Such profiles belong to the separate signed/complex branch already left open by the line; this finding does not obstruct them.

**The result is not a lower bound for the true remainder.** A specific analytic `log zeta` can cancel strongly against `K_X`. The theorem rules out only profile engineering as a way to make the reconstruction operator itself sublinear in `X` before using any structure of `log zeta`.

**The profile may vary arbitrarily with `X`.** It may narrow, drift anywhere inside the fixed shell, or have mass tending to zero. Equation (13) is normalized and uniform, so none of these changes removes the tariff.

**A growing logarithmic shell is a different representation.** The proof uses a uniformly bounded `y`-range. Letting the shell width grow with `X` changes the observable and may alter the local Fourier scale. Such a construction would need its own source-fidelity and positive-return audit; it is not covered here.

**Suppressing the central contour segment is not free.** The lower bound is local near `v=0`. A contour partition that deletes this neighbourhood must reconstruct its contribution by another term. If that replacement uses additional cancellation or a different norm, it is a genuinely different mechanism rather than a counterexample to (13).

**Destination coupling remains absent.** As in `NB-212`--`NB-213`, this is a source-side statement about positive Euler acquisition. It does not prove that a near-optimal Nyman approximant must realize the corresponding positive return, and it says nothing about unrestricted signed/complex synthesis.

## 7. Representation and prior-art audit

**Representation audit.** The lower bound is generic fixed-shell Fourier geometry: differentiating a carrier associated with physical location `X` multiplies a positive bounded-width profile by `X+O(1)`, and the Fourier transform of a positive finite measure retains a central lobe proportional to its mass. The specifically arithmetic content is the source/primitive pair

\[
-\zeta'/\zeta
\quad\leftrightarrow\quad
\log\zeta,
\tag{28}
\]

whose coefficients differ by `log n`, together with the Vinogradov--Korobov displacement that turns `X` into the coupled `Q^(2/3+o(1))` tariff. Thus the theorem is not new harmonic analysis; its role is to close a concrete representation escape in the Nyman source program.

**Prior-art audit.** The generic facts used above are elementary Fourier duality and the standard local nonvanishing of the Fourier transform of a positive finite measure near frequency zero. A targeted search found the expected general literature on characteristic functions and positive-definite/bandlimited Fourier transforms, but no additional theorem is load-bearing: (10)--(13) are direct one-line consequences of positivity and bounded support. The arithmetic identities in (16) and the Vinogradov--Korobov input are already anchored in `SOURCES.md`. No new source entry is required.

## 8. Research consequence

`NB-213` left two qualitatively different possibilities for beating the current contour ceiling: engineer a source-faithful observable that cancels the carrier reconstruction cost before absolute values, or retain the carrier and primitive inside a genuinely joint cancellation estimate. `NB-214` removes the first possibility **within the positive fixed-shell class**.

The live source-side question is therefore narrower. To improve the `NB-212` corridor one must either

1. estimate the actual oscillatory integral involving `log zeta` and the reconstruction kernel before reducing `log zeta` to an `L^infinity` envelope, gaining roughly `X^{-1+o(1)}` relative to the worst-case operator norm; or
2. leave the nonnegative fixed-shell observable class, for example through a signed/complex profile whose moment cancellation is itself source-justified and whose destination meaning can be controlled.

Merely allowing the positive smooth window to depend on `X`, rescaling it, concentrating it, or inserting a formal reciprocal carrier factor without tracking physical support does not change the growth class. The separate destination theorem coupling this source obstruction back to actual Nyman approximation remains open.