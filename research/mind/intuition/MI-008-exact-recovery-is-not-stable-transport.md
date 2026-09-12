# MI-008 — Exact recovery, timing provenance, and accumulated local loss are different resources

**Evidence level:** supported by the specified inverse, sampling, timing, and propagation models through AF-286 and PF-301; no common universal condition number or transport theorem is claimed.

Dirichlet acquisition already separates phase fibers from coupling. AF-279 classifies one regular vertical lattice; AF-280 shows that several **separate** resonant marginals can lose mixed interactions even when their phase-label tuple is injective; AF-281 shows that complete mixed samples recover the joint torus law when the common resonance intersection is trivial.

AF-282 prices finite-prefix label geometry for the concrete cadences `2pi/log2` and `2pi/log3`: the joint phase nodes of `1,...,N` have minimum spacing `Theta(1/N)`. AF-283 prices coefficient stability itself: coordinatewise mixed degree has sharp scale `L=Theta(N)`. AF-284--AF-285 then show that linear degree does not force quadratic acquisition. Deterministic subset selection gives an **unweighted subset of at most `8N` distinct raw mixed moments** with a breadth-uniform least-squares inverse under samplewise adversarial noise, while rank requires at least `N` complex observations. Hence

\[
q_{\mathrm{stable,raw}}(N)=\Theta(N).
\]

AF-286 adds a different resource that cannot be read off from this frame conditioning. A common clock-origin error factors exactly as

\[
\widetilde y=A D_\tau b,
\qquad D_\tau=\operatorname{diag}(n^{-i\tau}),
\]

so the nominal decoder returns `D_tau b` exactly. On the arbitrary-complex source class, clock origin and coefficient phase are a gauge pair. The exact worst-case relative displacement begins as `R_N(T)=2\sin(T\log N/2)` and fixed distortion has the sharp calibration scale `T=Theta(1/log N)`, only `Theta(log log N)` fractional clock bits in a fixed time unit. This cost is a **provenance/symmetry bill**, not a sample-count or condition-number bill. More samples do not remove a gauge; an external marking, source restriction, or gauge-invariant downstream target does.

Independent rowwise timing jitter belongs to another class. AF-286 currently gives a sufficient uniform relative scale `O(1/(sqrt(N) log N))`, while the common-offset subclass leaves only an `O(1/log N)` necessary obstruction. The `sqrt(N)` gap is therefore a derivative-frame/jitter-geometry question rather than evidence that clock precision generically scales like the stronger bound.

Prime Flute supplies a complementary distinction for repeated local maps. PF-297 shows that finite-section Robin contraction is truncation leakage and the complete positive map preserves `q`-mass. PF-298 gives scalar relative killing `r_n=O(s_n)`, and PF-299 identifies the seam sequence as the critical accumulation currency. PF-300 first converts monotone slowly varying losses into an intrinsic integral; PF-301 removes that regularity requirement entirely. With arbitrary bounded nonnegative

\[
b_n=\frac{r_n}{s_n}
\]

and intrinsic hat functions `\psi_n` satisfying `\int\psi_n=s_n`, the piecewise-linear density `B_N=\sum b_n\psi_n` obeys

\[
\int B_N=\sum r_n,
\]

and the scalar transmission product survives exactly when `B_N\in L^1`. Up to one finite positive renormalization it is `exp(-\int B_N)` asymptotically. Prime-gap-correlated oscillation is therefore not a separate accumulation loophole; the unresolved scalar quantity is the total intrinsic mass of the actual attenuation density.

The cross-line lesson is not a universal stability formula. **Classify the error or loss by its structural action before assigning a resource budget.** A common-mode acquisition error may be an exact source symmetry and should be quotiented or marked. Independent perturbations require a frame/derivative estimate. Repeated local transmission losses require an intrinsic accumulated-mass law, and once the correct measure is identified even arbitrary coefficient oscillation may become exactly integrable. Similar-looking “small errors” can therefore demand fundamentally different repairs.

**Boundary.** AF-286 is finite known-support and its gauge statement assumes arbitrary complex coefficients; constrained sources may fix the clock. PF-301 concerns the scalar pant channel and does not prove the complete `P/H` return factors through that channel. Neither conclusion transfers automatically to a different measurement, target norm, or mixed-response category.