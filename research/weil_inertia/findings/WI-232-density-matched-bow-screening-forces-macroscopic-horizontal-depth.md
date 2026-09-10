# WI-232 — density-matched bow screening forces macroscopic horizontal depth

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE + DECISIVE-NEGATIVE`.

WI-184 identifies `4\pi/\log T` as the asymptotic vertical spacing at which a symmetrized Maynard--Pratt bow saturates the mean Riemann--von Mangoldt zero count. WI-231 then proves that a local complementary population cancelling the first reciprocal harmonic must obey the exact count--depth tariff

\[
R\cosh a_{\max}\ge (2-\eta)M.
\tag{1}
\]

There is a stronger conclusion when the bow is matched to the **actual local Riemann--von Mangoldt density**, rather than only to its leading `\log T` approximation. Let `T_0\asymp T`, put

\[
\ell_0:=\log\frac{T_0}{2\pi},
\qquad
\Delta:=\frac{4\pi}{\ell_0},
\tag{2}
\]

and suppose `m` distinct right-half-plane off-line zeta zeros have ordinates

\[
\gamma_j=T_0+j\Delta,
\qquad 1\le j\le m,
\tag{3}
\]

with their compulsory same-ordinate functional-equation mirrors. Let

\[
I=(T_0,T_0+m\Delta].
\tag{4}
\]

If `m=T^{\vartheta+o(1)}` with fixed `0<\vartheta<1/2`, Riemann--von Mangoldt gives the sharper local budget

\[
\boxed{N(I)-2m=O(\log T).}
\tag{5}
\]

Consequently any complementary screen entirely inside `I`, including critical-line labels, extra off-line pairs, and extra multiplicity, has

\[
\boxed{R=O(\log T).}
\tag{6}
\]

If that same-interval screen cancels the selected first reciprocal harmonic to error `\eta=o(1)` in the sense of WI-231, then (1) and (6) force

\[
\boxed{a_{\max}\ge \log m-\log\log T+O(1).}
\tag{7}
\]

In the WI-231 normalization this is a **macroscopic horizontal escalation**. Writing `L=\log T` and

\[
d_T=\frac{\Delta L}{2\pi}=\frac{2L}{\ell_0},
\qquad
a=\frac{(\beta-1/2)L}{d_T},
\tag{8}
\]

one has the exact conversion

\[
\beta-\frac12=\frac{2a}{\ell_0}.
\tag{9}
\]

Thus every such locally screened fixed-power bow requires at least one complementary off-line zero satisfying

\[
\boxed{
\beta_{\max}-\frac12
\ge
\frac{2}{\ell_0}\bigl(\log m-\log\log T+O(1)\bigr)
=2\vartheta-o(1).
}
\tag{10}
\]

For every fixed `\vartheta>1/4`, (10) eventually exceeds the width of the critical strip. Hence a local-density-matched symmetrized bow of exponent `\vartheta>1/4` **cannot be screened by zeros from its own vertical interval**. This closes the same-interval screen model on the whole fixed-power range above one quarter without using the exponent-pair reservoir of WI-202--WI-203.

At the exact quarter scale the classical Vinogradov--Korobov zero-free region also matters. If, for example,

\[
m=T^{1/4}(\log T)^{O(1)},
\tag{11}
\]

then (7)--(10) require

\[
\beta_{\max}\ge1-O\!\left(\frac{\log\log T}{\log T}\right).
\tag{12}
\]

The established zero-free region

\[
\beta
<1-rac{1}{55.241(\log |\gamma|)^{2/3}(\log\log |\gamma|)^{1/3}}
\tag{13}
\]

for sufficiently large ordinate is much wider than the `O(\log\log T/\log T)` gap in (12). Therefore the density-matched same-interval screen is impossible at the fixed-power endpoint `\vartheta=1/4` as well. The endpoint statement is deliberately made only at a precision such as (11); an arbitrary factor `T^{o(1)}` can move `\log m` by more than the zero-free width and is not silently covered.

This does **not** prove that a zeta bow cannot occur. The screen may be nonlocal in ordinate, the prime-side source may supply cancellation not representable by the local zero screen, or a bow may carry a spacing surplus above the local-density-matched value and thereby acquire a larger complementary zero-count budget. The result instead identifies a rigid extremal fact: once the vertical geometry consumes the local mean zero budget to `O(\log T)`, local screening has no count reservoir left and must convert almost the entire bow exponent into horizontal depth.

## 1. The refined Riemann--von Mangoldt budget

Write

\[
F(t):=\frac{t}{2\pi}\log\frac{t}{2\pi e}.
\tag{14}
\]

The classical zero-count formula, in the explicit modern form used already in WI-184, gives

\[
N(t)=F(t)+O(\log t).
\tag{15}
\]

Its derivatives are

\[
F'(t)=\frac1{2\pi}\log\frac{t}{2\pi},
\qquad
F''(t)=\frac1{2\pi t}.
\tag{16}
\]

With

\[
H:=m\Delta=\frac{4\pi m}{\ell_0},
\tag{17}
\]

Taylor's theorem on `T_0\le t\le T_0+H` gives, whenever `H=o(T)`,

\[
\begin{aligned}
F(T_0+H)-F(T_0)
&=H\frac{\ell_0}{2\pi}+O\!\left(\frac{H^2}{T}\right)\\
&=2m+O\!\left(\frac{m^2}{T\ell_0^2}\right).
\end{aligned}
\tag{18}
\]

Combining (15) and (18),

\[
\boxed{
N(I)
=2m+O\!\left(\log T+\frac{m^2}{T\ell_0^2}\right).
}
\tag{19}
\]

The selected bow contributes `m` right-half labels and `m` distinct functional-equation mirrors inside `I`, hence already `2m` labels counted with multiplicity. Define the excess local budget

\[
E_I:=N(I)-2m\ge0.
\tag{20}
\]

Every complementary label available to a same-interval screen, and every unit of extra multiplicity at a selected ordinate, must be charged to `E_I`. Thus

\[
R\le E_I.
\tag{21}
\]

For fixed `\vartheta<1/2`, `m=T^{\vartheta+o(1)}` implies

\[
\frac{m^2}{T\ell_0^2}=o(1),
\tag{22}
\]

so (19)--(21) prove (5)--(6).

The distinction from WI-184 is quantitative. Using the coarser unfolded coordinate based on `L=\log T` writes the same density-matched step as

\[
d_T=2+O(1/L).
\]

The statement `E_I=(d_T-2+o(1))m` from a leading-order count is therefore only `o(m)` and can hide an apparent `m/L` scale. Equation (18) retains the local density `\ell_0` before expanding it and shows that this apparent surplus cancels: at the density-matched spacing the true remaining count budget is only the `O(\log T)` zero-count error, throughout the fixed-power range relevant here.

## 2. Count saturation converts directly into horizontal depth

Assume the local screen satisfies the first-harmonic cancellation hypothesis of WI-231 with selected population `M=m` and error `\eta=o(1)`. Its exact inequality is

\[
R\cosh a_{\max}\ge(2-\eta)m.
\tag{23}
\]

If the cancellation holds then `R>0`. Equations (6) and (23) imply

\[
\cosh a_{\max}\gg \frac{m}{\log T}.
\tag{24}
\]

Since `\operatorname{arcosh}x=\log(2x)+O(x^{-2})`,

\[
a_{\max}
\ge
\log m-\log\log T+O(1),
\tag{25}
\]

which proves (7).

The exact conversion (9) follows from (8), not from an asymptotic replacement of the local density. Hence

\[
\beta_{\max}-\frac12
\ge
\frac{2\log m}{\ell_0}
-O\!\left(\frac{\log\log T}{\log T}\right).
\tag{26}
\]

For `T_0\asymp T`, `\ell_0=\log T+O(1)`. If `\log m=(\vartheta+o(1))\log T`, equation (26) is exactly (10).

For any fixed `\vartheta>1/4`, choose `\delta>0` with `2\vartheta>1/2+2\delta`. Then (26) gives `\beta_{\max}>1+\delta` for all sufficiently large `T`, impossible for a nontrivial zeta zero. Thus no local screen satisfying the stated hypotheses exists.

## 3. The quarter endpoint is inside the Vinogradov--Korobov zero-free region

At `m=T^{1/4}(\log T)^{O(1)}`, equation (26) gives

\[
1-\beta_{\max}
=O\!\left(\frac{\log\log T}{\log T}\right).
\tag{27}
\]

Mossinghoff, Trudgian and Yang prove the explicit Vinogradov--Korobov region

\[
\zeta(\sigma+it)\ne0
\quad\text{for}\quad
\sigma\ge
1-rac{1}{55.241(\log|t|)^{2/3}(\log\log|t|)^{1/3}},
\qquad |t|\ge3.
\tag{28}
\]

The ratio of the gap in (27) to the width in (28) is

\[
O\!\left(
\frac{(\log\log T)^{4/3}}{(\log T)^{1/3}}
\right)
\longrightarrow0.
\tag{29}
\]

So every zero satisfying the lower bound (27) would eventually lie inside the zero-free region. This proves the endpoint exclusion under the precision stated in (11).

The zero-free input is used only here. The fixed `\vartheta>1/4` exclusion is already an exact consequence of Riemann--von Mangoldt, functional-equation symmetry, and WI-231's first-harmonic tariff.

## 4. Near-density matching and the exact failure mode

The `O(\log T)` budget depends on matching the bow spacing to the local main density. This is not cosmetic. If the spacing is enlarged to

\[
\Delta_\varepsilon
=\frac{4\pi}{\ell_0}(1+\varepsilon_T),
\qquad \varepsilon_T\ge0,
\tag{30}
\]

then the same Taylor calculation gives

\[
N(I)-2m
=2\varepsilon_Tm
+O\!\left(\log T+\frac{m^2(1+\varepsilon_T)^2}{T\ell_0^2}\right).
\tag{31}
\]

Thus a spacing surplus creates a genuine local cancellation reservoir. In the fixed-power range `\vartheta<1/2`, a same-interval screen may now have

\[
R=O(\varepsilon_Tm+\log T).
\tag{32}
\]

Combining this with (23) yields the quantitative alternative

\[
\boxed{
\cosh a_{\max}
\gg
\frac{1}{\varepsilon_T+(\log T)/m}.
}
\tag{33}
\]

Hence the macroscopic depth (10) is forced only when the spacing surplus is small enough that the local count remains essentially saturated. For a fixed positive surplus, (33) forces only bounded radial depth and the present argument gives no contradiction. This is the exact escape route rather than an omitted error term.

Equation (33) is useful as an extremal diagnostic: a proposed near-count-saturating bow cannot simultaneously have a large spacing surplus, a shallow local screen, and first-harmonic cancellation. Any one of those features must pay for the other two.

## 5. Prior art and novelty audit

The external inputs are established and are kept separate from the repository deduction.

**Maynard--Pratt bow.** James Maynard and Kyle Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, IMRN 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, arXiv:2206.11729, Section 8, supply the schematic slowly varying arithmetic-progression bow that motivates this control. The present density matching is a Mathia stress test of that adversarial geometry; it is not attributed to their paper.

**Zero count.** Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, Journal of Number Theory 235 (2022), 219--241, DOI `10.1016/j.jnt.2021.06.032`, arXiv:2107.06506, prove the explicit bound

\[
\left|N(T)-F(T)\right|
\le0.1038\log T+0.2573\log\log T+9.3675,
\]

which is stronger than the `O(\log T)` form used in (15)--(19).

**Zero-free region.** Michael J. Mossinghoff, Timothy S. Trudgian and Andrew Yang, *Explicit zero-free regions for the Riemann zeta-function*, Research in Number Theory 10 (2024), article 11, DOI `10.1007/s40993-023-00498-y`, arXiv:2212.06867, prove the explicit region (28). Only its asymptotic Vinogradov--Korobov scale is needed.

The Taylor expansion of the Riemann--von Mangoldt main term and the insertion of WI-231 are elementary exact deductions. A bounded prior-art search around Maynard--Pratt's bow, local mean-density normalization, Riemann--von Mangoldt spacing, and zero-free regions located the sources above but no published statement coupling them into (5)--(10) or the same-interval quarter obstruction. Absence of a search hit is not evidence of priority, and no priority claim is made.

Within Mathia, WI-184 proves only the leading spacing gate `c\ge4\pi-o(1)` and the `o(m)` excess statement at asymptotic count saturation. WI-231 proves the general screen count--depth tariff and the strip exponent condition when an independent screen exponent is supplied. The new durable delta is the **second-order matching of the bow spacing to the local Riemann--von Mangoldt density**, which collapses the same-interval complementary budget from an unspecified `o(m)` to `O(\log T)` and therefore feeds WI-231 with a nearly zero screen exponent.

## 6. Boundary conditions, audit test, and consequence

The finding is deliberately local and conditional on the WI-231 screen interface. It does not establish that the full explicit-formula cancellation responsible for a zeta configuration is carried by zeros from `I`. Remote zeros can contribute to global form-factor amplitudes, and WI-195/ANF-102 leave a separate prime-side distinguished-twist covariance problem. Therefore this result must not be used as an RH proof or as a global zero-density theorem.

The selected bow is assumed to contain distinct right-half-plane off-line labels, with one compulsory mirror copy each. If a selected point is multiple, the extra multiplicity consumes the already small budget `E_I` and does not weaken the count conclusion. Critical-line zeros and all other labels in `I` are likewise charged to the same excess budget.

The fixed `\vartheta>1/4` contradiction can be audited by checking only three interfaces:

1. the local-density step `\Delta=4\pi/\ell_0` makes the derivative term in Riemann--von Mangoldt exactly `2m`;
2. the Taylor remainder plus the zero-count error is `O(\log T)` for every fixed `\vartheta<1/2`;
3. WI-231 equation (23) then gives `a_{\max}\ge\log m-\log\log T+O(1)`, and the exact normalization gives `\beta_{\max}-1/2=2a_{\max}/\ell_0`.

The endpoint additionally requires the Vinogradov--Korobov region and a bow-size precision strong enough that deviations of `\log m` from `(1/4)\log T` are no larger than the zero-free width. Removing that precision would be an invalid strengthening.

For the research program, this sharpens the geometry of the live simple-off-line complement. A count-saturating local bow cannot hide behind a large but shallow same-interval population: **its residual count reservoir is only logarithmic, so local cancellation forces one screen zero to move from the bow scale to real part `1/2+2\vartheta-o(1)`.** The remaining escape is now explicit: cancellation must become nonlocal/source-side, or the bow must open a genuine spacing/count surplus. This is a structural defect-to-depth implication, not a new simple-critical percentage.