# MI-042 — Every fixed subfull response density can remain signed-noncoercive

**Evidence level:** exact source-specific synthesis from [FD-240](../../findings/FD-240-every-subfull-point-sampling-density-retains-a-macroscopic-signed-nullspace.md), extending FD-238--FD-239. This concerns unrestricted signed profiles under the stated coefficient envelope; it does not transfer to the physical nonnegative/source-coherent class without a separate transversality theorem.

Let `S` be any prescribed set of point samples of the divisor response and let `eta` be its upper sampling density on dyadic octaves. FD-240 removes the earlier low-density threshold completely: for every

`eta<1`,

there are integer signed coefficients `|b_n|<=n` whose divisor response vanishes at every point of `S` and every dyadic endpoint, remains `O(m)` between samples, and still carries a positive fraction of the available linear coefficient capacity in each sign.

The mechanism is local pairwise reset rather than a sparse-grid accident. Writing `b=1*g` makes the response the partial sum of `g`. Pairing consecutive integers inside every sample cell makes each pair contribute zero net response, so the prescribed zeros are exact. The unsampled fraction supplies linearly many disjoint pairs, and a reciprocal-totient estimate forces their aggregate amplitude to remain quadratic on each octave. The surviving capacity is quantitatively positive for every fixed missing fraction.

Thus **point-sampling density has no signed-coercivity threshold strictly below full density** in this model. Adding a larger but fixed fraction of scalar response coordinates cannot by itself remove the macroscopic signed nullspace. The first unresolved point-sampling endpoint is density one with a nonempty omitted set, where the geometry of the omissions rather than a fixed density deficit must matter.

This separates observation richness from source admissibility. A viable Farey argument must either use near-full/density-one response structure strong enough to control the omitted set, use a genuinely non-pointwise observable, or prove that positivity/capacity/arithmetic coherence makes the physical source quantitatively transverse to the signed nullspace. The response samples alone do not provide that transversality.

**Boundary.** Full all-integer response is injective, so FD-240 does not say every proper sampling set fails. It does not classify density-one omissions, nonlinear measurements, or physical nonnegative corrections. The exact conclusion is only that every prescribed sampling pattern whose octave density stays bounded away from one admits a macroscopic signed countermodel.