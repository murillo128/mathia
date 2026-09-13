# MI-020 — Complete one-signed screening trades discrete vanishing for support packing

**Evidence level:** exact on the hypothetical one-signed first unrestricted Suzuki crossing under complete active prime-power screening, by [WI-281](../../findings/WI-281-complete-one-signed-prime-screening-forces-log2-support-packing-and-a-smaller-archimedean-budget.md). No theorem that the first null mode is one-signed, no exclusion of complete screening, and no RH consequence is claimed.

Suppose the first null mode can be chosen `v>=0` and every active prime-power autocorrelation vanishes. The powers of two already impose a rigid geometric consequence. Since

`C_v(k log 2)=0`

and the integrand is nonnegative, the nonzero set `E={v>0}` cannot contain two points in the same `log 2` lattice fiber. Hence

`|E|<=log 2`.

So complete arithmetic screening is not merely absence of a discrete source term. It forces the mode to be a measurable selector modulo the smallest prime-power lattice. First-crossing geometry simultaneously requires full essential span, so the screened mode must be sparse across the whole aperture rather than a short compact bump.

WI-281 converts this support restriction into the continuous source budget. The positive part of the Suzuki archimedean kernel is symmetric decreasing, so Riesz rearrangement shows that the largest possible positive contribution under the packing constraint is exactly

`K_pack=(1/2) lambda_max(T_L)`,  `L=log 2`,

where `T_L` is the positive kernel compressed to one interval of length `L`. Finite support makes this strictly smaller than the unrestricted convolution budget:

`0<K_pack<K_+`.

Therefore complete one-signed screening implies the sharpened necessary condition

`2 int_(a/2)^a lambda_r dr <= K_pack<K_+`.

This is a source-specific bootstrap that generic cut geometry cannot see. The assumption used to erase the prime source feeds back and reduces the archimedean freedom available to do the erasing. In that sense screening consumes its own continuous budget.

The strongest current interpretation is not that screening is impossible, but that **discrete vanishing and continuous admissibility are coupled by the arithmetic lag semigroup**. Power-of-two packing is the first exact instance. Any stronger contradiction must use additional prime lags, the null equation, first-crossing structure, nodal regularity, or another source constraint to shrink the admissible class below the actual spectral-area requirement.

**Boundary.** The packing argument uses `v>=0`; it does not apply directly to sign-changing null modes because zero autocorrelation no longer forces pointwise disjointness. `K_pack<K_+` is strict but not numerically shown to contradict the source reserve. The result supplies a sharper necessary condition, not an exclusion theorem.
