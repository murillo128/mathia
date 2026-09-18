# NB-215 — Signed fixed-shell preconditioning can only export the Mellin tariff

**Date:** 2026-09-18  
**Status:** `EXACT-DERIVED + METHOD-BOUNDARY + SIGNED-COMPLEX + FOURIER-DUALITY + SOURCE-CONDITIONING + NB-214-EXTENSION`.

`NB-214` proves that positivity forces a central Fourier lobe of size `Theta(X)` after one Mellin primitive transfer, so no nonnegative profile on a fixed logarithmic shell can precondition away the reconstruction factor `X=log x`. The explicit boundary left open there is to use a signed or complex shell profile whose cancellations suppress that central lobe.

There is a sharper structural statement. **Signs cannot remove the global absolute reconstruction tariff at all.** For every nonzero-mean signed or complex fixed-shell profile, Fourier inversion gives a sign-blind lower bound of order `X` for the full `L^1` reconstruction kernel. A signed profile may suppress the kernel on the central contour segment, but then it can only do so by exporting reconstruction mass to other frequencies; if its total-variation conditioning stays moderate, even that local export is quantitatively limited.

Thus the positive hypothesis in `NB-214` is needed for its *fixed central-neighbourhood* lower bound, not for the global absolute Mellin tariff itself.

## 1. Setup

Fix `Delta>0`, let `X>0`, and let

\[
h\in L^1([0,\Delta];\mathbb C)
\]

have nonzero mean

\[
m:=\int_0^\Delta h(y)\,dy\ne0.
\tag{1}
\]

Write

\[
V:=\int_0^\Delta |h(y)|\,dy,
\qquad
\kappa:=\frac{V}{|m|}\ge1.
\tag{2}
\]

The Fourier amplitude and the one-primitive reconstruction kernel are

\[
A(v):=\int_0^\Delta h(y)e^{ivy}\,dy,
\tag{3}
\]

\[
K_X(v)
:=
\left(\frac d{dv}+iX\right)A(v)
=
i\int_0^\Delta (X+y)h(y)e^{ivy}\,dy.
\tag{4}
\]

This is exactly the fixed-shell carrier reconstruction from `NB-213`--`NB-214`, now without any positivity assumption on `h`.

For a measurable contour set `J`, define the source-normalized absolute reconstruction cost

\[
\mathcal C_X(J)
:=
\frac1{|m|}\int_J |K_X(v)|\,dv.
\tag{5}
\]

The corresponding bare source-acquisition functional on bounded shell defects is

\[
\mathcal S_h[d]
:=
\frac1m\int_0^\Delta h(y)d(y)\,dy,
\tag{6}
\]

whose exact `L^infty -> C` operator norm is

\[
\boxed{
\|\mathcal S_h\|=\kappa.
}
\tag{7}
\]

So `kappa` is not merely a heuristic cancellation count: it is the exact conditioning price paid when the signed source profile is controlled only by an absolute uniform envelope.

## 2. Global reconstruction is sign-blind and still costs `Theta(X)` from below

Put

\[
g_X(y):=(X+y)h(y),
\qquad
G_X(v):=\int_0^\Delta g_X(y)e^{ivy}\,dy,
\tag{8}
\]

so `|G_X|=|K_X|`. If `G_X` is not integrable on `R`, then `mathcal C_X(R)=+infinity` and the desired lower bound is automatic. Assume therefore that `G_X in L^1(R)`.

Fourier inversion gives, almost everywhere on the shell,

\[
g_X(y)
=
\frac1{2\pi}
\int_{\mathbb R}G_X(v)e^{-ivy}\,dv.
\tag{9}
\]

Since

\[
h(y)=\frac{g_X(y)}{X+y},
\tag{10}
\]

we may integrate (9) against `(X+y)^(-1)` on `[0,Delta]` and use Fubini:

