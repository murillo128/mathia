---
id: WP-368
title: Bounded source-fixed Whittaker scale forms have exponential arithmetic-index tails
branch: weil_positivity
status: supported
kind: source-fixed-whittaker-positive-form-exponential-tail-obstruction
claim_strength: exact exponential tail bound for bounded common radial positive forms supported away from the cusp origin
created: 2026-09-19
related: [WP-359, WP-360, WP-366, WP-367]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Classical large-argument asymptotics of the modified Bessel function K, e.g. NIST DLMF 10.40.2
  - Classical Whittaker/Fourier expansions of real-analytic Eisenstein series
  - Classical bounded-positive-operator inequality q_A(f) <= ||A|| ||f||^2
---

# WP-368 — Bounded source-fixed Whittaker scale forms have exponential arithmetic-index tails

## Claim

`WP-366` and `WP-367` left one natural escape from the Mellin-separation obstruction: keep a **source-fixed radial scale** instead of averaging over all heights with an exactly dilation-covariant geometry. That escape also fails for a broad positive class whenever the fixed radial geometry stays a positive distance away from `Y=0` and acts by one bounded positive operator on every Whittaker coordinate.

Fix `Y_*>0`, let `mu` be a positive measure on `[Y_*,infinity)` such that

\[
M_*:=\int_{Y_*}^{\infty}Y^{-1}e^{-4\pi Y}\,d\mu(Y)<\infty,
\tag{1}
\]

and put

\[
\mathcal H_\mu=L^2([Y_*,\infty),d\mu),\qquad
F_{r,n}(Y)=K_{ir}(2\pi nY).
\tag{2}
\]

For any bounded positive operator `A>=0` on `H_mu`, define

\[
q_A(f)=\langle f,Af\rangle=\|A^{1/2}f\|^2.
\tag{3}
\]

For every fixed real spectral parameter `r`, there is a constant `C=C(r,Y_*)` such that for every integer `n>=1`,

\[
\boxed{
q_A(F_{r,n})
\le
\|A\|\frac{C^2M_*}{2\pi n}
 e^{-4\pi(n-1)Y_*}.
}
\tag{4}
\]

Hence every induced norm has the corresponding bound

\[
\|A^{1/2}F_{r,n}\|
\ll_{A,r,\mu,Y_*}
n^{-1/2}e^{-2\pi(n-1)Y_*}.
\tag{5}
\]

The same exponential suppression survives multiplication by the standard Eisenstein/Hecke coefficients, by logarithms, and by any fixed polynomial in `n`. Therefore a bounded source-fixed positive radial form supported in `Y>=Y_*>0` cannot intrinsically generate the scale-free Weil finite-prime half-density `Lambda(n)/sqrt(n)` (or `log(p)/sqrt(p)` on primes). The obstruction is independent of RH and of any inserted zero data.

**Classification:** `EXACT-DERIVED + BOUNDED-POSITIVE-RADIAL-FORM + SOURCE-FIXED-SCALE + EXPONENTIAL-TAIL-BOUND + MATCHED-CONTROL + ROUTE-CLOSURE + CLASSICAL-BESSEL-INGREDIENT + NO-GRAND-NOVELTY-CLAIM`.

## 1. Large-index Whittaker decay

For fixed real `r`, the classical large-argument expansion

\[
K_{ir}(x)=\sqrt{\frac{\pi}{2x}}e^{-x}\bigl(1+O_r(x^{-1})\bigr)
\qquad(x\to\infty)
\tag{6}
\]

implies, by enlarging the constant over the compact initial interval, that for every fixed `x_0>0` there is `C=C(r,x_0)` with

\[
|K_{ir}(x)|\le Cx^{-1/2}e^{-x}
\qquad(x\ge x_0).
\tag{7}
\]

Take `x_0=2pi Y_*`. Since `n>=1` and `Y>=Y_*`, equation (7) gives

\[
|F_{r,n}(Y)|^2
\le
\frac{C^2}{2\pi nY}e^{-4\pi nY}.
\tag{8}
\]

Therefore

\[
\begin{aligned}
\|F_{r,n}\|_{\mathcal H_\mu}^2
&\le
\frac{C^2}{2\pi n}
\int_{Y_*}^{\infty}Y^{-1}e^{-4\pi nY}\,d\mu(Y)\\
&\le
\frac{C^2}{2\pi n}
e^{-4\pi(n-1)Y_*}
\int_{Y_*}^{\infty}Y^{-1}e^{-4\pi Y}\,d\mu(Y)\\
&=
\frac{C^2M_*}{2\pi n}e^{-4\pi(n-1)Y_*}.
\end{aligned}
\tag{9}
\]

Bounded positivity now gives

\[
0\le q_A(F_{r,n})
\le \|A\|\,\|F_{r,n}\|^2,
\tag{10}
\]

which is exactly (4).

