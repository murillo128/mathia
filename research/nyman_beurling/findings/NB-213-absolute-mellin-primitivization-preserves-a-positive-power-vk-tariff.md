# NB-213 — Absolute Mellin primitivization preserves a positive-power Vinogradov--Korobov tariff

**Date:** 2026-09-18  
**Status:** `DERIVED + METHOD-BOUNDARY + REPRESENTATION-AUDIT + SOURCE-ACQUISITION + VINOGRADOV-KOROBOV + NB-212-REFINEMENT`.

`NB-212` reduces the current source-side problem to the growth class of the prefactor in a smoothed full-von-Mangoldt contour estimate. A natural attempted repair is to integrate the logarithmic derivative once, replace `-zeta'/zeta` by the apparently smaller primitive `log zeta`, and hope that this turns a polynomial `Q`-prefactor into a polylogarithmic or bounded one.

That repair does **not** change the diagonal growth class if the transferred contour is then estimated by absolute values. The reason is representation-theoretic rather than a weakness of a particular bound: differentiating the Mellin carrier `exp(iXv)` costs a factor `X=log x`. On the coupled Vinogradov--Korobov scale relevant to `NB-212`,

\[
Q\asymp \frac{X^{3/2}}{(\log X)^\gamma},
\qquad
X=Q^{2/3+o(1)},
\]

so this carrier factor is itself a positive power of `Q`. Consequently, even granting the optimistic envelope `|log zeta|=Q^{o(1)}` on the shifted contour, ordinary integration by parts only replaces the old polynomial prefactor by

\[
XQ^{o(1)}=Q^{2/3+o(1)},
\]

which still lies in the polynomial class of the `NB-212` phase diagram and therefore still stops at the `X^(3/2)/(log X)^2` corridor. Any genuine improvement must avoid taking absolute values after the primitive transfer, exploit cancellation between the primitive and the oscillatory carrier, or change the observable so that a compensating reciprocal carrier factor is present before reconstruction.

## 1. The shifted full-source remainder has a fixed Mellin carrier

Use the notation of `NB-212`, writing

\[
X:=\log x,
\qquad
Q:=\log(10+|t|),
\qquad
R(Q):=Q^{2/3}(\log Q)^{1/3}.
\tag{1}
\]

After Mellin inversion and a shift to a safe fraction of the Vinogradov--Korobov zero-free width, the non-polar part of the normalized smoothed full-source correlation has the schematic form

