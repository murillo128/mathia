# MI-008 — Exact separation, joint coupling, label resolution, coefficient stability, and local contraction are different losses

**Evidence level:** supported by the specified inverse, sampling, and propagation models; no common universal condition number is claimed.

For finite Blaschke inversion, AF-178 gives a local inverse constant controlled by zero separation: exact recovery survives while conditioning diverges as zeros collide. This is a local metric statement, not a generic source-recovery law.

Dirichlet acquisition separates several different losses. AF-279 shows that one regular vertical lattice first quotients frequencies through `lambda -> e^{-ih lambda}`. AF-280 shows that finitely many **separate** lattice marginals cannot repair several individually resonant quotients on the unrestricted weighted `ell^1` source class: a mixed interaction can lie in every marginal kernel even when the tuple of phase labels is injective.

AF-281 shows what genuine joint coupling changes. Complete mixed samples `F(c+i(k\cdot h))` are the Fourier coefficients of the joint torus pushforward, so ordinary Dirichlet coefficient fidelity is equivalent to

\[
\bigcap_jR_{h_j}=\{1\}.
\]

If all individual cadences resonate, a strict repair requires their generated time subgroup to be dense rather than one discrete lattice. Exact repair therefore pays unbounded mixed integer-combination complexity, and every fixed mixed-index box still has remote near-aliases on an unrestricted infinite source.

AF-282 isolates a narrower finite-prefix bill for the concrete joint cadences `2\pi/\log2` and `2\pi/\log3`. The joint phase nodes of `1,\ldots,N` have minimum coordinatewise chord separation

\[
\delta_N=\Theta(N^{-1}),
\]

with explicit upper and lower constants. Thus direct source-label discrimination needs only inverse-breadth phase accuracy (`O(\log N)` bits of absolute resolution), not exponentially fine phase resolution. Any substantially worse finite-prefix instability must come from mixed-mode degree, collective interpolation geometry, coefficient inversion, the noise/observation model, or a broader source class. Pairwise label separation is not a Vandermonde singular-value theorem.

Prime Flute supplies a separate composition warning. PF-297 shows that finite-section Robin contraction is truncation leakage: the norms tend to one and the complete positive map preserves `q`-mass. PF-298 shows that the neighboring pant's lowest constant channel is likewise nearly conservative, with transmission `1-O(s_n)`. Local strictness or coercivity therefore does not supply a depth-uniform return gap.

The common lesson is not merely that “conditioning matters,” but that the relevant loss must be attached to the actual map. Source breadth can create phase fibers; acquisition can discard cross-channel coupling; finite labels can approach at a known `1/N` scale; coefficient recovery can be much worse than pairwise separation; and repeated propagation can lose a uniform gap even when every finite stage contracts. These are different quantities and none can substitute for another without an explicit comparison theorem.
