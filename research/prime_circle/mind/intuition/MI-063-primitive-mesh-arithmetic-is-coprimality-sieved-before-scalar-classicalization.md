# MI-063 — Primitive mesh arithmetic has a threshold but the scalar branch classicalizes throughout

**Evidence level:** exact/asymptotic synthesis from [PC-386](../../findings/PC-386-supercritical-primitive-mesh-chords-are-coprimality-sieved.md) and [PC-387](../../findings/PC-387-critical-and-subcritical-primitive-mesh-chords-lose-leading-sieve-data.md), refining the full-root universality of PC-384--PC-385. Exact-order Möbius extraction, Ramanujan sums, endpoint Riemann-sum asymptotics, Jordan totients and finite Euler products are classical; the line-specific content is the completed primitive-shell mesh phase boundary.

Restricting a root fiber to points of exact order changes the conclusion of the full-fiber scalar analysis. The primitive observable is exactly the Möbius extraction of the full-root observable, equivalently a Ramanujan-sum filter in Fourier space. Arithmetic can therefore re-enter at mesh scale even though the corresponding full-root positive scalar pushforward is universal.

For fixed inverse-power exponent `alpha>1/2` and mesh regularization `eta=tau/m`, every degree sequence has subsequences on which the divisibility status of each fixed prime stabilizes. Along such a subsequence, `m^(-2 alpha) S_m(alpha,tau/m)` converges to a one-dimensional lattice kernel with exactly those stabilized prime divisors sieved out. Prime and primorial degrees can have different limits, but the entire source dependence is the limiting coprimality sieve. At `alpha=1`, zero cutoff gives `S_m(1,0)=J_2(m)/12` and `S_m(1,0)/phi(m)=psi(m)/12`, so the familiar primorial RH threshold is the classical Dedekind-psi criterion.

PC-387 closes the other side of the threshold. For `0<=alpha<1/2`, the primitive average normalized by `phi(m)` converges to the same continuum integral for every degree sequence: the coprimality mask is asymptotically invisible at leading order. At `alpha=1/2`, the leading law is universally

`S_m(1/2,tau/m) ~ phi(m) log(m) / pi`

for every fixed `tau>=0`. At zero cutoff the first explicit radical-dependent correction is `sum_(p|m) log(p)/(p-1)`, exactly the logarithmic derivative at `s=1` of the finite Euler product `prod_(p|m)(1-p^(-s))`.

Thus the scalar primitive-shell mesh phase diagram is complete. Above the integrability threshold, arithmetic survives only as the classical coprimality sieve; at the threshold, the leading sieve data is washed out and the first explicit correction is finite-Euler-product data; below it, even the leading primitive average is universal. None of these scalar regimes supplies a new complex spectral parameter or an intrinsic critical-line selector.

**Boundary.** The classification concerns scalar primitive-shell common-anchor inverse-power energies with fixed mesh regularization. It does not rule out phase-sensitive, nonnormal, tensorial, cross-level or other genuinely nonseparable constructions. A viable continuation must retain source information before scalar summation and show that its surviving invariant is not exhausted by Möbius/Ramanujan/Jordan/finite-Euler-product data.