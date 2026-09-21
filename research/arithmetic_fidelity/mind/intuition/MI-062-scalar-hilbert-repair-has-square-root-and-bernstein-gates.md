# MI-062 — Scalar Hilbert repair has square-root and Bernstein gates

**Evidence level:** exact metric synthesis from [AF-468](../../findings/AF-468-any-scalar-hilbert-repair-must-amplify-tv-at-least-square-root.md) and [AF-469](../../findings/AF-469-exact-scalar-hilbert-repairs-obey-local-bernstein-sign-laws.md), extending the power-law boundary in AF-466--AF-467. The cube/type and Bernstein/Schoenberg ingredients are classical; the line-specific content is their transfer to the full probability-law source.

For the unrestricted TV simplex, a scalar radial transform cannot evade the paired-mixture obstruction by choosing a clever non-power profile. If a Hilbert representation has complexity-independent two-sided distortion in a transformed distance `phi(d_TV)`, then along `t=2/k`

`phi(t) >= c sqrt(t)`,

and under monotonicity the same lower scale holds throughout a neighborhood of zero. Relative to the original TV metric, any such repair therefore has singular forward sensitivity: the amplification ratio `phi(t)/t` must diverge at least like `t^(-1/2)` on the forced scales.

Exact radial repair is more rigid. Writing the squared transformed distance as `g=phi^2`, exact Hilbert embeddability of every finite subset of the simplex forces alternating finite differences of `g` at every scale below half the simplex diameter. Under smoothness, `g'` is completely monotone on `(0,1)`: `g` has the local Bernstein sign hierarchy. Bernstein transforms are therefore not merely a convenient sufficient family; their complete-alternation signature is locally necessary for exact scalar repair.

The durable distinction is between **bounded-distortion scale** and **exact radial structure**. Square-root-or-stronger amplification is necessary already for uniform distortion, while exactness additionally imposes the finite-difference sign laws. Neither statement classifies non-radial/state-dependent lifts, and neither supplies arithmetic selectivity.

**Boundary.** These obstructions use unrestricted growing mixture complexity. A physical arithmetic source can escape only through a proved restriction that excludes the weighted cube/hyperrectangle tests, or by using a non-radial representation whose extra structure is itself source-forced. Even then, the downstream theorem must be shown compatible with the changed metric and any later quotient or compression.