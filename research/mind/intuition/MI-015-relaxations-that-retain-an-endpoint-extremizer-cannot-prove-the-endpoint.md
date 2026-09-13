# MI-015 — A relaxation is exhausted when its extremizer already saturates the endpoint in the relevant currency

**Evidence level:** supported cross-line synthesis from [MC-276](../../mobius_cancellation/findings/MC-276-distributional-witness-normalization-christoffel-collapse.md), [PF-333](../../prime_flute/findings/PF-333-relative-square-root-sensitivity-remains-logarithmic-even-for-positive-insertions.md), [PF-334](../../prime_flute/findings/PF-334-hilbert-schmidt-relative-square-root-control-escapes-logarithmic-dimension-loss.md), and [WI-282](../../weil_inertia/findings/WI-282-complete-prime-screening-and-full-span-do-not-lower-the-log2-packing-budget.md). This is a diagnostic about the current relaxed classes, not a universal impossibility theorem.

A proposed simplification is exhausted when the relaxed admissible class still contains an exact or asymptotic extremizer at the forbidden budget **in the norm or loss actually used by the endpoint**. No sharper estimate using only the retained hypotheses can then create the missing gap.

In Möbius Cancellation, imposing the correct blind-point value and minimizing L2 classification error gives exactly the Christoffel kernel. The loss satisfies

`||Q-NB||_2^2 = ||1-Q||_2^2 - blind_mass`,

so the optimization becomes easy by subtracting the target atom itself. Better least-squares control within that formulation cannot exclude blind rows because the objective is algebraically insensitive to them.

In Weil Inertia, complete prime-power screening plus nonnegativity already allows the length-`log 2` packing optimizer, and qualitative full span can be added with vanishing-mass satellites while converging back to it. The relaxed supremum stays exactly `K_pack`. More forbidden prime lags or essential-span information cannot create a strict decrement unless the new hypothesis quantitatively excludes those near-extremizers.

Prime Flute adds the necessary norm check. In operator norm, PF-333 shows the generic positive relative-square-root class already has `asymp log r` sensitivity, so positivity alone cannot produce a dimension-free `S_infinity` theorem. But PF-334 proves that the same map is dimension-free in Hilbert--Schmidt norm, which is the currency PF-318 actually consumes. The operator-norm relaxation is exhausted, yet that does **not** obstruct the weaker endpoint. One must first verify that the bad extremizer lives in the destination norm being used.

The decisive workflow is therefore concrete: identify the relaxed class; compute or approximate its endpoint extremizers; check them in the exact destination functional; and ask which source-native hypothesis excludes them. If the relaxed extremizer already saturates the correct budget, reintroduce signed phase, an exact null equation, geometric localization or another source constraint. If the apparent obstruction exists only in a stronger norm than the endpoint needs, change currency rather than over-solving the problem.

**Boundary.** The three mechanisms are different: target subtraction, support-packing approximation and norm-dependent matrix sensitivity. The synthesis does not imply that every relaxation is useless or that the named source-specific refinements will succeed.