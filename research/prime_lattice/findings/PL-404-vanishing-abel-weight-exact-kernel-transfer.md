# PL-404 — A vanishing Abel weight transfers the zero-sensitive singular-series layer to the exact incomplete-gamma pair kernel

**Evidence/status:** `EXACT-DERIVED + LITERATURE-BASED + ROUTE-ADVANCE + CONTINUATION-KERNEL-TRANSFER + MODEL-SOURCE`.

**Parent findings:** `PL-399`, `PL-400`, `PL-401`, `PL-402`, `PL-403`.

## Claim

`PL-403` left one quantitative obstruction at the singular-series source level: the Abel-regularized cubic model has an RH-equivalent `H^-7/4` remainder, but the exact continuation coefficient from `PL-401` was only controlled through an aggregate `H^-1` error. That gap can be removed by two operations forced by the existing asymptotics:

1. multiply the exact pair channel by a quadratic vanishing factor `(d/H)^2`, which suppresses the fixed/subcubic gap region without moving any zeta-zero Mellin pole; and
2. retain the first omitted **lower-transition tail** of `Q_r`, whose contribution is an explicit universal `d^-2` term.

Let

\[
q=r+d,\qquad H=r^{1/3},\qquad T=2\pi rq,
\]

with integer `r>=1`, and reuse the exact continuation coefficient

\[
P_{r,d}
=\exp\!\big(i\{2\theta(T)-T\log(rq)\}\big)
 Q_q(T)Q_r(T)
\]

from `PL-400`--`PL-403`. Fix `eta>0`, put

\[
a_0=\frac\pi6,
\qquad
\chi_\eta(u)=u^2e^{-\eta u^3},
\]

and define the finite exact-kernel statistic

\[
\mathcal C_\eta(r)
:=\sum_{1\le d\le H\log H}
 \mathfrak S(d)\,
 \chi_\eta(d/H)\,
 \Re P_{r,d}.
\tag{1}
\]

Here `mathfrak S(d)` is the standard Hardy--Littlewood pair singular series already used in `PL-401`--`PL-403`; in particular it vanishes for odd `d`.

Define also

\[
w_\eta^{[2]}(u)
:=u e^{-\eta u^3}\sin(a_0u^3),
\tag{2}
\]

\[
A_\eta^{[2]}(H)
:=\frac1H\sum_{d\ge1}\mathfrak S(d)
 w_\eta^{[2]}(d/H),
\tag{3}
\]

and

\[
J_\eta:=\int_0^\infty e^{-\eta u^3}\,du
=\frac{\Gamma(1/3)}{3\eta^{1/3}}.
\tag{4}
\]

Then, as `r->infinity`,

\[
\boxed{
\mathcal C_\eta(r)
=-\frac{1}{\sqrt2\,\pi}A_\eta^{[2]}(H)
+\frac{J_\eta}{2\sqrt2\,\pi^2 H}
+O_\eta\!\left(H^{-2}(\log H)^3\right).
}
\tag{5}
\]

The power of the logarithm is inessential; the important point is that the transfer remainder is strictly below `H^-7/4`.

The shifted Abel weight (2) has Mellin transform

\[
\boxed{
\widehat w_\eta^{[2]}(s)
=\frac13
 \Gamma\!\left(\frac{s+1}{3}\right)
 R_\eta^{-(s+1)/3}
 \sin\!\left(\frac{\phi_\eta(s+1)}3\right),
}
\tag{6}
\]

where

\[
R_\eta=(\eta^2+a_0^2)^{1/2},
\qquad
\phi_\eta=\arctan(a_0/\eta)\in(0,\pi/2).
\]

At every nontrivial zeta-zero pole

\[
s_\rho=\frac\rho2-1,
\]

one has

\[
\frac{s_\rho+1}{3}=\frac\rho6,
\]

whose imaginary part is nonzero. Since Gamma has no zeros and the sine in (6) has only real zeros,

\[
\boxed{\widehat w_\eta^{[2]}(s_\rho)\ne0.}
\tag{7}
\]

Thus the extra quadratic vanishing at the origin does **not** erase the zero layer.

Write

