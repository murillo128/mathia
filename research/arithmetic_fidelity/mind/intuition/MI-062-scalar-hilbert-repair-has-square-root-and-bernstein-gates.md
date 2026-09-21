# MI-062 — Scalar Hilbert repair has square-root and full-diameter complete-alternation gates

**Evidence level:** exact metric synthesis from [AF-468](../../findings/AF-468-any-scalar-hilbert-repair-must-amplify-tv-at-least-square-root.md), [AF-469](../../findings/AF-469-exact-scalar-hilbert-repairs-obey-local-bernstein-sign-laws.md), and [AF-470](../../findings/AF-470-replicated-private-atoms-force-full-diameter-complete-alternation.md), extending the power-law boundary in AF-466--AF-467. The cube/type and Bernstein/Schoenberg ingredients are classical; the line-specific content is their transfer to the unrestricted probability-law source.

For the unrestricted TV simplex, a scalar radial transform cannot evade the paired-mixture obstruction by choosing a clever non-power profile. If a Hilbert representation has complexity-independent two-sided distortion in a transformed distance `phi(d_TV)`, then along `t=2/k`

`phi(t) >= c sqrt(t)`,

and under monotonicity the same lower scale holds throughout a neighborhood of zero. Relative to the original TV metric, any such repair therefore has singular forward sensitivity: `phi(t)/t` must diverge at least like `t^(-1/2)` on the forced scales.

Exact radial repair is more rigid. Writing the squared transformed distance as `g=phi^2`, AF-470 replaces AF-469's half-diameter/concentration argument by an exact replicated-private-atom realization. For every `k>=1`, `x>=0`, and positive increments with `x+sum_i epsilon_i<=2`, exact Hilbert embeddability forces

`(-1)^(k-1) Delta_(epsilon_1)...Delta_(epsilon_k) g(x) >= 0`.

Thus complete alternation is necessary across the entire TV diameter, and the finite-difference statement needs no continuity assumption. If `g` is smooth, `(-1)^(k-1) g^(k)(x)>=0` throughout `0<x<2`, so `g'` is completely monotone on the full interior.

The key geometric mechanism is that a positive base distance `x` can be carried by vertex-private probability mass. Replication increases alphabet breadth without consuming extra TV diameter; the diagonal defect is only one `g(x)` term against a `2^m` replicated Walsh contribution, and vanishes after dividing by `2^m` and sending `m` upward. The previous half-diameter boundary was therefore a realization artifact, not remaining scalar freedom.

**Boundary.** The exact theorem uses unrestricted alphabet breadth; it does not by itself impose arbitrary-order constraints on a fixed finite-dimensional simplex, prove sufficiency of bounded-interval complete alternation, classify approximate/bounded-distortion embeddings, or constrain non-radial/state-dependent lifts. There is still no arithmetic specificity: the live question is whether the physical arithmetic source contains enough comparable mixture geometry to inherit the obstruction, or whether a source-forced non-radial structure survives downstream with actual arithmetic selectivity.