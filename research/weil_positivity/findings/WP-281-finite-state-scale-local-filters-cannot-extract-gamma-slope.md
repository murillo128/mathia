---
id: WP-281
title: Finite-state scale-local filters cannot extract the Gamma slope from the critical Chebyshev residual
branch: weil_positivity
status: supported
kind: finite-state-archimedean-extraction-obstruction
claim_strength: exact conditional no-go under the favorable RH control for every fixed finite-dimensional stable logarithmic-translation-invariant linear response
created: 2026-09-13
related: [WP-278, WP-279, WP-280]
prior_art:
  - weighted von Mangoldt explicit formula at the critical half-density
  - Masatoshi Suzuki, On variants of Chebyshev's conjecture, The Ramanujan Journal 68, Article 95 (2025), DOI 10.1007/s11139-025-01238-9
  - classical Bohr almost-periodic-function theory
  - classical finite-dimensional linear-systems realization and rational transfer-function theory
---

# WP-281 — Finite-state scale-local filters cannot extract the Gamma slope from the critical Chebyshev residual

## Claim

`WP-279` rules out successive **scalar** high-energy renormalization of the critical Mangoldt tangent as a route to the Gamma layer, while `WP-280` shows that the canonical global logarithmic primitive does recover the central Gamma slope only through an RH-equivalent limit. A remaining natural escape is to keep the critical source in logarithmic scale and replace scalar normalization by a fixed finite-dimensional boundary system: a source-independent stable ODE or finite-state linear response that processes nearby scales before a scalar readout is taken.

That entire scale-local finite-state class fails even under the most favorable matched control, namely RH itself.

Let

\[
\psi_{1/2}(x)
:=\sum_{n\le x}^{\prime}\frac{\Lambda(n)}{\sqrt n},
\qquad
G(E):=\psi_{1/2}(e^E)-2e^{E/2},
\tag{1}
\]

and set

\[
C_\Gamma:=-\frac{\zeta'}{\zeta}\!\left(\frac12\right)
=\frac12\left(\psi\!\left(\frac14\right)-\log\pi\right).
\tag{2}
\]

Fix any `E_0>0`. For any fixed `a>0`, pass `G` through the one-state stable causal system

\[
Y_a'(E)+aY_a(E)=aG(E),
\qquad Y_a(E_0)=0.
\tag{3}
\]

Assume RH only as a **favorable control**. Then

\[
Y_a(E)=C_\Gamma+A_a(E)+r_a(E),
\qquad r_a(E)\to0,
\tag{4}
\]

where

\[
A_a(E)
=-\sum_{\rho=1/2+i\gamma}
\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E}
\tag{5}
\]

is a nonconstant uniformly Bohr almost-periodic function. The series in (5) is absolutely and uniformly convergent because

\[
\sum_\rho \frac1{1+\gamma^2}<\infty.
\tag{6}
\]

A nonconstant Bohr almost-periodic function cannot have a limit at `+infinity`. Hence

\[
\boxed{\lim_{E\to\infty}Y_a(E)\text{ does not exist, even under RH}.}
\tag{7}
\]

The obstruction is not special to the one-pole smoother. Append any fixed exponentially stable finite-dimensional scalar-input/scalar-output linear time-invariant system with transfer function `H`. If `H(0)\ne0`, so that the constant Gamma mode is retained, its asymptotic zero-frequency-preserving output contains Fourier--Bohr coefficients

\[
-\frac{aH(i\gamma)}{(i\gamma)(a+i\gamma)}.
\tag{8}
\]

Convergence would force `H(i\gamma)=0` for every nontrivial-zero ordinate. But a nonzero finite-dimensional transfer function is rational and therefore has only finitely many zeros, whereas zeta has infinitely many distinct nontrivial-zero ordinates. Thus no such finite-state response can suppress the zero oscillations while retaining the central Gamma mode.

This closes a genuine part of the non-scalar escape left by `WP-279`--`WP-280`: **finite-dimensional logarithmic-scale-local linear boundary dynamics, including every passive finite-state subclass, cannot isolate the archimedean center from the critical arithmetic source.** Any surviving mechanism must change category to an infinite-dimensional/nonrational response, a genuinely scale-nonlocal operation, or a global finite--archimedean coupling before the critical zero modes are scalarized.

