# MI-021 — Bounded source resolvents cannot reach Gamma, and the canonical one-sided Mangoldt carrier has the wrong affine curvature class

**Evidence level:** exact for the bounded-resolvent obstruction and pole-normalized Mangoldt Herglotz asymptotic in [WP-304](../../findings/WP-304-bounded-source-resolvents-are-too-small-pole-normalized-mangoldt-energy-yields-only-an-oriented-universal-logarithmic-herglotz-tail.md), sharpened by the first-subleading comparison in [WP-305](../../findings/WP-305-canonical-reflected-mangoldt-herglotz-has-the-wrong-next-order-gamma-curvature.md) and the support-preserving translation obstruction in [WP-306](../../findings/WP-306-support-preserving-spectral-translations-cannot-fix-reflected-mangoldt-gamma-curvature.md). No Weil-positivity theorem or derivation of the exact Gamma factor is claimed.

For any self-adjoint source operator `H` and bounded incidence/compression `V`,

`M_V(z)=V*(H-z)^(-1)V`

has finite compressed spectral mass and decays like `1/y` on the imaginary axis. Ordinary bounded source incidence is therefore categorically too small to produce the logarithmically growing Gamma/digamma scale.

The pole-normalized positive-energy Mangoldt measure

`mu_+ = sum_(n>=2) Lambda(n)/(n+1) delta_(log n)`

crosses that mass barrier. Its cumulative mass is `R+O(1)`, and its regularized Herglotz transform has a leading `-log y` real term. That logarithm is not arithmetic-specific: every positive unit-density measure has the same leading scale, while canonical evenization cancels it on the imaginary axis.

WP-305 shows that the obvious reflection repair fails at the first source-specific even order. Reflection gives the desired `+log y` orientation but forces

`Re m_-(iy)=log y-B+A_0/y^2+o(y^-2)`, `A_0>0`,

whereas the Riemann archimedean sector has coefficient `-1/24`. Constants and positive dilation cannot change this sign.

WP-306 proves that ordinary source recentering cannot rescue it either while preserving the intrinsic one-sided spectrum. Translating energies by `t` gives exactly

`A_t=A_0-tC_+ + t^2/2`.

The carrier remains in `[0,infinity)` precisely for `t>=-log2`, and on that whole range `A_t` is strictly increasing with

`A_t >= A_(-log2) > 583/60000 > 0`.

Thus the canonical one-sided Mangoldt source occupies the wrong **affine curvature class** for Gamma: reflection, additive renormalization, positive dilation and every support-preserving translation preserve the sign mismatch.

The surviving completion must add a genuinely new source-forced operation before exact Gamma matching. Possibilities include an independently derived archimedean/boundary sector, quotient/compression, nonlocal finite--infinite coupling, determinant/scattering construction or another observable whose positivity is proved separately. A translation that creates negative low-energy states is outside WP-306, but it is meaningful only if that spectrum is forced by the source geometry rather than selected to fit `-1/24`.

**Boundary.** WP-306 is source-specific and support-sensitive. It does not exclude arbitrary positive measures, unbounded boundary maps, extra sectors, nonlocal couplings or translations below `-log2`. The durable conclusion is categorical: reaching `log y` is too weak, the canonical source has the wrong first nonuniversal curvature, and its entire natural support-preserving affine family remains on the wrong side.