# MI-004 — The endpoint prime-free Fourier sector has an exact collision-safe infinite Volterra carrier

**Evidence level:** supported through XF-051 by the Guinand--Weil explicit formula, collision-safe symmetric finite heat transport, de Bruijn strip control, horizontal logarithmic derivatives, and an exact distributional half-line Volterra law

## Core intuition

The actual Xi endpoint has a source-specific low-frequency sector that a generic source-compatible counting model does not. In the `H_0` zero coordinate, the explicit formula has no nonzero prime-power frequency below `log 2/2`, while the memory scale relevant to Xi flow is `Theta(1/log T)`.

The required one-sided transport is no longer merely a finite real-root heuristic. Finite symmetric zero statistics satisfy the same Volterra law through complex roots and collisions, and the infinite Xi family has a canonical renormalized positive-frequency carrier obtained from the logarithmic derivative on a zero-free horizontal line. The remaining issue is quantitative control as the moving band approaches the singular endpoint `xi=0`, not existence, root reality, or high-to-low frequency leakage.

## Strongest justified principle

XF-048 constructs an endpoint probe whose actual zero response is `o(1)` while the coherent critical memory control has a nonzero limit. XF-050 strengthens this with a compactly bandlimited test: its Fourier support lies strictly between zero and the first prime-power line, so the prime contribution vanishes exactly, and the explicit formula remains meaningful for complex off-line zeros.

XF-049's finite Volterra law extends in XF-050 to arbitrary complex roots and through collisions because the exponential zero sum is a symmetric analytic function of the polynomial coefficients. Individual root branches may be singular, but the low-positive-frequency field is not.

XF-051 gives the infinite carrier. For any zero-free horizontal line `Im z=a>1`, the boundary logarithmic derivative `Q_a=H_t'/H_t` is a tempered upper-half-plane boundary value with Fourier support in `[0,infinity)`. Its Burgers equation becomes an exact distributional convolution law on that proper cone. After removing the auxiliary factor `e^{-a xi}`, the resulting distribution `mathcal Z_t` is independent of `a`, agrees with the finite zero characteristic sum on positive frequencies, and obeys the same Volterra-triangular equation.

Thus the Xi source/transport pairing is now exact away from `xi=0`: the endpoint explicit formula selects the memory band, and the true infinite heat flow cannot replenish a positive frequency from larger or opposite frequencies.

## What remains possible

The memory center tends to zero like `1/log T`, so the Volterra simplex still includes the entire lower-positive interval down to the singular endpoint. A proof must separate the deterministic archimedean/background component of `mathcal Z_t` near zero from the fluctuation and bound the quadratic lower-band contribution to the moving probe by `o(1)` over the relevant heat interval.

A decisive obstruction would be an order-one term generated from the endpoint singularity or frequencies below the memory band. Loss of root reality, root collision, taper-induced opposite-frequency mixing, or nonexistence of the raw infinite characteristic sum no longer addresses the active carrier.

## Status / novelty

Guinand--Weil, de Bruijn strip shrinking, Hadamard logarithmic derivatives, complex Burgers/Cole--Hopf structure, Paley--Wiener half-line support, and Volterra convolution are classical ingredients. The Mathia synthesis is the source/transport boundary: **the endpoint prime-free memory sector has a canonical collision-safe infinite one-sided transport; the sole remaining transport gate is quantitative control of the renormalized field as its positive-frequency band collapses toward zero**.

## Falsification criterion

Find a prime-power contribution inside the compact XF-050 endpoint band, derive positive-frequency Xi evolution involving frequencies above the target or the negative half-axis, show that the horizontal carrier depends on the auxiliary height, or exhibit an unavoidable order-one `xi downarrow 0` contribution that refills the endpoint selector over the needed heat interval.

## Lean-formalizable core

- Collision-safe Newton-sum/finite Volterra identity.
- Compact band separation from the first prime-power frequency.
- Horizontal-line height-cancellation identity for the positive-frequency carrier.
- Abstract cone-support implication for Volterra triangularity, with analytic inputs assumed.
