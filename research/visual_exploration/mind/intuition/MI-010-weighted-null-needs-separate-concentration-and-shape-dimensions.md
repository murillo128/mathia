# MI-010 — Weighted prime-phase nulls have separate concentration, shape, and full-law transfer regimes

**Evidence level:** supported by the weighted-Haar calculations and deterministic transfer theorems VIS-173--VIS-176.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

VIS-173 shows that `D_2` and `D_4` control different parts of the matched Haar null. `D_2` governs leading concentration/effective support, while `D_4` governs whether the first standardized correction Gaussianizes. The bulk can concentrate while a finite set of heavy low-prime coordinates keeps the law non-Gaussian.

VIS-174 shows that fixed moments of these matched Haar laws transfer to deterministic continuous prime-log averaging under the explicit horizon condition `y^k D_2(y)^(k/2)/H -> 0` for each declared order `k`.

VIS-175 and VIS-176 turn the weight geometry into a complete weak-law phase boundary. In the square-summable regime `sum_p w_p^2<infinity`, the full bounded-Lipschitz law converges under `yW_y^2/H -> 0` to the infinite weighted Haar convolution, which can retain a strictly non-Gaussian fourth cumulant. In the Lindeberg regime

\[
\max_p\frac{w_p}{\sqrt{Q_y}}\to0,
\]

if the VIS-174 gate holds for every fixed moment order, the deterministic vertical law converges instead to `N(0,1/8)`.

For prime-power weights `w_p=p^{-\alpha}` and any fixed polylogarithmic cutoff, these two theorems cover every `\alpha>=0`: the normalized law is Gaussian for `0<=\alpha<=1/2` and generally non-Gaussian infinite-Haar for `\alpha>1/2`. Both behaviors are representation-matched nulls. The change at `\alpha=1/2` is not a source discriminator.

A source-sensitive statistic must therefore leave more than one side of the square-summability boundary. It must use a different sampling rule, a source-bearing hybrid/zero variable, a rare/shrinking or unbounded functional beyond weak convergence, support growth outside the available transfer gates, or another observable not determined by the normalized additive prime torus.

**Boundary.** VIS-175--VIS-176 concern continuous vertical averaging and fixed bounded-continuous tests in their stated growth regimes. They do not cover Gram/discrete sampling, moving extreme thresholds, decoder singularities, hybrid variables, or arbitrary fast support growth.