\[
\mathcal R(X,t)
=
e^{-\delta X}
\int_{\mathcal I}
A_\delta(v)
\frac{\zeta'}{\zeta}
\bigl(\sigma+i(t+v)\bigr)
e^{iXv}\,dv
+\mathcal T(X,t),
\tag{2}
\]

where

\[
\delta\asymp \frac1{R(Q)},
\qquad
\sigma=1-\delta,
\tag{3}
\]

`A_delta` is the Mellin transform of a fixed smooth shell profile, `mathcal I` is the safe truncated vertical segment used in the contour argument, and `mathcal T` denotes the already-controlled Mellin and horizontal tails. For a fixed smooth profile, the relevant amplitudes satisfy uniformly

\[
\|A_\delta\|_{L^1}
+
\|A_\delta'\|_{L^1}
\ll_f 1
\tag{4}
\]

throughout the small displacements under discussion. The exact sign in front of `zeta'/zeta` is irrelevant below.

The only feature needed for the present audit is the simultaneous presence of the logarithmic derivative and the carrier

\[
e^{iXv}.
\tag{5}
\]

This carrier records that the arithmetic source has been localized near the multiplicative shell `n asymp x`.

## 2. One primitive transfer necessarily differentiates the carrier

On a zero-free connected segment of the shifted contour choose a branch

\[
L(v)
:=
\log\zeta\bigl(\sigma+i(t+v)\bigr).
\tag{6}
\]

Then

\[
L'(v)
=
i\frac{\zeta'}{\zeta}
\bigl(\sigma+i(t+v)\bigr).
\tag{7}
\]

Insert a harmless smooth truncation at the endpoints of `mathcal I` if necessary, so that the boundary term vanishes; this does not change (4). Integration by parts therefore rewrites the vertical integral in (2), up to an irrelevant unit complex factor, as

\[
\int_{\mathcal I}
\bigl(A_\delta'(v)+iX A_\delta(v)\bigr)
L(v)e^{iXv}\,dv.
\tag{8}
\]

Suppose, deliberately optimistically, that the primitive satisfies an envelope

\[
|L(v)|\le B(Q)
\tag{9}
\]

throughout the effective contour. Taking absolute values after (8) gives

\[
\boxed{
|\mathcal R(X,t)|
\ll_f
e^{-\delta X}
(1+X)B(Q)
+|\mathcal T(X,t)|.
}
\tag{10}
\]

Thus the ordinary primitive transfer has not removed the prefactor. It has exchanged the pointwise cost of `zeta'/zeta` for the derivative cost of the Mellin carrier. Even the hypothetical best-case size law

\[
B(Q)=Q^{o(1)}
\tag{11}
\]

leaves the normalized contour error with prefactor

\[
L_{\rm prim}(X,Q)
=
XQ^{o(1)}.
\tag{12}
\]

Equation (10) is a **method bound**, not a lower bound for the true contour integral. Cancellation in (8) may make the integral much smaller. What it rules out is obtaining the desired growth-class improvement merely by replacing `zeta'/zeta` with a primitive and then applying a uniform absolute-value estimate to that primitive.

## 3. On the coupled diagonal the carrier tariff is a positive power of `Q`

Test the same family of scales as `NB-212`,

\[
Q
=
\kappa
\frac{X^{3/2}}{(\log X)^\gamma},
\tag{13}
\]

with fixed `gamma>0`. Taking logarithms gives

\[
\log Q
=
\left(\frac32+o(1)\right)\log X,
\tag{14}
\]

and hence

\[
\boxed{
X=Q^{2/3+o(1)}.
}
\tag{15}
\]

Therefore (11)--(12) imply

\[
\boxed{
L_{\rm prim}(X,Q)
=
Q^{2/3+o(1)}.
}
\tag{16}
\]

This is exactly the positive-power class covered by the phase diagram in `NB-212`. One can also see the threshold directly. The Vinogradov--Korobov displacement supplies

\[
\frac{X}{R(Q)}
=
\left(C\kappa^{-2/3}+o(1)\right)
(\log X)^{(2\gamma-1)/3}
\tag{17}
\]

for a fixed `C>0`, while the carrier tariff contributes

\[
\log L_{\rm prim}(X,Q)
=
(1+o(1))\log X.
\tag{18}
\]

If `gamma<2`, then the exponent in (17) is `o(log X)` and cannot absorb (18). At `gamma=2`, both are order `log X`, and a sufficiently small fixed `kappa` lets the zero-free displacement win. Consequently

\[
\boxed{
\text{absolute primitive transfer}
\quad\Longrightarrow\quad
Q\lesssim
\frac{X^{3/2}}{(\log X)^2}
\text{ at the growth-class level.}
}
\tag{19}
\]

The conclusion remains unchanged if the primitive envelope is polylogarithmic in `Q`, since multiplying a polylogarithm by `X` still gives `Q^{2/3+o(1)}`.

## 4. The same tariff is visible directly in the Euler coefficients

For `Re(s)>1`,

\[
-\frac{\zeta'}{\zeta}(s)
=
\sum_{n\ge2}\frac{\Lambda(n)}{n^s},
\qquad
\log\zeta(s)
=
\sum_{n\ge2}
\frac{\Lambda(n)}{\log n}\frac1{n^s}.
\tag{20}
\]

On the fixed multiplicative shell `n in [x,e^Delta x]`,

\[
\log n
=
X+O_\Delta(1).
\tag{21}
\]

Thus primitivization divides the actual von-Mangoldt coefficient by `X+O(1)`. Recovering the original source correlation from that primitive must correspondingly restore a factor of shell logarithmic size. In the contour representation that restoration is exactly the `iX A_delta(v)` term in (8).

This gives a useful representation interpretation of (10): **the apparent analytic gain from replacing `Lambda(n)` by `Lambda(n)/log n` is cancelled by the cost of reconstructing the source on a shell with `log n asymp X`.** The phenomenon is not peculiar to a specific explicit bound for `log zeta`; it comes from the relation between the primitive coefficients and the Mellin carrier.

## 5. Finite repeated primitivization does not repair the growth class by itself

The same calculation applies to any finite sequence of ordinary contour primitive transfers. If a `j`-fold primitive `P_j(v)` is introduced and the resulting integral is bounded absolutely, the differentiated fixed carrier-amplitude is

\[
\left(\frac d{dv}+iX\right)^j A_\delta(v).
\tag{22}
\]

For fixed nonzero smooth `A_delta`, its `L^1` size is

\[
\left\|
\left(\frac d{dv}+iX\right)^j A_\delta
\right\|_1
=
X^j\|A_\delta\|_1+O_{f,j}(X^{j-1}).
\tag{23}
\]

Hence an envelope `|P_j|<=Q^{o(1)}` yields an absolute contour bound carrying

\[
X^jQ^{o(1)}
=
Q^{2j/3+o(1)}.
\tag{24}
\]

Every fixed `j>=1` therefore remains in the positive-power class of `NB-212`. Repeating the same maneuver more times makes the absolute prefactor larger, not smaller.

This statement is intentionally limited to **finite, ordinary primitive transfers with an absolute-value closure**. It does not rule out an `X`-dependent transform engineered so that the carrier derivative cancels, nor an oscillatory estimate for (8) or (22) that uses phase information before taking absolute values. Those would be genuinely different mechanisms.

## 6. What would actually count as progress past the `NB-212` boundary

The calculation closes one tempting but superficial route: a better pointwise size class for an antiderivative of `zeta'/zeta` is not enough if converting it back to the shell correlation costs `X`. To change the `NB-212` phase diagram, a source argument must instead produce at least one of the following effects intrinsically:

- cancellation in the shifted integral strong enough to recover a reciprocal `X^{1-o(1)}` factor before absolute values are taken;
- a source-faithful observable whose Mellin representation has subpolynomial `Q`-prefactor **without** reconstructing `Lambda` by differentiating an `e^{iXv}` carrier;
- a correlation or bilinear structure in which the primitive gain and carrier oscillation are estimated together rather than separately.

Merely improving a polynomial pointwise bound for `zeta'/zeta`, or replacing it by a bounded/polylogarithmic primitive and then using `L^1` control, cannot alter the logarithmic exponent of the current corridor.

The separate destination problem is unaffected: even a stronger source-side correlation theorem must still be coupled back to an actual Nyman approximant, and signed/complex synthesis still lies outside the monotone positive-return implication used in `NB-212`.

## 7. Representation and prior-art audit

**Representation audit.** The carrier tariff is generic Mellin/Fourier geometry. Whenever a source localized near `n asymp x` is represented by a vertical Mellin integral with carrier `e^{iXv}`, moving a derivative from the transform to the carrier introduces `X=log x`. The specifically arithmetic input here is that the full Euler source is represented by `-zeta'/zeta`, its primitive is `log zeta` with coefficients `Lambda(n)/log n`, and the available zero-free displacement has Vinogradov--Korobov shape `1/R(Q)`. Combining those facts with the coupled diagonal converts the generic carrier factor into the arithmetic statement (19).

**Prior-art audit.** Mellin inversion, the identity `(log zeta)'=zeta'/zeta`, integration by parts, and the Dirichlet series in (20) are classical. No novelty is claimed for them. The load-bearing zero-free input remains Bellotti's Vinogradov--Korobov region already recorded in `SOURCES.md`, and the smoothed full-source contour representation is inherited from `NB-211`--`NB-212`. A targeted prior-art search found standard explicit-formula and near-one logarithmic-derivative literature, but no additional theorem is required for the carrier-tariff calculation, so `SOURCES.md` does not need another anchor.

The project-local contribution is the coupled method audit: on the exact moving scale posed by `NB-212`, even an optimistically subpolynomial primitive envelope becomes polynomial after source reconstruction. This removes ordinary Mellin primitivization from the list of candidate mechanisms for reaching the polylogarithmic or bounded-prefactor regimes.

## 8. Adversarial checks and boundaries

**This is not a lower bound for the true contour remainder.** Equation (10) describes what the primitive-plus-absolute-values proof architecture can certify. The oscillatory integral in (8) could be much smaller through cancellation; exploiting that cancellation is precisely one of the remaining routes.

**The branch of `log zeta` is local to a zero-free contour.** The argument only requires a continuous analytic branch on the same safe truncated segment on which the Vinogradov--Korobov shift is performed. Smooth truncation removes endpoint terms. No global branch is assumed.

**A miraculous primitive size bound is granted rather than proved.** The conclusion is stronger as a method boundary because (11) is deliberately optimistic. If the available primitive bound grows polynomially, the obstruction is only worse. Conversely, a primitive estimate that already contains a compensating factor `X^{-1+o(1)}` is outside the hypothesis and would represent genuinely new cancellation, not a mere pointwise size improvement.

**The finding does not improve the positive-return corridor.** Its value is eliminative: it explains why a natural attempt to lower the contour prefactor cannot change its growth class and narrows the next source-side search to mechanisms that couple carrier oscillation and arithmetic cancellation before absolute values.

## 9. Research consequence

The live source question after `NB-212` should therefore be read more narrowly. A subpolynomial or bounded final prefactor cannot be obtained simply by integrating `-zeta'/zeta` to `log zeta` and estimating the latter pointwise. The desired gain has to survive **after** the source is reconstructed at shell scale.

A useful next test is consequently not another pointwise logarithmic-derivative estimate with a smaller polynomial exponent. It is to search for a source-faithful smoothed correlation identity in which the oscillatory Mellin carrier is retained inside the cancellation argument, and then ask whether that joint estimate produces an actual `Q^{o(1)}` prefactor. If no such mechanism is available, the `NB-212` log-squared corridor should be treated as the natural ceiling of absolute-value Vinogradov--Korobov contour methods rather than as an artifact of the particular `Q^2` bound used there.
