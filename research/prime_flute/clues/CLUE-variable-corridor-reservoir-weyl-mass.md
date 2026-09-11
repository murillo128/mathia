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
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Does the heavy extension-angle count obey the weak-trace Weyl law?

## Observation

PF-279 shows that a variable scalar reservoir can erase the favorable isolated cut scale, while PF-280/PF-281 separate that raw obstruction from the physically mixed low/high block and reduce the surviving endpoint to the energy-normalized form `T`. PF-282 then gives the exact physical factorization

\[
T=F_P\Gamma_{PF}F_H,
\qquad
F_P=f(|R_P|),\quad F_H=f(|R_H|),\quad
f(t)=\frac{t}{\sqrt{1+t^2}},
\]

where the bounded factors `F_P,F_H` record extension strength and `\Gamma_{PF}=V_P^*V_H` records the relative angle of the low-fed and high-fed extension ranges.

PF-283 sharpens the remaining weak-trace problem to one scale-coupled count. For `0<\tau<1`, let

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

so the concrete sufficient endpoint estimate is

\[
\boxed{
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)<\infty.}
\]

This is weaker than demanding `\Gamma_{PF}\in\mathcal S_{1,\infty}` and more precise than separately asking for “uniform heavy-channel decay” plus an unspecified weak-strength population estimate. It allows the two mechanisms to trade exactly at the scale relevant to `T`.

## Research question

For the canonical simultaneous prime-flute pant extension, does the physical heavy-angle compression satisfy

\[
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)=O(1)
\qquad(\tau\downarrow0)?
\]

Can this be proved from a Weyl/counting law for the heavy extension-strength populations alone,

\[
\min\{\operatorname{rank}Q_P^\tau,
       \operatorname{rank}Q_H^\tau\}
=O(\tau^{-1}),
\]

or, if those populations are denser, does the actual one-cusp-pant geometry force enough principal-angle decay that only `O(\tau^{-1})` singular directions of `\Gamma_{PF,\tau}` remain above scale `2\tau`?

A useful negative result should likewise be physical and quantitative: exhibit a canonical sequence `\tau_k\downarrow0` on which the heavy extension reservoir retains too many low/high overlap directions above the matching angular scale.

## Why it may matter

PF-281 shows that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-283 shows that the displayed heavy-angle counting law is sufficient for exactly that endpoint. The remaining question is therefore no longer an abstract choice of operator ideal: it is a concrete geometric/spectral Weyl problem for the simultaneous pant-extension ranges.

This also gives a diagnostic split. If heavy-strength population is already `O(\tau^{-1})`, no additional angular theorem is needed. If it grows faster, the exact amount of missing cancellation is visible in the singular-value count of `\Gamma_{PF,\tau}` rather than hidden in an unnormalized reservoir norm.

## Decisive test

Construct the actual simultaneous pant-extension realization of

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

with the physical `P/H` projectors fixed before any simplifying coordinate change. Form `R_P,R_H`, their bounded strength factors `F_P,F_H`, and the angle `\Gamma_{PF}=V_P^*V_H`.

First derive a corridor-dependent counting law for the spectral projections `Q_P^\tau,Q_H^\tau`. If their smaller rank is `O(\tau^{-1})`, PF-283 already proves the endpoint. Otherwise estimate the singular-value counting function of the heavy angle directly and test

\[
N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-1}).
\]

Retain the physical split throughout. Scalar same-mode reservoirs, raw high/high multiplicity, and fixed-threshold compactness do not decide this scale-coupled endpoint count.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization and fixed-threshold ideal equivalence. PF-283 establishes only the **sufficient reduction** from the desired weak-trace endpoint to the scale-coupled heavy-angle count above.

No current result proves the required `O(\tau^{-1})` count for the canonical prime flute, proves a heavy-population Weyl law, or constructs a physical sequence violating it. Failure of this sufficient criterion would not by itself prove `T\notin\mathcal S_{1,\infty}`. No wave-operator, trace-formula, prime/clone separation, or RH consequence follows yet.

## Research disposition

The clue remains `accepted`. Its live target is now precise: prove or refute the scale-coupled heavy-angle Weyl estimate `\tau N_{\Gamma_{PF,\tau}}(2\tau)=O(1)` from the complete one-cusp-pant extension geometry.