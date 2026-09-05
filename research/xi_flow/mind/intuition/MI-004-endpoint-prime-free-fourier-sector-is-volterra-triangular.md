# MI-004 — The endpoint prime-free Fourier sector is source-selected, and finite heat-zero transport is Volterra-triangular

**Evidence level:** supported through XF-049 by the Guinand--Weil explicit formula and an exact finite heat-zero Fourier evolution identity

## Core intuition

The actual Xi endpoint has a source-specific low-frequency sector that a generic source-compatible counting model does not. In the `H_0` zero coordinate, the explicit formula has only the archimedean zero mode until the first nonzero prime-power frequency `log 2/2`. The memory-scale frequency relevant to Xi flow is `Theta(1/log T)`, deep inside this prime-free interval.

Finite heat-zero dynamics also respects a compatible one-sided frequency structure. Positive-frequency zero modes evolve by a Volterra convolution using only lower positive frequencies. This does not yet prove the corresponding infinite localized Xi theorem, but it identifies a precise mechanism by which the endpoint source selector could survive: the nonlinear flow has no direct generic high-positive/high-negative down-conversion into the memory band.

## Strongest justified principle

XF-048 applies a Gaussian probe of physical width `Theta(log^3 T)` and memory frequency `Theta(1/log T)`. Its Fourier transform is exponentially small at every prime-power sample in the explicit formula, the archimedean constant-density contribution is killed by oscillation, and the actual endpoint zero statistic is `o(1)`. The coherent critical memory wave of XF-047 instead contributes a nonzero constant. The endpoint source therefore distinguishes the exact mode that counting and universal Cauchy dynamics failed to exclude.

XF-049 proves that for every finite real-simple polynomial heat flow, with `Z_N(xi,t)=sum_j exp(-i xi x_j(t))`,

`partial_t Z_N(xi)=xi^2 Z_N(xi)-xi integral_0^xi Z_N(eta)Z_N(xi-eta)deta`

for `xi>0`. The vector field at frequency `xi` depends only on `[0,xi]`. Linearization about a flat zero density has multiplier `xi^2-2 pi rho xi`; evaluated at the Xi memory frequency it reproduces exactly the periodic Cauchy slow-mode rate derived independently in XF-047.

This agreement shows that the memory clock and the one-sided Fourier transport are two views of the same logarithmic-particle/Burgers geometry, while the absence of low endpoint arithmetic frequencies is specifically Xi source information.

## What remains possible

The needed theorem is an infinite localized version of the finite Volterra law. One must define the renormalized low-frequency zero statistic for Xi, apply the `Theta(log^3 T)` taper used by the explicit-formula probe, and show that renormalization, boundary, and commutator terms are `o(1)` over the relevant fixed heat interval.

The finite triangular law does not imply that low frequencies are freely specifiable or invariant: an entire characteristic sum couples frequency values analytically, and localization itself mixes frequencies. The claim is only that there is no direct unconstrained high-to-low quadratic convolution in the exact finite vector field.

## Status / novelty

Guinand--Weil, complex Burgers/Cole--Hopf structure, Calogero pole dynamics, and Volterra convolutions are classical ingredients. The Mathia synthesis is the source/transport pairing: **the endpoint explicit formula creates a prime-free memory-frequency selector, and the finite heat-zero dynamics has exactly the one-sided Fourier architecture needed for that selector to plausibly propagate without high-frequency contamination**.

## Falsification criterion

Find a prime-power contribution in the XF-048 memory-frequency window under its normalization, derive a finite heat-zero positive-frequency evolution involving frequencies outside `[0,xi]`, or show that localization necessarily creates an order-one low-frequency commutator that defeats any infinite Xi transport theorem at the required scale.

## Lean-formalizable core

- Finite zero characteristic-sum Volterra identity.
- One-sided positive-frequency closure.
- Flat-density multiplier and match to periodic slow-mode rate.
- Gaussian frequency-separation inequalities, given the explicit-formula identity as an input.
