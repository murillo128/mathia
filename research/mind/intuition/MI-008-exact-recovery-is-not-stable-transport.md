# MI-008 — Exact separation, stable degree, scalar sample count, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, and propagation models through AF-283 and PF-299; no common universal condition number is claimed.

Dirichlet acquisition already separates phase fibers from coupling. AF-279 classifies one regular vertical lattice; AF-280 shows that several **separate** resonant marginals can lose mixed interactions even when their phase-label tuple is injective; AF-281 shows that complete mixed samples recover the joint torus law when the common resonance intersection is trivial.

AF-282 prices finite-prefix label geometry for the concrete cadences `2pi/log2` and `2pi/log3`: the joint phase nodes of `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 then prices coefficient stability itself. On the known prefix, coordinatewise mixed degree has the sharp scale

\[
L=\Theta(N).
\]

A two-point lower bound makes `L=o(N)` uniformly unstable, while the dense square with `L=30N` has a breadth-uniform least-squares inverse under per-sample absolute noise. Thus pairwise spacing did not hide an exponential Vandermonde barrier in the **degree** resource.

But stable degree is not observation complexity. The proved design uses `Theta(N^2)` scalar mixed moments and only the elementary `Omega(N)` rank lower bound is known. Sparse sample design, timing precision, support knowledge, source weighting, and the target coefficient norm remain separate bills. Exact injectivity, inverse-breadth labels, and linear stable degree do not imply near-linear acquisition.

Prime Flute supplies an analogous distinction for repeated local maps. PF-297 shows that finite-section Robin contraction is truncation leakage and the complete positive map preserves `q`-mass. PF-298 gives scalar pant transmission `1-O(s_n)`. PF-299 then proves

\[
(s_n)\notin\ell^1,
\qquad
(s_n)\in\ell^q\quad(q>1).
\]

So `O(s_n)` is exactly a critical accumulation bound: any fixed superlinear loss law is summable, whereas an eventual linear lower law forces total scalar absorption. A local factor tending to the identity is therefore not enough information; the first-order loss scale matters.

The common structural lesson is map-specific. Source breadth can create aliases; acquisition can discard coupling; stable interpolation can require a known degree; observation count can remain open after conditioning is controlled; and repeated propagation can sit at a sharp summability threshold. Each loss needs its own quantitative theorem rather than being inferred from a neighboring resource.