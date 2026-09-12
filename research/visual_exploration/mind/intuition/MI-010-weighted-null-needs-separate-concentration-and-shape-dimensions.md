# MI-010 — Weighted prime-phase nulls have separate concentration, shape, support-transfer, and moment-complexity regimes

**Evidence level:** supported by weighted-Haar calculations and deterministic transfer theorems VIS-173--VIS-178.

For positive weights `w_j`, put

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

VIS-173 shows that `D_2` and `D_4` control different parts of the matched Haar null. `D_2` governs leading concentration/effective support, while `D_4` governs whether standardized shape Gaussianizes. The bulk can concentrate while heavy low-prime coordinates keep a non-Gaussian law.

VIS-174 transfers fixed moments of the matched Haar law to deterministic continuous prime-log averaging. VIS-177 sharpens its character geometry: after balancing positive and negative multiplicities, every nonzero character in the `k`th moment has

\[
|\lambda|\ge\frac1{2y^{\lfloor k/2\rfloor}},
\]

so the deterministic/Haar discrepancy is controlled at scale

\[
\frac{y^{\lfloor k/2\rfloor}D_2(y)^{k/2}}H.
\]

VIS-175 and VIS-176 turn the weight geometry into full weak-law regimes. In the square-summable phase the limit is the infinite weighted Haar convolution under its transfer gate. In the Lindeberg phase, vanishing maximal normalized weight plus transfer of every fixed moment gives `N(0,1/8)`. For prime-power weights, VIS-177 already extends that Gaussian conclusion to every subpolynomial cutoff `y(H)=H^{o(1)}`.

VIS-178 shows that a **fixed positive-power support law is not automatically outside the null either**. For `w_p=p^{-\alpha}`, `0\le\alpha<1/2`,

\[
D_2(y)\sim\frac{1-2\alpha}{(1-\alpha)^2}\frac y{\log y},
\]

and at `\alpha=1/2`,

\[
D_2(y)\sim\frac{4y}{(\log y)^2\log\log y}.
\]

Let `e_k=\lfloor k/2\rfloor+k/2`. For `y=H^\delta`, the `k`th deterministic moment still matches Haar whenever

\[
\boxed{\delta\le1/e_k,}
\]

including the critical equality because the residual logarithmic denominator diverges. A fixed panel through order `K` therefore transfers for `\delta\le1/K` when `K` is even and `\delta\le1/(K-1/2)` when `K` is odd.

The null boundary is consequently indexed by **test complexity**, not just by support growth. For any fixed `\delta>0`, sufficiently high moment order eventually leaves the proved wedge, so VIS-178 does not give a full polynomial-support weak law. But a finite-order statistic cannot claim source sensitivity merely because its support is polynomial; it must first exceed its own order-matched transfer threshold.

A source-sensitive statistic must therefore change at least one actual gate: use moment/functional complexity growing with support, leave the order-dependent polynomial wedge, change sampling to Gram/discrete geometry, use a source-bearing hybrid/zero variable, enter a rare/shrinking or unbounded functional class, or otherwise leave the normalized additive prime torus.

**Boundary.** The transfer thresholds are sufficient, not known necessary. VIS-178 does not control `k->infinity`, all moments at one fixed `\delta>0`, moving extremes, Gram/discrete sampling, hybrid variables, or stronger-than-moment functionals. Failure of the bound beyond `1/e_k` is not evidence that the matched null fails.