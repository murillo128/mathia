# XF-095 — dynamic xi-log-squared corrector makes the reference defect guarded-small

**Status:** `EXACT-DERIVED` + `DYNAMIC-REFERENCE-CORRECTION` + `GUARDED-SOURCE-CLOSURE` + `STRUCTURAL/BRIDGE`. XF-090 shows that the Polymath high-line reference has a deterministic positive-time heat defect

\[
\mathcal D_t(\xi)
=\frac{t}{16}\,\xi\bigl(\log\xi+C_0\bigr)^2+O_t(\xi),
\qquad
C_0:=\gamma+\log(4\pi),
\tag{1}
\]

whose raw guarded resource grows like `(log q)^4`, while XF-094 shows that at `t=0` the Xi-specific residual starts with the deterministic linear term `-xi/3` and becomes source-small after subtracting it. The open question was whether that linear correction can be transported through positive heat time without reintroducing the XF-090 source floor.

It cannot remain a smooth linear correction. The reference forcing integrates into a **universal dynamic `xi log^2 xi` cusp in the residual**. More precisely, for the XF-089 residual

\[
\mathcal R_t:=\mathcal Z_t-\mathcal Z_t^M
\tag{2}
\]

there is a deterministic continuous scalar `beta(t)`, with `beta(0)=-1/3`, such that uniformly for `0<=t<=1/2`,

\[
\boxed{
\mathcal R_t(\xi)
=
\xi\left[
-\frac{t^2}{32}\bigl(\log\xi+C_0\bigr)^2
+\beta(t)
\right]
+O\!\left(\xi^2(1+|\log\xi|)^3\right),
\qquad \xi\downarrow0.
}
\tag{3}
\]

The finite scalar `beta(t)` is explicit in terms of the already-explicit Polymath defect. If

\[
d(t):=
\lim_{\xi\downarrow0}
\left[
\frac{\mathcal D_t(\xi)}{\xi}
-\frac{t}{16}(\log\xi+C_0)^2
\right],
\tag{4}
\]

then

\[
\boxed{
\beta(t)=-\frac13-\int_0^t d(s)\,ds.
}
\tag{5}
\]

Consequently the deterministic endpoint corrector

\[
\boxed{
\mathcal C_t(\xi)
=
\xi\left[
-\frac{t^2}{32}(\log\xi+C_0)^2+\beta(t)
\right]
}
\tag{6}
\]

(on a fixed cutoff below the first prime frequency) simultaneously does two things: the corrected Xi residual is `O(xi^2 log^3 xi)`, and the corrected reference itself has only an `O(xi^2 log^3 xi)` heat defect. Both are therefore `o(1)` in the exact XF-086 guarded resource on the canonical Xi source band.

Thus the large deterministic forcing discovered in XF-090 is not a permanent obstruction. It is the derivative of a forced endpoint jet. The price is structural: **any dynamic reference correction with bounded `C_t(xi)/xi` is insufficient at every fixed positive time.** The required reference is necessarily non-`C^1` at the spectral endpoint and must contain the coefficient `-t^2/32` of `xi(log xi+C_0)^2`.

This closes the deterministic positive-time source-floor gate left by XF-090/XF-094 at the continuum point-sample level. It does **not** close XF-093: extracting the corrected Xi-specific residual from high-line quotient control still requires mesh-scale Fourier regularity or a stable alternative discretization. The separate positive-`Lambda` destination coercivity gate also remains open.

## 1. The XF-090 forcing has a finite linear part after its logarithmic cusp

Keep the XF-090 notation on a fixed high line `3<a<4`:

\[
b=1+a,
\qquad
w=b-ix,
\qquad
\ell(x)=\Log\frac{w}{4\pi}.
\tag{7}
\]

XF-090 proves the exact decomposition

\[
\mathfrak e_t(s_a(x))
=
-\frac1{4w}
-\frac{t}{16}\frac{\ell(x)^2}{w}
+r_t(x),
\tag{8}
\]

with

\[
|r_t(x)|
\ll_a
\frac{\log^2(2+|x|)}{1+x^2}
\tag{9}
\]

uniformly for `0<=t<=1/2`. The tail in `(9)` is integrable, but it gives more than continuity of its Fourier transform at zero. For `0<xi<=1/2`, split at `|x|=xi^{-1}` and use `|e^{-ixi x}-1|<=min(2,xi|x|)`:

