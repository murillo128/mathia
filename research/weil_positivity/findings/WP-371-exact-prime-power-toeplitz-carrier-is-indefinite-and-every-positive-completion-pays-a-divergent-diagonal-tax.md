---
id: WP-371
title: Exact prime-power Toeplitz carrier is indefinite and every positive completion pays a divergent diagonal tax
branch: weil_positivity
status: supported
kind: prime-power-toeplitz-positive-completion-obstruction
claim_strength: exact local classification of translation-invariant positive scalar completions of the critical prime-power carrier, with a divergent global lower bound on the required diagonal mass
created: 2026-09-19
related: [WP-369, WP-370]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - classical Poisson kernel and Herglotz/Toeplitz positivity on the circle
  - Weil/Guinand explicit formula for the Riemann zeta function
  - Carneiro and Milinovich, On Littlewood's estimate for the modulus of the zeta function on the critical line, 2024
  - Chirre and Molero, Explicit conditional bounds for zeta(s) at the edge of the critical strip, 2026
---

# WP-371 — Exact prime-power Toeplitz carrier is indefinite and every positive completion pays a divergent diagonal tax

## Claim

`WP-370` leaves a genuinely non-diagonal escape open: keep the critical prime-power amplitudes linear until after a source-forced operator couples different translates, and only then invoke positivity. The most canonical translation-invariant version of that idea has an exact obstruction.

Let `U` be the bilateral unitary shift, or equivalently multiplication by `e^{i theta}` on `L^2(S^1)`. For `0<r<1`, define the centered prime-ray operator

\[
C_r:=\sum_{k\ge1}r^k(U^k+U^{-k}).
\tag{1}
\]

The series converges in operator norm. At the critical prime scale

\[
r=r_p:=p^{-1/2},
\tag{2}
\]

multiplication by `log p` gives exactly the symmetric prime-power coefficient pattern

\[
(\log p)C_{r_p}
 =\sum_{k\ge1}\frac{\log p}{p^{k/2}}(U^k+U^{-k}).
\tag{3}
\]

Thus (3) is the canonical translation-invariant Toeplitz carrier one would like to place inside a positive boundary form before scalarization.

It is not positive. Its Fourier symbol is

\[
c_r(\theta)
 =2\sum_{k\ge1}r^k\cos(k\theta)
 =\frac{1-r^2}{1-2r\cos\theta+r^2}-1
 =\frac{2r(\cos\theta-r)}{1-2r\cos\theta+r^2}.
\tag{4}
\]

Hence

\[
\min_{\theta}c_r(\theta)=c_r(\pi)=-\frac{2r}{1+r},
\qquad
\max_{\theta}c_r(\theta)=c_r(0)=\frac{2r}{1-r}.
\tag{5}
\]

More strongly, among **all scalar diagonal completions preserving every nonzero Fourier coefficient in (1)**,

\[
T_{r,a}:=aI+C_r,
\tag{6}
\]

one has the exact equivalence

\[
\boxed{
T_{r,a}\succeq0
\quad\Longleftrightarrow\quad
a\ge a_{\min}(r):=\frac{2r}{1+r}.
}
\tag{7}
\]

The extremal completion is just the centered Poisson kernel shifted until its minimum touches zero. Therefore at the Weil critical scale every local positive Toeplitz completion must introduce at least

\[
\boxed{
(\log p)a_{\min}(p^{-1/2})
 =\frac{2\log p}{\sqrt p+1}
}
\tag{8}
\]

of zero-frequency/diagonal mass. Globally,

\[
\boxed{
\sum_p\frac{2\log p}{\sqrt p+1}=\infty.
}
\tag{9}
\]

Consequently the canonical Poisson/Herglotz positivity of the prime-power shift does **not** supply Weil positivity for free. The exact arithmetic carrier is the *centered*, sign-indefinite part. Restoring local positivity necessarily adds a positive diagonal term whose total mass diverges over the primes. Removing that term again is a subtraction performed outside the local positivity theorem.

This does not rule out a genuinely global finite--archimedean operator whose assembly cancels or quotients the diagonal direction **before** the sign theorem is applied. It does rule out the simpler proposal that the symmetric critical prime-power coefficients themselves are the off-diagonal Fourier coefficients of a canonical positive translation-invariant local form with no further arithmetic counterterm.

**Classification:** `EXACT-DERIVED + PRIME-POWER-TRANSLATION + TOEPLITZ/HERGLOTZ + POISSON-KERNEL + CRITICAL-P^{-1/2}-COEFFICIENTS + EXACT-MINIMAL-POSITIVE-COMPLETION + DIVERGENT-DIAGONAL-TAX + NEGATIVE/NARROWING + NO-ZERO-DATA + CLASSICAL-INGREDIENTS + NO-GRAND-NOVELTY-CLAIM`.

