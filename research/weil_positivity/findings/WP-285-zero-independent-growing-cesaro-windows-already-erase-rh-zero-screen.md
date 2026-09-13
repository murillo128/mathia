---
id: WP-285
title: Zero-independent growing Cesàro windows already erase the favorable-RH zero screen
branch: weil_positivity
status: supported
kind: growing-memory-matched-control
claim_strength: exact favorable-RH matched control showing that positive target-independent growing memory can extract the Gamma-center scalar without spectral notches
created: 2026-09-13
related: [WP-279, WP-280, WP-281, WP-283, WP-284]
prior_art:
  - classical Bohr almost-periodic mean theory
  - classical Riemann-von Mangoldt zero counting
  - Masatoshi Suzuki, On variants of Chebyshev's conjecture, The Ramanujan Journal 68, Article 95 (2025), DOI 10.1007/s11139-025-01238-9
---

# WP-285 — Zero-independent growing Cesàro windows already erase the favorable-RH zero screen

## Claim

`WP-283` proves that a **fixed** compact-memory linear response cannot extract the Gamma-center constant from the regularized critical Chebyshev residual: a fixed entire transfer of finite exponential type does not have enough zeros to notch the `T log T` zeta-zero frequency screen. `WP-284` then gives a deliberately disallowed escape by programming a positive growing window with the zero ordinates themselves.

There is a stronger matched control. Exact notches and zero data are not needed at all.

Assume RH only as the same favorable control used in `WP-281`--`WP-284`. For fixed `a>0`, write the canonical one-state regularization as

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),
\qquad r_a(E)\to0,
\tag{1}
\]

with

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E}.
\tag{2}
\]

For `L>0` let `mu_L` be normalized Lebesgue measure on `[0,L]`, and define the trailing Cesàro readout

\[
(\mathcal C_LY)(E)
:=\frac1L\int_0^L Y(E-t)\,dt.
\tag{3}
\]

This is a positive probability average. Its transfer function is

\[
H_L(\omega)
=\frac{1-e^{-i\omega L}}{i\omega L}
=e^{-i\omega L/2}\frac{\sin(\omega L/2)}{\omega L/2},
\qquad H_L(0)=1,
\tag{4}
\]

and therefore

\[
|H_L(\omega)|\le \min\!\left(1,\frac{2}{L|\omega|}\right).
\tag{5}
\]

Since

\[
\left|\frac{a}{(i\gamma)(a+i\gamma)}\right|
\le \frac{a}{\gamma^2}
\tag{6}
\]

and the Riemann--von Mangoldt law implies

\[
\sum_\rho\frac1{|\gamma|^3}<\infty,
\tag{7}
\]

we get the uniform bound

\[
\boxed{
\|\mathcal C_LA_a\|_\infty
\le \frac{2a}{L}\sum_\rho\frac1{|\gamma|^3}
=O_a(L^{-1}).
}
\tag{8}
\]

Consequently, for **any deterministic zero-independent memory law** `L(E)` satisfying

\[
L(E)\to\infty,
\qquad
E-L(E)\to\infty,
\tag{9}
\]

one has

\[
\boxed{
(\mathcal C_{L(E)}Y_a)(E)\longrightarrow C_\Gamma
\qquad(E\to\infty),
}
\tag{10}
\]

under the favorable RH control. The memory may grow arbitrarily slowly; for example `L(E)=log(2+E)` works, and so does any slower divergent law with (9). No nontrivial-zero ordinate enters the support, weights, or scale law.

Thus the logarithmic lower bound in `WP-283` is specifically a lower bound for **exact notch interpolation**, not for asymptotic removal of the regularized zero field. More importantly, `WP-284`'s zero-coded Bernoulli convolution is not needed to demonstrate the false-positive power of positive growing memory. A generic target-independent Cesàro average already extracts the same Gamma-center scalar once RH is granted.