\[
\begin{aligned}
|\widehat r_t(\xi)-\widehat r_t(0)|
&\le
\xi\int_{|x|\le\xi^{-1}}|x r_t(x)|\,dx
+2\int_{|x|>\xi^{-1}}|r_t(x)|\,dx\\
&\ll_a
\xi(1+|\log\xi|)^3.
\end{aligned}
\tag{10}
\]

Insert `(8)` into the exact XF-090 transform

\[
\mathcal D_t(\xi)
=-\frac{\xi}{2\pi}e^{a\xi}
\widehat{\mathfrak e_t(s_a(\cdot))}(\xi).
\tag{11}
\]

Using the two singular transforms already evaluated there gives

\[
\mathcal D_t(\xi)
=
\frac{\xi}{4}e^{-\xi}
+\frac{t\xi}{16}e^{-\xi}
\left[(\log\xi+C_0)^2-\frac{\pi^2}{6}\right]
-\frac{\xi}{2\pi}e^{a\xi}\widehat r_t(\xi).
\tag{12}
\]

Therefore the limit in `(4)` exists, is continuous in `t`, and one may write it explicitly as

\[
\boxed{
d(t)
=
\frac14-rac{t\pi^2}{96}
-\frac1{2\pi}\widehat r_t(0).
}
\tag{13}
\]

More importantly, `(10)` sharpens XF-090 from an unspecified `O_t(xi)` remainder to

\[
\boxed{
\mathcal D_t(\xi)
=
\xi\left[
\frac{t}{16}(\log\xi+C_0)^2+d(t)
\right]
+O_a\!\left(\xi^2(1+|\log\xi|)^3\right).
}
\tag{14}
\]

No new external input is used: `(14)` is only the quantitative Fourier modulus forced by the `x^{-2} log^2 x` remainder already present in XF-090.

## 2. The residual equation integrates the forcing into a universal dynamic cusp

The exact XF-090 residual equation is

\[
\partial_t\mathcal R_t
=
\xi^2\mathcal R_t
-\xi\left(
2\mathcal Z_t^M*\mathcal R_t
+\mathcal R_t*\mathcal R_t
\right)
-\mathcal D_t.
\tag{15}
\]

XF-092 gives the endpoint structure

\[
\mathcal Z_t^M
=-\frac1{4\xi}-\frac t8\log\xi+O_a(1+\xi|\log\xi|)
\tag{16}
\]

on the open positive half-line, with the pole interpreted in the same finite-part normalization as XF-088/XF-091. XF-094 gives the exact initial residual

\[
\mathcal R_0(\xi)
=-\frac\xi3+\frac{\xi^2}{3}+O(\xi^3).
\tag{17}
\]

The nonlinear terms in `(15)` are one full endpoint degree smaller than the forcing. To see this quantitatively, suppose on a compact heat interval that

\[
|R(\xi)|+\xi|R'(\xi)|
\ll \xi(1+|\log\xi|)^2.
\tag{18}
\]

For the pole piece, the exact XF-091 finite-part identity

\[
(\tau*R)(\xi)
=R(\xi)(\log\xi+\gamma)
+\int_0^\xi\frac{R(\xi-\eta)-R(\xi)}\eta\,d\eta
\tag{19}
\]

gives

\[
\tau*R
=O\!\left(\xi(1+|\log\xi|)^3\right).
\tag{20}
\]

The logarithmic, bounded, and zero-frequency pieces of `Z_t^M` are no worse, so

\[
\mathcal Z_t^M*R
=O\!\left(\xi(1+|\log\xi|)^3\right),
\qquad
R*R=O\!\left(\xi^3(1+|\log\xi|)^4\right).
\tag{21}
\]

Hence

\[
\xi^2R
-\xi\left(2\mathcal Z_t^M*R+R*R\right)
=O\!\left(\xi^2(1+|\log\xi|)^3\right).
\tag{22}
\]

Starting from `(17)`, equations `(14)`--`(15)` close the weighted `C^1` bootstrap `(18)` uniformly on `0<=t<=1/2`. Integrating `(15)` in `t` and using `(14)` and `(22)` then yields

\[
\begin{aligned}
\mathcal R_t(\xi)
&=
-\frac\xi3
-\int_0^t
\xi\left[
\frac{s}{16}(\log\xi+C_0)^2+d(s)
\right]ds\\
&\qquad
+O_a\!\left(\xi^2(1+|\log\xi|)^3\right),
\end{aligned}
\tag{23}
\]

