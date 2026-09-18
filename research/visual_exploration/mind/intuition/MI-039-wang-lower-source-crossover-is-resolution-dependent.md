# MI-039 — Wang's moving lower-source crossover disappears after exact gamma recentering

**Evidence level:** exact error-budget and explicit-formula synthesis from [VIS-294](../../findings/VIS-294-wang-lower-moving-source-sqrtlog-crossover.md), [VIS-295](../../findings/VIS-295-wang-gamma-subtracted-residual-relative-crossover.md), [VIS-296](../../findings/VIS-296-wang-relative-boundary-reduces-to-explicit-formula-remainder-mean.md), [VIS-297](../../findings/VIS-297-wang-boundary-remainder-mean-is-gamma-normalization.md), and [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md), using the Wang/PNT inputs audited in those findings.

Write `H=T^theta` and `L=log T`. The earlier lower-source analysis first exposed two apparent thresholds. Keeping Wang's coarse gamma baseline visible led to an absolute-`H` error wall near `x~sqrt(L)`, while subtracting that leading term moved the relative boundary to `x^2 log x~L`. VIS-296--VIS-297 then showed that the finite relative crossover was only the deterministic gamma constant hidden by the coarse baseline.

VIS-298 completes the correction at absolute resolution. Returning to the exact Landau decomposition and recombining the gamma factor before estimating cross terms gives, for every fixed `lambda<theta` and every moving source `x=x(T)->infinity` with `x<=T^lambda`,

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

Thus the `sqrt(log T)` absolute boundary was also an artifact of proof packaging. The terms that looked like `H sqrt(L)/x` and `H L/x^2` were not independent source errors: they came from placing a deterministic gamma contribution inside a coarse remainder and then applying Cauchy--Schwarz before exploiting its exact structure. The absolutely convergent right-half-plane zeta term is small at the required scale once `x->infinity`.

The reusable diagnostic is stronger than “normalize deterministic terms first.” **Before promoting a moving error wall to a candidate arithmetic transition, recombine every exact deterministic component that the proof split only for estimation convenience and re-evaluate the cross terms in their native frequency structure.** A threshold created by an inequality between artificial pieces need not survive in the original observable.

For Wang's statistic, no moving lower-source branch remains under a fixed ceiling. Changing only the rate at which `x(T)->infinity` cannot reopen it. The genuine residual questions lie elsewhere: improve the fixed-power arithmetic source estimate with information weaker than the RH-equivalent half-plane condition, prove uniformity as the upper exponent approaches `theta`, or formulate a distinct bounded-source problem with its own destination-sensitive residual.

**Boundary.** VIS-298 assumes one fixed `lambda<theta` and `x->infinity`. It does not give a bounded-source asymptotic, improve the Korobov--Vinogradov arithmetic input, or justify a source exponent drifting to `theta`. Nor does it prove that no other statistic has meaningful lower-scale structure; it closes this moving-source interpretation of Wang's complete statistic at absolute `H` resolution.