\[
W_{1,\eta}
:=\widehat w_\eta^{[2]}(1)
=\frac{\Gamma(2/3)}{3R_\eta^{2/3}}
 \sin\!\left(\frac{2\phi_\eta}{3}\right),
\tag{8}
\]

and

\[
W_{0,\eta}
:=\widehat w_\eta^{[2]}(0)
=\frac{\Gamma(1/3)}{3R_\eta^{1/3}}
 \sin\!\left(\frac{\phi_\eta}{3}\right).
\tag{9}
\]

The same Goldston--Suriajaya/Mellin argument as in `PL-403`, now with (6), gives

\[
\mathrm{RH}
\iff
A_\eta^{[2]}(H)
=W_{1,\eta}
-\frac{W_{0,\eta}}{2H}
+O_{\eta,\varepsilon}(H^{-7/4+\varepsilon})
\tag{10}
\]

for every `epsilon>0`. Combining (5) and (10) yields the exact-kernel consequence

\[
\boxed{
\mathrm{RH}
\iff
\mathcal C_\eta(r)
=-\frac{W_{1,\eta}}{\sqrt2\,\pi}
+\frac1H\left(
 \frac{W_{0,\eta}}{2\sqrt2\,\pi}
 +\frac{J_\eta}{2\sqrt2\,\pi^2}
 \right)
+O_{\eta,\varepsilon}(H^{-7/4+\varepsilon})
}
\tag{11}
\]

for every `epsilon>0`, with `H=r^(1/3)` and integer `r->infinity`.

Equation (11) is **not yet an RH criterion for an intrinsic unweighted zeta observable**. The exact incomplete-gamma kernel is now present, but the arithmetic source remains the inserted classical singular series. The remaining bridge is the second one already separated in the Mind: replace the singular-series local-density model by an actual continuation-faithful arithmetic statistic without losing the `H^-7/4` scale.

## 1. The first omitted continuation term is explicit

Use the uniform incomplete-gamma transition notation from `PL-399`:

\[
A=\frac{s}{2},\qquad
\lambda_n=\frac{2\pi i n^2}{s},\qquad
f(\lambda)=\lambda-1-\log\lambda,
\qquad
y_n^2=A f(\lambda_n).
\]

For `d->infinity`, `d=o(r^(1/2))`, the two complementary-error-function tails satisfy

\[
Q_q(T)=E_q+O(r^{-1}),
\qquad
Q_r(T)=1-E_r+O(r^{-1}),
\tag{12}
\]

where DLMF §7.12 and §8.12 give

\[
E_q
=\frac{e^{-y_q^2}}{2\sqrt\pi\,y_q}
 \{1+O(d^{-2})\},
\qquad
E_r
=\frac{e^{-y_r^2}}{2\sqrt\pi\,(-y_r)}
 \{1+O(d^{-2})\}.
\tag{13}
\]

On the cubic window, with

\[
x=\frac{\pi d^3}{6r},
\]

`PL-400`--`PL-401` give

\[
E_q
=\frac{e^{-i\pi/4}}{\sqrt2\,\pi d}
 e^{-i\pi d^2/2-ix}
 +O\!\left(d^{-3}+r^{-1}+d^3r^{-2}\right).
\tag{14}
\]

The lower tail has the reflected cubic phase,

\[
E_r
=\frac{e^{-i\pi/4}}{\sqrt2\,\pi d}
 e^{-i\pi d^2/2+ix}
 +O\!\left(d^{-3}+r^{-1}+d^3r^{-2}\right).
\tag{15}
\]

There is a useful exact reason for the opposite signs. If `L=q/r`, then at the ideal critical-line saddle

\[
rq\{f(L)+f(L^{-1})\}
=rq\left(L+L^{-1}-2\right)
=(q-r)^2=d^2.
\tag{16}
\]

Hence the cubic term, and in fact the entire real-ratio transition phase, cancels in the product `E_q E_r`. The small displacement caused by the real part of `s` contributes only to the displayed subordinate error.

The Hardy phase is

\[
\exp\!\big(i\{2\theta(T)-T\log(rq)\}\big)
=e^{-i\pi/4}\{1+O(T^{-1})\}.
\tag{17}
\]

