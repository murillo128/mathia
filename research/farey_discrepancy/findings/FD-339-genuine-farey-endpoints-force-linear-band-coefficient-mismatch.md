# FD-339 — Genuine Farey endpoints force linear-band coefficient mismatch

**Status:** LITERATURE+DERIVED + EXACT-FINITE-INEQUALITY + UNCONDITIONAL-ENDPOINT-OBSTRUCTION.

FD-337 identifies rank-sine and position-Fourier coefficient vectors up to an error `o(sqrt(E_Q))` for every cutoff `q=o(Q)`. FD-338 shows why a generic extension to linear cutoffs fails on rational controls, but leaves the genuine Farey sequence untouched. Here the actual first empty Farey interval forces a nonzero coefficient mismatch at a fixed linear cutoff, without any conjecture about its energy.

Specifically, for the genuine order-`Q` sequence and `q=128Q-1`,
\[
\boxed{\liminf_{Q\to\infty}Q\sum_{j=1}^{q}
 |d_{2j}-a_j|^2\ \ge\ \frac{3}{2048\pi^2}>0.}
\tag{1}
\]
The coefficients have exactly FD-337's normalizations. This is a statement about the **distance between vectors**, not a difference between their squared norms. It does not settle the actual linear-band energy-share question. It does show that the genuine coefficient distance cannot be `o(Q^{-1/2})`, and that relative coefficient transfer on this band would require `QE_Q -> infinity`. No assertion that `QE_Q` is bounded or diverges is made.

The obstruction also survives subtracting any reflection-compatible `O(1/Q)` profile supported in the outer quarters: the empty interval immediately right of `1/2` supplies an interior coefficient-error floor below `512Q`. Section 6 states this robust form with its exact correction class.

## 1. Objects and finite statement

Let
\[
0=x_0<x_1<\cdots<x_N=1,\qquad
N=\sum_{b\le Q}\varphi(b),\qquad
D_k=x_k-k/N,\quad E_Q=\sum_{k=1}^{N-1}D_k^2.
\]
For `Q>=3`, `N` is even and `D_(N-k)=-D_k`. Put
\[
d_{2j}=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(2\pi jk/N),
\qquad
C_j=\sum_{k=1}^N\cos(2\pi jx_k),\qquad
a_j=-\frac{C_j}{\pi j\sqrt{2N}}.
\tag{2}
\]
For the genuine sequence the exact Ramanujan identity is
\[
C_j=B_Q(j)=\sum_{\substack{b\mid j\\b\le Q}}
 bM(\lfloor Q/b\rfloor),\qquad M(y)=\sum_{n\le y}\mu(n).
\tag{3}
\]
Thus the position vector is the same classical Mertens vector as in FD-337; no new transform is introduced.

Set `m=128Q` and `q=m-1`. Whenever `N>=8Q` and `q<N/2`, the following finite bound holds:
\[
\boxed{\left(\sum_{j=1}^{q}|d_{2j}-a_j|^2\right)^{1/2}
\ge\frac{\sqrt N}{4Q\sqrt m}
 -\frac{\pi^2q^2}{3N^2}\sqrt{E_Q}.}
\tag{4}
\]
A negative right-hand side is simply uninformative. Both size conditions hold for all sufficiently large `Q`, since `N~3Q^2/pi^2`. Dress's theorem supplies
\[
\max_k|D_k|\le 1/Q,\qquad E_Q\le N/Q^2.
\tag{5}
\]
The second term in (4) is then `O(Q^{-2})`, whereas the first is of order `Q^{-1/2}`. Squaring this positive asymptotic lower bound proves (1).

## 2. Put both vectors in one continuous coordinate

