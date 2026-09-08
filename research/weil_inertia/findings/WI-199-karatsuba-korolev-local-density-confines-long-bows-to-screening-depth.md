# WI-199 — Karatsuba--Korolev local density confines long bows to screening depth

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`. This finding does **not** improve the unconditional simple-critical-zero proportion and does not assert that Maynard--Pratt bows occur among the zeros of zeta. It combines the every-center short-rectangle zero-density theorem of Karatsuba--Korolev with the explicit Maynard--Pratt bow geometry. Above the Karatsuba exponent `27/82`, any source-selected bow of polynomial length and bounded critical-scale vertical spacing can contain only an exponentially small fraction of labels at any fixed positive normalized horizontal depth `A=(beta-1/2) log T`; in particular, only a power-saving fraction can stay a fixed physical distance to the right of the critical line. Thus the explicit Maynard--Pratt deep bow, whose middle half lies at `beta=3/4`, cannot occur in that exponent range even when the bow is **not** count-saturating. The surviving long-bow adversary is forced into the same `O(1/log T)` horizontal screening layer already isolated globally in WI-029.

## 1. Primary-source theorem used

The load-bearing source is A. A. Karatsuba and M. A. Korolev, **Behaviour of the argument of the Riemann zeta function on the critical line**, *Russian Mathematical Surveys* 61:3 (2006), 389--482, DOI `10.1070/RM2006v061n03ABEH004328` (Russian original: *Uspekhi Mat. Nauk* 61:3(369), 3--92). Their Chapter I fixes an arbitrarily small constant

\[
0<\eta<0.001,
\]

and, in the every-center case relevant here, takes

\[
h=t^{27/82+\eta},
\qquad
x=t^{0.1\eta}.
\tag{1}
\]

For every sufficiently large center `t` and every `1/2 <= sigma <= 1`, their displayed short-rectangle density bound is

\[
\boxed{
N(\sigma,t+h)-N(\sigma,t-h)
\le 13h(\log t)x^{1-2\sigma}.
}
\tag{2}
\]

Here `N(sigma,U)` counts zeta zeros with real part at least `sigma` and ordinate up to `U`, with multiplicity. The primary article states (2) explicitly in its notation summary and derives it in Chapter I; later in the same article the factor is used as `26H log T exp(-0.2 k eta)` after discretizing `beta-1/2` in units of `1/log T`. No RH, zero-line hypothesis, typical-center restriction, or finite-vertical-line hypothesis is present in this every-center form.

This exact theorem is stronger for the present normalized-depth question than merely applying a global/dyadic density estimate: it acts in a window of height `t^{27/82+eta}` around the **distinguished source-selected height**.

## 2. A local exponential tail inside any longer bow interval

Let `theta>27/82` be fixed. Consider a source-selected right-half-plane bow population `B_T` of

\[
m_T=T^{\theta+o(1)}
\tag{3}
\]

labels whose ordinates lie in one interval `I_T` at height `asymp T`, and suppose its unfolded vertical spacing scale is bounded above and below, so that

\[
|I_T|=L_T=(c_T+o(1))\frac{m_T}{\log T},
\qquad
0<c_-\le c_T\le c_+<\infty.
\tag{4}
\]

This includes the fixed-`c` Maynard--Pratt model. Choose

\[
0<\eta<\min\!\left(0.001,\theta-\frac{27}{82}\right).
\tag{5}
\]

Since every center in `I_T` is `T(1+o(1))`, windows of the form (1) have height

\[
h=T^{27/82+\eta+o(1)}=o(L_T).
\tag{6}
\]

Cover `I_T` by

\[
J_T=O\!\left(1+\frac{L_T}{h}\right)
\tag{7}
\]

such symmetric Karatsuba--Korolev windows. Summing (2) over the cover is harmless for an upper bound even if boundary zeros are counted more than once.

Fix `A>=0` and put

\[
\sigma_T(A)=\frac12+\frac{A}{\log T}.
\tag{8}
\]

For fixed `A` and `T` sufficiently large this lies in `[1/2,1]`. Uniformly over the covering centers,

\[
x^{1-2\sigma_T(A)}
=
\exp\!\left(-\frac{\eta}{5}A+o(1)\right).
\tag{9}
\]

Using (2), (6), and (7),

\[
\#\left\{\rho=\beta+i\gamma\in B_T:
(\beta-\tfrac12)\log T\ge A\right\}
\ll_{\theta,\eta,c_+}
L_T\log T\,e^{-\eta A/5+o(1)}.
\tag{10}
\]

By (4), `L_T log T=(c_T+o(1))m_T`, hence

\[
\boxed{
\limsup_{T\to\infty}
\frac{1}{m_T}
\#\left\{\rho\in B_T:
(\beta-\tfrac12)\log T\ge A\right\}
\ll_{\theta,\eta,c_+} e^{-\eta A/5}.
}
\tag{11}
\]

Consequently

\[
\boxed{
\lim_{A\to\infty}\limsup_{T\to\infty}
\frac{\#\{\rho\in B_T:(\beta-\tfrac12)\log T\ge A\}}{m_T}=0.
}
\tag{12}
\]

Equation (12) is a **source-localized screening-scale theorem**: a positive-density portion of a long bow cannot live at normalized depth tending to infinity.

## 3. Fixed physical depth is power-saving

The same calculation is stronger when the horizontal displacement is a fixed physical amount. Fix `0<delta<=1/2` and put

\[
\sigma=\frac12+\delta.
\]

Then (2) gives

\[
x^{1-2\sigma}=T^{-\eta\delta/5+o(1)},
\]

and the covering argument yields

\[
\boxed{
\frac{\#\{\rho\in B_T:\beta-\tfrac12\ge\delta\}}{m_T}
\ll_{\theta,\eta,c_+}
T^{-\eta\delta/5+o(1)}.
}
\tag{13}
\]

Thus every fixed positive physical depth has density zero inside such a bow, with an explicit power saving. This conclusion does not use the total zero count in `I_T` and therefore does not require the bow to saturate Riemann--von Mangoldt.

## 4. The explicit Maynard--Pratt deep bow is excluded above `27/82`

Maynard and Pratt's Section 8 adversarial model has `m=T^theta` consecutive hypothetical labels, ordinate spacing `c/log T`, and real parts that rise from `1/2` to `3/4`, stay at `3/4` through the middle portion, and then return to `1/2`. In particular, a fixed positive fraction of the selected right-half labels satisfy, for example,

\[
\beta-\frac12\ge\frac18.
\tag{14}
\]

If `theta>27/82`, equation (13) says that the fraction satisfying (14) tends to zero. Therefore

\[
\boxed{
\text{the explicit deep Maynard--Pratt bow cannot be an actual zeta-zero block when }
\theta>27/82.
}
\tag{15}
\]

This is logically different from WI-198. WI-198 uses Karatsuba's **critical-line lower reservoir** plus Riemann--von Mangoldt to show that a long source-compatible bow cannot be count-saturating and, at bounded spacing, must pay a positive spacing gap above the `4 pi` saturation scale. Equation (15) makes no count-saturation assumption: even if arbitrary complementary zeros are admitted, the selected bow itself cannot retain a positive-density deep off-line plateau.

Functional-equation reflection only strengthens the population bookkeeping and is not needed in the proof of (11)--(15): Karatsuba--Korolev already count all right-half zeros in each short rectangle, so the source-selected right-half bow labels form a subset of the population controlled by (2).

## 5. Relation to WI-029 and the screening obstruction

WI-029 rescales the published global Jutila density theorem and proves that any **dyadic positive-density** off-line population is exponentially tight in

\[
Y=|\beta-\tfrac12|\log T.
\]

It then shows that this global localization lands exactly in the WI-006 critical-sampling screening regime and therefore does not by itself produce a defect-to-zero bootstrap.

The new point here is locality. Equations (11)--(12) hold **inside the source-selected polynomial bow interval itself**, provided its exponent exceeds `27/82`. Thus complementary zeros elsewhere in `[T,2T]` cannot absorb the zero-density budget and leave the distinguished bow deep. The price is the hard interval-length threshold: Karatsuba--Korolev's every-center theorem does not reach the `0<theta<=27/82` range that remains live in the current bow program.

The unfavorable conclusion for Weil inertia is therefore also sharp at the level of mechanism: the theorem removes deep horizontal drift in the long-bow regime, but what survives is precisely a moving population with

\[
\beta-\frac12=O(1/\log T)
\]

for all but a small fraction of labels. That is the confluence/screening scale where WI-005/WI-006 and the current distinguished-covariance problem already show that horizontal depth alone is not a coercive observable.

## 6. Prior art and novelty audit

**Literature-backed inputs.** Equation (2), including the constant `13`, the exponent `27/82+eta`, and `x=T^{0.1 eta}`, is Karatsuba--Korolev prior art. The explicit deep bow geometry is Maynard--Pratt prior art from **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`.