\[
m
=
\frac1{2\pi}
\int_{\mathbb R}G_X(v)W_X(v)\,dv,
\tag{11}
\]

where

\[
W_X(v)
:=
\int_0^\Delta
\frac{e^{-ivy}}{X+y}\,dy.
\tag{12}
\]

The dual kernel satisfies the exact elementary bound

\[
\|W_X\|_\infty
\le
\int_0^\Delta\frac{dy}{X+y}
=
\log\!\left(1+\frac\Delta X\right).
\tag{13}
\]

Consequently

\[
2\pi|m|
\le
\|G_X\|_1
\log\!\left(1+\frac\Delta X\right),
\tag{14}
\]

and hence

\[
\boxed{
\mathcal C_X(\mathbb R)
\ge
\frac{2\pi}
{\log(1+\Delta/X)}
\ge
\frac{2\pi}{\Delta}X.
}
\tag{15}
\]

No sign, phase, smoothness, or total-variation hypothesis entered this estimate beyond the existence of the nonzero source mean `m`; rough profiles simply have infinite global `L^1` cost and satisfy (15) trivially.

This is the main sign-blind obstruction. A complex profile can cancel the central lobe identified by `NB-214`, but it cannot reduce the **full absolute reconstruction norm** below linear order in the carrier scale. It can only redistribute that norm in `v`.

## 3. The same global obstruction strengthens under repeated primitivization

The argument is not specific to one primitive. After `j>=1` ordinary primitive transfers, the differentiated carrier-amplitude is, up to a unit complex factor,

\[
K_{X,j}(v)
:=
\int_0^\Delta
(X+y)^j h(y)e^{ivy}\,dy
=
i^{-j}
\left(\frac d{dv}+iX\right)^j A(v).
\tag{16}
\]

If `K_{X,j}` is integrable, apply the same inversion argument with the reciprocal shell multiplier `(X+y)^(-j)`. Its Fourier transform has sup norm at most

\[
\int_0^\Delta (X+y)^{-j}\,dy
\le
\Delta X^{-j}.
\tag{17}
\]

Therefore

\[
\boxed{
\frac{\|K_{X,j}\|_{L^1(\mathbb R)}}{|m|}
\ge
\frac{2\pi}{\Delta}X^j.
}
\tag{18}
\]

So finite repeated primitivization cannot acquire a global absolute-norm advantage from signed preconditioning either. This is the signed/complex Fourier-dual counterpart of the carrier-differentiation observation in `NB-213`.

## 4. Exporting the tariff away from the central contour costs source conditioning

The global estimate still leaves a possible contour tactic: arrange signs so that most of the `L^1` mass in (15) lies outside the safe central segment where the Vinogradov--Korobov argument controls `log zeta`. That possibility has a quantitative conditioning price.

Assume

\[
X\ge4\Delta,
\tag{19}
\]

and let `I` contain the fixed interval

\[
I_\Delta
:=
\left[-\frac1{5\Delta},\frac1{5\Delta}\right].
\tag{20}
\]

At the origin,

\[
\begin{aligned}
|K_X(0)|
&=
\left|
\int_0^\Delta (X+y)h(y)\,dy
\right|\\
&\ge
X|m|-\Delta V
=|m|(X-\Delta\kappa).
\end{aligned}
\tag{21}
\]

Also

\[
|K_X'(v)|
\le
\Delta(X+\Delta)V
\le
\frac54\Delta X\kappa|m|.
\tag{22}
\]

If

\[
\kappa\ge\frac{X}{4\Delta},
\tag{23}
\]

then the source-conditioning norm (7) is already linear in `X`. Otherwise (21) gives

\[
|K_X(0)|>\frac34X|m|.
\tag{24}
\]

For

\[
|v|\le
r:=\frac1{5\Delta\kappa}
\le\frac1{5\Delta},
\tag{25}
\]

(22) implies

\[
|K_X(v)-K_X(0)|
\le\frac14X|m|,
\tag{26}
\]