Let `f` be the piecewise affine interpolant of the rank samples,
\[
f(k/N)=D_k,\qquad 0\le k\le N,
\]
extended periodically. Define the positive-point counting function and its centered discrepancy by
\[
A(t)=\#\{1\le k\le N:x_k\le t\},\qquad
g(t)=t-\frac{A(t)}N-\frac1{2N},\quad 0<t<1.
\tag{6}
\]
Values at the finitely many jumps do not affect any integral. The **minus** midpoint correction is required: away from these jumps,
`A(1-t)=N-1-A(t)`, so `g(1-t)=-g(t)`. The function `f` has the same antisymmetry. Hence `h=f-g` has zero mean and only sine modes on the unit circle.

Writing `sinc(z)=sin(z)/z`, with value one at zero, exact integration gives
\[
\sqrt{2N}\int_0^1 f(t)\sin(2\pi jt)\,dt
 =\operatorname{sinc}^2(\pi j/N)d_{2j},
\qquad
\sqrt{2N}\int_0^1 g(t)\sin(2\pi jt)\,dt=a_j.
\tag{7}
\]
For the first identity, each periodic linear hat centered at `k/N` has Fourier transform `N^{-1}sinc^2(pi j/N)e^{-2 pi i jk/N}`. For the second,
\[
\int_0^1 A(t)\sin(2\pi jt)\,dt
 =\sum_{k=1}^N\frac{\cos(2\pi jx_k)-1}{2\pi j}
 =\frac{C_j-N}{2\pi j},
\]
and `int_0^1 t sin(2 pi jt)dt=-1/(2 pi j)`. The constant in (6) contributes zero. These calculations retain the endpoint `x_N=1` consistently.

If `P_q` is orthogonal projection onto the trigonometric modes of frequencies at most `q`, (7) implies
\[
N\|P_qh\|_{L^2(0,1)}^2
=\sum_{j=1}^{q}
 |\operatorname{sinc}^2(\pi j/N)d_{2j}-a_j|^2.
\tag{8}
\]

## 3. The first empty interval gives a positive plateau

For `t` between consecutive actual points, (5) bounds (6) by
\[
|g(t)|\le 1/Q+1/(2N).
\]
The interpolant satisfies `|f|<=1/Q`; therefore, under `N>=8Q`,
\[
|h(t)|\le 3/Q.
\tag{9}
\]

The first positive Farey point is `1/Q`. If `t>=1/N`, the interpolated position `t+f(t)` is a convex combination of positive Farey points and is at least `1/Q`. On the other hand, `A(t)=0` when `0<t<1/Q`. Consequently, on
\[
I_Q=[1/(8Q),1/(4Q)]
\]
we have
\[
h(t)\ge 1/Q-2t+1/(2N)\ge1/(2Q).
\tag{10}
\]
The condition `N>=8Q` is precisely what places this whole interval beyond the initial interpolation cell. This plateau compares rank and position at the **same argument**; it is not a claim that the two counting conventions agree there.

## 4. A positive Fourier kernel detects the plateau below a linear cutoff

Use the period-one Fejér kernel
\[
K_m(u)=\frac1m\left(\frac{\sin(\pi mu)}{\sin(\pi u)}\right)^2
=\sum_{|j|<m}(1-|j|/m)e^{2\pi iju}.
\tag{11}
\]
It is nonnegative, has integral one and degree `m-1`, and Parseval gives
\[
\|K_m\|_2^2=1+2\sum_{j=1}^{m-1}(1-j/m)^2
=\frac{2m^2+1}{3m}\le m.
\tag{12}
\]
For circular distance `||u||<=1/2`, `|sin(pi u)|>=2||u||`. Thus for `0<delta<=1/2`,
\[
\int_{\|u\|\ge\delta}K_m(u)\,du
\le2\int_\delta^{1/2}\frac{du}{4mu^2}
\le\frac1{2m\delta}.
\tag{13}
\]