which is exactly `(3)`--`(5)`.

Two sign/factor checks are immediate. Differentiating the new coefficient `-t^2/32` gives `-t/16`, the negative of the XF-090 forcing coefficient as required by `(15)`. At `t=0`, `(3)` reduces to `R_0=-xi/3+O(xi^2)`, exactly the XF-094 coefficient.

## 3. The dynamic corrector makes both the state and the reference defect source-small

Choose a fixed `xi_*` with `0<2xi_*<lambda_2=(log 2)/2`, and a smooth cutoff `kappa` equal to one on `[0,xi_*]` and supported below `2xi_*`. Define

\[
\mathcal C_t(\xi)
:=
\kappa(\xi)\,
\xi\left[
-\frac{t^2}{32}(\log\xi+C_0)^2+\beta(t)
\right]
\tag{24}
\]

and the dynamically corrected deterministic reference

\[
\mathcal Z_t^{M,\sharp}:=
\mathcal Z_t^M+\mathcal C_t.
\tag{25}
\]

Because `K Delta ->0`, every canonical source frequency eventually lies where `kappa=1`; Volterra triangularity also means that the cutoff region cannot feed back into smaller target frequencies. Equation `(3)` gives the corrected Xi-specific residual

\[
\boxed{
\mathcal R_t^\sharp
:=
\mathcal Z_t-\mathcal Z_t^{M,\sharp}
=O_a\!\left(\xi^2(1+|\log\xi|)^3\right)
}
\tag{26}
\]

uniformly for `0<=t<=1/2` on the live endpoint band.

There is a second cancellation. Write the heat defect of the corrected reference in Volterra form as

\[
\partial_t\mathcal Z_t^{M,\sharp}
=
\xi^2\mathcal Z_t^{M,\sharp}
-\xi(\mathcal Z_t^{M,\sharp}*\mathcal Z_t^{M,\sharp})
+\mathcal D_t^\sharp.
\tag{27}
\]

From XF-090 and `(25)`,

\[
\mathcal D_t^\sharp
=
\mathcal D_t
+\partial_t\mathcal C_t
-\xi^2\mathcal C_t
+\xi\left(
2\mathcal Z_t^M*\mathcal C_t
+\mathcal C_t*\mathcal C_t
\right).
\tag{28}
\]

On `0<xi<=xi_*`, equations `(5)`, `(14)`, and `(24)` give the exact leading cancellation

\[
\mathcal D_t+\partial_t\mathcal C_t
=O_a\!\left(\xi^2(1+|\log\xi|)^3\right),
\tag{29}
\]

while the remaining terms in `(28)` have the same or smaller order by `(20)`--`(22)`. Therefore

\[
\boxed{
\mathcal D_t^\sharp(\xi)
=O_a\!\left(\xi^2(1+|\log\xi|)^3\right).
}
\tag{30}
\]

So the dynamic correction does not merely make the state residual small; it removes the nonperturbative deterministic **vector-field** mismatch that XF-090 found. The large `(log q)^4` reference forcing has been reduced to the same endpoint degree as the already-source-small XF-094 residual.

## 4. Both corrected quantities vanish in the exact guarded resource

Use the XF-086 resource

\[
\mathcal R_{[J,K]}(Q)
=
\frac1{4M^2}
\sum_{m=J}^K I_m|Q_m|^2,
\qquad
I_m=\int_{-1}^1(\pi m+u)^4|\chi(u)|^2\,du.
\tag{31}
\]

For the fixed selector window, `I_m \ll_g m^4`. On the canonical mesh `xi_m=m Delta`, equations `(26)` and `(30)` imply, for either `Q_m=R_t^sharp(xi_m)` or `Q_m=D_t^sharp(xi_m)`,

\[
\begin{aligned}
\mathcal R_{[J,K]}(Q)
&\ll_a
\frac{\Delta^4}{M^2}
\sum_{m=J}^K
m^8(1+|\log(m\Delta)|)^6\\
&\ll_a
\frac{\Delta^4K^9}{M^2}
(1+|\log\Delta|+\log K)^6.
\end{aligned}
\tag{32}
\]

With the XF-071 scales

\[
M=q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
K\asymp q\log\log T,
\tag{33}
\]

this becomes