Substituting (12)--(17) into `P_(r,d)` gives

\[
P_{r,d}
=e^{-i\pi/4}E_q
-e^{-i\pi/4}E_qE_r
+O\!\left(d^{-3}+r^{-1}+d^3r^{-2}\right).
\tag{18}
\]

For even `d`, `exp(-i pi d^2/2)=1`. Taking real parts therefore yields the sharpened transition expansion

\[
\boxed{
\Re P_{r,d}
=-\frac{1}{\sqrt2\,\pi d}
 \sin\!\left(\frac{\pi d^3}{6r}\right)
+\frac{1}{2\sqrt2\,\pi^2d^2}
+O\!\left(d^{-3}+r^{-1}+d^3r^{-2}\right).
}
\tag{19}
\]

This identifies the `O(d^-2)` term that was only bounded in `PL-401`. Its phase is universal: the two opposite cubic transition phases cancel before the real projection.

No new special-function theorem is asserted here. Equations (12)--(19) are the next retained terms of the same classical `erfc`/uniform incomplete-gamma expansions already audited in `PL-399`--`PL-401`.

## 2. Why the quadratic vanishing factor is enough

The purpose of `chi_eta(u)=u^2 exp(-eta u^3)` is not cosmetic. Without it, the asymptotic tail (19) is not uniform down to fixed `d`, and the sum of the `d^-2` correction over the subcubic region produces a larger boundary contribution whose size depends on where the transition approximation is started.

Take

\[
D=H^{1/16},
\qquad
L=H\log H.
\]

For `d<=D`, the uniform transition formula keeps `Q_q`, `Q_r`, and hence `P_(r,d)` bounded. Since `mathfrak S(d)>=0` and its first moment is `O(D)`,

\[
\sum_{d\le D}
 \mathfrak S(d)\chi_\eta(d/H)|P_{r,d}|
\ll H^{-2}\sum_{d\le D}\mathfrak S(d)d^2
\ll H^{-2}D^3
=H^{-29/16}.
\tag{20}
\]

This is already smaller than `H^-7/4=H^-28/16`. The contributions of the model term and of the explicit `d^-2` correction on `d<=D` are smaller still.

On `D<d<=L`, (19) is uniform because

\[
d\le H\log H=o(r^{1/2}).
\]

After multiplication by `chi_eta(d/H)`, the remainder in (19) sums to

\[
O_\eta\!\left(H^{-2}\log H\right).
\tag{21}
\]

Indeed the `d^-3` term becomes

\[
H^{-2}\sum_{D<d\le L}\frac{\mathfrak S(d)}d
 e^{-\eta(d/H)^3}
=O(H^{-2}\log H),
\]

while the `r^-1=H^-3` and `d^3r^-2` terms both contribute `O_eta(H^-2)` by partial summation and the first-moment bound for `mathfrak S`.

Finally, the cutoff `L=H log H` costs less than every fixed inverse power of `H`: the Abel factor is `exp(-eta u^3)`, so the omitted model tail begins with `exp(-eta (log H)^3)`. Thus the finite exact statistic (1) may be compared with the full Mellin sums (3) without introducing another algebraic error layer.

## 3. The `d^-2` layer is universal to first order

From (19), the explicit correction contributes

\[
\frac{1}{2\sqrt2\,\pi^2}
\sum_d \mathfrak S(d)
 \frac{(d/H)^2e^{-\eta(d/H)^3}}{d^2}
=
\frac{1}{2\sqrt2\,\pi^2H}
 B_\eta(H),
\tag{22}
\]

where

\[
B_\eta(H)
:=\frac1H\sum_{d\ge1}
 \mathfrak S(d)e^{-\eta(d/H)^3}.
\tag{23}
\]

An elementary divisor expansion of the pair singular series is enough here. Set

\[
g(k)
=\mu^2(k)\mathbf 1_{2\nmid k}
 \prod_{p\mid k}\frac1{p-2}.
\]

Then

\[
\mathfrak S(d)
=2C_2\mathbf 1_{2\mid d}
 \sum_{k\mid d}g(k),
\tag{24}
\]

and