Choose `t_*=3/(16Q)` and `delta=1/(16Q)`. The interval of radius `delta` around `t_*` is exactly `I_Q`. With `m=128Q`, the kernel mass outside this interval is at most `1/16`. Combining (9)–(10),
\[
\begin{aligned}
\int_0^1h(t)K_m(t_*-t)\,dt
&\ge\frac1{2Q}(1-1/16)-\frac3Q\frac1{16}\\
&=\frac9{32Q}\ge\frac1{4Q}.
\end{aligned}
\tag{14}
\]
This handles arbitrary signs in the rest of the discrepancy field: no cancellation outside the endpoint layer can erase the localized witness.

Since the kernel has degree `q`, the integral pairs only with `P_qh`. Cauchy–Schwarz and (12) give
\[
\|P_qh\|_2\ge\frac1{4Q\sqrt m}.
\tag{15}
\]
Equations (8) and (15) prove the corresponding lower bound for the coefficients with the interpolation factor retained.

To remove that factor, for `0<=z<=pi/2`,
\[
0\le1-\operatorname{sinc}^2z\le z^2/3.
\]
Indeed `sinc z=int_0^1 cos(zu)du>=1-z^2/6`, and
`1-sinc^2 z<=(2)(1-sinc z)`. Discrete sine orthogonality gives
`sum_(j<=q)d_(2j)^2<=E_Q` when `q<N/2`. Hence
\[
\left(\sum_{j\le q}
 |(1-\operatorname{sinc}^2(\pi j/N))d_{2j}|^2\right)^{1/2}
\le\frac{\pi^2q^2}{3N^2}\sqrt{E_Q}.
\tag{16}
\]
The reverse triangle inequality now proves (4), completing the argument.

## 5. What this changes, and what remains open

The genuine sequence itself has an unavoidable `Q^{-1/2}` coefficient-error floor in a band of width `Theta(Q)`. An attempted extension of FD-337 that claims an **absolute** `o(Q^{-1/2})` error there is false, even with all Farey arithmetic retained. Conditional on `E_Q<=C/Q` along any subsequence, (1) also gives
\[
\liminf\frac{\sum_{j\le128Q-1}|d_{2j}-a_j|^2}{E_Q}
\ge\frac{3}{2048\pi^2C}>0
\]
along that subsequence. More generally, a vanishing relative coefficient error for all growing `Q` would force `QE_Q -> infinity`. This is a necessary condition, not a sufficient condition or a proved energy asymptotic.

The distinction from FD-338 is material. That finding obtains different normalized **band energies** on artificial rational grids. Here the objects are genuinely Farey, but only **coefficient separation** is proved. Two separated vectors can have equal norms; (1) does not imply a nonzero difference between `E_q/E_Q` and `T_q/T_infinity`. Nor does it show failure at every positive linear cutoff. The coefficient `128` is a convenient unoptimized localization constant.

The first empty interval, global displacement bound, and reflection explain this obstruction. It is an endpoint-geometric effect, not an additional arithmetic information channel or improved cancellation estimate. RH only supplies the usual `E_Q=O_epsilon(Q^{-1+epsilon})` criterion, which does not assert bounded `QE_Q`; no contradiction to RH follows. Sublinear-band transfer, the total-energy identity, and the untouched confirmation panel in the local gap-ordering clue remain unchanged.

## 6. Bounded endpoint subtraction leaves an interior obstruction

The mismatch is not confined to the outermost Farey gaps. In particular, removing bounded endpoint profiles cannot restore absolute coefficient transfer at every linear cutoff. This follows from the same positive-kernel test at the exactly anchored rational point `1/2`; no asymptotic rational-rank estimate is needed.

