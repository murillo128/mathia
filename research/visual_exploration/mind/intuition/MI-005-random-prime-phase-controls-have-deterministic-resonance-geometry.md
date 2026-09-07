# MI-005 — Prime-phase geometry is controlled by signed support, coefficient weight, and actual window energy

**Evidence level:** exact finite-dimensional null law, classical Kronecker/Poisson analysis, fixed-support small-divisor control, and growing-support certificate/energy controls through VIS-078

## Core intuition

Prime-phase randomization is the source's own asymptotic law at fixed finite support, but finite windows require a finer classification. Signed Fourier support and small denominators are only admission data. What matters at theorem scale is the **coefficient mass after the exact sinc window filter**, and a proof certificate can grow even while the actual filtered spectral energy vanishes.

VIS-076 shows that signed support is not sufficient for a persistent finite-window signal: at fixed prime support, `|P_X|^2` has arbitrarily small `log(a/b)` frequencies, yet exponentially decaying Fourier coefficients make the reciprocal-frequency sum finite and every moving-window mean converges uniformly at `O(1/L)`. VIS-077 shows that this `l^1` certificate necessarily becomes expensive as support grows. VIS-078 then makes the decisive separation: the exact mean-square fluctuation is a sinc-filtered `l^2` energy, and the elementary neighboring-prime resonances that force both reciprocal-frequency certificates to grow carry vanishing actual energy.

The live boundary is therefore not “find smaller prime-log frequencies” or “make the Baker constant uniform.” It is the joint growth of the **full coefficient-weighted sinc-filtered energy** under the actual cutoff/window law.

## Strongest justified principle

VIS-067--VIS-070 determine the complete finite-dimensional shared-phase law from retained prime-power coefficients, and VIS-071 proves that deterministic vertical prime flow has the same Haar law in long-height average. VIS-072 gives the exact length-`L` multiplier `sinc(L lambda/2)` for every Fourier character with frequency `lambda=sum_p m_p log p`.

VIS-073 controls bounded-degree mixed Fourier boxes. VIS-074 shows that additive prime harmonics have no cross-prime small divisors; VIS-075 shows that raw holomorphic finite Euler products remain in the positive exponent cone. VIS-076 crosses to signed support with `|P_X|^2`, where fixed-support Baker bounds plus exponential weights imply finite `B_(X,sigma)` and uniform `O(1/L)` collapse.

VIS-077 proves that at `sigma=1/2`, neighboring-prime difference characters force the `l^1` certificate constant to grow at least like `X/log X`. That is a limitation of the absolute-value proof, not a lower bound on the observable.

VIS-078 supplies the exact cancellation-sensitive quantity:

`V_(X,sigma)(L)=A_X^2 sum_(k!=0) w_k^2 sinc^2(L lambda_k/2)`.

The reciprocal-frequency `l^2` upper certificate `Q=sum w_k^2/lambda_k^2` also has a growing coefficient, forcing `L >> sqrt(X/log X)` if one insists on that bound. Yet the same neighboring-prime modes contribute only `O(log X/X)` actual critical-line energy, uniformly in `L`. Small denominators can therefore dominate a certificate while becoming negligible after their true coefficient mass is measured.

## Counterevidence / boundary

VIS-078 does not prove that the full signed spectrum has vanishing growing-support energy. More complicated smooth-ratio resonances may carry appreciable mass, and no optimal joint cutoff/window threshold is established. The result only kills the inference from certificate divergence or a nearest-neighbor beat family to persistent signal.

Adaptive/nonlinear path statistics and the hybrid prime/zero residual remain outside this exact Euler-product mean-square observable and require their own support/weight/energy audit.

## Epistemic status

**Proved for the declared fixed-support control classes and for the neighboring-prime growing-support certificate/energy comparison; the full growing-support sinc-filtered energy remains open.**

## Falsification criterion

Violate the exact Parseval/sinc energy formula for finite `X`, or exhibit neighboring-prime critical-line modes whose actual contribution fails the VIS-078 vanishing bound. A growing-support family whose **full exact** sinc-filtered energy stays macroscopic at the theorem window scale would instead define the intended frontier.