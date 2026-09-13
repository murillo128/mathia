# MI-012 — Robin's sparse-host route has moved to the high-beta tail above roughly four fifths

**Evidence level:** exact for the host-to-frontier conversion through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md), the deformed-quadratic host reduction through RE-096, the ambient-packing obstruction through RE-097, the resonant/fourth-moment analysis through RE-098--RE-099, and the second-moment sparse-sampling splice through [RE-100](../../findings/RE-100-second-moment-sampling-pushes-the-sparse-host-bottleneck-past-four-fifths.md). The residual high-beta tail remains open.

After the higher-depth reductions, the residual bad hosts are sampled at `x(n)=eta_1^(-1)(eta_2(n))`, `n~X^(1/2)`. RE-095 shows that any fixed power saving for intervals of length `X^vartheta` with `vartheta<73/200` improves the Robin frontier. RE-096 supplies stable logarithmic phase geometry, while RE-097 proves that ordinary ambient exceptional-set packing cannot create the needed gain.

RE-098--RE-099 analyze a fourth-moment route. The near-resonant four-zero population is strong enough below the Robin window, but a high-shift architecture that pays the zero quartets by total mass has an exact `3/8` floor even under ideal pointwise sample-kernel cancellation. That is a real limitation of the fourth-moment bookkeeping.

RE-100 changes the location of the **actual sparse-host bottleneck**. The deformed-quadratic sample is separated enough in logarithmic phase for a direct trigonometric large sieve. For a zero slab beginning at `sigma`, the second moment gives

`sum_(n~X^(1/2)) |Z_sigma(t_n)|^2 << T N(sigma,T) X^o(1)`.

Combining Markov with current zero-density estimates yields a polynomial saving in bad sampled hosts uniformly through every fixed real-part range

`1/2 <= sigma <= sigma_0 < sigma_*(vartheta)`, where `sigma_*(vartheta)=(6 vartheta-1)/(4 vartheta)`.

For any fixed `1901/5216 < vartheta < 73/200`, this threshold lies above roughly `0.814`; at the limiting Robin endpoint it tends to `119/146=0.815068...`. The critical line is therefore not the sparse-host obstruction: its second-moment bad-host exponent is only `1-2 vartheta`, with abundant room below `1/2`.

This does **not** refute RE-099. RE-100 also shows that the ordinary fourth moment, even when coupled through a large-sieve estimate, reproduces the same `3/8` floor at the critical line, and that the `T^3` four-zero energy scale is combinatorially forced there. The correct interpretation is that the fourth-moment obstruction is method-specific and can be bypassed on the lower strip by using the cheaper statistic actually sufficient for host sparsity.

The live theorem is now sharply localized. Use the second moment below `sigma_*(vartheta)` and re-optimize shifted-quartet/kernel machinery only for

`beta >= sigma_*(vartheta) ~ 0.814--0.815`,

where zero density is already much thinner. Determine whether existing high-beta density/shifted-energy/exponent-pair input overlaps this second-moment range; if not, state the missing weighted theorem only on that tail.

The durable lesson is destination-sensitive moment choice. A fourth moment may expose useful additive structure yet be strictly more expensive than the sparse-host destination requires on most of the strip. The right statistic is the lowest-order one that preserves the target event while still exploiting the source sampling geometry.

**Boundary.** RE-100 does not finish the sparse-host theorem or the Robin frontier. Its second-moment splice stops before `sigma=1`, and the high-beta tail still requires analysis. The `3/8` floor remains valid for the fourth-moment architecture; it is simply no longer a barrier that must be crossed on the whole critical strip.
