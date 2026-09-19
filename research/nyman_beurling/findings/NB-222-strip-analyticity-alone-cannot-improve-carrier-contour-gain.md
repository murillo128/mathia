# NB-222 — Strip analyticity alone cannot improve the carrier contour gain

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + SHARP-METHOD-BOUNDARY + CARRIER-MATCHED-EXTREMIZER + STRIP-ANALYTICITY + VINOGRADOV-KOROBOV-INTERFACE + NB-221-REFINEMENT`.

`NB-221` reduced every fixed-depth soft zeta-primitive route to the same transported local logarithmic-derivative carrier. After a safe Vinogradov--Korobov contour displacement `eta`, the surviving term has the form

\[
e^{-X\eta}
\int
 e^{iXv}
 \Phi_\eta(v)
 w_V(v+i\eta)
 P_0(\sigma_X-\eta+i(t+v))\,dv,
\qquad
P_0=-\frac{\zeta'}{\zeta},
\]

and the existing proof loses the possible signed cancellation by replacing the last factor by its pointwise bound `O(Q^2)`. The live question was whether the rapid carrier `e^(iXv)`, together with analyticity in the same zero-free strip, could itself force an additional saving before arithmetic information about `P_0` is used.

It cannot. For the exact moving-shell kernel and the same flat Gaussian windows used in `NB-220`--`NB-221`, the contour-shift estimate

\[
\boxed{
|\mathcal T_{X,V}(F)|
\ll
M e^{-X\eta}
}
\]

is sharp, up to constants, over the class of functions holomorphic and bounded by `M` in the strip of height `eta`. A carrier-matched exponential realizes the lower bound. Moreover that extremizer obeys the full Cauchy-scale derivative envelope on the lower edge, so finite integration by parts or derivative estimates obtained only from strip analyticity cannot remove the loss either.

Consequently the `Q^2` pointwise tariff in `NB-221` cannot be improved by a theorem whose only inputs are the local zero-free strip, a uniform bound for `-zeta'/zeta`, and generic holomorphic regularity. Any improvement must use information that distinguishes the actual logarithmic derivative from an arbitrary bounded analytic function: its Euler/Dirichlet spectral amplitudes, zero structure, frequency-localized norms, or another genuinely arithmetic constraint. This is a method boundary, not a new bound for the actual Nyman source.

## 1. The moving-shell functional and its strip class

Fix `Delta>0`, a nonzero profile

\[
\phi\in C_c^\infty((0,\Delta);\mathbb C),
\]

and the shell transform used in `NB-221`,

\[
L_X(z)
:=
\int_0^\Delta
\phi(u)e^{iz(X+u)}\,du.
\tag{1}
\]

Thus

\[
L_X(z)=e^{iXz}\Phi(z),
\qquad
\Phi(z):=\int_0^\Delta\phi(u)e^{izu}\,du.
\tag{2}
\]

For a fixed integer `M_0>=0`, let

\[
W_{M_0}(z)
:=
e^{-z^2}\sum_{\ell=0}^{M_0}\frac{z^{2\ell}}{\ell!},
\qquad
w_V(z):=W_{M_0}(z/V),
\tag{3}
\]

exactly as in `NB-220`--`NB-221`. On the real axis,

\[
0<w_V(v)\le1,
\tag{4}
\]

and on every fixed horizontal strip the family `w_V`, `V>=1`, has Gaussian real-axis decay multiplied by a uniformly controlled polynomial factor.

For `0<eta<=1`, write

\[
\mathcal S_\eta
:=
\{z\in\mathbb C:0\le\operatorname{Im}z\le\eta\}.
\tag{5}
\]

Let `H^infinity(S_eta)` denote functions holomorphic in the interior, continuous on the closure, and bounded there. For such an `F`, define

\[
\mathcal T_{X,V}(F)
:=
\frac1{2\pi}
\int_{\mathbb R}
 w_V(v)L_X(v)F(v)\,dv.
\tag{6}
\]

The integral is absolutely convergent because `L_X(v)=e^(iXv) Phi(v)` and `Phi` is Schwartz on the real axis. The dependence on `X` is therefore entirely in the unimodular carrier before contour displacement.

The class in (5)--(6) is exactly the generic analytic information supplied by a local zero-free rectangle after the zeta-specific step has been forgotten: holomorphy in a strip and a pointwise envelope.