This includes a fixed-height source `mu=delta_{Y_0}`, positive finite cusp windows, and the usual locally finite radial measures restricted to a region `Y>=Y_*>0` whenever (1) holds. No dilation-homogeneity assumption is used.

## 2. Arithmetic coefficients cannot cancel the tail naturally

For the standard unitary Eisenstein normalization, the arithmetic coefficient at a prime has the form

\[
\lambda_r(p)=p^{ir}+p^{-ir},
\qquad |\lambda_r(p)|\le2,
\tag{11}
\]

and the general coefficients have divisor-type rather than exponential growth. Thus multiplying (4) or (5) by the native Eisenstein/Hecke arithmetic factor cannot turn the exponential `e^{-c n}` tail into the Weil scale

\[
\frac{\Lambda(n)}{\sqrt n},
\tag{12}
\]

which is only polynomial-logarithmic in `n` on prime powers.

More generally, any fixed finite collection of radial derivatives contributes at most a polynomial factor in `n` to the standard large-argument Whittaker asymptotic. Consequently finite-order positive Sobolev/local radial energies supported in `Y>=Y_*>0` retain an exponentially decaying arithmetic-index tail. Cancelling that decay requires an index-dependent or exponentially amplifying ingredient; such an ingredient is not supplied by the fixed positive radial geometry itself.

## 3. Cross-spectral pairings obey the same obstruction

The result is not an artefact of taking a diagonal spectral matrix element. For real `r,u`, positivity and Cauchy--Schwarz give

\[
|\langle F_{r,n},AF_{u,n}\rangle|
\le
q_A(F_{r,n})^{1/2}q_A(F_{u,n})^{1/2},
\tag{13}
\]

so the same `e^{-c n}` suppression holds for every fixed cross-spectral entry. A bounded common radial operator therefore cannot hide the required prime half-density in off-diagonal spectral correlations while retaining one fixed cusp scale.

## 4. Matched controls and falsification

The obstruction is deliberately tested against the obvious escape hatches.

First, it is **not prime-specific**: the estimate holds for every integer Fourier index `n`. Primes inherit the suppression rather than causing it. Second, moving the fixed window closer to the cusp origin changes only the constant `c=4pi Y_*`; every fixed `Y_*>0` is still exponentially suppressing at sufficiently large `n`. Third, multiplying by any fixed power of `n`, divisor-type Hecke coefficient, or logarithm cannot compensate for the exponential tail.

The only direct way to keep `K_{ir}(2pi nY)` out of its exponentially decaying regime for arbitrarily large `n` is to let the relevant source heights approach `0` as `n` grows. That is no longer one source-fixed positive cusp window. If instead one globalizes all scales with exact dilation homogeneity, `WP-366` and `WP-367` apply: the `nY` incidence separates into Mellin/Rankin--Selberg data and the critical positive diagonal is null or divergent.

This gives a clean two-sided narrowing of the current Whittaker route:

- exact scale covariance over all heights loses the incidence by Mellin separation (`WP-366`, `WP-367`);
- one bounded positive geometry at a fixed scale away from `0` keeps the incidence but suppresses large arithmetic indices exponentially (this finding).

A surviving construction must therefore violate at least one of those premises in a mathematically intrinsic way, for example through scale mixing that reaches `Y=0`, an operator-valued/global coupling across Fourier modes, or a genuinely cohomological/intersection structure. Merely choosing another fixed cusp height or bounded radial kernel is not enough.

## 5. Prior-art and novelty audit

The analytic ingredient is classical: large-argument exponential decay of `K`-Bessel/Whittaker functions is standard, as are the Eisenstein Fourier coefficients. The bounded-positive-operator estimate is elementary functional analysis. No novelty is claimed for any of those facts.

The branch-specific contribution is the **no-go synthesis**: the source-fixed-scale escape explicitly left open by `WP-366`/`WP-367` is incompatible with the scale-free Weil finite-prime half-density throughout the bounded common-positive radial class supported away from `Y=0`. A bounded prior-art search found the classical ingredients and standard automorphic applications of Whittaker decay, but no source establishing this exact Mathia/Weil route-closure statement. It should therefore be treated as a derived obstruction assembled from classical ingredients, not as a claim of a new standalone theorem in the literature.

## Scope

This finding does **not** rule out:

- positive geometries whose support genuinely reaches `Y=0` and whose domain controls that singular limit;
- unbounded operators with a canonical geometric origin and a proved positive closed form;
- arithmetic-index-dependent source heights forced independently by geometry rather than chosen to fit Weil weights;
- operators coupling different Fourier indices before positivity is taken;
- global cohomological, intersection-theoretic, or boundary structures not representable as one bounded common radial operator.

Those are materially different mechanisms. Any such proposal must still explain intrinsically both the finite-prime term and the archimedean/global counterterms and must survive the independent-positivity and prior-art gates of the `weil_positivity` mandate.