\[
\boxed{
\mathcal R_{[J,K]}(Q)
\ll_a
q^{-1}(\log\log T)^9
(1+\log q+\log\log\log T)^6
=o(1)
}
\tag{34}
\]

in the same asymptotic regime already used by XF-071/XF-088--XF-094. Thus the deterministic positive-time source floor is gone at exactly the norm required by the equal-weight realization and guarded Vieta transport.

The cutoff in `(24)` changes neither `(32)` nor the positive-frequency endpoint convolution on the live band: for target `xi<xi_*`, every Volterra integration variable also lies below `xi_*`, where `kappa=1`.

## 5. A smooth linear dynamic correction provably cannot work

The `xi log^2 xi` term is not optional. Fix `t_0>0`. Let `G_t` be any deterministic correction satisfying

\[
\sup_{0<\xi<\xi_*}\frac{|G_t(\xi)|}{\xi}<\infty
\tag{35}
\]

uniformly for `t_0<=t<=1/2`. This includes every endpoint-`C^1` correction and every purely time-dependent linear correction `b(t)xi`. From `(3)`,

\[
\mathcal R_t(\xi)-G_t(\xi)
=
-\frac{t^2}{32}\xi(\log\xi+C_0)^2
+O_t(\xi).
\tag{36}
\]

On the canonical block `q<=m<=2q`, one has `xi_m\asymp q^{-1/2}` and

\[
|\log\xi_m+C_0|
=\frac12\log q+O(1).
\tag{37}
\]

The exact XF-086 weights are bounded above and below by positive multiples of `m^4/M^2` on this block. Therefore `(36)` gives

\[
\boxed{
\mathcal R_{[q,2q]}(\mathcal R_t-G_t)
\asymp_{a,g,t_0}
(\log q)^4.
}
\tag{38}
\]

Thus XF-094's `-xi/3` is the correct **initial** normalization but cannot be frozen, or even replaced by another smooth linear coefficient, at positive time. Any successful deterministic dynamic reference must reproduce the endpoint cusp in `(6)` with the exact coefficient `-t^2/32`; after that, the finite scalar `beta(t)` must also be matched to remove the residual order-`xi` resource floor.

## 6. Stress tests and falsification boundary

The result is insensitive to root reality and collisions because it uses only the zero-free high-line carrier and the exact distributional Volterra equation. The first-prime cutoff is used only to keep the deterministic corrector in the source endpoint sector; no prime or zero statistic enters the derivation.

The strongest possible failure mode would be a missing order-`xi` contribution from the nonlinear residual terms. Equation `(19)` rules this out: the singular pole convolution of an `xi log^2 xi` residual is only `xi log^3 xi`, and the Volterra prefactor supplies another factor of `xi`. Zero-frequency delta pieces of the reference give `O(xi log^2 xi)` before that prefactor and are therefore also one degree lower. This is why the coefficient `-t^2/32` is forced solely by XF-090's deterministic defect.

The finding does **not** claim that `(26)` can already be read from fixed-strip quotient approximation. XF-093 gives an explicit narrow-spike counterexample to that implication. A separate Xi-specific mesh-scale `H^1`/bandwidth estimate, or a discretization stable under the available quotient norm, is still required before `(34)` becomes an extracted periodic moment statement. Nor does source smallness itself show that `Lambda>0` produces a nonzero destination resource.

## 7. Prior-art boundary and consequence

The literature audit again recovers the Polymath15 heat-flow approximation as the load-bearing external source for `M_t`, and the classical Burgers/Cole--Hopf framework as the neighboring transport class already recorded in this line. No source found states the Xi-specific residual jet `(3)`, the necessary dynamic coefficient `-t^2/32`, or the guarded-resource cancellation `(30)`--`(34)`. No new literature claim is load-bearing here, so `SOURCES.md` does not change.

The source-side frontier is now narrower. The deterministic Polymath defect, including its positive-time `xi log^2 xi` cusp, can be absorbed into a single explicit endpoint jet whose corrected state and corrected vector-field defect are both `o(1)` in the destination-matched guarded resource. The remaining source obstruction is no longer a deterministic positive-time floor; it is **sampling the corrected Xi-specific quotient residual at the Volterra mesh scale** as isolated by XF-093. After that, XF-085--XF-087 provide the static equal-weight realization and exact periodic transport, while positive-transition destination coercivity remains a separate final gate.