## 2. Generic strip transport gives the `exp(-X eta)` upper bound

Let

\[
\|F\|_{H^\infty(\mathcal S_\eta)}\le M.
\tag{7}
\]

Because `w_V` and `L_X` are entire and `F` is holomorphic in the strip, move the real contour to `Im(z)=eta`. The vertical sides vanish as their real parts tend to infinity: after removing `e^(iXz)`, the transform `Phi(z)` is uniformly Schwartz for `0<=Im(z)<=1`, while the Gaussian window gives at least as much decay.

Hence

\[
\mathcal T_{X,V}(F)
=
\frac1{2\pi}
\int_{\mathbb R}
 w_V(v+i\eta)
 L_X(v+i\eta)
 F(v+i\eta)\,dv.
\tag{8}
\]

From (1),

\[
\begin{aligned}
L_X(v+i\eta)
&=
 e^{-X\eta}e^{iXv}
 \Phi_\eta(v),\\
\Phi_\eta(v)
&:=
\int_0^\Delta
\phi(u)e^{-\eta u}e^{ivu}\,du.
\end{aligned}
\tag{9}
\]

The family `Phi_eta`, `0<=eta<=1`, is uniformly Schwartz. For fixed `M_0`,

\[
\sup_{\substack{0<\eta\le1\\V\ge1}}
\int_{\mathbb R}
|w_V(v+i\eta)\Phi_\eta(v)|\,dv
<\infty.
\tag{10}
\]

Therefore there is a constant `C=C(phi,M_0)` such that

\[
\boxed{
|\mathcal T_{X,V}(F)|
\le
C M e^{-X\eta}
}
\tag{11}
\]

for every `X>=1`, `0<eta<=1`, and `V>=1`.

This is precisely the generic contour-shift mechanism behind equation (35) of `NB-221`, stripped of the zeta-specific notation.

## 3. A carrier-matched bounded analytic function saturates the bound

Choose one point

\[
u_0\in(0,\Delta)
\qquad\text{with}\qquad
\phi(u_0)\ne0.
\tag{12}
\]

For given `X`, `eta`, and amplitude `M>0`, define

\[
F_{X,\eta}(z)
:=
M e^{-(X+u_0)\eta}
 e^{-i(X+u_0)z}.
\tag{13}
\]

If `z=v+iy` with `0<=y<=eta`, then

\[
|F_{X,\eta}(v+iy)|
=
M e^{-(X+u_0)(\eta-y)}
\le M.
\tag{14}
\]

Thus `F_(X,eta)` is entire and belongs to the unit strip class (7) after normalization by `M`.

Substitution into (6) cancels the moving carrier exactly:

\[
\begin{aligned}
\mathcal T_{X,V}(F_{X,\eta})
&=
M e^{-(X+u_0)\eta}
\frac1{2\pi}
\int_{\mathbb R}
 w_V(v)
\left[
\int_0^\Delta
\phi(u)e^{iv(u-u_0)}\,du
\right]dv.
\end{aligned}
\tag{15}
\]

For `w_V=1`, Fourier inversion makes the last factor exactly `phi(u_0)`. For the flat Gaussian window, `w_V(v)->1` pointwise as `V->infinity`, while `0<w_V(v)<=1` on the real axis and the bracketed Fourier transform is Schwartz. Dominated convergence therefore gives

\[
\frac1{2\pi}
\int_{\mathbb R}
 w_V(v)
\left[
\int_0^\Delta
\phi(u)e^{iv(u-u_0)}\,du
\right]dv
\longrightarrow
\phi(u_0).
\tag{16}
\]

Hence there is `V_0=V_0(phi,M_0)` and a constant `c>0` such that for every `V>=V_0`,

\[
\left|
\mathcal T_{X,V}(F_{X,\eta})
\right|
\ge
c M e^{-(X+u_0)\eta}.
\tag{17}
\]

Since `0<u_0<Delta` and `0<eta<=1`,

\[
e^{-u_0\eta}\ge e^{-\Delta}.
\tag{18}
\]

Combining (11) and (17),

\[
\boxed{
 c_\phi M e^{-X\eta}
\le
\sup_{\|F\|_{H^\infty(\mathcal S_\eta)}\le M}
|\mathcal T_{X,V}(F)|
\le
C_\phi M e^{-X\eta}
}
\tag{19}
\]

for every sufficiently large `V`, uniformly in `X>=1` and `0<eta<=1`.

