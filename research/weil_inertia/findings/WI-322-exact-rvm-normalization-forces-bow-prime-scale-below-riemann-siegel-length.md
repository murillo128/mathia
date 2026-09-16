# WI-322 — exact Riemann--von Mangoldt normalization forces the bow prime scale below Riemann--Siegel length

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + CORRECTION`.

WI-184 used Riemann--von Mangoldt only at exponent-level accuracy and obtained `c >= 4π-o(1)` for a long functional-equation-symmetrized Maynard--Pratt bow with ordinate step `c/log T`. WI-188 and WI-189 therefore kept the reciprocal prime length only as `X=T^(1/2+o(1))` and allowed the chirp parameter `rho_T=U/X^2` to tend to zero subpolynomially. Retaining the exact local zero-density factor `log(T_0/(2π))` before exponentiating gives a stronger one-sided statement.

For a source-compatible bow based at height `T_0 asymp T`, with `m=T^epsilon`, fixed `0<epsilon<1/2`, bounded positive spacing parameter `c_T`, and compulsory same-ordinate functional-equation mirrors, one has

\[
\boxed{
 c_T\ge
 \frac{4\pi\log T}{\log(T_0/(2\pi))}
 \left(1-O\!\left(\frac{\log T}{m}+\frac{m}{T(\log T)^2}\right)\right).
}
\]

Consequently, for the reciprocal exponent `alpha_*=2π/c_T` and prime-side length `X_*=T^(alpha_*)`,

\[
\boxed{
 X_*\le \sqrt{\frac{T_0}{2\pi}}\,(1+o(1)).
}
\]

If the localized Montgomery square is centered at any `U=T_0+o(T_0)` inside the bow interval, then

\[
\boxed{
 \rho_T:=\frac{U}{X_*^2}\ge 2\pi(1-o(1)).
}
\]

Thus the rate-free possibility `rho_T -> 0` is not source-compatible. At exact local count saturation the natural reciprocal scale is bounded by the usual Riemann--Siegel self-dual length `sqrt(U/(2π))`; larger bow spacing only shortens `X_*` and increases `rho_T`.

Combining this with WI-189's exact derivative-image formula restores a rate-free **linear lower bound** for the number of `B`-process stationary aliases at each growing shift. Uniformly for `h=o(X_*)`,

\[
\Delta_h
=\frac{U h}{4\pi X_*^2}
\frac{3+h/X_*}{(1+h/X_*)(2+h/X_*)}
=\left(\frac{3}{8\pi}+o(1)\right)\rho_T h,
\]

so

\[
\boxed{
 \Delta_h\ge\left(\frac34-o(1)\right)h.
}
\]

Since the integer stationary-level count satisfies `nu_h=Delta_h+O(1)`, every shift `h -> infinity` in the genuinely coupled range crosses at least `(3/4-o(1))h` integer derivative levels. If `K_kappa=floor(kappa X_*/H)` with fixed `kappa>0`, `H->infinity`, and `K_kappa->infinity`, then

\[
\boxed{
 \sum_{h\le K_\kappa}\nu_h
 \ge \left(\frac38-o(1)\right)K_\kappa^2.
}
\]

This sharpens the scale bookkeeping in WI-188/WI-189 but does **not** bound the signed twisted-prime covariance: stationary contributions may still cancel after the `B` process or across shifts. The accepted clue `CLUE-bow-distinguished-twist-offdiagonal-cancellation` therefore remains open. The durable consequence is narrower: one cannot use an uncontrolled approach of `c_T` to `4π` to make the distinguished source chirp sparse or asymptotically nonstationary.

## 1. Keep the exact local zero density

Use the Maynard--Pratt bow normalization

\[
\gamma_j=T_0+\frac{c_Tj}{L},
\qquad 1\le j\le m,
\qquad L:=\log T,
\qquad T_0\asymp T,
\tag{1}
\]

with `m=T^epsilon`, fixed `0<epsilon<1/2`, and `c_T` bounded above and below by positive constants. Its vertical span is

\[
Y:=\gamma_m-\gamma_1
=\frac{c_T(m-1)}{L}=o(T_0).
\tag{2}
\]

As in WI-184, functional-equation reflection at the same positive ordinate forces a baseline population

\[
B_I=2m-r_c=2m+O(1),
\tag{3}
\]

where the displayed Maynard--Pratt bow has only `r_c=O(1)` selected labels on the critical line. Multiplicity and any additional zeros only increase the interval count.

Write the classical Riemann--von Mangoldt main term as

\[
F(t)=\frac{t}{2\pi}\log\frac{t}{2\pi e}.
\tag{4}
\]

Then

\[
F'(t)=\frac1{2\pi}\log\frac{t}{2\pi},
\qquad
F''(t)=\frac1{2\pi t}.
\tag{5}
\]

Using `N(t)=F(t)+O(log t)` and Taylor expansion over `Y=o(T_0)` gives

\[
\boxed{
N(T_0+Y)-N(T_0)
=
\frac{Y}{2\pi}\log\frac{T_0}{2\pi}
+O\!\left(\frac{Y^2}{T_0}+L\right).
}
\tag{6}
\]

The `O(Y)` term used in the coarser WI-184 rewrite is unnecessary if the exact derivative `log(T_0/(2π))/(2π)` is retained.

Let

\[
L_0:=\log\frac{T_0}{2\pi}.
\tag{7}
\]

Since the interval contains at least the population (3), equations (2) and (6) imply

\[
2m-O(1)
\le
\frac{c_T(m-1)L_0}{2\pi L}
+O\!\left(\frac{m^2}{TL^2}+L\right).
\tag{8}
\]

Here `T_0 asymp T` and boundedness of `c_T` were used only in the error. Dividing by `m` and solving for `c_T` yields

\[
\boxed{
c_T
\ge
\frac{4\pi L}{L_0}
\left(1-O(\eta_T)\right),
\qquad
\eta_T:=\frac{L}{m}+\frac{m}{TL^2}.
}
\tag{9}
\]

For `m=T^epsilon`, fixed `0<epsilon<1/2`,

\[
\eta_T L
=O\!\left(\frac{L^2}{T^\epsilon}
+\frac{T^{\epsilon-1}}{L}\right)
=o(1).
\tag{10}
\]

That extra `o(1/L)` accuracy is exactly what disappears if `L_0` is replaced by `L` before the reciprocal exponent is exponentiated.

## 2. Reciprocal bow length is one-sided Riemann--Siegel bounded

The first reciprocal bow frequency in WI-184 is

\[
\alpha_*:=\frac{2\pi}{c_T}.
\tag{11}
\]

Taking reciprocals in (9), using (10), gives

\[
\alpha_*L
\le
\frac{L_0}{2}+O(\eta_TL)
=
\frac{L_0}{2}+o(1).
\tag{12}
\]

Therefore the corresponding BGSTB/Montgomery prime scale obeys

\[
\boxed{
X_*:=T^{\alpha_*}
\le
\exp\!\left(\frac{L_0}{2}+o(1)\right)
=
\sqrt{\frac{T_0}{2\pi}}\,(1+o(1)).
}
\tag{13}
\]

This is one-sided. No rate for the excess zero population is assumed, so `X_*` may be substantially *smaller* than the Riemann--Siegel length by a subpower factor. What is excluded is the opposite drift that WI-188 left formally open.

A local source square attached to this bow is centered at a height `U=T_0+O(Y)=T_0(1+o(1))`. Hence (13) gives

\[
\boxed{
\rho_T:=\frac{U}{X_*^2}
\ge 2\pi(1-o(1)).
}
\tag{14}
\]

In particular `rho_T` cannot tend to zero. If the zero-count lower constraint is nearly saturated at the stronger `o(1/L)` level, then `rho_T` approaches `2π`; if `c_T` lies above the count-minimal spacing by more, `X_*` is shorter and `rho_T` is larger.

The appearance of `sqrt{U/(2π)}` is not a new approximate-functional-equation theorem. It is the same classical self-dual normalization, recovered here from the exact local zero density and the reciprocal bow frequency.

## 3. The rate-free per-shift alias lower bound

WI-189 gives the exact derivative sweep for the chirp

\[
f_h(x)=\frac{U}{2\pi}\log\left(1+\frac hx\right)
\tag{15}
\]

on a central block `[X_*,2X_*]`:

\[
\Delta_h
=
\frac{Uh}{4\pi X_*^2}
\frac{3+u}{(1+u)(2+u)},
\qquad
u_h=\Delta_h+O(1),
\qquad
u:=\frac h{X_*}.
\tag{16}
\]

To avoid overloading notation, the last ratio will be denoted `u=h/X_*` below. For the localized shift family `h <= kappa X_*/H` with fixed `kappa` and `H->infinity`, one has `u=o(1)` uniformly. Thus

\[
\Delta_h
=\left(\frac{3}{8\pi}+o(1)\right)\rho_T h.
\tag{17}
\]

Equation (14) now implies the source-compatible lower bound

\[
\boxed{
\Delta_h\ge\left(\frac34-o(1)\right)h.
}
\tag{18}
\]

Therefore, uniformly for growing shifts in the coupled range,

\[
\boxed{
\nu_h\ge\left(\frac34-o(1)\right)h-O(1).
}
\tag{19}
\]

This does not give a matching upper bound because `rho_T` may grow subpolynomially. The corrected statement is consequently `nu_h \gtrsim h`, not `nu_h=Theta(h)` without an additional upper control on `rho_T`.

If

\[
K_\kappa:=\left\lfloor\kappa\frac{X_*}{H}\right\rfloor\to\infty,
\tag{20}
\]

summing (19) gives

\[
\boxed{
\sum_{h\le K_\kappa}\nu_h
\ge
\left(\frac38-o(1)\right)K_\kappa^2.
}
\tag{21}
\]

This is consistent with WI-189's exact aggregate asymptotic

\[
\sum_{h\le K_\kappa}\nu_h
=
\left(\frac{3\kappa^2}{16\pi}+o(1)\right)\frac{U}{H^2},
\tag{22}
\]

because `U/X_*^2 >= 2π(1-o(1))` turns (22) into precisely the lower scale `(3/8-o(1))K_kappa^2`.

## 4. Correction boundary relative to WI-184, WI-188, and WI-189

WI-184's exponent-level conclusions remain correct: source compatibility pushes the reciprocal bow line to `alpha_* <= 1/2+o(1)` and count saturation gives `c_T=4π+o(1)` in the coarser normalization. The new point is that the `O(1/log T)` distinction between `log T` and `log(T_0/(2π))` cannot be discarded before forming `T^(alpha_*)`.

Accordingly, WI-188's sentence that `rho_T=T^{o(1)}` "need not converge to a nonzero constant" is too weak on the **lower** side for an actual source-compatible bow: the exact count gives `liminf rho_T >= 2π`. Its broader conclusion survives unchanged: the height chirp is an arithmetic oscillation problem and first-derivative dismissal fails.

WI-189 is also unchanged at its main aggregate level. Its `U/H^2` alias-count identity remains exact and rate-robust. What improves is the interpretation of the per-shift scale: the missing approach rate of `c_T` to `4π` may increase `rho_T`, but cannot drive it below a positive constant. Thus an additional proposed escape is closed:

\[
\boxed{
\text{source-compatible count saturation}
\not\Rightarrow
\text{a vanishing chirp density }U/X_*^2.
}
\tag{23}
\]

None of these alias counts controls the sign or total size of the transformed von-Mangoldt covariance. The accepted distinguished-twist clue still requires genuine cancellation or a structural obstruction to it.

## 5. Prior art and evidence boundary

The bow itself and its normalization come from James Maynard and Kyle Pratt, **Half-Isolated Zeros and Zero-Density Estimates**, *International Mathematics Research Notices* 2024:19 (2024), 12978--13014, DOI `10.1093/imrn/rnae191`, especially Section 8. Functional-equation reflection and Riemann--von Mangoldt are classical. Elchin Hasanalizade, Quanli Shen and Peng-Jie Wong, **Counting zeros of the Riemann zeta function**, *Journal of Number Theory* 235 (2022), 219--241, DOI `10.1016/j.jnt.2021.06.032`, provides an explicit `O(log T)` version of the zero-count error more than sufficient for (6)--(10). The stationary-frequency interpretation of the derivative image is the classical van-der-Corput `B` process; WI-189 already anchors Graham--Kolesnik and a recent explicit zeta implementation.

A targeted external search around Maynard--Pratt bows, exact Riemann--von Mangoldt local density, reciprocal frequencies, and the `log(1+h/x)` B-process phase located the primary bow and zero-count sources but no statement of the scale bound (13) or the alias consequence (18). Absence from that search is not evidence of priority, and no priority claim is made.

The exact new deduction here is the retention of `log(T_0/(2π))` through the exponentiation step and its combination with the already-derived WI-189 phase geometry. No new theorem about primes, shifted correlations, zeta zeros beyond the classical count, or the signed bow covariance is claimed.

## 6. Research consequence

The bow route has one fewer normalization loophole. For a long source-compatible symmetrized bow, the reciprocal prime polynomial is not merely `T^(1/2+o(1))`: it is one-sided bounded by the local Riemann--Siegel length. Hence the distinguished high-twist covariance necessarily lies in a regime where every sufficiently large coupled shift carries at least linearly many stationary lattice aliases.

This strengthens the negative side of `CLUE-bow-distinguished-twist-offdiagonal-cancellation`: a successful proof cannot obtain de-exceptionalization by arguing that the count-saturating bow might approach `4π` at a rate making `U/X_*^2` vanish. The remaining viable mechanisms are genuinely arithmetic: cancellation inside the stationary dual family or across shifts, a source-fixed lower/coercive observable, or an independent charge on the cancellation reservoir. No unconditional simple-critical-zero percentage changes here.