**Classification:** `EXACT-DERIVED + DECISIVE-NEGATIVE-FOR-FINITE-STATE-SCALE-LOCAL-GAMMA-EXTRACTION + FAVORABLE-RH-MATCHED-CONTROL + ALMOST-PERIODIC-ZERO-REMAINDER + RATIONAL-TRANSFER-NO-GO + PRIOR-ART-CLASSICALIZED-INGREDIENTS + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Exact critical residual in logarithmic scale

The weighted Perron/explicit formula underlying `WP-280` can be written, with the usual half-weight convention at prime-power jumps, as

\[
\psi_{1/2}(x)
=2\sqrt x
+C_\Gamma
-\sum_\rho^{*}\frac{x^{\rho-1/2}}{\rho-1/2}
+\sum_{k\ge1}\frac{x^{-2k-1/2}}{2k+1/2}.
\tag{9}
\]

The star denotes the standard symmetric ordering of the nontrivial-zero sum. Formula (9) is simply the residue expansion of

\[
-\frac{\zeta'}{\zeta}\!\left(s+\frac12\right)\frac{x^s}{s}.
\tag{10}
\]

The pole at `s=1/2` gives `2 sqrt(x)`, the pole at `s=0` gives `C_Gamma`, a nontrivial zero `rho` gives the coefficient `-x^{rho-1/2}/(rho-1/2)`, and the trivial zero `-2k` gives the final positive decaying term in (9).

With `x=e^E`, (9) becomes

\[
G(E)
=C_\Gamma
-\sum_\rho^{*}\frac{e^{(\rho-1/2)E}}{\rho-1/2}
+T(E),
\tag{11}
\]

where, for every fixed `E>=E_0>0`,

\[
T(E)=\sum_{k\ge1}
\frac{e^{-(2k+1/2)E}}{2k+1/2}
\tag{12}
\]

converges absolutely and decays exponentially as `E->infinity`.

This representation makes the distinction from `WP-280` explicit. The global primitive used there introduces a second zero denominator and then divides by the growing interval length `E`. Here no growing averaging window is allowed: the candidate mechanism has a fixed finite amount of state and coefficients independent of the target zero divisor.

## 2. The minimal stable local response leaves a nonconstant almost-periodic zero field

The solution of (3) is

\[
Y_a(E)
=a\int_{E_0}^E e^{-a(E-u)}G(u)\,du.
\tag{13}
\]

A constant input `C_Gamma` contributes

\[
C_\Gamma\bigl(1-e^{-a(E-E_0)}\bigr)
=C_\Gamma+O(e^{-aE}).
\tag{14}
\]

For a mode `e^{\lambda E}`, the system transfer is

\[
\frac{a}{a+\lambda},
\tag{15}
\]

up to an exponentially decaying initial-condition transient. Under RH every nontrivial zero has

\[
\rho-\frac12=i\gamma,
\tag{16}
\]

so applying (13) to the zero term in (11) gives

\[
-\frac{a}{(i\gamma)(a+i\gamma)}e^{i\gamma E}
+O_\gamma(e^{-a(E-E_0)}).
\tag{17}
\]

The summed transient coefficients in (17) are absolutely summable. The trivial-zero input (12) produces only exponentially decaying output; if one of its decay rates happens to equal `a`, the corresponding contribution is of the harmless form `(E-E_0)e^{-a(E-E_0)}`. Consequently (4)--(5) follow.

The standard zero-counting estimate

\[
N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi}-\frac{T}{2\pi}+O(\log T)
\tag{18}
\]

implies (6). Therefore (5) is an absolutely and uniformly convergent exponential series. It is a Bohr almost-periodic function, and its Fourier--Bohr coefficient at every distinct zero ordinate `gamma` is nonzero (with zero multiplicity simply multiplying that coefficient).

There is a short self-contained reason why such a function cannot converge at `+infinity`. If an almost-periodic function `A` satisfied `A(E)->L`, then for any fixed `s` and any `epsilon>0`, choose an arbitrarily large `epsilon`-almost period `tau` with `s+tau` already in the tail where `|A-L|<epsilon`. Then

\[
|A(s)-L|
\le |A(s)-A(s+\tau)|+|A(s+\tau)-L|
<2\epsilon.
\tag{19}
\]

Thus `A` would equal `L` identically. Since (5) has nonzero nonzero-frequency Fourier--Bohr coefficients, it is not constant. Equations (4) and (19) prove (7).

This is deliberately a favorable falsification. The argument does not assume RH to infer a new arithmetic conclusion. Instead it grants the target hypothesis and asks whether the proposed finite-state local extraction would then expose the known Gamma constant. It still does not.

## 3. Every fixed finite-dimensional stable linear repair is rational and cannot kill the infinite zero spectrum

The one-state smoother is only a regularizer that makes the critical zero field absolutely summable. Suppose a second fixed finite-dimensional stable linear system is allowed to process `Y_a`. In state-space form it has

\[
Z'(E)=AZ(E)+BY_a(E),
\qquad
W(E)=RZ(E)+DY_a(E),
\tag{20}
\]

with the spectrum of `A` in the open left half-plane. Its scalar transfer function is

\[
H(s)=D+R(sI-A)^{-1}B,
\tag{21}
\]

a rational function with no poles on the imaginary axis.

The constant input mode is multiplied by `H(0)`. A response intended to retain the Gamma-center scalar must therefore have `H(0)\ne0`; after an irrelevant fixed rescaling one may impose `H(0)=1`.

Because the series (5) is uniformly absolutely convergent, the stable system may be applied mode by mode. Its almost-periodic part has coefficients

\[
-\frac{aH(i\gamma)}{(i\gamma)(a+i\gamma)}.
\tag{22}
\]

If the final scalar output converged, the same almost-periodic-limit argument would force every nonzero-frequency coefficient in (22) to vanish. Therefore

\[
H(i\gamma)=0
\qquad
\text{for every distinct nontrivial-zero ordinate }\gamma.
\tag{23}
\]

There are infinitely many such ordinates. A nonzero rational function has only finitely many zeros. Hence (23) forces `H` to be identically zero, contradicting `H(0)\ne0`.

The intermediate state may be arbitrarily non-scalar and may have any fixed finite dimension. Once the input and desired Gamma readout are scalar, its input-output transfer is still rational, so hidden finite-dimensional mixing does not evade the obstruction. Passive, contractive, positive-real, or energy-dissipating finite-state boundary systems are strict subclasses and therefore fail a fortiori.

## 4. Matched controls and boundaries of the no-go

The infinite zero divisor is essential. If the residual contained only finitely many oscillatory frequencies, one could choose a rational filter whose numerator vanishes at those frequencies while keeping `H(0)\ne0`. The obstruction is therefore not the vacuous statement that local filtering never removes oscillations; it is the incompatibility between **fixed finite state** and the infinite nontrivial-zero spectrum.

Conversely, an infinite-dimensional transfer function can have infinitely many prescribed zeros. This finding does not rule out such a response. But a transfer function constructed specifically to vanish at the zeta zero ordinates would merely insert the target divisor and violates the line's independence requirement. A surviving infinite-dimensional candidate must derive its annihilation or sign structure from independent geometry before the zero data are inspected.

The global operation of `WP-280` also evades this theorem. Dividing the logarithmic primitive by `E` is not a fixed logarithmic-translation-invariant finite-state response: its effective averaging window grows with `E`. Under RH that global averaging sends each bounded zero oscillation to zero. Suzuki's theorem then supplies the sharper obstruction: existence of the resulting exact Gamma-slope limit is itself equivalent to RH. Thus `WP-280` and the present result meet cleanly at the local/nonlocal boundary rather than duplicating one another.

Nonlinear readouts are not covered merely because they use finitely many internal variables. Squaring, taking absolute values, determinants, or other nonlinear energies can change the frequency support and may destroy the linear Gamma mode at the same time. They require their own exact bridge and sign audit. This result closes the fixed **linear** finite-state logarithmic-scale response class, not every conceivable finite-dimensional nonlinear geometry.

The theorem also does not assert that the Gamma factor itself is generated by the finite-prime source. Equation (2) uses the completed-zeta functional equation exactly as in `WP-280`. The point is narrower: once that correct scalar is present in the critical arithmetic residual, finite-state local dynamics still cannot separate it from the nontrivial-zero field.

## 5. Prior-art and novelty audit

All ingredients are classical. Formula (9) is the weighted von Mangoldt explicit formula used in the same critical regime by Suzuki and already audited in `WP-280`. The identity (2) is the central logarithmic derivative of the completed Riemann functional equation. The estimate (18) is the Riemann--von Mangoldt zero-counting law. Absolute exponential series are standard Bohr almost-periodic functions, and finite-dimensional LTI systems have rational transfer functions.

No novelty is claimed for any of those facts, nor for the generic observation that a rational filter cannot have infinitely many prescribed zeros. A targeted prior-art check found the relevant almost-periodic and finite-dimensional transfer-function facts as standard theory, not a distinct theorem about the weighted Chebyshev residual. The Mathia-specific delta is the exact combination forced by the current frontier: after the canonical one-state regularization, the RH critical-zero remainder becomes a uniformly almost-periodic field whose every zeta-zero frequency survives with nonzero amplitude, so **finite-state scale-local boundary processing cannot realize the non-scalar Gamma-extraction escape left open by `WP-279`**.

This should therefore be treated as a derived obstruction and category boundary, not as a new theorem about zeta or control theory.

## Consequence for `weil_positivity`

The source-side hierarchy is now more sharply partitioned. `WP-278` obtains the pole continuum from the critical Mangoldt atoms by a local high-energy tangent. `WP-279` shows that scalar tangent refinement hits the nontrivial-zero layer before Gamma. `WP-280` shows that the canonical global primitive can recover the Gamma-center slope only through an RH-equivalent asymptotic. The present result rules out the natural fixed finite-state compromise between those two extremes: a logarithmic-scale-local boundary system cannot average away the infinite critical zero field while preserving the center mode.

Accordingly, the remaining archimedean/sign route must contain genuinely new structure. It must use an independently forced infinite-dimensional/nonrational response, a global scale-nonlocal operation not equivalent to the Suzuki criterion, or a finite--archimedean operator/cohomological coupling formed before the zero modes become the scalar residual (11). Merely adding more finite boundary states, stable resonators, passive channels, or fixed rational filters cannot supply the missing global Weil positivity mechanism.