Let `A_0>=0` be fixed, and for each `Q` let `e_Q` be any real measurable function satisfying, almost everywhere,
\[
e_Q(1-t)=-e_Q(t),\qquad
\operatorname{supp}e_Q\subset[0,1/4]\cup[3/4,1],\qquad
\|e_Q\|_\infty\le A_0/Q.
\tag{17}
\]
It may depend arbitrarily on the genuine Farey grid. Its coefficient correction is
\[
b_{Q,j}=\sqrt{2N}\int_0^1e_Q(t)\sin(2\pi jt)\,dt.
\]
Set `m=512Q`, `q=m-1`. Uniformly over every family (17),
\[
\boxed{\liminf_{Q\to\infty}Q\sum_{j=1}^{512Q-1}
 |d_{2j}-a_j-b_{Q,j}|^2
 \ge\frac{3}{32768\pi^2}>0.}
\tag{18}
\]
Thus even a correction supported on the entire outer quarters, rather than just shrinking endpoint neighborhoods, cannot remove the critical absolute mismatch at this bandwidth. Differences of two endpoint corrections also satisfy (17), with their amplitude bounds added. This is a statement about the explicitly defined additive corrections to the coefficient vector, not every possible nonlinear change of coordinates.

To prove (18), let `B` be the largest odd integer at most `Q`. The Farey fraction immediately to the right of `1/2` is
\[
x_{N/2+1}=\frac12+\frac1{2B}.
\tag{19}
\]
Indeed any reduced `a/b>1/2` has displacement `(2a-b)/(2b)`. For odd `b` this is at least `1/(2B)`; for even `b` the positive numerator is at least two, so the displacement is at least `1/b>=1/Q>=1/(2B)` for `Q>=3`. The fraction `((B+1)/2)/B` attains the minimum and is reduced. Reflection gives `x_(N/2)=1/2` exactly.

Assume `N>=16Q`. For
\[
s\in[1/(16Q),1/(8Q)],\qquad t=1/2+s,
\]
the affine position interpolant is beyond the first rank cell to the right of `1/2`, so `t+f(t)>=1/2+1/(2B)`. Meanwhile the actual counting function is constant, `A(t)=N/2`, throughout this interval. Here `A(t)` is the counting function from (6). Consequently,
\[
h(1/2+s)\ge\frac1{2Q}-2s+\frac1{2N}
\ge\frac1{4Q}.
\tag{20}
\]
This is an interior plateau at the same physical coordinate used for both transforms.

Center the Fejér kernel at `t_*=1/2+3/(32Q)`, with radius `delta=1/(32Q)`. Equation (13) bounds its mass outside the plateau by `1/32`. Equations (9) and (20) then give
\[
\int h(t)K_m(t_*-t)\,dt
\ge\frac1Q\left(\frac14\frac{31}{32}-\frac3{32}\right)
=\frac{19}{128Q}\ge\frac1{8Q}.
\tag{21}
\]
Every point in the support of (17) has circular distance at least `1/8` from `t_*`. The pointwise kernel estimate used in (13) therefore gives `K_m(t_*-t)<=16/m` there. Since that support has measure at most `1/2`,
\[
\left|\int e_Q(t)K_m(t_*-t)\,dt\right|
\le\frac{8A_0}{mQ}.
\tag{22}
\]
The signal in (21) is of order `Q^-1`, while this entire remote correction is only `O_(A_0)(Q^-2)`.

The function `h-e_Q` is antisymmetric and has only sine modes. Repeating (8), (12), and (16) gives the explicit finite estimate, whenever `q<N/2` and `N>=16Q`,
\[
\boxed{\left(\sum_{j\le q}|d_{2j}-a_j-b_{Q,j}|^2\right)^{1/2}
\ge\frac{\sqrt N}{\sqrt m}
 \left(\frac1{8Q}-\frac{8A_0}{mQ}\right)
 -\frac{\pi^2q^2}{3N^2}\sqrt{E_Q}.}
\tag{23}
\]
As before, a negative right side is uninformative. The correction term inside parentheses and the interpolation error are negligible relative to the leading `Q^-1/2` term after normalization, by `N~3Q^2/pi^2` and (5). Squaring proves (18).