## 1. The critical prime-power coefficients are a centered Poisson kernel

For `|r|<1`, the classical Poisson kernel has Fourier series

\[
P_r(\theta)
 =\frac{1-r^2}{1-2r\cos\theta+r^2}
 =1+2\sum_{k\ge1}r^k\cos(k\theta).
\tag{10}
\]

Functional calculus for a unitary `U` gives the positive operator

\[
P_r(U)
 =(1-r^2)(I-rU)^{-1}(I-rU^*)^{-1}
 \succeq0.
\tag{11}
\]

Equation (10) implies the exact operator identity

\[
P_r(U)=I+C_r.
\tag{12}
\]

The distinction between `P_r` and `C_r` is the whole issue. The nonzero Fourier coefficients of `C_r` are exactly `r^{|k|}`. Setting `r=p^{-1/2}` gives the critical prime-power half-density in the Riemann--Weil formula before the test function is evaluated. The positive Poisson kernel contains the same off-diagonal coefficients, but also contains an additional constant Fourier coefficient equal to `1`.

For a vector `g` in the spectral realization and the unitary translation

\[
(U_pg)(t)=e^{it\log p}g(t),
\tag{13}
\]

we have

\[
\langle g,C_{r_p}g\rangle
 =\sum_{k\ge1}p^{-k/2}
 \left(
 \langle g,U_p^kg\rangle+
 \langle g,U_p^{-k}g\rangle
 \right).
\tag{14}
\]

The matrix coefficients on the right are the autocorrelation samples at `\pm k\log p`. Multiplying by `log p` therefore gives exactly the local prime-power coefficient pattern tested by a Weil autocorrelation. No zero divisor or RH assumption is used to obtain (14).

But (4)--(5) show that centering the Poisson kernel at its natural zero Fourier mode destroys positivity. At `theta=pi`, the symbol is strictly negative for every `r>0`; at `theta=0`, it is strictly positive. Thus the desired local carrier is intrinsically indefinite on the full translation representation.

## 2. The minimal positive diagonal completion is exact

Consider a translation-invariant self-adjoint Toeplitz operator whose nonzero Fourier coefficients are fixed to the prime-ray values `r^{|k|}`. The only remaining scalar degree of freedom is the zero Fourier coefficient `a`, giving (6). Its symbol is

\[
t_{r,a}(\theta)=a+c_r(\theta).
\tag{15}
\]

Because Fourier transform diagonalizes the bilateral shift,

\[
T_{r,a}\succeq0
\quad\Longleftrightarrow\quad
t_{r,a}(\theta)\ge0
\text{ for a.e. }\theta.
\tag{16}
\]

Using the exact minimum in (5), (16) is equivalent to

\[
a\ge -\min c_r=\frac{2r}{1+r},
\tag{17}
\]

which proves (7). Equality is attainable: `T_{r,a_min}` has nonnegative symbol and vanishes only at the antipodal frequency `theta=pi`.

So this is not merely an objection to choosing the standard normalization `P_r=I+C_r`. The full translation-invariant scalar completion problem is solved: **every** positive completion preserving the exact nonzero prime-power coefficients must pay the diagonal cost (17), and no smaller scalar counterterm can work.

The ordinary Poisson kernel uses the larger diagonal `a=1`. It is canonical as harmonic measure, but it is not extremal for this completion problem. Allowing the best possible diagonal improves the counterterm from `1` to `2r/(1+r)` but does not remove it.

## 3. At the Weil scale the unavoidable diagonal mass is globally divergent

Substituting `r=p^{-1/2}` into (17) yields

\[
a_{\min,p}=\frac{2}{\sqrt p+1}.
\tag{18}
\]

Because the prime contribution is weighted by `log p`, the least diagonal term compatible with local positivity is (8). Its sum diverges. Indeed, for every sufficiently large prime,

\[
\frac{2\log p}{\sqrt p+1}
 \ge \frac1p,
\tag{19}
\]

and Euler's theorem gives `\sum_p1/p=\infty`. This proves (9) without using the prime number theorem.

For a finite prime cutoff `P`, the best locally positive completion therefore has the form

\[
\sum_{p\le P}(\log p)T_{r_p,a_{\min,p}}
 =\sum_{p\le P}(\log p)C_{r_p}
 +D_P I,
\tag{20}
\]

where

\[
D_P:=\sum_{p\le P}\frac{2\log p}{\sqrt p+1}\longrightarrow\infty.
\tag{21}
\]

