---
id: CLUE-prime-flute-variable-corridor-reservoir-weyl-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-279-variable-scalar-schur-reservoirs-can-erase-local-corridor-cut-gain.md
  - research/prime_flute/findings/PF-280-one-sided-frequency-decoupled-schur-transfer-is-reservoir-stable.md
  - research/prime_flute/findings/PF-281-energy-normalized-cross-form-removes-bounded-frequency-coupling-gate.md
  - research/prime_flute/findings/PF-282-energy-normalized-cross-form-is-a-saturated-extension-angle.md
  - research/prime_flute/findings/PF-283-heavy-angle-counting-criterion-for-weak-trace-endpoint.md
  - research/prime_flute/findings/PF-284-two-sided-heavy-angle-counting-sandwich.md
  - research/prime_flute/findings/PF-285-complementary-weak-schatten-extension-strengths-close-the-weak-trace-endpoint-without-angle-decay.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the physical strength-angle budget close the weak-trace endpoint?

## Observation

PF-279 shows that a variable scalar reservoir can erase the favorable isolated cut scale, while PF-280/PF-281 separate that raw obstruction from the physically mixed low/high block and reduce the surviving endpoint to the energy-normalized form `T`. PF-282 then gives the exact physical factorization

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(|R_P|),\quad F_H=f(|R_H|),\quad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where the bounded factors `F_P,F_H` record extension strength and `\Gamma_{PF}=V_P^*V_H` records the relative angle of the low-fed and high-fed extension ranges.

PF-283 isolates a clean sufficient endpoint estimate. For `0<\tau<1`, let

\[
Q_P^\tau=\mathbf1_{[\tau,1]}(F_P),
\qquad
Q_H^\tau=\mathbf1_{[\tau,1]}(F_H),
\qquad
\Gamma_{PF,\tau}=Q_P^\tau\Gamma_{PF}Q_H^\tau.
\]

Then

\[
N_T(4\tau)\le N_{\Gamma_{PF,\tau}}(2\tau),
\]

so

\[
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)<\infty
\]

is sufficient for `T\in\mathcal S_{1,\infty}`.

PF-284 supplies the reverse heavy-sector comparison and shows that failure of this convenient criterion need not be endpoint failure. In the same symmetric scaling,

\[
N_T(4\tau)
\le N_{\Gamma_{PF,\tau}}(2\tau)
\le N_T(2\tau^3),
\]

so weak trace class itself implies only `N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-3})`. The interval between the `\tau^{-1}` sufficient scale and the `\tau^{-3}` necessary scale is genuine.

PF-285 identifies one exact mechanism occupying that interval. If the two strength populations satisfy

\[
\operatorname{rank}Q_P^\tau=O(\tau^{-p}),
\qquad
\operatorname{rank}Q_H^\tau=O(\tau^{-q}),
\qquad
\frac1p+\frac1q\ge1,
\]

then `F_P\in\mathcal S_{p,\infty}`, `F_H\in\mathcal S_{q,\infty}`, and the exact product factorization already gives

\[
T\in\mathcal S_{1,\infty}
\]

for every bounded `\Gamma_{PF}`. In particular, two `O(\tau^{-2})` heavy populations close the endpoint even with maximally aligned extension ranges. PF-285 gives an explicit diagonal model where `N_{\Gamma_\tau}(2\tau)\asymp\tau^{-2}`, so PF-283 fails while `T` is still weak trace class and PF-284's necessary budget remains satisfied.

The physical endpoint is therefore a **joint strength-angle budget**, not an angle-only Weyl problem. The cheapest first test is now the separate low/high strength census. Principal-angle decay is needed only for the reciprocal exponent deficit left after the two outer strength factors are accounted for.

## Research question

For the canonical simultaneous prime-flute pant extension, what are the asymptotic heavy-strength populations

\[
N_{F_P}(\tau)=\operatorname{rank}Q_P^\tau,
\qquad
N_{F_H}(\tau)=\operatorname{rank}Q_H^\tau,
\]

and do their effective weak-Schatten exponents already satisfy the PF-285 closure condition

\[
\frac1{p_P}+\frac1{p_H}\ge1?
\]

If yes, close the endpoint directly through PF-285 without demanding any angle decay. If not, quantify the residual reciprocal deficit

