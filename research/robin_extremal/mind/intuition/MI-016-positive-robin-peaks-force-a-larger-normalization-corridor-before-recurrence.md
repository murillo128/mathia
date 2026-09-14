# MI-016 — Positive Robin peaks force a PNT-priced normalization corridor before recurrence

**Evidence level:** exact for the colossally abundant recurrence geometry through [RE-108](../../findings/RE-108-quantitative-robin-peaks-force-inter-block-normalization-corridors.md)--[RE-109](../../findings/RE-109-pnt-regular-event-sweeps-stretch-inter-block-robin-recovery-corridors.md), combined with the false-RH quantitative block family and the intra-fan transport of RE-107. No contradiction to false RH and no RH consequence is claimed.

RE-108 shows that a quantitative positive Robin state cannot return to a nonpositive CA state before the denominator normalization grows by at least `R_C Y log Y`, with `Y=log C`. That bound is sharp if one remembers only monotonicity of `sigma(n)/n`; a frozen-numerator control saturates it.

RE-109 restores a source constraint that the matched control discards. The same prime-layer event atoms generate both the numerator increment and the physical logarithmic mass. Their cumulative event staircase satisfies a Vinogradov--Korobov PNT discrepancy

`Phi(x)=x+O(x E(x))`,

with `E(x)=exp[-a(log x)^(3/5)(log log x)^(-1/5)]`. Coupling each event atom to the physical mass interval it creates rewrites Robin recovery as a quadrature error between `g(s)=1/(s log s)` and `g(eta_e)`.

On a corridor of scale `Y`, this gives

`|h(C)-h(D)| << (V-Y) E(Y)/(Y log Y)`.

Hence a positive height `h(C)` requires, unless the corridor already exceeds a fixed multiple of `Y`,

`V-Y >> h(C) Y log Y / E(Y)`.

For the false-RH quantitative states `h(C_b)>>Y_b^(-b)`, the recovery corridor therefore acquires the stretched-subpower factor `E(Y)^(-1)`. Successive block starts satisfy the same strengthened spacing, and their dyadic packing gains the reciprocal factor.

The key change is conceptual: **recovery time is now priced by source/event coherence, not only normalization monotonicity.** The frozen-numerator matched control is no longer source-admissible once the same PNT-regular atoms must create numerator and physical mass. But the resulting spacing remains subpower on the exponent scale and still does not contradict infinitely many false-RH blocks.

The next theorem must use selection-conditioned source phase, not merely a sharper global PNT error. One must show that CA-selected recovery intervals cannot keep the extremal sign/magnitude needed to saturate the quadrature bound, or couple Chebyshev and reciprocal-Mertens coordinates across those intervals so that the next quantitative witness cannot regenerate.

**Boundary.** RE-109 uses the global sup-norm PNT envelope for the event staircase and is sharp for that information class by a synthetic staircase control. It does not prove favorable discrepancy sign on CA-selected corridors, does not exclude recurrence, and does not propagate the RE-107 intra-fan debt unchanged to the next block.