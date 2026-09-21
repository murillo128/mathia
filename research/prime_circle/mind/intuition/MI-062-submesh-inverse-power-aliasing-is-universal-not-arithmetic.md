# MI-062 — Submesh inverse-power aliasing is universal, not arithmetic

**Evidence level:** asymptotic synthesis from [PC-385](../../findings/PC-385-submesh-inverse-power-chords-have-universal-aliasing-phase-diagram.md), closing the submesh loophole left by PC-384. The singular quadrature/aliasing ingredients are classical; the line-specific content is the exact root-pushforward reduction and prime/composite falsification.

For every fixed positive inverse-power exponent, the normalized positive multiplier is exactly the pushforward of a one-point singular probability measure under `z -> z^m`. Its nonconstant Fourier modes are therefore just source Fourier coefficients sampled at multiples of `m`, with nonnegative coefficients and no hidden angular cancellation.

In the genuinely submesh regime `m eta_m ->0`, all asymptotic phases are still universal. For `alpha<1/2`, the measure weakly uniformizes, while the anchor may be flat, have a finite universal spike, or diverge according to `m eta_m^(2alpha)`. At `alpha=1/2`, the same trichotomy is controlled by `m eta_m log(1/eta_m)`. For `alpha>1/2`, the pushed-forward mass concentrates at the anchor. None of these regimes depends on whether `m` is prime or composite.

Together with PC-383--PC-384, this closes both exact-mesh and submesh cutoff scaling for fixed positive inverse-power common-anchor modulus. Altering only the scalar singular exponent or cutoff scale cannot create prime-sensitive information after root-fiber averaging.

**Boundary.** Phase/nonnormal information, source-sensitive profiles, nonlinear/tensor observables, varying exponents with additional structure, and cross-level couplings remain outside the scalar positive pushforward. A successor must retain arithmetic information before this scalarization rather than search for another cutoff regime of the same inverse-power modulus.