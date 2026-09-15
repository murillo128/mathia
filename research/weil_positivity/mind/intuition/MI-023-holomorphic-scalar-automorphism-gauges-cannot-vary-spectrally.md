# MI-023 — Holomorphic scalar automorphism gauges cannot vary spectrally

**Evidence level:** exact Schwarz--Pick rigidity and Weil-positivity consequence from [WP-309](../../findings/WP-309-jointly-holomorphic-scalar-boundary-automorphism-families-are-constant.md)

A scalar positivity-preserving boundary coordinate cannot gain genuine spectral-variable freedom merely by letting its automorphism parameters depend holomorphically on the spectral parameter. If `Phi: Omega x H -> H` is jointly holomorphic and every slice `Phi_z` is a biholomorphic automorphism of the upper half-plane, then `Phi_z` is independent of `z`.

After Cayley conjugation to the disk, put `a(z)=F(z,0)` and `b(z)=partial_u F(z,0)`. Schwarz--Pick equality gives `|b|=1-|a|^2`. Since `b` is nonvanishing holomorphic, `log|b|` is harmonic, while

`Delta log(1-|a|^2) = -4|a'|^2/(1-|a|^2)^2`.

Hence `a'=0`; then `|b|` is constant and holomorphy makes `b` constant. A disk automorphism is determined by its value and derivative at one point, so the whole family is constant.

For the reflected Mangoldt Herglotz response this collapses the proposed `z`-dependent scalar **gauge** escape back to WP-308: preserving the logarithmic end leaves only a positive affine output map, which cannot reverse the wrong positive curvature.

The boundary is exact. Noninvertible Herglotz self-maps, source-moment Schur transforms, compressions/generalized resolvents, added positive channels and operator-valued boundary spaces evade the theorem because they are genuinely new structure rather than coordinate freedom. Any such route must therefore justify its added data and positivity intrinsically.