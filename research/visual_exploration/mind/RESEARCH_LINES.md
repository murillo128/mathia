# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Move beyond fixed-power source escape and analytic reformulations of the target divisor

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-038-wang-source-continuation-is-rh-equivalent-in-the-first-half-plane`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

VIS-282--VIS-284 identify the fixed-source coefficient-scale arithmetic profile `Q_gamma(x)=S_D(x)+C_Lambda/x^2` and show that fixed-interior packet localization is a bounded linear projection problem. A Laplace-null packet of support diameter `b` loses response like `b||h||_1`; keeping a nonzero localized signal therefore costs inverse-width conditioning and amplifies unresolved errors by the same factor.

VIS-285 closes the left source boundary for this isolated profile: on the first source cell, `Q_gamma(e^(2pi q))=2 C_Lambda cosh(4pi q)`, so `q=0` is regular with zero first derivative rather than singular. VIS-286 closes the opposite isolated-profile escape: `Q_gamma(x)=log x+o(1)`, so after subtracting the universal linear law there is no persistent bounded residual at `q->infinity` for bounded-total-variation translating packets.

VIS-287--VIS-291 then move from the isolated diagonal to Wang's complete pair statistic in a genuine moving-source regime. For every compact power panel `x=T^beta` with `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly `F_I(T^beta)=(H beta log T)/(2pi)+residual`. The successive audit removes the apparent `H` frontier and propagates the strongest standard unconditional PNT remainder through Wang's decomposition. The complete residual is bounded by `H exp(-c (log T)^(3/5)(loglog T)^(-1/5))` for some `c>0` depending on the fixed panel. Thus a fixed power-law source escape strictly inside `(0,theta)` carries no larger hidden coefficient-scale profile after the linear baseline is removed.

VIS-292 narrows the remaining “symmetric smoothing” explanation. On logarithmic source scale, Wang's squared-von-Mangoldt profile is exactly convolution with `K(u)=e^(-2|u|)`, the Green kernel of `4-d^2/du^2`. Its Fourier multiplier `4/(4+xi^2)` has no real zeros, and the Mellin multiplier `4/(4-w^2)` has no zeros in its strip. The smoothing attenuates high frequencies but has no exact blind mode; any improvement beyond the Korobov--Vinogradov envelope must come from arithmetic structure of the weighted prime-power source.

VIS-293 closes the most direct analytic-continuation escape for that source. Its Dirichlet transform satisfies

`D(s)=sum Lambda(n)^2 n^(-s)=(log zeta)''(s)+A(s)`,

with `A` holomorphic on `Re(s)>1/2`. Since Wang's Green multiplier is nonzero in the same first-half-plane, meromorphic continuation of the exact source profile cannot cancel the nontrivial zeta poles. After removing the pole at `s=1`, holomorphy on `Re(s)>1/2` is equivalent to RH. Analytic continuation of the source transform is therefore a reformulation of the target divisor, not an independent source-specific cancellation theorem.

The live frontier is now genuinely real-axis and nonuniform: `beta(T)` approaching `0` or the short-interval ceiling, packets whose support/variation grow with `T`, source-boundary scalings outside one fixed compact power panel, or a real-axis estimate for the weighted prime-power source with an explicit zero-free consequence that does not assume the desired continuation. Claims based only on fixed-power escape, a boundary singularity, a persistent large-source residual, an exact smoothing null, or first-half-plane source holomorphy are already classified.

## Keep packet conditioning, source arithmetic, theorem uniformity and analytic continuation separate

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, distance to the admissible source boundary, prime-power source measure, smoothing multiplier, the uniformity range of Wang's remainder and the analytic domain of the source Dirichlet transform. Exact invertibility of the Green filter is not stable recovery: applying `4-d^2/du^2` amplifies high log-frequencies quadratically. Conversely, strong smoothing does not imply information loss when the multiplier is nonzero, and exact meromorphic access to the source transform does not supply a new proof mechanism when its first-half-plane poles are exactly the zeta divisor.

A useful next probe must therefore declare its moving family before asymptotics, charge the corresponding norm growth, and identify a real-axis arithmetic term that remains after the linear source baseline and known PNT envelope are removed. Only then can a visual/source-localization effect be interpreted as new mathematical information rather than conditioning, analytic continuation of the target, or a repackaging of classical prime-number-theorem error.
