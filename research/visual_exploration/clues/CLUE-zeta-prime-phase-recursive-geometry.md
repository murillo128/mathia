---
id: CLUE-visual-exploration-zeta-prime-phase-recursive-geometry
type: research-clue
status: accepted
origin: research-watch
target_line: visual_exploration
based_on:
  - research/visual_exploration/README.md
  - research/visual_exploration/findings/VIS-010-hybrid-euler-hadamard-scale-transfer-tautology.md
  - research/visual_exploration/findings/VIS-064-hybrid-independent-scale-transfer-error-bound.md
  - research/visual_exploration/findings/VIS-065-hybrid-contrast-single-factor-residual-coordinate.md
  - research/visual_exploration/findings/VIS-066-hybrid-joint-field-factor-residual-shear.md
  - research/visual_exploration/findings/VIS-067-independent-prime-phase-scale-covariance-gram-kernel.md
  - research/visual_exploration/findings/VIS-068-shared-prime-phase-third-order-harmonic-resonances.md
  - research/visual_exploration/findings/VIS-069-shared-prime-phase-all-order-connected-resonance-cumulants.md
  - research/visual_exploration/findings/VIS-070-shared-prime-phase-full-characteristic-law.md
  - research/visual_exploration/findings/VIS-071-finite-prime-vertical-flow-shared-phase-haar-law.md
  - research/visual_exploration/findings/VIS-072-fixed-prime-window-discrepancy-sinc-spectrum.md
  - research/visual_exploration/findings/VIS-073-growing-prime-support-averaging-corridor.md
  - research/visual_exploration/findings/VIS-074-additive-log-euler-window-corridor.md
  - research/visual_exploration/findings/VIS-075-holomorphic-euler-product-positive-cone-window-law.md
  - research/visual_exploration/findings/VIS-076-squared-euler-product-signed-mode-fixed-support-bound.md
  - research/visual_exploration/findings/VIS-077-neighbor-prime-signed-resonance-norm-growth.md
  - research/visual_exploration/findings/VIS-078-signed-euler-product-l2-energy-certificate-gap.md
  - research/visual_exploration/findings/VIS-079-signed-euler-product-triangular-autocorrelation.md
---

# Can prime-by-prime zeta approximants expose structure beyond the prime torus itself?

## Observation
The hybrid Euler--Hadamard representation gives a mathematically justified critical-strip scale decomposition into a finite von-Mangoldt prime factor, an independently defined smoothed zero factor, and an explicit residual. `VIS-010` and `VIS-064`--`VIS-066` show that quotient compensation, the raw prime/zero contrast, and arbitrary deterministic recombinations of the complete prime/zero increment fields do not create an additional information channel once the residual is retained.

`VIS-067`--`VIS-070` make the shared-prime-phase control exact: its covariance, all finite connected cumulants, and complete finite-dimensional characteristic law are deterministic consequences of the prime-power coefficient arrays. `VIS-071` then identifies that Haar control with the long-height law of the deterministic finite prime-phase orbit itself.

`VIS-072` closes the nearest finite-window escape at fixed finite support. A fixed window is a continuous function of the same torus initial phase, so the population of actual sliding-window statistics across starting heights converges to the frequency-preserving random-initial-phase control. For trigonometric-polynomial witnesses, the finite-window discrepancy is exactly a sinc-filtered spectrum of log-rational small divisors `lambda_m=sum_p m_p log p`.

`VIS-073` closes a first generic part of the growing-support escape by bounding a bounded-degree Fourier box through `exp(D_X vartheta(X))`. `VIS-074` then shows that this worst-case small-divisor cost is absent for additive one-prime-at-a-time harmonics. A coordinate-separable prime field has only frequencies `k log p`, and the logarithmic Euler field satisfies

`sup_h |(1/L) integral_h^(h+L) E_X(sigma,t) dt|`
` <= (2/L) sum_(p<=X) Li_2(p^(-sigma))/log p`.

On the critical line the right-hand side is `(4+o(1)) sqrt(X)/(L (log X)^2)`.

`VIS-075` closes the next apparent nonlinear escape. The raw holomorphic finite Euler product has the absolutely convergent smooth-number expansion

`P_X(sigma,t)=sum_(n in S_X) n^(-sigma-it)`.

Its Fourier characters can mix many primes, but every exponent vector remains nonnegative and every nonconstant vertical frequency is `log n>=log 2`. Exponentiation therefore changes the coefficient mass without creating cross-prime near-zero frequencies.

`VIS-076` then crosses the signed-support boundary with the first natural example, `|P_X(sigma,t)|^2`. At fixed finite `X`, its exact Poisson-product Fourier series has coefficients

`P_X(2 sigma,0) prod_(p<=X) p^(-sigma |k_p|)`

at signed frequencies `lambda_k=sum_(p<=X) k_p log p`. Genuine near-resonances `log(a/b)` occur, but classical fixed-set lower bounds for linear forms in logarithms make

