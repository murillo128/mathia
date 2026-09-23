# FD-285 — Reciprocal-zeta phase cone protects most of the right Perron collar

- **Date:** 2026-09-23
- **Status:** proved RH-conditional route-narrowing bound
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** grouped Perron collar / reciprocal-zeta phase cone / signed prime witness / cross-strip cancellation / route narrowing
- **Depends on:** FD-261, FD-282, FD-283, FD-284
- **Classification:** `DERIVED + RH-CONDITIONAL + SIGNED-PERRON-LOWER-BOUND + PHASE-CONE + PRIME-PHASE-WITNESS + ROUTE-NARROWING`

## Claim

FD-284 proves that a sufficiently thin strip at the outer edge of the strict-right Perron collar retains an `Nx^(1-o(1))` signed physical-band plateau after the `sigma` integration and upper/lower pairing. The thinness can be quantified much more sharply. The reciprocal-zeta factor cannot rotate enough across most of the standard right collar to cancel the prime self-divisor contribution internally.

Assume the Riemann hypothesis, let

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

put

\[
L:=\log(2Nx),\qquad c:=1+\frac1L,
\tag{2}
\]

and fix

\[
\boxed{
 e^{-\pi/2}<\eta<1.
}
\tag{3}
\]

Set

\[
a_\eta:=1+\frac{\eta}{L}.
\tag{4}
\]

With the grouped physical kernel

\[
K_s(d)
:=\sum_{q\mid d}\frac{q^s-(q-1)^s}{s}
 =\sum_{q\mid d}\int_{q-1}^{q}u^{s-1}\,du,
\tag{5}
\]

define the upper/lower-paired signed contribution of the whole strict-right strip `[a_eta,c]` by

\[
\mathcal H_d^{(\eta)}(T)
:=-\frac1\pi\operatorname{Im}
\int_{a_\eta}^{c}
\frac{N^{\sigma+iT}K_{\sigma+iT}(d)}
     {\zeta(\sigma+iT)}\,d\sigma.
\tag{6}
\]

Then for every fixed `epsilon in (0,1/2)`, uniformly in

\[
x^\varepsilon\le T\le x^{1/2-\varepsilon},
\tag{7}
\]

one has

\[
\boxed{
\sum_{x<d\le2x}
\left|\mathcal H_d^{(\eta)}(T)\right|
\gg_{\lambda,\varepsilon,\eta}
\frac{Nx}{L^2\log x}.
}
\tag{8}
\]

Thus

\[
\sum_{x<d\le2x}|\mathcal H_d^{(\eta)}(T)|
\ge Nx^{1-o(1)}.
\tag{9}
\]

The strip in (6) occupies the fraction `1-eta` of the standard strict-right collar `(1,c]`. Since `eta` may be any fixed number strictly above `exp(-pi/2)`, the argument protects every fixed outer fraction strictly smaller than

\[
\boxed{
1-e^{-\pi/2}=0.7921204236\ldots
}
\tag{10}
\]

from cancellation internal to that fraction. The present hard-Perron route can therefore cancel the signed prime plateau only by drawing on the remaining near-one slice, on the horizontal portion at or left of `Re(s)=1`, or by changing the contour/truncation architecture.

## 1. An exact phase budget on `Re(s)>1`

Write

\[
g(\sigma):=\frac1{\zeta(\sigma+iT)}.
\tag{11}
\]

There are no zeros of `zeta` for `sigma>1`, so a continuous argument of `g` may be chosen on `[a_eta,c]`. Absolute convergence of the logarithmic-derivative series gives

