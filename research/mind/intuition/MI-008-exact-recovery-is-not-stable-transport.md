# MI-008 — Exact separation, stable degree, raw sample count, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, and propagation models through AF-285 and PF-300; no common universal condition number is claimed.

Dirichlet acquisition already separates phase fibers from coupling. AF-279 classifies one regular vertical lattice; AF-280 shows that several **separate** resonant marginals can lose mixed interactions even when their phase-label tuple is injective; AF-281 shows that complete mixed samples recover the joint torus law when the common resonance intersection is trivial.

AF-282 prices finite-prefix label geometry for the concrete cadences `2pi/log2` and `2pi/log3`: the joint phase nodes of `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 then prices coefficient stability itself: coordinatewise mixed degree has sharp scale `L=Theta(N)`.

AF-284 shows that linear degree does not force quadratic acquisition. AF-285 closes the remaining logarithmic sample-order gap: deterministic subset selection on the realified stable frame, followed by closure under complete complex samples, gives an **unweighted subset of at most `8N` distinct raw mixed moments** with a breadth-uniform least-squares inverse under samplewise adversarial noise. Since injectivity on `C^N` requires at least `N` complex observations,

\[
q_{\mathrm{stable,raw}}(N)=\Theta(N).
\]

The finite-prefix resource ladder is therefore explicit even though two costs share the same order. Exact joint separation is a fiber statement; `Theta(N)` mixed degree is a resolution/horizon statement; `Theta(N)` raw sample count is a rank/frame-selection statement. Equality of asymptotic order does not make them the same resource. Explicit sampling geometry, maximal time horizon, timing precision, support knowledge, source weighting, target norm, and infinite-source conditioning remain independent.

Prime Flute supplies an analogous distinction for repeated local maps. PF-297 shows that finite-section Robin contraction is truncation leakage and the complete positive map preserves `q`-mass. PF-298 gives scalar pant transmission `1-O(s_n)`. PF-299 identifies the seam sequence as the `ell^1` endpoint, and PF-300 sharpens that endpoint into an intrinsic quadrature law. For decreasing `phi`, `sum s_n phi(F(p_n))` converges exactly when `int phi(t)dt` does; in particular the loss scale

\[
s_n(\log p_n)^{-\beta}
\]

is nonsummable for `\beta<=1` and summable for `\beta>1`.

So neither a linear stable inverse nor an `o(s_n)` local loss determines the downstream global result by itself. **Price the exact resource consumed by the next operation**: observation geometry for inversion, slowly varying accumulation for propagation.

**Boundary.** AF-285 is finite known-support and does not solve timing/unknown-support/infinite-source stability; PF-300 concerns the scalar monotone-weight accumulation channel. Neither conclusion transfers automatically to a different measurement or mixed-response category.