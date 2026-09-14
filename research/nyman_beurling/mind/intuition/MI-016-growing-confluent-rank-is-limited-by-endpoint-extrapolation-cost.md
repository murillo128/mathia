# MI-016 — Growing confluent rank is limited by endpoint extrapolation cost, not monomial conditioning

**Evidence level:** exact growing-rank target-poorness reduction from [NB-109](../../findings/NB-109-near-logarithmic-confluent-rank-remains-target-poor-after-full-backfill.md), extending NB-108. No theorem is claimed for arbitrary zero multiplicity or for several-distinct-zero state spaces.

For one hypothetical off-critical zero at height `G`, let `S^(d)` be the span of its first `d` confluent derivative states after complete early-cell backfill. NB-109 replaces the badly conditioned monomial Gram matrix by the polynomial function represented by the packet and obtains the intrinsic estimate

`delta^2 = ||P_(S^(d)) e||^2 / ||e||^2 << G^(-1) [C_L(1+A)]^(2d)`,

where `A=2a log(m/r)` is the radial distance from the resolved terminal band back to the fixed target endpoint. Thus `d log(2+A)=o(log G)` already forces `delta->0`; without further scale information, every

`d <= (1/2-epsilon) log G / log log G`

packet remains target-poor.

The mechanism is **polynomial extrapolation**, not coordinate conditioning. On a fixed terminal radial interval the packet norm controls the `L^2` norm of its polynomial state, while the fully backfilled target sees only endpoint jets obtained by exact integration by parts. Reaching the remote target endpoint costs roughly `(1+A)^d`; whitening or changing the derivative basis cannot remove that cost.

Chebyshev polynomials give the matched control: exterior endpoint values really can grow exponentially like `[c(1+A)]^d` while the interior `L^2` norm stays moderate. So the growing-rank loss is geometric information about extrapolating the state function, not an artifact of the smallest eigenvalue of a monomial moment matrix.

Once the whole packet has vanishing principal angle to the target, NB-108's leverage-target Pareto law remains dimension-free: `sup_(eta>=theta) chi = 1-theta+o(1)`. Near-logarithmically many confluent directions therefore do not create a hidden high-leverage/high-target channel.

**Boundary.** This does not close all multiplicity growth. Classical unconditional zero-multiplicity bounds allow `O(log G)`, larger than the rate-free `log G/log log G` window. The remaining one-zero route must enter the transition where endpoint extrapolation can compete with terminal coercivity, use source-specific multiplicity information, or move to genuinely multi-zero growing-rank geometry.
