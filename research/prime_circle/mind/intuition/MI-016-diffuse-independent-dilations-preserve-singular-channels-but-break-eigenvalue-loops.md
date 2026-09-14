# MI-016 — Diffuse independent dilations preserve singular channels but break eigenvalue loops

**Evidence level:** exact consequence of [PC-295](../../findings/PC-295-diffuse-boundary-log-singular-values-converge-to-classical-green-spectrum.md) and [PC-296](../../findings/PC-296-diffuse-boundary-log-eigenvalues-collapse-to-zero.md) under their common diffuseness hypothesis `(log q)^2 sqrt(q beta_q/N)->0`. No pseudospectral collapse, joint-profile theorem or non-diffuse statement is claimed.

The diffuse boundary-log finite section has a sharp nonnormal split. PC-295 proves that its normalized singular values converge to the nonzero classical Green sequence, so the fixed low Fourier channels survive with order-one singular strength. PC-296 proves simultaneously that the entire normalized eigenvalue set collapses to zero in spectral radius.

The mechanism is relational. For a fixed low-frequency block the matrix factors as

`A = X D Z*`.

The same-side Gram matrices `X*X` and `Z*Z` approach the identity under diffuse source dilations, so the diagonal Fourier amplitudes in `D` survive as singular values. But the nonzero eigenvalues are governed by the small matrix

`D Z*X`.

Diffuse independent left/right dilations make the **cross-Gram** `Z*X` vanish. The channels remain individually strong but fail to close into spectral loops. PC-296 then uses the operator-small high-frequency tail through a resolvent argument, rather than an invalid spectral-radius Lipschitz step, to show that no order-one eigenvalues reappear.

This distinction is useful beyond the specific matrix calculation. Nonnormal information is not one currency. Same-side channel strength controls singular values; left/right recurrence or loop closure controls eigenvalues. A source can preserve the former while averaging away the latter.

For Prime Circle this closes the raw-eigenvalue escape that remained after absolute singular-spectrum classicalization. The surviving nonnormal question must keep more than the eigenvalue set: pseudospectral amplification, transient response, a joint family of profiles, cross-level coupling, or another observable that retains source-sensitive left/right relations before cross-Gram averaging. An exceptional non-diffuse source regime is also outside the theorem.

**Boundary.** Quasinilpotent eigenvalue scale does not imply small pseudospectrum or small operator norm; indeed PC-295 gives the opposite operator-norm limit. The result is averaged under the stated diffuseness condition and is reproduced by the matched diffuse controls. The durable insight is the separation between strong channels and closed loops, not a general theorem that nonnormality is source-blind.