`B_(X,sigma)=sum_(k!=0) prod_(p<=X) p^(-sigma |k_p|)/|lambda_k|`

finite. Consequently

`sup_h |(1/L) integral_h^(h+L) |P_X(sigma,t)|^2 dt - P_X(2 sigma,0)|`
` <= 2 P_X(2 sigma,0) B_(X,sigma)/L`.

`VIS-077` shows that this particular `l^1` certificate cannot be made dimension-uniform merely by sharpening the fixed-set Diophantine estimate. Neighboring primes in `(X/2,X]` force

`B_(X,1/2) >= (1/4+o(1)) X/(log X)^2`,

so after restoring the critical-line Haar factor the coefficient of `1/L` in the `VIS-076` bound is at least order `X/log X`. This is a limitation of the certificate, not a lower bound on the true window discrepancy.

`VIS-078` writes the cancellation-sensitive quantity exactly. The long-height mean-square fluctuation is

`V_(X,sigma)(L)`
` = P_X(2 sigma,0)^2 sum_(k!=0) w_k^2 sinc^2(L lambda_k/2)`.

A reciprocal-frequency `l^2` certificate based on

`Q_(X,sigma)=sum_(k!=0) w_k^2/lambda_k^2`

is softer than the `VIS-077` `l^1` bound but still cannot remain dimension-uniform: on the critical line neighboring primes force `Q_(X,1/2)>=(1/4+o(1))X/(log X)^3`, so the simple `L^-2` certificate can vanish only in a regime at least as restrictive as `L >> sqrt(X/log X)`. Crucially, the actual sinc-filtered energy of those same neighboring-prime modes is at most `(4e^(2gamma)+o(1))log X/X`, uniformly in `L`, and therefore tends to zero. The modes that make the reciprocal-frequency certificates expensive are certificate-heavy but energy-light.

`VIS-079` removes the remaining high-dimensional bookkeeping from this exact energy. For finite `X` and `sigma>0`, if `A_X=P_X(2 sigma,0)`, then the normalized squared Euler product has exact long-height autocorrelation

`C_(X,sigma)(u)=|P_X(2 sigma,u)|^2/P_X(4 sigma,0)`,

and therefore

`V_(X,sigma)(L)/A_X^2`
` = (2/L^2) integral_0^L (L-u)[C_(X,sigma)(u)-1] du`.

On the critical-line parameter `sigma=1/2`, the full signed growing-support energy is exactly

`(2/L^2) integral_0^L (L-u)`
` [|P_X(1,u)|^2/P_X(2,0)-1] du`.

The unresolved signed route is thus a one-variable triangular mean-value problem for a finite Euler product on `Re(s)=1`, under the same frozen joint law `X=X(L)`. Enumerating individual signed near-resonances is no longer necessary for this witness.

## Research question
After quotient/reconstruction controls, fixed-prime vertical equidistribution, the exact finite-window resonance null, the generic safe growing-support corridor, the additive log-Euler corridor, the positive-cone holomorphic Euler-product law, the fixed-support signed `|P_X|^2` closure, the separation between reciprocal-frequency certificate growth and actual spectral energy, and the exact autocorrelation reduction are accounted for, is there a representation-stable visual statistic in the hybrid hierarchy that genuinely leaves the prime-torus information class?

The signed growing-support route is now specific: determine the asymptotic behavior of the exact triangularly weighted centered mean

`(2/L^2) integral_0^L (L-u)`
` [|P_X(1,u)|^2/P_X(2,0)-1] du`

under a predeclared joint regime `X=X(L)`, or prove an equivalent theorem for the same sinc-filtered spectral energy. Growth of `l^1` or reciprocal-frequency `l^2` certificate constants, visually dramatic beats, and tiny denominators are not admissible positive evidence. Independently anchored finite windows and independently calibrated factor/residual coordinates remain separate admissible routes.

## Why it may matter
The prime-phase visual program has progressively removed increasingly sophisticated false positives: quotient algebra, residual-controlled compensation, coordinate recombination, covariance structure, all finite cumulants, the full fixed-finite phase law, finite-window population geometry driven by the same Kronecker frequencies, a generic bounded-degree growing-support corridor, additive log-Euler support growth, raw holomorphic Euler-product exponentiation, and fixed-support signed Euler-product beats.

`VIS-077` prevents failure of an absolute-value estimate from being mistaken for persistence. `VIS-078` sharpens that diagnosis: even a natural reciprocal-frequency `l^2` certificate can be forced large by a family whose actual squared spectral mass vanishes. `VIS-079` then replaces the complete signed resonance census by an exact one-dimensional autocorrelation object. A meaningful positive route must therefore establish non-negligible triangular correlation energy in the declared growing regime, not merely exhibit small divisors or a proof bound that stops shrinking.

## Decisive test
For a prime-torus route, first classify the frozen witness by its signed Fourier support, coefficient law, observation-window multiplier, and claim norm.

