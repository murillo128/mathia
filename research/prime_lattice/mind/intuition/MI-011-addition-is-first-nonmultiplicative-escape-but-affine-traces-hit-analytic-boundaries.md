# MI-011 — Addition is a genuine missing variable, but ordinary affine averaging either erases it or inherits the hard zero-frequency problem

**Evidence level:** supported through PL-189 by exact affine identities, persisted prime-equidistribution inputs, and classical compact-support Fourier uniqueness

## Core intuition

Ordinary addition is genuinely outside the multiplicative exponent-difference quotient: ratios, one-swap terms, and shifted correlations use relations `n` with `n+h`. But preserving addition in the definition is not enough. Canonical regularization, diffuse higher-order averaging, broad Kronecker averaging, slowly varying target weights, and now ordinary bounded positive-width phase averaging all fail to create an easier arithmetic channel.

There are two complementary failure modes. If the effective affine phase window grows, PL-187 shows that averaging erases every bounded target without learning its arithmetic mean. If the normalized window has fixed positive width and bounded center, PL-189 shows that uniform flattening is so rigid that it already forces the zero-frequency coefficient mean to cancel. The useful regime must therefore preserve a more singular/coherent observation or a genuinely joint source relation.

## Strongest justified principle

PL-169--PL-176 establish the first boundary. Additive shifted correlation is absent from exponent differences, yet simple affine traces telescope or remain behind absolute-convergence walls; `det_2` deletes the first trace carrying fixed-shift Chowla data; fixed finite logarithmic sectors become Haar/Bernoulli under current theorems; and complete additive-cube averaging collapses to generic multiplicative pseudorandomness.

PL-177--PL-186 isolate the direct prime-shift channel and its information boundary. An oriented nonselfadjoint phase can retain shifted-prime arithmetic, but broad prime/Kronecker averages scalarize under continuum density, bounded slowly varying target weights do not stop that collapse, and every subpower local exponent block can remain classically distributed while full parity stays unresolved behind the sieve barrier.

PL-187 proves universal erasure when the effective normalized phase width diverges. PL-189 then compactifies the complementary bounded-width, bounded-center regime: after removing a common phase, the normalized frequencies lie in one fixed compact interval, so any weak limit is a compactly supported complex measure. If its Fourier transform vanishes on a positive-length interval, analytic uniqueness forces it to vanish at zero. Thus bounded-window flattening of a hard target is not a spectral shortcut; it already contains the hard arithmetic cancellation at zero frequency.

The durable principle is therefore: **addition supplies missing arithmetic information, but ordinary affine averaging has no easy middle regime. Broad windows erase the target universally, while fixed positive-width bounded-center windows can flatten only by already solving the signed zero-frequency problem.**

## What remains possible

Ordinary fixed-shift Cesaro correlations remain outside the diffuse theorems. Within affine phase space, isolated pointwise frequencies, shrinking normalized windows, or windows whose normalized centers escape to infinity are not covered by PL-189. More importantly, source-forced sparse/completed additive relations or genuinely joint multi-prime carriers may preserve parity-sensitive information that a one-point phase average cannot.

A target-relative construction must therefore change a load-bearing hypothesis: preserve a parity-sensitive cross-tail coupling, use singular/thin conditioning, remain pointwise enough to avoid generic erasure, or introduce a joint/completed operator whose final observation does not reduce to one compact-frequency Fourier transform.

## Status / novelty

Shifted correlations, Chowla-type problems, regularized determinants, Furstenberg systems, Gowers uniformity, Kronecker phases, prime equidistribution, compactly supported Fourier transforms, and analytic uniqueness are classical/persisted inputs. The synthesis is the observation boundary: **addition supplies missing information, but neither diverging nor fixed positive-width bounded-center affine averaging creates an easier route to hard signed cancellation.**

## Falsification criterion

Produce a covered diverging-width affine average retaining an arbitrary bounded hard target beyond the PL-187 estimate, or a bounded positive-width bounded-center sequence whose `L^2` transform vanishes while its zero-frequency mean stays bounded away from zero. Otherwise an affine survivor must lie in one of the explicitly uncovered singular/coherent regimes or carry genuinely joint source information.

## Lean-formalizable core

- Affine operator and regularization deletion identities.
- Uniform/all-shift averaging reductions.
- Compact-frequency reduction for bounded normalized phase windows.
- Fourier-uniqueness implication from interval flattening to zero-frequency cancellation.
