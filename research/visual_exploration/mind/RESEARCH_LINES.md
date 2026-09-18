# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond fixed-power source escape and generic smoothing explanations

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-037-laplace-null-localization-pays-an-inverse-width-conditioning-cost`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

VIS-282--VIS-284 identify the fixed-source coefficient-scale arithmetic profile

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`

and show that fixed-interior packet localization is a bounded linear projection problem. A Laplace-null packet of support diameter `b` loses response like `b||h||_1`; keeping a nonzero localized signal therefore costs inverse-width conditioning and amplifies unresolved errors by the same factor.

VIS-285 closes the left source boundary for this isolated profile: on the first source cell, `Q_gamma(e^(2pi q))=2 C_Lambda cosh(4pi q)`, so `q=0` is regular with zero first derivative rather than singular. VIS-286 closes the opposite isolated-profile escape: `Q_gamma(x)=log x+o(1)`, so after subtracting the universal linear law there is no persistent bounded residual at `q->infinity` for bounded-total-variation translating packets.

VIS-287--VIS-291 then move from the isolated diagonal to Wang's complete pair statistic in a genuine moving-source regime. For every compact power panel `x=T^beta` with `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly

`F_I(T^beta)=(H beta log T)/(2pi)+residual`.

The successive audit removes the apparent `H` frontier and propagates the strongest standard unconditional PNT remainder through Wang's decomposition. The complete residual is bounded by

`H exp(-c (log T)^(3/5)(loglog T)^(-1/5))`

for some `c>0` depending on the fixed panel. Thus a fixed power-law source escape strictly inside `(0,theta)` carries no larger hidden coefficient-scale profile after the linear baseline is removed.

VIS-292 narrows the remaining “symmetric smoothing” explanation further. On logarithmic source scale, Wang's squared-von-Mangoldt profile is exactly convolution with `K(u)=e^(-2|u|)`, the Green kernel of `4-d^2/du^2`. Its Fourier multiplier `4/(4+xi^2)` has no real zeros, and the Mellin multiplier `4/(4-w^2)` has no zeros in its strip. The smoothing attenuates high frequencies but has **no exact blind mode**; any improvement beyond the Korobov--Vinogradov envelope must come from arithmetic structure of the weighted prime-power source, not from an automatic spectral null of the kernel.

The live frontier is therefore concentrated in genuinely nonuniform regimes: `beta(T)` approaching `0` or the short-interval ceiling, packets whose support/variation grow with `T`, source-boundary scalings not contained in one fixed compact power panel, or a source-specific cancellation theorem for `D(s)=sum Lambda(n)^2 n^(-s)` that survives Wang's complete error budget. A claim based only on fixed-power escape, the left boundary singularity, a persistent large-source diagonal residual or an exact blind frequency of the symmetric kernel is now excluded.

## Keep packet conditioning, source arithmetic and theorem uniformity separate

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, distance to the admissible source boundary, prime-power source measure, smoothing multiplier and the uniformity range of Wang's remainder. Exact invertibility of the Green filter is not stable recovery: applying `4-d^2/du^2` amplifies high log-frequencies quadratically. Conversely, strong smoothing does not imply information loss when the multiplier is nonzero.

A useful next probe must therefore declare its moving family before asymptotics, charge the corresponding norm growth, and identify an arithmetic term that remains after the linear source baseline and the known PNT envelope are removed. Only then can a visual/source-localization effect be interpreted as new mathematical information rather than conditioning or a repackaging of classical prime-number-theorem error.