\[
\delta
=1-\frac1{p_P}-\frac1{p_H}>0
\]

and determine whether the physical extension angle supplies that deficit. A global weak-Schatten angle law with `1/r\ge\delta` is sufficient, but the thresholded PF-283/PF-284 counts may close the endpoint under weaker, strength-dependent angular information.

If the strong PF-283 law

\[
N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-1})
\]

fails, determine whether the resulting growth is merely intermediate and compensated by the two strength factors, or whether the canonical geometry actually violates the necessary PF-284 budget. In symmetric form a genuine obstruction requires

\[
\sup_{0<\tau<\tau_0}
\tau^3N_{\Gamma_{PF,\tau}}(2\tau)=\infty.
\]

More generally, seek physically adapted thresholds `\alpha_k,\beta_k,a_k` for which

\[
\alpha_k\beta_k a_k\,
N_{\Gamma_{PF,\alpha_k,\beta_k}}(a_k)
\]

can be proved uniformly bounded or forced to diverge.

## Why it may matter

PF-281 shows that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-285 materially lowers the cost of the next geometric theorem: a balanced low/high strength census can close the endpoint before any principal-angle theorem is attempted.

This also prevents a false negative. A `\tau^{-2}` heavy-angle count would violate PF-283's convenient sufficient law, but PF-285 proves that exactly such a count can coexist with the endpoint when both strength factors are weak Hilbert--Schmidt. The geometry must therefore be classified by how **strength and angle share the singular-value budget**, rather than by one symmetric angle count in isolation.

The asymmetric PF-284 test remains essential because the physical low-fed and high-fed populations need not have comparable scales. Once their separate exponents are known, the amount of angular decay still required becomes quantitative rather than qualitative.

## Decisive test

Construct the actual simultaneous pant-extension realization of

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

with the physical `P/H` projectors fixed before any simplifying coordinate change. Form `R_P,R_H`, their bounded strength factors `F_P,F_H`, and the angle `\Gamma_{PF}=V_P^*V_H`.

**First**, derive corridor-dependent counting laws for `Q_P^\tau,Q_H^\tau` separately. If

\[
\operatorname{rank}Q_P^\tau=O(\tau^{-p_P}),
\qquad
\operatorname{rank}Q_H^\tau=O(\tau^{-p_H})
\]

with `1/p_P+1/p_H\ge1`, PF-285 closes the endpoint and no angle estimate is required.

**Only if a positive deficit remains**, estimate the actual singular-value count of `\Gamma_{PF,\alpha,\beta}` rather than replacing it by rank alone. Use the deficit to set the target strength of the angular theorem, while retaining PF-283's thresholded sufficient route and PF-284's weighted necessary obstruction test.

Classify the resulting geometry into four regimes: strength-only closure via PF-285; combined strength-angle closure; intermediate growth that defeats one sufficient estimate but remains endpoint-compatible; or a canonical weighted PF-284 divergence that genuinely rules out `T\in\mathcal S_{1,\infty}`.

Retain the physical split throughout. Scalar same-mode reservoirs, raw high/high multiplicity, fixed-threshold compactness, and a convenient coordinate-mode split do not decide the physical strength-angle budget.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization. PF-283 establishes the `O(\tau^{-1})` symmetric heavy-angle count as a sufficient endpoint criterion. PF-284 establishes the reverse heavy-sector comparison and the necessary weighted budget. PF-285 establishes a separate population-only sufficient route and proves abstractly that the PF-283 criterion can fail even while `T` is weak trace class.

No current result estimates `N_{F_P}(\tau)` or `N_{F_H}(\tau)` for the canonical simultaneous prime-flute extension, proves a physical complementary-exponent law, proves the strong heavy-angle Weyl law, or constructs a physical sequence violating the necessary PF-284 budget. The diagonal PF-285 model is an abstract falsifier for overinterpreting the PF-283 criterion, not a model of the canonical prime-flute spectrum. No wave-operator, trace-formula, prime/clone separation, or RH consequence follows yet.

## Research disposition

The clue remains `accepted`. The first live target is now the physical low/high **strength-population census**. If the two exponents close the reciprocal budget, use PF-285 immediately. Otherwise carry only the residual deficit into the angle problem and use PF-283/PF-284 to distinguish sufficient closure, intermediate route failure, and a genuine endpoint obstruction.