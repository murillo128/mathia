# MI-036 — Exact zero density locks source-compatible bow duality on the noncontracting side of Riemann--Siegel

**Evidence level:** exact/literature-backed synthesis from [WI-322](../../findings/WI-322-exact-rvm-normalization-forces-bow-prime-scale-below-riemann-siegel-length.md) and [WI-323](../../findings/WI-323-riemann-siegel-duality-makes-source-compatible-bow-transform-noncontracting.md), building on the earlier bow stationary-phase geometry. Riemann--von Mangoldt and approximate-functional-equation reciprocity are classical; the source-compatible bow consequence is line-specific.

The bow scale had previously been known only at exponent accuracy: a source-compatible symmetrized Maynard--Pratt configuration forces reciprocal prime length `T^(1/2+o(1))`, but that left open whether a subpower drift could make the distinguished logarithmic chirp effectively sparse.

WI-322 removes that loophole by retaining the exact local zero-density normalization before exponentiation. If `X_*` is the reciprocal prime length and `U` the local height, then

`X_* <= sqrt(U/(2pi))(1+o(1))`,

so

`rho_T=U/X_*^2 >= 2pi(1-o(1))`.

The count-compatible source therefore lies on or below the Riemann--Siegel self-dual length. The B-process derivative image at every growing coupled shift has at least linear width; the missing rate at which the bow spacing approaches its count threshold can make the chirp denser, but cannot make it vanish.

WI-323 shows that the same normalization also fixes the direction of the direct reciprocal transform. Put `A=U/(2pi)`. The two-dimensional logarithmic stationary map sends

`(m,n) -> (p,q)=(A/m,A/n)`

and has natural dual length `Y_*=A/X_*`. Hence

`Y_*/X_* = A/X_*^2 >= 1-o(1)`.

At exact count saturation the transform is asymptotically self-dual; if the source length is shorter, the dual is longer. More strongly, the map preserves the multiplicative coordinate `p/q=n/m`, hence the relative logarithmic bandwidth, and the Hessian converts the square-root normalization exactly from `1/sqrt(mn)` to `1/sqrt(pq)`.

The reusable conclusion is that **source-compatible zero counting and Riemann--Siegel reciprocity eliminate geometric compression as a bow escape**. Neither a vanishing chirp density nor a second pass through direct approximate-functional-equation/Poisson/B-process geometry can produce a shorter or better-normalized arithmetic object merely from scale duality. Any gain after the transform must come from new arithmetic information in the coefficients.

This sharpens the remaining bow problem: the distinguished off-diagonal covariance is not hard because the phase transform has been normalized poorly. The geometric transform is already noncontracting and self-normalized. A successful de-exceptionalization theorem must prove signed cancellation or another source-fixed incompatibility for the von-Mangoldt coefficient structure itself.

**Boundary.** WI-322--WI-323 do not bound the signed transformed covariance, prove a simple-zero proportion, or resolve the accepted distinguished-twist clue. The exact identities describe source-compatible scale and stationary geometry; treating `Lambda(m)Lambda(n)` rigorously still requires arithmetic analysis. A different decomposition or spectral transform may succeed if its gain comes from information absent from this direct duality.