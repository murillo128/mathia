# MI-021 — Bounded source resolvents cannot reach Gamma; the first natural Mangoldt Herglotz escape has universal leading log and wrong subleading curvature

**Evidence level:** exact for the bounded-resolvent obstruction and pole-normalized Mangoldt Herglotz asymptotic in [WP-304](../../findings/WP-304-bounded-source-resolvents-are-too-small-pole-normalized-mangoldt-energy-yields-only-an-oriented-universal-logarithmic-herglotz-tail.md), sharpened by the exact first-subleading comparison in [WP-305](../../findings/WP-305-canonical-reflected-mangoldt-herglotz-has-the-wrong-next-order-gamma-curvature.md). The Herglotz/Nevanlinna representation, weighted Mertens estimates, Stieltjes constants and digamma asymptotics used there are classical. No Weil-positivity theorem or derivation of the exact Gamma factor is claimed.

For any self-adjoint source operator `H` and bounded incidence/compression `V`,

`M_V(z)=V^*(H-z)^(-1)V`

has finite compressed spectral mass and `||M_V(iy)||<=||V||^2/y`. Ordinary bounded source incidence is therefore categorically too small at high energy: it decays and cannot produce the logarithmically growing Gamma/digamma scale.

The pole-normalized positive-energy Mangoldt measure

`mu_+ = sum_(n>=2) Lambda(n)/(n+1) delta_(log n)`

crosses that mass barrier. Its cumulative mass is

`M(R)=R+C_+ + epsilon(R)`, `epsilon(R)->0`,

with an integrable remainder, so the canonical regularized Herglotz transform has

`Re m_+(iy)=-log y+B-A_0/y^2+o(y^-2)`

and

`Im m_+(iy)=pi/2+C_+/y+o(y^-1)`.

The leading real logarithm is not arithmetic-specific: every positive measure with cumulative mass `R+O(1)` has the same first asymptotic, with Lebesgue measure as an exact matched control. The canonical even `+/-log n` carrier cancels that real logarithm entirely on the imaginary axis, so a one-sided orientation is already required before any Gamma comparison.

WP-305 shows that the obvious reflection/orientation repair fails at the next real order for the **actual** Mangoldt weights. The zeroth moment of the counting remainder is

`A_0 = gamma^2 + 2 gamma_1 + sum_(n>=2) Lambda(n) log n/[n(n+1)] > 0`.

Reflecting the measure to the negative half-line flips the leading logarithm to the desired orientation but also forces

`Re m_-(iy)=log y-B+A_0/y^2+o(y^-2)`.

The Riemann archimedean factor instead has

`Re psi(1/4+iy/2)=log(y/2)-1/(24y^2)+O(y^-4)`.

Thus the first nonconstant even real curvature is source-specific but has the **wrong sign**. An additive real renormalization changes only the constant, and positive spectral dilation cannot flip the sign of the `y^-2` term. Reflection plus constants/dilation therefore cannot turn this source into the Gamma sector.

This produces a useful two-stage diagnostic. Reaching `log y` only identifies the correct infinite-mass class and carries no arithmetic content. Passing to the exact Mangoldt source supplies arithmetic subleading information, but that information falsifies the simplest Gamma identification. A viable completion must derive an additional operation that changes the source remainder before exact archimedean matching while preserving independent positivity.

Admissible escapes include a source-forced spectral translation, extra boundary/archimedean sector, quotient/compression, genuinely nonlocal finite--archimedean coupling, determinant/scattering construction or nonlinear spectral observable. They remain admissible only if Mathia derives them independently of the target coefficient. Selecting one specifically to turn `+A_0` into `-1/24` would be programmable target fitting.

**Boundary.** WP-305 does not prove that every positive unit-density source has positive curvature; the sign is specific to the exact weights `Lambda(n)/(n+1)`. It does not exclude unbounded boundary maps, additional sectors or nontrivial couplings that alter the remainder. The durable conclusion is narrower: bounded resolvents are too small, the first infinite-mass logarithm is universal, and the canonical reflected Mangoldt source already disagrees with Gamma at the first subleading real term.