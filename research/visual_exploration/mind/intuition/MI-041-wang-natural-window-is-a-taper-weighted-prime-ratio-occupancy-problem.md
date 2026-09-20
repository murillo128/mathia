# MI-041 — Wang's surviving prime source and square-log summatory source are invertible images of the theta remainder

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-340](../../findings/VIS-340-wang-prime-squarelog-partial-summation-invertible.md). No improved prime-number-theorem remainder, arithmetic frequency migration, or RH consequence is claimed.

VIS-330--VIS-334 classify the fixed-source Wang transform: no real log-frequency is annihilated, high frequencies are attenuated by one order, and exact inversion charges one derivative plus memory. VIS-335--VIS-336 show that this derivative tax is sharp generically, including on an increasing-frequency trajectory.

VIS-337 tests the actual squared-von-Mangoldt source. Distributionally, for `F(u)=e^(-u)E_A(e^u)` one has `(1+D)F=mu-u du`, and every prime-power jump is copied exactly into Wang's derivative channel. VIS-338 removes the higher-prime-power branch collectively: the complete `k>=2` source, its Green response, one-sided derivatives and far-tail jump mass are `O(U^2 e^(-U/2))`, exponentially below the live Korobov--Vinogradov envelope.

VIS-339 identifies the remaining centered prime carrier. With `G(u)=e^(-u)theta(e^u)-1` and `nu_prime=mu_prime-u du`, one has the exact distributional identity `nu_prime=u(1+D)G`; every smooth prime packet is therefore an exact functional of `G`, and `G` is recoverable after one boundary value.

VIS-340 closes the parallel summatory representation. If `P(u)` is the normalized prime-only squared-log summatory remainder, then
`P(u)=uG(u)-H(u)+2e^(-u)`,
where `H` is the one-sided exponential average of `G`, and this map has an explicit causal inverse after removing the endpoint term. The full normalized `Lambda^2` summatory remainder differs only by `O(u^2e^(-u/2))` from proper prime powers. On a fixed Korobov--Vinogradov envelope, `H` stays on the same envelope scale; at envelope-saturating heights, `F(u)/(uG(u))->1`.

The source-side lesson is therefore stronger than the packet test alone. Neither atomic prime coordinates, smooth packetization, square-log weighting nor ordinary partial summation supplies an independent arithmetic channel before Wang's actual filter. Both natural descriptions of the surviving source quotient back explicitly to the same normalized theta remainder. A useful mechanism must be a genuine quantitative property of `G` itself—such as nonstationary or scale-migrating structure not equivalent to a stronger PNT remainder—and the complete destination must retain the resulting smaller `Q` without reconstructing the larger source scale through `Q'` or equivalent unsmoothed information.

**Boundary.** VIS-339--VIS-340 classify these linear source representations, not nonlinear statistics of the prime configuration. They do not prove nonstationarity, a new bound for `G`, or destination-level avoidance of derivative repayment. The remaining Wang question begins only after the exact theta/source reparameterizations have been factored out.
