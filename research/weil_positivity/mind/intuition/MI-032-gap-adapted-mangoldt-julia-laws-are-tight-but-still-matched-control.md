# MI-032 — Gap-adapted Mangoldt Julia laws are tight but still matched-control realizable

**Evidence level:** literature+exact-derived compactness and subsequential classification from [WP-319](../../findings/WP-319-gap-adapted-mangoldt-julia-laws-are-tight-but-matched-control.md), interpreted through the exact derivative-biased-law reduction of WP-318.

WP-315 shows that scaling reflected Mangoldt atoms by their own mass `a_p~log p/p` is not locally compact: bounded prime clusters collapse many comparable atoms into every fixed normalized neighborhood. WP-319 changes the affine unit to the **actual adjacent support gap**.

Along infinitely many bounded gaps, pass to a subsequence where the next prime-power support point is `p_j+d` with fixed integer `d`. Center at the support-free logarithmic midpoint and scale by

`g_j=log((p_j+d)/p_j) ~ d/p_j`.

The derivative-biased probability laws are then tight. After a further subsequence, every limit has the explicit form

`rho = Z^(-1) sum_h theta_h/(h-d/2)^2 delta_(1/2-h/d)`,

with `theta_0=1`, no support at the normalized gap interior, and each coefficient `theta_h` either `0` or `1/k` according to the limiting local prime-power pattern. The source-specific tangent is therefore a shifted arithmetic lattice with inverse-square derivative bias and quantized decorations.

This repairs the compactness failure but not the positivity problem. The normalized Julia response is exactly `-K_rho`. Because the support stays away from the node, WP-318's matched-control construction produces a non-arithmetic positive Herglotz measure whose derivative-biased law is **the same `rho`**. Its normalized Julia response, including its Pick sign, is identical.

The reusable distinction is: a canonical normalization can expose a real arithmetic fingerprint without making the theorem that acts on the normalized object source-selective. Here the source information is in the particular `theta_h`, but scalar Julia positivity only uses that `rho` is a probability law.

A viable next scalar theorem must therefore constrain the **family or coupling** of these Mangoldt laws in a way that cannot be copied by choosing a positive measure with the same law: for example a relation across gaps/scales, a restriction involving the Gamma/global counterterm, or another invariant not determined by one normalized probability law alone.

**Boundary.** WP-319 gives subsequential, not unique, gap-scale limits and does not assert a canonical distribution of the `theta_h`. Tightness and lattice structure are not RH progress by themselves. Any cross-gap rigidity or finite--archimedean coupling remains unproved.