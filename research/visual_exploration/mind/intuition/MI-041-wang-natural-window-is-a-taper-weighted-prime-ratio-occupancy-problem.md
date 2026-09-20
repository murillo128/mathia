# MI-041 — Wang's surviving prime source is exactly a differential image of the theta remainder and must survive derivative repayment

**Evidence level:** exact/literature-backed synthesis from VIS-313--[VIS-339](../../findings/VIS-339-wang-prime-source-chebyshev-theta-differential-image.md). No improved prime-number-theorem remainder, arithmetic frequency migration, or RH consequence is claimed.

VIS-330--VIS-334 classify the fixed-source transform: no real log-frequency is annihilated, high frequencies are attenuated by one order, and exact inversion charges one derivative plus memory. VIS-335--VIS-336 show that this derivative tax is sharp generically, including on one increasing-frequency trajectory.

VIS-337 tests the actual squared-von-Mangoldt source. Distributionally, for `F(u)=e^(-u)E_A(e^u)` one has `(1+D)F=mu-u du`, and Wang's output satisfies `(4-D^2)Q=4(mu-u du)`. Every prime-power jump is copied exactly into the derivative channel. VIS-338 then removes the higher-prime-power branch collectively: the complete `k>=2` source, its Green response, one-sided derivatives and far-tail jump mass are `O(U^2 e^(-U/2))`, exponentially below every fixed Korobov--Vinogradov subexponential envelope.

VIS-339 identifies the remaining prime-only carrier rather than merely narrowing it. With
`G(u)=e^(-u)theta(e^u)-1`
and
`nu_prime=mu_prime-u du`,
one has the exact distributional identity
`nu_prime=u(1+D)G`.
Hence every compactly supported smooth packet satisfies
`int phi d nu_prime = int [(u-1)phi-u phi']G du`,
and conversely `G` is recoverable from `nu_prime` after one boundary value. The centered prime source and the normalized theta remainder are therefore equivalent representations for this linear Wang channel, not independent sources of structure.

This changes what can count as evidence for a packet mechanism. A visually or spectrally attractive organization of prime atoms is not new leverage unless, after the exact translation above, it becomes a nontrivial quantitative property of `G` at the live envelope scale. If such a property exists, Wang's nonvanishing filter may still redistribute it between `Q` and `Q'`; usefulness at the destination requires the complete downstream decomposition to consume the smaller `Q` without reconstructing the larger source scale through the derivative channel.

**Boundary.** VIS-339 does not prove cancellation or a new bound for `G`; nonlinear properties of the prime configuration are not declared trivial merely because this linear source channel is invertible. The result says that smooth linear packet statistics entering Wang through `nu_prime` must first be quotient-tested as theta-remainder functionals.
