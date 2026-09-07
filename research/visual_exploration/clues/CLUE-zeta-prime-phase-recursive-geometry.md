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

`VIS-077` now shows that this particular `l^1` certificate cannot be made dimension-uniform merely by sharpening the fixed-set Diophantine estimate. Neighboring primes in `(X/2,X]` already force

`B_(X,sigma) >= X^(-2 sigma) (pi(X)-pi(X/2)-1)^2`,

hence

`B_(X,1/2) >= (1/4+o(1)) X/(log X)^2`.

After restoring the critical-line Haar factor `P_X(1,0)~e^gamma log X`, the coefficient of `1/L` in the `VIS-076` triangle-inequality bound is at least order `X/log X`. Therefore that proof mechanism can certify joint-limit uniform collapse only in a regime at least as restrictive as `L >> X/log X`. This is a limitation of the certificate, not a lower bound on the true window discrepancy: cancellation-sensitive estimates may be substantially sharper.

## Research question
After quotient/reconstruction controls, fixed-prime vertical equidistribution, the exact finite-window resonance null, the generic safe growing-support corridor, the additive log-Euler corridor, the positive-cone holomorphic Euler-product law, the fixed-support signed `|P_X|^2` closure, and the unavoidable growth of its coefficientwise `l^1` resonance certificate are accounted for, is there a representation-stable visual statistic in the hybrid hierarchy that genuinely leaves the prime-torus information class?

The signed growing-support route is now more specific: it must use a **cancellation-sensitive** quantitative control of the actual sinc-filtered signed spectrum, rather than expecting the absolute reciprocal-frequency norm from `VIS-076` to remain small. Independently anchored finite windows and independently calibrated factor/residual coordinates remain separate admissible routes.

## Why it may matter
The prime-phase visual program has progressively removed increasingly sophisticated false positives: quotient algebra, residual-controlled compensation, coordinate recombination, covariance structure, all finite cumulants, the full fixed-finite phase law, finite-window population geometry driven by the same Kronecker frequencies, a generic bounded-degree growing-support corridor, additive log-Euler support growth, raw holomorphic Euler-product exponentiation, and fixed-support signed Euler-product beats.

`VIS-077` prevents a different false conclusion: failure of the `VIS-076` absolute-value estimate at growing support must not be mistaken for evidence that a visual signal survives. The certificate itself is forced to grow because many elementary neighboring-prime difference modes accumulate. A meaningful positive route must distinguish true finite-window energy from an artifact of discarding phase cancellation term by term.

## Decisive test
For a prime-torus route, first classify the frozen witness by its **signed Fourier support**, coefficient law, and observation-window multiplier.

If it is coordinate-separable, apply `VIS-074` directly; for the critical-line logarithmic Euler field, kill the window-average route whenever `L (log X)^2/sqrt(X) -> infinity`. If it is the raw holomorphic finite Euler product, apply `VIS-075`: all modes remain in the nonnegative exponent cone, and the relevant finite-window cost is coefficient mass rather than a `log(a/b)` small divisor.

If the witness is the fixed-support squared modulus `|P_X|^2`, apply `VIS-076`: its signed small divisors are real, but the exact coefficient-weighted reciprocal-frequency sum is finite for every fixed `X`, forcing uniform `O_(X,sigma)(1/L)` collapse of the moving-window mean.

For growing `|P_X|^2`, apply `VIS-077` before using that same `l^1` certificate. On the critical line its coefficient is already at least order `X/log X`, so a proof that only asks the `VIS-076` right-hand side to vanish cannot certify the regime `L=O(X/log X)`. Do not interpret this failure as persistence.

The next signed test should instead write the exact sinc-filtered Fourier law and control a cancellation-sensitive quantity such as its long-height `l^2` spectral energy, or import a direct growing-cutoff mean-value theorem for the exact observable. Freeze the cutoff law `X=X(L)`, normalization, window statistic, and any selected spectral band before confirmation. A positive claim must show that the resulting deviation survives the matched prime-torus law rather than merely lying outside an `l^1` sufficient corridor.

For an externally anchored finite-window route, define the anchor independently of the prime-torus statistic, freeze the window rule and witness before confirmation, and compare against the exact frequency-preserving random-initial-phase law from `VIS-072`. Account for any search over anchors, windows, scales, or witnesses. Kill the route if the anchor is reconstructible from the same finite prime field or if the effect is reproduced by the matched resonance null.

For a factor/residual statistic, construct the hybrid prime factor, zero factor, and explicit residual independently, reduce deterministic prime/zero recombinations using `VIS-064`--`VIS-066`, and calibrate the joint `(factor,residual)` null at the actual claim strength. Apply `VIS-060`--`VIS-063` to separate exact null specification from finite-window/control uncertainty.

## Evidence boundary
`VIS-067`--`VIS-070` determine the fixed finite shared-phase null, `VIS-071` proves that the deterministic vertical prime field has that same long-height Haar law, and `VIS-072` gives the exact fixed-window sinc spectrum. `VIS-073` supplies a sufficient bounded-degree growing-support corridor for general trigonometric window averages. `VIS-074` supplies a substantially stronger corridor for additive coordinate-separable prime harmonics. `VIS-075` shows that holomorphic Euler-product exponentiation introduces mixed-prime coefficient mass but still no signed small-divisor frequencies. `VIS-076` shows that the moving-window mean of `|P_X|^2` collapses uniformly at every fixed finite prime support. `VIS-077` shows that the absolute reciprocal-frequency norm used by that proof necessarily grows at least like `X/(log X)^2` on the critical line, and that its full `1/L` certificate carries at least order `X/log X`.

None of these findings determines the true cancellation-sensitive growing-support window variance, a sharp cutoff/window threshold, proof that a witness outside the sufficient corridors separates from the torus null, control of arbitrary nonlinear growing-dimensional path functionals, proof that a particular externally anchored window is arithmetic-specific, a new prime/zero independence result, an unexpected factor/residual joint law, or an RH consequence.

## Research disposition
Accepted in further narrowed form. Treat fixed-finite population separation, fixed-finite sliding-window separation, the `VIS-073` generic safe corridor, the `VIS-074` additive corridor, the `VIS-075` raw holomorphic Euler-product positive-cone route, the `VIS-076` fixed-support squared-modulus signed route, and any expectation that its coefficientwise `l^1` resonance norm stays dimension-uniform as closed. Continue the signed route only through cancellation-sensitive growing-support analysis; the independently anchored-window and independently calibrated factor/residual routes remain open.