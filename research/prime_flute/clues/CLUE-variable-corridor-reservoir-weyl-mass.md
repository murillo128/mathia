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
\boxed{
\sup_{0<\tau<\tau_0}
\tau\,N_{\Gamma_{PF,\tau}}(2\tau)<\infty
}
\]

is sufficient for `T\in\mathcal S_{1,\infty}`.

PF-284 now supplies the reverse heavy-sector comparison and changes how a negative geometric result must be interpreted. In the same symmetric scaling,

\[
N_T(4\tau)
\le N_{\Gamma_{PF,\tau}}(2\tau)
\le N_T(2\tau^3).
\]

Hence weak trace class itself implies only

\[
N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-3}).
\]

The interval between the `\tau^{-1}` sufficient scale and the `\tau^{-3}` necessary scale is therefore real. A dense reservoir may defeat the convenient PF-283 Weyl law without yet disproving the endpoint.

PF-284 also permits asymmetric strength thresholds. With

\[
\Gamma_{PF,\alpha,\beta}
=Q_P^\alpha\Gamma_{PF}Q_H^\beta,
\]

weak trace class necessarily bounds

\[
\alpha\beta a\,
N_{\Gamma_{PF,\alpha,\beta}}(a).
\]

This gives the variable-corridor problem both a positive closure target and a genuine falsification target.

## Research question

For the canonical simultaneous prime-flute pant extension, which heavy-angle regime does the physical reservoir geometry enforce?

Can one prove the strong sufficient law

\[
N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-1}),
\]

perhaps first from

\[
\min\{\operatorname{rank}Q_P^\tau,
       \operatorname{rank}Q_H^\tau\}
=O(\tau^{-1}),
\]

or otherwise from principal-angle decay inside a denser heavy population?

If that strong law fails, determine whether the resulting growth is merely intermediate and still compatible with weak trace, or whether the canonical geometry actually violates the necessary PF-284 budget. In symmetric form a true obstruction requires

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

PF-281 shows that `T\in\mathcal S_{1,\infty}` closes the mixed Schur/reciprocal-prime commutator gate. PF-283 gives an efficient sufficient theorem surface, while PF-284 prevents overinterpreting failure of that theorem surface as endpoint failure.

The geometric task is therefore sharper than “prove or refute an `O(\tau^{-1})` count.” It must distinguish three outcomes: a count strong enough to close the endpoint, an intermediate reservoir law that only invalidates the current sufficient route, or a weighted-count violation strong enough to rule out weak trace class itself. The asymmetric PF-284 test is especially relevant because the physical low-fed and high-fed extension-strength populations need not have comparable scales.

## Decisive test

Construct the actual simultaneous pant-extension realization of

\[
K_{PF}=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

with the physical `P/H` projectors fixed before any simplifying coordinate change. Form `R_P,R_H`, their bounded strength factors `F_P,F_H`, and the angle `\Gamma_{PF}=V_P^*V_H`.

First derive corridor-dependent counting laws for the spectral projections `Q_P^\alpha,Q_H^\beta`. If the smaller symmetric heavy rank is `O(\tau^{-1})`, PF-283 already proves the endpoint. Otherwise estimate the actual singular-value count of `\Gamma_{PF,\alpha,\beta}` rather than replacing it by rank alone.

Classify the resulting geometry against both PF-283 and PF-284:

- a bound `N_{\Gamma_{PF,\tau}}(2\tau)=O(\tau^{-1})` proves the sufficient endpoint criterion;
- growth faster than `\tau^{-1}` but still within every necessary weighted PF-284 budget kills only this sufficient route;
- any canonical sequence with `\alpha\beta a\,N_{\Gamma_{PF,\alpha,\beta}}(a)\to\infty` is a genuine obstruction to `T\in\mathcal S_{1,\infty}`.

Retain the physical split throughout. Scalar same-mode reservoirs, raw high/high multiplicity, and fixed-threshold compactness do not decide these scale-coupled counts.

## Evidence boundary

PF-282 establishes the exact strength-angle factorization. PF-283 establishes the `O(\tau^{-1})` symmetric heavy-angle count as a **sufficient** endpoint criterion. PF-284 establishes the reverse heavy-sector comparison and therefore the necessary weighted budget, including the symmetric `O(\tau^{-3})` upper envelope under weak trace class.

No current result proves any of these asymptotic counts for the canonical prime flute, proves a heavy-population Weyl law, or constructs a physical sequence violating the necessary PF-284 budget. Failure of the PF-283 sufficient criterion still does not prove `T\notin\mathcal S_{1,\infty}`. No wave-operator, trace-formula, prime/clone separation, or RH consequence follows yet.

## Research disposition

The clue remains `accepted`. Its live target is now two-sided: use complete one-cusp-pant extension geometry either to obtain a sufficient heavy-angle Weyl estimate closing the endpoint, or to cross the PF-284 necessary weighted-count boundary and thereby obtain a genuine endpoint obstruction. Intermediate growth must be recorded only as failure of the current sufficient route.