This closes the specific repair that attributes the linear-band coefficient obstruction solely to neighborhoods of `0` and `1`, then subtracts natural-size profiles supported there. It includes every fixed endpoint cutoff and every growing endpoint neighborhood that stays inside the outer quarters and obeys (17); it makes no assertion that such a subtraction is arithmetically neutral. It does not exclude a correction that also treats interior rational gaps, amplitudes outside (17), a different nonlinear transport, or a smaller fixed linear cutoff. Just as in (1), coefficient separation does not imply unequal band energies, and a relative-error obstruction additionally needs a bound on `QE_Q`. The midpoint argument supplies no improvement of the Franel exponent.

## 7. Audit and prior-art boundary

A standard-library Python audit independently enumerated the genuine grids at `Q=8,16,32,48,64,80`. It checked the two integration identities in (7) in 110 modes by directly integrating the affine interpolant and the counting discrepancy on their respective intervals. Maximum absolute discrepancies were below `7.0e-15` and `5.2e-16`. For the four orders satisfying `N>=8Q`, 260 exact rational samples checked (10); exact rational summation verified (12) for `1<=m<=500`. These checks test conventions and algebra, not the large-`Q` theorem. The analytic inequalities (9)–(16) prove that theorem; no large-order spectral panel, inferred asymptotic fit, independent adversarial approval, or Lean validation is claimed.

An independent standard-library audit checked the exact midpoint neighbor (19) at every `3<=Q<=120` (118 orders). At the 68 orders satisfying `N>=16Q`, 2,244 exact rational samples verified (20). For the antisymmetric correction equal to `1/Q` on `[0,1/4]` and `-1/Q` on `[3/4,1]`, composite Simpson integration at `Q=16,32,64` checked the remote-kernel bound (22); 15 sine-integral checks agreed with the explicit integral `(1-cos(pi j/2))/(pi j Q)` to within `5.3e-15`. These small-order checks test the midpoint anchor, sign, and correction normalization. They do not test the large-`Q` band directly; (19)–(23) provide its proof. No larger-order confirmation panel was used.

The required arithmetic bound is François Dress, *Discrépance des suites de Farey*, Journal de théorie des nombres de Bordeaux **11**(2) (1999), 345–367, [primary paper record](https://www.numdam.org/item/JTNB_1999__11_2_345_0/). The kernel and its positivity/localization are classical Fourier analysis; [NIST DLMF §1.15(iii), equations 1.15.15–1.15.17](https://dlmf.nist.gov/1.15#iii) supplies the standard normalization, while (11)–(13) give all estimates used here explicitly. M. N. Huxley, *Identities involving Farey fractions*, Proc. Steklov Inst. Math. **276** (2012), 125–139, [primary record](https://www.mathnet.ru/eng/tm3374), remains the neighboring discrete/continuous Franel-identity literature. Its full-energy identity is not a coefficientwise equality.

The novelty audit considered Farey rank/discrepancy Fourier comparisons, classical empirical/quantile inversion, and localized Fourier kernels. No stochastic empirical-quantile theorem is applied to this deterministic array. The proof uses elementary interpolation and classical positive-kernel localization; it makes no claim to a new general Fourier or quantile principle, or to literature priority. Its local mathematical delta is the explicit **genuine-Farey coefficient obstruction**, including its finite normalization and its limitation to vector distance. This is not a routine reformulation of the scalar Franel criterion: that criterion alone does not compare the two coefficient vectors at the same frequency cutoff.

The midpoint strengthening uses the elementary nearest-fraction calculation (19), not a new Farey-neighbor theorem. Targeted comparison with local rational Farey discrepancy, discrete/continuous Franel identities, and empirical/quantile remainder theory revealed no input giving (18) directly; stochastic empirical/quantile estimates require hypotheses not supplied by this deterministic array. The mathematical addition is the uniform obstruction to the specific endpoint-subtraction repair, proved by the same kernel mechanism as the original claim, rather than a separate general principle or priority claim.
