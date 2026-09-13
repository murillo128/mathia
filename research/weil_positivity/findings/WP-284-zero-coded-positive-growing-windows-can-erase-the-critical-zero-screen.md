---
id: WP-284
title: Zero-coded positive growing windows can erase the critical zero screen
branch: weil_positivity
status: supported
kind: target-coded-growing-memory-positive-control
claim_strength: exact favorable-RH matched control showing positive growing-memory scalar filters can erase the critical zero screen when their delays are explicitly programmed from the zeta zero ordinates
created: 2026-09-13
related: [WP-280, WP-281, WP-282, WP-283]
prior_art:
  - classical finite Bernoulli convolutions and products of characteristic functions
  - classical Riemann-von Mangoldt zero counting
  - classical partial summation for reciprocal zero ordinates
---

# WP-284 — Zero-coded positive growing windows can erase the critical zero screen

## Claim

`WP-283` proves that no **fixed** bounded compact-memory scalar response preserving the constant mode can remove the critical zeta-zero screen, and that a cutoff-dependent positive window which notches all simple critical ordinates through frequency `T` must have memory horizon at least of order `log T`. That leaves a deliberately dangerous escape: perhaps positivity together with growing memory is already restrictive enough to count as geometric evidence.

It is not. There is an elementary matched control showing that **positive growing-memory filters are programmable enough to erase any prescribed finite frequency set exactly while preserving DC**.

For every positive target frequency `gamma`, define the positive probability measure

\[
\nu_\gamma:=\frac12\left(\delta_0+\delta_{\pi/\gamma}\right).
\tag{1}
\]

For the positive ordinates `gamma<=T` of the nontrivial zeta zeros, counted with multiplicity, set

\[
\mu_T:=\underset{0<\gamma\le T}{*}\,\nu_\gamma.
\tag{2}
\]

Then `mu_T` is a positive probability measure supported in `[0,L_T]`, where

\[
L_T=\pi\sum_{0<\gamma\le T}\frac1\gamma,
\tag{3}
\]

and its logarithmic-translation transfer is

\[
H_T(\omega)
=\int e^{-i\omega t}\,d\mu_T(t)
=\prod_{0<\gamma\le T}
\frac{1+e^{-i\pi\omega/\gamma}}2.
\tag{4}
\]

Consequently

\[
H_T(0)=1,
\qquad
|H_T(\omega)|\le1\quad(\omega\in\mathbb R),
\qquad
H_T(\pm\gamma)=0
\quad(0<\gamma\le T).
\tag{5}
\]

The first two properties are genuine positivity/passivity controls: constants are retained exactly and no real-frequency mode is amplified. The last property is also exact, because the factor indexed by the target ordinate `gamma` equals `(1+e^{-i\pi})/2=0` at `+gamma` and `(1+e^{i\pi})/2=0` at `-gamma`.

The price is explicit target insertion. The delay `pi/gamma` is manufactured from the very zero ordinate that the filter is intended to remove. Thus (1)--(5) are **not** a candidate Mathia mechanism and do not satisfy the research mandate. They are a falsifying control: positivity and scale-nonlocality alone cannot distinguish a source-forced geometric completion from a zero-coded notch filter.

Moreover the required memory is quantitatively modest enough that this is a serious control rather than an unconstrained infinite-horizon tautology. Riemann--von Mangoldt plus partial summation gives

\[
\sum_{0<\gamma\le T}\frac1\gamma
=\frac{1}{4\pi}(\log T)^2+O(\log T),
\tag{6}
\]

hence

\[
\boxed{
L_T=\frac14(\log T)^2+O(\log T).
}
\tag{7}
\]

So `WP-283`'s universal positive-window lower bound `L_T=Omega(log T)` is compatible with an explicit zero-coded positive construction of size `O((log T)^2)`. No optimality between those scales is claimed.

Finally, under the same favorable RH assumption used in `WP-281`--`WP-283`, applying this family to the canonically regularized critical source actually extracts the Gamma-center scalar asymptotically. If

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),
\qquad r_a(E)\to0,
\tag{8}
\]

with

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E},
\tag{9}
\]

then, choosing the observation energy `E=T`,

\[
\boxed{
(\mathcal F_{\mu_T}Y_a)(T)\longrightarrow C_\Gamma.
}
\tag{10}
\]

Thus even successful positive extraction of the correct central Gamma scalar would be weak evidence unless the kernel is forced independently of the target zero data.