\[
\left|\frac{g'(\sigma)}{g(\sigma)}\right|
=
\left|\frac{\zeta'}{\zeta}(\sigma+iT)\right|
\le
\sum_{n\ge1}\frac{\Lambda(n)}{n^\sigma}
=
-\frac{\zeta'}{\zeta}(\sigma).
\tag{12}
\]

Hence for every `sigma in [a_eta,c]`,

\[
\begin{aligned}
\left|\arg g(\sigma)-\arg g(c)\right|
&\le
\int_\sigma^c
\left|\frac{g'(u)}{g(u)}\right|du\\
&\le
\int_\sigma^c-\frac{\zeta'}{\zeta}(u)\,du\\
&=
\log\frac{\zeta(\sigma)}{\zeta(c)}\\
&\le
\log\frac{\zeta(a_\eta)}{\zeta(c)}.
\end{aligned}
\tag{13}
\]

The elementary pole asymptotic

\[
\zeta(1+t)=\frac1t+O(1),\qquad t\downarrow0,
\tag{14}
\]

gives

\[
\log\frac{\zeta(a_\eta)}{\zeta(c)}
=
\log\frac1\eta+O_\eta(L^{-1}).
\tag{15}
\]

Condition (3) is exactly

\[
\log\frac1\eta<\frac\pi2.
\tag{16}
\]

Therefore there is a fixed `delta=delta(eta)>0` such that, for all sufficiently large `x`,

\[
\boxed{
\left|\arg g(\sigma)-\arg g(c)\right|
\le \frac\pi2-2\delta
\qquad(a_\eta\le\sigma\le c).
}
\tag{17}
\]

This is the new structural input. It controls the **entire** interval `[a_eta,c]` at once, rather than subdividing it into thin strips and allowing their signed outputs to cancel later.

## 2. Positive radial weights preserve the phase cone

For a prime `p in (x,2x]`, define the coefficient of its self-divisor cell by

\[
A_{p,\eta}
:=
\int_{a_\eta}^{c}
N^\sigma p^{\sigma-1}g(\sigma)\,d\sigma.
\tag{18}
\]

The scalar weight `N^sigma p^(sigma-1)` is positive. Consequently (17) puts every integrand vector in one open half-plane centered at `arg g(c)`, so their integral cannot cancel. More quantitatively,

\[
\operatorname{Re}\!\left(
 e^{-i\arg g(c)}A_{p,\eta}
\right)
\ge
\sin(2\delta)
\int_{a_\eta}^{c}
N^\sigma p^{\sigma-1}|g(\sigma)|\,d\sigma.
\tag{19}
\]

For `sigma>1`, triangle inequality for the zeta Dirichlet series gives

\[
|g(\sigma)|
=\frac1{|\zeta(\sigma+iT)|}
\ge
\frac1{\zeta(\sigma)}.
\tag{20}
\]

On `[a_eta,c]`, the elementary integral comparison `zeta(1+t)<=1+1/t` yields

\[
\frac1{\zeta(\sigma)}\gg_\eta\frac1L.
\tag{21}
\]

Also, uniformly for `p in (x,2x]`,

\[
N^\sigma p^{\sigma-1}
=N(Np)^{\sigma-1}
\asymp_{\lambda,\eta}N,
\tag{22}
\]

because `(sigma-1)L` remains in the fixed interval `[eta,1]` and `log(Np)/L=1+o(1)`. Since the strip width is `(1-eta)/L`, (19)--(22) give

\[
\boxed{
|A_{p,\eta}|\gg_{\lambda,\eta}\frac{N}{L^2},
\qquad
\left|\arg A_{p,\eta}-\arg g(c)\right|
\le\frac\pi2-2\delta.
}
\tag{23}
\]

Thus the full strict-right fraction in (6) has already been integrated before any absolute value is taken, yet its prime coefficient still has both a power-relevant size and a controlled phase.

## 3. Prime coordinates convert the phase cone into a signed lower bound

For prime `p`, as in FD-284,

\[
K_s(p)
=
\frac1s+
\int_{p-1}^{p}u^{s-1}\,du,
\tag{24}
\]

and uniformly for `sigma in [a_eta,c]`,

\[
\int_{p-1}^{p}u^{s-1}\,du
=
p^{s-1}
\left(1+O\!\left(\frac{T+1}{p}\right)\right).
\tag{25}
\]

Substitution into (6) yields

\[
\mathcal H_p^{(\eta)}(T)
=
-\frac1\pi
\operatorname{Im}\left(
 e^{iT\log(Np)}A_{p,\eta}
\right)
+
O_\eta\!\left(
N\left(\frac{T}{x}+\frac1T\right)
\right).
\tag{26}
\]

The error estimate uses only absolute convergence on `sigma>=a_eta`: `|1/zeta(s)|<=zeta(sigma)<<_eta L`, the strip width `O_eta(1/L)`, and the `1/s` term in (24). In the height window (7),

\[
N\left(\frac{T}{x}+\frac1T\right)
=o\!\left(\frac{N}{L^2}\right).
\tag{27}
\]

Let

\[
\Phi:=T\log N+\arg g(c).
\tag{28}
\]

The phase uncertainty in (23) is at most `pi/2-2delta`. Hence every prime satisfying

\[
\operatorname{dist}_{\pi}\!\left(
T\log p+\Phi,\frac\pi2
\right)
\le\delta
\tag{29}
\]

has, for all sufficiently large `x`,

\[
\left|
\operatorname{Im}\left(
 e^{iT\log(Np)}A_{p,\eta}
\right)
\right|
\ge
\sin(\delta)|A_{p,\eta}|.
\tag{30}
\]

Here `dist_pi` denotes distance modulo `pi`. Combining (23), (26), and (27),

\[
\boxed{
|\mathcal H_p^{(\eta)}(T)|
\gg_{\lambda,\eta}\frac{N}{L^2}
}
\tag{31}
\]

on the robust phase sector (29).

The set of `y in [x,2x]` satisfying (29) is a union of `O(T)` intervals and has ordinary length `>>_eta x`. Indeed, in the variable `v=log y`, the phase `Tv+Phi` is periodic with period `pi`, the accepted phase window has fixed positive width `2delta`, and within one period the Jacobian `dy=e^v dv` changes only by `1+O(1/T)` because `T>=x^epsilon`.

Under RH, the Schoenfeld estimate already anchored for FD-284,

\[
\vartheta(y)=y+O(y^{1/2}\log^2y),
\tag{32}
\]

applied at the `O(T)` interval endpoints gives total error

\[
O(Tx^{1/2}\log^2x)=o(x)
\tag{33}
\]

through (7). Therefore

\[
\#\left\{
 p\in(x,2x]: p\text{ satisfies }(29)
\right\}
\gg_{\eta}\frac{x}{\log x}.
\tag{34}
\]

Summing (31) over these prime coordinates proves (8).

## 4. Quantitative narrowing of the cross-strip escape

FD-283 shows that `sigma` integration on a strict-right collar is a positive radial Mellin averaging mode by mode. FD-284 then proves that one sufficiently thin outer strip cannot become polynomially small after summing all Möbius coefficients and pairing the horizontal edges. The present result identifies how far that sign protection extends without partitioning the collar.

The worst-case accumulated phase rotation supplied by the absolutely convergent reciprocal-zeta factor from `c=1+1/L` down to `a_eta=1+eta/L` is asymptotically at most

\[
\log(1/\eta).
\tag{35}
\]

As long as this is below `pi/2`, all prime self-divisor coefficients remain in one open half-plane and internal cross-strip cancellation cannot remove their signed plateau. The critical value generated by this deterministic phase budget is therefore

\[
\eta_0=e^{-\pi/2}=0.2078795763\ldots.
\tag{36}
\]

Equivalently, for every fixed `rho<1-e^{-pi/2}`, the outer `rho/L` portion of the standard right collar has band norm `Nx^(1-o(1))` throughout (7).

The repair target from FD-261 is

\[
N^\theta x^{2-\beta_*},
\qquad
\beta_*:=\log_2(3/2).
\tag{37}
\]

Since the witness in (8) still has power scale `Nx`, the same exponent comparison as FD-284 applies: it is power-larger than the repair target whenever

\[
\lambda<\frac{1-\theta}{1-\beta_*}.
\tag{38}
\]

At the RH calibration `theta=1/2`, this includes every first-row depth `lambda<=1`.

What remains is narrower but not small in norm by any theorem here. The inner strict-right slice

\[
1<\sigma<1+\frac{\eta}{L}
\tag{39}
\]

may have a much larger pointwise reciprocal-zeta envelope than the protected strip and could still cancel it coordinate by coordinate; the horizontal portion at or left of `Re(s)=1` also remains available. Thus (8) is not a lower bound for the complete horizontal contour and does not prove failure of hard Perron itself.

## Prior-art and novelty boundary

The ingredients in the phase budget are classical: absolute convergence of `-zeta'/zeta` for `Re(s)>1`, the simple pole of `zeta` at `1`, and the RH prime-counting estimate already anchored in `SOURCES.md` for FD-284. The literature audit found general work on bounds for the logarithmic derivative of `zeta`, but no source asserting the grouped Farey-repair consequence (8) or the `exp(-pi/2)` collar threshold. No novelty is claimed for the classical analytic-number-theory ingredients themselves.

No new durable external theorem is imported beyond the existing Schoenfeld anchor, so this finding requires no `SOURCES.md` update.

## Boundaries and adversarial checks

- **The threshold is a sufficient phase-cone threshold, not a claimed sharp barrier.** The estimate (13) uses the full absolute log-derivative budget. Cancellation inside `zeta'/zeta` could permit a wider protected strip. Nothing here proves failure when `eta<=exp(-pi/2)`.
- **There is no uniformity as `eta` approaches the threshold.** The cone margin `delta(eta)` and the robust prime-sector proportion both tend to zero as `eta` decreases to `exp(-pi/2)`. Equation (10) means every fixed smaller fraction is admissible, not that the endpoint fraction is attained uniformly.
- **RH remains load-bearing only for prime phase-sector density.** The reciprocal-zeta phase cone and prime-coordinate reduction are unconditional on the strict-right collar.
- **The square-root height ceiling remains a prime-counting limitation.** The analytic phase argument itself does not stop at `T=x^(1/2)`; the `O(T)` endpoint accumulation in (33) does.
- **The polynomial lower-height condition remains technical.** It makes the cell and `1/s` errors in (27) negligible. No bounded- or subpolynomial-height theorem is asserted.
- **The inner collar is not proved too weak to cancel the protected strip.** Its width is smaller, but available upper bounds near `Re(s)=1` are correspondingly larger. Width alone cannot close the route.
- **All internal strip cancellation is retained before the norm.** The integral defining `A_(p,eta)` spans the whole interval `[a_eta,c]`; (19) is a cone projection after that signed integration, not a sum of absolute strip norms.

## Audit test

A decisive audit should check four interfaces independently: the argument-variation inequality (13), including the sign in the real-zeta integral; the asymptotic phase threshold (15)--(17); the cone-projection and lower-modulus estimates (19)--(23); and the robust prime-sector count (29)--(34). In particular, replacing `|1/zeta(s)|>=1/zeta(sigma)` by the opposite inequality would invalidate the magnitude lower bound, and allowing the phase cone to reach a closed half-plane would invalidate the robust sine sector.

## Research consequence

The surviving hard-Perron question after FD-284 was whether the rest of the strict-right collar could simply undo the thin outer-strip witness. FD-285 rules out that explanation across **most of the right collar at once**. Up to any fixed fraction below `79.212%` of its width, the reciprocal-zeta factor has insufficient worst-case phase rotation to make the positive radial prime coefficient cross a half-plane boundary, so the signed `Nx^(1-o(1))` plateau survives the complete integration over that fraction.

A viable cross-collar rescue must therefore reach into the final near-one part where the deterministic phase budget reaches `pi/2`, exploit the horizontal contour at or left of `Re(s)=1`, improve the available prime-density input to work at larger `T`, or replace the hard Perron architecture. The next useful theorem should control one of those interfaces; further subdivision of the already protected outer collar cannot by itself create the missing power saving.