If it is coordinate-separable, apply `VIS-074` directly; for the critical-line logarithmic Euler field, kill the window-average route whenever `L (log X)^2/sqrt(X) -> infinity`. If it is the raw holomorphic finite Euler product, apply `VIS-075`: all modes remain in the nonnegative exponent cone, and the relevant finite-window cost is coefficient mass rather than a `log(a/b)` small divisor.

If the witness is the fixed-support squared modulus `|P_X|^2`, apply `VIS-076`: its signed small divisors are real, but the exact coefficient-weighted reciprocal-frequency sum is finite for every fixed `X`, forcing uniform `O_(X,sigma)(1/L)` collapse of the moving-window mean.

For growing `|P_X|^2`, use `VIS-077` and `VIS-078` only as certificate diagnostics. On the critical line the `l^1` certificate is already at least order `X/(L log X)`, while the elementary reciprocal-frequency `l^2` certificate cannot vanish unless `L >> sqrt(X/log X)`. Neither failure is persistence. The neighboring-prime modes that force both lower bounds have vanishing actual long-height `l^2` energy.

The next signed test should use the exact `VIS-079` reduction. Freeze a joint law `X=X(L)` and analyze

`T_(X,L)=(2/L^2) integral_0^L (L-u)`
` [|P_X(1,u)|^2/P_X(2,0)-1] du`.

A positive claim must give a theorem-level lower bound, asymptotic, or other characterization showing that `T_(X,L)` retains non-negligible mass in the declared regime; a closing result may instead prove `T_(X,L)->0`. Compare the exact triangular weight, normalization, and cutoff law with the hypotheses of existing finite-Euler-product mean-value theorems rather than importing a result for a different moment or averaging regime. The equivalent sinc-spectrum formula remains available as a cross-check, but do not infer signal from divergence of `B_X`, `Q_X`, a nearest-neighbor resonance count, or failure of a sufficient corridor.

For an externally anchored finite-window route, define the anchor independently of the prime-torus statistic, freeze the window rule and witness before confirmation, and compare against the exact frequency-preserving random-initial-phase law from `VIS-072`. Account for any search over anchors, windows, scales, or witnesses. Kill the route if the anchor is reconstructible from the same finite prime field or if the effect is reproduced by the matched resonance null.

For a factor/residual statistic, construct the hybrid prime factor, zero factor, and explicit residual independently, reduce deterministic prime/zero recombinations using `VIS-064`--`VIS-066`, and calibrate the joint `(factor,residual)` null at the actual claim strength. Apply `VIS-060`--`VIS-063` to separate exact null specification from finite-window/control uncertainty.

## Evidence boundary
`VIS-067`--`VIS-070` determine the fixed finite shared-phase null, `VIS-071` proves that the deterministic vertical prime field has that same long-height Haar law, and `VIS-072` gives the exact fixed-window sinc spectrum. `VIS-073` supplies a sufficient bounded-degree growing-support corridor for general trigonometric window averages. `VIS-074` supplies a substantially stronger corridor for additive coordinate-separable prime harmonics. `VIS-075` shows that holomorphic Euler-product exponentiation introduces mixed-prime coefficient mass but still no signed small-divisor frequencies. `VIS-076` shows that the moving-window mean of `|P_X|^2` collapses uniformly at every fixed finite prime support. `VIS-077` shows that the absolute reciprocal-frequency norm used by that proof necessarily grows at least like `X/(log X)^2` on the critical line. `VIS-078` gives the exact long-height sinc-filtered `l^2` energy, shows that the corresponding reciprocal-frequency `l^2` certificate also grows, and proves that the neighboring-prime family responsible for these certificate lower bounds has vanishing actual spectral energy. `VIS-079` proves that this full finite-support energy is exactly the triangular centered autocorrelation mean of `|P_X(1,u)|^2/P_X(2,0)` on the doubled line.

None of these findings determines the joint-limit behavior of that triangular mean for growing `X=X(L)`, a sharp cutoff/window threshold, proof that a witness outside the sufficient corridors separates from the torus null, control of arbitrary nonlinear growing-dimensional path functionals, proof that a particular externally anchored window is arithmetic-specific, a new prime/zero independence result, an unexpected factor/residual joint law, or an RH consequence.

## Research disposition
Accepted in further narrowed form. Treat fixed-finite population separation, fixed-finite sliding-window separation, the `VIS-073` generic safe corridor, the `VIS-074` additive corridor, the `VIS-075` raw holomorphic Euler-product positive-cone route, the `VIS-076` fixed-support squared-modulus signed route, dimension-uniform `l^1`/reciprocal-frequency `l^2` certificate expectations, nearest-neighbor small-divisor mass, and a separate high-dimensional resonance-census formulation as closed positive routes. Continue the signed route only through the exact `VIS-079` triangular mean or its equivalent full sinc-filtered growing-support energy under a frozen joint law; the independently anchored-window and independently calibrated factor/residual routes remain open.