and therefore

\[
|K_X(v)|\ge\frac12X|m|.
\tag{27}
\]

Integrating on `[-r,r] subset I` yields

\[
\boxed{
\mathcal C_X(I)
\ge
\frac{X}{5\Delta\kappa}
}
\qquad
\left(
\kappa<\frac{X}{4\Delta}
\right).
\tag{28}
\]

Combining the two cases gives the compact tradeoff

\[
\boxed{
\kappa\,
\max\{1,\mathcal C_X(I)\}
\ge
\frac{X}{5\Delta}.
}
\tag{29}
\]

In particular, for sufficiently large `X`,

\[
\boxed{
\max\{\kappa,\mathcal C_X(I)\}
\ge
\sqrt{\frac{X}{5\Delta}}.
}
\tag{30}
\]

Thus a nonzero-mean complex profile cannot simultaneously have a well-conditioned absolute source map and a subpolynomial central reconstruction norm. Suppressing the `NB-214` central lobe is possible only by increasing the amount of signed cancellation in the source normalization or by paying the reconstruction tariff directly.

## 5. What the tradeoff means on the Vinogradov--Korobov diagonal

The coupled scale in `NB-212`--`NB-214` is

\[
X=Q^{2/3+o(1)},
\qquad
Q:=\log(10+|t|).
\tag{31}
\]

Equation (15) says that any **global** absolute reconstruction after one primitive still has normalized cost

\[
\mathcal C_X(\mathbb R)
\ge
Q^{2/3+o(1)}.
\tag{32}
\]

Even if one exports most of that norm outside the central contour segment, (30) shows that a proof which closes both the source acquisition and the central primitive reconstruction only through their bare `L^infinity` operator norms must pay at least

\[
\boxed{
Q^{1/3+o(1)}
}
\tag{33}
\]

in one of the two channels.

That is still a positive-power prefactor. By the phase diagram in `NB-212`, changing the exponent of a positive power does not move this absolute-norm architecture into the polylogarithmic or bounded-prefactor classes; it remains in the same log-squared diagonal growth class.

The conclusion is deliberately about **operator-norm closure**. A source-specific estimate can beat `kappa` by exploiting structure of the actual defect rather than a uniform envelope, and the actual analytic function `log zeta` can cancel against `K_X` far below `mathcal C_X(I)`. Such improvements would use precisely the correlation discarded by the absolute-value method and are not ruled out here.

## 6. Why signed modulation moves the cost rather than destroying it

The geometry behind (15) is simple. Multiplying a fixed shell profile by an oscillatory phase `e^{-iOmega y}` translates its Fourier amplitude toward frequency `Omega`. Such a modulation can make the central values of `A` and `K_X` small, apparently evading the positive central-lobe proof of `NB-214`.

But the source mean then becomes the Fourier coefficient of the unmodulated profile at frequency `Omega`. As that coefficient shrinks, the normalization ratio `kappa=V/|m|` grows, while the global reconstruction mass has merely moved toward the translated frequency. Equations (15) and (29) formalize exactly this two-sided effect without requiring a particular modulation model.

This also explains why an artificial carrier cancellation is not free. A profile oscillating on the carrier scale can shift reconstruction mass out of the central contour, but relative to its remaining mean signal it becomes strongly ill-conditioned. The tariff has been exported from local reconstruction to source normalization and contour tails, not removed.

## 7. Boundaries and adversarial checks

**Zero mean is not covered.** If

\[
\int_0^\Delta h(y)\,dy=0,
\tag{34}
\]

then the barycentric source signal used for normalization here vanishes, and neither (15) nor (29) applies. A zero-mean profile must justify a different destination-visible signal, for example a higher moment or another source functional. That is a genuinely different signed/complex branch rather than a counterexample to this finding.

