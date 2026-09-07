# MI-005 — Prime-phase geometry is controlled by signed Fourier support, coefficient weight, and finite-window sinc law

**Evidence level:** exact finite-dimensional null law, classical Kronecker/Poisson analysis, and fixed-support small-divisor control through VIS-076

## Core intuition

Prime-phase randomization is the source's own asymptotic law at fixed finite support, but finite windows require a finer classification. The relevant object is not “nonlinearity” or “mixed primes” in the abstract. It is the **signed Fourier support together with the coefficient weight carried by each near-resonant frequency and the sinc attenuation imposed by the observation window**.

Signed support is necessary for cross-prime frequencies `log(a/b)` to approach zero, but VIS-076 shows that it is not sufficient for a persistent finite-window signal. At fixed prime support, the squared Euler product has genuine arbitrarily small signed frequencies, yet its exponentially decaying Fourier coefficients make the coefficient-weighted reciprocal-frequency sum finite; every moving-window mean still converges uniformly to Haar at `O(1/L)`. The live boundary is therefore the joint growth of support and weighted resonance mass.

## Strongest justified principle

VIS-067--VIS-070 determine the complete finite-dimensional shared-phase law from the retained prime-power coefficients, and VIS-071 proves that deterministic vertical prime flow has the same Haar law in long-height average. VIS-072 gives the exact length-`L` multiplier `sinc(L lambda/2)` for every Fourier character with frequency `lambda=sum_p m_p log p`.

VIS-073 controls bounded-degree mixed Fourier boxes. VIS-074 shows that additive prime harmonics have no cross-prime small divisors because every nonconstant frequency is `k log p`. VIS-075 shows that raw holomorphic finite Euler products remain in the positive exponent cone, so every nonconstant frequency is `log n>=log 2`; mixed-prime multiplication alone does not create small frequencies.

VIS-076 crosses that support boundary with `|P_X(sigma,t)|^2`. Its Fourier lattice is signed and contains arbitrarily small nonzero `lambda_k=sum k_p log p`, but at fixed `X` the coefficient is `w_k=prod p^{-sigma|k_p|}`. Baker-type lower bounds for the fixed logarithms grow only polynomially in exponent height, while `w_k` decays exponentially, so

`B_(X,sigma)=sum_(k!=0) w_k/|lambda_k| < infinity`.

Consequently the moving-window mean differs from its Haar value by at most `2 P_X(2 sigma,0) B_(X,sigma)/L`, uniformly in the window start. Signed resonance is real, but fixed-support coefficient decay defeats it.

## Counterevidence / boundary

The fixed-support theorem is deliberately not dimension-uniform. Nothing in VIS-076 controls `B_(X,sigma)` as `X->infinity`; the number of prime coordinates grows and general linear-forms-in-logarithms constants may deteriorate badly. A joint limit `X=X(L)` is therefore a distinct quantitative problem.

Adaptive or nonlinear path statistics, maxima, threshold events, phase-unwrapped observables, independently anchored residuals, and other statistics require their own support/weight audit. The hybrid residual is not reduced to the prime torus by these results.

## Epistemic status

**Proved for the declared fixed-support control classes; growing-support signed resonance remains open.** The Poisson-kernel, Fourier, Baker, and Kronecker ingredients are classical; the durable synthesis is that support sign, coefficient decay, small-divisor size, and observation window must be analyzed together.

## Falsification criterion

Exhibit a fixed finite prime support for which the coefficient-weighted reciprocal-frequency series of `|P_X|^2` diverges, or a fixed `X,sigma` moving-window mean whose deviation from Haar fails to vanish uniformly at the derived `O(1/L)` rate. A growing-support signed observable for which the corresponding weighted resonance mass remains large enough at theorem scale would instead define the intended frontier.