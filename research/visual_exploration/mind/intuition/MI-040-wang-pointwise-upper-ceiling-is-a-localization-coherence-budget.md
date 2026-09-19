# MI-040 — Wang's upper pointwise ceiling has narrowed from support geometry to exceptional finite-height phase coherence

**Evidence level:** exact synthesis from [VIS-298](../../findings/VIS-298-wang-gamma-recentering-removes-moving-h-barrier.md) through [VIS-309](../../findings/VIS-309-wang-bohr-time-haar-equivalence.md), using Wang's displayed localization/mean-value identities, the classical weighted Hilbert inequality and the matched support/phase controls audited there.

The upper pointwise boundary in Wang's short-interval pair statistic has moved repeatedly because generic estimates were applied before the exact structure of their load-bearing terms was exposed.

VIS-298 removes the lower moving-source crossover by exact gamma recentering. VIS-299--VIS-301 decompose the apparent localization ceiling and show that only one inside--outside coherence term is load-bearing; the unconditional Vinogradov--Korobov zero-free region suppresses it enough that the first generic `H`-scale obstruction moves into the interior mean-value estimate.

VIS-302 specializes the coefficient majorant from `x log^2 x` to `x log x`. VIS-303 specializes the support and deletes the power-of-two/odd-shift sector. VIS-304 specializes the prime-power frequency geometry and obtains the absolute Hilbert-spacing cost `O(x log log x)`.

VIS-305 applies a parity- and density-matched Bernoulli control to that absolute norm. Its reciprocal-spacing cost is already `Theta(x log log x)`, so the absolute `log log x` layer is generic under density/parity matching. VIS-306 strengthens the control to the signed endpoint remainder and gets `o_p(H)` at `H~x log log x`.

VIS-307 then keeps the actual prime-power support and every Wang coefficient magnitude, randomizing only one independent phase per support point. Phase orthogonality gives a signed second moment `O(x log^3 x)`, so exact support and coefficient magnitudes still do not explain the boundary.

VIS-308 preserves substantially more of the arithmetic phase geometry. One Steinhaus phase is assigned per base prime and extended completely multiplicatively, `f(p^k)=f(p)^k`. All harmonic relations among powers of the same prime therefore survive exactly. The additional same-base torus-character collisions are negligible, and the same `O(x log^3 x)` second-moment scale persists. Hence **same-base multiplicative phase coherence is not sufficient** to sustain an `H`-scale signed remainder.

VIS-309 then tests the next candidate—collective deterministic alignment across distinct primes—against the actual one-parameter time orbit. For fixed `x` and `H`, the deterministic phase point

`p -> p^(-it)`

moves on the base-prime torus. Rational independence of the prime logarithms makes its Bohr mean agree exactly with Haar averaging for the quadratic signed remainder: the only surviving time-average frequencies are the same multiplicative character collisions already counted by the completely multiplicative Steinhaus model. Consequently the long-time mean square is still `O(x log^3(3x))`, and at `H~x log log x` the set of times with `|R_(x,H)(t)|>=eta H` has Bohr upper density tending to zero in the corresponding large-`x` calibration.

Thus generic deterministic common-time alignment is not the missing mechanism either. The actual arithmetic phase orbit is Haar-typical **in the long-time quadratic mean for every fixed frequency set**. Any pointwise obstruction that survives VIS-309 must exploit what the Bohr limit discards: exceptional finite heights, a finite observation interval too short for the growing log-prime frequency set to equidistribute, a moving joint regime `x=x(T)`, or another endpoint statistic not controlled by the same quadratic torus average.

The reusable lesson is a layered survivor test. Preserve the exact object until the first inequality that discards structure; match support statistics; preserve exact support; restore multiplicative phase relations; then compare the actual deterministic orbit with the resulting Haar control. A nominal critical scale becomes arithmetic only after the relevant **finite-height/moving-frequency** regime defeats a control that already matches its infinite-time torus average.

**Boundary.** VIS-309 is a Bohr-mean/upper-density statement for fixed finite frequency sets before the relevant limit. It is not a pointwise bound at a prescribed height, a quantitative finite-window equidistribution theorem, or a theorem uniform when `x=x(T)` grows. It therefore removes generic long-time phase alignment as an explanation but leaves exceptional-height and moving-frequency coherence genuinely open. The RH-equivalent continuation route remains separate.