**New repository deduction.** The covering argument (10), normalized bow-local tail (11)--(12), fixed-depth power saving (13), and the count-saturation-free exclusion (15) are exact consequences obtained by combining those two published theorem surfaces. A targeted search found no source making this specific source-localized bow consequence; no priority claim is made from absence of a search hit.

There is neighboring exponent-pair literature reporting shorter critical-line and short-rectangle thresholds, including Rakhmonov's work. A detailed 2020 scholarly review states an exponent-pair version with `theta(kappa,lambda)=(kappa+lambda)/(2kappa+2)` and records `131/416` as an admissible upper bound. The original 2006 Rakhmonov critical-line paper was not independently retrieved and audited in this pass, so **that lower threshold is deliberately not used as evidence here**. Any attempt to replace `27/82` in (5)--(15) must first verify the exact primary theorem, its zero-count convention, quantifiers, and admissibility of the claimed exponent input.

## 7. Boundaries and falsification tests

This finding would fail if the every-center Karatsuba--Korolev bound (2) had an omitted exceptional-center hypothesis, if its `x=T^{0.1 eta}` normalization were misread, or if the bow interval could not be covered by `O(L_T/h)` comparable-height windows. The primary article was checked directly on all three points: (2) is stated for every sufficiently large center in the `27/82+eta` case; the exceptional-set construction belongs to the separate almost-all-center shorter-window case; and `theta>27/82+eta` gives `h=o(L_T)`.

The result does **not**:

- cover `theta<=27/82`, including the endpoint;
- show that every off-line zero in a long bow is shallow, only that deep labels have vanishing density with the quantitative tail (11);
- distinguish a shallow off-line mirror pair from an on-line multiple zero through the support-one Weil compression;
- prove the source-fixed negative off-diagonal cancellation required by WI-195;
- improve the current unconditional simple-critical-zero proportion;
- rule out a bow whose selected labels already live at normalized depth `Y=O(1)`.

The decisive next question in the long-bow direction is whether a fully audited every-center theorem below `27/82` exists and carries a strong enough **near-line** dependence to reproduce (11), rather than merely guaranteeing one or many critical-line zeros. In the surviving short-bow regime, the canonical source-fixed `L^2` covariance gate remains unchanged.