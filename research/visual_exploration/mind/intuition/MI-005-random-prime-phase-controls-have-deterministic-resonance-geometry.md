# MI-005 — Random prime-phase controls have deterministic resonance geometry

**Evidence level:** exact finite product-torus covariance and third-cumulant identities through VIS-068

## Core intuition

Randomizing prime phases does not create a featureless or Gaussian visual null when the same phase is shared by all powers of one prime. The deterministic coefficient system already forces structured second-order and third-order geometry. A covariance ridge, scale band, skewness pattern, or bispectral resonance can therefore survive prime-phase randomization for reasons completely determined by the chosen smoothing and prime-power harmonics.

The right null is not “random-looking.” It is the exact harmonic geometry implied by the randomized model itself.

## Strongest justified principle

VIS-067 proves that for finite observables

`A_alpha = Re sum_{p,k} c_{alpha,p,k} exp(i k theta_p)`

with independent uniform `theta_p`, the covariance is exactly one half of the real Gram matrix of the coefficient vectors. Shared scale support and deterministic height phases can therefore force covariance blocks, oscillatory bands, and anisotropy with no additional arithmetic organization. The baseline can be computed analytically; simulation is only needed for finite-control uncertainty or genuinely nonlinear distributional questions.

VIS-068 lifts the same product-torus orthogonality to third order. A third moment survives precisely when three same-prime harmonics satisfy an additive resonance `k+l=m`, giving an exact tensor built from products such as `c_k c_l conjugate(c_{k+l})`. With only the first harmonic the tensor vanishes, but ordinary Euler-factor logarithms retain prime powers and hence retain these resonances.

Thus **second-order Gram structure and third-order additive-harmonic structure are properties of the shared-prime-phase null itself**. Moving from covariance to skewness is not a new information channel unless the observed statistic is compared with the corresponding exact null tensor.

## What remains possible

An arithmetic field may differ from the null in a frozen residual covariance, a higher cumulant after all lower-order deterministic resonance terms are removed, a tail/topological statistic, or a conditional law. Such a claim must preserve the same phase-sharing convention and calibrate its confirmation uncertainty at the declared claim strength.

Higher-order null tensors may contain more complicated signed harmonic resonances. They should be derived when they become load-bearing rather than assumed Gaussian or generated post hoc from an attractive image.

## Status / novelty

Steinhaus random multiplicative functions and product-torus Fourier orthogonality are classical. The persisted Visual Exploration contribution is their exact specialization to the hybrid prime-phase control: **the randomized null carries computable multiscale geometry through deterministic coefficient overlaps and same-prime harmonic resonances.** No zeta or RH claim follows from those null features.

## Falsification criterion

Give a finite shared-prime-phase coefficient family whose covariance differs from VIS-067's Gram formula or whose third cumulant differs from VIS-068's additive-resonance tensor. Alternatively, demonstrate a proposed visual statistic whose null distribution is provably insensitive to both structures; that would justify a different confirmation target.