\[
C_2\sum_{k\ge1}\frac{g(k)}k
=C_2\prod_{p>2}
 \left(1+\frac1{p(p-2)}\right)
=1.
\tag{25}
\]

The elementary Euler-product bounds

\[
\sum_{k\le x}g(k)\ll (\log x)(\log\log(3x))^2,
\qquad
\sum_{k>x}\frac{g(k)}k
\ll \frac{(\log\log(3x))^2}{x}
\tag{26}
\]

follow, for example, from

\[
g(k)\ll\frac{(\log\log(3k))^2}{k}
\]

on square-free odd `k`. Hence

\[
\sum_{d\le x}\mathfrak S(d)
=x+O\!\left((\log x)(\log\log(3x))^2\right).
\tag{27}
\]

Partial summation with `exp(-eta u^3)` now gives

\[
B_\eta(H)
=J_\eta
+O_\eta\!\left(
 \frac{(\log H)(\log\log H)^2}{H}
 \right).
\tag{28}
\]

Substituting (28) into (22), together with (20)--(21), proves the transfer formula (5). In particular, the first continuation correction needs only its **mean** at the zero-sensitive scale. Its own arithmetic sublayers begin one extra factor `H^-1` lower and cannot interfere with the `H^-7/4` layer inherited from (3).

## 4. Mellin audit of the shifted Abel weight

Near zero,

\[
w_\eta^{[2]}(u)=a_0u^4+O(u^7),
\]

while at infinity it has exponential Abel decay. Therefore its Mellin transform is absolutely convergent on a half-plane wide enough to cross all singular-series zero poles. Substituting `t=u^3` gives (6).

The vertical decay is again exponential. Stirling contributes

\[
\exp(-\pi|t|/6),
\]

while the sine factor contributes at most

\[
\exp(\phi_\eta|t|/3),
\]

so the net decay is

\[
\exp\!\left(-\frac{\pi-2\phi_\eta}{6}|t|\right)
\]

up to polynomial factors. Thus the same contour/Mellin uniqueness argument used in `PL-403` applies without a new regularization issue.

At a nontrivial zero pole, the Gamma/sine argument is `rho/6`; (7) follows immediately. The pole at `s=1` of the singular-series Dirichlet transform gives (8), and its pole at `s=0` with residue `-1/2` gives the deterministic term `-W_(0,eta)/(2H)`. Goldston--Suriajaya's RH bound and omega mechanism then give (10), exactly as in `PL-403`.

There is one sampling detail in (11). The exact statistic is indexed by integer `r`, hence by

\[
H_r=r^{1/3}.
\]

The spacing satisfies

\[
H_{r+1}-H_r=O(H_r^{-2}).
\]

The absolutely convergent sum (3) has derivative `A_eta^[2]'(H)=O_eta(H^-1)` by the same first-moment/partial-summation bound. Therefore interpolation between neighboring `H_r` changes `A_eta^[2]` by `O_eta(H^-3)`, far below `H^-7/4`. Consequently an asymptotic on every integer `r` is equivalent, at the precision of (10), to the continuous-`H` asymptotic used in the Mellin converse. No zero can hide between the sampled cube-root scales.

## 5. Matched control

Replace the singular series by the parity surrogate

\[
\mathfrak S_{\rm par}(d)=2\mathbf 1_{2\mid d}.
\]

The exact transition expansion (19) is unchanged. The leading shifted Abel average is now an ordinary smooth lattice quadrature. Its Dirichlet transform is `2^(1-s) zeta(s)`, so it has the mean pole at `s=1` but neither the singular-series pole at `s=0` nor the denominator `1/zeta(2s+2)` that creates the nontrivial-zero poles.

Accordingly the parity control has

\[
\mathcal C_\eta^{\rm par}(r)
=-\frac{W_{1,\eta}}{\sqrt2\,\pi}
+\frac{J_\eta}{2\sqrt2\,\pi^2H}
+O_\eta(H^{-2}),
\tag{29}
\]

up to the same harmless cutoff convention. The extra

\[
\frac{W_{0,\eta}}{2\sqrt2\,\pi H}
\]

in (11), and then the `H^-7/4` zero layer, are absent. Thus the transfer does not manufacture the RH-sensitive hierarchy from the cubic phase or from even-gap density alone.

