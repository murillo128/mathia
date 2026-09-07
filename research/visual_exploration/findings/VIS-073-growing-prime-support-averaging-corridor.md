# VIS-073 — bounded-degree growing prime support has an explicit averaging corridor

## Claim

For each cutoff `X>=2`, let

`P_X = {p prime : p<=X}`

and write

`vartheta(X) = sum_(p<=X) log p`.

Let

`f_X(theta) = sum_(m in M_X) c_X(m) exp(i m dot theta)`

be a trigonometric polynomial on `T^{|P_X|}`. Assume that every participating mode satisfies

`|m_p| <= D_X` for every `p<=X`.

Define the nonconstant coefficient masses

`A_X = sum_(m != 0) |c_X(m)|`,

`R_X = (sum_(m != 0) |c_X(m)|^2)^(1/2)`,

and the length-`L` vertical window average

`B_(X,L)(theta) = (1/L) integral_0^L f_X(theta - t omega_X) dt`,

where `omega_X=(log p)_(p<=X)`.

Then

`sup_theta |B_(X,L)(theta)-c_X(0)|`
` <= A_X min(1, 2 exp(D_X vartheta(X))/L)`

and, for Haar-uniform `Theta_X` on the same torus,

`(E |B_(X,L)(Theta_X)-c_X(0)|^2)^(1/2)`
` <= R_X min(1, 2 exp(D_X vartheta(X))/L)`.

Consequently a growing-support family still collapses uniformly to its Haar mean whenever

`A_X exp(D_X vartheta(X))/L -> 0`,

and collapses in Haar RMS under the weaker coefficient condition

`R_X exp(D_X vartheta(X))/L -> 0`.

Thus **support growth by itself does not escape the finite-prime torus obstruction**. For bounded-degree trigonometric window averages with controlled coefficient mass there is an explicit growing-support corridor in which the frequency-preserving torus null remains uniformly decisive.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER/KRONECKER COROLLARY + DECISIVE-NEGATIVE + NO-NOVELTY-CLAIM`.

No optimal discrepancy rate, sharp small-divisor theorem, statement for arbitrary continuous path functionals, hybrid factor/residual independence result, or RH consequence is claimed.

## 1. Uniform small-divisor separation inside a degree box

`VIS-072` writes every nonzero Fourier frequency as

`lambda_m = sum_(p<=X) m_p log p = log(a_m/b_m)`,

where `a_m` and `b_m` are distinct coprime positive integers formed from the positive and negative prime exponents of `m`.

If

`Q_m = max(a_m,b_m)`,

then `VIS-072` proves the elementary separation

`|lambda_m| >= 1/Q_m`.

The degree-box assumption gives

`Q_m <= product_(p<=X) p^(|m_p|)`
`     <= product_(p<=X) p^(D_X)`
`     = exp(D_X vartheta(X))`.

Therefore every nonzero mode in the entire admitted Fourier box satisfies the common lower bound

`|lambda_m| >= exp(-D_X vartheta(X))`.

This estimate is intentionally crude. Its role is to give a completely explicit sufficient corridor without solving the finer Diophantine problem of the actual smallest prime-log resonance.

## 2. Window averaging suppresses the whole admitted box

For each mode, `VIS-072` gives the exact window multiplier

`exp(-i L lambda_m/2) sinc(L lambda_m/2)`

and hence

`|sinc(L lambda_m/2)| <= min(1, 2/(L |lambda_m|))`.

Using the uniform separation above,

`|sinc(L lambda_m/2)|`
` <= min(1, 2 exp(D_X vartheta(X))/L)`

for every nonzero admitted mode simultaneously.

Taking the `l1` sum of the Fourier expansion yields

`sup_theta |B_(X,L)(theta)-c_X(0)|`
` <= A_X min(1, 2 exp(D_X vartheta(X))/L)`.

Nothing probabilistic enters this estimate. It holds for every initial torus phase.

## 3. Haar RMS has the same corridor with `l2` mass

Under Haar phase, distinct torus characters are orthogonal. The exact variance formula from `VIS-072` is

`E |B_(X,L)(Theta_X)-c_X(0)|^2`
` = sum_(m != 0) |c_X(m)|^2 sinc^2(L lambda_m/2)`.

Applying the same uniform mode bound and taking square roots gives

`RMS <= R_X min(1, 2 exp(D_X vartheta(X))/L)`.

The load-bearing distinction is therefore coefficient geometry rather than support size alone: uniform pointwise control pays the nonconstant Fourier `l1` mass, while Haar RMS pays only the `l2` mass.

## 4. The safe growing-support corridor

Suppose now that `X`, `D_X`, the coefficient arrays, and the window length vary together along some asymptotic family. If

`log L - D_X vartheta(X) - log A_X -> +infinity`,

then the pointwise window discrepancy tends to zero uniformly in the initial phase. If instead

`log L - D_X vartheta(X) - log R_X -> +infinity`,

then the Haar RMS tends to zero.

These conditions are sufficient, not necessary. They identify a region in parameter space where a proposed growing-support visual cannot claim to have escaped the prime-torus null merely because more primes or more coordinates were admitted.

The sharper mode-by-mode condition remains the one already visible in `VIS-072`: the actual witness may behave much better than the degree-box bound when its Fourier mass avoids near-resonant modes. Conversely, leaving this sufficient corridor does not establish a positive signal; it only means the present elementary bound no longer kills it.

## 5. Prior art and novelty boundary

This is an elementary quantitative specialization of the classical Fourier/Weyl viewpoint already anchored in `VIS-072` by Kuipers--Niederreiter and Drmota--Tichy. The only arithmetic input beyond that finding is the same unique-factorization separation of prime-log frequencies used there.

No new general quantitative Kronecker theorem or Diophantine approximation result is claimed. The Mathia-specific content is the explicit **safe corridor** obtained by aggregating the exact sinc multiplier and rational-separation bound over a growing prime cutoff and a bounded Fourier-degree box.

## 6. Boundary and falsification

The theorem concerns window averages of trigonometric polynomials. It does not extend automatically to arbitrary continuous functionals of the whole window path when dimension and support grow, because approximation complexity and continuity moduli may themselves deteriorate with `X`.

The coefficient masses `A_X` and `R_X` are essential. A family with rapidly increasing Fourier mass can leave the displayed corridor even when `D_X vartheta(X)` is small relative to `log L`.

The degree-box bound is also not sharp. It ignores the actual support of each mode and the true spacing of distinct `P_X`-smooth integers. A stronger route may replace `D_X vartheta(X)` by a materially smaller witness-specific small-divisor envelope, but it must prove that improvement rather than infer it visually.

Falsify the displayed inequalities by exhibiting an admitted trigonometric polynomial and window for which the exact `VIS-072` sinc expansion exceeds either bound.

## Research consequence

The growing-support branch of `CLUE-zeta-prime-phase-recursive-geometry` is narrower than “let the number of primes increase.” Any bounded-degree trigonometric window-average witness satisfying

`A_X exp(D_X vartheta(X))/L -> 0`

is already uniformly swallowed by the frequency-preserving torus null. A positive growing-support experiment must therefore leave this safe corridor, or use a witness class not covered by it, and then supply the stronger quantitative control needed to show that the observed structure is not merely unresolved prime-log resonance geometry.