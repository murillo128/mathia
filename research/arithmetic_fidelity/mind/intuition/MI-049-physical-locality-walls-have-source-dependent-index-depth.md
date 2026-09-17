# MI-049 — Physical locality walls have source-dependent index depth and exceptional-set transfer costs

**Evidence level:** exact synthesis from [AF-395](../../findings/AF-395-fixed-successor-radius-misses-disconnected-curvature-on-prime-log-meshes.md) through [AF-402](../../findings/AF-402-exceptional-set-inertia-transfers-short-interval-pnt-to-density-one-prime-starts.md). The locality conversions and exceptional-set transfer are exact in their stated regimes; no detector theorem is transferred between source families.

A locality threshold should first be stated in the source's intrinsic physical coordinate and only then converted into a combinatorial index budget. For an increasing regularly varying source scale `a_N` of index `rho>0`, fixed logarithmic reach `h` costs

`B_N(h)/N -> exp(h/rho)-1`.

For shrinking reach `h_N->0`, regular variation alone is insufficient: AF-400 constructs smooth counterexamples where `B_N(h_N)/(N h_N)` oscillates. A same-scale local density law is needed. Under `x f'(x)/f(x)->rho` and `N h_N->infinity`, one recovers `B_N(h_N)~N h_N/rho`.

For primes, AF-401 gives the all-start version from uniform primes-in-short-interval control. If `h_N=p_N^(-beta)` with `beta<13/30`, then

`B_N(h_N) ~ N h_N`

for every sufficiently large prime index. AF-402 shows that an almost-all ambient theorem can reach substantially thinner physical walls, but only after paying a separate sparse-sampling transfer. A failure of a short-interval PNT persists over a macroscopic interval of nearby starts; Brun--Titchmarsh then bounds how many prime starts can lie inside those persistence regions. Combining this inertia with the ambient exceptional-set estimate transfers the theorem to **relative density one of prime starts**. With the current almost-all short-interval input, this yields

`B_N(p_N^(-beta)) ~ N p_N^(-beta)`

for relative density one of prime indices whenever `beta<13/15`.

The reusable rule is therefore three-stage. **Define the physical relation first; obtain source-density control at that same physical scale; and, if the source is sampled on a sparse subset, prove that ambient exceptional sets cannot concentrate on the sampled starts.** Successor count is not an intrinsic locality resource, and an almost-everywhere theorem in the ambient coordinate does not automatically become an almost-everywhere theorem on primes.

This separates two different theorem currencies. Uniform short-interval control buys an all-start statement but currently only down to the AF-401 scale. Stronger almost-all control buys a thinner density-one statement after the AF-402 inertia/packing transfer. The exponents `13/30` and `13/15` therefore measure present source-density technology and sampling mode, not intrinsic `PF_3` locality constants.

**Boundary.** AF-402 does not give all-prime-start control below the AF-401 range, does not claim either exponent sharp, and does not supply a shrinking `PF_3` detector wall. Exceptional-set inertia must be proved for the actual source theorem and sampling set; density-one transfer is not formal. The remaining arithmetic question is whether a proposed source-native detector requires all starts, only density-one starts, or another exceptional-set geometry, and whether its physical wall lies inside the corresponding source theorem.