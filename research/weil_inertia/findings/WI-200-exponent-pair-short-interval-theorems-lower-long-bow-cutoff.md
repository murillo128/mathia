# WI-200 — exponent-pair short-interval theorems lower the long-bow cutoff to 1515/4816

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT + DECISIVE-NEGATIVE`.

WI-198 and WI-199 used the audited Karatsuba every-interval threshold `27/82` to constrain source-compatible Maynard--Pratt bows. A primary-source audit now closes the lower-threshold evidence gate that WI-199 deliberately left open. Two published theorem surfaces parameterize the relevant short-interval results by an arbitrary exponent pair `(kappa,lambda)` through

\[
\theta(\kappa,\lambda)=\frac{\kappa+\lambda}{2\kappa+2},
\]

and both record the Bourgain--Watt consequence

\[
\boxed{\theta_*\le \frac{1515}{4816}=0.314576411960\ldots<\frac{27}{82}.}
\]

Sh. A. Khayrulloev proves an every-interval Selberg-type lower bound for odd-order critical-line zeros at length `T^(theta(kappa,lambda)+epsilon)`. Z. Kh. Rakhmonov proves a narrow-rectangle zero-density theorem for every interval of length exceeding the same exponent-pair threshold. Combining those theorem surfaces with the exact bow bookkeeping already established in WI-184, WI-198, and WI-199 removes the entire exponent band

\[
\boxed{\frac{1515}{4816}<\vartheta\le\frac{27}{82}}
\]

from two previously live bow mechanisms.

First, a mirror-closed count-saturating Maynard--Pratt bow is impossible for every fixed `vartheta>1515/4816`, not only for `vartheta>27/82`; the same argument forces a fixed positive spacing gap above the `4 pi` mirror-count threshold for bounded-scale families. Second, even without count saturation, the explicit Maynard--Pratt deep plateau is impossible in that larger range: Rakhmonov's density theorem forces the fraction of selected bow labels at every fixed physical depth `beta-1/2>1/12` to tend to zero. The latter theorem does **not** reproduce WI-199's stronger normalized-depth screening tail `A=(beta-1/2) log T=O(1)`, so the screening-scale/source-covariance problem remains genuinely separate.

No unconditional simple-critical-zero proportion changes here. The result does not prove RH, does not exclude short bows with `vartheta<=1515/4816`, and does not turn odd-order critical-line zeros into simple zeros.

## 1. Audited every-interval critical-line input

The primary source is Sh. A. Khayrulloev, **On the estimate of the number of odd-order zeros of the Riemann zeta function lying on the critical line**, *Izvestiya of the National Academy of Sciences of Tajikistan, Department of Physical, Mathematical, Chemical, Geological and Technical Sciences*, 2024, No. 4 (197), pp. 51--64, ISSN 2791-2337, journal PDF:

https://journals.anrt.tj/files/News_m/news_m_2024_04.pdf

Theorem 1 states that for an arbitrary exponent pair `(kappa,lambda)`, any fixed `0<epsilon<=0.001`, and sufficiently large `T`, with

\[
\theta(\kappa,\lambda)=\frac{\kappa+\lambda}{2\kappa+2},
\qquad
H=T^{\theta(\kappa,\lambda)+\epsilon},
\]

there is a constant `c(epsilon)>0` such that

\[
\boxed{
N_{0,\mathrm{odd}}(T+H)-N_{0,\mathrm{odd}}(T)
\ge c(\epsilon)H\log T.
}
\tag{1}
\]

Here `N_{0,odd}` counts odd-order zeros of `zeta(1/2+it)` on the critical line. There is no exceptional-center qualifier in the theorem. Khayrulloev then invokes the Bourgain--Watt exponent-pair bound and states Corollary 1.1 with exponent `1515/4816`.

The load-bearing point for the bow application is the **every-interval** quantifier. An almost-all theorem would not suffice because the bow height is source-selected.

## 2. Count-saturating bows are excluded above 1515/4816

Retain the source-compatible bow notation of WI-184 and WI-198. Let the selected right-half bow contain

\[
m_T=T^{\vartheta+o(1)}
\]

labels, with bounded positive unfolded spacing scale `c_T`, so its vertical span is

\[
L_T=(c_T+o(1))\frac{m_T}{\log T}.
\tag{2}
\]

Assume all but `O(1)` selected right-half labels are off the critical line and include their compulsory same-ordinate functional-equation mirrors, exactly as in the displayed Maynard--Pratt bow.

Fix

\[
\vartheta>\theta_*:=\frac{1515}{4816}.
\]

Choose a fixed `epsilon>0` with

\[
\theta_*+\epsilon<\vartheta,
\qquad epsilon\le0.001.
\]

Let

\[
h=T^{\theta_*+\epsilon}.
\]

Then

\[
\frac{L_T}{h}
=T^{\vartheta-\theta_*-\epsilon+o(1)}\frac1{\log T}
\longrightarrow\infty.
\tag{3}
\]

Pack a `1-o(1)` fraction of the bow interval by disjoint intervals of admissible Khayrulloev length `h`, adjusting each base point by its `1+o(1)` height if desired. Applying (1) on every packed interval and summing gives

\[
\begin{aligned}
N_{0,\mathrm{odd}}(I_{\mathrm{bow}})
&\gg_\epsilon \frac{L_T}{h}\,h\log T\\
&\asymp L_T\log T\\
&\asymp c_Tm_T.
\end{aligned}
\tag{4}
\]

Thus

\[
\boxed{N_{0,\mathrm{odd}}(I_{\mathrm{bow}})\gg_\vartheta m_T.}
\tag{5}
\]

Only `O(1)` of these can be the selected on-line bow endpoints in the Maynard--Pratt geometry. The rest are a compulsory complementary critical-line population. In WI-184's excess-count notation,

\[
\boxed{E_I\gg_\vartheta m_T.}
\tag{6}
\]

Therefore a mirror-closed bow with `E_I=o(m_T)` cannot exist for any fixed

\[
\boxed{\vartheta>1515/4816.}
\tag{7}
\]

This strictly strengthens WI-198's cutoff `vartheta>27/82`.

The spacing-gap consequence of WI-198 transports verbatim. If the packed theorem gives `C_I>=kappa_vartheta c_Tm_T` complementary critical-line locations, while the mirror-closed selected bow already contributes `2m_T+O(1)` off-line labels, then Riemann--von Mangoldt gives

\[
\frac{c_T}{2\pi}
\ge 2+\kappa_\vartheta c_T+o(1).
\tag{8}
\]

Hence either no bounded-scale family exists, or

\[
\boxed{
\liminf_{T\to\infty}c_T
\ge\frac{4\pi}{1-2\pi\kappa_\vartheta}
=4\pi+\delta_\vartheta
}
\tag{9}
\]

for some `delta_vartheta>0`.

## 3. Audited narrow-rectangle density input

The second primary source is Z. Kh. Rakhmonov, **Density of zeros of the Riemann zeta function in narrow rectangles of the critical strip**, *Chebyshevskii Sbornik* 26:5 (2025), 158--183, DOI `10.22405/2226-8383-2025-26-5-158-183`:

https://www.mathnet.ru/eng/cheb1627

Rakhmonov's Theorem 1 states that for an arbitrary exponent pair `(kappa,lambda)`, fixed positive `epsilon<10^-4`, sufficiently large `T`, and

\[
H>T^{\theta(\kappa,\lambda)+\epsilon},
\]

one has

\[
\boxed{
N(\alpha,T+H)-N(\alpha,T)
\ll H^{a(1-\alpha)}(\log T)^c.
}
\tag{10}
\]

For

\[
\frac12\le\alpha\le\frac23
\quad\text{or}\quad
\frac56\le\alpha\le1,
\]

the theorem gives `a=12/5` and `c=172`; for `2/3<alpha<5/6`, it gives `a=8/3` and `c=50`. The paper explicitly records Bourgain--Watt's bound `theta_*<=1515/4816` and the resulting corollary at that interval exponent. No almost-all-center qualifier appears in the theorem.

## 4. Fixed-depth long bows vanish above the same cutoff

Apply (10) directly to the whole bow interval (2). For every fixed `vartheta>theta_*`, choose fixed `epsilon>0` with `theta_*+epsilon<vartheta`. Then eventually

\[
L_T>T^{\theta_*+\epsilon}.
\]

Fix a physical horizontal depth

\[
\delta>0,
\qquad
\alpha=\frac12+\delta.
\]

When `0<delta<=1/6`, the `a=12/5` branch gives

\[
N\!\left(\frac12+\delta,I_{\mathrm{bow}}\right)
\ll
L_T^{\frac65-\frac{12}{5}\delta}(\log T)^{172}.
\tag{11}
\]

Since `m_T\asymp L_T\log T`, division by the selected bow population yields

\[
\boxed{
\frac{N(\frac12+\delta,I_{\mathrm{bow}})}{m_T}
\ll
L_T^{\frac15-\frac{12}{5}\delta}(\log T)^{171}.
}
\tag{12}
\]

Thus the right side tends to zero whenever

\[
\boxed{\delta>\frac1{12}.}
\tag{13}
\]

For `1/6<delta<1/3`, the middle branch has exponent

\[
\frac83\left(\frac12-\delta\right)<\frac89<1,
\]

so the ratio to `m_T` also tends to zero. For `delta>=1/3`, the outer `12/5` branch is smaller still. Hence, uniformly over every fixed physical depth above `1/12`,

\[
\boxed{
\frac1{m_T}
\#\left\{\rho\in B_T:\beta-\frac12\ge\delta\right\}
\longrightarrow0
\qquad
(\delta>1/12,\ \vartheta>1515/4816).
}
\tag{14}
\]

Maynard--Pratt's explicit deep bow has a fixed positive fraction of selected right-half labels at `beta=3/4`, i.e. `delta=1/4`. Equation (14) therefore rules out that deep plateau for every fixed `vartheta>1515/4816`, **without** assuming count saturation or limiting the complementary zero population.

This strictly extends WI-199's count-saturation-free exclusion of the explicit deep bow from `vartheta>27/82` down to `vartheta>1515/4816`.

## 5. The new density theorem does not reach the screening layer

The strengthening above must not be confused with WI-199's normalized-depth theorem. Put

\[
\alpha=\frac12+\frac{A}{\log T}
\]

with fixed `A`. The first Rakhmonov branch gives

\[
H^{\frac{12}{5}(1-\alpha)}
=
H^{6/5}
\exp\!\left(
-\frac{12A}{5}\frac{\log H}{\log T}
\right).
\tag{15}
\]

After division by the natural bow population `H log T`, a factor `H^(1/5)` remains, up to logarithms and an `A`-dependent constant. For fixed normalized depth `A`, this grows polynomially and (10) supplies no useful density tail.

Therefore Rakhmonov's newer threshold does **not** prove

\[
\lim_{A\to\infty}\limsup_T
\frac{\#\{\rho\in B_T:(\beta-1/2)\log T\ge A\}}{m_T}=0
\]

below the `27/82` range where WI-199 already obtained such a statement from the stronger Karatsuba--Korolev local density shape. The two consequences must remain separate:

- count saturation is excluded for `vartheta>1515/4816` by the every-interval critical-line reservoir;
- the explicit fixed-depth Maynard--Pratt plateau is excluded for `vartheta>1515/4816` by Rakhmonov;
- full normalized screening-scale localization is still established only in the range controlled by WI-199.

This distinction is load-bearing for the RH-facing program because support-one screening acts precisely at horizontal depth `O(1/log T)`.

## 6. Prior art, novelty, and evidence boundary

The exponent-pair theorem forms are prior art. Khayrulloev's 2024 paper supplies the every-interval odd-order-zero lower bound, and Rakhmonov's 2025 paper supplies the narrow-rectangle density estimate. Both explicitly credit Bourgain--Watt for the numerical exponent-pair bound `1515/4816`. The current finding does not claim any of those theorems or that exponent as new.

WI-199 had already identified exponent-pair/Rakhmonov literature as the obvious possible way to lower `27/82`, but deliberately refused to use it because the relevant primary theorem had not been independently retrieved and audited. This pass closes that evidence gate with the exact primary theorem statements. The new Mathia deduction is the application to the mirror-closed Maynard--Pratt bow: equations (4)--(9) lower the count-saturation cutoff, while equations (11)--(14) lower the count-saturation-free fixed-depth cutoff. A targeted prior-art search did not locate this specific bow consequence; no priority claim is made from absence of a search hit.

Several boundaries are essential:

1. The endpoint `vartheta=1515/4816` is **not** covered. A bow span `T^vartheta/log T` is shorter than `T^(vartheta+epsilon)` for every fixed positive `epsilon`.
2. Odd-order critical-line zeros are not necessarily simple. They are sufficient for the count-reservoir contradiction but do not increase the certified simple-critical-zero proportion by themselves.
3. Equation (14) begins only at strict fixed depth `delta>1/12`; the theorem as used does not exclude a positive-density population at shallower fixed depth, much less at `delta=A/log T`.
4. The result constrains source-compatible Maynard--Pratt bow families; it does not assert such bows occur among actual zeta zeros and does not exclude all possible off-line geometries.
5. The accepted distinguished-twist covariance clue remains unresolved. The exponent range in which a count-saturating bow can still require that source-side analysis is smaller, but the pointwise arithmetic `L^2` gate of WI-195--WI-197 is unchanged inside the surviving range.

## 7. Research consequence

The hard count-saturating bow regime is now confined to

\[
\boxed{0<\vartheta\le\frac{1515}{4816}}
\]

rather than `0<vartheta<=27/82`. The explicit deep Maynard--Pratt plateau is likewise eliminated above `1515/4816` even if arbitrary complementary zeros are allowed. What survives beyond this prior-art improvement is structurally sharper: either bows are shorter than the exponent-pair threshold, or their off-line labels must already avoid fixed physical depth; and the support-one screening problem still lives in the much thinner `O(1/log T)` layer.

Accordingly, this finding redirects rather than resolves the source-covariance program. Future bow work should not spend effort on the newly excluded exponent band. The remaining meaningful tests are the distinguished source-fixed covariance for `vartheta<=1515/4816`, or a genuinely stronger every-center near-line density theorem whose dependence on `alpha-1/2` is strong enough to reach normalized screening depth below WI-199's `27/82` threshold.