Thus the contour-shift factor is not merely an artifact of taking absolute values after transport. It is the correct operator-norm scale on the full bounded-analytic strip class.

The finite-height geometry of `NB-221` does not alter this conclusion. If (6) is truncated to `|v|<=T`, the omitted contribution in the lower-bound construction is bounded by a Schwartz tail of `Phi`, uniformly in `X`, `eta`, and `V` on the real axis. Therefore (19) remains valid, with a smaller constant, once `T>=T_0(phi)`. In `NB-221`, `T=|t|/2`, so this requirement is automatic at high ordinate.

## 4. Cauchy-scale derivative information does not rescue integration by parts

A natural response to (19) is to retain analyticity but use derivatives of `F` rather than only its supremum, hoping that repeated integration by parts against `e^(iXv)` produces inverse powers of `X`.

The same extremizer defeats every derivative bound that follows generically from the strip width. On the lower edge,

\[
\left|
F_{X,\eta}^{(m)}(v)
\right|
=
M (X+u_0)^m e^{-(X+u_0)\eta}.
\tag{20}
\]

Put

\[
y:=(X+u_0)\eta.
\tag{21}
\]

Then

\[
\eta^m
\frac{|F_{X,\eta}^{(m)}(v)|}{M}
=
y^m e^{-y}.
\tag{22}
\]

The maximum of `y^m e^(-y)` over `y>=0` occurs at `y=m`, and the elementary Stirling lower bound gives

\[
y^m e^{-y}
\le
m^m e^{-m}
\le
m!.
\tag{23}
\]

Consequently

\[
\boxed{
|F_{X,\eta}^{(m)}(v)|
\le
m! M\eta^{-m}
\qquad(m\ge0).
}
\tag{24}
\]

This is exactly the scale furnished by Cauchy estimates from a strip of width `eta`. The phase-matched extremizer therefore survives not only a pointwise `H^infinity` hypothesis but also the whole lower-edge Cauchy derivative envelope.

Equivalently, integration by parts can only trade a factor `X^(-m)` against derivative costs of order `eta^(-m)`. That exchange depends on `X eta`, and the extremizer shows that no uniform extra factor tending to zero can be forced from this information alone. Any argument that uses only generic strip holomorphy, its supremum norm, and derivative bounds inherited from that same strip remains inside the sharp class (19).

## 5. Why the extremizer is relevant to the Euler representation

The lower-bound witness is generic, so (19) is not itself an arithmetic theorem. But its phase is not foreign to the zeta logarithmic derivative. On `Re(s)>1`,

\[
P_0(s+iv)
=
\sum_{n\ge2}
\Lambda(n)n^{-s}e^{-iv\log n}.
\tag{25}
\]

Every Euler/Dirichlet atom therefore has exactly the form

\[
e^{-iv\lambda},
\qquad
\lambda=\log n,
\tag{26}
\]

used by the extremizer. A carrier near `X` is matched by atoms with `log n=X+O(1)`, precisely the logarithmic shell selected by `L_X`.

This observation must not be overread. Equation (13) is allowed to place the full abstract amplitude `M` into one matched frequency. The actual function `P_0` cannot choose its amplitudes freely: on the absolutely convergent side they are fixed by `Lambda(n)n^(-s)`, and after transport they remain tied to the analytic continuation of that same arithmetic object. The theorem therefore does **not** say that `P_0` attains the generic extremum.

It says something narrower and useful: a proof that forgets those amplitude and coefficient constraints cannot distinguish `P_0` from an admissible phase-matched extremizer. The extra saving sought after `NB-221` has to enter through arithmetic spectral information, not through carrier oscillation considered in isolation.

## 6. Consequence for the Vinogradov--Korobov corridor

Use the notation of `NB-221`,

\[
Q:=\log(10+|t|),
\qquad
R:=Q^{2/3}(\log Q)^{1/3},
\qquad
\eta=\frac cR.
\tag{27}
\]

That finding obtains, for the leading transported term,

\[
|A_0|
\ll
Q^2 e^{-cX/R}
\tag{28}
\]

by combining the contour factor with the local pointwise estimate