**The global and local statements have different force.** Equation (15) is completely sign-blind but concerns the whole frequency line. Equation (29) concerns one fixed central contour neighbourhood and therefore introduces the total-variation conditioning `kappa`. A profile with very large `kappa` may indeed move almost all reconstruction mass outside that neighbourhood.

**This is not a lower bound for the true zeta remainder.** The actual integral against `log zeta` can be much smaller than its `L^infinity -> C` operator norm. The result only says that signed shell engineering cannot improve the absolute-norm architecture without transferring the cost to another channel.

**A growing shell is outside the theorem.** The constants use fixed `Delta`. Allowing the logarithmic support width to grow with `X` changes the physical observable and the reciprocal reconstruction multiplier. That representation needs a separate source-fidelity audit.

**The positive Euler defect is an averaged source condition, not an `L^infinity` one.** Equation (7) identifies the exact cost for a bare uniform source envelope. Transferring the actual averaged positive-return condition to a signed profile may require additional regularity or a stronger norm, and can therefore be more expensive; this finding does not claim that `kappa` is always the complete acquisition cost.

**No Nyman destination theorem is obtained.** As in `NB-212`--`NB-214`, the result remains source-side. It does not prove that near-optimal Nyman approximation forces the positive Euler return or any particular signed-shell observable.

## 8. Representation, duplication, and prior-art audit

**Representation audit.** The global inequality is generic Fourier-algebra duality. A fixed-shell multiplier `(X+y)` can be inverted on its physical support by `(X+y)^(-1)`, whose Fourier transform has sup norm `O(1/X)`. Pairing that inverse multiplier with the reconstruction transform forces an `Omega(X)` Fourier `L^1` norm. The arithmetic content is not the harmonic-analysis inequality itself; it is that the source/primitive pair

\[
-\zeta'/\zeta
\quad\leftrightarrow\quad
\log\zeta
\tag{35}
\]

produces exactly this shell multiplier, and that the Vinogradov--Korobov diagonal identifies `X=Q^(2/3+o(1))`.

**Duplication audit.** `NB-161` also prices signed cancellation by conditioning, but for Jordan transport of a Poisson zero sampler; `NB-164` prices growing moment annihilation through polynomial approximation of the Poisson target. The present claim is different: it is a Fourier-dual lower bound for the Mellin *reconstruction operator* of the fixed Euler shell, plus a local source-conditioning tradeoff. `NB-214` proves the stronger central `Omega(X)` bound under positivity; the new content is that global `Omega(X)` survives arbitrary signs and that escaping the central segment has the quantitative tariff (29).

**Prior-art audit.** A targeted search found the expected general literature around Fourier/Wiener algebras, Paley--Wiener/Bernstein inequalities, and uncertainty principles. No external theorem is load-bearing here. Equations (11)--(15) are direct Fourier inversion plus `L^1`--`L^infinity` duality, while (21)--(29) use only the derivative bound coming from fixed support. The zeta identities and Vinogradov--Korobov inputs are already anchored in `SOURCES.md`, so no new source entry is required.

## 9. Research consequence

`NB-214` left signed/complex fixed-shell preconditioning as one of the explicit routes around positivity. `NB-215` narrows that route substantially.

For any signed or complex profile that retains the same nonzero barycentric source signal, **the full absolute reconstruction tariff remains linear in `X` regardless of sign cancellation**. To make the central safe-contour norm smaller, the profile must either become increasingly ill-conditioned relative to that mean or export the unavoidable reconstruction mass into contour tails. If both source acquisition and central reconstruction are then closed by absolute operator norms, at least one retains a positive-power `Q` tariff on the coupled diagonal.

The live escape is therefore no longer merely “use signs.” It must do at least one genuinely stronger thing: exploit the actual oscillatory correlation with `log zeta` before absolute values, replace the nonzero-mean barycentric signal by a source-justified zero-mean/higher-moment observable, or change the fixed-shell geometry itself. Those are mathematically different mechanisms and can now be tested separately.