## 6. Prior-art and novelty audit

The analytic ingredients are classical and already anchored in `SOURCES.md`:

- Paris--Cang and Paris supply the exact normalized-incomplete-gamma representation and the critical-line smoothing context;
- DLMF §§7.12 and 8.12 supply the large-complex-`erfc` and uniform incomplete-gamma expansions used in (12)--(19);
- Goldston--Suriajaya supply the meromorphic singular-series transform, its zeta-zero poles, the RH `-7/4` normalized exponent, and the converse omega mechanism used in `PL-402`--`PL-403`.

Targeted searches for combinations of Riemann-zeta incomplete-gamma transition tails, Hardy--Littlewood pair singular-series averages, cubic gap scaling, and `erfc` pair corrections found the separate classical literatures but no source for the specific composition (19), the exact cancellation (16), or the transfer (5)/(11).

The safe novelty claim is therefore only the **Mathia-line composition**: the first discarded lower-transition tail can be computed, its cubic phase cancels against the upper tail, and a quadratic source weight suppresses the nonuniform small-gap region strongly enough that the resulting exact-kernel statistic inherits the already-known singular-series RH scale. No novelty is claimed for incomplete-gamma asymptotics, singular-series Mellin theory, or RH-equivalent Riesz bounds themselves.

## 7. Boundaries and falsification tests

1. **The arithmetic source is still a model.** Equation (11) uses `mathfrak S(d)` as an inserted Hardy--Littlewood local-density weight. It does not replace that model by actual `Lambda(r)Lambda(r+d)` data and does not prove a new theorem about prime pairs.

2. **The quadratic vanishing is structural.** It is what makes the fixed-gap region negligible below `H^-7/4`. Removing it reintroduces a larger subcubic boundary layer. A different source weight must recheck that endpoint explicitly.

3. **The first correction coefficient is falsifiable locally.** Re-expanding the exact normalized incomplete-gamma factors at `T=2 pi r(r+d)` must give, for even growing `d`,

\[
d^2\left[
 \Re P_{r,d}
 +\frac{1}{\sqrt2\,\pi d}
  \sin\!\left(\frac{\pi d^3}{6r}\right)
\right]
\longrightarrow
\frac{1}{2\sqrt2\,\pi^2}
\]

whenever `d->infinity`, `d=o(r^(1/2))`, and the displayed cubic phase remains bounded. A different constant or sign invalidates the transfer formula.

4. **The phase cancellation has an exact algebraic check.** Equation (16) follows directly from `f(lambda)=lambda-1-log lambda`. Failure of the `d^-2` universality cannot be blamed on an omitted cubic term; it would have to come from branch normalization, the subordinate incomplete-gamma coefficient, or the Hardy phase.

5. **The cutoff is not an arithmetic input.** `H log H` is used only to keep the exact statistic inside the uniform transition regime. Abel damping makes the difference from the full model super-polynomially small. Replacing `log H` by any slowly growing cutoff with cubic Abel tail smaller than every required algebraic scale gives the same result.

6. **This is not Hilbert--Polya.** The zeros remain poles of the analytically continued singular-series Mellin transform. The advance is a continuation-kernel transfer theorem, not a self-adjoint spectral realization.

7. **No claim is made beyond the same-sign pair channel.** Other completed-zeta channels may have different second-order transition geometry and must be audited separately.

## Consequence for the line

The first transfer obstruction recorded in `PL-403` is resolved at the **singular-series-weighted exact-kernel** level. The `H^-1` discrepancy was not an uncontrolled floor: it is the universal interaction of the upper and lower incomplete-gamma tails, and after its explicit subtraction the aggregate special-function error is `O(H^-2 polylog H)`, below the RH-sensitive `H^-7/4` layer.

The live obstruction therefore moves one step outward. Further work should not spend another pass refining this singular-series-to-exact-kernel comparison. The remaining difficult bridge is arithmetic: derive the same regulated statistic from an intrinsic continuation observable or from controlled prime-pair/Möbius data, with replacement error below `H^-7/4`, rather than inserting `mathfrak S(d)` as the source weight.