The first term in (20) is the exact symmetric critical prime-power carrier. The second is not part of that carrier; it is the price of making each local Toeplitz block positive.

A global theory may of course contain a quotient, one distinguished global direction, or a finite--archimedean coupling that changes this conclusion after the places are assembled. What (21) forbids is silently treating the locally positive Poisson completion as if its zero mode were harmless. In the infinite-prime limit the added diagonal is not a finite normalization. Any cancellation of it must itself be supplied and justified by the global geometry, and positivity must survive that cancellation.

## 4. Matched controls and falsification

**Do not center.** Keeping the full Poisson kernel gives a genuine positive operator by (11). It also keeps its constant Fourier coefficient. Summing `(log p)P_{p^{-1/2}}` over primes therefore has an even larger diagonal divergence `\sum_p\log p`. Positivity is real, but the arithmetic object is no longer the centered Weil prime carrier.

**Use the optimal scalar center.** Replacing `1` by the exact minimum shift `2r/(1+r)` is the strongest possible scalar repair. Equation (21) shows that even this optimized completion has divergent total diagonal mass.

**Finite cutoff.** For any finite prime set, (20) is a perfectly good positive Toeplitz completion. This is not evidence for global Weil positivity: the required diagonal coefficient depends monotonically on the finite-prime cutoff and diverges when the cutoff is removed.

**Change the phase coordinate.** Conjugating `U` by a unitary or shifting `theta` only rotates the symbol. The range of `c_r` and therefore the minimal diagonal shift (17) are unchanged. The obstruction is not a basis artifact.

**Use a unilateral rather than bilateral ray.** Compression of a positive bilateral Toeplitz operator remains positive, but compression cannot make the exact centered symbol globally positive in the translation-invariant limit. Finite Toeplitz sections may have cutoff-dependent lower eigenvalues, so a finite-section repair is again a boundary/cutoff effect rather than a source-independent global theorem.

**Allow non-scalar or cross-prime completion.** This finding does not classify it. A matrix-valued, cross-prime, or finite--archimedean completion could move the negative directions into a global constrained subspace. That is precisely the surviving category: the compensating sector must be part of the same source-forced operator before positivity is asserted, not a subtraction added after local Poisson positivity has done its work.

**Drop exact prime-power coefficients.** Positive majorants/minorants of Poisson-type kernels are useful in analytic number theory, but changing the coefficients is no longer an exact realization of the Weil prime carrier. Such estimates cannot by themselves establish the line's requested exact global sign mechanism.

## 5. Prior-art and novelty audit

Every analytic ingredient used here is classical. The Poisson kernel, its positive harmonic-extension interpretation, Toeplitz/Herglotz positivity, and the Fourier-series calculation (10) are standard harmonic analysis. The symmetric coefficients `(log p)p^{-k/2}` are the standard prime-power side of the Weil/Guinand explicit formula. Recent analytic-number-theory work also uses Poisson kernels together with the Guinand--Weil formula for extremal bounds, confirming that the appearance of Poisson structure near explicit-formula problems is not itself novel.

The claim is therefore intentionally narrow. It is not a new Poisson-kernel theorem and not a new formulation of the Weil criterion. The line-specific contribution is the exact **completion audit** for a live operator-valued escape: once the nonzero Toeplitz coefficients are fixed to the critical prime-power half-density, the centered carrier is indefinite, the smallest scalar diagonal needed to restore positivity is `2/(sqrt(p)+1)` at prime `p`, and those minimal diagonal costs have infinite total mass after the required `log p` weighting.

This is also not a proof that no global operator can work. Classical explicit-formula, trace-formula, and noncommutative-geometric frameworks already warn that local terms need not be positive place by place. The useful conclusion here is that any successful Mathia construction must exploit exactly that global fact rather than claim positivity from the local prime-ray Poisson kernels independently.

## Consequence for the research line

The non-diagonal/operator-valued escape left by `WP-370` remains open only in a stronger form. A canonical prime-power translation does provide a natural positive harmonic object, but **its exact Weil coefficients live in the centered part, not in the positive kernel itself**. Positive scalar Toeplitz completion necessarily inserts a divergent zero-mode counterterm.

Therefore a viable next object must assemble finite primes with an archimedean/global sector before the sign theorem, or impose a source-forced quotient/constraint that removes the accumulated diagonal direction while preserving positivity on the admissible global subspace. A direct sum of independently positive local Poisson blocks, followed by subtraction of their diagonal baselines, is another repackaging of the required counterterm rather than an intrinsic explanation of Weil positivity.