**Classification:** `EXACT-DERIVED + FAVORABLE-RH-MATCHED-CONTROL + POSITIVE-PROBABILITY-GROWING-MEMORY + ZERO-CODED-TARGET-INSERTION + DECISIVE-CANONICITY-CONTROL + CLASSICAL-INGREDIENTS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. A positive two-tap notch at one prescribed frequency

For a scalar logarithmic-translation readout

\[
(\mathcal F_\mu Y)(E)
:=\int Y(E-t)\,d\mu(t),
\tag{11}
\]

the transfer at frequency `omega` is

\[
H_\mu(\omega)=\int e^{-i\omega t}\,d\mu(t).
\tag{12}
\]

The measure (1) is the law of a Bernoulli variable taking values `0` and `pi/gamma` with equal probability. Its transfer is

\[
H_\gamma(\omega)
=\frac{1+e^{-i\pi\omega/\gamma}}2
=e^{-i\pi\omega/(2\gamma)}
\cos\frac{\pi\omega}{2\gamma}.
\tag{13}
\]

It is a positive normalized average, not a signed cancellation inserted at the level of measure weights. Yet its characteristic function vanishes at `omega=+-gamma`. The cancellation occurs between the two phase-shifted copies of the input after a half-period delay.

For finitely many target frequencies, convolution of the corresponding probability measures multiplies their transfers. Equation (2) therefore remains a probability measure and (4)--(5) follow immediately. Repeated zero ordinates merely repeat a factor; that is unnecessary for annihilating the associated frequency but convenient because the resulting memory estimate can use the standard zero-counting function with multiplicity directly.

This already defeats a possible overinterpretation of `WP-283`: **positivity of the time-domain averaging measure does not forbid a dense family of frequency notches once the support is allowed to grow with the target set.**

## 2. The exact memory cost is quadratic logarithmic for the zero-coded product

Let `N(T)` count positive nontrivial zeta zeros through height `T`, with multiplicity. Riemann--von Mangoldt gives

\[
N(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T).
\tag{14}
\]

Stieltjes partial summation yields, after absorbing the fixed lower endpoint into the constant,

\[
\begin{aligned}
\sum_{0<\gamma\le T}\frac1\gamma
&=\frac{N(T)}T+\int^{T}\frac{N(t)}{t^2}\,dt+O(1)\\
&=\frac{1}{4\pi}(\log T)^2+O(\log T).
\end{aligned}
\tag{15}
\]

Multiplying by `pi` proves (7). The support of a convolution of measures supported in `[0,l_j]` is contained in `[0,sum l_j]`, so no cancellation or signed support bookkeeping enters this estimate.

This gives an explicit upper control complementary to `WP-283`. That finding proves that any normalized positive compact window able to notch the required `gg T log T` distinct critical frequencies must have `L_T >= c log T`; the present target-coded family achieves all zeta ordinates through `T`, counted with multiplicity in its construction, using `L_T=O((log T)^2)`. The logarithmic gap is left open.

The raw atomic expansion of `mu_T` can contain exponentially many atoms, but that is irrelevant to the mathematical control: the convolution/product representation (2)--(4) is exact. No claim of computational efficiency is being made.

## 3. Under favorable RH the complete zero screen is uniformly suppressed

Assume RH only for this matched control, exactly as in `WP-281`--`WP-283`, so that the nontrivial-zero contribution to the critical source is the bounded almost-periodic field (9). The coefficients obey

\[
\left|
\frac{a}{(i\gamma)(a+i\gamma)}
\right|
=\frac{a}{|\gamma|\sqrt{a^2+\gamma^2}}
\le\frac{a}{\gamma^2}.
\tag{16}
\]

Because `H_T(gamma)=0` for every ordinate through `T` and `|H_T(gamma)|<=1` above the cutoff,

\[
\|\mathcal F_{\mu_T}A_a\|_\infty
\le
a\sum_{|\gamma|>T}\frac1{\gamma^2}.
\tag{17}
\]

Another partial-summation consequence of (14) is

\[
\sum_{\gamma>T}\frac1{\gamma^2}
=O\left(\frac{\log T}{T}\right),
\tag{18}
\]

so

\[
\|\mathcal F_{\mu_T}A_a\|_\infty
=O_a\left(\frac{\log T}{T}\right)
\longrightarrow0.
\tag{19}
\]

The constant survives exactly because `H_T(0)=1`:

\[
\mathcal F_{\mu_T}C_\Gamma=C_\Gamma.
\tag{20}
\]

For the remainder, positivity and normalization give

\[
|\mathcal F_{\mu_T}r_a(E)|
\le
\sup_{0\le t\le L_T}|r_a(E-t)|.
\tag{21}
\]

Set `E=T`. By (7), `L_T=o(T)`, hence `T-L_T->+infinity`. Since `r_a(E)->0`, the entire moving interval `[T-L_T,T]` eventually lies in the tail on which `r_a` is uniformly smaller than any prescribed epsilon. Therefore the right-hand side of (21) tends to zero. Combining (19)--(21) proves (10).

Nothing here proves RH. RH is granted only to put the source into the pure-frequency favorable form already used by the predecessor no-go findings. The construction is expressly forbidden as a solution because the zero ordinates are inserted into the filter itself.

## 4. Adversarial controls and exact boundary

The construction is positive in a strong elementary sense. Every `mu_T` is a probability measure, so the readout is an average of delayed source values. There are no negative measure weights, no arbitrary subtraction constant, and no growth in total variation. Thus rejecting the example merely because its transfer uses phase cancellation would incorrectly reject ordinary positive averaging as well.

What invalidates it as a Mathia mechanism is **source selection**. The support contains the delays `pi/gamma` chosen from the zeta zero divisor. Replacing the zeta ordinates by any other finite prescribed frequency multiset produces the same construction verbatim. The filter therefore explains nothing arithmetic or geometric about why those particular frequencies should be annihilated.

This is the relevant matched control for a future growing-memory proposal. A candidate that merely exhibits

\[
\mu_T\ge0,
\qquad
\mu_T([0,L_T])=1,
\qquad
L_T\to\infty,
\qquad
\mathcal F_{\mu_T}Y_a\to C_\Gamma
\tag{22}
\]

has not crossed the substantive gate. To distinguish itself from (1)--(4), it needs an **independent source-forcing theorem** deriving its support, weights, or evolution from the Mathia-native geometry without using nontrivial-zero data or an equivalent RH/explicit-formula target condition.

The control also does not close the whole growing-memory route. A source-fixed family may have support dictated by prime geometry, an archimedean boundary law, a semigroup, or an operator/cohomological construction and only subsequently be shown to suppress the zero screen. Such a theorem would be mathematically different because the notch set would be a consequence rather than input. Likewise nonlinear pre-scalarization couplings remain outside the convolution model.

Nor does the `O((log T)^2)` construction prove the `Omega(log T)` lower bound in `WP-283` sharp. Improving either side is a separate approximation/entire-function problem and, by itself, would not produce Weil positivity.

## 5. Prior-art and novelty audit

No novelty is claimed for the filter construction itself. A two-point probability measure has the characteristic function (13), convolution multiplies characteristic functions, and finite products of such factors belong to the elementary theory of Bernoulli sums/finite Bernoulli convolutions. The zero-counting and partial-summation inputs in (14)--(18) are classical.

The Mathia-specific result is the **matched-control boundary** exposed by combining those elementary facts with the exact source reduction in `WP-281` and the compact-memory lower bound in `WP-283`: a completely positive normalized family with only `O((log T)^2)` growing memory can asymptotically recover the same Gamma-center scalar if one is allowed to program the family with the zero ordinates. Therefore positivity, bounded gain, DC preservation, growing memory, and even successful Gamma extraction together are still insufficient evidence of a geometric Weil mechanism.

This is not classical Weil positivity, Hilbert--Polya, Connes/trace, Sonin localization, Frobenius/cohomology, or an intersection-form construction. It does not improve a zeta theorem. Its role is adversarial: it supplies an explicit false-positive mechanism that any source-native candidate must beat.

## Consequence for `weil_positivity`

The surviving post-scalarization linear frontier is narrower in a different sense than a new no-go theorem. `WP-283` forces any positive compact-window escape to become scale-nonlocal. The present control shows that **scale-nonlocal positivity is itself too permissive**: once the window may depend on the cutoff, exact notch programming is easy while retaining positive normalized averaging.

Accordingly, future growing-memory claims should not be judged primarily by whether they are positive or whether they numerically/analytically remove the zero screen. The decisive question is whether the memory law is forced independently by the Mathia construction and then, without zero insertion, yields the finite-prime and archimedean structure required by the Weil criterion. A kernel whose delays or weights are reverse-engineered from the zero divisor is a control, not progress toward the primary mandate.