\[
\left|\frac{\zeta'}{\zeta}\right|
\ll Q^2.
\tag{29}
\]

Set `M=Q^2` in (19). There exist bounded analytic functions on the very same strip for which the corresponding carrier functional is

\[
\asymp
Q^2 e^{-cX/R}.
\tag{30}
\]

Therefore no theorem with hypotheses consisting only of

1. holomorphy in the local zero-free strip,
2. the pointwise envelope `O(Q^2)`, and
3. generic Cauchy regularity from that strip,

can replace (28) by

\[
o\!\left(Q^2e^{-cX/R}\right)
\tag{31}
\]

uniformly in the coupled parameters.

This is the precise method boundary left implicit by `NB-221`. The rapid carrier is potentially useful only after one proves that the **actual** `-zeta'/zeta` cannot concentrate its allowed amplitude in a carrier-matched spectral component. Such a statement is strictly stronger than a zero-free strip plus a pointwise logarithmic-derivative bound.

A useful next target is therefore frequency-localized rather than pointwise: estimate the actual projection

\[
\int
 e^{iXv}
\Phi_\eta(v)
 w_V(v+i\eta)
P_0(\sigma_X-\eta+i(t+v))\,dv
\tag{32}
\]

using the prescribed Euler coefficients, an explicit-formula constraint, a genuinely local mean-square/large-values input, or another arithmetic mechanism that excludes the matched analytic extremizer. Merely integrating by parts, taking another primitive, or invoking the same zero-free rectangle in a different norm does not supply that distinction.

## 7. Prior-art and novelty audit

The generic background is classical. Paley--Wiener theory relates holomorphic extension to a strip with exponential Fourier decay; the contour displacement proving (11) is a standard manifestation of that principle. A representative strip formulation is Zen Harper, *Laplace transform representations and Paley-Wiener theorems for functions on vertical strips*, Documenta Mathematica 15 (2010), 235--254, DOI `10.4171/DM/296`.

No external theorem is load-bearing for (19): both the upper bound and the saturating function are derived directly above. For that reason this finding does not require a new `SOURCES.md` anchor. No theorem-level novelty is claimed for the abstract strip operator norm.

The line-local delta is the falsification of a specific post-`NB-221` route. `NB-221` identified cancellation inside the transported carrier as the remaining source-side escape. The present result separates two meanings of that phrase. **Generic analytic cancellation is exhausted by the contour factor `e^(-X eta)` and is sharp.** Any further cancellation has to be a property of the arithmetic logarithmic derivative itself.

This remains compatible with classical Paley--Wiener theory rather than competing with it: the matched exponential is exactly the sort of boundary-frequency witness showing why strip width determines the exponential decay scale.

## 8. Boundary conditions and adversarial audit

The main limitation is deliberate. The extremizer (13) is not asserted to equal `-zeta'/zeta` on any rectangle. It proves a sharpness statement for the information class used by the generic contour argument. A zeta-specific theorem may and should beat the bound if it exploits additional structure.

The result also assumes a nonzero fixed-width shell profile and the soft windows of `NB-220`--`NB-221` with `V` eventually larger than a profile-dependent constant. This includes the operational regime `V=X^epsilon` used there. If a future argument changes the source profile with `X`, shrinks its support, or imposes a new frequency-localized norm, its constants and extremizers must be re-audited rather than imported from (19).

The finite-height rectangle causes no hidden problem because the lower witness needs only a fixed amount of the Schwartz mass in `v`; truncation at `T=|t|/2` preserves that mass for large `|t|`.

A decisive falsification test for the method-boundary claim would be a uniform estimate strictly stronger than (19) for **every** bounded holomorphic `F` in `S_eta` under only the hypotheses stated in Sections 1--2. The explicit function (13) rules this out. By contrast, a stronger estimate proved only for the actual `P_0` would not falsify this finding; it would supply exactly the arithmetic information that the finding says is missing.

## Consequence for the research line

`NB-218`--`NB-221` removed the absolute Mellin tariff, localized the primitive pairing, continued it safely across the one-line, and reduced all fixed primitive depths to the same local `-zeta'/zeta` carrier. `NB-222` now removes one more generic escape: **the carrier oscillation cannot be converted into an additional uniform saving from strip analyticity alone.**

The source-side frontier is correspondingly narrower. The next useful estimate must distinguish the logarithmic derivative from the phase-matched bounded analytic witnesses admitted by the Vinogradov--Korobov rectangle. In practical terms, the missing currency is an arithmetic, frequency-localized anti-concentration bound for the carrier projection (32), not another representation change or another application of generic holomorphy.