**Classification:** `EXACT-DERIVED + FAVORABLE-RH-MATCHED-CONTROL + POSITIVE-PROBABILITY-AVERAGING + ZERO-INDEPENDENT + UNIFORM-O(1/L)-ZERO-SUPPRESSION + CLASSICAL-BOHR-MEAN-MECHANISM + NOT-SOURCE-FORCED + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Uniform suppression of the zero field

The absolutely convergent representation (2) is the key feature supplied by the one-state regularizer of `WP-281`. Applying (3) mode by mode is justified by uniform absolute convergence and gives

\[
\mathcal C_LA_a(E)
=-\sum_\rho
\frac{aH_L(\gamma)}{(i\gamma)(a+i\gamma)}e^{i\gamma E}.
\tag{11}
\]

Using (5)--(6),

\[
|\mathcal C_LA_a(E)|
\le
\frac{2a}{L}
\sum_\rho\frac1{|\gamma|^3}.
\tag{12}
\]

The sum converges because `N(T)=O(T log T)`, so partial summation gives convergence of `sum |gamma|^{-s}` for every `s>1`. The estimate is uniform in the observation point `E`; no phase cancellation between different zero ordinates is used.

This is stronger than merely saying that each individual frequency is attenuated. Every nonzero Fourier--Bohr mode is multiplied by the sinc transfer (4), while the additional `1/|gamma|` decay from (5) makes the complete zero screen uniformly `O(1/L)`.

At the conceptual level this is just the classical Bohr-mean mechanism. A Bohr almost-periodic function has a translation-invariant mean, and long interval averages project onto its zero-frequency component. Here the coefficients are sufficiently summable to make the projection quantitative by the elementary estimate (12). No new almost-periodic theorem is being claimed.

## 2. The Gamma-center constant survives and the remainder is harmless

The constant mode is preserved exactly:

\[
\mathcal C_L C_\Gamma=C_\Gamma.
\tag{13}
\]

For the decaying remainder in (1), positivity and normalization give

\[
|\mathcal C_{L(E)}r_a(E)|
\le
\sup_{0\le t\le L(E)}|r_a(E-t)|.
\tag{14}
\]

Condition (9) implies that the whole trailing interval `[E-L(E),E]` escapes to `+infinity`. Since `r_a(u)->0`, the right-hand side of (14) tends to zero. Combining (8), (13), and (14) proves (10).

The construction is therefore substantially less tailored than `WP-284`. Its kernel shape is fixed once and for all, it is positive, normalized, contractive on `L^infinity`, and independent of the zero divisor. Only its support length grows. There is not even a preferred growth rate: any divergent `L(E)` whose left endpoint still escapes to infinity succeeds under RH.

That last freedom is itself an obstruction to interpretation. The successful extraction does not identify a distinguished geometric memory scale. It says instead that after the source has been reduced to an absolutely summable almost-periodic zero field, ordinary long-time averaging is enough to retain only the invariant scalar mode.

## 3. Matched controls: the mechanism is generic, not Riemann-specific

Nothing in the proof uses the arithmetic location of the frequencies. Let

\[
A(E)=\sum_{\lambda\in\Lambda}c_\lambda e^{i\lambda E},
\qquad 0\notin\Lambda,
\tag{15}
\]

with

\[
\sum_{\lambda\in\Lambda}\frac{|c_\lambda|}{|\lambda|}<\infty.
\tag{16}
\]

Then the same box averages satisfy

\[
\|\mathcal C_LA\|_\infty
\le \frac2L
\sum_{\lambda\in\Lambda}\frac{|c_\lambda|}{|\lambda|}
\longrightarrow0.
\tag{17}
\]

Thus any absolutely summable discrete oscillatory field with the mild weighted condition (16) is erased in exactly the same way. Replacing the zeta ordinates by a generic frequency set leaves the mechanism unchanged. This is the decisive matched control: **target independence is not arithmetic selection**.

The distinction from `WP-283` is equally sharp. That finding asks a fixed compact window to annihilate every zero frequency exactly, forcing the transfer to carry a zero divisor of density `T log T`. The present family asks only for asymptotic suppression. Its transfer has the ordinary sinc zero lattice, unrelated to zeta; the factor `1/(L|gamma|)` is already enough because the regularized source coefficients decay like `1/gamma^2`.

Therefore the `Omega(log T)` memory cost from exact notch counting cannot be used as a lower bound on the memory needed for favorable-RH Gamma extraction. In the present class the memory can diverge arbitrarily slowly.

## 4. Aggressive falsification of the route

The construction does **not** yield an independent positivity theorem. Its positivity is merely that of an averaging kernel: nonnegative inputs remain nonnegative and constants are preserved. The Weil functional is not shown to be nonnegative, no intersection form or cohomological pairing appears, and no finite-prime-plus-archimedean quadratic form is produced.

RH is also load-bearing. If a nontrivial zero has `rho=beta+i gamma` with `beta>1/2`, the corresponding critical mode is exponential rather than purely oscillatory. For `lambda=rho-1/2`, box averaging multiplies `e^{lambda E}` by

\[
\frac{1-e^{-\lambda L}}{\lambda L}.
\tag{18}
\]

For the slow memory laws relevant here, such as `L(E)=log(2+E)` or more generally `L(E)=o(E)`, a mode with `Re lambda>0` still has exponentially growing magnitude up to the subexponential `1/L(E)` factor. The averaging theorem therefore does not prove RH or make the off-critical zero field harmless. It succeeds because RH was granted first.

One could ask whether convergence of some particular growing average is itself equivalent to RH, as happens for Suzuki's canonical primitive in `WP-280`. That is a different theorem and is not asserted here. The present result deliberately avoids turning a favorable-control calculation into an arithmetic equivalence.

Nor is the box window Mathia-native merely because it is zero-independent. Nothing in Prime Circle, Prime Flute, Prime Lattice, Bost--Connes, or the current critical source forces normalized Lebesgue averaging over `[0,L(E)]`, much less selects a unique `L(E)`. Choosing this generic harmonic-analysis projection after seeing the scalar almost-periodic decomposition would be another post hoc readout.

## 5. Prior-art and novelty audit

The analytic mechanism is classical. Bohr almost-periodic functions are uniform limits of trigonometric polynomials and possess a translation-invariant mean obtained by long interval averaging. Long Cesàro windows therefore suppress nonzero Fourier--Bohr frequencies; the explicit sinc multiplier (4) is elementary Fourier analysis. The Riemann--von Mangoldt estimate used only to justify (7) is classical, and the critical source decomposition itself is inherited from `WP-281` and the weighted explicit-formula/Suzuki audit already recorded for this line.

A targeted literature search therefore does not support presenting (3)--(8) as a new harmonic-analysis or zeta theorem. The Mathia-specific content is the **frontier correction**: once the favorable-RH critical residual has been regularized into the absolutely convergent almost-periodic field of `WP-281`, positive growing-window extraction is generic enough that it does not require either zero coding or the `Omega(log T)` exact-notch memory budget of `WP-283`.

This is not classical Weil positivity, Hilbert--Pólya, Connes/trace, Sonin localization, Frobenius/cohomology, or an intersection-form construction. It is a negative matched control for claims that successful source-independent smoothing is evidence of a new geometric sign mechanism.

## Consequence for `weil_positivity`

The post-scalarization growing-memory frontier is narrower than `WP-284` left it. A future proposal does not become substantive merely by replacing a zero-programmed kernel with a zero-independent positive family and proving that its output tends to `C_Gamma` under RH. The generic Cesàro family already does exactly that, with no arithmetic frequency selection and with arbitrarily slow memory growth.

The surviving requirement is stronger: the geometry must force the averaging/coupling **before** the favorable-RH decomposition is used, and the resulting object must carry an independent sign or completion theorem rather than merely project an almost-periodic scalar field onto its invariant mode. In particular, a useful route must explain why the same intrinsic structure generates the finite-prime coefficients, the archimedean/polar terms, and the required Weil sign, or else prove a genuinely off-RH/source-side constraint. Positive normalized smoothing plus target independence is now an explicit matched control, not evidence for the primary mandate.
