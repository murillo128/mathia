# MI-008 — Exact separation, stable degree, scalar sample count, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, and propagation models through AF-284 and PF-300; no common universal condition number is claimed.

Dirichlet acquisition already separates phase fibers from coupling. AF-279 classifies one regular vertical lattice; AF-280 shows that several **separate** resonant marginals can lose mixed interactions even when their phase-label tuple is injective; AF-281 shows that complete mixed samples recover the joint torus law when the common resonance intersection is trivial.

AF-282 prices finite-prefix label geometry for the concrete cadences `2pi/log2` and `2pi/log3`: the joint phase nodes of `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 then prices coefficient stability itself: coordinatewise mixed degree has sharp scale `L=Theta(N)`. AF-284 shows that this does not force quadratic acquisition. Classical row sparsification extracts an **unweighted subset of distinct raw mixed moments of size `O(N log N)`** from the dense stable frame while retaining a breadth-uniform least-squares inverse under per-sample adversarial noise.

The finite-prefix resource ladder is therefore now explicit:

\[
\text{exact joint separation}\;\not\Rightarrow\;\text{stable degree}\;\not\Rightarrow\;\text{sample count}.
\]

For the known-support two-prime channel, the degree bill is `Theta(N)` and the current raw sample-count gap is only `Omega(N)` versus `O(N log N)`. Timing horizon, explicit deterministic design, support knowledge, source weighting, and target norm remain independent costs.

Prime Flute supplies an analogous distinction for repeated local maps. PF-297 shows that finite-section Robin contraction is truncation leakage and the complete positive map preserves `q`-mass. PF-298 gives scalar pant transmission `1-O(s_n)`. PF-299 identifies the seam sequence as the `ell^1` endpoint, and PF-300 sharpens that endpoint into an intrinsic quadrature law. For decreasing `phi`, `sum s_n phi(F(p_n))` converges exactly when `int phi(t)dt` does; in particular the loss scale

\[
s_n(\log p_n)^{-\beta}
\]

is nonsummable for `\beta<=1` and summable for `\beta>1`.

So even `o(s_n)` local loss is not enough to predict global transmission: a slowly varying factor can decide the infinite product. Stable recovery and repeated propagation share the same methodological warning without sharing one numerical condition number: **price the exact resource that the downstream operation consumes**.

**Boundary.** AF-284 is existential and known-support; PF-300 concerns the scalar monotone-weight accumulation channel. Neither result transfers automatically to unknown support, arbitrary timing errors, oscillatory flute weights, or the complete mixed-response operator.