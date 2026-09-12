# WI-256 — The next small-aperture remainder is a local translation-defect modulus

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-AUDITED`.

`WI-255` proves that the complete `O(r)` correction to the first-crossing sliding-aperture profile is universal: once the null equation `Q_W(v)=0` is imposed, the apparently arithmetic coefficient collapses to `psi(2)-log(4pi)`. A natural next attempt is to continue the expansion to order `r^2` and compare it with Suzuki's small-window eigenvalue asymptotic. That continuation is **not justified by the regularity currently available for the first global zero mode**.

More precisely, the exact remainder after the `WI-255` terms splits into a universal quadratic term and a nonnegative local translation-defect modulus. The latter can be larger than `r^2` under `H^log` regularity, and even generic membership in Suzuki's operator domain does not determine its quadratic coefficient. Therefore an `r^2` bootstrap must first extract extra translation regularity from the actual zero-mode equation `A_{a_*}v=0`; it cannot be obtained by Taylor-expanding the existing profile under the form-domain or operator-domain hypotheses alone.

Assume RH is false and let `a_*`, the normalized first global zero mode `v`, and

\[
C(h)=\operatorname{Re}\int_{\mathbb R}v(x+h)\overline{v(x)}\,dx,
\qquad \|v\|_2=1,
\]

be as in `WI-253`--`WI-255`. Put

\[
\delta(h):=1-C(h)=\frac12\|\tau_hv-v\|_2^2\ge0,
\qquad H:=2a_*.
\]

Then for `0<r<min(a_*,(log 2)/2)`, the exact aperture profile satisfies

\[
\boxed{
\mathcal F_v(r)
=r\log(1/r)
+r\bigl(\psi(2)-\log(4\pi)\bigr)
+E_v(r)+\frac72r^2+o(r^2),
}
\tag{1}
\]

where

\[
\boxed{
E_v(r)
:=\int_0^{2r}\left(\frac rh-\frac12\right)\delta(h)\,dh
=r\int_0^{2r}\frac{1-C(h)}h\,dh
-\frac12\int_0^{2r}(1-C(h))\,dh
\ge0.
}
\tag{2}
\]

The formula does **not** assert that `E_v(r)=O(r^2)` for the actual zero mode. It identifies that estimate as the missing regularity theorem.

## 1. Exact decomposition of the next remainder

Retain the `WI-255` notation

\[
w(h)=\frac{e^{-5h/2}}{1-e^{-2h}}-e^{h/2}
=\frac1{2h}+q(h).
\]

The regular part extends continuously to zero, and direct expansion gives

\[
q(0)=-\frac74.
\tag{3}
\]

For `r<(log2)/2`, all prime-power atoms are still on the linear branch of the aperture. If `P_v` denotes the same finite prime coefficient as in `WI-255`, its exact profile identity is

\[
\mathcal F_v(r)
=2rP_v
+\frac12\int_0^{2r}C(h)\,dh
+r\int_{2r}^{H}\frac{C(h)}h\,dh
+2r\int_0^Hq(h)C(h)\,dh
+\int_0^{2r}(h-2r)q(h)C(h)\,dh.
\tag{4}
\]

Write

\[
I_v:=\int_0^H\frac{C(h)-1}{h}\,dh,
\]

which is finite by the `H^log` form-domain identity proved in `WI-255`. The singular two integrals in (4) give exactly

\[
\begin{aligned}
\frac12\int_0^{2r}C(h)\,dh
+r\int_{2r}^{H}\frac{C(h)}h\,dh
={}&r+r\log\frac{H}{2r}+rI_v+E_v(r).
\end{aligned}
\tag{5}
\]

Thus every departure from the `WI-255` linear coefficient coming from the singular kernel is concentrated in the nonnegative quantity (2).

For the remaining short-interval regular term, `L^2` translation continuity gives `C(h)->1`, while `q(h)->-7/4`. Hence

\[
\begin{aligned}
\int_0^{2r}(h-2r)q(h)C(h)\,dh
&=-\frac74\int_0^{2r}(h-2r)\,dh+o(r^2)\\
&=\frac72r^2+o(r^2).
\end{aligned}
\tag{6}
\]

All other terms in (4) are exactly the linear coefficient already simplified in `WI-255`; applying the zero-mode identity `Q_W(v)=0` again gives `psi(2)-log(4pi)`. Equations (5)--(6) prove (1).

The decomposition is useful because it separates two very different effects. The coefficient `7/2` is a local Taylor coefficient of the regular archimedean kernel and is universal. `E_v(r)` is instead an autocorrelation regularity modulus of the particular mode and has no universal quadratic size under the hypotheses used so far.

## 2. `H^log` alone permits nonquadratic translation defects

The form-domain inclusion used in `WI-255` is logarithmic rather than Sobolev. It is enough to make `int_0^H delta(h)/h dh` finite, but that does not imply `delta(h)=O(h)` or `O(h^2)`.

A concrete family makes the obstruction explicit. For `0<beta<1/2`, let

\[
v_\beta(x)=\sqrt{1-2\beta}\,x^{-\beta}\mathbf 1_{(0,1)}(x),
\]

extended by zero. It is normalized in `L^2`. For `h->0+`, splitting the translation norm into the new-support interval, the overlap, and the far endpoint and scaling `x=hy` on the overlap gives

\[
\|\tau_hv_\beta-v_\beta\|_2^2
\sim K_\beta h^{1-2\beta},
\qquad K_\beta>0.
\tag{7}
\]

Indeed, the new-support piece contributes `(1-2beta) h^(1-2beta)/(1-2beta)`, the scaled overlap converges to a finite positive integral

\[
(1-2\beta)\int_0^\infty
\bigl((y+1)^{-\beta}-y^{-\beta}\bigr)^2\,dy,
\]

and the opposite endpoint is only `O(h)`. Meanwhile

\[
|\widehat v_\beta(\xi)|=O(|\xi|^{\beta-1})
\qquad(|\xi|\to\infty),
\]

because the rescaled oscillatory integral `int_0^{|xi|} u^{-beta} e^{-iu}du` is uniformly bounded. Since `2beta-2<-1`,

\[
\int_{\mathbb R}\log(2+|\xi|)|\widehat v_\beta(\xi)|^2\,d\xi<\infty.
\]

Thus these vectors belong to the ambient logarithmic Fourier class controlled by Suzuki's form-domain estimate. This does **not** claim that they lie in the actual localized Weil form domain; it shows only that the `H^log` inclusion by itself cannot furnish the missing quadratic modulus.

More generally, if locally

\[
\delta(h)\sim c h^\alpha,\qquad \alpha>0,
\]

then (2) gives

\[
\boxed{
E_v(r)\sim
\frac{2^\alpha c}{\alpha(\alpha+1)}r^{1+\alpha}.
}
\tag{8}
\]

For every `0<alpha<1`, this term lies strictly between the linear and quadratic scales and dominates the universal `7r^2/2` term.

## 3. Generic membership in `D(A_a)` still does not determine the quadratic coefficient

Suzuki's operator-domain theorem is stronger than the form-domain embedding, but generic membership in `D(A_a)` is still insufficient for a universal second-order profile.

Suzuki explicitly notes that the normalized constant

\[
v_{\mathrm{const}}(x)=(2a)^{-1/2}\mathbf 1_{(-a,a)}(x)
\]

belongs to `D(A_a)` even though `D(A_a)` is strictly larger than `H_0^1(-a,a)`. Its zero-extension autocorrelation is

\[
C(h)=1-\frac{h}{2a}\qquad(0<h<2a),
\]

so (2) gives the exact value

\[
\boxed{E_{v_{\mathrm{const}}}(r)=\frac{r^2}{2a}}
\qquad(0<r<a).
\tag{9}
\]

By contrast, any normalized `phi in C_c^infty(-a,a)` lies in the symmetric operator domain `D(B_a)=H_0^1(-a,a)` and hence in the Friedrichs extension domain `D(A_a)`. Its translation defect is `delta(h)=O(h^2)`, so

\[
E_\phi(r)=O(r^3).
\tag{10}
\]

Therefore even the operator domain contains vectors whose `E_v` contributes different quadratic coefficients. What distinguishes the hypothetical first-crossing vector is not merely `v in D(A_{a_*})`, but the additional equation

\[
A_{a_*}v=0.
\tag{11}
\]

Any valid second-order bootstrap must use (11), or an equivalent zero-mode-specific consequence, to prove a sharper translation modulus.

## 4. Consequence for the sliding-aperture program

This closes the tempting continuation

\[
\text{`WI-255` first-order expansion}
\;\Longrightarrow\;
\text{universal second-order coefficient from generic regularity}.
\]

The exact obstruction is now visible rather than hidden in an `o(r)` term. Before comparing second-order coefficients with Suzuki's `lambda_r`, one must control `E_v(r)` for the **actual zero mode**. A theorem such as `E_v(r)=o(r^2)`, or even an exact asymptotic `E_v(r)=c_*r^2+o(r^2)` with source-sensitive `c_*`, would be genuine new information and could reopen the small-aperture route. Neither `H^log` membership nor generic `D(A_a)` membership supplies it.

This is a decisive negative result for one proposed refinement, not a negative result for the full sliding-symbol clue. The credible next targets are now sharper: derive zero-mode-specific translation/boundary regularity directly from `A_{a_*}v=0`; otherwise move to medium radii where prime thresholds separate, or use the full operator equation rather than its scalar null form.

## 5. Evidence boundary and prior-art audit

Primary source: Masatoshi Suzuki, **Weil's quadratic form via the screw function**, arXiv:2606.09096v2 (revised 17 Aug 2026), especially the localized Friedrichs operator/domain construction, the logarithmic form-domain analysis, and Theorem 1.4: https://arxiv.org/abs/2606.09096. Suzuki proves the operator/form facts consumed above; he does not state (1)--(2) or this small-aperture obstruction.

The identities `1-C(h)=||tau_hv-v||_2^2/2` and continuity of translations in `L^2` are classical. The power-law examples above are used only as regularity countermodels and are not asserted to solve Suzuki's zero-mode equation. A targeted prior-art search around Suzuki's localized Weil operator, sliding autocorrelation/aperture expansions, logarithmic Fourier regularity, and second-order translation defects did not locate a source stating the decomposition (1)--(2) or resolving the zero-mode-specific modulus. Search absence is audit context only and is not a priority claim.

No numerical zeta-zero evidence, unproved RH input, or conjectural pair correlation enters the deduction. The result neither changes the established simple-critical-zero proportion nor constrains an actual off-line zero directly; it narrows the first-crossing defect-elimination program by identifying the exact missing regularity quantity.